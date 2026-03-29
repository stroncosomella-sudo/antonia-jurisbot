"""Módulo de ingesta de documentos jurídicos."""

from jurisbot.ingestion.detector import SmartFormatDetector, DocumentFormat
from jurisbot.ingestion.orchestrator import IngestionOrchestrator

__all__ = ["SmartFormatDetector", "DocumentFormat", "IngestionOrchestrator"]
