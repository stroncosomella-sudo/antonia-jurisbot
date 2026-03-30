"""
indexar_worker.py — AntonIA v4.1
Procesa UN solo archivo y sale.
- exit 0  = indexado OK
- exit 2  = sin chunks (archivo vacío/corrupto)
- exit 139 = segfault (capturado por el coordinador)

Uso interno — no llamar directamente.
"""
from __future__ import annotations
import sys, os, gc, time
from pathlib import Path

# Forzar single-thread ANTES de importar onnxruntime/torch
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

ROOT      = Path(__file__).parent.parent
SRC       = ROOT / "src"
CHROMA    = ROOT / "data" / "chroma"

sys.path.insert(0, str(SRC))
import warnings; warnings.filterwarnings("ignore")

def main():
    if len(sys.argv) < 3:
        print("Uso: indexar_worker.py <archivo> <rama>", file=sys.stderr)
        sys.exit(1)

    archivo = Path(sys.argv[1])
    rama    = sys.argv[2]

    if not archivo.exists():
        print(f"No existe: {archivo}", file=sys.stderr)
        sys.exit(2)

    try:
        from jurisbot.config import settings
        from jurisbot.ingestion.orchestrator import IngestionOrchestrator
        from jurisbot.rag.engine import RAGEngine
        settings.llm_provider = "anthropic"
    except ImportError as e:
        print(f"Import error: {e}", file=sys.stderr)
        sys.exit(3)

    try:
        orch   = IngestionOrchestrator()
        engine = RAGEngine(chroma_path=CHROMA)

        result = orch.ingest(
            file_path=archivo,
            rama_derecho=rama,
            norma_fuente=archivo.stem[:100],
        )

        if not result or not result.chunks:
            sys.exit(2)

        n = engine.index_chunks(result.chunks, collection_name="biblioteca_doctrina")

        # Flush ChromaDB antes de salir
        del engine, orch
        gc.collect()
        time.sleep(0.5)

        print(f"OK:{n}", flush=True)
        sys.exit(0)

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(4)

if __name__ == "__main__":
    main()
