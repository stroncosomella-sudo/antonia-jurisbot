from __future__ import annotations
"""Chunking jurídico inteligente para legislación chilena.

Segmenta texto jurídico preservando estructura legal:
artículos, incisos, capítulos, títulos, libros.
"""

import re
from dataclasses import dataclass, field
from typing import Optional

import structlog

logger = structlog.get_logger()


@dataclass
class LegalChunk:
    """Fragmento de texto jurídico con contexto estructural completo."""
    text: str
    chunk_id: str = ""
    # Jerarquía normativa
    libro: Optional[str] = None
    titulo: Optional[str] = None
    capitulo: Optional[str] = None
    parrafo: Optional[str] = None
    articulo: Optional[str] = None
    # Metadata
    page: int = 0
    char_offset: int = 0
    norma_fuente: str = ""
    rama_derecho: str = ""
    token_estimate: int = 0

    @property
    def context_path(self) -> str:
        """Ruta jerárquica del chunk (e.g., 'Libro IV > Título XII > Art. 1545')."""
        parts = []
        if self.libro:
            parts.append(f"Libro {self.libro}")
        if self.titulo:
            parts.append(f"Título {self.titulo}")
        if self.capitulo:
            parts.append(f"Capítulo {self.capitulo}")
        if self.articulo:
            parts.append(f"Art. {self.articulo}")
        return " > ".join(parts) if parts else "Sin clasificar"

    def to_dict(self) -> dict:
        return {
            "text": self.text,
            "chunk_id": self.chunk_id,
            "context_path": self.context_path,
            "articulo": self.articulo,
            "capitulo": self.capitulo,
            "titulo": self.titulo,
            "libro": self.libro,
            "norma_fuente": self.norma_fuente,
            "rama_derecho": self.rama_derecho,
            "token_estimate": self.token_estimate,
            "page": self.page,
        }


