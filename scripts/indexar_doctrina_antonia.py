"""
indexar_doctrina_antonia.py — AntonIA v4.1 (coordinador subprocess)
Indexa la doctrina_antonia procesando cada archivo en un subproceso aislado.

Si un PDF causa segfault (crash de Python), el coordinador principal lo detecta,
anota el archivo como fallido y continúa con el siguiente — sin morir nunca.

Uso:
    cd ~/Desktop/jurisbot-chile-temp
    source venv_mac/bin/activate
    python3 scripts/indexar_doctrina_antonia.py

Retoma donde quedó si se interrumpe.
"""
from __future__ import annotations
import sys, os, json, time, hashlib, subprocess, gc
from pathlib import Path

# Forzar single-thread antes de importar nada
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["OMP_NUM_THREADS"]        = "1"
os.environ["OPENBLAS_NUM_THREADS"]   = "1"
os.environ["MKL_NUM_THREADS"]        = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

ROOT      = Path(__file__).parent.parent
SKIP_FILE = ROOT / "data" / "indexed_hashes.json"
MANIFEST  = ROOT / "data" / "biblioteca_manifest_v2.json"
WORKER    = Path(__file__).parent / "indexar_worker.py"

import platform
if platform.system() == "Darwin":
    DOCTRINA = Path.home() / "Desktop" / "doctrina_antonia"
    if not DOCTRINA.exists():
        DOCTRINA = Path("/Users/sergiotroncoso/Documents/Claude/doctrina_antonia")
    if not DOCTRINA.exists():
        DOCTRINA = Path.home() / "Documents" / "doctrina_antonia"
else:
    DOCTRINA = Path("/sessions/epic-blissful-fermat/mnt/doctrina_antonia")

# ── Mapeo carpeta → rama ──────────────────────────────────────────────────
CARPETAS = [
    ("Derecho Civil",                             "civil"),
    ("Derecho Civil - Bienes y Derechos Reales",  "civil"),
    ("Derecho Civil - Obligaciones y Contratos",  "civil"),
    ("Derecho Penal",                             "penal"),
    ("Derecho Constitucional y Administrativo",   "constitucional"),
    ("Derecho Constitucional y Administrativo ",  "constitucional"),
    ("Derecho Procesal",                          "procesal"),
    ("Derecho Comercial",                         "comercial"),
    ("Derecho Internacional",                     "internacional"),
    ("Derecho Laboral",                           "laboral"),
    ("Derecho Sucesorio",                         "sucesorio"),
    ("Derecho Ambiental",                         "ambiental"),
    ("Derecho Romano",                            "civil"),
    ("Derecho Concursal",                         "comercial"),
    ("Derecho Urbanístico",                       "ambiental"),
    ("Filosofía y Teoría del Derecho",            "civil"),
    ("Derecho Canónico",                          "civil"),
]

# .docx y .doc causan segfault en Mac — solo PDF y TXT
EXTENSIONES = {".pdf", ".txt"}

TIMEOUT_POR_ARCHIVO = 180  # segundos máx por PDF

# ── Utilidades ──────────────────────────────────────────────────────────────
def sha_prefix(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:12]

def load_skip() -> set:
    if SKIP_FILE.exists():
        try:
            with open(SKIP_FILE) as f:
                return set(json.load(f))
        except Exception:
            pass
    return set()

def save_skip(s: set):
    SKIP_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = SKIP_FILE.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(sorted(s), f)
    tmp.replace(SKIP_FILE)  # escritura atómica

