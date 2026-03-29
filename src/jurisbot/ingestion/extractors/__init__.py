"""Extractores de texto para diferentes formatos de documentos."""

from jurisbot.ingestion.extractors.base import ExtractionResult, BaseExtractor
from jurisbot.ingestion.extractors.pdf_extractor import PDFExtractor
from jurisbot.ingestion.extractors.docx_extractor import DocxExtractor
from jurisbot.ingestion.extractors.txt_extractor import TxtExtractor

__all__ = [
    "ExtractionResult", "BaseExtractor",
    "PDFExtractor", "DocxExtractor", "TxtExtractor",
]
