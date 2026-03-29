from __future__ import annotations
"""Generador de herramientas de estudio jurídico usando LLM.

Genera: resúmenes, fichas de estudio, cuestionarios, glosarios,
mapas conceptuales y análisis de casos prácticos.
"""

import json
from dataclasses import dataclass, field
from typing import Optional

import structlog

from jurisbot.nlp.llm_client import LLMClient

logger = structlog.get_logger()


@dataclass
class Flashcard:
    """Ficha de estudio jurídica."""
    question: str
    answer: str
    difficulty: str  # basico, intermedio, avanzado
    source_ref: str  # "Art. 1545 CC"
    topic: str = ""


@dataclass
class QuizQuestion:
    """Pregunta de cuestionario jurídico."""
    question: str
    options: list[str]
    correct_answer: int  # índice de la opción correcta (0-based)
    explanation: str
    source_ref: str
    difficulty: str
    question_type: str = "multiple_choice"  # multiple_choice, true_false


@dataclass
class GlossaryEntry:
    """Entrada del glosario jurídico."""
    term: str
    definition: str
    legal_source: str  # Fuente legal de la definición
    example: str = ""
    related_terms: list[str] = field(default_factory=list)


@dataclass
class StudyMaterials:
    """Conjunto completo de materiales de estudio generados."""
    summary_brief: str = ""
    summary_medium: str = ""
    summary_full: str = ""
    flashcards: list[Flashcard] = field(default_factory=list)
    quiz: list[QuizQuestion] = field(default_factory=list)
    glossary: list[GlossaryEntry] = field(default_factory=list)
    concept_map_mermaid: str = ""
    key_articles: list[str] = field(default_factory=list)


