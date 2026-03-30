#!/bin/bash
# indexar_loop.sh — Auto-reinicia el indexador si crashea (segfault)
# Uso:
#   cd ~/Desktop/jurisbot-chile-temp
#   source venv_mac/bin/activate
#   bash scripts/indexar_loop.sh

SCRIPT="scripts/indexar_doctrina_antonia.py"
INTENTOS=0
MAX_INTENTOS=200   # máximo de reinicios (evita loop infinito)
PAUSA=3            # segundos entre reinicios

echo "════════════════════════════════════════════════════════"
echo "  AntonIA — Indexador con auto-reinicio"
echo "  Presiona Ctrl+C para detener"
echo "════════════════════════════════════════════════════════"
echo ""

while [ $INTENTOS -lt $MAX_INTENTOS ]; do
    INTENTOS=$((INTENTOS + 1))
    echo "[Intento $INTENTOS de $MAX_INTENTOS] $(date '+%H:%M:%S')"
    echo "────────────────────────────────────────────────────────"

    python3 "$SCRIPT"
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        echo ""
        echo "════════════════════════════════════════════════════════"
        echo "  ✅ ¡Indexación completada con éxito!"
        echo "════════════════════════════════════════════════════════"
        exit 0
    elif [ $EXIT_CODE -eq 139 ] || [ $EXIT_CODE -eq 11 ]; then
        # 139 = SIGSEGV (segmentation fault)
        echo ""
        echo "⚠️  Segmentation fault detectado (exit $EXIT_CODE)"
        echo "   El archivo problemático quedó marcado como procesado."
        echo "   Reiniciando en ${PAUSA}s..."
        sleep $PAUSA
    elif [ $EXIT_CODE -eq 130 ]; then
        # 130 = Ctrl+C
        echo ""
        echo "⏹  Detenido por el usuario."
        exit 0
    else
        echo ""
        echo "⚠️  Script terminó con código $EXIT_CODE"
        echo "   Reiniciando en ${PAUSA}s..."
        sleep $PAUSA
    fi

    echo ""
done

echo "❌ Se alcanzó el límite de $MAX_INTENTOS intentos."
echo "   Revisa data/indexed_hashes.json para ver el progreso."
exit 1