def append_manifest(entry: dict):
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    data = []
    if MANIFEST.exists():
        try:
            with open(MANIFEST) as f:
                data = json.load(f)
        except Exception:
            pass
    data.append(entry)
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ── Main ────────────────────────────────────────────────────────────────────
def main():
    print("=" * 65)
    print("AntonIA v4.1 — Indexación con subprocesos aislados")
    print("=" * 65)

    if not DOCTRINA.exists():
        print(f"\nERROR: No se encontró doctrina_antonia en:\n  {DOCTRINA}")
        sys.exit(1)

    print(f"doctrina_antonia: {DOCTRINA}")
    print(f"Worker:           {WORKER}")
    print()

    already_done = load_skip()
    print(f"Archivos ya indexados (skip): {len(already_done)}")

    # Recopilar PDFs pendientes
    pendientes = []
    for carpeta, rama in CARPETAS:
        ruta = DOCTRINA / carpeta
        if not ruta.exists():
            continue
        for f in sorted(ruta.rglob("*")):
            if not f.is_file() or f.suffix.lower() not in EXTENSIONES:
                continue
            try:
                sz = f.stat().st_size
            except Exception:
                continue
            if sz < 5000:
                continue
            prefix = sha_prefix(f)
            if prefix not in already_done:
                pendientes.append((sz, f, rama, prefix))

    pendientes.sort(key=lambda x: x[0])  # pequeños primero
    print(f"Por indexar: {len(pendientes)} archivos")
    print()

    if not pendientes:
        print("¡Todo indexado! No hay archivos pendientes.")
        sys.exit(0)

    ok_total    = 0
    error_total = 0
    crash_total = 0
    # Archivos que crasharon en ESTA sesión → no reintentar en el mismo run
    crashed_session: set = set()
    t0 = time.time()

    for idx, (sz, archivo, rama, prefix) in enumerate(pendientes, 1):
        if prefix in crashed_session:
            continue  # ya crashó esta sesión, saltar

        elapsed = time.time() - t0
        eta_s   = (elapsed / idx) * (len(pendientes) - idx) if idx > 1 else 0
        pct     = idx / len(pendientes) * 100

        print(
            f"[{idx:4d}/{len(pendientes)}] {pct:.0f}%  "
            f"ETA:{eta_s/60:.0f}min  "
            f"{rama[:8]:8s}  {archivo.name[:48]}",
            end="  ", flush=True
        )

        try:
            proc = subprocess.run(
                [sys.executable, str(WORKER), str(archivo), rama],
                capture_output=True,
                text=True,
                timeout=TIMEOUT_POR_ARCHIVO,
            )
        except subprocess.TimeoutExpired:
            print("⏱ timeout", flush=True)
            already_done.add(prefix)  # no reintentar archivos que cuelgan
            save_skip(already_done)
            error_total += 1
            continue
        except Exception as e:
            print(f"✗ {e}", flush=True)
            error_total += 1
            continue

        if proc.returncode == 0:
            # Extraer chunks del output "OK:N"
            chunks_n = 0
            for line in proc.stdout.strip().splitlines():
                if line.startswith("OK:"):
                    try:
                        chunks_n = int(line.split(":")[1])
                    except Exception:
                        pass

            print(f"✓ {chunks_n} chunks", flush=True)
            already_done.add(prefix)
            save_skip(already_done)
            append_manifest({
                "titulo":       archivo.stem[:120],
                "archivo":      archivo.name,
                "rama_derecho": rama,
                "hash":         prefix,
                "chunks":       chunks_n,
                "fuente":       "doctrina_antonia",
            })
            ok_total += 1

        elif proc.returncode == 2:
            # Sin chunks (archivo corrupto/vacío)
            print("✗ sin chunks", flush=True)
            already_done.add(prefix)  # no reintentar
            save_skip(already_done)
            error_total += 1

        elif proc.returncode in (-11, 139):
            # Segmentation fault — NO marcar como hecho, anotar en sesión
            print("💥 segfault (se reintentará en próxima sesión)", flush=True)
            crashed_session.add(prefix)
            crash_total += 1

        else:
            # Otro error
            stderr_short = (proc.stderr or "")[-80:].replace("\n", " ")
            print(f"✗ exit:{proc.returncode} {stderr_short}", flush=True)
            already_done.add(prefix)
            save_skip(already_done)
            error_total += 1

    # ── Resumen final ─────────────────────────────────────────────────────
    elapsed_total = time.time() - t0
    print()
    print("=" * 65)
    print(f"✓ Indexados:   {ok_total:,}")
    print(f"✗ Errores:     {error_total:,}")
    print(f"💥 Segfaults:  {crash_total:,}  (se reintentarán en próxima sesión)")
    print(f"Tiempo total:  {elapsed_total / 60:.1f} minutos")
    print("=" * 65)

    if crash_total > 0:
        print(f"\n⚠️  {crash_total} archivos crasharon con segfault.")
        print("   Solución permanente:")
        print("   cd ~/Desktop/jurisbot-chile-temp && source venv_mac/bin/activate")
        print("   pip uninstall onnxruntime onnxruntime-silicon -y")
        print("   pip install onnxruntime-silicon   # Apple Silicon (M1/M2/M3)")
        print("   # o si el comando anterior falla:")
        print("   pip install onnxruntime==1.16.3")
        sys.exit(1)  # salir con error para que indexar_loop.sh reinicie

    sys.exit(0)

if __name__ == "__main__":
    main()
