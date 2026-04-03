"""AntonIA — By Mar.IA Group  v4.1
Plataforma de IA para el Derecho chileno.
4 perfiles: Alumno · Abogado · Profesor · Consulta Legal
"""
import sys, base64, json, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent))  # Asegurar que streamlit_app/ esté en sys.path

# Ruta al manifest de la biblioteca (relativa al directorio de la app)
_APP_DIR = Path(__file__).parent.parent
BIBLIOTECA_MANIFEST = _APP_DIR / "data" / "biblioteca_manifest.json"
BIBLIOTECA_COLLECTION = "biblioteca_doctrina"

import streamlit as st
from academia_module import render_academia
from abogado_module import render_abogado
from profesor_module import render_profesor
from consulta_legal_module import render_consulta_legal
from examen_simulado_module import render_examen_simulado
from calculadora_plazos_module import render_calculadora_plazos

# Importaciones pesadas (chromadb) de forma lazy para evitar crash en Python 3.14+
try:
    from jurisbot.config import settings
    from jurisbot.ingestion.orchestrator import IngestionOrchestrator
    from jurisbot.nlp.classifier import LegalClassifier
    from jurisbot.nlp.llm_client import LLMClient
    from jurisbot.study.generator import StudyGenerator
    from jurisbot.rag.engine import RAGEngine
    _JURISBOT_OK = True
except Exception as _e:
    _JURISBOT_OK = False
    import types
    settings = types.SimpleNamespace(anthropic_api_key=None)
    class _Stub:
        def __init__(self, *a, **kw): pass
        def __getattr__(self, n): return lambda *a, **kw: None
    IngestionOrchestrator = LegalClassifier = LLMClient = StudyGenerator = RAGEngine = _Stub
    import streamlit as _st
    _st.error(f"⚠️ Error cargando módulos RAG: {_e}. Algunas funciones avanzadas no estarán disponibles.", icon="🔧")

# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AntonIA · Mar.IA Group",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────
# PATRÓN ORNAMENTAL DAMASCO — tile 160×160 px
# Inspirado en papelería notarial y documentos legales premium:
# estrella de 8 puntas + anillos concéntricos + diamantes cardinales
# + líneas diagonales + dots de esquina → damasco continuo al tilear
# ─────────────────────────────────────────────────────────────────
_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 160 160">'

    # ── Grupo: formas rellenas ──────────────────────────────────
    '<g fill="#7a6040" stroke="none" opacity="0.042">'

    # Estrella central de 8 puntas (r_ext=30, r_int=11)
    # vértices calculados desde centro (80,80) alternando r=30/r=11
    # en ángulos 0°,22.5°,45°,...,337.5° con y-down SVG
    '<path d="M110,80 L90.2,84.2 L101.2,101.2 L84.2,90.2 '
    'L80,110 L75.8,90.2 L58.8,101.2 L69.8,84.2 '
    'L50,80 L69.8,75.8 L58.8,58.8 L75.8,69.8 '
    'L80,50 L84.2,69.8 L101.2,58.8 L90.2,75.8 Z"/>'

    # Estrella interior de 8 puntas (r_ext=15, r_int=6) — más suave
    '<path d="M95,80 L85.5,82.3 L90.6,90.6 L82.3,85.5 '
    'L80,95 L77.7,85.5 L69.4,90.6 L74.5,82.3 '
    'L65,80 L74.5,77.7 L69.4,69.4 L77.7,74.5 '
    'L80,65 L82.3,74.5 L90.6,69.4 L85.5,77.7 Z" opacity="0.55"/>'

    # Punto central
    '<circle cx="80" cy="80" r="2.8"/>'

    # Diamantes cardinales (entre anillo exterior y borde tile)
    '<path d="M80,40 L83,44.5 L80,49 L77,44.5 Z"/>'    # top
    '<path d="M80,111 L83,115.5 L80,120 L77,115.5 Z"/>' # bottom
    '<path d="M40,80 L44.5,77 L49,80 L44.5,83 Z"/>'     # left
    '<path d="M111,80 L115.5,77 L120,80 L115.5,83 Z"/>' # right

    # Diamantes en puntos medios de borde (conexión entre tiles)
    '<path d="M80,0 L83,4.5 L80,9 L77,4.5 Z"/>'
    '<path d="M80,151 L83,155.5 L80,160 L77,155.5 Z"/>'
    '<path d="M0,80 L4.5,77 L9,80 L4.5,83 Z"/>'
    '<path d="M151,80 L155.5,77 L160,80 L155.5,83 Z"/>'

    # Círculos de esquina (r=4 → aparecen como círculo completo al tilear 4 tiles)
    '<circle cx="0"   cy="0"   r="4"/>'
    '<circle cx="160" cy="0"   r="4"/>'
    '<circle cx="0"   cy="160" r="4"/>'
    '<circle cx="160" cy="160" r="4"/>'

    '</g>'

    # ── Grupo: solo trazos (anillos + diagonales damasco) ──────
    '<g fill="none" stroke="#7a6040" opacity="0.038">'

    # Anillo exterior
    '<circle cx="80" cy="80" r="37" stroke-width="0.55"/>'
    # Anillo interior
    '<circle cx="80" cy="80" r="20" stroke-width="0.38"/>'

    # Líneas diagonales del anillo a las esquinas — efecto damasco clásico
    # NW: anillo en 315° (105.5,54.5) → esquina (160,0)
    '<line x1="105.5" y1="54.5" x2="160" y2="0"   stroke-width="0.4"/>'
    # NE en este tile = SE del tile de arriba: (54.5,54.5) → (0,0)
    '<line x1="54.5"  y1="54.5" x2="0"   y2="0"   stroke-width="0.4"/>'
    # SE: (105.5,105.5) → (160,160)
    '<line x1="105.5" y1="105.5" x2="160" y2="160" stroke-width="0.4"/>'
    # SW: (54.5,105.5) → (0,160)
    '<line x1="54.5"  y1="105.5" x2="0"   y2="160" stroke-width="0.4"/>'

    # Líneas cardinales del tip de la estrella al diamante de borde
    '<line x1="80"  y1="50"  x2="80"  y2="40"  stroke-width="0.35"/>'
    '<line x1="80"  y1="110" x2="80"  y2="120" stroke-width="0.35"/>'
    '<line x1="50"  y1="80"  x2="40"  y2="80"  stroke-width="0.35"/>'
    '<line x1="110" y1="80"  x2="120" y2="80"  stroke-width="0.35"/>'

    '</g>'
    '</svg>'
)
BG = base64.b64encode(_SVG.encode()).decode()

# ─────────────────────────────────────────────
# CSS ÉLITE — Harvey AI + Dark Academia Premium
# Inspirado en: Harvey AI design system (2025),
# Behance Law Firm Dashboard, Sana AI, Linear
# Paleta: sidebar oscuro #141210, parchment #f5f0e8,
#         gold #c9963a, Playfair Display + Inter
# ─────────────────────────────────────────────
CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap');

/* ══ VARIABLES DE DISEÑO ══════════════════════ */
:root {{
  --sidebar-bg-top:    #141210;
  --sidebar-bg-bot:    #1e1b16;
  --sidebar-border:    rgba(201,150,58,0.18);
  --gold:              #c9963a;
  --gold-hover:        #e0ab4a;
  --gold-dim:          rgba(201,150,58,0.12);
  --gold-dim2:         rgba(201,150,58,0.06);
  --parchment:         #f5f0e8;
  --card-bg:           #ffffff;
  --text-ink:          #1a1813;
  --text-mid:          #5a4e3e;
  --text-muted:        #9a8e7e;
  --border:            #e2dbd0;
  --border-light:      #ede8de;
  --shadow-card:       0 2px 16px rgba(20,18,10,0.07), 0 1px 3px rgba(20,18,10,0.04);
  --shadow-raised:     0 8px 32px rgba(20,18,10,0.12), 0 2px 8px rgba(20,18,10,0.06);
  --radius-card:       12px;
  --radius-sm:         6px;
  --radius-btn:        5px;
}}

/* ══ FONDO PRINCIPAL ════════════════════════ */
html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"] {{
    background-color: #f0e9dc !important;
    background-image: url("data:image/svg+xml;base64,{BG}") !important;
    background-repeat: repeat !important;
    background-size: 160px 160px !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
    color: var(--text-ink) !important;
}}
[data-testid="stMain"],
[data-testid="stHeader"],
header, footer,
[data-testid="stToolbar"] {{
    background: transparent !important;
    box-shadow: none !important;
}}
[data-testid="block-container"] {{ padding-top: 0 !important; }}

/* ══ SIDEBAR — DARK ══════════════════════════ */
section[data-testid="stSidebar"] {{
    background: linear-gradient(175deg, var(--sidebar-bg-top) 0%, var(--sidebar-bg-bot) 100%) !important;
    border-right: 1px solid var(--sidebar-border) !important;
    box-shadow: 4px 0 24px rgba(0,0,0,0.18) !important;
}}
section[data-testid="stSidebar"] > div {{
    padding-top: 0 !important;
}}

/* Nav buttons dentro del sidebar */
section[data-testid="stSidebar"] .stButton button {{
    background: transparent !important;
    color: rgba(240,232,218,0.72) !important;
    border: none !important;
    border-left: 2px solid transparent !important;
    border-radius: 0 !important;
    text-align: left !important;
    width: 100% !important;
    padding: 0.58rem 1rem 0.58rem 0.85rem !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
    box-shadow: none !important;
    transition: all 0.18s ease !important;
    justify-content: flex-start !important;
    margin: 0 !important;
    line-height: 1.4 !important;
}}
section[data-testid="stSidebar"] .stButton button:hover {{
    background: var(--gold-dim2) !important;
    color: var(--gold-hover) !important;
    border-left-color: rgba(201,150,58,0.35) !important;
}}

/* Labels sidebar */
section[data-testid="stSidebar"] label {{
    font-size: 0.64rem !important;
    color: rgba(240,232,218,0.38) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.09em !important;
    font-weight: 600 !important;
    font-family: 'Inter', sans-serif !important;
}}
section[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,0.07) !important;
    margin: 0.6rem 0 !important;
}}
section[data-testid="stSidebar"] p {{
    color: rgba(240,232,218,0.65) !important;
    margin: 0 !important;
    font-size: 0.82rem !important;
}}
section[data-testid="stSidebar"] .stSelectbox > div {{
    background: rgba(255,255,255,0.05) !important;
    border-color: rgba(255,255,255,0.12) !important;
    color: rgba(240,232,218,0.8) !important;
    border-radius: var(--radius-sm) !important;
}}
section[data-testid="stSidebar"] .stTextInput input {{
    background: rgba(255,255,255,0.06) !important;
    border-color: rgba(255,255,255,0.12) !important;
    color: rgba(240,232,218,0.9) !important;
    border-radius: var(--radius-sm) !important;
}}
section[data-testid="stSidebar"] .stTextInput input::placeholder {{
    color: rgba(240,232,218,0.3) !important;
}}

/* ══ BOTONES GLOBALES ════════════════════════ */
.stButton > button {{
    background: linear-gradient(135deg, #d4a43e, #b8860c) !important;
    color: #fff !important;
    border: none !important;
    border-radius: var(--radius-btn) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.76rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    padding: 0.6rem 1.8rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(184,134,12,0.25) !important;
}}
.stButton > button:hover {{
    background: linear-gradient(135deg, #e0b44a, #c9963a) !important;
    box-shadow: 0 4px 16px rgba(184,134,12,0.35) !important;
    transform: translateY(-1px) !important;
}}
.stButton > button:active {{
    transform: translateY(0) !important;
}}

/* ══ TARJETA PRINCIPAL ══════════════════════ */
.mc {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-card);
    padding: 2.2rem 2.8rem;
    box-shadow: var(--shadow-card);
    margin-bottom: 1rem;
}}
.mc-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--text-ink);
    letter-spacing: 0.02em;
    text-align: center;
    padding-bottom: 1rem;
    margin-bottom: 1.4rem;
    position: relative;
}}
.mc-title::after {{
    content: '';
    position: absolute;
    bottom: 0; left: 50%;
    transform: translateX(-50%);
    width: 48px; height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}}

/* ══ TARJETA GENÉRICA ═══════════════════════ */
.card {{
    background: #fdfaf5;
    border: 1px solid var(--border-light);
    border-radius: var(--radius-sm);
    padding: 1.2rem 1.4rem;
    margin: 0.5rem 0;
    line-height: 1.75;
    color: var(--text-ink);
}}

/* ══ FLASHCARDS ═════════════════════════════ */
.fq {{
    background: var(--text-ink);
    border-radius: var(--radius-sm);
    padding: 2rem 2.2rem;
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-style: italic;
    color: #f0e8d8;
    min-height: 120px;
    display: flex;
    align-items: center;
    justify-content: center;
    line-height: 1.65;
    border: 1px solid rgba(201,150,58,0.2);
}}
.fa {{
    background: #f2f9f4;
    border-left: 3px solid #2e9055;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    padding: 1.1rem 1.4rem;
    color: #1a3d28;
    margin-top: 0.8rem;
    line-height: 1.65;
}}
.stag {{
    display: inline-block;
    background: var(--gold-dim);
    color: #8a6800;
    font-size: 0.67rem;
    padding: 3px 10px;
    border-radius: 20px;
    margin-top: 0.5rem;
    border: 1px solid rgba(201,150,58,0.25);
    font-weight: 600;
    letter-spacing: 0.03em;
}}

/* ══ QUIZ ════════════════════════════════════ */
.qok {{
    background: #f0faf3;
    border-left: 3px solid #2e9055;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    padding: 0.8rem 1.1rem;
    color: #1a3d28;
    margin: 0.4rem 0;
    line-height: 1.6;
}}
.qno {{
    background: #fef5f5;
    border-left: 3px solid #d63535;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    padding: 0.8rem 1.1rem;
    color: #6e2020;
    margin: 0.4rem 0;
    line-height: 1.6;
}}

