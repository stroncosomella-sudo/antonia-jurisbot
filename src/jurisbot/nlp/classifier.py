from __future__ import annotations
"""Clasificador de documentos jurídicos chilenos por rama del derecho y tipo."""

import re
from dataclasses import dataclass

import structlog

logger = structlog.get_logger()


@dataclass
class ClassificationResult:
    """Resultado de la clasificación de un documento jurídico."""
    rama_derecho: str       # "Constitucional", "Civil", "Penal", etc.
    tipo_documento: str     # "ley", "sentencia", "doctrina", "contrato", etc.
    confidence: float       # 0.0 a 1.0
    keywords_found: list[str]
    norma_identifier: str   # "Ley N° 19.496", "Código Civil", etc.


class LegalClassifier:
    """Clasifica documentos jurídicos por rama del derecho y tipo.

    Usa heurísticas basadas en palabras clave específicas del derecho chileno
    para una clasificación rápida sin necesidad de modelos ML pesados.
    """

    # Palabras clave por rama del derecho
    BRANCH_KEYWORDS: dict[str, list[str]] = {
        "Constitucional": [
            "constitución", "constitucional", "derechos fundamentales",
            "recurso de protección", "acción de amparo", "tribunal constitucional",
            "garantías constitucionales", "artículo 19", "artículo 20",
            "inaplicabilidad", "inconstitucionalidad", "CPR",
        ],
        "Civil": [
            "código civil", "obligaciones", "contratos", "responsabilidad civil",
            "bienes", "sucesión", "herencia", "matrimonio", "filiación",
            "prescripción", "posesión", "dominio", "servidumbre",
            "arrendamiento", "compraventa", "hipoteca", "prenda",
        ],
        "Penal": [
            "código penal", "delito", "pena", "imputado", "querella",
            "fiscalía", "ministerio público", "presidio", "reclusión",
            "robo", "hurto", "homicidio", "estafa", "procesado",
            "auto de apertura", "acusación", "defensoría penal",
        ],
        "Laboral": [
            "código del trabajo", "trabajador", "empleador", "despido",
            "indemnización por años", "tutela laboral", "sindicato",
            "negociación colectiva", "juzgado de letras del trabajo",
            "dirección del trabajo", "contrato de trabajo", "finiquito",
        ],
        "Administrativo": [
            "administración del estado", "licitación", "contraloría",
            "dictamen", "acto administrativo", "municipalidad",
            "bases generales", "servicio público", "función pública",
            "procedimiento administrativo", "transparencia",
        ],
        "Tributario": [
            "código tributario", "impuesto", "SII", "renta", "IVA",
            "contribución", "tributario", "evasión", "elusión",
            "declaración de impuestos", "PPM", "FUT",
        ],
        "Comercial": [
            "código de comercio", "sociedad anónima", "sociedad limitada",
            "letra de cambio", "pagaré", "cheque", "quiebra",
            "reorganización", "liquidación", "comerciante", "SpA",
        ],
        "Procesal": [
            "código de procedimiento civil", "demanda", "contestación",
            "prueba", "sentencia", "recurso de apelación", "casación",
            "excepciones", "incidente", "medida precautoria",
            "juicio ordinario", "juicio sumario", "juicio ejecutivo",
        ],
        "Familia": [
            "tribunal de familia", "divorcio", "pensión de alimentos",
            "cuidado personal", "relación directa y regular", "adopción",
            "violencia intrafamiliar", "mediación familiar",
        ],
    }

    # Patrones para identificar tipo de documento
    TYPE_PATTERNS: dict[str, list[str]] = {
        "ley": [
            r"ley\s+n[°º]?\s*[\d\.]+",
            r"decreto\s+(?:ley|con\s+fuerza\s+de\s+ley)",
            r"DFL\s+N[°º]?\s*\d+",
            r"DL\s+N[°º]?\s*\d+",
        ],
        "codigo": [
            r"código\s+(?:civil|penal|del?\s+trabajo|de\s+comercio|tributario|procesal|orgánico)",
        ],
        "sentencia": [
            r"rol\s+n[°º]?\s*[\d\.\-]+",
            r"(?:vistos|considerando|se\s+resuelve)",
            r"corte\s+(?:suprema|de\s+apelaciones)",
            r"juzgado\s+(?:civil|penal|de\s+letras|de\s+familia)",
        ],
        "dictamen": [
            r"dictamen\s+n[°º]?\s*[\d\.]+",
            r"contraloría\s+general",
            r"dirección\s+del\s+trabajo",
        ],
        "doctrina": [
            r"revista\s+de\s+derecho",
            r"derecho\s+(?:civil|penal|constitucional|administrativo|laboral)",
            r"bibliografía",
            r"ISBN",
        ],
        "contrato": [
            r"comparecen?",
            r"las\s+partes\s+acuerdan",
            r"cláusula\s+(?:primera|segunda|\d+)",
            r"otorgado\s+ante\s+notario",
        ],
    }

    def classify(self, text: str, metadata: dict | None = None) -> ClassificationResult:
        """Clasifica un documento jurídico por rama y tipo.

        Args:
            text: Texto del documento (se analiza los primeros 5000 chars).
            metadata: Metadatos del documento (título, autor, etc.).

        Returns:
            ClassificationResult con rama, tipo y confianza.
        """
        # Analizar solo inicio del documento (más eficiente)
        sample = text[:5000].lower()
        if metadata:
            title = (metadata.get("title", "") or "").lower()
            sample = title + " " + sample

        # Clasificar rama del derecho
        rama, rama_confidence, keywords = self._classify_branch(sample)

        # Clasificar tipo de documento
        tipo, tipo_confidence = self._classify_type(sample)

        # Detectar identificador de norma
        norma_id = self._detect_norma_identifier(sample)

        confidence = (rama_confidence + tipo_confidence) / 2

        result = ClassificationResult(
            rama_derecho=rama,
            tipo_documento=tipo,
            confidence=confidence,
            keywords_found=keywords,
            norma_identifier=norma_id,
        )

        logger.info(
            "document_classified",
            rama=rama,
            tipo=tipo,
            confidence=round(confidence, 2),
            norma=norma_id,
        )

        return result

    def _classify_branch(self, text: str) -> tuple[str, float, list[str]]:
        """Clasifica la rama del derecho por frecuencia de keywords."""
        scores: dict[str, int] = {}
        found_keywords: dict[str, list[str]] = {}

        for branch, keywords in self.BRANCH_KEYWORDS.items():
            count = 0
            found = []
            for kw in keywords:
                occurrences = text.count(kw.lower())
                if occurrences > 0:
                    count += occurrences
                    found.append(kw)
            scores[branch] = count
            found_keywords[branch] = found

        if not any(scores.values()):
            return "General", 0.3, []

        best_branch = max(scores, key=scores.get)
        total = sum(scores.values())
        confidence = scores[best_branch] / total if total > 0 else 0.3

        return best_branch, min(confidence, 0.95), found_keywords[best_branch]

    def _classify_type(self, text: str) -> tuple[str, float]:
        """Clasifica el tipo de documento jurídico."""
        type_scores: dict[str, int] = {}

        for doc_type, patterns in self.TYPE_PATTERNS.items():
            count = 0
            for pattern in patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                count += len(matches)
            type_scores[doc_type] = count

        if not any(type_scores.values()):
            return "documento_general", 0.3

        best_type = max(type_scores, key=type_scores.get)
        return best_type, min(0.9, 0.5 + type_scores[best_type] * 0.1)

    def _detect_norma_identifier(self, text: str) -> str:
        """Detecta el identificador de la norma (e.g., 'Ley N° 19.496')."""
        patterns = [
            r"(ley\s+n[°º]?\s*[\d\.]+)",
            r"(DFL\s+n[°º]?\s*[\d\.]+)",
            r"(DL\s+n[°º]?\s*[\d\.]+)",
            r"(código\s+(?:civil|penal|del?\s+trabajo|de\s+comercio|tributario|orgánico\s+de\s+tribunales))",
            r"(constitución\s+política\s+de\s+la\s+república)",
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip().title()

        return ""