class LegalChunker:
    """Segmenta texto jurídico chileno en chunks con contexto jerárquico.

    Prioriza cortes en límites de artículos. Si un artículo excede
    max_chunk_size, divide por párrafos/incisos con overlap.
    """

    # Patrones para legislación chilena
    ARTICLE_PATTERN = re.compile(
        r'^(?:Art(?:ículo|\.)\s*(\d+[\w°]*(?:\s*(?:bis|ter|quáter|quinquies|sexies|septies|octies))?))\s*[\.\-°]?\s*',
        re.IGNORECASE | re.MULTILINE
    )
    CHAPTER_PATTERN = re.compile(
        r'^(?:CAP[ÍI]TULO|Capítulo)\s+([IVXLCDM]+|\d+)[\.\-\s:]*(.*)$',
        re.IGNORECASE | re.MULTILINE
    )
    TITLE_PATTERN = re.compile(
        r'^(?:T[ÍI]TULO|Título)\s+([IVXLCDM]+|\d+)[\.\-\s:]*(.*)$',
        re.IGNORECASE | re.MULTILINE
    )
    LIBRO_PATTERN = re.compile(
        r'^(?:LIBRO|Libro)\s+([IVXLCDM]+|\d+)[\.\-\s:]*(.*)$',
        re.IGNORECASE | re.MULTILINE
    )
    TRANSITORY_PATTERN = re.compile(
        r'^(?:DISPOSICI[OÓ]N(?:ES)?\s+TRANSITORIA|Art(?:ículo|\.)\s*transitorio)',
        re.IGNORECASE | re.MULTILINE
    )

    def __init__(self, max_chunk_size: int = 1000, overlap: int = 200):
        self.max_chunk_size = max_chunk_size
        self.overlap = overlap

    def chunk(
        self,
        text: str,
        norma_fuente: str = "",
        rama_derecho: str = "",
    ) -> list[LegalChunk]:
        """Segmenta texto jurídico en chunks inteligentes.

        Args:
            text: Texto completo del documento jurídico.
            norma_fuente: Nombre del cuerpo legal (e.g., "Código Civil").
            rama_derecho: Rama del derecho (e.g., "Civil").

        Returns:
            Lista de LegalChunk con contexto jerárquico.
        """
        if not text.strip():
            return []

        # Fase 1: Detectar estructura jerárquica
        articles = self._split_by_articles(text)

        if not articles:
            # Si no hay artículos detectados, hacer chunking por tamaño
            return self._chunk_by_size(text, norma_fuente, rama_derecho)

        # Fase 2: Crear chunks respetando artículos
        chunks: list[LegalChunk] = []
        current_libro = ""
        current_titulo = ""
        current_capitulo = ""

        for i, article in enumerate(articles):
            art_text = article["text"].strip()
            if not art_text:
                continue

            # Actualizar contexto jerárquico
            libro_match = self.LIBRO_PATTERN.search(art_text)
            titulo_match = self.TITLE_PATTERN.search(art_text)
            chapter_match = self.CHAPTER_PATTERN.search(art_text)

            if libro_match:
                current_libro = libro_match.group(1)
            if titulo_match:
                current_titulo = titulo_match.group(1)
            if chapter_match:
                current_capitulo = chapter_match.group(1)

            # Si el artículo es muy largo, dividir por párrafos
            if len(art_text) > self.max_chunk_size:
                sub_chunks = self._split_long_article(art_text)
                for j, sub_text in enumerate(sub_chunks):
                    chunk = LegalChunk(
                        text=sub_text,
                        chunk_id=f"chunk_{i}_{j}",
                        libro=current_libro or None,
                        titulo=current_titulo or None,
                        capitulo=current_capitulo or None,
                        articulo=article.get("number"),
                        norma_fuente=norma_fuente,
                        rama_derecho=rama_derecho,
                        token_estimate=len(sub_text.split()),
                    )
                    chunks.append(chunk)
            else:
                chunk = LegalChunk(
                    text=art_text,
                    chunk_id=f"chunk_{i}",
                    libro=current_libro or None,
                    titulo=current_titulo or None,
                    capitulo=current_capitulo or None,
                    articulo=article.get("number"),
                    norma_fuente=norma_fuente,
                    rama_derecho=rama_derecho,
                    token_estimate=len(art_text.split()),
                )
                chunks.append(chunk)

        logger.info(
            "text_chunked",
            total_chunks=len(chunks),
            norma=norma_fuente,
            articles_detected=len(articles),
        )
        return chunks

    def _split_by_articles(self, text: str) -> list[dict]:
        """Divide texto en artículos individuales."""
        matches = list(self.ARTICLE_PATTERN.finditer(text))
        if not matches:
            return []

        articles = []
        for i, match in enumerate(matches):
            start = match.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            articles.append({
                "number": match.group(1),
                "text": text[start:end].strip(),
                "start": start,
                "end": end,
            })
        return articles

    def _split_long_article(self, text: str) -> list[str]:
        """Divide un artículo largo por párrafos con overlap."""
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        if len(paragraphs) <= 1:
            paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

        chunks = []
        current = ""
        for para in paragraphs:
            if len(current) + len(para) > self.max_chunk_size and current:
                chunks.append(current.strip())
                # Overlap: mantener último párrafo
                overlap_text = current.split("\n")[-1] if "\n" in current else ""
                current = overlap_text + "\n" + para if overlap_text else para
            else:
                current = current + "\n\n" + para if current else para

        if current.strip():
            chunks.append(current.strip())

        return chunks if chunks else [text]

    def _chunk_by_size(
        self, text: str, norma_fuente: str, rama_derecho: str
    ) -> list[LegalChunk]:
        """Chunking por tamaño para documentos sin estructura de artículos."""
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
        chunks = []
        current = ""

        for para in paragraphs:
            if len(current) + len(para) > self.max_chunk_size and current:
                chunks.append(LegalChunk(
                    text=current.strip(),
                    chunk_id=f"chunk_{len(chunks)}",
                    norma_fuente=norma_fuente,
                    rama_derecho=rama_derecho,
                    token_estimate=len(current.split()),
                ))
                # Overlap
                words = current.split()
                overlap_words = words[-self.overlap // 5:] if len(words) > self.overlap // 5 else []
                current = " ".join(overlap_words) + "\n\n" + para
            else:
                current = current + "\n\n" + para if current else para

        if current.strip():
            chunks.append(LegalChunk(
                text=current.strip(),
                chunk_id=f"chunk_{len(chunks)}",
                norma_fuente=norma_fuente,
                rama_derecho=rama_derecho,
                token_estimate=len(current.split()),
            ))

        return chunks
