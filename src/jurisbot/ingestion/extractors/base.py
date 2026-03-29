from __future__ import annotations
"""Clase base y resultado de extracción para documentos jurídicos."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ExtractionResult:
    """Resultado de la extracción de un documento jurídico.

    Attributes:
        raw_text: Texto completo extraído del documento.
        pages: Número total de páginas.
        metadata: Metadatos del documento (autor, fecha, etc.).
        structured_sections: Secciones detectadas con estructura jerárquica.
        tables: Tablas extraídas del documento.
        confidence_score: Calidad de extracción (0.0 a 1.0).
        warnings: Advertencias durante la extracción.
    """
    raw_text: str
    pages: int = 0
    metadata: dict = field(default_factory=dict)
    structured_sections: list[dict] = field(default_factory=list)
    tables: list[dict] = field(default_factory=list)
    confidence_score: float = 1.0
    warnings: list[str] = field(default_factory=list)

    @property
    def word_count(self) -> int:
        return len(self.raw_text.split())

    @property
    def char_count(self) -> int:
        return len(self.raw_text)

    @property
    def is_empty(self) -> bool:
        return len(self.raw_text.strip()) == 0


class BaseExtractor(ABC):
    """Clase base abstracta para extractores de documentos."""

    @abstractmethod
    def extract(self, file_path: Path) -> ExtractionResult:
        """Extrae texto estructurado del documento.

        Args:
            file_path: Ruta al archivo a procesar.

        Returns:
            ExtractionResult con texto y metadatos.

        Raises:
            ExtractionError: Si falla la extracción.
        """
        ...

    @abstractmethod
    def supported_formats(self) -> list[str]:
        """Retorna lista de formatos soportados por este extractor."""
        ...
