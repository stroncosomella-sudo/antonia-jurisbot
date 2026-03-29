from __future__ import annotations
"""Cliente LLM configurable: soporta Anthropic (Claude) y Ollama (local)."""

from typing import Optional

import httpx
import structlog

from jurisbot.config import settings
from jurisbot.exceptions import LLMError

logger = structlog.get_logger()

# System prompt jurídico de élite — especializado en Derecho chileno
LEGAL_SYSTEM_PROMPT = """Eres un asistente jurídico académico de élite, especializado en el \
ordenamiento jurídico chileno. Operas con la precisión de un abogado de la Corte Suprema \
y la claridad pedagógica de un profesor universitario de primer nivel.

═══════════════════════════════════════════
JERARQUÍA NORMATIVA CHILENA QUE CONOCES:
═══════════════════════════════════════════
1. Constitución Política de la República (1980 y sus reformas)
2. Tratados Internacionales ratificados y vigentes (Art. 5° inc. 2° CPR)
3. Leyes Orgánicas Constitucionales (4/7 del Congreso)
4. Leyes de Quórum Calificado (mayoría absoluta)
5. Leyes simples, Decretos con Fuerza de Ley (DFL), Decretos Ley (DL)
6. Decretos Supremos, Reglamentos, Ordenanzas municipales
7. Autos Acordados de la Corte Suprema y Corte de Apelaciones

═══════════════════════════════════════════
REGLAS INVIOLABLES — INCUMPLIRLAS ES INACEPTABLE:
═══════════════════════════════════════════
1. NUNCA inventar artículos, numerales, incisos ni normas que no estén en el texto fuente.
2. NUNCA inventar roles de causa, sentencias, fechas ni tribunales ficticios.
3. NUNCA atribuir citas a autores sin estar seguro de la obra y año.
4. Cuando no tengas certeza de un dato específico, escribir:
   "(dato no verificable en el texto fuente — consulte fuente original)"
5. SIEMPRE citar la fuente legal exacta de cada afirmación relevante.
6. Responder en español chileno formal, tratamiento de "usted".
7. Este análisis es exclusivamente académico y NO constituye asesoría legal profesional.

═══════════════════════════════════════════
FORMATO DE CITACIÓN OBLIGATORIO:
═══════════════════════════════════════════
• Legislación:    "Art. [N°] inciso [N°] del [Cuerpo Legal completo]"
                  Ej: "Art. 1545 inciso 1° del Código Civil"
• Jurisprudencia: "[Tribunal], [tipo fallo], Rol N° [número]-[año]"
                  Ej: "Corte Suprema, sentencia de casación, Rol N° 12345-2023"
• Doctrina:       "[Apellido], [Nombre]. '[Título]'. [Editorial], [año], p. [N°]."
                  Ej: "Alessandri R., Arturo. 'De los Contratos'. Ed. Jurídica, 2009, p. 45."
• Si la fuente NO está en el texto: indicarlo explícitamente.

═══════════════════════════════════════════
TERMINOLOGÍA JURÍDICA CHILENA OBLIGATORIA:
═══════════════════════════════════════════
• Sentencias:  ratio decidendi, obiter dicta, norma decisoria litis,
               considerandos, vistos, teniendo presente, por tanto
• Contratos:   oferta, aceptación, vicios del consentimiento (error, fuerza, dolo),
               objeto lícito, causa lícita, lesión enorme
• Obligaciones: fuentes (contrato, cuasicontrato, delito, cuasidelito, ley),
                modos de extinguir, efectos, clasificación
• Procesal:    legitimación activa/pasiva, litisconsorcio, prejudicialidad,
               cosa juzgada, prescripción, caducidad, recursos
"""


