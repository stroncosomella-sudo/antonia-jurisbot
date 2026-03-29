"""Excepciones custom de JurisBot Chile."""


class JurisBotError(Exception):
    """Excepción base de JurisBot."""
    pass


class UnsupportedFormatError(JurisBotError):
    """Formato de documento no soportado."""
    pass


class ExtractionError(JurisBotError):
    """Error durante la extracción de texto de un documento."""
    pass


class LLMError(JurisBotError):
    """Error de comunicación con el proveedor LLM."""
    pass


class EmbeddingError(JurisBotError):
    """Error generando embeddings."""
    pass


class DocumentNotFoundError(JurisBotError):
    """Documento no encontrado en la base de datos."""
    pass
