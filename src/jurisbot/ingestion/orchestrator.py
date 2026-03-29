"""Orquestador del pipeline completo de ingesta de documentos."""

from pathlib import Path
from dataclasses import dataclass, field

import structlog

from jurisbot.ingestion.detector import SmartFormatDetector, DocumentFormat
from jurisbot.ingestion.extractors.base import ExtractionResult
from jurisbot.ingestion.extractors.pdf_extractor import PDFExtractor
from jurisbot.ingestion.extractors.docx_extractor import DocxExtractor
from jurisbot.ingestion.extractors.txt_extractor import TxtExtractor
from jurisbot.ingestion.chunker import LegalChunker, LegalChunk
from jurisbot.exceptions import UnsupportedFormatError

logger = structlog.get_logger()


@dataclass
class IngestionResult:
    """Resultado completo del pipeline de ingesta."""
    file_name: str
    format: DocumentFormat
    extraction: ExtractionResult
    chunks: list[LegalChunk]
    norma_fuente: str = ""
    rama_derecho: str = ""

    @property
    def summary(self) -> dict:
        return {
            "archivo": self.file_name,
            "formato": self.format.display_name,
            "páginas": self.extraction.pages,
            "caracteres": self.extraction.char_count,
            "palabras": self.extraction.word_count,
            "chunks": len(self.chunks),
            "confianza": f"{self.extraction.confidence_score:.0%}",
            "secciones": len(self.extraction.structured_sections),
            "tablas": len(self.extraction.tables),
            "advertencias": self.extraction.warnings,
        }


class IngestionOrchestrator:
    """Orquesta el pipeline completo: detección → extracción → chunking."""

    def __init__(self, max_chunk_size: int = 1000, chunk_overlap: int = 200):
        self.detector = SmartFormatDetector()
        self.chunker = LegalChunker(max_chunk_size=max_chunk_size, overlap=chunk_overlap)

        # Registro de extractores
        self._extractors = {
            DocumentFormat.PDF_NATIVE: PDFExtractor(),
            DocumentFormat.PDF_HYBRID: PDFExtractor(),
            DocumentFormat.DOCX: DocxExtractor(),
            DocumentFormat.TXT: TxtExtractor(),
            DocumentFormat.RTF: TxtExtractor(),
            DocumentFormat.HTML: TxtExtractor(),
        }

    def ingest(
        self,
        file_path: Path,
        norma_fuente: str = "",
        rama_derecho: str = "",
    ) -> IngestionResult:
        """Ejecuta el pipeline completo de ingesta.

        Args:
            file_path: Ruta al archivo a procesar.
            norma_fuente: Nombre del cuerpo legal (opcional).
            rama_derecho: Rama del derecho (opcional).

        Returns:
            IngestionResult con extracción y chunks.

        Raises:
            UnsupportedFormatError: Si el formato no es soportado.
            ExtractionError: Si falla la extracción.
        """
        logger.info("ingestion_started", file=file_path.name)

        # 1. Detectar formato
        doc_format = self.detector.detect(file_path)
        logger.info("format_detected", format=doc_format.display_name)

        # 2. Obtener extractor
        extractor = self._extractors.get(doc_format)
        if not extractor:
            raise UnsupportedFormatError(
                f"No hay extractor disponible para: {doc_format.display_name}. "
                f"Formatos soportados: PDF, DOCX, TXT, RTF, HTML."
            )

        # 3. Extraer texto
        extraction = extractor.extract(file_path)

        if extraction.is_empty:
            if doc_format == DocumentFormat.PDF_SCANNED:
                extraction.warnings.append(
                    "El PDF parece escaneado y no contiene texto extraíble. "
                    "Se requiere OCR (no disponible en esta versión)."
                )
            else:
                extraction.warnings.append(
                    "El documento parece estar vacío o no se pudo extraer texto."
                )

        # 4. Chunking jurídico
        chunks = self.chunker.chunk(
            text=extraction.raw_text,
            norma_fuente=norma_fuente,
            rama_derecho=rama_derecho,
        )

        result = IngestionResult(
            file_name=file_path.name,
            format=doc_format,
            extraction=extraction,
            chunks=chunks,
            norma_fuente=norma_fuente,
            rama_derecho=rama_derecho,
        )

        logger.info(
            "ingestion_completed",
            file=file_path.name,
            format=doc_format.name,
            pages=extraction.pages,
            chunks=len(chunks),
            words=extraction.word_count,
        )

        return result
