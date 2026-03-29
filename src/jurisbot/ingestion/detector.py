from __future__ import annotations
"""Detección inteligente de formato de documentos jurídicos."""

from enum import Enum, auto
from pathlib import Path

import magic
import structlog

logger = structlog.get_logger()


class DocumentFormat(Enum):
    """Formatos de documentos soportados por JurisBot."""
    PDF_NATIVE = auto()
    PDF_SCANNED = auto()
    PDF_HYBRID = auto()
    DOCX = auto()
    DOC = auto()
    TXT = auto()
    RTF = auto()
    HTML = auto()
    IMAGE = auto()

    @property
    def display_name(self) -> str:
        names = {
            DocumentFormat.PDF_NATIVE: "PDF (texto nativo)",
            DocumentFormat.PDF_SCANNED: "PDF (escaneado — requiere OCR)",
            DocumentFormat.PDF_HYBRID: "PDF (híbrido)",
            DocumentFormat.DOCX: "Word (.docx)",
            DocumentFormat.DOC: "Word legacy (.doc)",
            DocumentFormat.TXT: "Texto plano",
            DocumentFormat.RTF: "Rich Text Format",
            DocumentFormat.HTML: "HTML",
            DocumentFormat.IMAGE: "Imagen (requiere OCR)",
        }
        return names.get(self, self.name)


class SmartFormatDetector:
    """Detecta formato de archivo por magic bytes, NO por extensión."""

    MIME_MAP: dict[str, DocumentFormat] = {
        "application/pdf": DocumentFormat.PDF_NATIVE,
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document": DocumentFormat.DOCX,
        "application/msword": DocumentFormat.DOC,
        "text/plain": DocumentFormat.TXT,
        "text/html": DocumentFormat.HTML,
        "application/rtf": DocumentFormat.RTF,
        "text/rtf": DocumentFormat.RTF,
    }

    IMAGE_MIMES: set[str] = {
        "image/jpeg", "image/png", "image/tiff",
        "image/webp", "image/bmp",
    }

    def detect(self, file_path: Path) -> DocumentFormat:
        """Detecta el formato del documento de forma inteligente.

        Args:
            file_path: Ruta al archivo a analizar.

        Returns:
            DocumentFormat detectado.

        Raises:
            FileNotFoundError: Si el archivo no existe.
            UnsupportedFormatError: Si el formato no es soportado.
        """
        if not file_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

        mime = magic.from_file(str(file_path), mime=True)
        logger.info("format_detected", file=file_path.name, mime=mime)

        if mime in self.IMAGE_MIMES:
            return DocumentFormat.IMAGE

        if mime == "application/pdf":
            return self._classify_pdf(file_path)

        # Fallback por extensión para casos edge
        if mime in ("application/octet-stream", "application/zip"):
            return self._fallback_by_extension(file_path)

        from jurisbot.exceptions import UnsupportedFormatError

        if fmt := self.MIME_MAP.get(mime):
            return fmt

        raise UnsupportedFormatError(
            f"Formato no soportado: {mime} ({file_path.name}). "
            f"Formatos aceptados: PDF, DOCX, TXT, RTF, HTML, imágenes."
        )

    def _classify_pdf(self, file_path: Path) -> DocumentFormat:
        """Clasifica un PDF en nativo, escaneado o híbrido."""
        import fitz

        doc = fitz.open(file_path)
        total_pages = len(doc)
        if total_pages == 0:
            doc.close()
            return DocumentFormat.PDF_NATIVE

        text_pages = 0
        for page in doc:
            text = page.get_text().strip()
            if len(text) > 50:  # Más de 50 chars = tiene texto real
                text_pages += 1
        doc.close()

        ratio = text_pages / total_pages

        if ratio > 0.85:
            fmt = DocumentFormat.PDF_NATIVE
        elif ratio < 0.15:
            fmt = DocumentFormat.PDF_SCANNED
        else:
            fmt = DocumentFormat.PDF_HYBRID

        logger.info(
            "pdf_classified",
            file=file_path.name,
            format=fmt.name,
            text_pages=text_pages,
            total_pages=total_pages,
            ratio=round(ratio, 2),
        )
        return fmt

    def _fallback_by_extension(self, file_path: Path) -> DocumentFormat:
        """Fallback por extensión cuando magic bytes no son concluyentes."""
        ext = file_path.suffix.lower()
        ext_map = {
            ".pdf": DocumentFormat.PDF_NATIVE,
            ".docx": DocumentFormat.DOCX,
            ".doc": DocumentFormat.DOC,
            ".txt": DocumentFormat.TXT,
            ".rtf": DocumentFormat.RTF,
            ".html": DocumentFormat.HTML,
            ".htm": DocumentFormat.HTML,
        }

        from jurisbot.exceptions import UnsupportedFormatError

        if fmt := ext_map.get(ext):
            logger.warning("fallback_extension", file=file_path.name, ext=ext)
            return fmt

        raise UnsupportedFormatError(
            f"No se pudo determinar el formato de: {file_path.name}"
        )
