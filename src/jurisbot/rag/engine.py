from __future__ import annotations
"""Motor RAG híbrido para búsqueda semántica en documentos jurídicos.

Combina ChromaDB (dense retrieval) con el LLM para generar respuestas
citadas y verificadas contra las fuentes originales.
"""

import hashlib
from pathlib import Path
from typing import Optional

import chromadb
from chromadb.config import Settings as ChromaSettings
import structlog

from jurisbot.config import settings
from jurisbot.ingestion.chunker import LegalChunk
from jurisbot.nlp.llm_client import LLMClient
from jurisbot.exceptions import EmbeddingError

logger = structlog.get_logger()


# System prompt compacto para RAG (reemplaza el prompt jurídico largo de llm_client)
_RAG_SYSTEM = (
    "Eres un asistente jurídico académico especializado en Derecho chileno. "
    "Responde SOLO con la información de los fragmentos proporcionados. "
    "Cita cada afirmación con [N°] de la fuente. "
    "Si algo no está en las fuentes, indícalo explícitamente. "
    "Responde en español chileno formal. Este análisis es exclusivamente académico."
)


class RAGEngine:
    """Motor RAG para búsqueda y respuesta sobre documentos jurídicos.

    Uso:
        engine = RAGEngine()
        engine.index_chunks(chunks, collection_name="codigo_civil")
        answer = engine.query("¿Qué es la buena fe en los contratos?")
    """

    def __init__(
        self,
        llm_client: Optional[LLMClient] = None,
        chroma_path: Optional[Path] = None,
    ):
        self.llm = llm_client or LLMClient()
        self.chroma_path = chroma_path or settings.chroma_dir

        # Inicializar ChromaDB con embeddings por defecto
        self.chroma_client = chromadb.PersistentClient(
            path=str(self.chroma_path),
            settings=ChromaSettings(anonymized_telemetry=False),
        )
        # Cache de colecciones para evitar round-trips repetidos
        self._col_cache: dict = {}

    def get_or_create_collection(self, name: str) -> chromadb.Collection:
        """Obtiene o crea una colección en ChromaDB.

        Args:
            name: Nombre de la colección (sanitizado automáticamente).

        Returns:
            Colección de ChromaDB.
        """
        # Sanitizar nombre (ChromaDB requiere alfanumérico + guiones)
        safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in name)
        safe_name = safe_name[:63] or "default"  # Max 63 chars

        # Devolver desde caché si ya existe (evita round-trip a ChromaDB)
        if safe_name in self._col_cache:
            return self._col_cache[safe_name]

        col = self.chroma_client.get_or_create_collection(
            name=safe_name,
            metadata={"hnsw:space": "cosine"},
        )
        self._col_cache[safe_name] = col
        return col

    def index_chunks(
        self,
        chunks: list[LegalChunk],
        collection_name: str = "documents",
    ) -> int:
        """Indexa chunks jurídicos en ChromaDB para búsqueda semántica.

        Args:
            chunks: Lista de LegalChunk a indexar.
            collection_name: Nombre de la colección.

        Returns:
            Número de chunks indexados.

        Raises:
            EmbeddingError: Si falla la generación de embeddings.
        """
        if not chunks:
            return 0

        collection = self.get_or_create_collection(collection_name)

        documents = []
        metadatas = []
        ids = []

        for chunk in chunks:
            if not chunk.text.strip():
                continue

            # Generar ID único basado en contenido
            chunk_id = hashlib.md5(chunk.text.encode()).hexdigest()[:16]
            chunk_id = f"{collection_name}_{chunk_id}"

            documents.append(chunk.text)
            metadatas.append({
                "articulo": chunk.articulo or "",
                "capitulo": chunk.capitulo or "",
                "titulo": chunk.titulo or "",
                "libro": chunk.libro or "",
                "norma_fuente": chunk.norma_fuente or "",
                "rama_derecho": chunk.rama_derecho or "",
                "context_path": chunk.context_path,
            })
            ids.append(chunk_id)

        if not documents:
            return 0

        try:
            # ChromaDB genera embeddings automáticamente con su modelo default
            collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids,
            )

            logger.info(
                "chunks_indexed",
                collection=collection_name,
                count=len(documents),
            )
            return len(documents)

        except Exception as e:
            raise EmbeddingError(f"Error indexando chunks: {e}") from e

    def retrieve(
        self,
        question: str,
        collection_name: str = "documents",
        top_k: int = 4,
        filter_metadata: Optional[dict] = None,
    ) -> tuple[str, list[str]]:
        """Fase 1 (rápida): recupera chunks relevantes de ChromaDB.

        Returns:
            (context_str, sources_list) — listo para pasarle al LLM.
            Devuelve ("", []) si no hay documentos o no hay resultados relevantes.
        """
        collection = self.get_or_create_collection(collection_name)

        try:
            count = collection.count()
        except Exception:
            count = 0

        if count == 0:
            return "", []

        where = filter_metadata if filter_metadata else None
        results = collection.query(
            query_texts=[question],
            n_results=min(top_k, count),
            where=where,
            include=["documents", "metadatas", "distances"],
        )

        if not results["documents"] or not results["documents"][0]:
            return "", []

        # Filtrar por relevancia (umbral coseno)
        RELEVANCE_THRESHOLD = 0.75
        filtered = [
            (doc, meta, dist)
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            )
            if dist < RELEVANCE_THRESHOLD
        ]
        if not filtered:
            filtered = list(zip(
                results["documents"][0][:2],
                results["metadatas"][0][:2],
                results["distances"][0][:2],
            ))

        context_parts = []
        sources = []
        for i, (doc, meta, dist) in enumerate(filtered):
            articulo  = meta.get("articulo", "")
            titulo    = meta.get("titulo", "")
            norma     = meta.get("norma_fuente", "")
            context_p = meta.get("context_path", "")
            rama      = meta.get("rama_derecho", "")

            label_parts = []
            if norma:     label_parts.append(norma)
            if articulo:  label_parts.append(articulo)
            if titulo:    label_parts.append(titulo)
            if context_p and context_p not in " ".join(label_parts):
                label_parts.append(context_p)
            source_label = " — ".join(label_parts) if label_parts else f"Sección {i+1}"
            sources.append(f"[{i+1}] {source_label}")

            header = f"═══ FUENTE [{i+1}]"
            if norma:    header += f" | {norma}"
            if articulo: header += f" | {articulo}"
            if rama:     header += f" | {rama}"
            header += f" | {(1-dist)*100:.0f}% relevancia ═══"
            context_parts.append(f"{header}\n{doc}")

        return "\n\n".join(context_parts), sources

    def _build_rag_prompt(self, question: str, context: str, sources: list[str]) -> str:
        """Construye el prompt RAG compacto para el LLM."""
        return (
            f"CONTEXTO JURÍDICO:\n---\n{context}\n---\n\n"
            f"CONSULTA: {question}\n\n"
            f"Responde SOLO basándote en el contexto. "
            f"Cita cada afirmación con [N°]. "
            f"Al final añade:\n📎 **Fuentes:** {'; '.join(sources)}\n"
            f"\n⚠️ *Análisis exclusivamente académico. No constituye asesoría legal profesional.*"
        )

    def query_stream(
        self,
        question: str,
        collection_name: str = "documents",
        top_k: int = 4,
        filter_metadata: Optional[dict] = None,
        max_tokens: int = 1200,
    ):
        """Búsqueda RAG con streaming del LLM — para uso con st.write_stream().

        Yields:
            Fragmentos de texto de la respuesta generada.
        Raises:
            ValueError: si no hay documentos indexados.
        """
        context, sources = self.retrieve(question, collection_name, top_k, filter_metadata)

        if not context:
            yield (
                "No hay documentos indexados todavía. "
                "Sube un documento jurídico primero para poder hacer consultas."
                if self.get_or_create_collection(collection_name).count() == 0
                else "No se encontraron fragmentos relevantes para su consulta."
            )
            return

        prompt = self._build_rag_prompt(question, context, sources)
        yield from self.llm.generate_stream(
            prompt=prompt,
            system=_RAG_SYSTEM,
            max_tokens=max_tokens,
        )

        # Disclaimer legal — se emite al final de cada respuesta RAG
        yield (
            "\n\n---\n"
            "*⚠️ Uso exclusivamente académico. Las obras citadas son propiedad intelectual "
            "de sus respectivos autores. Esta respuesta no constituye asesoría jurídica "
            "profesional ni reproduce el texto original de las fuentes.*"
        )

        logger.info(
            "rag_stream_completed",
            question=question[:100],
            chunks=len(sources),
        )

    def query(
        self,
        question: str,
        collection_name: str = "documents",
        top_k: int = 5,
        filter_metadata: Optional[dict] = None,
    ) -> str:
        """Busca en los documentos indexados y genera respuesta con citas.

        Args:
            question: Pregunta del usuario en lenguaje natural.
            collection_name: Colección donde buscar.
            top_k: Número de chunks a recuperar.
            filter_metadata: Filtros opcionales (rama, norma, etc.).

        Returns:
            Respuesta generada con citas a fuentes.
        """
        collection = self.get_or_create_collection(collection_name)

        # Verificar que hay documentos
        if collection.count() == 0:
            return (
                "No hay documentos indexados todavía. "
                "Sube un documento jurídico primero para poder hacer consultas."
            )

        # Buscar chunks relevantes
        where = filter_metadata if filter_metadata else None
        results = collection.query(
            query_texts=[question],
            n_results=min(top_k, collection.count()),
            where=where,
            include=["documents", "metadatas", "distances"],
        )

        if not results["documents"] or not results["documents"][0]:
            return "No se encontraron fragmentos relevantes para su consulta en el documento cargado."

        # Filtrar chunks por relevancia (distancia coseno < 0.75 = relevante)
        RELEVANCE_THRESHOLD = 0.75
        filtered = [
            (doc, meta, dist)
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            )
            if dist < RELEVANCE_THRESHOLD
        ]

        # Si el filtro elimina todo, usar los 2 mejores igualmente
        if not filtered:
            filtered = list(zip(
                results["documents"][0][:2],
                results["metadatas"][0][:2],
                results["distances"][0][:2],
            ))

        # Construir contexto enriquecido con metadata jurídica (SAC-inspired)
        context_parts = []
        sources = []
        for i, (doc, meta, dist) in enumerate(filtered):
            articulo   = meta.get("articulo", "")
            titulo     = meta.get("titulo", "")
            norma      = meta.get("norma_fuente", "")
            context_p  = meta.get("context_path", "")
            rama       = meta.get("rama_derecho", "")

            # Construir etiqueta de fuente rica
            label_parts = []
            if norma:       label_parts.append(norma)
            if articulo:    label_parts.append(articulo)
            if titulo:      label_parts.append(titulo)
            if context_p and context_p not in " ".join(label_parts):
                label_parts.append(context_p)
            source_label = " — ".join(label_parts) if label_parts else f"Sección {i+1}"
            sources.append(f"[{i+1}] {source_label}")

            # Cabecera enriquecida del chunk (Summary-Augmented)
            header = f"═══ FUENTE [{i+1}]"
            if norma:    header += f" | {norma}"
            if articulo: header += f" | {articulo}"
            if rama:     header += f" | Rama: {rama}"
            header += f" | Relevancia: {(1-dist)*100:.0f}% ═══"
            context_parts.append(f"{header}\n{doc}")

        context = "\n\n".join(context_parts)

        # Prompt de consultoría jurídica con exigencia de citación estricta
        prompt = (
            f"CONSULTA JURÍDICA: {question}\n\n"
            f"INSTRUCCIONES PARA RESPONDER:\n"
            f"1. Responda EXCLUSIVAMENTE basándose en las fuentes numeradas proporcionadas\n"
            f"2. Cite cada afirmación con [N°] de la fuente correspondiente al final de la oración\n"
            f"3. Si la respuesta NO está en las fuentes, diga explícitamente: "
            f"   'Esta información no se encuentra en el documento cargado'\n"
            f"4. Use lenguaje académico jurídico chileno (tratamiento de 'usted')\n"
            f"5. Estructure su respuesta con párrafos claros\n"
            f"6. Al final, agregue una sección '📎 Fuentes consultadas:' con las referencias usadas\n"
            f"7. Termine con el aviso académico\n\n"
            f"NUNCA invente artículos, sentencias ni autores que no estén en las fuentes."
        )

        answer = self.llm.generate(prompt=prompt, context=context)

        # Asegurar que las fuentes aparezcan al final
        if "📎" not in answer and "fuentes consultadas" not in answer.lower():
            answer += "\n\n📎 **Fuentes consultadas:**\n"
            for src in sources:
                answer += f"  {src}\n"

        if "académico" not in answer.lower() and "asesoría" not in answer.lower():
            answer += (
                "\n\n⚠️ *Análisis exclusivamente académico. No constituye "
                "asesoría legal profesional.*"
            )

        logger.info(
            "rag_query_completed",
            question=question[:100],
            chunks_retrieved=len(results["documents"][0]),
        )

        return answer

    def get_collection_stats(self, collection_name: str = "documents") -> dict:
        """Obtiene estadísticas de la colección."""
        try:
            collection = self.get_or_create_collection(collection_name)
            return {
                "nombre": collection_name,
                "documentos_indexados": collection.count(),
            }
        except Exception:
            return {"nombre": collection_name, "documentos_indexados": 0}

    def list_collections(self) -> list[str]:
        """Lista todas las colecciones disponibles."""
        collections = self.chroma_client.list_collections()
        return [c.name for c in collections]

    def delete_collection(self, collection_name: str) -> bool:
        """Elimina una colección."""
        try:
            self.chroma_client.delete_collection(collection_name)
            return True
        except Exception:
            return False
