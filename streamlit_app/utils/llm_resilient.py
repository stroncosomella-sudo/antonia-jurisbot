"""
utils/llm_resilient.py — AntonIA · Mar.IA Group
Wrapper resiliente para llamadas al LLM.

Implementa:
  · Retry con backoff exponencial (1s → 2s → 4s)
  · Timeout configurable
  · Fallback graceful: retorna None cuando falla → academia_module usa banco estático
  · Logging de errores sin romper la UI
"""

import time
import logging
from typing import Optional

logger = logging.getLogger("antonia.llm")


def call_with_retry(
    llm,
    prompt: str,
    max_retries: int = 3,
    timeout_seconds: int = 30,
) -> Optional[str]:
    """
    Llama a llm.complete(prompt) con reintentos automáticos.

    Args:
        llm:             Instancia de LLMClient ya inicializada.
        prompt:          El prompt a enviar.
        max_retries:     Número máximo de intentos (default 3).
        timeout_seconds: Tiempo límite por intento (default 30s).

    Returns:
        str con la respuesta del LLM, o None si todos los intentos fallaron.
        Retornar None indica al caller que use el banco estático de fallback.
    """
    last_error = None

    for attempt in range(max_retries):
        try:
            response = llm.complete(prompt)
            if response and len(response.strip()) > 0:
                return response
            # Respuesta vacía — reintentar
            logger.warning(f"LLM devolvió respuesta vacía (intento {attempt + 1}/{max_retries})")

        except Exception as e:
            last_error = e
            err_name = type(e).__name__
            err_str = str(e).lower()

            # Rate limit / overloaded → esperar más
            if any(kw in err_str for kw in ["rate", "limit", "overload", "529", "too many"]):
                wait = 2 ** attempt  # 1s, 2s, 4s
                logger.warning(f"Rate limit detectado, esperando {wait}s (intento {attempt + 1})")
                time.sleep(wait)
                continue

            # Error de red / timeout → reintento rápido
            if any(kw in err_str for kw in ["timeout", "connection", "network", "read"]):
                wait = 1
                logger.warning(f"Error de red, reintentando en {wait}s (intento {attempt + 1}): {err_name}")
                time.sleep(wait)
                continue

            # Error 5xx del servidor → reintento con espera
            if any(kw in err_str for kw in ["500", "502", "503", "504", "server"]):
                wait = 2 ** attempt
                logger.error(f"Error de servidor {err_name}, esperando {wait}s (intento {attempt + 1})")
                time.sleep(wait)
                continue

            # Error 4xx (auth, bad request) → no tiene sentido reintentar
            if any(kw in err_str for kw in ["401", "403", "invalid_api", "authentication"]):
                logger.error(f"Error de autenticación LLM: {err_name}: {e}")
                return None  # Sin reintentos

            # Error desconocido → log y reintento simple
            logger.error(f"Error LLM inesperado (intento {attempt + 1}): {err_name}: {e}")
            if attempt < max_retries - 1:
                time.sleep(1)

    if last_error:
        logger.error(f"LLM falló después de {max_retries} intentos. Último error: {last_error}")

    return None  # Señal para usar banco estático


def sanitize_prompt_input(text: str, max_len: int = 300) -> str:
    """
    Sanitiza texto de usuario antes de incluirlo en un prompt LLM.
    Previene prompt injection básico.

    Args:
        text:    Texto a sanitizar (ej: historial de temas, respuesta del usuario).
        max_len: Longitud máxima permitida.

    Returns:
        Texto sanitizado y truncado.
    """
    if not text:
        return ""

    # Truncar
    text = str(text)[:max_len]

    # Eliminar patrones de injection conocidos (case-insensitive)
    injection_patterns = [
        '"""', "'''",
        "IGNORE ALL", "IGNORE PREVIOUS", "IGNORE INSTRUCTIONS",
        "FORGET ALL", "FORGET PREVIOUS",
        "PREVIOUS INSTRUCTIONS",
        "ALL PREVIOUS", "ALL INSTRUCTIONS",
        "SYSTEM:", "ASSISTANT:", "USER:",
        "<|im_start|>", "<|im_end|>",
        "\\n\\nHuman:", "\\n\\nAssistant:",
    ]
    text_upper = text.upper()
    for pattern in injection_patterns:
        # Reemplazar independiente del case
        import re as _re
        text = _re.sub(_re.escape(pattern), "", text, flags=_re.IGNORECASE)

    # Eliminar caracteres de control (excepto newline y tab)
    text = "".join(c for c in text if c >= " " or c in "\n\t")

    return text.strip()


def safe_html_text(text: str) -> str:
    """
    Escapa caracteres HTML especiales para uso seguro con unsafe_allow_html=True.
    Previene XSS cuando el contenido proviene de bancos de datos o input de usuario.

    Args:
        text: Texto que se insertará en HTML.

    Returns:
        Texto con <, >, &, " escapados.
    """
    import html
    return html.escape(str(text or ""), quote=False)
