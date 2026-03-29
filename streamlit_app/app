"""AntonIA — By Mar.IA Group  v4.0 ÉLITE
Plataforma de IA para el estudio y análisis del Derecho chileno.
Diseño inspirado en Harvey AI + Dark Academia Premium.
"""
import sys, base64, json, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Ruta al manifest de la biblioteca (relativa al directorio de la app)
_APP_DIR = Path(__file__).parent.parent
BIBLIOTECA_MANIFEST = _APP_DIR / "data" / "biblioteca_manifest.json"
BIBLIOTECA_COLLECTION = "biblioteca_doctrina"

import streamlit as st
from jurisbot.config import settings
from jurisbot.ingestion.orchestrator import IngestionOrchestrator
from jurisbot.nlp.classifier import LegalClassifier
from jurisbot.nlp.llm_client import LLMClient
from jurisbot.study.generator import StudyGenerator
from academia_module import render_academia
from jurisbot.rag.engine import RAGEngine

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


# ─────────────────────────────────────────────
# ESTADO DE SESIÓN
# ─────────────────────────────────────────────
DEFAULTS = {
    "nav": "ENTRENA",
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


# ─────────────────────────────────────────────
# SIDEBAR — DARK PREMIUM
# ─────────────────────────────────────────────
with st.sidebar:
    # ── LOGO MAR.IA GROUP ──
    st.markdown("""
    <div style="padding:1.6rem 1rem 1rem;border-bottom:1px solid rgba(255,255,255,0.07);">
      <div style="display:flex;align-items:center;gap:0.75rem;">
        <svg width="38" height="38" viewBox="0 0 38 38" fill="none">
          <circle cx="19" cy="19" r="17" stroke="rgba(201,150,58,0.45)" stroke-width="1.2" fill="rgba(201,150,58,0.06)"/>
          <text x="19" y="25" text-anchor="middle"
                font-family="Playfair Display,Georgia,serif" font-size="18"
                font-weight="700" fill="#e8c97a" font-style="italic">M</text>
        </svg>
        <div>
          <div style="font-family:'Playfair Display',Georgia,serif;font-size:1.1rem;
                      font-weight:700;color:#f0e8d8;letter-spacing:0.01em;line-height:1.1;">
            Mar.<span style="color:#c9963a;">IA</span> Group
          </div>
          <div style="font-size:0.6rem;color:rgba(201,150,58,0.6);text-transform:uppercase;
                      letter-spacing:0.12em;margin-top:2px;">LegalTech Chile</div>
        </div>
      </div>
      <div style="margin-top:0.9rem;padding:0.55rem 0.75rem;background:rgba(201,150,58,0.07);
                  border:1px solid rgba(201,150,58,0.18);border-radius:6px;text-align:center;">
        <span style="font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:600;
                     color:#c9963a;font-style:italic;letter-spacing:0.03em;">AntonIA</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── CARGA DE DOCUMENTO ──
    st.markdown("""
    <div style="padding:0.9rem 1rem 0.4rem;">
      <div style="font-size:0.6rem;font-weight:700;color:rgba(201,150,58,0.55);
                  text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.5rem;">
        Documento
      </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader("Subir", type=["pdf","docx","doc","txt","rtf","html","htm"],
                                  label_visibility="collapsed")
    if uploaded:
        if st.button("⬆  Procesar Documento", use_container_width=True, key="proc"):
            settings.ensure_dirs()
            tmp = settings.upload_dir / uploaded.name
            tmp.write_bytes(uploaded.getvalue())
            for k in ["ingestion_result","classification","chat_history","quiz_data",
                       "quiz_answers","quiz_submitted","flashcards","fc_idx","fc_show",
                       "glossary","concept_map","summary_text","jurisprudencia","doctrina"]:
                st.session_state[k] = DEFAULTS[k]
            with st.spinner("Procesando…"):
                try:
                    res = get_orch().ingest(tmp)
                    st.session_state.ingestion_result = res
                    cls = get_clf().classify(res.extraction.raw_text, res.extraction.metadata)
                    st.session_state.classification = cls
                    try:
                        rag = get_rag()
                        rag.delete_collection("current_doc")
                        rag.index_chunks(res.chunks, "current_doc")
                    except Exception: pass
                    st.success("✓ Documento listo")
                except Exception as e:
                    st.error(f"Error: {e}")

    if st.session_state.ingestion_result:
        r = st.session_state.ingestion_result
        st.markdown(
            f'<div style="margin:0.5rem 0.3rem;padding:0.6rem 0.8rem;'
            f'background:rgba(201,150,58,0.08);border:1px solid rgba(201,150,58,0.2);'
            f'border-radius:6px;">'
            f'<div style="font-size:0.77rem;color:#e8d8b8;font-weight:500;'
            f'overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{r.file_name[:26]}</div>'
            f'<div style="font-size:0.66rem;color:rgba(201,150,58,0.55);margin-top:2px;">'
            f'{r.extraction.pages} págs · {len(r.chunks)} fragmentos</div>'
            f'</div>',
            unsafe_allow_html=True)
        if st.session_state.classification:
            st.markdown(
                f'<div style="margin:0 0.3rem 0.2rem;font-size:0.67rem;'
                f'color:#c9963a;padding:0 0.5rem;">⚖ {st.session_state.classification.rama_derecho}</div>',
                unsafe_allow_html=True)

    st.markdown('<hr style="border-color:rgba(255,255,255,0.07);margin:0.5rem 0;">', unsafe_allow_html=True)

    # ── NAVEGACIÓN ──
    st.markdown("""
    <div style="padding:0.3rem 1rem 0.2rem;">
      <div style="font-size:0.6rem;font-weight:700;color:rgba(201,150,58,0.5);
                  text-transform:uppercase;letter-spacing:0.1em;">Navegación</div>
    </div>
    """, unsafe_allow_html=True)

    NAV_ITEMS = [
        ("🧠", "ENTRENA"),
        ("📋", "RESUMEN EJECUTIVO"),
        ("🔍", "ANÁLISIS"),
        ("⚖️", "JURISPRUDENCIA RELACIONADA"),
        ("📚", "DOCTRINA RELACIONADA"),
        ("📖", "GLOSARIO LEGAL"),
        ("🗺️", "MAPA CONCEPTUAL"),
        ("💬", "CONSULTORÍA VIRTUAL"),
        ("🏛", "BIBLIOTECA DOCTRINA"),
        ("🏛️", "QUIÉNES SOMOS"),
        ("💎", "SUSCRIPCIONES"),
    ]
    for icon, label in NAV_ITEMS:
        active = st.session_state.nav == label
        if active:
            st.markdown(
                f'<div style="border-left:2px solid #c9963a;'
                f'background:linear-gradient(90deg,rgba(201,150,58,0.12),rgba(201,150,58,0.04));'
                f'padding:0.58rem 1rem 0.58rem 0.85rem;'
                f'font-size:0.72rem;font-weight:700;'
                f'color:#c9963a;'
                f'text-transform:uppercase;letter-spacing:0.04em;'
                f'font-family:Inter,sans-serif;">'
                f'{icon} {label}</div>', unsafe_allow_html=True)
        else:
            st.button(f"{icon}  {label}", key=f"nav_{label}",
                      use_container_width=True,
                      on_click=set_nav, args=(label,))

    st.markdown('<hr style="border-color:rgba(255,255,255,0.07);margin:0.5rem 0;">', unsafe_allow_html=True)

    # ── MOTOR IA (hardcoded — invisible al usuario) ──
    # Anthropic Claude como único motor. API key desde secrets o env var.
    _provider_key = "anthropic"
    _model        = "claude-sonnet-4-20250514"
    _api_key      = (
        st.secrets.get("ANTHROPIC_API_KEY", "")
        if hasattr(st, "secrets")
        else os.environ.get("ANTHROPIC_API_KEY", "")
    )
    settings.llm_provider        = _provider_key
    settings.anthropic_api_key   = _api_key
    settings.anthropic_model     = _model

    # ── Indicador Biblioteca ──
    if _bib_activa:
        n_docs  = len(_bib_manifest)
        n_ramas = len(_bib_ramas)
        st.markdown(
            f'<div style="margin:0.5rem 0.4rem 0.3rem;padding:0.55rem 0.8rem;'
            f'background:rgba(46,144,85,0.08);border:1px solid rgba(46,144,85,0.25);'
            f'border-left:2px solid rgba(46,144,85,0.6);border-radius:0 6px 6px 0;">'
            f'<div style="font-size:0.6rem;font-weight:700;color:rgba(46,144,85,0.85);'
            f'text-transform:uppercase;letter-spacing:0.08em;">📚 Biblioteca activa</div>'
            f'<div style="font-size:0.65rem;color:rgba(200,220,200,0.7);margin-top:2px;">'
            f'{n_docs} obras · {n_ramas} ramas</div>'
            f'</div>',
            unsafe_allow_html=True)
    else:
        st.markdown(
            '<div style="margin:0.5rem 0.4rem 0.3rem;padding:0.55rem 0.8rem;'
            'background:rgba(180,134,12,0.06);border:1px solid rgba(180,134,12,0.18);'
            'border-left:2px solid rgba(180,134,12,0.4);border-radius:0 6px 6px 0;">'
            '<div style="font-size:0.6rem;font-weight:700;color:rgba(180,134,12,0.7);'
            'text-transform:uppercase;letter-spacing:0.08em;">📚 Biblioteca</div>'
            '<div style="font-size:0.62rem;color:rgba(200,180,100,0.5);margin-top:2px;">'
            'No indexada aún</div>'
            '</div>',
            unsafe_allow_html=True)

    st.markdown("""
    <div style="margin:0.3rem 0.4rem 0.8rem;padding:0.6rem 0.8rem;
                background:rgba(218,165,32,0.06);
                border:1px solid rgba(218,165,32,0.18);
                border-left:2px solid rgba(218,165,32,0.45);
                border-radius:0 6px 6px 0;
                font-size:0.67rem;color:rgba(218,165,32,0.7);line-height:1.5;">
      ⚠ Análisis académico. No constituye asesoría legal profesional.
    </div>""", unsafe_allow_html=True)


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
        Suba un archivo PDF, Word o TXT en el panel izquierdo para comenzar.
      </div>
    </div>""", unsafe_allow_html=True)

def doc_text(limit=5500):
    return st.session_state.ingestion_result.extraction.raw_text[:limit]

def make_gen():
    return StudyGenerator(get_llm(provider_key, api_key, model))

def active_llm():
    return get_llm(provider_key, api_key, model)

def section_header(title):
    return f'<div class="mc"><div class="mc-title">{title}</div>'

nav = st.session_state.nav


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
# SECCIÓN: ENTRENA
# ═══════════════════════════════════════════════
elif nav == "ENTRENA":
    llm = LLMClient() if settings.anthropic_api_key else None
    render_academia(llm_client=llm)


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