class StudyGenerator:
    """Genera herramientas de estudio a partir de texto jurídico."""

    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm = llm_client or LLMClient()

    # =================================================================
    # RESÚMENES
    # =================================================================

    def generate_summary(self, text: str, level: str = "medio") -> str:
        """Genera resumen ejecutivo jurídico en 3 niveles.

        Args:
            text: Texto del documento jurídico.
            level: "breve" (1 párrafo), "medio" (1 página), "extenso" (completo).

        Returns:
            Resumen generado.
        """
        level_instructions = {
            "breve": """Genera un RESUMEN EJECUTIVO BREVE (4-6 oraciones) con esta estructura exacta:
1. Naturaleza y tipo del documento (ley, sentencia, contrato, doctrina, etc.)
2. Norma o cuerpo legal principal con número de artículo
3. Tesis central o ratio decidendi (si es sentencia)
4. Conclusión o efecto jurídico principal
NO uses bullets. Redacta en prosa académica formal.""",

            "medio": """Genera un RESUMEN EJECUTIVO COMPLETO con esta estructura:

**I. IDENTIFICACIÓN DEL DOCUMENTO**
Tipo, nombre, cuerpo legal, fecha (si aplica).

**II. ESTRUCTURA Y CONTENIDO PRINCIPAL**
Artículos, secciones o considerandos más relevantes con su contenido esencial.

**III. TESIS CENTRAL Y RATIO DECIDENDI**
(Para sentencias: ratio decidendi, norma decisoria litis, obiter dicta distinguidos claramente)
(Para leyes: principio rector, bienes jurídicos protegidos)
(Para contratos: obligaciones principales de cada parte)

**IV. NORMAS Y FUENTES CITADAS**
Lista de artículos y cuerpos legales mencionados en el texto.

**V. CONCLUSIÓN JURÍDICA**
Impacto y aplicación práctica en el ordenamiento jurídico chileno.

Cita SIEMPRE el artículo y fuente exacta. Si no está en el texto, no lo inventes.""",

            "extenso": """Genera un ANÁLISIS JURÍDICO EXTENSO Y EXHAUSTIVO con esta estructura:

**I. FICHA TÉCNICA DEL DOCUMENTO**
Tipo, nombre completo, promulgación/fecha, estado de vigencia.

**II. CONTEXTO NORMATIVO**
Ubicación en la jerarquía normativa chilena. Relación con la Constitución y otras leyes.

**III. ANÁLISIS ARTÍCULO POR ARTÍCULO**
Los artículos o considerandos más importantes, con comentario de su alcance y efectos.

**IV. RATIO DECIDENDI Y OBITER DICTA** (si es sentencia)
Distinción precisa entre la razón decisiva del fallo y las afirmaciones incidentales.

**V. DOCTRINA CITADA O APLICABLE**
Autores chilenos que han tratado esta materia (solo si están en el texto o son conocidos con certeza).

**VI. JURISPRUDENCIA RELACIONADA**
Fallos citados en el documento o directamente relacionados (solo los que consten en el texto).

**VII. RELACIONES CON OTRAS NORMAS**
Conexiones con el Código Civil, Código Penal, Código del Trabajo u otras normas según la rama.

**VIII. CONCLUSIÓN Y ANÁLISIS CRÍTICO**
Valoración académica del documento, fortalezas, vacíos normativos o controversias doctrinarias.

REGLA ABSOLUTA: Solo cita lo que está en el texto. Indica explícitamente cuando algo es inferencia.""",
        }

        instruction = level_instructions.get(level, level_instructions["medio"])

        prompt = (
            f"{instruction}\n\n"
            f"REGLA INVIOLABLE: NUNCA inventes artículos, roles, ni citas que no estén "
            f"en el texto fuente. Si no tienes el dato exacto, escribe "
            f"'(no especificado en el texto)'.\n"
            f"Formato: Prosa académica formal en español chileno. "
            f"Tratamiento de 'usted' para el lector."
        )

        return self.llm.generate(prompt=prompt, context=text[:12000])

    # =================================================================
    # FICHAS DE ESTUDIO
    # =================================================================

    def generate_flashcards(
        self, text: str, count: int = 10, difficulty: str = "mixto"
    ) -> list[Flashcard]:
        """Genera fichas de estudio (flashcards) a partir del texto jurídico.

        Args:
            text: Texto del documento jurídico.
            count: Número de fichas a generar.
            difficulty: "basico", "intermedio", "avanzado", o "mixto".

        Returns:
            Lista de Flashcard generadas.
        """
        difficulty_guide = {
            "basico": "definiciones de conceptos, contenido literal de artículos",
            "intermedio": "relaciones entre normas, requisitos legales, efectos jurídicos",
            "avanzado": "casos de aplicación, excepciones, jurisprudencia, doctrina divergente",
            "mixto": "mezcla de los 3 niveles anteriores",
        }

        tipo_pregunta = {
            "basico":      "definición literal de conceptos y contenido textual de artículos",
            "intermedio":  "relaciones entre normas, requisitos legales, efectos jurídicos y distinciones",
            "avanzado":    "aplicación a casos prácticos, excepciones, jurisprudencia y doctrina divergente",
            "mixto":       "30% básico (definiciones), 40% intermedio (relaciones), 30% avanzado (casos y excepciones)",
        }
        prompt = (
            f"Genera exactamente {count} fichas de estudio jurídicas TIPO CORNELL para preparación "
            f"de examen de grado en Derecho chileno.\n\n"
            f"Nivel: {difficulty} — {tipo_pregunta.get(difficulty, tipo_pregunta['mixto'])}\n\n"
            f"FORMATO JSON ESTRICTO:\n"
            f'{{"flashcards": [\n'
            f'  {{\n'
            f'    "question": "Pregunta específica y clara (puede incluir un caso hipotético breve)",\n'
            f'    "answer": "Respuesta completa citando artículo, inciso y cuerpo legal exacto. '
            f'Incluye requisitos, efectos o excepciones según corresponda.",\n'
            f'    "difficulty": "basico|intermedio|avanzado",\n'
            f'    "source_ref": "Art. N° del Código/Ley exacta",\n'
            f'    "topic": "nombre del tema jurídico (ej: Responsabilidad extracontractual)"\n'
            f'  }}\n'
            f"]}}\n\n"
            f"REGLAS INVIOLABLES:\n"
            f"- NUNCA inventes artículos ni normas que no estén en el texto\n"
            f"- Las preguntas deben ser útiles para preparar examen oral o escrito\n"
            f"- Los distractores de las preguntas deben cubrir errores comunes de estudiantes\n"
            f"- source_ref DEBE incluir número de artículo específico cuando esté disponible\n"
            f"- Responde SOLO con el JSON válido, sin texto adicional ni backticks"
        )

        response = self.llm.generate(prompt=prompt, context=text[:10000], temperature=0.4)
        return self._parse_flashcards(response)

    def _parse_flashcards(self, response: str) -> list[Flashcard]:
        """Parsea la respuesta del LLM en objetos Flashcard."""
        try:
            # Extraer JSON de la respuesta
            json_str = response
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                json_str = response.split("```")[1].split("```")[0]

            # Limpiar posibles problemas
            json_str = json_str.strip()
            if not json_str.startswith("{"):
                # Buscar el primer {
                idx = json_str.find("{")
                if idx >= 0:
                    json_str = json_str[idx:]

            data = json.loads(json_str)
            cards = data.get("flashcards", [])

            return [
                Flashcard(
                    question=c.get("question", ""),
                    answer=c.get("answer", ""),
                    difficulty=c.get("difficulty", "basico"),
                    source_ref=c.get("source_ref", ""),
                    topic=c.get("topic", ""),
                )
                for c in cards
                if c.get("question") and c.get("answer")
            ]
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            logger.warning("flashcard_parse_error", error=str(e))
            # Fallback: crear una ficha con la respuesta raw
            return [Flashcard(
                question="Error al generar fichas automáticamente",
                answer=response[:500],
                difficulty="basico",
                source_ref="",
            )]

    # =================================================================
    # CUESTIONARIOS
    # =================================================================

    def generate_quiz(
        self, text: str, count: int = 5, difficulty: str = "intermedio"
    ) -> list[QuizQuestion]:
        """Genera cuestionario de autoevaluación.

        Args:
            text: Texto del documento jurídico.
            count: Número de preguntas.
            difficulty: Nivel de dificultad.

        Returns:
            Lista de QuizQuestion.
        """
        nivel_desc = {
            "basico":      "definiciones y conceptos fundamentales, literalidad de normas",
            "intermedio":  "aplicación de normas a casos, relaciones entre instituciones jurídicas",
            "avanzado":    "casos complejos, excepciones, conflictos normativos, jurisprudencia contradictoria",
        }
        prompt = (
            f"Genera exactamente {count} preguntas de cuestionario jurídico chileno de selección "
            f"múltiple, nivel {difficulty} ({nivel_desc.get(difficulty, '')}).\n\n"
            f"FORMATO JSON ESTRICTO:\n"
            f'{{"quiz": [\n'
            f'  {{\n'
            f'    "question": "Pregunta clara. Para nivel avanzado, incluir un caso hipotético breve.",\n'
            f'    "options": [\n'
            f'      "A) Opción correcta con lenguaje técnico preciso",\n'
            f'      "B) Distractor plausible (error común de estudiantes)",\n'
            f'      "C) Distractor plausible (confunde norma parecida o artículo cercano)",\n'
            f'      "D) Distractor plausible (mezcla elementos correctos e incorrectos)"\n'
            f'    ],\n'
            f'    "correct_answer": 0,\n'
            f'    "explanation": "Explicación que cita el artículo exacto y explica por qué '
            f'los distractores son incorrectos.",\n'
            f'    "source_ref": "Art. N° del Código/Ley",\n'
            f'    "difficulty": "{difficulty}"\n'
            f'  }}\n'
            f"]}}\n\n"
            f"REGLAS INVIOLABLES:\n"
            f"- correct_answer es el ÍNDICE 0-based de la opción correcta (0=A, 1=B, 2=C, 3=D)\n"
            f"- NUNCA colocar la respuesta correcta siempre en la misma posición\n"
            f"- Los distractores deben ser plausibles para un estudiante de Derecho\n"
            f"- La explicación debe citar artículo exacto y refutar cada distractor\n"
            f"- NUNCA inventar artículos o normas que no estén en el texto\n"
            f"- Responde SOLO con JSON válido, sin texto adicional ni backticks"
        )

        response = self.llm.generate(prompt=prompt, context=text[:10000], temperature=0.4)
        return self._parse_quiz(response)

    def _parse_quiz(self, response: str) -> list[QuizQuestion]:
        """Parsea la respuesta del LLM en objetos QuizQuestion."""
        try:
            json_str = response
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                json_str = response.split("```")[1].split("```")[0]

            json_str = json_str.strip()
            if not json_str.startswith("{"):
                idx = json_str.find("{")
                if idx >= 0:
                    json_str = json_str[idx:]

            data = json.loads(json_str)
            questions = data.get("quiz", [])

            return [
                QuizQuestion(
                    question=q.get("question", ""),
                    options=q.get("options", []),
                    correct_answer=int(q.get("correct_answer", 0)),
                    explanation=q.get("explanation", ""),
                    source_ref=q.get("source_ref", ""),
                    difficulty=q.get("difficulty", "intermedio"),
                )
                for q in questions
                if q.get("question") and q.get("options")
            ]
        except (json.JSONDecodeError, KeyError) as e:
            logger.warning("quiz_parse_error", error=str(e))
            return []

    # =================================================================
    # GLOSARIO
    # =================================================================

    def generate_glossary(self, text: str, max_terms: int = 15) -> list[GlossaryEntry]:
        """Genera glosario jurídico contextual.

        Args:
            text: Texto del documento jurídico.
            max_terms: Máximo de términos a incluir.

        Returns:
            Lista de GlossaryEntry.
        """
        prompt = (
            f"Identifica los {max_terms} términos jurídicos más importantes del texto "
            f"y genera un glosario jurídico de precisión académica.\n\n"
            f"FORMATO JSON ESTRICTO:\n"
            f'{{"glossary": [\n'
            f'  {{\n'
            f'    "term": "Término jurídico exacto",\n'
            f'    "definition": "1) DEFINICIÓN TÉCNICA: según doctrina/ley. '
            f'2) DEFINICIÓN ACCESIBLE: en lenguaje claro sin jerga.",\n'
            f'    "legal_source": "Artículo exacto que define el término (ej: Art. 1438 CC) '
            f'o escribir No definido legalmente si no hay definición explícita",\n'
            f'    "example": "Ejemplo práctico concreto del término en contexto chileno",\n'
            f'    "related_terms": ["término relacionado 1", "término relacionado 2"]\n'
            f'  }}\n'
            f"]}}\n\n"
            f"CRITERIOS DE SELECCIÓN DE TÉRMINOS:\n"
            f"1. Priorizar términos definidos legalmente en el texto con artículo específico\n"
            f"2. Incluir instituciones jurídicas propias del derecho chileno\n"
            f"3. Incluir términos técnicos que un estudiante de pregrado pueda confundir\n"
            f"4. NUNCA inventar definiciones que no sean verificables en el texto o en la legislación chilena\n"
            f"5. Responde SOLO con JSON válido"
        )

        response = self.llm.generate(prompt=prompt, context=text[:10000], temperature=0.3)

        try:
            json_str = response
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0]
            elif "```" in response:
                json_str = response.split("```")[1].split("```")[0]

            json_str = json_str.strip()
            if not json_str.startswith("{"):
                idx = json_str.find("{")
                if idx >= 0:
                    json_str = json_str[idx:]

            data = json.loads(json_str)
            entries = data.get("glossary", [])

            return [
                GlossaryEntry(
                    term=e.get("term", ""),
                    definition=e.get("definition", ""),
                    legal_source=e.get("legal_source", ""),
                    example=e.get("example", ""),
                    related_terms=e.get("related_terms", []),
                )
                for e in entries
                if e.get("term") and e.get("definition")
            ]
        except (json.JSONDecodeError, KeyError) as e:
            logger.warning("glossary_parse_error", error=str(e))
            return []

    # =================================================================
    # MAPA CONCEPTUAL
    # =================================================================

    def generate_concept_map(self, text: str) -> str:
        """Genera mapa conceptual en formato Mermaid.

        Args:
            text: Texto del documento jurídico.

        Returns:
            String con diagrama Mermaid.
        """
        prompt = (
            "Genera un mapa conceptual JERÁRQUICO del documento jurídico en formato Mermaid.\n\n"
            "ESTRUCTURA OBLIGATORIA del mapa:\n"
            "- NIVEL 0 (raíz): Nombre del documento o institución jurídica principal\n"
            "- NIVEL 1: Ramas o instituciones principales (ej: Requisitos, Efectos, Excepciones)\n"
            "- NIVEL 2: Sub-conceptos con artículo entre corchetes cuando esté disponible\n"
            "- NIVEL 3 (opcional): Casos específicos, excepciones, sanciones\n\n"
            "TIPOS DE RELACIÓN que debes usar:\n"
            "- --> (flecha): jerarquía o derivación\n"
            "- -->|requiere| (etiquetada): cuando un elemento requiere otro\n"
            "- -->|produce| (etiquetada): cuando genera un efecto jurídico\n"
            "- -->|excepción| (etiquetada): cuando es una excepción a la regla\n\n"
            "EJEMPLO DE FORMATO CORRECTO:\n"
            "graph TD\n"
            "    A[Contrato Art.1438 CC] --> B[Requisitos Art.1445]\n"
            "    A --> C[Efectos Art.1545]\n"
            "    B --> D[Consentimiento libre]\n"
            "    B --> E[Objeto lícito Art.1461]\n"
            "    B --> F[Causa lícita Art.1467]\n"
            "    C -->|produce| G[Ley para las partes]\n"
            "    C -->|obliga| H[Ejecución de buena fe]\n\n"
            "REGLAS ESTRICTAS:\n"
            "- Máximo 18 nodos (para legibilidad)\n"
            "- Incluir número de artículo cuando esté disponible\n"
            "- Los nodos deben tener texto conciso (máximo 5 palabras)\n"
            "- NUNCA inventar artículos que no estén en el texto\n"
            "- Responde SOLO con el código Mermaid puro (SIN backticks, SIN ```mermaid)"
        )

        response = self.llm.generate(prompt=prompt, context=text[:8000], temperature=0.3)

        # Limpiar respuesta
        if "```mermaid" in response:
            response = response.split("```mermaid")[1].split("```")[0]
        elif "```" in response:
            response = response.split("```")[1].split("```")[0]

        return response.strip()

    # =================================================================
    # GENERACIÓN COMPLETA
    # =================================================================

    def generate_all(self, text: str, document_name: str = "") -> StudyMaterials:
        """Genera TODAS las herramientas de estudio de una vez.

        Args:
            text: Texto del documento jurídico.
            document_name: Nombre del documento (para logging).

        Returns:
            StudyMaterials con todos los materiales generados.
        """
        logger.info("generating_all_study_materials", document=document_name)

        materials = StudyMaterials()

        # 1. Resumen breve
        try:
            materials.summary_brief = self.generate_summary(text, "breve")
        except Exception as e:
            logger.error("summary_brief_failed", error=str(e))
            materials.summary_brief = f"Error generando resumen: {e}"

        # 2. Resumen medio
        try:
            materials.summary_medium = self.generate_summary(text, "medio")
        except Exception as e:
            logger.error("summary_medium_failed", error=str(e))

        # 3. Fichas de estudio
        try:
            materials.flashcards = self.generate_flashcards(text, count=10, difficulty="mixto")
        except Exception as e:
            logger.error("flashcards_failed", error=str(e))

        # 4. Cuestionario
        try:
            materials.quiz = self.generate_quiz(text, count=5, difficulty="intermedio")
        except Exception as e:
            logger.error("quiz_failed", error=str(e))

        # 5. Glosario
        try:
            materials.glossary = self.generate_glossary(text, max_terms=10)
        except Exception as e:
            logger.error("glossary_failed", error=str(e))

        # 6. Mapa conceptual
        try:
            materials.concept_map_mermaid = self.generate_concept_map(text)
        except Exception as e:
            logger.error("concept_map_failed", error=str(e))

        logger.info(
            "study_materials_generated",
            document=document_name,
            flashcards=len(materials.flashcards),
            quiz_questions=len(materials.quiz),
            glossary_terms=len(materials.glossary),
            has_concept_map=bool(materials.concept_map_mermaid),
        )

        return materials
