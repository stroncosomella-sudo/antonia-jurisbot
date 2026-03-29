#!/bin/bash
# ============================================================
#  AntonIA — Script de lanzamiento para Mac
#  Ejecutar desde terminal: bash LANZAR_ANTONIA.sh
# ============================================================

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo ""
echo "  ⚖️  AntonIA — Mar.IA Group"
echo "  ================================"
echo ""

# 1. Verificar Python 3
if ! command -v python3 &>/dev/null; then
  echo "❌ Python3 no encontrado. Instala desde https://python.org"
  exit 1
fi
echo "✅ Python3 encontrado"

# 2. Crear venv si no existe
if [ ! -f "venv_mac/bin/activate" ]; then
  echo "📦 Creando entorno virtual (solo primera vez)..."
  python3 -m venv venv_mac
fi

source venv_mac/bin/activate

# 3. Instalar/actualizar todas las dependencias siempre
echo "📥 Verificando dependencias..."
pip install --quiet --upgrade pip
pip install --quiet \
  streamlit \
  chromadb \
  anthropic \
  "sentence-transformers>=3.0.0" \
  pydantic \
  "pydantic-settings>=2.5.0" \
  python-dotenv \
  structlog \
  rich \
  PyMuPDF \
  pdfplumber \
  python-docx \
  sqlalchemy \
  httpx \
  python-magic \
  chardet \
  ftfy \
  wcwidth
echo "✅ Dependencias listas"

# 4. Matar instancias previas de Streamlit en puertos 8501/8502
for PORT in 8501 8502; do
  PID=$(lsof -ti :$PORT 2>/dev/null)
  if [ -n "$PID" ]; then
    echo "🔄 Liberando puerto $PORT (PID $PID)..."
    kill -9 $PID 2>/dev/null || true
    sleep 1
  fi
done

# 5. Configurar .env para Anthropic (solo si está vacío o no existe)
if [ ! -f ".env" ] || ! grep -q "JURISBOT_ANTHROPIC_API_KEY=sk-" .env 2>/dev/null; then
  cat > .env << 'ENVEOF'
JURISBOT_LLM_PROVIDER=anthropic
JURISBOT_ANTHROPIC_API_KEY=sk-ant-api03-IefGtCmp6UUuL3M2OlSb0GJiI6YiUyagMORFahEKB8g9lIoQ0-BClH26KW39yPeWnDpwTjrL-gGejU7LKLynNQ-4KvflQAA
JURISBOT_ANTHROPIC_MODEL=claude-sonnet-4-20250514
ENVEOF
  echo "✅ .env configurado"
fi

echo ""
echo "  ✅ Lanzando AntonIA en http://localhost:8501"
echo ""
echo "  Para URL pública: abre otra terminal y ejecuta: ngrok http 8501"
echo ""

# 6. Lanzar Streamlit
python3 -m streamlit run streamlit_app/app.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless false
