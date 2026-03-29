#!/usr/bin/env python3
"""
index_biblioteca.py — Indexa la Biblioteca de Doctrina Jurídica en ChromaDB

Este script procesa todos los documentos de la carpeta "Agrupación doctrina"
y los indexa en ChromaDB como la colección permanente 'biblioteca_doctrina'.

La colección persiste entre reinicios de la app (ChromaDB guarda en disco).

USO:
    # Desde la raíz del proyecto (con venv activo):
    python scripts/index_biblioteca.py --folder ~/Downloads/doctrina

    # Reiniciar (borrar colección anterior y reindexar):
    python scripts/index_biblioteca.py --folder ~/Downloads/doctrina --reset

    # Ver estadísticas de la biblioteca ya indexada:
    python scripts/index_biblioteca.py --stats

ESTRUCTURA ESPERADA DE LA CARPETA:
    doctrina/
      Derecho Civil/
        Alessandri-Contratos.pdf
        Peñailillo-Bienes.pdf
      Derecho Penal/
        Etcheberry-Tomo1.pdf
      Derecho Procesal/
        ...
      (una subcarpeta por rama del derecho)
"""

import sys
import argparse
import json
import time
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jurisbot.config import settings
from jurisbot.ingestion.orchestrator import IngestionOrchestrator
from jurisbot.rag.engine import RAGEngine

# ─── Constantes ───────────────────────────────────────────────
COLLECTION      = "biblioteca_doctrina"
MANIFEST_FILE   = Path("data/biblioteca_manifest.json")
SUPPORTED_EXTS  = {".pdf", ".docx", ".doc", ".txt", ".rtf"}
SKIP_KEYWORDS   = ["_OLD", "_old", "Pendiente"]   # carpetas a ignorar


def banner():
    print("\n" + "═"*60)
    print("  📚  AntonIA — Indexador de Biblioteca de Doctrina")
    print("  Mar.IA Group · LegalTech Chile")
    print("═"*60 + "\n")


def get_rag_engine() -> RAGEngine:
    settings.ensure_dirs()
    return RAGEngine()


def show_stats():
    """Muestra estadísticas de la biblioteca indexada."""
    banner()
    rag = get_rag_engine()
    col = rag.get_or_create_collection(COLLECTION)
    count = col.count()

    if count == 0:
        print("⚠  La biblioteca no está indexada aún.")
        print("   Ejecute: python scripts/index_biblioteca.py --folder <ruta>")
        return

    print(f"✅ Biblioteca activa: {count} fragmentos indexados en ChromaDB")

    if MANIFEST_FILE.exists():
        manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        ramas = {}
        for entry in manifest:
            r = entry.get("rama", "Sin clasificar")
            ramas[r] = ramas.get(r, 0) + 1
        print(f"   📁 {len(manifest)} documentos · {len(ramas)} ramas del derecho\n")
        for rama, n in sorted(ramas.items()):
            print(f"   {'⚖':>3}  {rama:<45} {n:>3} doc{'s' if n>1 else ''}")
    print()


def index_folder(folder: Path, reset: bool = False):
    """Indexa todos los documentos de la carpeta en ChromaDB."""
    banner()

    if not folder.exists():
        print(f"❌  Carpeta no encontrada: {folder}")
        print("    Descargue primero desde Google Drive.")
        sys.exit(1)

    # Recopilar archivos (excluyendo carpetas _OLD)
    all_files = [
        f for f in folder.rglob("*")
        if f.suffix.lower() in SUPPORTED_EXTS
        and not any(kw in str(f) for kw in SKIP_KEYWORDS)
    ]

    if not all_files:
        print(f"⚠  No se encontraron documentos en: {folder}")
        print(f"   Formatos soportados: {', '.join(SUPPORTED_EXTS)}")
        sys.exit(1)

    print(f"📂  Carpeta: {folder}")
    print(f"📄  Documentos encontrados: {len(all_files)}\n")

    settings.ensure_dirs()
    orch = IngestionOrchestrator()
    rag  = get_rag_engine()

    # Resetear colección si se solicita
    if reset:
        try:
            rag.delete_collection(COLLECTION)
            print("🗑   Colección anterior eliminada.\n")
        except Exception:
            pass

    manifest    = []
    ok_count    = 0
    err_count   = 0
    total_chunks = 0
    t_start     = time.time()

    for i, filepath in enumerate(all_files, 1):
        # Determinar rama desde la carpeta padre
        rama = filepath.parent.name
        if rama == folder.name:
            rama = "Sin clasificar"

        titulo_doc = filepath.stem.replace("-", " ").replace("_", " ")

        print(f"[{i:>3}/{len(all_files)}] {rama[:35]:<35} │ {filepath.name[:40]}")

        try:
            res = orch.ingest(filepath)

            # Enriquecer chunks con metadata de la biblioteca
            for chunk in res.chunks:
                chunk.rama_derecho = rama
                if not chunk.norma_fuente:
                    chunk.norma_fuente = titulo_doc

            n_indexed = rag.index_chunks(res.chunks, COLLECTION)
            total_chunks += n_indexed

            manifest.append({
                "file":   str(filepath),
                "rama":   rama,
                "titulo": titulo_doc,
                "pages":  res.extraction.pages,
                "words":  res.extraction.metadata.get("word_count", 0),
                "chunks": n_indexed,
            })

            print(f"{'':>8}✓ {n_indexed} fragmentos indexados ({res.extraction.pages} págs.)")
            ok_count += 1

        except Exception as e:
            print(f"{'':>8}✗ Error: {e}")
            err_count += 1

    # Guardar manifest
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_FILE.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    elapsed = time.time() - t_start
    print("\n" + "═"*60)
    print(f"  ✅  Indexación completada en {elapsed:.0f}s")
    print(f"  📚  {ok_count} documentos indexados · {total_chunks} fragmentos totales")
    if err_count:
        print(f"  ⚠   {err_count} documentos con error (revisar más arriba)")
    print(f"  💾  Manifest guardado en: {MANIFEST_FILE}")
    print("═"*60)
    print("\n  Reinicie AntonIA y acceda a 'BIBLIOTECA DOCTRINA' en el menú.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Indexa la Biblioteca de Doctrina en ChromaDB para AntonIA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--folder", "-f",
        type=Path,
        help="Ruta a la carpeta raíz de doctrina (e.g., ~/Downloads/doctrina)"
    )
    parser.add_argument(
        "--reset", "-r",
        action="store_true",
        help="Eliminar colección existente y reindexar desde cero"
    )
    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Mostrar estadísticas de la biblioteca actual sin reindexar"
    )

    args = parser.parse_args()

    if args.stats:
        show_stats()
        return

    if not args.folder:
        parser.print_help()
        print("\n❌  Especifique --folder o --stats\n")
        sys.exit(1)

    index_folder(args.folder.expanduser().resolve(), reset=args.reset)


if __name__ == "__main__":
    main()
