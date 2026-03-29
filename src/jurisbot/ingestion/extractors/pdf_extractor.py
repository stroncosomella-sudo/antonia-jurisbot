from __future__ import annotations
"""Extractor de texto para documentos PDF usando PyMuPDF y pdfplumber."""

from pathlib import Path

import fitz
import pdfplumber
import structlog

from jurisbot.ingestion.extractors.base import BaseExtractor, ExtractionResult
from jurisbot.exceptions import ExtractionError

logger = structlog.get_logger()


class PDFExtractor(BaseExtractor):
    """Extrae texto de PDFs nativos y con tablas complejas.

    Usa PyMuPDF (fitz) como motor principal por velocidad,
    y pdfplumber como respaldo para tablas complejas.
    """

    def supported_formats(self) -> list[str]:
        return ["PDF_NATIVE", "PDF_HYBRID"]

    def extract(self, file_path: Path) -> ExtractionResult:
        """Extrae texto de un PDF preservando estructura.

        Args:
            file_path: Ruta al archivo PDF.

        Returns:
            ExtractionResult con texto y estructura.

        Raises:
            ExtractionError: Si el PDF no se puede abrir o procesar.
        """
        try:
            return self._extract_with_fitz(file_path)
        except Exception as e:
            logger.warning("fitz_failed_trying_pdfplumber", error=str(e))
            try:
                return self._extract_with_pdfplumber(file_path)
            except Exception as e2:
                raise ExtractionError(
                    f"No se pudo extraer texto del PDF '{file_path.name}': {e2}"
                ) from e2

    def _extract_with_fitz(self, file_path: Path) -> ExtractionResult:
        """Extracción principal con PyMuPDF (fitz)."""
        doc = fitz.open(file_path)
        pages_text: list[str] = []
        structured_sections: list[dict] = []
        tables: list[dict] = []

        metadata = {
            "title": doc.metadata.get("title", ""),
            "author": doc.metadata.get("author", ""),
            "subject": doc.metadata.get("subject", ""),
            "creator": doc.metadata.get("creator", ""),
            "pages": len(doc),
            "format": "PDF",
            "extractor": "PyMuPDF",
        }

        for page_num, page in enumerate(doc, 1):
            text = page.get_text("text")
            pages_text.append(text)

            # Extraer bloques de texto con posición para detectar estructura
            blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
            for block in blocks.get("blocks", []):
                if block.get("type") == 0:  # Bloque de texto
                    for line in block.get("lines", []):
                        line_text = ""
                        max_size = 0
                        for span in line.get("spans", []):
                            line_text += span.get("text", "")
                            max_size = max(max_size, span.get("size", 0))

                        line_text = line_text.strip()
                        if not line_text:
                            continue

                        # Detectar títulos por tamaño de fuente
                        if max_size > 14 and len(line_text) > 3:
                            structured_sections.append({
                                "type": "heading",
                                "text": line_text,
                                "page": page_num,
                                "font_size": max_size,
                            })

        doc.close()
        raw_text = "\n\n".join(pages_text)

        # Intentar extraer tablas con pdfplumber
        try:
            tables = self._extract_tables(file_path)
        except Exception:
            pass

        logger.info(
            "pdf_extracted",
            file=file_path.name,
            pages=metadata["pages"],
            chars=len(raw_text),
            sections=len(structured_sections),
            tables=len(tables),
        )

        return ExtractionResult(
            raw_text=raw_text,
            pages=metadata["pages"],
            metadata=metadata,
            structured_sections=structured_sections,
            tables=tables,
            confidence_score=0.95 if raw_text.strip() else 0.1,
        )

    def _extract_with_pdfplumber(self, file_path: Path) -> ExtractionResult:
        """Extracción de respaldo con pdfplumber."""
        pages_text: list[str] = []
        tables: list[dict] = []

        with pdfplumber.open(file_path) as pdf:
            total_pages = len(pdf.pages)
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text() or ""
                pages_text.append(text)

                # Extraer tablas
                page_tables = page.extract_tables()
                for table in page_tables:
                    if table:
                        tables.append({
                            "page": page_num,
                            "headers": table[0] if table else [],
                            "rows": table[1:] if len(table) > 1 else [],
                        })

        raw_text = "\n\n".join(pages_text)
        return ExtractionResult(
            raw_text=raw_text,
            pages=total_pages,
            metadata={"format": "PDF", "extractor": "pdfplumber", "pages": total_pages},
            tables=tables,
            confidence_score=0.85,
        )

    def _extract_tables(self, file_path: Path) -> list[dict]:
        """Extrae solo tablas usando pdfplumber."""
        tables = []
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                page_tables = page.extract_tables()
                for table in page_tables:
                    if table and len(table) > 1:
                        tables.append({
                            "page": page_num,
                            "headers": table[0],
                            "rows": table[1:],
                        })
        return tables
