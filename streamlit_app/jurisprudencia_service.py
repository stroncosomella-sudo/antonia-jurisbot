"""
jurisprudencia_service.py — Servicio de Jurisprudencia Chilena para AntonIA
Datos pre-computados del corpus PJUD (1.15M+ sentencias).
Búsqueda local por materia/tribunal/fecha + referencia a legislación.
"""
import json
from pathlib import Path

_REF_PATH = Path(__file__).parent.parent / "data" / "jurisprudencia_reference.json"
_REF = None


def _load_ref():
    global _REF
    if _REF is None:
        try:
            with open(_REF_PATH, "r", encoding="utf-8") as f:
                _REF = json.load(f)
        except Exception:
            _REF = {"total_sentencias": 0, "materias_principales": [],
                    "legislacion_frecuente": {}, "sentencias_recientes_ejemplo": []}
    return _REF


def total_sentencias() -> int:
    return _load_ref().get("total_sentencias", 0)


def ultima_actualizacion() -> str:
    return _load_ref().get("ultima_actualizacion", "desconocida")


def materias_principales(limit: int = 16) -> list:
    """Retorna las materias más frecuentes del corpus con su total de sentencias."""
    return _load_ref().get("materias_principales", [])[:limit]


def legislacion_citada(materia: str) -> list:
    """Retorna la legislación más citada para una materia específica."""
    ref = _load_ref()
    leg = ref.get("legislacion_frecuente", {})
    return leg.get(materia, [])


def sentencias_recientes(limit: int = 5) -> list:
    """Retorna sentencias recientes de ejemplo del corpus."""
    return _load_ref().get("sentencias_recientes_ejemplo", [])[:limit]


def categorias() -> list:
    """Retorna las categorías de tribunal disponibles."""
    return _load_ref().get("categorias", ["Corte Suprema", "Cortes de Apelaciones", "Juzgados"])


def buscar_materia(query: str) -> list:
    """Busca materias que coincidan con el texto dado."""
    q = query.lower().strip()
    materias = _load_ref().get("materias_principales", [])
    return [m for m in materias if q in m["materia"].lower()]


def generar_contexto_jurisprudencial(materia_query: str) -> str:
    """Genera un contexto rico para que el LLM haga mejor análisis jurisprudencial.
    Incluye: total de sentencias, materias relacionadas, legislación citada, sentencias recientes.
    """
    ref = _load_ref()
    total = ref.get("total_sentencias", 0)
    materias = buscar_materia(materia_query) if materia_query else ref.get("materias_principales", [])[:5]
    recientes = ref.get("sentencias_recientes_ejemplo", [])

    ctx_parts = [
        f"CORPUS JURISPRUDENCIAL PJUD: {total:,} sentencias chilenas indexadas.",
        f"Última actualización: {ref.get('ultima_actualizacion', 'N/D')}.",
        "",
        "MATERIAS RELACIONADAS EN EL CORPUS:"
    ]
    for m in materias[:8]:
        ctx_parts.append(f"  • {m['materia']}: {m['total']:,} sentencias")

    if materia_query:
        leg = legislacion_citada(materia_query.upper())
        if leg:
            ctx_parts.append("")
            ctx_parts.append("LEGISLACIÓN MÁS CITADA EN ESTA MATERIA:")
            for l in leg:
                ctx_parts.append(f"  • {l['ley']} ({l['citas']} citas)")

    if recientes:
        ctx_parts.append("")
        ctx_parts.append("SENTENCIAS RECIENTES DE EJEMPLO:")
        for s in recientes[:3]:
            ctx_parts.append(f"  • ROL {s['rol']} — {s['tribunal']} — {s['fecha']} — {s['materia']}")
            if "caratulado" in s:
                ctx_parts.append(f"    Caratulado: {s['caratulado']}")

    return "\n".join(ctx_parts)