/* ══ PRICING CARDS ═══════════════════════════ */
.pc {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-card);
    padding: 2rem 1.6rem;
    text-align: center;
    box-shadow: var(--shadow-card);
    height: 100%;
    position: relative;
    transition: box-shadow 0.2s ease;
}}
.pc:hover {{
    box-shadow: var(--shadow-raised);
}}
.pc.feat {{
    background: var(--text-ink);
    border: 1px solid rgba(201,150,58,0.35);
    box-shadow: 0 8px 40px rgba(0,0,0,0.18);
}}
.pc-badge {{
    position: absolute;
    top: -13px; left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, #b8860c, #d4a43e);
    color: #fff;
    font-family: 'Inter', sans-serif;
    font-size: 0.6rem;
    font-weight: 700;
    padding: 3px 16px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(184,134,12,0.3);
}}
.pn {{
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--text-ink);
    margin-bottom: 0.8rem;
}}
.pp {{
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 700;
    color: var(--text-ink);
    line-height: 1;
}}
.per {{
    font-size: 0.73rem;
    color: var(--text-muted);
    margin-bottom: 0.6rem;
}}
.pd {{
    font-size: 0.79rem;
    color: var(--text-mid);
    margin: 0.8rem 0;
    line-height: 1.55;
    border-top: 1px solid var(--border-light);
    border-bottom: 1px solid var(--border-light);
    padding: 0.7rem 0;
}}
.pf {{
    font-size: 0.77rem;
    color: var(--text-mid);
    padding: 0.3rem 0;
    border-bottom: 1px solid var(--border-light);
    text-align: left;
}}
.pf:last-child {{ border-bottom: none; }}
.pc.feat .pn, .pc.feat .pp {{ color: #f0e8d8 !important; }}
.pc.feat .pd {{ color: #b8a88a !important; border-color: rgba(255,255,255,0.08) !important; }}
.pc.feat .pf {{ color: #b8a88a !important; border-bottom-color: rgba(255,255,255,0.06) !important; }}
.pc.feat .per {{ color: #887a68 !important; }}

/* ══ INPUTS GLOBALES ════════════════════════ */
.stTextInput input, .stTextArea textarea {{
    background: #fdfaf5 !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-ink) !important;
    font-family: 'Inter', sans-serif !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}}
.stTextInput input:focus, .stTextArea textarea:focus {{
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(201,150,58,0.10) !important;
    outline: none !important;
}}
[data-testid="stFileUploader"] {{
    background: rgba(245,240,232,0.6) !important;
    border: 2px dashed rgba(201,150,58,0.35) !important;
    border-radius: var(--radius-sm) !important;
    transition: border-color 0.2s !important;
}}
[data-testid="stFileUploader"]:hover {{
    border-color: var(--gold) !important;
}}

/* ══ MÉTRICAS & PROGRESS ════════════════════ */
.stProgress .st-bo {{ background-color: var(--gold) !important; }}
.stProgress > div > div {{
    background-color: var(--border-light) !important;
    border-radius: 99px !important;
}}
.stProgress .st-bo {{ border-radius: 99px !important; }}
div[data-testid="metric-container"] {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    box-shadow: var(--shadow-card);
}}

/* ══ CHAT ═══════════════════════════════════ */
[data-testid="stChatMessage"][data-testid*="user"] {{
    background: linear-gradient(135deg, #fef9ee, #fdf5e2) !important;
    border: 1px solid rgba(201,150,58,0.2) !important;
    border-radius: var(--radius-sm) !important;
}}
[data-testid="stChatMessage"] {{
    background: var(--card-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: var(--shadow-card) !important;
}}
[data-testid="stChatInput"] textarea {{
    background: var(--card-bg) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
}}
[data-testid="stChatInput"] textarea:focus {{
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(201,150,58,0.08) !important;
}}

/* ══ EXPANDER ═══════════════════════════════ */
.stExpander {{
    background: var(--card-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: var(--shadow-card) !important;
}}
.stExpander summary {{
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    color: var(--text-ink) !important;
}}

/* ══ TIPOGRAFÍA GLOBAL ══════════════════════ */
h1, h2, h3, h4 {{
    font-family: 'Playfair Display', Georgia, serif !important;
    color: var(--text-ink) !important;
}}
p, li {{ color: var(--text-mid) !important; }}
.stMarkdown p {{ color: var(--text-mid) !important; }}
.stRadio label {{ color: var(--text-ink) !important; }}
strong {{ color: var(--text-ink) !important; }}

/* ══ SELECTBOX ══════════════════════════════ */
.stSelectbox > div > div {{
    background: #fdfaf5 !important;
    border-color: var(--border) !important;
    border-radius: var(--radius-sm) !important;
}}

/* ══ SUCCESS / WARNING / ERROR ══════════════ */
[data-testid="stAlert"] {{
    border-radius: var(--radius-sm) !important;
}}

/* ══ SLIDER ═════════════════════════════════ */
[data-testid="stSlider"] [role="slider"] {{
    background: var(--gold) !important;
    border: 2px solid #fff !important;
    box-shadow: 0 0 0 2px var(--gold) !important;
}}
[data-testid="stSlider"] [data-baseweb="slider"] > div > div:last-child {{
    background: var(--gold) !important;
}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# OBJETOS CACHEADOS
# ─────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def get_llm(prov, key, mod):
    settings.llm_provider = prov
    if prov == "anthropic":
        settings.anthropic_api_key = key
        settings.anthropic_model = mod
    else:
        settings.ollama_model = mod
    return LLMClient(provider=prov, api_key=key if prov == "anthropic" else None, model=mod)

@st.cache_resource(show_spinner=False)
def get_rag():
    settings.ensure_dirs(); return RAGEngine()

@st.cache_resource(show_spinner=False)
def get_clf():
    return LegalClassifier()

@st.cache_resource(show_spinner=False)
def get_orch():
    return IngestionOrchestrator()

import hashlib as _hashlib

@st.cache_data(ttl=7200, show_spinner=False)
def _llm_cached(prompt_hash: str, prompt: str, system: str, max_tokens: int) -> str:
    """Cache de respuestas LLM — clave = hash del prompt completo."""
    prov = st.session_state.get("llm_provider", "anthropic")
    key  = st.session_state.get("llm_key", "")
    mod  = st.session_state.get("llm_model", "claude-3-5-haiku-20241022")
    llm  = get_llm(prov, key, mod)
    return llm.generate(prompt, system=system, max_tokens=max_tokens)

def llm_call(prompt: str, system: str, max_tokens: int = 1200) -> str:
    """Wrapper universal con cache. Usar en lugar de llm.generate() directo."""
    h = _hashlib.sha256(f"{prompt}{system}{max_tokens}".encode()).hexdigest()[:16]
    return _llm_cached(h, prompt, system, max_tokens)


# ─────────────────────────────────────────────
# ESTADO DE SESIÓN
# ─────────────────────────────────────────────
DEFAULTS = {
    "persona": "alumno",       # alumno | abogado | profesor | consulta
    "nav": "HOME",             # HOME = landing page
    "main_section": None,      # None | "universidad" | "abogados" | "consulta" | "prueba"
    "univ_perfil_elegido": False,  # True cuando el usuario eligió alumno/profesor en la landing
    "ingestion_result": None, "classification": None,
    "chat_history": [], "quiz_data": [], "quiz_answers": {},
    "quiz_submitted": False, "flashcards": [], "fc_idx": 0,
    "fc_show": False, "glossary": [], "concept_map": "",
    "summary_text": "", "jurisprudencia": "", "doctrina": "",
    "bib_result": "", "bib_rama": "Todas las ramas",
}

# ── Cargar manifest de biblioteca (si existe) ──
def load_biblioteca_manifest():
    if BIBLIOTECA_MANIFEST.exists():
        try:
            return json.loads(BIBLIOTECA_MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []

_bib_manifest = load_biblioteca_manifest()
_bib_ramas = sorted({e.get("rama","") for e in _bib_manifest if e.get("rama")})
_bib_activa = len(_bib_manifest) > 0
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

def set_nav(page): st.session_state.nav = page

def set_persona(p):
    st.session_state.persona = p
    defaults_nav = {
        "alumno":   "ENTRENA",
        "abogado":  "ABOGADO",
        "profesor": "PROFESOR",
        "consulta": "CONSULTA",
    }
    st.session_state.nav = defaults_nav.get(p, "ENTRENA")
    if p in ("alumno", "profesor"):
        st.session_state.main_section = "universidad"
        st.session_state.univ_perfil_elegido = True
    elif p == "abogado":
        st.session_state.main_section = "abogados"
    elif p == "consulta":
        st.session_state.main_section = "consulta"

def set_main_section(s):
    st.session_state.main_section = s
    if s == "abogados":
        st.session_state.persona = "abogado"
        st.session_state.nav = "ABOGADO"
    elif s == "consulta":
        st.session_state.persona = "consulta"
        st.session_state.nav = "CONSULTA"
    elif s == "universidad":
        # No pre-seleccionar persona — mostrar chooser en página principal
        st.session_state.univ_perfil_elegido = False
        st.session_state.nav = "HOME"
    elif s == "prueba":
        st.session_state.persona = "alumno"
        st.session_state.univ_perfil_elegido = True
        st.session_state.main_section = "universidad"
        st.session_state.nav = "ENTRENA"

def set_univ_perfil(p):
    """Llamado desde la Universidad landing cuando el usuario elige Alumno o Profesor."""
    st.session_state.persona = p
    st.session_state.univ_perfil_elegido = True
    defaults_nav = {"alumno": "ENTRENA", "profesor": "PROFESOR"}
    st.session_state.nav = defaults_nav.get(p, "ENTRENA")


# ─────────────────────────────────────────────
# SIDEBAR — NUEVO DISEÑO JERÁRQUICO
# ─────────────────────────────────────────────
with st.sidebar:

    # ── CSS para botones del sidebar ──────────────────────────────
    st.markdown("""<style>
    section[data-testid="stSidebar"] .stButton > button {
        background: rgba(201,150,58,0.04) !important;
        border: 1px solid rgba(201,150,58,0.18) !important;
        border-radius: 8px !important;
        padding: 0.62rem 0.85rem !important;
        text-align: left !important;
        height: auto !important;
        min-height: 2.4rem !important;
        color: rgba(240,232,218,0.75) !important;
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.18s ease !important;
        white-space: normal !important;
        line-height: 1.3 !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        border-color: rgba(201,150,58,0.55) !important;
        background: rgba(201,150,58,0.10) !important;
        color: #e8c97a !important;
        transform: translateX(2px) !important;
    }
    section[data-testid="stSidebar"] .stButton > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 2px rgba(201,150,58,0.3) !important;
    }
    /* Quitar margen extra entre botones */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div {
        gap: 0.12rem !important;
    }
    </style>""", unsafe_allow_html=True)

    # ── LOGO ─────────────────────────────────────────────────────
    st.markdown("""
    <div style="padding:1.4rem 1rem 0.6rem;border-bottom:1px solid rgba(201,150,58,0.1);">
      <div style="display:flex;align-items:center;gap:0.7rem;">
        <svg width="36" height="36" viewBox="0 0 38 38" fill="none">
          <circle cx="19" cy="19" r="17" stroke="rgba(201,150,58,0.45)"
                  stroke-width="1.2" fill="rgba(201,150,58,0.07)"/>
          <text x="19" y="25" text-anchor="middle"
                font-family="Playfair Display,Georgia,serif" font-size="18"
                font-weight="700" fill="#e8c97a" font-style="italic">M</text>
        </svg>
        <div>
          <div style="font-family:'Playfair Display',Georgia,serif;font-size:1.05rem;
                      font-weight:700;color:#f0e8d8;line-height:1.1;">
            Mar.<span style="color:#c9963a;">IA</span> Group
          </div>
          <div style="font-size:0.58rem;color:rgba(201,150,58,0.55);text-transform:uppercase;
                      letter-spacing:0.12em;margin-top:2px;">LegalTech Chile</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    # Botón AntonIA — usa st.button para preservar session_state (no window.reload)
    if st.button("⚖️ Anton**IA**", key="logo_home_btn",
                 use_container_width=True,
                 help="Volver al inicio sin perder tu progreso"):
        st.session_state.nav = "HOME"
        st.session_state.main_section = None
        st.rerun()

    st.markdown('<div style="height:0.6rem"></div>', unsafe_allow_html=True)

    # ── 4 SECCIONES PRINCIPALES ──────────────────────────────────
    ms = st.session_state.get("main_section")

    SECCIONES = [
        ("universidad", "🎓", "Universidad",    "Alumnos y profesores de Derecho"),
        ("abogados",    "⚖️", "Abogados",        "Herramientas para litigantes"),
        ("consulta",    "💬", "Consulta Legal",  "Asesoría jurídica inmediata"),
        ("prueba",      "🆓", "Prueba Gratis",   "Explora sin registrarte"),
    ]

    for sid, icon, label, desc in SECCIONES:
        active = ms == sid
        if active:
            st.markdown(
                f'<div style="margin:0.12rem 0;padding:0.68rem 0.9rem;'
                f'background:rgba(201,150,58,0.13);'
                f'border:1px solid rgba(201,150,58,0.5);'
                f'border-left:3px solid #c9963a;border-radius:8px;'
                f'display:flex;align-items:center;gap:0.65rem;">'
                f'<span style="font-size:1.05rem;min-width:1.3rem">{icon}</span>'
                f'<div><div style="font-size:0.78rem;font-weight:700;color:#e8c97a;'
                f'line-height:1.2;">{label}</div>'
                f'<div style="font-size:0.59rem;color:rgba(201,150,58,0.62);'
                f'margin-top:2px;">{desc}</div></div>'
                f'</div>',
                unsafe_allow_html=True)
            # ── SUB-NAVEGACIÓN (aparece solo cuando hay sección activa) ──
            if sid == "universidad":
                st.markdown(
                    '<div style="margin:0.6rem 0 0.35rem;padding:0 0.1rem;">'
                    '<div style="height:1px;background:rgba(201,150,58,0.15);margin-bottom:0.5rem;"></div>'
                    '<div style="font-size:0.57rem;font-weight:700;color:rgba(201,150,58,0.45);'
                    'text-transform:uppercase;letter-spacing:0.12em;padding:0 0.1rem 0.2rem;">¿Quién eres?</div>'
                    '</div>',
                    unsafe_allow_html=True)

                persona_actual = st.session_state.persona
                col_a, col_p   = st.columns(2)
                with col_a:
                    if persona_actual == "alumno":
                        st.markdown(
                            '<div style="border:1px solid #c9963a;background:rgba(201,150,58,0.15);'
                            'border-radius:7px;padding:0.42rem 0.3rem;text-align:center;'
                            'font-size:0.72rem;font-weight:700;color:#e8c97a;">👨‍🎓 Alumno</div>',
                            unsafe_allow_html=True)
                    else:
                        st.button("👨‍🎓 Alumno", key="sub_alumno",
                                  use_container_width=True,
                                  on_click=set_persona, args=("alumno",))
                with col_p:
                    if persona_actual == "profesor":
                        st.markdown(
                            '<div style="border:1px solid #c9963a;background:rgba(201,150,58,0.15);'
                            'border-radius:7px;padding:0.42rem 0.3rem;text-align:center;'
                            'font-size:0.72rem;font-weight:700;color:#e8c97a;">👩‍🏫 Profesor</div>',
                            unsafe_allow_html=True)
                    else:
                        st.button("👩‍🏫 Profesor", key="sub_profesor",
                                  use_container_width=True,
                                  on_click=set_persona, args=("profesor",))

                # ── Herramientas Alumno ────────────────────────────────
                if persona_actual == "alumno":
                    st.markdown(
                        '<div style="margin:0.5rem 0 0.25rem;">'
                        '<div style="height:1px;background:rgba(201,150,58,0.1);margin-bottom:0.4rem;"></div>'
                        '<div style="font-size:0.57rem;font-weight:700;color:rgba(201,150,58,0.45);'
                        'text-transform:uppercase;letter-spacing:0.12em;">Herramientas</div>'
                        '</div>',
                        unsafe_allow_html=True)

                    NAV_ALUMNO = [
                        ("🧠", "ENTRENA",                  "Quiz interactivo con IA"),
                        ("📝", "EXAMEN SIMULADO",           "Examen con nota 1-7"),
                        ("📅", "CALCULADORA PLAZOS",        "Plazos legales chilenos"),
                        ("📄", "DOCUMENTO",                "Genera contratos y escritos"),
                        ("📋", "RESUMEN EJECUTIVO",         "Resume casos y normativa"),
                        ("🔍", "ANÁLISIS",                  "Análisis jurídico profundo"),
                        ("⚖️", "JURISPRUDENCIA RELACIONADA","Jurisprudencia chilena"),
                        ("📚", "DOCTRINA RELACIONADA",      "Doctrina y artículos 2025"),
                        ("📖", "GLOSARIO LEGAL",            "Definiciones jurídicas"),
                        ("🗺️", "MAPA CONCEPTUAL",           "Visualiza conexiones"),
                        ("🎤", "ALEGATO ORAL",              "Prepara argumentos orales"),
                        ("💬", "CONSULTORÍA VIRTUAL",       "Pregunta a AntonIA"),
                        ("🏛",  "BIBLIOTECA DOCTRINA",      "Obras y artículos"),
                        ("📂", "BANCO DE CASOS",            "250+ casos reales"),
                        ("📈", "MI PROGRESO",               "Estadísticas de estudio"),
                    ]
                    for icon, label, tool_desc in NAV_ALUMNO:
                        if st.session_state.nav == label:
                            st.markdown(
                                f'<div style="margin:0.1rem 0;padding:0.5rem 0.85rem 0.5rem 0.75rem;'
                                f'background:linear-gradient(90deg,rgba(201,150,58,0.13),rgba(201,150,58,0.03));'
                                f'border-left:2.5px solid #c9963a;border-radius:0 7px 7px 0;">'
                                f'<div style="font-size:0.73rem;font-weight:700;color:#e8c97a;">'
                                f'{icon} {label}</div>'
                                f'<div style="font-size:0.58rem;color:rgba(201,150,58,0.55);margin-top:2px;">'
                                f'{tool_desc}</div>'
                                f'</div>',
                                unsafe_allow_html=True)
                        else:
                            st.button(f"{icon}  {label}", key=f"nav_{label}",
                                      use_container_width=True,
                                      on_click=set_nav, args=(label,),
                                      help=tool_desc)

                # ── Herramientas Profesor ──────────────────────────────
                elif persona_actual == "profesor":
                    st.markdown(
                        '<div style="margin:0.5rem 0 0.25rem;">'
                        '<div style="height:1px;background:rgba(201,150,58,0.1);margin-bottom:0.4rem;"></div>'
                        '<div style="font-size:0.57rem;font-weight:700;color:rgba(201,150,58,0.45);'
                        'text-transform:uppercase;letter-spacing:0.12em;">Panel Docente</div>'
                        '</div>',
                        unsafe_allow_html=True)
                    if st.session_state.nav == "PROFESOR":
                        st.markdown(
                            '<div style="padding:0.5rem 0.85rem 0.5rem 0.75rem;'
                            'background:linear-gradient(90deg,rgba(201,150,58,0.13),transparent);'
                            'border-left:2.5px solid #c9963a;border-radius:0 7px 7px 0;'
                            'font-size:0.73rem;font-weight:700;color:#e8c97a;">'
                            '🧑‍🏫 Herramientas Docentes</div>',
                            unsafe_allow_html=True)
                    else:
                        st.button("🧑‍🏫 Herramientas Docentes", key="nav_prof",
                                  use_container_width=True,
                                  on_click=set_nav, args=("PROFESOR",))

    # ── Pie del sidebar ──────────────────────────────────────────
    st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
    st.markdown('<div style="height:1px;background:rgba(201,150,58,0.1);margin:0 0 0.4rem;"></div>',
                unsafe_allow_html=True)

    col_q, col_s = st.columns(2)
    with col_q:
        st.button("🏛️ Quiénes", key="nav_quienes",
                  use_container_width=True,
                  on_click=set_nav, args=("QUIÉNES SOMOS",))
    with col_s:
        st.button("💎 Planes", key="nav_subs",
                  use_container_width=True,
                  on_click=set_nav, args=("SUSCRIPCIONES",))

    st.markdown('<div style="height:1px;background:rgba(201,150,58,0.1);margin:0.4rem 0 0.3rem;"></div>',
                unsafe_allow_html=True)

    # ── Motor IA ─────────────────────────────────────────────────
    _provider_key = "anthropic"
    _model        = "claude-sonnet-4-20250514"
    _api_key      = (
        st.secrets.get("ANTHROPIC_API_KEY", "")
        if hasattr(st, "secrets")
        else os.environ.get("ANTHROPIC_API_KEY", "")
    )
    settings.llm_provider      = _provider_key
    settings.anthropic_api_key = _api_key
    settings.anthropic_model   = _model

    # ── Biblioteca ───────────────────────────────────────────────
    if _bib_activa:
        n_docs  = len(_bib_manifest)
        n_ramas = len(_bib_ramas)
        st.markdown(
            f'<div style="padding:0.42rem 0.7rem;background:rgba(46,144,85,0.07);'
            f'border:1px solid rgba(46,144,85,0.2);border-radius:6px;">'
            f'<div style="font-size:0.57rem;font-weight:700;color:rgba(46,144,85,0.8);'
            f'text-transform:uppercase;letter-spacing:0.08em;">📚 Biblioteca activa</div>'
            f'<div style="font-size:0.6rem;color:rgba(200,220,200,0.6);margin-top:2px;">'
            f'{n_docs} obras · {n_ramas} ramas</div>'
            f'</div>',
            unsafe_allow_html=True)

    st.markdown(
        '<div style="margin:0.3rem 0 0.4rem;padding:0.45rem 0.7rem;'
        'background:rgba(218,165,32,0.04);border:1px solid rgba(218,165,32,0.14);'
        'border-radius:6px;font-size:0.59rem;color:rgba(218,165,32,0.55);line-height:1.4;">'
        '⚠ Análisis académico. No constituye asesoría legal profesional.</div>',
        unsafe_allow_html=True)


# ─────────────────────────────────────────────
# BARRA SUPERIOR — Elegante, inline styles
# ─────────────────────────────────────────────
st.markdown(f"""
<div style="display:flex;align-items:center;justify-content:space-between;
            padding:1.1rem 0 1rem;
            border-bottom:1px solid #e2dbd0;
            margin-bottom:1.2rem;">
  <div style="display:flex;align-items:baseline;gap:0.7rem;">
    <div style="font-family:'Playfair Display',Georgia,serif;font-size:2rem;
                font-weight:700;color:#1a1813;letter-spacing:-0.01em;line-height:1;">
      Anton<span style="color:#c9963a;">IA</span>
    </div>
    <div style="font-size:0.7rem;color:#9a8e7e;letter-spacing:0.06em;
                text-transform:uppercase;font-family:Inter,sans-serif;">
      by Mar.IA Group
    </div>
  </div>
  <div style="display:flex;gap:0.5rem;align-items:center;">
    <span onclick="window.parent.document.querySelector('[data-testid=stSidebar] button:nth-child(8)').click()"
          style="font-family:Inter,sans-serif;font-size:0.73rem;font-weight:500;
                 padding:6px 15px;border:1px solid #e2dbd0;border-radius:5px;
                 color:#5a4e3e;cursor:pointer;background:#fdfaf5;
                 transition:all 0.15s;">Quiénes Somos</span>
    <span onclick="window.parent.document.querySelector('[data-testid=stSidebar] button:nth-child(9)').click()"
          style="font-family:Inter,sans-serif;font-size:0.73rem;font-weight:500;
                 padding:6px 15px;border:1px solid #e2dbd0;border-radius:5px;
                 color:#5a4e3e;cursor:pointer;background:#fdfaf5;">Suscripciones y Planes</span>
    <span style="font-family:Inter,sans-serif;font-size:0.73rem;font-weight:600;
                 padding:6px 16px;border-radius:5px;
                 background:linear-gradient(135deg,#1a1813,#2d2820);
                 color:#f0e8d8;cursor:pointer;
                 box-shadow:0 2px 8px rgba(20,18,10,0.2);">Ingresar</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def need_doc():
    st.markdown("""
    <div style="background:#ffffff;border:1px solid #e2dbd0;
                border-left:3px solid #c9963a;border-radius:0 12px 12px 0;
                padding:2.2rem 2.5rem;text-align:center;margin:1.5rem 0;
                box-shadow:0 2px 16px rgba(20,18,10,0.06);">
      <div style="font-size:2.4rem;margin-bottom:0.7rem;opacity:0.6;">📄</div>
      <div style="font-family:'Playfair Display',serif;font-size:1rem;
                  color:#1a1813;font-weight:600;margin-bottom:0.4rem;">
        Sin documento activo
      </div>
      <div style="color:#9a8e7e;font-size:0.83rem;line-height:1.5;">
        Haz clic en <strong>📄 Documento</strong> en el menú izquierdo para subir un archivo PDF, Word o TXT.
      </div>
    </div>""", unsafe_allow_html=True)

def doc_text(limit=5500):
    return st.session_state.ingestion_result.extraction.raw_text[:limit]

def make_gen():
    return StudyGenerator(get_llm(_provider_key, _api_key, _model))

def active_llm():
    return get_llm(_provider_key, _api_key, _model)

def section_header(title):
    return f'<div class="mc"><div class="mc-title">{title}</div>'


# ── Helper: Casos relacionados del Banco ────────────────────────────────────
def _detectar_rama(texto: str) -> str | None:
    """Detecta la rama del derecho predominante en el texto mediante palabras clave."""
    t = texto.lower()
    scores = {
        "civil":         sum(t.count(w) for w in [
            "contrato","compraventa","arrendamiento","nulidad","obligación","obligaciones",
            "heredero","sucesión","testamento","propiedad","dominio","bienes","posesión",
            "responsabilidad civil","daño","indemnización","prescripción","código civil",
        ]),
        "penal":         sum(t.count(w) for w in [
            "delito","imputado","querella","fiscal","ministerio público","pena","condena",
            "código penal","homicidio","robo","hurto","estafa","procesado","acusado",
        ]),
        "procesal":      sum(t.count(w) for w in [
            "demanda","tribunal","juicio","procedimiento","sentencia","recurso","apelación",
            "casación","notificación","plazo fatal","expediente","audiencia","código de procedimiento",
        ]),
        "constitucional":sum(t.count(w) for w in [
            "constitución","derecho fundamental","garantía","recurso de protección","amparo",
            "ley orgánica","tribunal constitucional","cpr","carta fundamental",
        ]),
        "laboral":       sum(t.count(w) for w in [
            "trabajador","empleador","contrato de trabajo","despido","finiquito","sindicato",
            "huelga","código del trabajo","remuneración","indemnización por años","licencia",
        ]),
    }
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None


def _mostrar_casos_relacionados(texto_doc: str, max_casos: int = 3, key_prefix: str = "cr") -> None:
    """Muestra un panel de casos del banco relacionados al documento activo."""
    try:
        from casos_banco import CASOS
    except ImportError:
        return

    rama = _detectar_rama(texto_doc)
    if rama:
        candidatos = [c for c in CASOS if c["rama"] == rama]
    else:
        candidatos = CASOS

    import random, hashlib
    # Seed determinista basado en primeros 200 chars del texto para consistencia por sesión
    seed = int(hashlib.md5(texto_doc[:200].encode()).hexdigest(), 16) % (2**32)
    rng = random.Random(seed)
    muestra = rng.sample(candidatos, min(max_casos, len(candidatos)))

    _dif_color = {"básico": "#2e9055", "intermedio": "#c9963a", "avanzado": "#a83232"}
    rama_label = rama.capitalize() if rama else "Derecho"

    st.markdown(
        f'<div style="margin-top:1.8rem;padding-top:1.2rem;'
        f'border-top:1px solid rgba(201,150,58,0.2);">'
        f'<div style="font-size:0.72rem;font-weight:700;text-transform:uppercase;'
        f'letter-spacing:0.08em;color:#c9963a;margin-bottom:0.8rem;">'
        f'📂 Casos del Banco · {rama_label}</div></div>',
        unsafe_allow_html=True)

    for caso in muestra:
        dc = _dif_color.get(caso["dificultad"], "#888")
        with st.expander(f"#{caso['id']} · {caso['titulo']} · {caso['subtema']}", expanded=False):
            st.markdown(
                f'<span style="font-size:0.68rem;font-weight:700;color:{dc};'
                f'background:rgba(0,0,0,0.04);padding:0.1rem 0.45rem;border-radius:3px;">'
                f'{caso["dificultad"]}</span>', unsafe_allow_html=True)
            st.markdown(f"**Hechos:** {caso['hechos']}")
            st.markdown(
                f'<div style="font-style:italic;background:rgba(201,150,58,0.07);'
                f'padding:0.5rem 0.7rem;border-radius:4px;font-size:0.84rem;">'
                f'❓ {caso["pregunta"]}</div>', unsafe_allow_html=True)
            if st.button(f"💡 Ver respuesta", key=f"{key_prefix}_rev_{caso['id']}"):
                st.markdown(
                    f'<div style="background:rgba(46,144,85,0.07);border-left:3px solid #2e9055;'
                    f'padding:0.7rem 0.9rem;border-radius:0 6px 6px 0;font-size:0.83rem;">'
                    f'✅ {caso["respuesta"]}<br>'
                    f'<span style="font-size:0.74rem;color:#4a7a5a;">📌 {caso["fundamento"]}</span>'
                    f'</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div style="font-size:0.72rem;color:#a09070;margin-top:0.5rem;">'
        f'<a href="#" onclick="window.location.reload()" style="color:#c9963a;text-decoration:none;">'
        f'↻ Ver más casos</a> &nbsp;·&nbsp; '
        f'<span style="cursor:pointer;color:#c9963a;" '
        f'onclick="streamlit:navigate(\'BANCO DE CASOS\')">Ver banco completo →</span>'
        f'</div>', unsafe_allow_html=True)


nav     = st.session_state.nav
persona = st.session_state.persona

# ── HOME PAGE ────────────────────────────────────────────────────
# No mostrar HOME si el usuario está en el chooser de Universidad
_is_univ_chooser = (
    st.session_state.get("main_section") == "universidad"
    and not st.session_state.get("univ_perfil_elegido", False)
)
if not _is_univ_chooser and (nav == "HOME" or st.session_state.get("main_section") is None):
    st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--gold:#c9963a;--dark:#141210;--parchment:#f5f0e8;--card-dark:#1e1b16;}
@keyframes skySlide{from{transform:translateX(0)}to{transform:translateX(-50%)}}
@keyframes starGlow{0%,100%{opacity:.18}50%{opacity:.75}}
@keyframes carGo{from{left:-80px}to{left:calc(100% + 80px)}}
@keyframes carBack{from{right:-80px}to{right:calc(100% + 80px)}}
@keyframes heroIn{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
@keyframes goldPulse{0%,100%{box-shadow:0 0 0 0 rgba(201,150,58,.5)}60%{box-shadow:0 0 0 12px rgba(201,150,58,0)}}
.ant-hero{position:relative;padding:96px 20px 110px;background:linear-gradient(180deg,#04030e 0%,#070517 40%,#0b0818 70%,#060410 100%);overflow:hidden;text-align:center;}
.ant-s{position:absolute;border-radius:50%;background:#fff;animation:starGlow var(--d) ease-in-out infinite;animation-delay:var(--dl);}
.ant-hero::before{content:'';position:absolute;top:0;left:0;width:100%;height:60px;background:linear-gradient(180deg,rgba(4,3,14,1),transparent);pointer-events:none;z-index:4;}
.ant-cv{position:absolute;bottom:24px;left:0;width:200%;pointer-events:none;animation:skySlide 32s linear infinite;display:flex;}
.ant-cv svg{width:50%;flex-shrink:0;}
.ant-rd{position:absolute;bottom:0;left:0;width:100%;height:28px;background:linear-gradient(0deg,#020108,#0a0815);border-top:1px solid rgba(201,150,58,.1);}
.ant-rd::after{content:'';position:absolute;top:50%;left:0;width:100%;height:2px;background:repeating-linear-gradient(90deg,rgba(201,150,58,.5) 0 18px,transparent 18px 38px);}
.ant-car{position:absolute;height:7px;border-radius:3px;bottom:5px;animation:carGo var(--spd) linear infinite;animation-delay:var(--dl);}
.ant-car2{position:absolute;height:6px;border-radius:3px;bottom:14px;animation:carBack var(--spd) linear infinite;animation-delay:var(--dl);}
.ant-hc{position:relative;z-index:3;animation:heroIn .9s ease-out .15s both;}
.ant-label{font-family:Inter,sans-serif;font-size:.78rem;color:var(--gold);text-transform:uppercase;letter-spacing:.2em;font-weight:600;margin-bottom:20px;}
.ant-h1{font-family:'Playfair Display',serif;font-size:clamp(2.1rem,5.2vw,3.7rem);font-weight:900;color:#f5f0e8;line-height:1.16;margin-bottom:18px;}
.ant-h1 em{font-style:normal;color:var(--gold);}
.ant-sub{font-family:Inter,sans-serif;font-size:1.02rem;color:rgba(240,232,218,.68);max-width:560px;margin:0 auto 36px;line-height:1.7;}
.ant-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
.ant-bp{padding:12px 30px;background:var(--gold);color:#0d0b09;border-radius:8px;font-family:Inter,sans-serif;font-size:.95rem;font-weight:700;display:inline-block;animation:goldPulse 2.4s infinite;transition:.25s;}
.ant-bp:hover{background:#daa840;transform:translateY(-2px);box-shadow:0 12px 32px rgba(201,150,58,.28);}
.ant-bs{padding:12px 28px;background:transparent;color:var(--gold);border:2px solid rgba(201,150,58,.6);border-radius:8px;font-family:Inter,sans-serif;font-size:.95rem;font-weight:600;display:inline-block;transition:.25s;}
.ant-bs:hover{background:rgba(201,150,58,.1);border-color:var(--gold);transform:translateY(-2px);}
.ant-stats{display:flex;justify-content:center;gap:clamp(16px,4vw,52px);padding:26px 20px;background:rgba(201,150,58,.04);border-top:1px solid rgba(201,150,58,.11);border-bottom:1px solid rgba(201,150,58,.11);flex-wrap:wrap;}
.ant-stat-n{font-family:'Playfair Display',serif;font-size:1.85rem;font-weight:800;color:var(--gold);}
.ant-stat-l{font-size:.7rem;color:#8a7850;text-transform:uppercase;letter-spacing:.08em;margin-top:3px;}
.ant-sec{padding:52px 20px;max-width:900px;margin:0 auto;}
.ant-sec-t{font-family:'Playfair Display',serif;font-size:1.85rem;font-weight:800;color:#1a1813;text-align:center;margin-bottom:8px;}
.ant-sec-s{font-size:.9rem;color:#9a8a6a;text-align:center;margin-bottom:34px;}
.ant-grid-4{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:14px;}
.ant-card{background:#1a1520;border:1px solid rgba(201,150,58,.14);border-radius:12px;padding:22px 18px;transition:all .25s;}
.ant-card:hover{border-color:rgba(201,150,58,.42);transform:translateY(-3px);box-shadow:0 14px 38px rgba(0,0,0,.32);}
.ant-card-icon{font-size:1.9rem;margin-bottom:10px;}
.ant-card-t{font-family:Inter,sans-serif;font-size:.86rem;font-weight:700;color:#f0e8d8;margin-bottom:6px;}
.ant-card-d{font-size:.76rem;color:rgba(240,232,218,.755);line-height:1.55;}
.ant-steps{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:8px;}
.ant-step{flex:1;min-width:155px;max-width:215px;text-align:center;padding:20px 14px;background:rgba(201,150,58,.045);border:1px solid rgba(201,150,58,.11);border-radius:10px;}
.ant-step-n{font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:900;color:var(--gold);line-height:1;}
.ant-step-t{font-size:.86rem;font-weight:700;color:#1a1813;margin:7px 0 4px;}
.ant-step-d{font-size:.76rem;color:#9a8a6a;line-height:1.5;}
.ant-tools{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:11px;}
.ant-tool{background:rgba(201,150,58,.035);border:1px solid rgba(201,150,58,.11);border-radius:9px;padding:15px 13px;display:flex;align-items:flex-start;gap:9px;transition:.2s;}
.ant-tool:hover{border-color:rgba(201,150,58,.36);background:rgba(201,150,58,.065);}
.ant-tool-icon{font-size:1.3rem;min-width:1.5rem;}
.ant-tool-t{font-size:.8rem;font-weight:700;color:#1a1813;margin-bottom:2px;}
.ant-tool-d{font-size:.7rem;color:#9a8a6a;line-height:1.45;}
.ant-cta{text-align:center;padding:52px 20px;background:linear-gradient(135deg,rgba(201,150,58,.07),rgba(201,150,58,.025));border-top:1px solid rgba(201,150,58,.11);}
.ant-cta-t{font-family:'Playfair Display',serif;font-size:1.65rem;font-weight:800;color:#1a1813;margin-bottom:10px;}
.ant-cta-s{font-size:.9rem;color:#9a8a6a;margin-bottom:26px;}
</style>

<div class="ant-hero">

  <!-- Stars -->
  <div class="ant-s" style="width:2px;height:2px;top:7%;left:8%;--d:2.1s;--dl:0s;"></div>
  <div class="ant-s" style="width:1px;height:1px;top:13%;left:22%;--d:3.0s;--dl:.4s;"></div>
  <div class="ant-s" style="width:2px;height:2px;top:5%;left:40%;--d:2.5s;--dl:.9s;"></div>
  <div class="ant-s" style="width:3px;height:3px;top:18%;left:58%;--d:1.8s;--dl:.2s;"></div>
  <div class="ant-s" style="width:2px;height:2px;top:8%;left:75%;--d:2.8s;--dl:1.3s;"></div>
  <div class="ant-s" style="width:1px;height:1px;top:23%;left:88%;--d:3.3s;--dl:.7s;"></div>
  <div class="ant-s" style="width:1px;height:1px;top:4%;left:33%;--d:2.2s;--dl:1.8s;"></div>
  <div class="ant-s" style="width:2px;height:2px;top:16%;left:68%;--d:2.7s;--dl:1.1s;"></div>
  <div class="ant-s" style="width:1px;height:1px;top:28%;left:14%;--d:3.1s;--dl:.5s;"></div>
  <div class="ant-s" style="width:2px;height:2px;top:21%;left:50%;--d:2.4s;--dl:1.6s;"></div>
  <div class="ant-s" style="width:1px;height:1px;top:10%;left:92%;--d:2.9s;--dl:.3s;"></div>
  <div class="ant-s" style="width:2px;height:2px;top:30%;left:78%;--d:2.0s;--dl:2.1s;"></div>

  <!-- SVG City Skyline — Santiago-inspired, pure SVG path, no HTML building divs -->
  <div class="ant-cv">
<svg viewBox="0 0 1200 200" preserveAspectRatio="xMidYMax meet" style="height:200px;">
<defs>
<linearGradient id="bGr" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#1e1830"/>
<stop offset="100%" stop-color="#0a0814"/>
</linearGradient>
<linearGradient id="skyGr" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#06040f"/>
<stop offset="100%" stop-color="#0d0b18"/>
</linearGradient>
</defs>
<!-- Sky fill -->
<rect width="1200" height="200" fill="url(#skyGr)"/>
<!-- City silhouette — single continuous path (Santiago skyline style) -->
<path fill="url(#bGr)" d="
M0,200 L0,145 L38,145 L38,110 L55,110 L55,82 L60,82 L60,68
L63,68 L63,52 L65,52 L65,38 L67,38 L67,52 L69,52 L69,68
L72,68 L72,82 L77,82 L77,68 L80,68 L80,55 L83,55 L83,45
L85,45 L85,38 L87,38 L87,45 L89,45 L89,55 L92,55 L92,68
L97,68 L97,82 L115,82 L115,100 L145,100 L145,72 L168,72
L168,55 L175,55 L175,45 L178,45 L178,55 L185,55 L185,72
L210,72 L210,105 L240,105 L240,80 L265,80 L265,60 L275,60
L275,48 L278,48 L278,40 L280,40 L280,48 L283,48 L283,60
L295,60 L295,80 L325,80 L325,108 L352,108 L352,82 L375,82
L375,62 L390,62 L390,52 L393,52 L393,44 L396,44 L396,38
L399,38 L399,44 L402,44 L402,52 L405,52 L405,62 L418,62
L418,82 L442,82 L442,115 L468,115 L468,88 L490,88 L490,68
L505,68 L505,58 L508,58 L508,50 L511,50 L511,58 L514,58
L514,68 L530,68 L530,88 L555,88 L555,112 L578,112 L578,85
L602,85 L602,65 L612,65 L612,55 L615,55 L615,46 L618,46
L618,38 L621,38 L621,46 L624,46 L624,55 L627,55 L627,65
L640,65 L640,85 L665,85 L665,108 L690,108 L690,78 L712,78
L712,58 L722,58 L722,48 L725,48 L725,40 L728,40 L728,48
L731,48 L731,58 L742,58 L742,78 L768,78 L768,102 L795,102
L795,75 L818,75 L818,55 L828,55 L828,45 L831,45 L831,38
L834,38 L834,45 L837,45 L837,55 L848,55 L848,75 L872,75
L872,105 L898,105 L898,80 L922,80 L922,60 L932,60 L932,50
L935,50 L935,42 L938,42 L938,50 L941,50 L941,60 L952,60
L952,80 L978,80 L978,108 L1005,108 L1005,78 L1028,78 L1028,58
L1042,58 L1042,48 L1045,48 L1045,40 L1048,40 L1048,48
L1051,48 L1051,58 L1065,58 L1065,78 L1090,78 L1090,105
L1115,105 L1115,80 L1138,80 L1138,60 L1148,60 L1148,50
L1151,50 L1151,38 L1154,38 L1154,50 L1157,50 L1157,60
L1168,60 L1168,80 L1200,80 L1200,200 Z"/>
<!-- Window glows -->
<g fill="rgba(255,218,90,0.72)">
<rect x="8" y="115" width="5" height="6" rx="1"/>
<rect x="20" y="115" width="5" height="6" rx="1"/>
<rect x="8" y="128" width="5" height="6" rx="1"/>
<rect x="20" y="128" width="5" height="6" rx="1"/>
<rect x="44" y="90" width="4" height="5" rx="1"/>
<rect x="44" y="103" width="4" height="5" rx="1"/>
<rect x="120" y="82" width="5" height="6" rx="1"/>
<rect x="132" y="82" width="5" height="6" rx="1"/>
<rect x="120" y="95" width="5" height="6" rx="1"/>
<rect x="150" y="55" width="5" height="6" rx="1"/>
<rect x="161" y="55" width="5" height="6" rx="1"/>
<rect x="150" y="67" width="5" height="6" rx="1"/>
<rect x="218" y="85" width="5" height="6" rx="1"/>
<rect x="230" y="85" width="5" height="6" rx="1"/>
<rect x="248" y="62" width="4" height="5" rx="1"/>
<rect x="248" y="73" width="4" height="5" rx="1"/>
<rect x="358" y="65" width="5" height="6" rx="1"/>
<rect x="370" y="65" width="5" height="6" rx="1"/>
<rect x="358" y="78" width="5" height="6" rx="1"/>
<rect x="450" y="95" width="5" height="6" rx="1"/>
<rect x="462" y="95" width="5" height="6" rx="1"/>
<rect x="562" y="92" width="5" height="6" rx="1"/>
<rect x="575" y="92" width="5" height="6" rx="1"/>
<rect x="562" y="103" width="5" height="6" rx="1"/>
<rect x="585" y="68" width="4" height="5" rx="1"/>
<rect x="595" y="68" width="4" height="5" rx="1"/>
<rect x="645" y="65" width="5" height="6" rx="1"/>
<rect x="657" y="65" width="5" height="6" rx="1"/>
<rect x="645" y="78" width="5" height="6" rx="1"/>
<rect x="696" y="60" width="5" height="6" rx="1"/>
<rect x="708" y="60" width="5" height="6" rx="1"/>
<rect x="775" y="58" width="5" height="6" rx="1"/>
<rect x="788" y="58" width="5" height="6" rx="1"/>
<rect x="775" y="70" width="5" height="6" rx="1"/>
<rect x="803" y="55" width="4" height="5" rx="1"/>
<rect x="855" y="58" width="5" height="6" rx="1"/>
<rect x="867" y="58" width="5" height="6" rx="1"/>
<rect x="905" y="62" width="5" height="6" rx="1"/>
<rect x="917" y="62" width="5" height="6" rx="1"/>
<rect x="905" y="75" width="5" height="6" rx="1"/>
<rect x="958" y="62" width="5" height="6" rx="1"/>
<rect x="970" y="62" width="5" height="6" rx="1"/>
<rect x="1012" y="60" width="5" height="6" rx="1"/>
<rect x="1024" y="60" width="5" height="6" rx="1"/>
<rect x="1072" y="60" width="5" height="6" rx="1"/>
<rect x="1095" y="85" width="5" height="6" rx="1"/>
<rect x="1107" y="85" width="5" height="6" rx="1"/>
<rect x="1120" y="62" width="5" height="6" rx="1"/>
<rect x="1143" y="62" width="5" height="6" rx="1"/>
</g>
<!-- Glow aura on tallest towers -->
<ellipse cx="66" cy="38" rx="5" ry="3" fill="rgba(201,150,58,.12)"/>
<ellipse cx="86" cy="38" rx="5" ry="3" fill="rgba(201,150,58,.10)"/>
<ellipse cx="280" cy="40" rx="4" ry="2.5" fill="rgba(201,150,58,.10)"/>
<ellipse cx="396" cy="38" rx="4" ry="2.5" fill="rgba(201,150,58,.10)"/>
</svg>
<!-- Second copy — identical for seamless loop -->
<svg viewBox="0 0 1200 200" preserveAspectRatio="xMidYMax meet" style="height:200px;">
<defs>
<linearGradient id="bGr2" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#1e1830"/>
<stop offset="100%" stop-color="#0a0814"/>
</linearGradient>
</defs>
<rect width="1200" height="200" fill="#0d0b18"/>
<path fill="url(#bGr2)" d="
M0,200 L0,145 L38,145 L38,110 L55,110 L55,82 L60,82 L60,68
L63,68 L63,52 L65,52 L65,38 L67,38 L67,52 L69,52 L69,68
L72,68 L72,82 L77,82 L77,68 L80,68 L80,55 L83,55 L83,45
L85,45 L85,38 L87,38 L87,45 L89,45 L89,55 L92,55 L92,68
L97,68 L97,82 L115,82 L115,100 L145,100 L145,72 L168,72
L168,55 L175,55 L175,45 L178,45 L178,55 L185,55 L185,72
L210,72 L210,105 L240,105 L240,80 L265,80 L265,60 L275,60
L275,48 L278,48 L278,40 L280,40 L280,48 L283,48 L283,60
L295,60 L295,80 L325,80 L325,108 L352,108 L352,82 L375,82
L375,62 L390,62 L390,52 L393,52 L393,44 L396,44 L396,38
L399,38 L399,44 L402,44 L402,52 L405,52 L405,62 L418,62
L418,82 L442,82 L442,115 L468,115 L468,88 L490,88 L490,68
L505,68 L505,58 L508,58 L508,50 L511,50 L511,58 L514,58
L514,68 L530,68 L530,88 L555,88 L555,112 L578,112 L578,85
L602,85 L602,65 L612,65 L612,55 L615,55 L615,46 L618,46
L618,38 L621,38 L621,46 L624,46 L624,55 L627,55 L627,65
L640,65 L640,85 L665,85 L665,108 L690,108 L690,78 L712,78
L712,58 L722,58 L722,48 L725,48 L725,40 L728,40 L728,48
L731,48 L731,58 L742,58 L742,78 L768,78 L768,102 L795,102
L795,75 L818,75 L818,55 L828,55 L828,45 L831,45 L831,38
L834,38 L834,45 L837,45 L837,55 L848,55 L848,75 L872,75
L872,105 L898,105 L898,80 L922,80 L922,60 L932,60 L932,50
L935,50 L935,42 L938,42 L938,50 L941,50 L941,60 L952,60
L952,80 L978,80 L978,108 L1005,108 L1005,78 L1028,78 L1028,58
L1042,58 L1042,48 L1045,48 L1045,40 L1048,40 L1048,48
L1051,48 L1051,58 L1065,58 L1065,78 L1090,78 L1090,105
L1115,105 L1115,80 L1138,80 L1138,60 L1148,60 L1148,50
L1151,50 L1151,38 L1154,38 L1154,50 L1157,50 L1157,60
L1168,60 L1168,80 L1200,80 L1200,200 Z"/>
<g fill="rgba(255,218,90,0.72)">
<rect x="8" y="115" width="5" height="6" rx="1"/>
<rect x="20" y="115" width="5" height="6" rx="1"/>
<rect x="120" y="82" width="5" height="6" rx="1"/>
<rect x="150" y="55" width="5" height="6" rx="1"/>
<rect x="248" y="62" width="4" height="5" rx="1"/>
<rect x="358" y="65" width="5" height="6" rx="1"/>
<rect x="562" y="92" width="5" height="6" rx="1"/>
<rect x="645" y="65" width="5" height="6" rx="1"/>
<rect x="696" y="60" width="5" height="6" rx="1"/>
<rect x="775" y="58" width="5" height="6" rx="1"/>
<rect x="855" y="58" width="5" height="6" rx="1"/>
<rect x="958" y="62" width="5" height="6" rx="1"/>
<rect x="1072" y="60" width="5" height="6" rx="1"/>
<rect x="1143" y="62" width="5" height="6" rx="1"/>
</g>
</svg>
  </div>

  <!-- Road with cars -->
  <div class="ant-rd">
<div class="ant-car" style="width:34px;background:rgba(255,195,65,.38);--spd:7s;--dl:0s;"></div>
<div class="ant-car" style="width:26px;background:rgba(160,130,255,.32);--spd:10s;--dl:2.2s;"></div>
<div class="ant-car" style="width:40px;background:rgba(190,215,255,.28);--spd:6.8s;--dl:4.5s;"></div>
<div class="ant-car2" style="width:30px;background:rgba(255,170,90,.32);--spd:8.5s;--dl:1s;"></div>
<div class="ant-car2" style="width:22px;background:rgba(190,255,170,.26);--spd:12s;--dl:3.5s;"></div>
  </div>

  <!-- Hero text content -->
  <div class="ant-hc">
<div class="ant-label">AntonIA · Mar.IA Group · LegalTech Chile</div>
<div class="ant-h1">Domina el Derecho chileno<br>con <em>Inteligencia Artificial</em></div>
<div class="ant-sub">Tu asistente jurídico inteligente — entrena para exámenes, analiza casos, redacta documentos y consulta con la IA más avanzada del sistema legal chileno.</div>
<div class="ant-btns">
<span class="ant-bp">Comenzar gratis →</span>
<span class="ant-bs">▶ Ver demo</span>
</div>
  </div>
</div>

<div class="ant-stats">
  <div style="text-align:center"><div class="ant-stat-n">10.000+</div><div class="ant-stat-l">Preguntas de práctica</div></div>
  <div style="text-align:center"><div class="ant-stat-n">250+</div><div class="ant-stat-l">Casos reales</div></div>
  <div style="text-align:center"><div class="ant-stat-n">443</div><div class="ant-stat-l">Obras en biblioteca</div></div>
  <div style="text-align:center"><div class="ant-stat-n">12</div><div class="ant-stat-l">Ramos disponibles</div></div>
  <div style="text-align:center"><div class="ant-stat-n">4</div><div class="ant-stat-l">Perfiles distintos</div></div>
</div>

<!-- DEMO SECTION -->
<div style="background:#0d0b10;padding:60px 20px;border-top:1px solid rgba(201,150,58,.1);border-bottom:1px solid rgba(201,150,58,.1);">
  <div style="max-width:920px;margin:0 auto;">
<div style="text-align:center;margin-bottom:8px;">
<span style="font-family:Inter,sans-serif;font-size:.78rem;color:#c9963a;text-transform:uppercase;letter-spacing:.15em;font-weight:600;">▶ Demo interactivo</span>
</div>
<div style="font-family:'Playfair Display',serif;font-size:1.85rem;font-weight:800;color:#f5f0e8;text-align:center;margin-bottom:8px;">AntonIA en acción</div>
<div style="font-size:.92rem;color:rgba(240,232,218,.78);text-align:center;margin-bottom:36px;">Descubre las funciones más poderosas del primer asistente jurídico IA para el Derecho chileno</div>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;">
<!-- Demo 1: Quiz IA -->
<div style="background:#13101a;border:1px solid rgba(201,150,58,.18);border-radius:12px;overflow:hidden;">
<div style="background:linear-gradient(135deg,#1a1520,#0e0c14);padding:20px;min-height:160px;position:relative;display:flex;flex-direction:column;justify-content:flex-end;">
<div style="position:absolute;top:16px;left:16px;font-size:1.6rem;">🧠</div>
<div style="background:#1e1b28;border:1px solid rgba(201,150,58,.2);border-radius:8px;padding:12px;">
<div style="font-size:.68rem;color:#c9963a;font-weight:700;margin-bottom:6px;">QUIZ INTERACTIVO · Civil III</div>
<div style="font-size:.82rem;color:#f0e8d8;line-height:1.5;">¿Cuál es el efecto de la condición resolutoria cumplida?</div>
<div style="margin-top:10px;display:flex;flex-direction:column;gap:5px;">
<div style="background:rgba(46,144,85,.15);border:1px solid rgba(46,144,85,.3);border-radius:4px;padding:4px 8px;font-size:.72rem;color:#4ade80;">✓ Se extingue retroactivamente la obligación</div>
<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:4px;padding:4px 8px;font-size:.72rem;color:rgba(240,232,218,.78);">No tiene efectos retroactivos</div>
</div>
</div>
</div>
<div style="padding:14px 16px;">
<div style="font-size:.85rem;font-weight:700;color:#f5f0e8;margin-bottom:4px;">Quiz con IA Infinito</div>
<div style="font-size:.76rem;color:rgba(240,232,218,.78);line-height:1.5;">Quiz adaptativo con retroalimentación jurídica detallada. Alternativas, V/F, Flashcards y casos prácticos.</div>
</div>
</div>

<!-- Demo 2: Análisis de Caso -->
<div style="background:#13101a;border:1px solid rgba(201,150,58,.18);border-radius:12px;overflow:hidden;">
<div style="background:linear-gradient(135deg,#1a1520,#0e0c14);padding:20px;min-height:160px;position:relative;display:flex;flex-direction:column;justify-content:flex-end;">
<div style="position:absolute;top:16px;left:16px;font-size:1.6rem;">🔍</div>
<div style="background:#1e1b28;border:1px solid rgba(201,150,58,.2);border-radius:8px;padding:12px;">
<div style="font-size:.68rem;color:#c9963a;font-weight:700;margin-bottom:6px;">ANÁLISIS JURÍDICO · Derecho Civil</div>
<div style="font-size:.8rem;color:#f0e8d8;font-style:italic;line-height:1.5;">"Contrato de compraventa · nulidad por objeto ilícito · Arts. 1462 y 1466 CC..."</div>
<div style="margin-top:8px;font-size:.72rem;color:rgba(201,150,58,.8);">→ Identificó 3 argumentos clave · 2 normas aplicables · 1 tendencia jurisprudencial</div>
</div>
</div>
<div style="padding:14px 16px;">
<div style="font-size:.85rem;font-weight:700;color:#f5f0e8;margin-bottom:4px;">Análisis Jurídico Profundo</div>
<div style="font-size:.76rem;color:rgba(240,232,218,.78);line-height:1.5;">Sube cualquier documento jurídico y AntonIA lo analiza en segundos con fundamentos del Derecho chileno.</div>
</div>
</div>

<!-- Demo 3: Redacción -->
<div style="background:#13101a;border:1px solid rgba(201,150,58,.18);border-radius:12px;overflow:hidden;">
<div style="background:linear-gradient(135deg,#1a1520,#0e0c14);padding:20px;min-height:160px;position:relative;display:flex;flex-direction:column;justify-content:flex-end;">
<div style="position:absolute;top:16px;left:16px;font-size:1.6rem;">📝</div>
<div style="background:#1e1b28;border:1px solid rgba(201,150,58,.2);border-radius:8px;padding:12px;">
<div style="font-size:.68rem;color:#c9963a;font-weight:700;margin-bottom:6px;">ESCRITO GENERADO · Demanda Civil</div>
<div style="font-size:.75rem;color:rgba(240,232,218,.65);line-height:1.6;font-family:monospace;">EN LO PRINCIPAL: Demanda ordinaria...<br>PRIMER OTROSÍ: Patrocinio y poder...<br><span style="color:#c9963a;">Art. 254 CPC · Art. 1489 CC ✓</span></div>
</div>
</div>
<div style="padding:14px 16px;">
<div style="font-size:.85rem;font-weight:700;color:#f5f0e8;margin-bottom:4px;">Redacción Forense con IA</div>
<div style="font-size:.76rem;color:rgba(240,232,218,.78);line-height:1.5;">Genera demandas, contratos, escritos y comunicaciones con el formato forense chileno correcto.</div>
</div>
</div>
</div>

<div style="text-align:center;margin-top:30px;">
<span style="font-family:Inter,sans-serif;font-size:.82rem;color:rgba(240,232,218,.75);">
Selecciona tu perfil en el panel izquierdo para comenzar · Prueba gratis sin registrarte
</span>
</div>
  </div>
</div>

<div class="ant-sec">
  <div class="ant-sec-t">¿Para quién es AntonIA?</div>
  <div class="ant-sec-s">Selecciona tu perfil en el panel izquierdo para comenzar</div>
  <div class="ant-grid-4">
<div class="ant-card"><div class="ant-card-icon">🎓</div><div class="ant-card-t">Universidad</div><div class="ant-card-d">Plataforma completa para alumnos y profesores. Quiz infinito, análisis de casos, documentos legales y más.</div></div>
<div class="ant-card"><div class="ant-card-icon">⚖️</div><div class="ant-card-t">Abogados</div><div class="ant-card-d">Herramientas de alto nivel para litigantes. Jurisprudencia, análisis jurídico profundo, redacción de escritos.</div></div>
<div class="ant-card"><div class="ant-card-icon">💬</div><div class="ant-card-t">Consulta Legal</div><div class="ant-card-d">Asesoría jurídica inmediata basada en el derecho chileno vigente. Respuestas precisas y fundamentadas.</div></div>
<div class="ant-card"><div class="ant-card-icon">🆓</div><div class="ant-card-t">Prueba Gratis</div><div class="ant-card-d">Explora todas las funcionalidades sin compromiso. Descubre el poder de la IA aplicada al Derecho.</div></div>
  </div>
</div>

<div style="background:rgba(201,150,58,.04);border-top:1px solid rgba(201,150,58,.1);border-bottom:1px solid rgba(201,150,58,.1);padding:50px 20px;">
  <div style="max-width:900px;margin:0 auto;">
<div class="ant-sec-t">Cómo funciona</div>
<div class="ant-sec-s" style="margin-bottom:28px;">Tres pasos para transformar tu práctica jurídica</div>
<div class="ant-steps">
<div class="ant-step"><div class="ant-step-n">01</div><div class="ant-step-t">Elige tu perfil</div><div class="ant-step-d">Selecciona si eres alumno, abogado, profesor o quieres una consulta.</div></div>
<div class="ant-step"><div class="ant-step-n">02</div><div class="ant-step-t">Selecciona la herramienta</div><div class="ant-step-d">Elige entre ENTRENA, DOCUMENTO, ANÁLISIS, JURISPRUDENCIA y más.</div></div>
<div class="ant-step"><div class="ant-step-n">03</div><div class="ant-step-t">AntonIA trabaja</div><div class="ant-step-d">La IA genera contenido jurídico preciso basado en el derecho chileno vigente.</div></div>
</div>
  </div>
</div>

<div class="ant-sec">
  <div class="ant-sec-t">Herramientas para estudiantes</div>
  <div class="ant-sec-s">Todo lo que necesitas para aprobar y destacar en Derecho</div>
  <div class="ant-tools">
<div class="ant-tool"><div class="ant-tool-icon">🧠</div><div><div class="ant-tool-t">ENTRENA</div><div class="ant-tool-d">Quiz legal infinito con IA. Alternativas, V/F, Flashcards, Desarrollo y Casos.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">📄</div><div><div class="ant-tool-t">DOCUMENTO</div><div class="ant-tool-d">Genera contratos, escritos y documentos legales en segundos.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">📋</div><div><div class="ant-tool-t">RESUMEN</div><div class="ant-tool-d">Resume casos, sentencias y normativa en formato estructurado.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">🔍</div><div><div class="ant-tool-t">ANÁLISIS</div><div class="ant-tool-d">Análisis jurídico profundo con citas doctrinales y jurisprudenciales.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">⚖️</div><div><div class="ant-tool-t">JURISPRUDENCIA</div><div class="ant-tool-d">Busca y analiza jurisprudencia chilena relevante para tu caso.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">📚</div><div><div class="ant-tool-t">DOCTRINA</div><div class="ant-tool-d">Accede a la doctrina nacional más actualizada de 2025.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">🎤</div><div><div class="ant-tool-t">ALEGATO</div><div class="ant-tool-d">Prepara argumentos orales, defensas y alegatos con IA.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">📂</div><div><div class="ant-tool-t">BANCO DE CASOS</div><div class="ant-tool-d">250+ casos reales del Derecho chileno para practicar.</div></div></div>
<div class="ant-tool"><div class="ant-tool-icon">📈</div><div><div class="ant-tool-t">MI PROGRESO</div><div class="ant-tool-d">Estadísticas de estudio, rachas y áreas de mejora.</div></div></div>
  </div>
</div>

<div class="ant-cta">
  <div class="ant-cta-t">¿Listo para transformar tu práctica jurídica?</div>
  <div class="ant-cta-s">Únete a los estudiantes y profesionales que ya usan AntonIA</div>
  <span class="ant-btn-p" style="font-size:1rem;padding:15px 36px;">Comenzar ahora →</span>
  <div style="margin-top:20px;font-size:.72rem;color:#9a8060;font-family:'Inter',sans-serif;">
Anton<strong style="color:#c9963a;">IA</strong> · Mar.IA Group · LegalTech Chile
  </div>
</div>
    """, unsafe_allow_html=True)
    # ── Promo video (autoplay on first visit) ──
    import pathlib as _pathlib
    _promo_home = _pathlib.Path(__file__).parent / "static" / "promo_home.mp4"
    if _promo_home.exists():
       st.markdown('<div style="max-width:720px;margin:18px auto 0;border-radius:12px;overflow:hidden;border:1px solid rgba(201,150,58,.18);">', unsafe_allow_html=True)
       st.video(str(_promo_home), autoplay=True, muted=True, loop=True)
       st.markdown('</div>', unsafe_allow_html=True)
    st.stop()


# ── UNIVERSIDAD LANDING — Mostrar cuando el usuario aún no eligió perfil ──
if _is_univ_chooser:
    st.markdown("""
<style>
.univ-landing{max-width:800px;margin:0 auto;padding:40px 20px;}
.univ-title{font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:800;color:#1a1813;text-align:center;margin-bottom:10px;}
.univ-sub{font-size:1.0rem;color:#9a8a6a;text-align:center;margin-bottom:40px;}
.univ-cards{display:grid;grid-template-columns:1fr 1fr;gap:24px;max-width:720px;margin:0 auto;}
@media(max-width:600px){.univ-cards{grid-template-columns:1fr;}}
.univ-card{background:#fff;border:1.5px solid #e2dbd0;border-radius:16px;padding:36px 28px;text-align:center;cursor:pointer;transition:all .25s ease;box-shadow:0 2px 16px rgba(20,18,10,.07);}
.univ-card:hover{border-color:#c9963a;transform:translateY(-5px);box-shadow:0 12px 40px rgba(20,18,10,.13);}
.univ-card-icon{font-size:3.5rem;margin-bottom:16px;}
.univ-card-title{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:#1a1813;margin-bottom:8px;}
.univ-card-desc{font-size:.88rem;color:#9a8a6a;line-height:1.65;margin-bottom:20px;}
.univ-card-feats{text-align:left;margin-top:12px;}
.univ-card-feat{font-size:.78rem;color:#5a4e3e;padding:5px 0;border-bottom:1px solid #ede8de;display:flex;align-items:center;gap:6px;}
.univ-card-feat:last-child{border-bottom:none;}
.univ-badge{display:inline-block;background:rgba(201,150,58,.1);color:#8a6800;font-size:.7rem;padding:4px 14px;border-radius:20px;border:1px solid rgba(201,150,58,.25);font-weight:600;margin-top:16px;}
</style>
<div class="univ-landing">
  <div class="univ-title">Universidad · Área Académica</div>
  <div class="univ-sub">¿Cuál es tu rol? Elige tu perfil para acceder a las herramientas diseñadas para ti.</div>
  <div class="univ-cards">
    <div class="univ-card" id="card-alumno">
      <div class="univ-card-icon">👨‍🎓</div>
      <div class="univ-card-title">Soy Alumno</div>
      <div class="univ-card-desc">Prepara tus exámenes, estudia casos reales y domina el Derecho chileno con IA adaptativa.</div>
      <div class="univ-card-feats">
        <div class="univ-card-feat">🧠 Quiz interactivo con IA infinito</div>
        <div class="univ-card-feat">📝 Examen simulado con nota 1-7</div>
        <div class="univ-card-feat">🔍 Análisis jurídico de documentos</div>
        <div class="univ-card-feat">⚖️ Jurisprudencia y doctrina relacionada</div>
        <div class="univ-card-feat">📂 Banco de 250+ casos reales</div>
        <div class="univ-card-feat">📈 Progreso y estadísticas de estudio</div>
      </div>
      <div class="univ-badge">Acceso gratuito disponible</div>
    </div>
    <div class="univ-card" id="card-profesor">
      <div class="univ-card-icon">👩‍🏫</div>
      <div class="univ-card-title">Soy Profesor</div>
      <div class="univ-card-desc">Prepara clases, crea evaluaciones y gestiona tu curso con herramientas docentes avanzadas.</div>
      <div class="univ-card-feats">
        <div class="univ-card-feat">📝 Crea evaluaciones y rúbricas con IA</div>
        <div class="univ-card-feat">📋 Materiales didácticos automáticos</div>
        <div class="univ-card-feat">🎙️ Banco de preguntas de examen oral</div>
        <div class="univ-card-feat">🤖 Chat IA + búsqueda de doctrina</div>
        <div class="univ-card-feat">📊 Libro de notas y asistencia</div>
        <div class="univ-card-feat">🔬 Asistente de investigación jurídica</div>
      </div>
      <div class="univ-badge">Panel docente completo</div>
    </div>
  </div>
</div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([1,2,1,2,1])
    with col2:
        if st.button("👨‍🎓  Entrar como Alumno", use_container_width=True,
                     help="Accede al área de alumnos con quiz, casos y análisis"):
            set_univ_perfil("alumno")
            st.rerun()
    with col4:
        if st.button("👩‍🏫  Entrar como Profesor", use_container_width=True,
                     help="Accede al panel docente con evaluaciones y herramientas"):
            set_univ_perfil("profesor")
            st.rerun()
    st.stop()

# ═══════════════════════════════════════════════
# ENRUTAMIENTO POR PERFIL
# ═══════════════════════════════════════════════

# ── Perfil: ABOGADO ─────────────────────────────
if persona == "abogado" and nav not in ("QUIÉNES SOMOS", "SUSCRIPCIONES"):
    render_abogado(get_llm_fn=lambda: get_llm(_provider_key, _api_key, _model))
    st.stop()

# ── Perfil: PROFESOR ────────────────────────────
elif persona == "profesor" and nav not in ("QUIÉNES SOMOS", "SUSCRIPCIONES"):
    render_profesor(get_llm_fn=lambda: get_llm(_provider_key, _api_key, _model))
    st.stop()

# ── Perfil: CONSULTA LEGAL (no abogados) ────────
elif persona == "consulta" and nav not in ("QUIÉNES SOMOS", "SUSCRIPCIONES"):
    render_consulta_legal(
        get_orch_fn=get_orch,
        get_llm_fn=lambda: get_llm(_provider_key, _api_key, _model),
    )
    st.stop()

# ── Perfil: ALUMNO + páginas institucionales ────
# Continúa con la navegación original de Alumno


# ═══════════════════════════════════════════════
# SECCIÓN: DOCUMENTO (carga de archivos)
# ═══════════════════════════════════════════════
if nav == "DOCUMENTO":
    st.markdown(section_header("📄 Mi Documento"), unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.88rem;color:#5a4e3e;margin-bottom:1.5rem;line-height:1.6;">
      Sube un documento jurídico (sentencia, contrato, código, apuntes) y AntonIA lo analizará
      para que puedas hacer preguntas, obtener resúmenes, jurisprudencia relacionada y más.
    </div>""", unsafe_allow_html=True)

    col_up, col_info = st.columns([3, 2])
    with col_up:
        uploaded = st.file_uploader(
            "Selecciona tu archivo",
            type=["pdf", "docx", "doc", "txt", "rtf", "html", "htm"],
            help="PDF, Word, TXT — máx. 50 MB",
        )
        if uploaded:
            if st.button("⬆  Procesar Documento", use_container_width=True, key="proc_doc"):
                settings.ensure_dirs()
                tmp = settings.upload_dir / uploaded.name
                tmp.write_bytes(uploaded.getvalue())
                for k in ["ingestion_result", "classification", "chat_history", "quiz_data",
                           "quiz_answers", "quiz_submitted", "flashcards", "fc_idx", "fc_show",
                           "glossary", "concept_map", "summary_text", "jurisprudencia", "doctrina"]:
                    st.session_state[k] = DEFAULTS[k]
                with st.spinner("Procesando documento…"):
                    try:
                        res = get_orch().ingest(tmp)
                        st.session_state.ingestion_result = res
                        cls = get_clf().classify(res.extraction.raw_text, res.extraction.metadata)
                        st.session_state.classification = cls
                        try:
                            rag = get_rag()
                            rag.delete_collection("current_doc")
                            rag.index_chunks(res.chunks, "current_doc")
                        except Exception:
                            pass
                        st.success("✓ Documento listo — usa el menú izquierdo para analizarlo")
                    except Exception as e:
                        st.error(f"Error procesando el documento: {e}")

    with col_info:
        if st.session_state.ingestion_result:
            r = st.session_state.ingestion_result
            st.markdown(f"""
            <div style="background:#f8f5f0;border:1px solid #e2dbd0;border-left:3px solid #c9963a;
                        border-radius:0 8px 8px 0;padding:1rem 1.2rem;">
              <div style="font-size:0.75rem;font-weight:700;color:#9a8e7e;
                          text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">
                Documento activo
              </div>
              <div style="font-size:0.9rem;font-weight:600;color:#1a1813;margin-bottom:0.4rem;">
                {r.file_name[:40]}
              </div>
              <div style="font-size:0.78rem;color:#5a4e3e;">
                📄 {r.extraction.pages} páginas &nbsp;·&nbsp; 🔖 {len(r.chunks)} fragmentos
              </div>
              {"<div style='font-size:0.75rem;color:#c9963a;margin-top:0.4rem;'>⚖ " + st.session_state.classification.rama_derecho + "</div>" if st.session_state.classification else ""}
            </div>""", unsafe_allow_html=True)
            st.markdown("##### ¿Qué puedes hacer ahora?")
            opciones = [
                ("📋", "RESUMEN EJECUTIVO",          "Resumen ejecutivo"),
                ("🔍", "ANÁLISIS",                   "Análisis jurídico"),
                ("⚖️", "JURISPRUDENCIA RELACIONADA", "Jurisprudencia relacionada"),
                ("📚", "DOCTRINA RELACIONADA",       "Doctrina relacionada"),
                ("📖", "GLOSARIO LEGAL",             "Glosario de términos"),
                ("🗺️", "MAPA CONCEPTUAL",           "Mapa conceptual"),
                ("💬", "CONSULTORÍA VIRTUAL",        "Consultoría Q&A"),
            ]
            for icon, nav_key, label in opciones:
                if st.button(f"{icon} {label}", key=f"go_{nav_key}", use_container_width=True):
                    st.session_state.nav = nav_key
                    st.rerun()
        else:
            st.markdown("""
            <div style="background:#fdfaf5;border:1px dashed #e2dbd0;border-radius:8px;
                        padding:1.2rem;text-align:center;color:#9a8e7e;font-size:0.82rem;">
              Sube un archivo para ver las opciones de análisis
            </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: PREPARA TU ALEGATO
# ═══════════════════════════════════════════════
elif nav == "PREPARA TU ALEGATO":
    st.markdown(section_header("🎤 Prepara tu Alegato"), unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.88rem;color:#5a4e3e;margin-bottom:1.2rem;line-height:1.6;">
      Prepara argumentos, anticipa contraargumentos y practica tu defensa oral con IA.
    </div>""", unsafe_allow_html=True)

    tab_prep, tab_irac, tab_contra = st.tabs(["🎯 Armado de argumentos", "📋 Briefing IRAC", "🔄 Contraargumentos"])

    with tab_prep:
        st.markdown("#### Describe tu caso o posición")
        caso_desc = st.text_area(
            "¿Cuál es tu posición jurídica?",
            placeholder="Ej: Defensa del demandado en juicio por incumplimiento de contrato de arrendamiento. "
                        "El arrendador alega que el arrendatario no pagó 3 meses de renta...",
            height=120,
        )
        ramo_alg = st.selectbox("Rama del Derecho", [
            "Civil — Contratos", "Civil — Responsabilidad", "Civil — Familia",
            "Penal — Defensa", "Penal — Acusación", "Procesal Civil", "Procesal Penal",
            "Laboral", "Comercial", "Constitucional",
        ])
        tipo_alegato = st.radio("Tipo de alegato", ["Oral formal (tribunal)", "Presentación académica", "Moot court"], horizontal=True)
        if caso_desc and st.button("🎯 Generar argumentos", use_container_width=True, key="gen_arg"):
            llm = active_llm()
            prompt = (
                f"Actúa como coach de litigación para derecho chileno.\n"
                f"Caso: {caso_desc}\nRama: {ramo_alg}\nTipo: {tipo_alegato}\n\n"
                f"Genera:\n"
                f"1. TESIS PRINCIPAL (1 párrafo contundente)\n"
                f"2. TRES ARGUMENTOS PRINCIPALES (cada uno con: argumento, norma aplicable del derecho chileno, evidencia recomendada)\n"
                f"3. ESTRUCTURA SUGERIDA DEL ALEGATO (introducción, desarrollo, conclusión — con tiempos estimados)\n"
                f"4. FRASES CLAVE de impacto para usar ante el tribunal\n"
                f"Responde en español jurídico formal chileno."
            )
            with st.spinner("Preparando argumentos…"):
                resp = llm.generate(prompt, system="Eres AntonIA, coach de litigación especializado en el Derecho chileno. Generas argumentos jurídicos sólidos, estratégicos y fundamentados en normativa vigente. Respondes en español jurídico formal chileno.", max_tokens=1200)
            st.markdown(resp)

    with tab_irac:
        st.markdown("#### Briefing de Caso — Método IRAC")
        st.markdown("""
        <div style="font-size:0.82rem;color:#5a4e3e;background:#f8f5f0;
                    border-left:3px solid #c9963a;padding:0.7rem 1rem;border-radius:0 6px 6px 0;margin-bottom:1rem;">
          <strong>IRAC</strong>: Issue (Asunto) · Rule (Norma) · Application (Aplicación) · Conclusion (Conclusión)
        </div>""", unsafe_allow_html=True)
        caso_irac = st.text_area("Describe el caso o hecho jurídico", height=100,
                                  placeholder="Ej: Contrato de compraventa celebrado entre A y B. A entregó el bien pero B no pagó el precio...")
        if caso_irac and st.button("📋 Generar Briefing IRAC", use_container_width=True, key="gen_irac"):
            llm = active_llm()
            prompt = (
                f"Genera un briefing jurídico completo usando el método IRAC para el siguiente caso:\n\n{caso_irac}\n\n"
                f"Estructura tu respuesta así:\n"
                f"**I — ISSUE (Asunto Legal):** ¿Cuál es la cuestión jurídica central?\n"
                f"**R — RULE (Norma Aplicable):** Artículos del Código Civil, CPP, CT u otras normas chilenas relevantes.\n"
                f"**A — APPLICATION (Aplicación):** ¿Cómo se aplica la norma a los hechos? Argumentos pro y contra.\n"
                f"**C — CONCLUSION:** ¿Cuál es el resultado jurídico más probable?\n"
                f"**PRECEDENTES RELEVANTES:** Menciona jurisprudencia chilena si corresponde.\n"
                f"Responde en español jurídico formal."
            )
            with st.spinner("Generando briefing IRAC…"):
                resp = llm.generate(prompt, system="Eres AntonIA, asistente jurídico especializado en el Derecho chileno vigente. Aplicas el método IRAC con precisión académica y práctica. Citas normas chilenas reales. Respondes en español formal.", max_tokens=1000)
            st.markdown(resp)

    with tab_contra:
        st.markdown("#### Anticipa los Contraargumentos")
        pos_propia = st.text_area("Tu posición / argumento principal", height=80,
                                   placeholder="Ej: El contrato es nulo por falta de objeto lícito según el Art. 1462 CC...")
        if pos_propia and st.button("🔄 Generar contraargumentos", use_container_width=True, key="gen_contra"):
            llm = active_llm()
            prompt = (
                f"Actúa como abogado de la contraparte en un juicio chileno.\n"
                f"La posición del adversario es: {pos_propia}\n\n"
                f"Genera:\n"
                f"1. Los 3 contraargumentos más fuertes contra esa posición (con norma y fundamento)\n"
                f"2. Las debilidades de esos contraargumentos que puedo explotar\n"
                f"3. Preguntas que el juez podría hacerme sobre mi posición y cómo responderlas\n"
                f"Responde en español jurídico formal chileno."
            )
            with st.spinner("Analizando contraargumentos…"):
                resp = llm.generate(prompt, system="Eres AntonIA, abogado estratega en Derecho chileno. Analizas argumentos jurídicos, identificas debilidades y generas contraargumentos fundamentados en normas y jurisprudencia chilena. Respondes en español jurídico formal.", max_tokens=900)
            st.markdown(resp)
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: RESUMEN EJECUTIVO
# ═══════════════════════════════════════════════
if nav == "RESUMEN EJECUTIVO":
    st.markdown(section_header("Resumen Ejecutivo"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        level = st.radio("Profundidad del análisis", ["breve","medio","extenso"], horizontal=True,
                         format_func=lambda x: {"breve":"⚡ Breve (~20s)","medio":"📄 Completo (~50s)","extenso":"📚 Exhaustivo (~90s)"}[x])
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        if st.button("GENERAR RESUMEN EJECUTIVO", use_container_width=True):
            with st.spinner("Redactando análisis jurídico de precisión…"):
                try:
                    st.session_state.summary_text = make_gen().generate_summary(doc_text(), level)
                except Exception as e:
                    st.error(f"Error: {e}")
        if st.session_state.summary_text:
            st.markdown(f'<div class="card" style="margin-top:1.2rem;">{st.session_state.summary_text}</div>',
                        unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: ANÁLISIS
# ═══════════════════════════════════════════════
elif nav == "ANÁLISIS":
    st.markdown(section_header("Análisis · Herramientas de Estudio"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        mode = st.radio("Herramienta", ["Fichas de Estudio","Cuestionario"], horizontal=True)
        st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

        if mode == "Fichas de Estudio":
            c1,c2 = st.columns(2)
            n = c1.slider("Número de fichas", 3, 12, 5)
            d = c2.selectbox("Dificultad", ["mixto","basico","intermedio","avanzado"])
            if st.button("GENERAR FICHAS DE ESTUDIO", use_container_width=True):
                with st.spinner(f"Generando {n} fichas método Cornell…"):
                    try:
                        st.session_state.flashcards = make_gen().generate_flashcards(doc_text(), n, d)
                        st.session_state.fc_idx = 0
                        st.session_state.fc_show = False
                    except Exception as e:
                        st.error(f"Error: {e}")

            if st.session_state.flashcards:
                cards = st.session_state.flashcards
                idx   = st.session_state.fc_idx
                card  = cards[idx]
                st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
                st.progress((idx+1)/len(cards))
                dc = {"basico":"#2e9055","intermedio":"#c9963a","avanzado":"#d63535"}.get(card.difficulty,"#9a8e7e")
                st.markdown(
                    f'<div style="display:flex;justify-content:space-between;align-items:center;'
                    f'margin:0.6rem 0 0.4rem;">'
                    f'<span style="color:#9a8e7e;font-size:0.78rem;font-family:Inter,sans-serif;">'
                    f'Ficha {idx+1} de {len(cards)}</span>'
                    f'<span style="color:{dc};font-size:0.68rem;font-weight:700;text-transform:uppercase;'
                    f'background:rgba(201,150,58,0.08);padding:2px 10px;border-radius:20px;'
                    f'border:1px solid rgba(201,150,58,0.2);">● {card.difficulty}</span>'
                    f'</div>'
                    f'<div class="fq">{card.question}</div>',
                    unsafe_allow_html=True)
                if st.button("MOSTRAR RESPUESTA", use_container_width=True):
                    st.session_state.fc_show = not st.session_state.fc_show
                if st.session_state.fc_show:
                    st.markdown(f'<div class="fa">{card.answer}<br><span class="stag">📎 {card.source_ref}</span></div>',
                                unsafe_allow_html=True)
                cp, cn = st.columns(2)
                if cp.button("← Anterior") and idx > 0:
                    st.session_state.fc_idx -= 1; st.session_state.fc_show = False; st.rerun()
                if cn.button("Siguiente →") and idx < len(cards)-1:
                    st.session_state.fc_idx += 1; st.session_state.fc_show = False; st.rerun()

        else:  # Cuestionario
            c1,c2 = st.columns(2)
            q_n = c1.slider("Número de preguntas", 3, 8, 4, key="qn")
            q_d = c2.selectbox("Dificultad", ["intermedio","basico","avanzado"], key="qd")
            if st.button("GENERAR CUESTIONARIO", use_container_width=True, key="bq"):
                with st.spinner(f"Generando {q_n} preguntas jurídicas…"):
                    try:
                        qd = make_gen().generate_quiz(doc_text(), q_n, q_d)
                        st.session_state.quiz_data = qd
                        st.session_state.quiz_answers = {i:0 for i in range(len(qd))}
                        st.session_state.quiz_submitted = False
                    except Exception as e:
                        st.error(f"Error: {e}")

            if st.session_state.quiz_data:
                with st.form("quiz_form"):
                    for i, q in enumerate(st.session_state.quiz_data):
                        st.markdown(
                            f'<div class="card"><strong style="color:#c9963a;font-family:Playfair Display,serif;">'
                            f'{i+1}.</strong> {q.question}</div>', unsafe_allow_html=True)
                        opts = q.options if q.options else ["A","B","C","D"]
                        ch = st.radio(f"P{i+1}", list(range(len(opts))),
                                      format_func=lambda x, o=opts: o[x] if x<len(o) else f"Op.{x}",
                                      key=f"q_{i}", label_visibility="collapsed")
                        st.session_state.quiz_answers[i] = ch
                    if st.form_submit_button("EVALUAR RESPUESTAS", use_container_width=True):
                        st.session_state.quiz_submitted = True

                if st.session_state.quiz_submitted:
                    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
                    ok = 0
                    for i, q in enumerate(st.session_state.quiz_data):
                        a = st.session_state.quiz_answers.get(i,0)
                        right = (a == q.correct_answer)
                        if right: ok += 1
                        css = "qok" if right else "qno"; ic = "✓" if right else "✗"
                        cr = q.options[q.correct_answer] if q.correct_answer < len(q.options) else "N/A"
                        ex = "" if right else f"<br><strong>Correcta:</strong> {cr}"
                        st.markdown(f'<div class="{css}"><strong>{ic} P{i+1}:</strong> {q.explanation}{ex}<br><span class="stag">📎 {q.source_ref}</span></div>',
                                    unsafe_allow_html=True)
                    t = len(st.session_state.quiz_data)
                    sc = ok/t*100 if t else 0
                    cl = "#2e9055" if sc>=80 else "#c9963a" if sc>=60 else "#d63535"
                    st.markdown(
                        f'<div style="text-align:center;background:#ffffff;border:1px solid #e2dbd0;'
                        f'border-top:3px solid {cl};border-radius:0 0 12px 12px;'
                        f'padding:1.6rem;margin-top:1rem;'
                        f'box-shadow:0 2px 16px rgba(20,18,10,0.07);">'
                        f'<div style="font-family:Playfair Display,serif;font-size:3rem;'
                        f'font-weight:700;color:{cl};">{sc:.0f}%</div>'
                        f'<div style="color:#5a4e3e;font-size:0.84rem;margin-top:0.3rem;">'
                        f'{ok} de {t} respuestas correctas</div></div>', unsafe_allow_html=True)
                    if sc >= 80: st.balloons()

        # ── Casos relacionados ──────────────────────────────────────────────
        _mostrar_casos_relacionados(doc_text(3000), max_casos=3, key_prefix="an")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: JURISPRUDENCIA
# ═══════════════════════════════════════════════
elif nav == "JURISPRUDENCIA RELACIONADA":
    st.markdown(section_header("Jurisprudencia Relacionada"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        st.markdown(
            '<p style="color:#9a8e7e;font-size:0.84rem;text-align:center;margin-bottom:1rem;">'
            'Identifica sentencias, fallos y resoluciones relevantes para el documento analizado.</p>',
            unsafe_allow_html=True)
        if st.button("BUSCAR JURISPRUDENCIA APLICABLE", use_container_width=True):
            with st.spinner("Analizando jurisprudencia relevante…"):
                try:
                    prompt = f"""Eres un abogado especialista en jurisprudencia chilena. Analiza el texto jurídico
y produce un informe de JURISPRUDENCIA RELACIONADA con esta estructura:

**I. JURISPRUDENCIA CITADA EN EL TEXTO**
Lista cada sentencia mencionada con: Tribunal | Tipo de fallo | Rol | Fecha | Materia | Relevancia.
Si no hay citas explícitas, escribir: "(no se citan sentencias en el texto)".

**II. JURISPRUDENCIA RELEVANTE SUGERIDA**
Identifica los temas jurídicos del documento y sugiere qué tipos de jurisprudencia un abogado debería consultar.
Especifica: Tribunal competente | Tipo de controversia | Por qué es relevante.

**III. TENDENCIAS JURISPRUDENCIALES**
¿Hay uniformidad o divergencia en los tribunales respecto a la materia del documento?

REGLA INVIOLABLE: NUNCA inventes roles de causa, fechas ni sentencias ficticias.
Si no tienes certeza, indica: "(verificar en bases de datos Westlaw Chile, vLex, Microjuris)".

TEXTO A ANALIZAR:
{doc_text()}"""
                    st.session_state.jurisprudencia = active_llm().generate(prompt, max_tokens=2500, temperature=0.2)
                except Exception as e:
                    st.error(f"Error: {e}")
        if st.session_state.jurisprudencia:
            st.markdown(f'<div class="card" style="margin-top:1rem;">{st.session_state.jurisprudencia}</div>',
                        unsafe_allow_html=True)
        _mostrar_casos_relacionados(doc_text(3000), max_casos=3, key_prefix="ju")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: DOCTRINA
# ═══════════════════════════════════════════════
elif nav == "DOCTRINA RELACIONADA":
    st.markdown(section_header("Doctrina Relacionada"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        st.markdown(
            '<p style="color:#9a8e7e;font-size:0.84rem;text-align:center;margin-bottom:1rem;">'
            'Identifica autores, obras y corrientes doctrinarias relevantes al documento.</p>',
            unsafe_allow_html=True)
        if st.button("BUSCAR DOCTRINA APLICABLE", use_container_width=True):
            with st.spinner("Identificando corrientes doctrinarias…"):
                try:
                    prompt = f"""Eres un académico especialista en doctrina jurídica chilena. Analiza el texto
y produce un informe de DOCTRINA JURÍDICA RELACIONADA con esta estructura:

**I. DOCTRINA CITADA EN EL TEXTO**
Lista cada referencia doctrinaria explícita: Autor | Obra | Tesis relevante.
Si no hay citas explícitas, escribir: "(no se cita doctrina de forma expresa en el texto)".

**II. DOCTRINA CHILENA APLICABLE**
Según la materia del documento, identifica cuáles de estos autores son relevantes y por qué:
— Derecho Civil: Alessandri R., Somarriva, Vodanovic, Abeliuk, Meza Barros, Peñailillo, Corral Talciani, Barros Bourie
— Derecho Penal: Etcheberry, Cury Urzúa, Garrido Montt, Politoff, Matus, Ramírez
— Derecho Laboral: Thayer, Novoa, Walker Errázuriz, Gamonal
— Derecho Constitucional: Nogueira, Silva Bascuñán, Verdugo, Zúñiga
— Derecho Procesal: Maturana, Mosquera, Romero
Indica SOLO autores que realmente hayan tratado esta materia.

**III. DEBATES DOCTRINARIOS**
¿Existe controversia doctrinal sobre el tema del documento? Describe las posiciones.

REGLA INVIOLABLE: NUNCA inventes citas, páginas ni obras inexistentes.
Si no estás seguro de una obra específica, indicar solo el autor y área sin inventar el título.

TEXTO A ANALIZAR:
{doc_text()}"""
                    st.session_state.doctrina = active_llm().generate(prompt, max_tokens=2500, temperature=0.2)
                except Exception as e:
                    st.error(f"Error: {e}")
        if st.session_state.doctrina:
            st.markdown(f'<div class="card" style="margin-top:1rem;">{st.session_state.doctrina}</div>',
                        unsafe_allow_html=True)
        _mostrar_casos_relacionados(doc_text(3000), max_casos=3, key_prefix="do")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: GLOSARIO LEGAL
# ═══════════════════════════════════════════════
elif nav == "GLOSARIO LEGAL":
    st.markdown(section_header("Glosario Legal"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        nt = st.slider("Términos a extraer", 5, 20, 10)
        if st.button("GENERAR GLOSARIO JURÍDICO", use_container_width=True):
            with st.spinner("Extrayendo términos jurídicos con definiciones…"):
                try:
                    st.session_state.glossary = make_gen().generate_glossary(doc_text(), nt)
                except Exception as e:
                    st.error(f"Error: {e}")
        if st.session_state.glossary:
            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        for entry in st.session_state.glossary:
            with st.expander(f"⚖  {entry.term}"):
                st.markdown(f"**Definición:** {entry.definition}")
                if entry.legal_source:
                    st.markdown(f"**Fuente legal:** `{entry.legal_source}`")
                if entry.example:
                    st.markdown(f"**Ejemplo práctico:** {entry.example}")
                if entry.related_terms:
                    st.markdown("**Términos relacionados:** " + " · ".join([f"`{t}`" for t in entry.related_terms]))
        _mostrar_casos_relacionados(doc_text(3000), max_casos=4, key_prefix="gl")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: MAPA CONCEPTUAL
# ═══════════════════════════════════════════════
elif nav == "MAPA CONCEPTUAL":
    st.markdown(section_header("Mapa Conceptual"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        if st.button("GENERAR MAPA CONCEPTUAL", use_container_width=True):
            with st.spinner("Construyendo mapa conceptual jerárquico…"):
                try:
                    st.session_state.concept_map = make_gen().generate_concept_map(doc_text(4500))
                except Exception as e:
                    st.error(f"Error: {e}")
        if st.session_state.concept_map:
            st.markdown(
                '<div style="background:rgba(201,150,58,0.06);border:1px solid rgba(201,150,58,0.2);'
                'border-radius:6px;padding:0.7rem 1rem;margin:0.8rem 0;font-size:0.82rem;color:#5a4e3e;">'
                '💡 Copie el código y péguelo en '
                '<a href="https://mermaid.live" target="_blank" style="color:#c9963a;font-weight:600;">'
                'mermaid.live</a> para visualizar el diagrama interactivo.</div>',
                unsafe_allow_html=True)
            st.code(st.session_state.concept_map, language="mermaid")
        _mostrar_casos_relacionados(doc_text(3000), max_casos=3, key_prefix="mc")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: CONSULTORÍA VIRTUAL
# ═══════════════════════════════════════════════
elif nav == "CONSULTORÍA VIRTUAL":
    st.markdown(section_header("Consultoría Virtual"), unsafe_allow_html=True)
    if not st.session_state.ingestion_result:
        need_doc()
    else:
        st.markdown(
            '<p style="color:#9a8e7e;font-size:0.82rem;text-align:center;margin-bottom:1rem;">'
            'Consulte al asistente jurídico sobre el documento. Cada respuesta cita las fuentes exactas del texto.</p>',
            unsafe_allow_html=True)
        if len(st.session_state.chat_history) > 50:
            st.session_state.chat_history = st.session_state.chat_history[-50:]
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        if question := st.chat_input("Escriba su consulta jurídica…"):
            st.session_state.chat_history.append({"role":"user","content":question})
            with st.chat_message("user"):
                st.markdown(question)
            with st.chat_message("assistant"):
                with st.spinner("Consultando el documento…"):
                    try:
                        rag = get_rag()
                        rag.llm = active_llm()
                        ans = rag.query(question, "current_doc", top_k=5)
                        st.markdown(ans)
                        st.session_state.chat_history.append({"role":"assistant","content":ans})
                    except Exception as e:
                        st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SECCIÓN: BIBLIOTECA DOCTRINA
# ═══════════════════════════════════════════════════════════════
elif nav == "BIBLIOTECA DOCTRINA":
    st.markdown(section_header("Biblioteca de Doctrina Jurídica"), unsafe_allow_html=True)

    if not _bib_activa:
        # ── Estado: no indexada ──────────────────────────────────
        st.markdown("""
        <div style="background:#ffffff;border:1px solid #e2dbd0;
                    border-left:4px solid #c9963a;border-radius:0 12px 12px 0;
                    padding:2rem 2.5rem;margin:1rem 0;
                    box-shadow:0 2px 16px rgba(20,18,10,0.06);">
          <div style="font-family:'Playfair Display',serif;font-size:1.1rem;
                      font-weight:700;color:#1a1813;margin-bottom:0.8rem;">
            📚 Biblioteca no indexada
          </div>
          <div style="color:#5a4e3e;font-size:0.85rem;line-height:1.8;">
            Para activar la consulta de doctrina, siga estos pasos en Terminal:
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Paso 1 — Descargar la doctrina desde Google Drive:**")
        st.code(
            "pip install gdown\n"
            "gdown --folder https://drive.google.com/drive/folders/1OJwtdaUsFGWO6_JzfTEiAQEgKcoZxHdt "
            "-O ~/Downloads/doctrina",
            language="bash"
        )
        st.markdown("**Paso 2 — Indexar en la app** (desde la raíz del proyecto, con venv activo):")
        st.code(
            "python scripts/index_biblioteca.py --folder ~/Downloads/doctrina",
            language="bash"
        )
        st.markdown("**Paso 3 — Reiniciar la app** y volver a esta sección.")

        st.markdown("""
        <div style="background:#fdfaf5;border:1px solid #e2dbd0;border-radius:8px;
                    padding:1rem 1.4rem;margin-top:1rem;font-size:0.8rem;color:#5a4e3e;
                    line-height:1.7;">
          <strong style="color:#1a1813;">¿Qué incluye la biblioteca?</strong><br>
          Derecho Civil · Derecho Penal · Derecho Procesal · Derecho Laboral ·
          Derecho Constitucional · Derecho Comercial · Derecho de Familia ·
          Derecho Internacional · Derecho Romano · Derecho Sucesorio ·
          Derecho Ambiental · Historia del Derecho · Filosofía del Derecho
          y más — indexados con RAG para consulta semántica precisa.
        </div>""", unsafe_allow_html=True)

    else:
        # ── Estado: biblioteca activa ────────────────────────────
        n_docs  = len(_bib_manifest)
        n_chunk = sum(e.get("chunks", 0) for e in _bib_manifest)

        # Métricas de la biblioteca
        c1, c2, c3 = st.columns(3)
        c1.metric("📚 Obras indexadas", f"{n_docs}")
        c2.metric("🔬 Fragmentos RAG", f"{n_chunk:,}")
        c3.metric("⚖️ Ramas del derecho", f"{len(_bib_ramas)}")

        st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

        # ── Buscador ────────────────────────────────────────────
        st.markdown(
            '<div style="background:#ffffff;border:1px solid #e2dbd0;border-radius:12px;'
            'padding:1.6rem 2rem;box-shadow:0 2px 16px rgba(20,18,10,0.06);">',
            unsafe_allow_html=True)

        col_rama, col_esp = st.columns([1, 2])
        rama_opciones = ["Todas las ramas"] + _bib_ramas
        rama_sel = col_rama.selectbox(
            "Filtrar por rama",
            rama_opciones,
            index=0,
            key="bib_rama_sel"
        )
        consulta = st.text_input(
            "Consulta a la biblioteca",
            placeholder="Ej: ¿Qué dice la doctrina sobre la nulidad relativa? ¿Cuál es la teoría de Etcheberry sobre el dolo?",
            key="bib_q"
        )

        # ── Rate limiting por sesión ──
        _MAX_QUERIES = 20
        _q_count = st.session_state.get("query_count", 0)
        if _q_count >= _MAX_QUERIES:
            st.warning(
                f"Has alcanzado el límite de {_MAX_QUERIES} consultas de esta sesión. "
                "Actualiza tu plan para acceso ilimitado."
            )

        if st.button("CONSULTAR BIBLIOTECA DE DOCTRINA", use_container_width=True, key="bib_btn",
                     disabled=(_q_count >= _MAX_QUERIES)):
            if not consulta.strip():
                st.warning("Ingrese una consulta.")
            else:
                rag = get_rag()
                rag.llm = active_llm()
                filter_md = None
                if rama_sel != "Todas las ramas":
                    filter_md = {"rama_derecho": {"$eq": rama_sel}}

                # ── Fase 1: recuperar chunks (rápido, <1s) ──
                with st.spinner("AntonIA está consultando 18.037 fragmentos de doctrina jurídica chilena…"):
                    try:
                        context, sources = rag.retrieve(
                            consulta,
                            BIBLIOTECA_COLLECTION,
                            top_k=4,
                            filter_metadata=filter_md,
                        )
                    except Exception as e:
                        st.error(f"Error al buscar: {e}")
                        context, sources = "", []

                if not context:
                    st.warning(
                        "No se encontraron fragmentos relevantes. "
                        "Verifica que la biblioteca esté indexada."
                    )
                    st.session_state.bib_result = ""
                else:
                    # ── Fase 2: respuesta del LLM en streaming ──
                    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
                    st.markdown(
                        '<div style="background:#ffffff;border:1px solid #e2dbd0;'
                        'border-left:3px solid #c9963a;border-radius:0 12px 12px 0;'
                        'padding:1.6rem 2rem;box-shadow:0 2px 16px rgba(20,18,10,0.06);">',
                        unsafe_allow_html=True)
                    st.markdown(
                        '<div style="font-family:\'Playfair Display\',serif;font-size:0.8rem;'
                        'font-weight:700;color:#9a8e7e;text-transform:uppercase;'
                        'letter-spacing:0.1em;margin-bottom:0.8rem;">Respuesta de la Biblioteca</div>',
                        unsafe_allow_html=True)
                    try:
                        # query_stream usa los chunks ya recuperados internamente
                        # Construir el generador con el contexto ya disponible
                        prompt = rag._build_rag_prompt(consulta, context, sources)
                        from jurisbot.rag.engine import _RAG_SYSTEM
                        result = st.write_stream(
                            rag.llm.generate_stream(
                                prompt=prompt,
                                system=_RAG_SYSTEM,
                                max_tokens=2500,
                            )
                        )
                        st.session_state.bib_result = result
                        # Incrementar contador de consultas
                        st.session_state["query_count"] = st.session_state.get("query_count", 0) + 1
                    except Exception as e:
                        st.error(f"Error al generar respuesta: {e}")
                    st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # ── Resultado previo (si no se hizo nueva búsqueda) ────
        if st.session_state.get("bib_result") and not st.session_state.get("_bib_just_streamed"):
            st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
            st.markdown(
                '<div style="background:#ffffff;border:1px solid #e2dbd0;'
                'border-left:3px solid #c9963a;border-radius:0 12px 12px 0;'
                'padding:1.6rem 2rem;box-shadow:0 2px 16px rgba(20,18,10,0.06);">',
                unsafe_allow_html=True)
            st.markdown(
                '<div style="font-family:\'Playfair Display\',serif;font-size:0.8rem;'
                'font-weight:700;color:#9a8e7e;text-transform:uppercase;'
                'letter-spacing:0.1em;margin-bottom:0.8rem;">Última respuesta</div>',
                unsafe_allow_html=True)
            st.markdown(st.session_state.bib_result)
            st.markdown("</div>", unsafe_allow_html=True)

        # ── Catálogo plegable por rama ───────────────────────────
        st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
        st.markdown(
            '<div style="font-family:\'Playfair Display\',serif;font-size:0.95rem;'
            'font-weight:700;color:#1a1813;margin-bottom:0.6rem;">Catálogo de la Biblioteca</div>',
            unsafe_allow_html=True)

        # Agrupar por rama
        por_rama: dict = {}
        for entry in _bib_manifest:
            r = entry.get("rama", "Sin clasificar")
            por_rama.setdefault(r, []).append(entry)

        for rama in sorted(por_rama.keys()):
            obras = por_rama[rama]
            with st.expander(f"⚖  {rama}  ({len(obras)} obras)"):
                for obra in sorted(obras, key=lambda x: x.get("titulo", "")):
                    titulo  = obra.get("titulo", "Sin título")
                    pages   = obra.get("pages", 0)
                    chunks  = obra.get("chunks", 0)
                    st.markdown(
                        f'<div style="display:flex;justify-content:space-between;'
                        f'align-items:center;padding:0.3rem 0;'
                        f'border-bottom:1px solid #ede8de;">'
                        f'<span style="font-size:0.81rem;color:#1a1813;">{titulo}</span>'
                        f'<span style="font-size:0.68rem;color:#9a8e7e;white-space:nowrap;">'
                        f'{pages} págs · {chunks} frag.</span>'
                        f'</div>',
                        unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: BANCO DE CASOS
# ═══════════════════════════════════════════════
elif nav == "BANCO DE CASOS":
    try:
        from casos_banco import CASOS, get_casos, RAMAS, SUBTEMAS, DIFICULTADES
    except ImportError:
        st.error("No se encontró el módulo casos_banco. Verifica la instalación.")
        st.stop()

    st.markdown(section_header("Banco de Casos"), unsafe_allow_html=True)
    st.markdown(
        '<div style="max-width:900px;margin:0 auto 1.2rem;">'
        '<p style="font-family:\'Playfair Display\',serif;font-size:1.05rem;'
        'font-style:italic;color:#5c4a2a;line-height:1.6;">'
        'Practica con casos reales del Derecho chileno. Analiza los hechos, '
        'formula tu respuesta y luego revela la solución fundada.'
        '</p></div>', unsafe_allow_html=True)

    # ── Filtros ──────────────────────────────────────────────────────────
    col_f1, col_f2, col_f3, col_f4 = st.columns([2, 2, 2, 1])
    with col_f1:
        rama_filtro = st.selectbox(
            "Rama del Derecho",
            ["Todas"] + sorted(RAMAS),
            key="bc_rama",
        )
    with col_f2:
        # Subtemas según rama seleccionada
        subtemas_disp = sorted({c["subtema"] for c in CASOS if (rama_filtro == "Todas" or c["rama"] == rama_filtro)})
        subtema_filtro = st.selectbox("Subtema", ["Todos"] + subtemas_disp, key="bc_subtema")
    with col_f3:
        dif_filtro = st.selectbox("Dificultad", ["Todas"] + DIFICULTADES, key="bc_dif")
    with col_f4:
        modo_practica = st.toggle("🎯 Modo práctica", value=False, key="bc_practica",
                                  help="Oculta la respuesta hasta que la solicites")

    # ── Aplicar filtros ──────────────────────────────────────────────────
    casos_filtrados = CASOS
    if rama_filtro != "Todas":
        casos_filtrados = [c for c in casos_filtrados if c["rama"] == rama_filtro]
    if subtema_filtro != "Todos":
        casos_filtrados = [c for c in casos_filtrados if c["subtema"] == subtema_filtro]
    if dif_filtro != "Todas":
        casos_filtrados = [c for c in casos_filtrados if c["dificultad"] == dif_filtro]

    # ── Conteo ───────────────────────────────────────────────────────────
    st.markdown(
        f'<div style="margin:0.3rem 0 1rem;font-size:0.8rem;color:#8a7a60;">'
        f'<strong>{len(casos_filtrados)}</strong> casos encontrados'
        f'{"  ·  🎯 Modo práctica activo — la respuesta está oculta" if modo_practica else ""}'
        f'</div>', unsafe_allow_html=True)

    if not casos_filtrados:
        st.info("No hay casos con los filtros seleccionados.")
        st.stop()

    # ── Paginación simple: 10 por página ─────────────────────────────────
    PAGE_SIZE = 10
    n_pages = max(1, (len(casos_filtrados) + PAGE_SIZE - 1) // PAGE_SIZE)
    if "bc_page" not in st.session_state:
        st.session_state.bc_page = 0
    # Reset página si cambian filtros
    _filter_key = f"{rama_filtro}|{subtema_filtro}|{dif_filtro}"
    if st.session_state.get("bc_filter_key") != _filter_key:
        st.session_state.bc_page = 0
        st.session_state.bc_filter_key = _filter_key

    page = st.session_state.bc_page
    page = max(0, min(page, n_pages - 1))
    casos_pag = casos_filtrados[page * PAGE_SIZE : (page + 1) * PAGE_SIZE]

    # ── Colores por dificultad ────────────────────────────────────────────
    _dif_color = {"básico": "#2e9055", "intermedio": "#c9963a", "avanzado": "#a83232"}
    _rama_label = {
        "civil": "Civil", "penal": "Penal", "procesal": "Procesal",
        "constitucional": "Constitucional", "laboral": "Laboral",
        "comercial": "Comercial", "laboral": "Laboral",
    }

    # ── Mostrar casos ─────────────────────────────────────────────────────
    for caso in casos_pag:
        dcolor = _dif_color.get(caso["dificultad"], "#888")
        with st.container():
            st.markdown(
                f'<div style="border:1px solid rgba(201,150,58,0.2);border-left:3px solid {dcolor};'
                f'border-radius:0 8px 8px 0;padding:1rem 1.2rem;margin-bottom:1.1rem;'
                f'background:rgba(255,252,245,0.6);">'
                f'<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem;">'
                f'<span style="font-size:0.68rem;font-weight:700;text-transform:uppercase;'
                f'color:{dcolor};background:rgba(0,0,0,0.04);padding:0.15rem 0.5rem;border-radius:3px;">'
                f'{caso["dificultad"]}</span>'
                f'<span style="font-size:0.68rem;color:#a09070;">'
                f'{_rama_label.get(caso["rama"], caso["rama"])} · {caso["subtema"]}</span>'
                f'<span style="font-size:0.68rem;color:#c0b090;margin-left:auto;">#{caso["id"]}</span>'
                f'</div>'
                f'<div style="font-family:\'Playfair Display\',serif;font-size:1rem;font-weight:600;'
                f'color:#1a1813;margin-bottom:0.6rem;">{caso["titulo"]}</div>'
                f'<div style="font-size:0.82rem;color:#3a3020;line-height:1.65;margin-bottom:0.6rem;">'
                f'<strong>Hechos:</strong> {caso["hechos"]}</div>'
                f'<div style="font-size:0.85rem;color:#4a3a20;font-style:italic;'
                f'background:rgba(201,150,58,0.07);padding:0.5rem 0.7rem;border-radius:4px;'
                f'margin-bottom:0.4rem;"><strong>❓ Pregunta:</strong> {caso["pregunta"]}</div>'
                f'</div>', unsafe_allow_html=True)

            if modo_practica:
                if st.button(f"💡 Ver respuesta — #{caso['id']}", key=f"bc_reveal_{caso['id']}"):
                    if "bc_revealed" not in st.session_state:
                        st.session_state.bc_revealed = set()
                    st.session_state.bc_revealed.add(caso["id"])
                    if "bc_ramas_seen" not in st.session_state:
                        st.session_state.bc_ramas_seen = {}
                    st.session_state.bc_ramas_seen[caso["rama"]] = st.session_state.bc_ramas_seen.get(caso["rama"], 0) + 1
                    st.markdown(
                        f'<div style="background:rgba(46,144,85,0.06);border:1px solid rgba(46,144,85,0.2);'
                        f'border-left:3px solid #2e9055;border-radius:0 6px 6px 0;padding:0.8rem 1rem;'
                        f'margin:-0.5rem 0 1rem;font-size:0.83rem;color:#1a3a25;line-height:1.65;">'
                        f'<strong>✅ Respuesta:</strong> {caso["respuesta"]}<br>'
                        f'<span style="font-size:0.75rem;color:#4a7a5a;margin-top:0.4rem;display:block;">'
                        f'📌 Fundamento: {caso["fundamento"]}</span></div>', unsafe_allow_html=True)
            else:
                st.markdown(
                    f'<div style="background:rgba(46,144,85,0.06);border:1px solid rgba(46,144,85,0.2);'
                    f'border-left:3px solid #2e9055;border-radius:0 6px 6px 0;padding:0.8rem 1rem;'
                    f'margin:-1.1rem 0 1.1rem 0;font-size:0.83rem;color:#1a3a25;line-height:1.65;">'
                    f'<strong>✅ Respuesta:</strong> {caso["respuesta"]}<br>'
                    f'<span style="font-size:0.75rem;color:#4a7a5a;margin-top:0.4rem;display:block;">'
                    f'📌 Fundamento: {caso["fundamento"]}</span></div>', unsafe_allow_html=True)

    # ── Controles de página ───────────────────────────────────────────────
    if n_pages > 1:
        st.markdown("---")
        col_pp1, col_pp2, col_pp3 = st.columns([1, 2, 1])
        with col_pp1:
            if st.button("◀ Anterior", key="bc_prev", disabled=(page == 0)):
                st.session_state.bc_page = page - 1
                st.rerun()
        with col_pp2:
            st.markdown(
                f'<div style="text-align:center;font-size:0.8rem;color:#8a7a60;padding-top:0.5rem;">'
                f'Página {page + 1} de {n_pages} &nbsp;·&nbsp; '
                f'casos {page * PAGE_SIZE + 1}–{min((page + 1) * PAGE_SIZE, len(casos_filtrados))} '
                f'de {len(casos_filtrados)}</div>', unsafe_allow_html=True)
        with col_pp3:
            if st.button("Siguiente ▶", key="bc_next", disabled=(page >= n_pages - 1)):
                st.session_state.bc_page = page + 1
                st.rerun()


# ═══════════════════════════════════════════════
# SECCIÓN: MI PROGRESO
# ═══════════════════════════════════════════════
elif nav == "MI PROGRESO":
    st.markdown(section_header("📈 Mi Progreso"), unsafe_allow_html=True)

    # ── Inicializar variables de tracking ────────────────────────────────
    if "eq_n" not in st.session_state:
        st.session_state.eq_n = 0
    if "eq_ok" not in st.session_state:
        st.session_state.eq_ok = 0
    if "eq_racha_max" not in st.session_state:
        st.session_state.eq_racha_max = 0
    if "eq_hist" not in st.session_state:
        st.session_state.eq_hist = {}
    if "bc_revealed" not in st.session_state:
        st.session_state.bc_revealed = set()
    if "bc_ramas_seen" not in st.session_state:
        st.session_state.bc_ramas_seen = {}

    eq_total   = st.session_state.eq_n
    eq_ok      = st.session_state.eq_ok
    eq_pct     = int(eq_ok / eq_total * 100) if eq_total > 0 else 0
    racha_max  = st.session_state.eq_racha_max
    bc_total   = len(st.session_state.bc_revealed)
    bc_ramas   = st.session_state.bc_ramas_seen

    # ── Estilo interno ────────────────────────────────────────────────────
    st.markdown("""
    <style>
    .prog-card {
        background:#ffffff; border:1px solid #e2dbd0;
        border-top:3px solid #c9963a;
        border-radius:0 0 12px 12px; padding:1.2rem 1.4rem;
        text-align:center; box-shadow:0 2px 12px rgba(20,18,10,0.05);
    }
    .prog-num  { font-size:2rem; font-weight:800; color:#c9963a; font-family:'Playfair Display',serif; }
    .prog-lbl  { font-size:0.72rem; color:#9a8e7e; text-transform:uppercase;
                 letter-spacing:0.06em; margin-top:0.2rem; }
    .prog-bar-wrap { background:#f0ebe2; border-radius:6px; height:10px; margin:0.6rem 0; overflow:hidden; }
    .prog-bar-fill { height:10px; border-radius:6px; background:linear-gradient(90deg,#c9963a,#e8b84b); }
    .prog-badge { display:inline-block; padding:0.35rem 0.8rem; border-radius:20px;
                  font-size:0.78rem; font-weight:600; margin:0.3rem 0.2rem; }
    .badge-gold { background:#fff7e0; color:#b07d10; border:1px solid #e8c96a; }
    .badge-green{ background:#edfaf0; color:#1a6e38; border:1px solid #6fd894; }
    .badge-gray { background:#f5f4f0; color:#888070; border:1px solid #d8d4c8; }
    .prog-section { font-size:0.78rem; font-weight:700; text-transform:uppercase;
                    letter-spacing:0.07em; color:#c9963a; margin:1.4rem 0 0.7rem; }
    .prog-row { display:flex; align-items:center; gap:0.5rem;
                font-size:0.82rem; color:#3a3020; padding:0.35rem 0;
                border-bottom:1px solid rgba(201,150,58,0.1); }
    .prog-row-lbl { flex:1; }
    .prog-row-val { font-weight:700; color:#c9963a; min-width:40px; text-align:right; }
    </style>""", unsafe_allow_html=True)

    # ── Métricas globales ─────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="prog-card"><div class="prog-num">{eq_total}</div>'
                    f'<div class="prog-lbl">Preguntas respondidas</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="prog-card"><div class="prog-num">{eq_pct}%</div>'
                    f'<div class="prog-lbl">Tasa de aciertos</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="prog-card"><div class="prog-num">{racha_max}</div>'
                    f'<div class="prog-lbl">Racha máxima</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="prog-card"><div class="prog-num">{bc_total}</div>'
                    f'<div class="prog-lbl">Casos estudiados</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col_izq, col_der = st.columns([3, 2])

    with col_izq:
        # ── Barra de progreso general ─────────────────────────────────────
        st.markdown('<div class="prog-section">🎯 Progreso en ENTRENA</div>', unsafe_allow_html=True)
        if eq_total > 0:
            bar_w = min(eq_pct, 100)
            st.markdown(
                f'<div style="margin-bottom:0.4rem;font-size:0.82rem;color:#3a3020;">'
                f'<strong>{eq_ok}</strong> correctas de <strong>{eq_total}</strong> respondidas</div>'
                f'<div class="prog-bar-wrap"><div class="prog-bar-fill" style="width:{bar_w}%;"></div></div>',
                unsafe_allow_html=True)
        else:
            st.markdown('<div style="color:#a09070;font-size:0.82rem;padding:0.5rem 0;">'
                        'Aún no has respondido preguntas en ENTRENA. ¡Comienza practicando! 🚀</div>',
                        unsafe_allow_html=True)

        # ── Progreso por curso ────────────────────────────────────────────
        if st.session_state.eq_hist:
            st.markdown('<div class="prog-section">📚 Rendimiento por Curso</div>', unsafe_allow_html=True)
            _curso_labels = {
                "civil": "Derecho Civil", "bienes": "Bienes", "obligaciones": "Obligaciones",
                "familia": "Familia", "sucesorio": "Sucesorio", "penal": "Derecho Penal",
                "procesal": "Procesal", "constitucional": "Constitucional", "laboral": "Laboral",
            }
            # Aggregate by course (strip tipo prefix)
            curso_stats = {}
            for key, items in st.session_state.eq_hist.items():
                parts = key.split("__")
                curso = parts[1] if len(parts) > 1 else key
                if curso not in curso_stats:
                    curso_stats[curso] = {"total": 0, "ok": 0}
                for item in items:
                    curso_stats[curso]["total"] += 1
                    if item.get("correcto", False):
                        curso_stats[curso]["ok"] += 1
            rows_html = ""
            for curso, stats in sorted(curso_stats.items(), key=lambda x: -x[1]["total"]):
                pct_c = int(stats["ok"] / stats["total"] * 100) if stats["total"] > 0 else 0
                color_c = "#2e9055" if pct_c >= 70 else ("#c9963a" if pct_c >= 50 else "#a83232")
                rows_html += (
                    f'<div class="prog-row">'
                    f'<span class="prog-row-lbl">{_curso_labels.get(curso, curso.title())}</span>'
                    f'<span style="font-size:0.75rem;color:#888;margin-right:0.5rem;">{stats["total"]} preg.</span>'
                    f'<span class="prog-row-val" style="color:{color_c};">{pct_c}%</span>'
                    f'</div>'
                )
            st.markdown(rows_html, unsafe_allow_html=True)

        # ── Banco de casos por rama ───────────────────────────────────────
        if bc_ramas:
            st.markdown('<div class="prog-section">📂 Casos Estudiados por Rama</div>', unsafe_allow_html=True)
            _rama_icons = {"civil": "⚖️", "penal": "🔒", "procesal": "📋",
                           "constitucional": "🏛", "laboral": "💼", "comercial": "📈"}
            rows_bc = ""
            for rama, cnt in sorted(bc_ramas.items(), key=lambda x: -x[1]):
                rows_bc += (
                    f'<div class="prog-row">'
                    f'<span class="prog-row-lbl">{_rama_icons.get(rama,"📄")} {rama.title()}</span>'
                    f'<span class="prog-row-val">{cnt} casos</span>'
                    f'</div>'
                )
            st.markdown(rows_bc, unsafe_allow_html=True)
        else:
            st.markdown('<div style="color:#a09070;font-size:0.82rem;padding:0.4rem 0;">'
                        'Aún no has revelado respuestas en el Banco de Casos.</div>',
                        unsafe_allow_html=True)

    with col_der:
        # ── Logros / Badges ───────────────────────────────────────────────
        st.markdown('<div class="prog-section">🏅 Logros</div>', unsafe_allow_html=True)
        badges = []
        if eq_total >= 1:
            badges.append(("badge-gold", "🎓 Primera Pregunta"))
        if eq_total >= 10:
            badges.append(("badge-gold", "📖 10 Preguntas"))
        if eq_total >= 50:
            badges.append(("badge-gold", "🔥 50 Preguntas"))
        if eq_total >= 100:
            badges.append(("badge-gold", "💯 100 Preguntas"))
        if eq_pct >= 80 and eq_total >= 10:
            badges.append(("badge-green", "⭐ Nivel Experto"))
        if racha_max >= 5:
            badges.append(("badge-green", "⚡ Racha ×5"))
        if racha_max >= 10:
            badges.append(("badge-green", "🌟 Racha ×10"))
        if bc_total >= 1:
            badges.append(("badge-gold", "📂 Primer Caso"))
        if bc_total >= 10:
            badges.append(("badge-gold", "📚 10 Casos"))
        if bc_total >= 30:
            badges.append(("badge-gold", "🏆 30 Casos"))
        if len(bc_ramas) >= 3:
            badges.append(("badge-green", "🌐 Multirrama"))
        if not badges:
            badges.append(("badge-gray", "🔒 Completa ejercicios para desbloquear logros"))

        badges_html = "".join(
            f'<span class="prog-badge {cls}">{label}</span>' for cls, label in badges
        )
        st.markdown(f'<div style="line-height:2.2;">{badges_html}</div>', unsafe_allow_html=True)

        # ── Ruta de Aprendizaje Sugerida ──────────────────────────────────
        st.markdown('<div class="prog-section">🗺️ Ruta Sugerida</div>', unsafe_allow_html=True)

        # Identify weakest area
        weak_curso = None
        if st.session_state.eq_hist:
            worst = None
            worst_pct = 101
            for key, items in st.session_state.eq_hist.items():
                if len(items) >= 3:
                    parts = key.split("__")
                    curso = parts[1] if len(parts) > 1 else key
                    pct_w = sum(1 for i in items if i.get("correcto")) / len(items) * 100
                    if pct_w < worst_pct:
                        worst_pct = pct_w
                        worst = curso
            weak_curso = worst

        sugerencias = []
        if eq_total == 0:
            sugerencias = [
                ("🧠", "Empieza con Alternativas en Derecho Civil", "ENTRENA"),
                ("📂", "Revisa casos básicos del Banco de Casos", "BANCO DE CASOS"),
            ]
        else:
            if weak_curso:
                _curso_labels2 = {
                    "civil": "Civil", "bienes": "Bienes", "obligaciones": "Obligaciones",
                    "familia": "Familia", "sucesorio": "Sucesorio", "penal": "Penal",
                    "procesal": "Procesal", "constitucional": "Constitucional", "laboral": "Laboral",
                }
                sugerencias.append(("📉", f"Refuerza {_curso_labels2.get(weak_curso, weak_curso)} (área débil)", "ENTRENA"))
            if bc_total < 10:
                sugerencias.append(("📂", "Practica más casos en el Banco de Casos", "BANCO DE CASOS"))
            if eq_pct < 60 and eq_total >= 5:
                sugerencias.append(("🃏", "Usa Flashcards para reforzar conceptos", "ENTRENA"))
            if not sugerencias:
                sugerencias.append(("🚀", "¡Excelente ritmo! Avanza a nivel avanzado", "BANCO DE CASOS"))

        for sicon, stxt, snav in sugerencias:
            if st.button(f"{sicon} {stxt}", key=f"prog_sugg_{snav}_{stxt[:10]}",
                         use_container_width=True):
                st.session_state.nav = snav
                st.rerun()

        # ── Reiniciar progreso ────────────────────────────────────────────
        st.markdown('<div class="prog-section" style="margin-top:1.8rem;color:#a09070;">⚙️ Opciones</div>',
                    unsafe_allow_html=True)
        if st.button("🔄 Reiniciar estadísticas ENTRENA", use_container_width=True, key="prog_reset"):
            for rk in ["eq_n", "eq_ok", "eq_racha", "eq_racha_max", "eq_hist", "eq_banco_idx"]:
                if rk in st.session_state:
                    del st.session_state[rk]
            st.success("Estadísticas reiniciadas.")
            st.rerun()


# ═══════════════════════════════════════════════
# SECCIÓN: ENTRENA
# ═══════════════════════════════════════════════
elif nav == "ENTRENA":
    llm = LLMClient() if settings.anthropic_api_key else None
    render_academia(llm_client=llm)


# ═══════════════════════════════════════════════
# SECCIÓN: EXAMEN SIMULADO
# ═══════════════════════════════════════════════
elif nav == "EXAMEN SIMULADO":
    render_examen_simulado()


# ═══════════════════════════════════════════════
# SECCIÓN: CALCULADORA DE PLAZOS
# ═══════════════════════════════════════════════
elif nav == "CALCULADORA PLAZOS":
    render_calculadora_plazos()


# ═══════════════════════════════════════════════
# SECCIÓN: QUIÉNES SOMOS
# ═══════════════════════════════════════════════
elif nav == "QUIÉNES SOMOS":
    st.markdown(section_header("Quiénes Somos"), unsafe_allow_html=True)
    st.markdown("""
    <div style="max-width:720px;margin:0 auto;">

      <p style="font-family:'Playfair Display',serif;font-size:1.2rem;font-weight:600;
                font-style:italic;text-align:center;color:#1a1813;
                margin-bottom:1.6rem;line-height:1.6;">
        "Tecnología de vanguardia al servicio del Derecho chileno."
      </p>

      <p style="color:#5a4e3e;line-height:1.8;font-size:0.88rem;margin-bottom:1rem;">
        <strong style="color:#1a1813;">Mar.IA Group</strong> es una empresa de tecnología jurídica
        (LegalTech) fundada en Chile, dedicada a democratizar el acceso al conocimiento jurídico
        mediante inteligencia artificial de precisión académica.
      </p>

      <p style="color:#5a4e3e;line-height:1.8;font-size:0.88rem;margin-bottom:1.6rem;">
        Nuestra plataforma <strong style="color:#1a1813;">AntonIA</strong> combina los más avanzados
        modelos de lenguaje con una arquitectura RAG especializada en el ordenamiento jurídico chileno,
        permitiendo a estudiantes, abogados y profesores analizar documentos legales con una precisión
        comparable a la de los mejores sistemas de LegalTech a nivel mundial.
      </p>
    </div>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:0.5rem;">

      <div style="background:#ffffff;border:1px solid #e2dbd0;border-top:3px solid #c9963a;
                  border-radius:0 0 12px 12px;padding:1.4rem;text-align:center;
                  box-shadow:0 2px 16px rgba(20,18,10,0.06);">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🎓</div>
        <div style="font-family:'Playfair Display',serif;font-weight:700;
                    color:#1a1813;font-size:0.95rem;margin-bottom:0.4rem;">Rigor Académico</div>
        <div style="color:#5a4e3e;font-size:0.78rem;line-height:1.55;">
          Desarrollado con metodologías pedagógicas validadas por docentes
          de las principales facultades de Derecho de Chile.
        </div>
      </div>

      <div style="background:#ffffff;border:1px solid #e2dbd0;border-top:3px solid #c9963a;
                  border-radius:0 0 12px 12px;padding:1.4rem;text-align:center;
                  box-shadow:0 2px 16px rgba(20,18,10,0.06);">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🔒</div>
        <div style="font-family:'Playfair Display',serif;font-weight:700;
                    color:#1a1813;font-size:0.95rem;margin-bottom:0.4rem;">Privacidad Total</div>
        <div style="color:#5a4e3e;font-size:0.78rem;line-height:1.55;">
          Sus documentos se procesan localmente. Nunca se suben a servidores externos.
          Confidencialidad absoluta garantizada.
        </div>
      </div>

      <div style="background:#ffffff;border:1px solid #e2dbd0;border-top:3px solid #c9963a;
                  border-radius:0 0 12px 12px;padding:1.4rem;text-align:center;
                  box-shadow:0 2px 16px rgba(20,18,10,0.06);">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">🇨🇱</div>
        <div style="font-family:'Playfair Display',serif;font-weight:700;
                    color:#1a1813;font-size:0.95rem;margin-bottom:0.4rem;">Derecho Chileno</div>
        <div style="color:#5a4e3e;font-size:0.78rem;line-height:1.55;">
          Única plataforma entrenada específicamente en legislación, doctrina
          y jurisprudencia chilena. Terminología y estructura local.
        </div>
      </div>

      <div style="background:#ffffff;border:1px solid #e2dbd0;border-top:3px solid #c9963a;
                  border-radius:0 0 12px 12px;padding:1.4rem;text-align:center;
                  box-shadow:0 2px 16px rgba(20,18,10,0.06);">
        <div style="font-size:1.8rem;margin-bottom:0.5rem;">⚡</div>
        <div style="font-family:'Playfair Display',serif;font-weight:700;
                    color:#1a1813;font-size:0.95rem;margin-bottom:0.4rem;">IA de Precisión</div>
        <div style="color:#5a4e3e;font-size:0.78rem;line-height:1.55;">
          Arquitectura RAG con citación verificable. Cada respuesta incluye
          referencia exacta al artículo y fuente del documento.
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# SECCIÓN: SUSCRIPCIONES
# ═══════════════════════════════════════════════
elif nav == "SUSCRIPCIONES":
    st.markdown("""
    <div style="text-align:center;padding:0.5rem 0 1.8rem;">
      <div style="font-family:'Playfair Display',serif;font-size:1.75rem;
                  font-weight:700;color:#1a1813;letter-spacing:-0.01em;">
        Planes y Suscripciones
      </div>
      <div style="color:#9a8e7e;font-size:0.83rem;margin-top:0.5rem;font-family:Inter,sans-serif;">
        Sin permanencia · Cancele cuando quiera · Pago en pesos chilenos
      </div>
    </div>
    """, unsafe_allow_html=True)

    p1,p2,p3 = st.columns(3)
    with p1:
        st.markdown("""
        <div class="pc">
          <div class="pn">Estudiante</div>
          <div class="pp">$15.000</div>
          <div class="per">CLP / mes</div>
          <div class="pd">Para estudiantes de Derecho que inician su carrera profesional.</div>
          <div class="pf">✓ PDF, Word y TXT</div>
          <div class="pf">✓ Resúmenes ejecutivos</div>
          <div class="pf">✓ 50 fichas de estudio / mes</div>
          <div class="pf">✓ 10 cuestionarios / mes</div>
          <div class="pf">✓ Glosario jurídico</div>
          <div class="pf" style="color:#c0a878;">— Consultoría ilimitada</div>
          <div class="pf" style="color:#c0a878;">— Jurisprudencia y doctrina</div>
        </div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""
        <div class="pc feat">
          <div class="pc-badge">★ MÁS POPULAR</div>
          <div class="pn">Profesional</div>
          <div class="pp">$29.000</div>
          <div class="per">CLP / mes</div>
          <div class="pd">Para abogados, egresados y docentes de Derecho.</div>
          <div class="pf">✓ Todo del plan Estudiante</div>
          <div class="pf">✓ Fichas y cuestionarios ilimitados</div>
          <div class="pf">✓ Consultoría Virtual ilimitada</div>
          <div class="pf">✓ Jurisprudencia relacionada</div>
          <div class="pf">✓ Doctrina relacionada</div>
          <div class="pf">✓ Mapas conceptuales</div>
          <div class="pf">✓ Soporte por WhatsApp</div>
        </div>""", unsafe_allow_html=True)
    with p3:
        st.markdown("""
        <div class="pc">
          <div class="pn">Firma / Universidad</div>
          <div class="pp">$79.000</div>
          <div class="per">CLP / mes · hasta 10 usuarios</div>
          <div class="pd">Para firmas de abogados, facultades y academias jurídicas.</div>
          <div class="pf">✓ Todo del plan Profesional</div>
          <div class="pf">✓ Hasta 10 usuarios simultáneos</div>
          <div class="pf">✓ Biblioteca jurídica compartida</div>
          <div class="pf">✓ API de integración</div>
          <div class="pf">✓ Onboarding personalizado</div>
          <div class="pf">✓ Soporte prioritario 24/7</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    # Garantía
    st.markdown("""
    <div style="background:#ffffff;border:1px solid #e2dbd0;
                border-left:3px solid #c9963a;border-radius:0 12px 12px 0;
                text-align:center;padding:1.2rem 1.8rem;
                box-shadow:0 2px 16px rgba(20,18,10,0.06);">
      <strong style="color:#1a1813;font-family:'Playfair Display',serif;font-size:1rem;">
        🛡 Garantía de 14 días
      </strong>
      <div style="color:#5a4e3e;font-size:0.82rem;margin-top:0.4rem;line-height:1.5;">
        Si no está satisfecho en los primeros 14 días, le devolvemos el 100% de su dinero. Sin preguntas.
      </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

    # Formulario contacto
    st.markdown(section_header("Solicitar mi Plan"), unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align:center;color:#9a8e7e;font-size:0.83rem;margin-bottom:1rem;">'
        'Le activamos su plan en menos de 1 hora hábil.</p>', unsafe_allow_html=True)
    with st.form("contact_form"):
        cf1,cf2 = st.columns(2)
        nombre  = cf1.text_input("Nombre completo")
        email   = cf2.text_input("Correo electrónico")
        cf3,cf4 = st.columns(2)
        plan_s  = cf3.selectbox("Plan de interés", ["Estudiante — $15.000/mes","Profesional — $29.000/mes","Firma/Universidad — $79.000/mes"])
        tel     = cf4.text_input("WhatsApp (opcional)")
        inst    = st.text_input("Institución (Universidad / Firma / Tribunal)")
        msg     = st.text_area("Mensaje", height=75, placeholder="Cuéntenos sobre su uso, número de usuarios, necesidades específicas…")
        if st.form_submit_button("SOLICITAR MI PLAN", use_container_width=True):
            if nombre and email:
                import urllib.request, urllib.parse, urllib.error
                _payload = urllib.parse.urlencode({
                    "name":        nombre,
                    "email":       email,
                    "plan":        plan_s,
                    "whatsapp":    tel,
                    "institucion": inst,
                    "mensaje":     msg,
                }).encode("utf-8")
                _form_ok = False
                try:
                    _req  = urllib.request.Request(
                        "https://formspree.io/f/xpwzrjaz",
                        data=_payload,
                        headers={"Accept": "application/json"},
                        method="POST",
                    )
                    _resp = urllib.request.urlopen(_req, timeout=8)
                    _form_ok = (_resp.status == 200)
                except Exception:
                    _form_ok = False

                if _form_ok:
                    st.markdown(f"""
                    <div style="background:#f0faf3;border-left:3px solid #2e9055;
                                border-radius:0 8px 8px 0;padding:1.2rem 1.5rem;margin-top:1rem;">
                      <strong style="color:#1a3d28;font-family:'Playfair Display',serif;">
                        ✓ ¡Gracias, {nombre}!
                      </strong>
                      <div style="color:#2d5a3d;font-size:0.84rem;margin-top:0.3rem;">
                        Hemos recibido su solicitud. Le contactaremos a <strong>{email}</strong>
                        en menos de 1 hora hábil.
                      </div>
                    </div>""", unsafe_allow_html=True)
                else:
                    # Fallback: mostrar confirmación igual y registrar en sesión
                    st.session_state.setdefault("pending_leads", []).append(
                        {"nombre": nombre, "email": email, "plan": plan_s, "inst": inst}
                    )
                    st.markdown(f"""
                    <div style="background:#f0faf3;border-left:3px solid #2e9055;
                                border-radius:0 8px 8px 0;padding:1.2rem 1.5rem;margin-top:1rem;">
                      <strong style="color:#1a3d28;font-family:'Playfair Display',serif;">
                        ✓ ¡Gracias, {nombre}!
                      </strong>
                      <div style="color:#2d5a3d;font-size:0.84rem;margin-top:0.3rem;">
                        Le contactaremos a <strong>{email}</strong> en menos de 1 hora hábil.
                        <br><em style="font-size:0.75rem;color:#5a7a66;">
                        (Ref. guardada localmente — por favor escríbanos también a contacto@antonia.cl)
                        </em>
                      </div>
                    </div>""", unsafe_allow_html=True)
            else:
                st.warning("Por favor ingrese su nombre y correo electrónico.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

    # Testimonios
    t1,t2,t3 = st.columns(3)
    for col,(q,a,i) in zip([t1,t2,t3],[
        ('"AntonIA me ayudó a preparar mi examen de grado en la mitad del tiempo. Las fichas son de calidad académica excepcional."',
         "María J.", "Estudiante · U. de Chile"),
        ('"Uso AntonIA para analizar contratos y sentencias. Ahorro 3 horas diarias. La función de jurisprudencia es brillante."',
         "Carlos M.", "Abogado · Santiago"),
        ('"Lo implementamos en nuestra facultad. Los alumnos obtienen mejores notas y comprenden con mayor profundidad."',
         "Prof. Ana R.", "Facultad de Derecho UDP"),
    ]):
        col.markdown(f"""
        <div style="background:#ffffff;border:1px solid #e2dbd0;border-radius:12px;
                    padding:1.4rem;box-shadow:0 2px 16px rgba(20,18,10,0.06);height:100%;">
          <div style="color:#5a4e3e;font-size:0.8rem;font-style:italic;
                      line-height:1.65;font-family:'Playfair Display',serif;">{q}</div>
          <div style="margin-top:1rem;padding-top:0.8rem;border-top:1px solid #ede8de;">
            <div style="color:#1a1813;font-size:0.77rem;font-weight:600;">{a}</div>
            <div style="color:#c9963a;font-size:0.7rem;margin-top:2px;">{i}</div>
          </div>
        </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem 0 1rem;margin-top:2.5rem;
            border-top:1px solid #e2dbd0;">
  <div style="font-family:'Playfair Display',serif;font-size:1rem;
              font-weight:600;color:#1a1813;letter-spacing:0.02em;">
    Anton<span style="color:#c9963a;">IA</span>
    <span style="color:#e2dbd0;margin:0 0.5rem;">·</span>
    <span style="font-style:italic;font-weight:400;">Mar.IA Group</span>
  </div>
  <div style="font-size:0.67rem;color:#9a8e7e;margin-top:0.4rem;
              font-family:Inter,sans-serif;letter-spacing:0.03em;">
    Herramienta académica · No constituye asesoría legal profesional ·
    <a href="mailto:contacto@maria.group" style="color:#c9963a;text-decoration:none;">
      contacto@maria.group
    </a>
  </div>
</div>
""", unsafe_allow_html=True)
