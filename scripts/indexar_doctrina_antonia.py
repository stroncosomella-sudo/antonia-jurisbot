"""
indexar_doctrina_antonia.py — AntonIA v3.0
Indexa toda la doctrina disponible en la carpeta doctrina_antonia
hacia ChromaDB (colección biblioteca_doctrina).

Uso:
    cd ~/Desktop/jurisbot-chile-temp
    source venv_mac/bin/activate
    python3 scripts/indexar_doctrina_antonia.py

Retoma desde donde quedó si se interrumpe (skip archivos ya indexados).
"""
from __future__ import annotations
import sys, os, json, time, hashlib
from pathlib import Path

# Rutas
ROOT       = Path(__file__).parent.parent
SRC        = ROOT / "src"
CHROMA_DIR = ROOT / "data" / "chroma"
MANIFEST   = ROOT / "data" / "biblioteca_manifest.json"
DOCTRINA   = Path("/Users/sergiotroncoso/Documents/Claude/Scheduled").parent.parent / \
             "Documents/Claude/Scheduled"

# Ajustar ruta a doctrina_antonia según el entorno
import platform
if platform.system() == "Darwin":  # Mac
    DOCTRINA = Path.home() / "Desktop" / "doctrina_antonia"
    # Si no existe, probar rutas alternativas
    if not DOCTRINA.exists():
        DOCTRINA = Path("/Users/sergiotroncoso/Documents/Claude/doctrina_antonia")
else:  # Linux (sandbox)
    DOCTRINA = Path("/sessions/epic-blissful-fermat/mnt/doctrina_antonia")

sys.path.insert(0, str(SRC))
sys.path.insert(0, str(ROOT / "streamlit_app"))

import warnings; warnings.filterwarnings("ignore")

# ── Mapeo carpeta → rama_derecho ──────────────────────────────
MAPEO_RAMAS = {
    "Derecho Civil":                           "civil",
    "Derecho Civil - Bienes y Derechos Reales":"civil",
    "Derecho Civil - Obligaciones y Contratos":"civil",
    "Derecho Penal":                           "penal",
    "Derecho Constitucional y Administrativo": "constitucional",
    "Derecho Constitucional y Administrativo ":"constitucional",
    "Derecho Procesal":                        "procesal",
    "Derecho Comercial":                       "comercial",
    "Derecho Internacional":                   "internacional",
    "Derecho Laboral":                         "laboral",
    "Derecho Sucesorio":                       "sucesorio",
    "Derecho Ambiental":                       "ambiental",
    "Derecho Romano":                          "civil",
    "Derecho Concursal":                       "comercial",
    "Derecho Urbanístico":                     "ambiental",
    "Filosofía y Teoría del Derecho":          "civil",
    "Derecho Canónico":                        "civil",
}

EXTENSIONES = {".pdf", ".docx", ".txt", ".doc"}

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]

def cargar_manifest() -> dict:
    """Carga el manifest existente como {hash: True} para saber qué ya está indexado."""
    if not MANIFEST.exists():
        return {}
    with open(MANIFEST) as f:
        data = json.load(f)
    return {w.get("hash", ""): True for w in data if w.get("hash")}

def guardar_manifest_entrada(obra: dict):
    """Agrega una entrada al manifest JSON."""
    data = []
    if MANIFEST.exists():
        with open(MANIFEST) as f:
            data = json.load(f)
    data.append(obra)
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("=" * 60)
    print("AntonIA — Indexación masiva doctrina_antonia")
    print("=" * 60)

    if not DOCTRINA.exists():
        print(f"ERROR: No se encontró la carpeta doctrina_antonia en:\n  {DOCTRINA}")
        print("Ajusta la variable DOCTRINA en este script.")
        sys.exit(1)

    # Importar pipeline de ingesta
    try:
        import chromadb
        from jurisbot.config import settings
        from jurisbot.ingestion.orchestrator import IngestionOrchestrator, IngestionResult
        from jurisbot.rag.engine import RAGEngine
    except ImportError as e:
        print(f"ERROR de import: {e}")
        print("Asegúrate de tener el venv activado: source venv_mac/bin/activate")
        sys.exit(1)

    # Conectar ChromaDB
    chroma = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        col = chroma.get_collection("biblioteca_doctrina")
        print(f"Colección actual: {col.count():,} chunks")
    except Exception:
        print("Colección no encontrada, se creará al indexar el primer documento.")
        col = None

    # Cargar hashes ya indexados (para no duplicar)
    ya_indexados = cargar_manifest()
    print(f"Obras ya en manifest: {len(ya_indexados)}")

    # Recopilar todos los archivos
    archivos = []
    for carpeta, rama in MAPEO_RAMAS.items():
        ruta = DOCTRINA / carpeta
        if not ruta.exists():
            continue
        for archivo in ruta.rglob("*"):
            if archivo.is_file() and archivo.suffix.lower() in EXTENSIONES:
                archivos.append((archivo, rama))

    print(f"Archivos encontrados: {len(archivos):,}")
    print()

    # Configurar LLM (no se usa para indexar, solo para RAG)
    settings.llm_provider = "anthropic"

    # Orquestador de ingesta
    orch = IngestionOrchestrator(chroma_path=CHROMA_DIR)

    # Estadísticas
    ok = 0
    skip = 0
    error = 0
    t0 = time.time()

    for i, (archivo, rama) in enumerate(archivos, 1):
        # Verificar si ya está indexado
        file_hash = sha256_file(archivo)
        if file_hash in ya_indexados:
            skip += 1
            continue

        # Mostrar progreso
        pct = i / len(archivos) * 100
        elapsed = time.time() - t0
        eta = (elapsed / i) * (len(archivos) - i) if i > 1 else 0
        print(f"[{i:4d}/{len(archivos)}] {pct:.0f}%  ETA:{eta/60:.0f}min  "
              f"{rama[:10]:10s}  {archivo.name[:55]}", end="\r", flush=True)

        try:
            result = orch.ingest_file(
                file_path=archivo,
                collection_name="biblioteca_doctrina",
                metadata_extra={
                    "rama_derecho": rama,
                    "fuente":       "doctrina_antonia",
                    "carpeta":      archivo.parent.name,
                },
            )

            if result and result.chunks_indexed > 0:
                ok += 1
                # Registrar en manifest
                guardar_manifest_entrada({
                    "titulo":       archivo.stem[:120],
                    "archivo":      archivo.name,
                    "rama_derecho": rama,
                    "hash":         file_hash,
                    "chunks":       result.chunks_indexed,
                    "fuente":       "doctrina_antonia",
                })
            else:
                error += 1

        except Exception as e:
            error += 1
            # Log silencioso para no interrumpir el progreso
            with open(ROOT / "data" / "indexacion_errores.log", "a") as log:
                log.write(f"{archivo.name}: {e}\n")

    print()  # nueva línea después del \r
    print()
    print("=" * 60)
    print(f"✓ Indexados:  {ok:,}")
    print(f"⏭ Saltados:   {skip:,}  (ya estaban en la biblioteca)")
    print(f"✗ Errores:    {error:,}  (ver data/indexacion_errores.log)")
    print()

    # Verificar estado final
    try:
        col2 = chroma.get_collection("biblioteca_doctrina")
        print(f"Chunks totales en ChromaDB: {col2.count():,}")
    except Exception:
        pass

    elapsed_total = time.time() - t0
    print(f"Tiempo total: {elapsed_total/60:.1f} minutos")
    print("=" * 60)

if __name__ == "__main__":
    main()
