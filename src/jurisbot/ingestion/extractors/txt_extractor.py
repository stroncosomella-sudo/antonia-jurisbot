from __future__ import annotations
"""Extractor de texto para archivos de texto plano con detección de encoding."""

from pathlib import Path

import chardet
import ftfy
import structlog

from jurisbot.ingestion.extractors.base import BaseExtractor, ExtractionResult
from jurisbot.exceptions import ExtractionError

logger = structlog.get_logger()


class TxtExtractor(BaseExtractor):
    """Extrae texto de archivos planos con detección inteligente de encoding."""

    def supported_formats(self) -> list[str]:
        return ["TXT", "RTF", "HTML"]

    def extract(self, file_path: Path) -> ExtractionResult:
        """Extrae texto de un archivo plano detectando encoding automáticamente.

        Args:
            file_path: Ruta al archivo de texto.

        Returns:
            ExtractionResult con texto limpio y normalizado.
        """
        try:
            raw_bytes = file_path.read_bytes()
        except Exception as e:
            raise ExtractionError(
                f"No se pudo leer el archivo '{file_path.name}': {e}"
            ) from e

        # Detectar encoding
        detection = chardet.detect(raw_bytes)
        encoding = detection.get("encoding", "utf-8") or "utf-8"
        confidence = detection.get("confidence", 0.0)

        logger.info(
            "encoding_detected",
            file=file_path.name,
            encoding=encoding,
            confidence=round(confidence, 2),
        )

        # Decodificar
        try:
            text = raw_bytes.decode(encoding, errors="replace")
        except (UnicodeDecodeError, LookupError):
            text = raw_bytes.decode("utf-8", errors="replace")
            encoding = "utf-8 (fallback)"

        # Reparar encoding corrupto con ftfy
        text = ftfy.fix_text(text)

        # Si es RTF, intentar limpiar tags
        if file_path.suffix.lower() == ".rtf":
            text = self._clean_rtf(text)

        # Si es HTML, extraer solo texto
        if file_path.suffix.lower() in (".html", ".htm"):
            text = self._clean_html(text)

        warnings = []
        if confidence < 0.7:
            warnings.append(
                f"Encoding detectado con baja confianza ({confidence:.0%}). "
                f"Algunos caracteres podrían no mostrarse correctamente."
            )

        metadata = {
            "format": file_path.suffix.upper().lstrip("."),
            "encoding": encoding,
            "encoding_confidence": confidence,
            "extractor": "TxtExtractor",
        }

        return ExtractionResult(
            raw_text=text,
            pages=max(1, len(text) // 3000),
            metadata=metadata,
            confidence_score=min(confidence, 0.9),
            warnings=warnings,
        )

    def _clean_rtf(self, text: str) -> str:
        """Limpia tags RTF básicos."""
        try:
            from striprtf.striprtf import rtf_to_text
            return rtf_to_text(text)
        except Exception:
            # Fallback: remover tags RTF manualmente
            import re
            text = re.sub(r'\\[a-z]+\d*\s?', '', text)
            text = re.sub(r'[{}]', '', text)
            return text.strip()

    def _clean_html(self, text: str) -> str:
        """Extrae texto limpio de HTML."""
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(text, "html.parser")
            # Remover scripts y styles
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()
            return soup.get_text(separator="\n", strip=True)
        except Exception:
            import re
            return re.sub(r'<[^>]+>', '', text)
