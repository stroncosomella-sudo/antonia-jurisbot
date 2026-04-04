"""
doctrina_service.py — Búsqueda en la Biblioteca de Doctrina AntonIA
1,845 obras indexadas de 26 áreas del Derecho chileno.
"""
import json
from pathlib import Path

_INDEX_PATH = Path(__file__).parent.parent / "data" / "doctrina_index.json"
_INDEX = None


def _load_index():
    global _INDEX
    if _INDEX is None:
        try:
            with open(_INDEX_PATH, "r", encoding="utf-8") as f:
                _INDEX = json.load(f)
        except Exception:
            _INDEX = []
    return _INDEX


def buscar_doctrina(query: str = "", area: str = "", limit: int = 20) -> list:
    """Buscar obras en la biblioteca de doctrina.
    query: texto libre (busca en autor y título)
    area: filtrar por área del derecho (ej: "Derecho Civil")
    """
    index = _load_index()
    q = query.lower().strip()
    results = []
    for item in index:
        if area and area.lower() not in item["area"].lower():
            continue
        if q:
            text = f"{item['autor']} {item['titulo']} {item['area']}".lower()
            if not all(w in text for w in q.split()):
                continue
        results.append(item)
        if len(results) >= limit:
            break
    return results


def listar_areas() -> list:
    """Retorna lista de áreas del derecho con conteo de obras."""
    index = _load_index()
    areas = {}
    for item in index:
        a = item["area"]
        areas[a] = areas.get(a, 0) + 1
    return sorted([{"area": a, "obras": c} for a, c in areas.items()],
                  key=lambda x: -x["obras"])


def buscar_por_autor(autor: str, limit: int = 30) -> list:
    """Buscar todas las obras de un autor específico."""
    index = _load_index()
    a = autor.lower().strip()
    return [item for item in index if a in item["autor"].lower()][:limit]


def total_obras() -> int:
    return len(_load_index())