class LLMClient:
    """Cliente unificado para proveedores de LLM (Anthropic / Ollama).

    Uso:
        client = LLMClient()
        response = client.generate("Explica el Art. 1545 del Código Civil")
    """

    def __init__(
        self,
        provider: Optional[str] = None,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ):
        self.provider = provider or settings.llm_provider
        self.api_key = api_key or settings.anthropic_api_key
        self.model = model or (
            settings.anthropic_model if self.provider == "anthropic"
            else settings.ollama_model
        )

    def generate_stream(
        self,
        prompt: str,
        system: str = LEGAL_SYSTEM_PROMPT,
        max_tokens: int = 1200,
        temperature: float = 0.3,
    ):
        """Genera texto en streaming (generador de strings) para UI reactiva.

        Uso con Streamlit:
            st.write_stream(llm.generate_stream(prompt))

        Yields:
            Fragmentos de texto a medida que llegan del LLM.
        """
        if self.provider == "anthropic":
            yield from self._stream_anthropic(prompt, system, max_tokens, temperature)
        else:
            # Ollama no soporta streaming en esta implementación → fallback síncrono
            yield self.generate(prompt, system, max_tokens, temperature)

    def _stream_anthropic(
        self, prompt: str, system: str, max_tokens: int, temperature: float
    ):
        """Stream desde la API de Anthropic usando el context manager .stream()."""
        if not self.api_key:
            raise LLMError(
                "API key de Anthropic no configurada. "
                "Configura JURISBOT_ANTHROPIC_API_KEY en tu archivo .env"
            )
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.api_key)
            with client.messages.stream(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system,
                messages=[{"role": "user", "content": prompt}],
            ) as stream:
                for text in stream.text_stream:
                    yield text
        except Exception as e:
            raise LLMError(f"Error en streaming con Anthropic: {e}") from e

    def generate(
        self,
        prompt: str,
        system: str = LEGAL_SYSTEM_PROMPT,
        max_tokens: int = 4096,
        temperature: float = 0.3,
        context: str = "",
    ) -> str:
        """Genera texto usando el LLM configurado.

        Args:
            prompt: Instrucción principal del usuario.
            system: System prompt (por defecto el jurídico).
            max_tokens: Máximo de tokens en la respuesta.
            temperature: Creatividad (0.0 = determinista, 1.0 = creativo).
            context: Contexto adicional (chunks recuperados del RAG).

        Returns:
            Texto generado por el LLM.

        Raises:
            LLMError: Si falla la comunicación con el proveedor.
        """
        # Construir prompt completo con contexto
        full_prompt = prompt
        if context:
            full_prompt = (
                f"CONTEXTO JURÍDICO (extraído del documento):\n"
                f"---\n{context}\n---\n\n"
                f"INSTRUCCIÓN: {prompt}\n\n"
                f"Responde basándote SOLO en el contexto proporcionado. "
                f"Cita artículos y fuentes específicas."
            )

        if self.provider == "anthropic":
            return self._generate_anthropic(full_prompt, system, max_tokens, temperature)
        elif self.provider == "ollama":
            return self._generate_ollama(full_prompt, system, max_tokens, temperature)
        else:
            raise LLMError(f"Proveedor LLM no soportado: {self.provider}")

    def _generate_anthropic(
        self, prompt: str, system: str, max_tokens: int, temperature: float
    ) -> str:
        """Genera texto usando la API de Anthropic (Claude)."""
        if not self.api_key:
            raise LLMError(
                "API key de Anthropic no configurada. "
                "Configura JURISBOT_ANTHROPIC_API_KEY en tu archivo .env"
            )

        try:
            import anthropic

            client = anthropic.Anthropic(api_key=self.api_key)
            response = client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system,
                messages=[{"role": "user", "content": prompt}],
            )

            text = response.content[0].text
            logger.info(
                "llm_response",
                provider="anthropic",
                model=self.model,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
            )
            return text

        except anthropic.AuthenticationError:
            raise LLMError("API key de Anthropic inválida. Verifica tu JURISBOT_ANTHROPIC_API_KEY.")
        except anthropic.RateLimitError:
            raise LLMError("Límite de rate de la API de Anthropic excedido. Intenta en unos minutos.")
        except Exception as e:
            raise LLMError(f"Error comunicándose con Anthropic: {e}") from e

    def _generate_ollama(
        self, prompt: str, system: str, max_tokens: int, temperature: float
    ) -> str:
        """Genera texto usando Ollama (LLM local)."""
        try:
            response = httpx.post(
                f"{settings.ollama_url}/api/generate",
                json={
                    "model": self.model,
                    "system": system,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": temperature,
                        "num_predict": max_tokens,
                    },
                },
                timeout=120.0,
            )
            response.raise_for_status()
            data = response.json()

            text = data.get("response", "")
            logger.info(
                "llm_response",
                provider="ollama",
                model=self.model,
                eval_count=data.get("eval_count", 0),
            )
            return text

        except httpx.ConnectError:
            raise LLMError(
                f"No se pudo conectar a Ollama en {settings.ollama_url}. "
                f"Asegúrate de que Ollama esté corriendo (ollama serve)."
            )
        except Exception as e:
            raise LLMError(f"Error comunicándose con Ollama: {e}") from e

    def is_available(self) -> bool:
        """Verifica si el LLM está disponible y configurado."""
        try:
            if self.provider == "anthropic":
                return bool(self.api_key)
            elif self.provider == "ollama":
                resp = httpx.get(f"{settings.ollama_url}/api/tags", timeout=5.0)
                return resp.status_code == 200
        except Exception:
            return False
        return False
