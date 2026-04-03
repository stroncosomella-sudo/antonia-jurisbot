"""
abogado_module.py — AntonIA v4.1 · Módulo Abogados
Gestión profesional: causas, clientes, reportes diarios,
consulta Poder Judicial, plazos, documentos y honorarios.
"""

import streamlit as st
import datetime, re, json, hashlib
from typing import Optional
from pathlib import Path as _Path
import io as _io

@st.cache_data(ttl=600, show_spinner=False)
def _extract_doc_text(file_path: str) -> str:
    """Extrae texto de PDF, DOCX o TXT. Cacheado por path."""
    p = _Path(file_path)
    try:
        if p.suffix.lower() == ".pdf":
            import pypdf
            r = pypdf.PdfReader(str(p))
            return "\n".join(page.extract_text() or "" for page in r.pages)
        elif p.suffix.lower() == ".docx":
            import docx
            return "\n".join(par.text for par in docx.Document(str(p)).paragraphs)
        elif p.suffix.lower() in (".txt", ".md"):
            return p.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"[Error extrayendo texto: {e}]"
    return ""

def _get_library_path() -> _Path | None:
    """Retorna la ruta a doctrina_antonia/ o None si no existe."""
    candidates = [
        _Path(__file__).parent.parent.parent / "doctrina_antonia",
        _Path(__file__).parent.parent / "doctrina_antonia",
        _Path("/sessions/epic-blissful-fermat/mnt/doctrina_antonia"),
    ]
    for p in candidates:
        if p.exists() and p.is_dir():
            return p
    return None

# ── Colores ──────────────────────────────────────────────────────────────────
_GOLD  = "#c9963a"
_DARK  = "#141210"
_CARD  = "#1e1b16"
_RED   = "#ef4444"
_GREEN = "#22c55e"
_BLUE  = "#3b82f6"
_MUTED = "#a09070"
_WHITE = "#f5f0e8"

# ── Estilos ───────────────────────────────────────────────────────────────────
_CSS = """
<style>
/* Ocultar botones Streamlit de tabs (usamos HTML decorativo encima) */
[data-testid="stMainBlockContainer"] div[data-testid="column"] .stButton > button[kind="secondary"] {
    position:absolute !important;
    opacity:0 !important;
    height:100% !important;
    top:0 !important;
    left:0 !important;
    width:100% !important;
    cursor:pointer !important;
    z-index:10 !important;
}
[data-testid="stMainBlockContainer"] div[data-testid="column"] {
    position:relative !important;
    overflow:visible !important;
}
.abg-tab-header{font-family:'Playfair Display',serif;font-size:1.15rem;font-weight:700;
  color:#1a1813;margin-bottom:.2rem;}
.abg-tab-sub{font-size:.78rem;color:#c0b8a8;margin-bottom:1rem;}
.abg-card{background:#fff;border:1px solid #e2dbd0;border-left:3px solid #c9963a;
  border-radius:0 8px 8px 0;padding:.75rem 1rem;margin-bottom:.6rem;
  box-shadow:0 1px 4px rgba(20,18,10,.05);}
.abg-card-title{font-family:'Playfair Display',serif;font-size:.92rem;font-weight:700;color:#1a1813;}
.abg-badge{font-size:.62rem;font-weight:700;text-transform:uppercase;padding:2px 8px;
  border-radius:12px;letter-spacing:.05em;}
.badge-activo{background:rgba(34,197,94,.12);color:#15803d;}
.badge-pendiente{background:rgba(251,191,36,.12);color:#92400e;}
.badge-cerrado{background:rgba(160,144,112,.12);color:#9a8a6a;}
.abg-plazo-urgent{background:rgba(239,68,68,.08);border-left:3px solid #ef4444;
  border-radius:0 6px 6px 0;padding:.55rem .9rem;margin-bottom:.5rem;}
.abg-plazo-warning{background:rgba(251,191,36,.08);border-left:3px solid #fbbf24;
  border-radius:0 6px 6px 0;padding:.55rem .9rem;margin-bottom:.5rem;}
.abg-plazo-ok{background:rgba(34,197,94,.08);border-left:3px solid #22c55e;
  border-radius:0 6px 6px 0;padding:.55rem .9rem;margin-bottom:.5rem;}
.abg-report-card{background:linear-gradient(135deg,#fffcf5,#fff9ee);
  border:1px solid rgba(201,150,58,.25);border-radius:8px;padding:1.2rem 1.4rem;
  margin-bottom:.8rem;font-size:.84rem;line-height:1.7;color:#2a2015;}
.abg-pj-row{border-bottom:1px solid rgba(201,150,58,.1);padding:.5rem 0;
  font-size:.78rem;color:#3a3020;}
.abg-section-label{font-size:.68rem;font-weight:700;text-transform:uppercase;
  letter-spacing:.08em;color:#c9963a;margin-bottom:.6rem;margin-top:1.2rem;}
.abg-activity{background:rgba(201,150,58,.05);border-left:2px solid rgba(201,150,58,.3);
  padding:.4rem .7rem;margin-bottom:.4rem;font-size:.76rem;color:#5a4a30;border-radius:0 4px 4px 0;}
</style>
"""

# ── Competencias OJV ────────────────────────────────────────────────────────
_COMP_MAP = {
    "Civil":              "3",
    "Laboral":            "4",
    "Penal":              "5",
    "Cobranza":           "6",
    "Familia":            "7",
    "Corte de Apelaciones": "2",
    "Corte Suprema":      "1",
}

_OJV_BASE = "https://oficinajudicialvirtual.pjud.cl/"

_ENDPOINT_RIT = {
    "1": "ADIR_871/suprema/consultaRitSuprema.php",
    "2": "ADIR_871/apelaciones/consultaRitApelaciones.php",
    "3": "ADIR_871/civil/consultaRitCivil.php",
    "4": "ADIR_871/laboral/consultaRitLaboral.php",
    "5": "ADIR_871/penal/consultaRitPenal.php",
    "6": "ADIR_871/cobranza/consultaRitCobranza.php",
    "7": "ADIR_871/familia/consultaRitFamilia.php",
}

# ── Defaults ─────────────────────────────────────────────────────────────────
DEFAULTS = {
    "abg_tab":          "casos",
    "abg_casos":        [],
    "abg_plazos":       [],
    "abg_tasks":        [],
    "abg_honorarios":   [],
    "abg_timer_acum":   {},
    "abg_timer_start":  None,
    "abg_timer_causa":  None,
    "abg_correo_result":"",
    "abg_doc_result":   "",
    "abg_hon_propuesta":"",
    "abg_reportes":     [],
    "abg_report_draft": "",
    "abg_pj_result":    "",
    "abg_pj_cortes":    {},
    "abg_pj_tribs":     {},
    "abg_caso_sel":     None,
}

def _init():
    for k, v in DEFAULTS.items():
        if k not in st.session_state:
            st.session_state[k] = v if not isinstance(v, (list, dict)) else type(v)()

# ── PJ Helper functions ───────────────────────────────────────────────────────
def _pjud_session():
    """Crea sesión OJV sin autenticación (acceso consulta unificada)."""
    try:
        import requests as _req
        s = _req.Session()
        s.headers.update({
            "User-Agent":       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer":          _OJV_BASE + "consultaUnificada.php",
            "Accept":           "*/*",
        })
        s.post(_OJV_BASE + "includes/sesion-invitado.php", data={"nombreAcceso": "CC"}, timeout=10)
        s.get(_OJV_BASE + "consultaUnificada.php", timeout=8)
        return s
    except Exception:
        return None


def _pjud_get_cortes(comp_code: str) -> dict:
    """Devuelve {code: nombre} para las cortes de una competencia."""
    cache_key = f"pj_cortes_{comp_code}"
    if st.session_state.abg_pj_cortes.get(cache_key):
        return st.session_state.abg_pj_cortes[cache_key]
    try:
        s = _pjud_session()
        if not s:
            return {}
        r = s.post(_OJV_BASE + "ADIR_871/json/comboCausas.php",
                   data={"codCompetencia": comp_code, "accion": "cmbCorte", "tabs": "60"}, timeout=10)
        cortes = dict(re.findall(r'value=["\'](\d+)["\'][^>]*>\s*([^\s<][^<]+?)\s*<', r.text))
        cortes = {k: v.strip() for k, v in cortes.items() if k != "0"}
        st.session_state.abg_pj_cortes[cache_key] = cortes
        return cortes
    except Exception:
        return {}


def _pjud_get_tribunales(comp_code: str, corte_code: str) -> dict:
    """Devuelve {code: nombre} para los tribunales de una corte."""
    cache_key = f"pj_tribs_{comp_code}_{corte_code}"
    if st.session_state.abg_pj_tribs.get(cache_key):
        return st.session_state.abg_pj_tribs[cache_key]
    try:
        s = _pjud_session()
        if not s:
            return {}
        r = s.post(_OJV_BASE + "ADIR_871/json/comboCausas.php",
                   data={"codCompetencia": comp_code, "accion": "cmbTribunal",
                         "codCorte": corte_code, "tabs": "60"}, timeout=10)
        tribs = dict(re.findall(r'value=["\'](\d+)["\'][^>]*>\s*([^\s<][^<]+?)\s*<', r.text))
        tribs = {k: v.strip() for k, v in tribs.items() if k != "0"}
        st.session_state.abg_pj_tribs[cache_key] = tribs
        return tribs
    except Exception:
        return {}


def _pjud_consultar(comp_code: str, corte_code: str, trib_code: str, rol: str, anio: str) -> str:
    """
    Consulta Poder Judicial OJV sin CAPTCHA.
    Devuelve HTML con tabla de resultados o mensaje de error.
    """
    endpoint = _ENDPOINT_RIT.get(comp_code, "ADIR_871/civil/consultaRitCivil.php")
    try:
        s = _pjud_session()
        if not s:
            return "<em>No se pudo conectar con Poder Judicial</em>"
        r = s.post(_OJV_BASE + endpoint, data={
            "token":        "",
            "conRolCausa":  rol,
            "conEraCausa":  anio,
            "conCorte":     corte_code,
            "conTribunal":  trib_code,
            "competencia":  comp_code,
        }, timeout=15)
        if "No se han encontrado resultados" in r.text:
            return ""
        return r.text
    except Exception as e:
        return f"<em>Error de conexión: {e}</em>"


def _parse_pjud_table(html: str) -> list:
    """
    Parsea la tabla HTML de resultados OJV y devuelve lista de dicts
    con keys: rol, caratulado, tribunal, estado, ultima_actuacion, fecha
    """
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL | re.IGNORECASE)
    results = []
    for row in rows:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL | re.IGNORECASE)
        if not cells or len(cells) < 2:
            continue
        clean = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
        clean = [c for c in clean if c]
        if len(clean) >= 2:
            results.append({
                "col0": clean[0] if len(clean) > 0 else "",
                "col1": clean[1] if len(clean) > 1 else "",
                "col2": clean[2] if len(clean) > 2 else "",
                "col3": clean[3] if len(clean) > 3 else "",
                "col4": clean[4] if len(clean) > 4 else "",
                "_raw": clean,
            })
    return results


# ── Helpers UI ────────────────────────────────────────────────────────────────
def _caso_label(c: dict) -> str:
    return f"{c['rol']} — {c['partes'][:35]}"

def _fmt_monto(m: int) -> str:
    return f"${m:,.0f}"



# ═══════════════════════════════════════════════════════════════════════════════
# RENDER PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════
def render_abogado(get_llm_fn=None):
    _init()
    st.markdown(_CSS, unsafe_allow_html=True)

    TABS = [
        ("📁", "casos",       "Causas"),
        ("⏱",  "cronometro",  "Tiempo"),
        ("📅", "plazos",      "Plazos"),
        ("📊", "reportes",    "Reportes"),
        ("📚", "doctrina",    "Doctrina & Jurispr."),
        ("📝", "redaccion",   "Redactar Doc."),
        ("✉️", "correos",     "Correos"),
        ("📋", "pendientes",  "Pendientes"),
        ("📄", "documentos",  "Documentos"),
        ("💰", "honorarios",  "Honorarios"),
    ]
    # ── Navegación en 2 filas: 5 + 5 tabs ──
    st.markdown(f"""<style>
    [data-testid="stMainBlockContainer"] .abg-tab-active {{
        display:block;
        padding:0.38rem 0.4rem;
        background:rgba(201,150,58,0.18) !important;
        border:1px solid {_GOLD} !important;
        border-radius:6px;
        text-align:center;
        font-size:0.73rem;
        font-weight:700;
        color:{_GOLD};
        font-family:'Inter',sans-serif;
        letter-spacing:0.02em;
        white-space:nowrap;
    }}
    </style>""", unsafe_allow_html=True)

    def _abg_tab_row(subset):
        cols = st.columns(len(subset))
        for col, (icon, tid, label) in zip(cols, subset):
            if st.session_state.abg_tab == tid:
                col.markdown(
                    f'<div class="abg-tab-active">{icon} {label}</div>',
                    unsafe_allow_html=True)
            else:
                if col.button(f"{icon} {label}", key=f"abg_tab_{tid}",
                              use_container_width=True):
                    st.session_state.abg_tab = tid
                    st.rerun()

    _abg_tab_row(TABS[:5])   # Fila 1: Causas · Tiempo · Plazos · Reportes · Consulta PJ
    st.markdown('<div style="height:0.3rem"></div>', unsafe_allow_html=True)
    _abg_tab_row(TABS[5:])   # Fila 2: Correos · Pendientes · Documentos · Honorarios

    st.markdown('<hr style="border-color:rgba(201,150,58,.2);margin:.5rem 0 1rem;">', unsafe_allow_html=True)
    tab = st.session_state.abg_tab

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: CAUSAS
    # ═══════════════════════════════════════════════════════════════════════════
    if tab == "casos":
        st.markdown('<div class="abg-tab-header">📁 Cartera de Causas</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Registro, clientes y seguimiento de causas activas</div>', unsafe_allow_html=True)

        col_form, col_list = st.columns([1, 1.7])

        with col_form:
            with st.expander("➕ Nueva Causa", expanded=not st.session_state.abg_casos):
                rol      = st.text_input("ROL / RIT", placeholder="C-1234-2025", key="abg_caso_rol")
                tribunal = st.text_input("Tribunal", placeholder="1° Juzgado Civil Santiago", key="abg_caso_trib")
                partes   = st.text_input("Partes (Demandante vs. Demandado)", key="abg_caso_partes")
                materia  = st.selectbox("Materia", [
                    "Civil — General", "Civil — Obligaciones", "Civil — Bienes",
                    "Civil — Familia", "Civil — Sucesorio",
                    "Penal", "Laboral", "Comercial", "Constitucional",
                    "Contencioso-Administrativo", "Otra",
                ], key="abg_caso_materia")
                estado   = st.selectbox("Estado", ["Activo", "Pendiente", "Cerrado"], key="abg_caso_estado")
                # Datos del cliente
                st.markdown('<div class="abg-section-label">Cliente</div>', unsafe_allow_html=True)
                cli_nombre = st.text_input("Nombre cliente", key="abg_caso_cli_nom")
                cli_email  = st.text_input("Email cliente", placeholder="cliente@correo.com", key="abg_caso_cli_email")
                cli_rut    = st.text_input("RUT cliente (opcional)", key="abg_caso_cli_rut")
                cli_tel    = st.text_input("Teléfono (opcional)", key="abg_caso_cli_tel")
                # Datos OJV para consulta automática
                st.markdown('<div class="abg-section-label">Consulta PJ (opcional)</div>', unsafe_allow_html=True)
                pj_comp_label = st.selectbox("Competencia PJ", list(_COMP_MAP.keys()), key="abg_caso_pj_comp")
                pj_rol    = st.text_input("ROL numérico (solo número)", placeholder="1234", key="abg_caso_pj_rol")
                pj_anio   = st.text_input("Año", value=str(datetime.date.today().year), key="abg_caso_pj_anio")
                notas     = st.text_area("Notas iniciales", key="abg_caso_notas", height=80)

                if st.button("💾 Guardar Causa", use_container_width=True, type="primary"):
                    if rol and partes:
                        nuevo = {
                            "id":         f"caso_{len(st.session_state.abg_casos)+1}_{hashlib.md5(rol.encode()).hexdigest()[:6]}",
                            "rol":        rol,
                            "tribunal":   tribunal,
                            "partes":     partes,
                            "materia":    materia,
                            "estado":     estado.lower(),
                            "notas":      notas,
                            "horas":      0.0,
                            "fecha":      datetime.date.today().isoformat(),
                            "cliente":    {"nombre": cli_nombre, "email": cli_email,
                                           "rut": cli_rut, "tel": cli_tel},
                            "pj_comp":    _COMP_MAP.get(pj_comp_label, "3"),
                            "pj_rol":     pj_rol,
                            "pj_anio":    pj_anio,
                            "actividades": [],
                        }
                        st.session_state.abg_casos.append(nuevo)
                        st.success("✓ Causa guardada")
                        st.rerun()
                    else:
                        st.warning("Completa ROL y Partes.")

        with col_list:
            casos = st.session_state.abg_casos
            if not casos:
                st.markdown(
                    '<div style="text-align:center;padding:3rem 1rem;color:#c0a880;font-size:.85rem;">'
                    '📁 Aún no hay causas registradas.<br>'
                    '<span style="font-size:.72rem;">Agrega tu primera causa a la izquierda.</span>'
                    '</div>', unsafe_allow_html=True)
            else:
                filtro = st.selectbox("Filtrar", ["Todas", "Activo", "Pendiente", "Cerrado"], key="abg_filtro", label_visibility="collapsed")
                casos_vis = [c for c in reversed(casos) if filtro == "Todas" or c["estado"] == filtro.lower()]

                for c in casos_vis:
                    badge_cls = {"activo":"badge-activo","pendiente":"badge-pendiente","cerrado":"badge-cerrado"}.get(c["estado"],"badge-pendiente")
                    horas_str = f"{st.session_state.abg_timer_acum.get(c['id'],0)/3600:.1f}h"
                    cli_str   = c.get("cliente", {}).get("nombre", "")

                    with st.expander(f"📁 {c['rol']} — {c['partes'][:40]}", expanded=False):
                        col_info, col_acc = st.columns([3, 1])
                        with col_info:
                            notas_html = ('<div style="font-size:.72rem;color:#c8b890;margin-top:6px;">' + c["notas"][:100] + "…</div>") if c.get("notas") else ""
                            cli_html   = ("  · 👤 " + cli_str) if cli_str else ""
                            card_html  = (
                                '<div class="abg-card">'
                                '<div style="display:flex;justify-content:space-between;align-items:flex-start;">'
                                f'<div class="abg-card-title">{c["rol"]} — {c["partes"][:50]}</div>'
                                f'<span class="abg-badge {badge_cls}">{c["estado"]}</span>'
                                '</div>'
                                f'<div style="font-size:.68rem;color:#c0a880;margin-top:4px;">'
                                f'{c["materia"]} · {c["tribunal"][:40]} · ⏱ {horas_str}{cli_html}'
                                '</div>'
                                + notas_html +
                                '</div>'
                            )
                            st.markdown(card_html, unsafe_allow_html=True)

                            # Actividad log
                            actividades = c.get("actividades", [])
                            if actividades:
                                st.markdown('<div class="abg-section-label">Últimas actividades</div>', unsafe_allow_html=True)
                                for act in reversed(actividades[-5:]):
                                    st.markdown(
                                        f'<div class="abg-activity">📌 {act["fecha"]} · {act["texto"][:120]}</div>',
                                        unsafe_allow_html=True)

                        with col_acc:
                            # Acción rápida: agregar actividad
                            nueva_act = st.text_area("Agregar nota", height=60, key=f"act_txt_{c['id']}",
                                                     placeholder="Ej: Audiencia realizada...")
                            if st.button("📌 Agregar", key=f"act_add_{c['id']}", use_container_width=True):
                                if nueva_act:
                                    if "actividades" not in c:
                                        c["actividades"] = []
                                    c["actividades"].append({
                                        "fecha": datetime.date.today().isoformat(),
                                        "texto": nueva_act,
                                    })
                                    st.success("✓ Nota agregada")
                                    st.rerun()

                            # Consulta rápida PJ
                            if c.get("pj_rol") and c.get("pj_comp"):
                                if st.button("🌐 Ver PJ", key=f"pj_quick_{c['id']}", use_container_width=True,
                                             help="Consultar estado en Poder Judicial"):
                                    st.session_state.abg_tab = "doctrina"
                                    st.session_state["abg_pj_prefill"] = {
                                        "comp": c["pj_comp"], "rol": c["pj_rol"], "anio": c["pj_anio"]
                                    }
                                    st.rerun()

                            # Reporte rápido
                            if st.button("📊 Reporte", key=f"rep_quick_{c['id']}", use_container_width=True,
                                         help="Generar reporte para cliente"):
                                st.session_state.abg_tab = "reportes"
                                st.session_state["abg_rep_prefill"] = c["id"]
                                st.rerun()

                            # Cambiar estado
                            nuevo_estado = st.selectbox("Estado", ["activo","pendiente","cerrado"],
                                                        index=["activo","pendiente","cerrado"].index(c["estado"]),
                                                        key=f"est_{c['id']}", label_visibility="collapsed")
                            if nuevo_estado != c["estado"]:
                                c["estado"] = nuevo_estado
                                st.rerun()


    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: CRONÓMETRO
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "cronometro":
        st.markdown('<div class="abg-tab-header">⏱ Cronómetro de Horas</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Registro de tiempo facturable por causa</div>', unsafe_allow_html=True)

        casos_ids     = [_caso_label(c) for c in st.session_state.abg_casos]
        casos_ids_raw = [c["id"] for c in st.session_state.abg_casos]

        if not casos_ids:
            st.info("Primero registra una causa en la pestaña **Causas**.")
        else:
            sel_idx = st.selectbox("Causa", range(len(casos_ids)), format_func=lambda i: casos_ids[i], key="abg_crono_sel")
            caso_id = casos_ids_raw[sel_idx]

            now = datetime.datetime.now()
            acum = st.session_state.abg_timer_acum.get(caso_id, 0)

            col_t, col_btn = st.columns([2, 1])
            if st.session_state.abg_timer_start and st.session_state.abg_timer_causa == caso_id:
                elapsed = (now - st.session_state.abg_timer_start).total_seconds() + acum
                with col_t:
                    h, r  = divmod(int(elapsed), 3600)
                    m, s  = divmod(r, 60)
                    st.markdown(
                        f'<div style="font-family:monospace;font-size:2.5rem;color:#c9963a;'
                        f'text-align:center;padding:1rem;">{h:02d}:{m:02d}:{s:02d}</div>',
                        unsafe_allow_html=True)
                with col_btn:
                    if st.button("⏹ DETENER", use_container_width=True, type="primary"):
                        elapsed_final = (now - st.session_state.abg_timer_start).total_seconds() + acum
                        st.session_state.abg_timer_acum[caso_id] = elapsed_final
                        st.session_state.abg_timer_start = None
                        st.session_state.abg_timer_causa = None
                        st.rerun()
            else:
                h, r  = divmod(int(acum), 3600)
                m, s  = divmod(r, 60)
                with col_t:
                    st.markdown(
                        f'<div style="font-family:monospace;font-size:2.5rem;color:#c0b8a8;'
                        f'text-align:center;padding:1rem;">{h:02d}:{m:02d}:{s:02d}</div>',
                        unsafe_allow_html=True)
                with col_btn:
                    if st.button("▶ INICIAR", use_container_width=True, type="primary"):
                        st.session_state.abg_timer_start = now
                        st.session_state.abg_timer_causa = caso_id
                        st.rerun()

            # Manual add
            with st.expander("➕ Agregar horas manualmente"):
                col_h, col_m = st.columns(2)
                hrs_man = col_h.number_input("Horas", 0, 24, 0, key="crono_hrs")
                min_man = col_m.number_input("Minutos", 0, 59, 0, key="crono_min")
                if st.button("Agregar tiempo", use_container_width=True):
                    add_secs = hrs_man * 3600 + min_man * 60
                    st.session_state.abg_timer_acum[caso_id] = acum + add_secs
                    st.success(f"✓ {hrs_man}h {min_man}m agregados")
                    st.rerun()

            # Resumen por causa
            if st.session_state.abg_timer_acum:
                st.markdown('<div class="abg-section-label">Acumulado por causa</div>', unsafe_allow_html=True)
                for c in st.session_state.abg_casos:
                    secs = st.session_state.abg_timer_acum.get(c["id"], 0)
                    if secs > 0:
                        h2, r2 = divmod(int(secs), 3600)
                        m2, _  = divmod(r2, 60)
                        st.markdown(
                            f'<div class="abg-pj-row"><strong>{c["rol"]}</strong> — {c["partes"][:35]} '
                            f'<span style="float:right;color:#c9963a;font-weight:700;">{h2}h {m2}m</span></div>',
                            unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: PLAZOS
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "plazos":
        st.markdown('<div class="abg-tab-header">📅 Agenda de Plazos</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Vencimientos procesales, audiencias y notificaciones</div>', unsafe_allow_html=True)

        col_add, col_list = st.columns([1, 1.5])
        with col_add:
            casos_opts = ["(sin causa)"] + [_caso_label(c) for c in st.session_state.abg_casos]
            pl_causa_idx = st.selectbox("Causa", range(len(casos_opts)), format_func=lambda i: casos_opts[i], key="abg_pl_ci")
            pl_causa = casos_opts[pl_causa_idx] if pl_causa_idx > 0 else ""
            tipo     = st.selectbox("Tipo", ["Audiencia", "Vencimiento plazo", "Notificación pendiente",
                                              "Escrito a presentar", "Perención", "Otra"], key="abg_pl_tipo")
            fecha    = st.date_input("Fecha", key="abg_pl_fecha")
            hora     = st.time_input("Hora (opcional)", value=None, key="abg_pl_hora")
            nota_pl  = st.text_input("Descripción", key="abg_pl_nota")

            if st.button("📌 Agregar plazo", use_container_width=True, type="primary"):
                if nota_pl:
                    st.session_state.abg_plazos.append({
                        "tipo":  tipo,
                        "fecha": fecha.isoformat(),
                        "hora":  str(hora) if hora else "",
                        "causa": pl_causa,
                        "nota":  nota_pl,
                        "done":  False,
                    })
                    st.success("✓ Plazo agregado")
                    st.rerun()

        with col_list:
            plazos = sorted(
                [p for p in st.session_state.abg_plazos if not p.get("done")],
                key=lambda x: x["fecha"]
            )
            if not plazos:
                st.markdown('<div style="text-align:center;padding:2rem;color:#c0a880;">📅 Sin plazos pendientes.</div>', unsafe_allow_html=True)
            else:
                hoy = datetime.date.today()
                for i, p in enumerate(plazos):
                    fdate  = datetime.date.fromisoformat(p["fecha"])
                    dias   = (fdate - hoy).days
                    if   dias < 0:    cls, color, txt = "abg-plazo-urgent",  _RED,    f"Venció hace {-dias}d"
                    elif dias == 0:   cls, color, txt = "abg-plazo-urgent",  _RED,    "HOY"
                    elif dias <= 3:   cls, color, txt = "abg-plazo-warning", "#fbbf24", f"En {dias} día{'s' if dias != 1 else ''}"
                    else:             cls, color, txt = "abg-plazo-ok",      _GREEN,   f"En {dias} días"

                    col_pl, col_btn = st.columns([5, 1])
                    with col_pl:
                        st.markdown(
                            f'<div class="{cls}">'
                            f'<div style="display:flex;justify-content:space-between;">'
                            f'<span style="font-size:.8rem;font-weight:700;color:#1a1813;">{p["tipo"]} · {p["nota"]}</span>'
                            f'<span style="font-size:.72rem;color:{color};font-weight:700;">{txt}</span>'
                            f'</div>'
                            f'<div style="font-size:.67rem;color:#c0a880;margin-top:2px;">'
                            f'{p["fecha"]}{" " + p["hora"] if p.get("hora") else ""}'
                            f'{" · " + p["causa"] if p.get("causa") else ""}'
                            f'</div></div>', unsafe_allow_html=True)
                    with col_btn:
                        orig_idx = st.session_state.abg_plazos.index(p)
                        if st.button("✓", key=f"pl_done_{orig_idx}", help="Marcar cumplido"):
                            st.session_state.abg_plazos[orig_idx]["done"] = True
                            st.rerun()


    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: REPORTES DIARIOS (NEW)
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "reportes":
        st.markdown('<div class="abg-tab-header">📊 Reportes al Cliente</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Genera y envía reportes diarios de estado de causa a tus clientes</div>', unsafe_allow_html=True)

        casos = st.session_state.abg_casos
        if not casos:
            st.info("Primero registra causas en la pestaña **Causas**.")
        else:
            col_cfg, col_prev = st.columns([1, 1.4])

            with col_cfg:
                # Pre-fill si viene desde botón "Reporte" en Causas
                _prefill_id = st.session_state.pop("abg_rep_prefill", None)
                casos_labels = [_caso_label(c) for c in casos]
                default_idx = 0
                if _prefill_id:
                    for idx, c in enumerate(casos):
                        if c["id"] == _prefill_id:
                            default_idx = idx
                            break

                sel_idx  = st.selectbox("Causa", range(len(casos_labels)),
                                        format_func=lambda i: casos_labels[i],
                                        index=default_idx, key="rep_caso_idx")
                caso_sel = casos[sel_idx]
                cli      = caso_sel.get("cliente", {})
                cli_nom  = cli.get("nombre", "")
                cli_email= cli.get("email",  "")

                st.markdown(f'<div style="font-size:.74rem;color:#c0b8a8;margin:.3rem 0 .8rem;">'
                            f'👤 Cliente: <strong>{cli_nom or "(sin nombre)"}</strong>'
                            f'{"  ·  📧 " + cli_email if cli_email else ""}</div>', unsafe_allow_html=True)

                tipo_rep = st.selectbox("Tipo de reporte", [
                    "Estado diario de la causa",
                    "Resultado de audiencia",
                    "Actuación procesal realizada",
                    "Resumen semanal",
                    "Notificación a cliente",
                    "Alerta de plazo próximo",
                ], key="rep_tipo")

                novedades = st.text_area(
                    "¿Qué novedades hay hoy?",
                    height=130,
                    placeholder="Ej: Se realizó la audiencia preparatoria. El juez ordenó prueba testimonial. Próxima audiencia fijada para el 15/04/2025 a las 10:00 hrs.",
                    key="rep_novedades")

                tono_rep = st.radio("Tono", ["Formal", "Cordial", "Detallado"], horizontal=True, key="rep_tono")
                incluir_prox = st.checkbox("Incluir próximos pasos", value=True, key="rep_prox")
                incluir_plazos_rep = st.checkbox("Incluir plazos pendientes de esta causa", value=True, key="rep_plazos")

                # Plazos de esta causa
                plazos_causa = [p for p in st.session_state.abg_plazos
                                if not p.get("done") and caso_sel["rol"] in p.get("causa", "")]

                if st.button("🤖 Generar Reporte con IA", use_container_width=True, type="primary"):
                    if novedades and get_llm_fn:
                        plazos_txt = ""
                        if incluir_plazos_rep and plazos_causa:
                            plazos_txt = "\n\nPLAZOS PENDIENTES:\n" + "\n".join(
                                [f"- {p['tipo']}: {p['nota']} ({p['fecha']})" for p in plazos_causa[:5]])
                        horas_acum = st.session_state.abg_timer_acum.get(caso_sel["id"], 0) / 3600

                        prompt = (
                            f"Eres un abogado chileno redactando un reporte para su cliente.\n"
                            f"ROL/RIT: {caso_sel['rol']}\n"
                            f"Partes: {caso_sel['partes']}\n"
                            f"Tribunal: {caso_sel['tribunal']}\n"
                            f"Materia: {caso_sel['materia']}\n"
                            f"Horas trabajadas total: {horas_acum:.1f}h\n"
                            f"Cliente: {cli_nom or 'estimado cliente'}\n\n"
                            f"TIPO DE REPORTE: {tipo_rep}\n"
                            f"TONO: {tono_rep}\n"
                            f"NOVEDADES DEL DÍA:\n{novedades}"
                            f"{plazos_txt}\n\n"
                            f"INSTRUCCIONES:\n"
                            f"1. Redacta el reporte en español chileno, dirigido al cliente\n"
                            f"2. Comienza con la fecha de hoy ({datetime.date.today().strftime('%d de %B de %Y')})\n"
                            f"3. Usa lenguaje {'técnico-jurídico' if tono_rep == 'Formal' else 'claro y accesible'}\n"
                            f"4. {'Incluye sección de próximos pasos y recomendaciones' if incluir_prox else ''}\n"
                            f"5. Cierra con firma profesional [Nombre Abogado] · [Teléfono] · [Email]\n"
                            f"6. Máximo 350 palabras, directo y útil para el cliente\n"
                            f"7. NUNCA especules ni inventes hechos no indicados en las novedades"
                        )
                        with st.spinner("Generando reporte…"):
                            try:
                                llm = get_llm_fn()
                                resp = llm.generate(prompt, system="Eres AntonIA, asistente jurídico para abogados chilenos. Proporciona análisis precisos del Derecho chileno.", max_tokens=1200)
                                st.session_state.abg_report_draft = resp
                                # Guardar en historial
                                st.session_state.abg_reportes.append({
                                    "fecha":    datetime.date.today().isoformat(),
                                    "caso_rol": caso_sel["rol"],
                                    "caso_id":  caso_sel["id"],
                                    "tipo":     tipo_rep,
                                    "cliente":  cli_nom,
                                    "email":    cli_email,
                                    "resumen":  novedades[:100],
                                })
                                # Agregar a actividades de la causa
                                if "actividades" not in caso_sel:
                                    caso_sel["actividades"] = []
                                caso_sel["actividades"].append({
                                    "fecha": datetime.date.today().isoformat(),
                                    "texto": f"Reporte enviado al cliente: {novedades[:80]}",
                                })
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error: {e}")
                    elif not get_llm_fn:
                        st.warning("API no disponible. Configura tu API key en console.anthropic.com")
                    else:
                        st.warning("Describe las novedades del día.")

            with col_prev:
                if st.session_state.abg_report_draft:
                    st.markdown('<div class="abg-section-label">Reporte generado</div>', unsafe_allow_html=True)

                    rep_editado = st.text_area(
                        "Edita antes de enviar:",
                        value=st.session_state.abg_report_draft,
                        height=380, key="rep_edit")

                    col_cp, col_email = st.columns(2)
                    with col_cp:
                        if st.button("📋 Copiar texto", use_container_width=True):
                            st.code(rep_editado, language=None)
                            st.caption("Selecciona todo el texto de arriba y copia (Ctrl+A, Ctrl+C)")

                    with col_email:
                        if cli_email:
                            mailto = f"mailto:{cli_email}?subject=Estado%20Causa%20{caso_sel['rol']}&body={rep_editado[:500].replace(' ','%20').replace(chr(10),'%0A')}"
                            st.markdown(
                                f'<a href="{mailto}" target="_blank">'
                                f'<button style="width:100%;background:#c9963a;color:#fff;'
                                f'border:none;border-radius:6px;padding:.5rem;cursor:pointer;'
                                f'font-size:.8rem;font-weight:700;">📧 Abrir en correo</button></a>',
                                unsafe_allow_html=True)
                        else:
                            st.caption("Agrega email del cliente en la causa para enviar directamente")

                    # Historial
                    if st.session_state.abg_reportes:
                        st.markdown('<div class="abg-section-label">Historial de reportes</div>', unsafe_allow_html=True)
                        for rep in reversed(st.session_state.abg_reportes[-8:]):
                            st.markdown(
                                f'<div class="abg-pj-row">📊 {rep["fecha"]} · {rep["caso_rol"]} · '
                                f'{rep["tipo"]} · <em>{rep["cliente"] or "sin cliente"}</em></div>',
                                unsafe_allow_html=True)
                else:
                    st.markdown(
                        '<div style="height:320px;display:flex;flex-direction:column;'
                        'align-items:center;justify-content:center;gap:1rem;'
                        'border:1px dashed rgba(201,150,58,.2);border-radius:8px;'
                        'color:#c0a880;font-size:.82rem;text-align:center;">'
                        '📊<br><strong style="color:#c9963a;">Reporte diario al cliente</strong><br>'
                        'Selecciona una causa, describe las novedades<br>y AntonIA genera el reporte listo para enviar.'
                        '</div>', unsafe_allow_html=True)


    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: CONSULTA PODER JUDICIAL (NEW)
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "doctrina":
        st.markdown('<div class="abg-tab-header">📚 Doctrina y Jurisprudencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Búsqueda precisa en la biblioteca de AntonIA · Sin alucinaciones — solo fuentes verificadas</div>', unsafe_allow_html=True)
        # ── SELECTOR DE FUENTE ──────────────────────────────────────
        _lib_path = _get_library_path()
        _source_opts = ["🤖 Consulta IA (knowledge base)", "📚 Biblioteca Local (documentos propios)"]
        _source = st.radio("Fuente de consulta", _source_opts, horizontal=True, key="abg_doc_source_sel")

        if _source == _source_opts[1]:  # Biblioteca Local
            if _lib_path is None:
                st.info("📚 La biblioteca local no está disponible en esta versión. Usa 'Consulta IA' para acceder a doctrina y jurisprudencia.")
            else:
                ramas_disponibles = sorted([d.name for d in _lib_path.iterdir() if d.is_dir()])
                if not ramas_disponibles:
                    st.warning("No se encontraron carpetas en la biblioteca local.")
                else:
                    rama_bib = st.selectbox("Rama del Derecho", ramas_disponibles, key="bib_rama_sel")
                    rama_path = _lib_path / rama_bib
                    archivos_disp = sorted([
                        f.name for f in rama_path.iterdir()
                        if f.suffix.lower() in (".pdf", ".docx", ".txt", ".md")
                    ])
                    if not archivos_disp:
                        st.warning(f"No hay documentos en '{rama_bib}'.")
                    else:
                        archivo_bib = st.selectbox(f"Documento ({len(archivos_disp)} disponibles)", archivos_disp, key="bib_archivo_sel")
                        consulta_bib = st.text_area(
                            "¿Qué quieres saber de este documento?",
                            placeholder="Ej: Explica los requisitos de la condición resolutoria ordinaria según este autor.",
                            height=90, key="bib_query_input")
                        col_bib1, col_bib2 = st.columns([1, 1])
                        with col_bib1:
                            modo_bib = st.radio("Modo", ["Búsqueda puntual", "Resumen del documento"], key="bib_modo")
                        with col_bib2:
                            max_chars_bib = st.slider("Contexto (caracteres)", 5000, 40000, 16000, 1000, key="bib_maxchars")
                        if st.button("🔍 Consultar documento", type="primary", use_container_width=True, key="bib_btn_buscar"):
                            if not consulta_bib.strip() and modo_bib == "Búsqueda puntual":
                                st.warning("Escribe tu consulta.")
                            elif get_llm_fn:
                                with st.spinner(f"Leyendo {archivo_bib}…"):
                                    texto_doc = _extract_doc_text(str(rama_path / archivo_bib))
                                if texto_doc.startswith("[Error"):
                                    st.error(texto_doc)
                                else:
                                    ctx = texto_doc[:max_chars_bib]
                                    if modo_bib == "Resumen del documento":
                                        prompt_bib = (
                                            f"Documento jurídico: '{archivo_bib}'\n"
                                            f"Contenido ({len(ctx):,} chars):\n{ctx}\n\n"
                                            f"Genera un resumen ejecutivo estructurado del documento con: "
                                            f"1) Tema central y tesis del autor, "
                                            f"2) Conceptos jurídicos clave desarrollados, "
                                            f"3) Normas y artículos citados, "
                                            f"4) Conclusiones principales, "
                                            f"5) Relevancia práctica para litigantes chilenos."
                                        )
                                    else:
                                        prompt_bib = (
                                            f"Documento jurídico: '{archivo_bib}'\n"
                                            f"Contenido:\n{ctx}\n\n"
                                            f"Consulta del abogado: {consulta_bib}\n\n"
                                            f"Responde basándote EXCLUSIVAMENTE en el contenido del documento. "
                                            f"Cita los pasajes relevantes con comillas y número de sección si lo hay. "
                                            f"Si la respuesta no está en el documento, indícalo claramente."
                                        )
                                    system_bib = (
                                        "Eres AntonIA, asistente jurídico para abogados chilenos. "
                                        "Analizas documentos jurídicos con precisión académica. "
                                        "Citas textualmente los pasajes relevantes. "
                                        "Usas terminología jurídica chilena vigente."
                                    )
                                    try:
                                        llm = get_llm_fn()
                                        resp_bib = llm.generate(prompt_bib, system=system_bib, max_tokens=2000)
                                        st.markdown(f"**📄 {archivo_bib}**")
                                        st.markdown(resp_bib)
                                        st.caption(f"Contexto usado: {len(ctx):,} de {len(texto_doc):,} caracteres totales")
                                    except Exception as e:
                                        st.error(f"Error: {e}")
                            else:
                                st.warning("LLM no disponible.")
            st.stop()
        col_busq, col_res = st.columns([1, 1.6])
        with col_busq:
            tipo_consulta = st.selectbox("Tipo de consulta", [
                "Doctrina sobre un tema", "Jurisprudencia chilena",
                "Normativa vigente aplicable", "Análisis de caso con fundamentos",
                "Comparación de posiciones doctrinales",
            ], key="abg_doc_tipo_consulta")
            ramo_doc = st.selectbox("Rama del Derecho", [
                "Civil — General", "Civil — Obligaciones", "Civil — Bienes",
                "Civil — Familia", "Civil — Sucesorio",
                "Penal General", "Penal Especial", "Procesal Civil", "Procesal Penal",
                "Laboral", "Comercial", "Constitucional", "Administrativo",
            ], key="abg_doc_ramo")
            consulta_text = st.text_area(
                "Consulta o tema específico",
                placeholder="Ej: Requisitos de la acción resolutoria en contratos bilaterales. Art. 1489 CC.",
                height=120, key="abg_doc_consulta")
            nivel_precision = st.radio("Nivel de precisión",
                ["Resumen ejecutivo", "Análisis detallado", "Citas con fuentes"],
                horizontal=True, key="abg_doc_nivel")
            st.markdown(
                '<div style="background:rgba(201,150,58,0.06);border:1px solid rgba(201,150,58,0.2);'
                'border-radius:6px;padding:0.7rem 0.9rem;font-size:0.78rem;color:#9a8a6a;line-height:1.55;">'
                '⚠️ <strong>Anti-alucinación:</strong> AntonIA solo cita autores y sentencias '
                'cuando tiene certeza de su existencia. Si hay incertidumbre lo indicará.'
                '</div>', unsafe_allow_html=True)
            if st.button("🔍 Buscar", use_container_width=True, type="primary", key="abg_doc_search"):
                if consulta_text.strip() and get_llm_fn:
                    system_doc = (
                        "Eres AntonIA, asistente jurídico para abogados chilenos. "
                        "REGLA CRÍTICA: Solo cita autores y sentencias que existan con certeza. "
                        "Si no tienes total certeza de una cita, usa frases como 'la doctrina mayoritaria sostiene' "
                        "sin inventar autores ni fechas. Para jurisprudencia, solo menciona casos que conozcas "
                        "(tribunal, rol, año). Siempre indica el artículo específico aplicable. "
                        "Responde en español jurídico formal chileno."
                    )
                    nivel_map = {
                        "Resumen ejecutivo": "Proporciona un resumen ejecutivo conciso (máx 400 palabras)",
                        "Análisis detallado": "Proporciona un análisis detallado y completo",
                        "Citas con fuentes": "Incluye citas relevantes con indicación de fuentes"
                    }
                    nivel_instr = nivel_map.get(nivel_precision, "Proporciona un análisis")
                    type_prompts = {
                        "Doctrina sobre un tema": (
                            f"Rama: {ramo_doc}\nTema: {consulta_text}\n\n{nivel_instr} sobre la doctrina chilena.\n"
                            f"Estructura: 1) Marco legal (artículos) 2) Posición doctrinal mayoritaria "
                            f"3) Posiciones minoritarias 4) Evolución reciente 5) Conclusión práctica para litigante"
                        ),
                        "Jurisprudencia chilena": (
                            f"Rama: {ramo_doc}\nTema: {consulta_text}\n\n{nivel_instr} sobre jurisprudencia chilena.\n"
                            f"IMPORTANTE: Solo menciona jurisprudencia que conozcas con certeza.\n"
                            f"Estructura: 1) Tendencia dominante 2) Criterios CS/CA 3) Casos paradigmáticos 4) Implicancias para litigio"
                        ),
                        "Normativa vigente aplicable": (
                            f"Rama: {ramo_doc}\nMateria: {consulta_text}\n\n{nivel_instr}.\n"
                            f"Estructura: 1) Normas principales (código + artículo) 2) Normas complementarias 3) Modificaciones recientes"
                        ),
                        "Análisis de caso con fundamentos": (
                            f"Caso: {consulta_text}\nRama: {ramo_doc}\n\n{nivel_instr}. Aplica método IRAC:\n"
                            f"I-Issue: cuestión jurídica central\nR-Rule: norma aplicable\n"
                            f"A-Application: argumentos pro/contra\nC-Conclusion + estrategia procesal"
                        ),
                        "Comparación de posiciones doctrinales": (
                            f"Tema: {consulta_text}\nRama: {ramo_doc}\n\n{nivel_instr}.\n"
                            f"Estructura: 1) Posición mayoritaria 2) Posición minoritaria 3) Argumentos de cada una 4) Postura jurisprudencial 5) Recomendación para litigio"
                        ),
                    }
                    prompt = type_prompts.get(tipo_consulta, f"Analiza: {consulta_text} en {ramo_doc}")
                    try:
                        llm = get_llm_fn()
                        with st.spinner("Consultando biblioteca jurídica…"):
                            resultado = llm.generate(prompt, system=system_doc, max_tokens=1800)
                        if "abg_doc_results" not in st.session_state:
                            st.session_state.abg_doc_results = []
                        st.session_state.abg_doc_results.insert(0, {
                            "tipo": tipo_consulta, "tema": consulta_text[:60],
                            "ramo": ramo_doc, "resultado": resultado
                        })
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.warning("Escribe tu consulta.")
        with col_res:
            resultados_doc = st.session_state.get("abg_doc_results", [])
            if resultados_doc:
                r = resultados_doc[0]
                st.markdown(
                    f'<div style="background:rgba(201,150,58,0.07);border:1px solid rgba(201,150,58,0.2);'
                    f'border-radius:8px;padding:0.6rem 0.9rem;margin-bottom:0.8rem;">'
                    f'<div style="font-size:0.68rem;font-weight:700;color:#c9963a;text-transform:uppercase;">'
                    f'{r["tipo"]} · {r["ramo"]}</div>'
                    f'<div style="font-size:0.85rem;color:#3a2a10;margin-top:2px;">{r["tema"]}</div>'
                    f'</div>', unsafe_allow_html=True)
                st.markdown(r["resultado"])
                if len(resultados_doc) > 1:
                    with st.expander(f"📋 Historial ({len(resultados_doc)-1} anteriores)"):
                        for r_prev in resultados_doc[1:5]:
                            st.markdown(f"**{r_prev['tipo']} — {r_prev['tema']}**")
                            st.markdown(r_prev["resultado"][:300] + "…")
                            st.divider()
            else:
                st.markdown(
                    '<div style="height:400px;display:flex;flex-direction:column;align-items:center;'
                    'justify-content:center;border:1px dashed rgba(201,150,58,.2);border-radius:8px;'
                    'color:#c0a880;font-size:.85rem;text-align:center;gap:0.5rem;">'
                    '📚<br><strong style="color:#c9963a;font-size:1rem;">Doctrina y Jurisprudencia</strong><br>'
                    'Consulta la biblioteca jurídica de AntonIA<br>'
                    '<span style="font-size:.72rem;">Civil · Penal · Laboral · Procesal · Comercial</span>'
                    '</div>', unsafe_allow_html=True)

    elif tab == "redaccion":
        st.markdown('<div class="abg-tab-header">📝 Redacción Profesional con IA</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Genera escritos judiciales, contratos y comunicaciones con asistencia de AntonIA</div>', unsafe_allow_html=True)
        sub_tabs = st.tabs(["⚖️ Escritos Judiciales", "📋 Contratos", "✉️ Comunicaciones", "🗂 Borradores"])
        with sub_tabs[0]:
            col_f, col_r = st.columns([1, 1.3])
            with col_f:
                tipo_escrito = st.selectbox("Tipo de escrito", [
                    "Demanda civil ordinario", "Demanda civil monitorio", "Demanda laboral",
                    "Demanda de divorcio unilateral", "Demanda ejecutiva",
                    "Contestación de demanda", "Réplica", "Dúplica",
                    "Recurso de apelación", "Recurso de casación en la forma",
                    "Recurso de protección", "Solicitud de medida cautelar",
                    "Escrito de observaciones a prueba", "Otro (describir)",
                ], key="abg_red_escrito")
                demandante = st.text_input("Demandante / Recurrente", key="abg_red_ddte")
                demandado  = st.text_input("Demandado / Recurrido", key="abg_red_ddo")
                tribunal   = st.text_input("Tribunal competente", placeholder="1° Juzgado Civil de Santiago", key="abg_red_trib")
                hechos     = st.text_area("Hechos relevantes", height=120,
                    placeholder="Describe los hechos cronológicamente…", key="abg_red_hechos")
                peticiones = st.text_area("Peticiones concretas", height=70,
                    placeholder="Ej: Se declare resolución del contrato + indemnización…", key="abg_red_peticiones")
                normas_ref = st.text_input("Normas de referencia", placeholder="Ej: Art. 1489 CC, Art. 254 CPC", key="abg_red_normas")
                if st.button("⚖️ Generar Escrito", use_container_width=True, type="primary", key="abg_red_gen"):
                    if hechos.strip() and get_llm_fn:
                        prompt_r = (
                            f"Redacta un escrito judicial profesional chileno:\n"
                            f"Tipo: {tipo_escrito}\nDemandante: {demandante}\nDemandado: {demandado}\n"
                            f"Tribunal: {tribunal}\nHechos: {hechos}\nPeticiones: {peticiones}\n"
                            f"Normas: {normas_ref}\n\n"
                            f"Usa formato forense chileno estándar (encabezado, cuerpo, otrosí).\n"
                            f"Cita artículos exactos del CPC, CC y normas especiales chilenas.\n"
                            f"Marca con [COMPLETAR] los datos faltantes.\n"
                            f"BORRADOR para revisión del abogado responsable."
                        )
                        system_r = "Eres un abogado litigante chileno experto en redacción forense. Usa el formato correcto chileno y cita solo normas que existan."
                        with st.spinner("Redactando escrito…"):
                            try:
                                llm = get_llm_fn()
                                st.session_state["abg_red_resultado"] = llm.generate(prompt_r, system=system_r, max_tokens=2000)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error: {e}")
                    else:
                        st.warning("Describe los hechos para generar el escrito.")
            with col_r:
                if "abg_red_resultado" in st.session_state and st.session_state.abg_red_resultado:
                    doc_edit = st.text_area("Edita el borrador:", value=st.session_state.abg_red_resultado, height=500, key="abg_red_edit_txt")
                    st.caption("⚠️ Borrador orientativo. Revisa antes de presentar al tribunal.")
                    if st.button("💾 Guardar", key="abg_red_save"):
                        if "abg_borradores" not in st.session_state:
                            st.session_state.abg_borradores = []
                        st.session_state.abg_borradores.append({
                            "tipo": tipo_escrito, "partes": f"{demandante} vs {demandado}",
                            "contenido": doc_edit, "fecha": str(datetime.date.today()),
                        })
                        st.success("✓ Guardado en Borradores")
                else:
                    st.markdown('<div style="height:400px;display:flex;align-items:center;justify-content:center;color:#c0a880;font-size:.82rem;text-align:center;border:1px dashed rgba(201,150,58,.15);border-radius:8px;flex-direction:column;">⚖️<br>Completa el formulario para generar el escrito</div>', unsafe_allow_html=True)
        with sub_tabs[1]:
            col_f2, col_r2 = st.columns([1, 1.3])
            with col_f2:
                tipo_cto = st.selectbox("Tipo de contrato", [
                    "Compraventa (bienes muebles)", "Compraventa (bienes inmuebles)",
                    "Arrendamiento", "Prestación de servicios", "Contrato de trabajo",
                    "Mutuo", "Poder simple", "Poder especial", "NDA", "Transacción extrajudicial", "Finiquito laboral",
                ], key="abg_cto_tipo")
                partes_cto = st.text_area("Partes (nombre, RUT, domicilio)", height=70, key="abg_cto_partes")
                objeto_cto = st.text_area("Objeto y condiciones principales", height=100, key="abg_cto_objeto",
                    placeholder="Describe objeto, precio, plazo y condiciones especiales…")
                if st.button("📋 Generar Contrato", use_container_width=True, type="primary", key="abg_cto_gen"):
                    if objeto_cto.strip() and get_llm_fn:
                        prompt_c = (
                            f"Redacta un {tipo_cto} chileno completo:\n"
                            f"Partes: {partes_cto}\nObjeto y condiciones: {objeto_cto}\n\n"
                            f"Incluye todas las cláusulas esenciales según el CC chileno.\n"
                            f"Añade cláusulas de domicilio y resolución de conflictos.\n"
                            f"Marca [COMPLETAR] donde falten datos."
                        )
                        system_c = "Eres un abogado contractualista chileno. Redacta contratos completos según el Código Civil chileno."
                        with st.spinner("Redactando contrato…"):
                            try:
                                llm = get_llm_fn()
                                st.session_state["abg_cto_resultado"] = llm.generate(prompt_c, system=system_c, max_tokens=2000)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error: {e}")
                    else:
                        st.warning("Describe el objeto del contrato.")
            with col_r2:
                if "abg_cto_resultado" in st.session_state and st.session_state.abg_cto_resultado:
                    st.text_area("Contrato:", value=st.session_state.abg_cto_resultado, height=500, key="abg_cto_edit")
                    st.caption("⚠️ Borrador para revisión profesional.")
                else:
                    st.markdown('<div style="height:400px;display:flex;align-items:center;justify-content:center;color:#c0a880;font-size:.82rem;text-align:center;border:1px dashed rgba(201,150,58,.15);border-radius:8px;flex-direction:column;">📋<br>El contrato aparecerá aquí</div>', unsafe_allow_html=True)
        with sub_tabs[2]:
            col_f3, col_r3 = st.columns([1, 1.3])
            with col_f3:
                tipo_com = st.selectbox("Tipo", [
                    "Carta de notificación extrajudicial", "Comunicación a cliente",
                    "Carta de cobranza", "Notificación de incumplimiento",
                    "Propuesta de honorarios", "Informe jurídico a cliente",
                ], key="abg_com_tipo")
                contexto_com = st.text_area("Contexto y mensaje", height=120, key="abg_com_ctx")
                tono_com = st.radio("Tono", ["Formal profesional", "Firme y directo", "Conciliatorio"], horizontal=True, key="abg_com_tono")
                if st.button("✉️ Generar", use_container_width=True, key="abg_com_gen"):
                    if contexto_com.strip() and get_llm_fn:
                        prompt_com = f"Redacta una {tipo_com} profesional chilena.\nContexto: {contexto_com}\nTono: {tono_com}\nUsa formato de carta profesional chilena."
                        system_com = "Eres un abogado chileno redactando comunicaciones profesionales formales."
                        with st.spinner("Redactando…"):
                            try:
                                llm = get_llm_fn()
                                st.session_state["abg_com_resultado"] = llm.generate(prompt_com, system=system_com, max_tokens=1000)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error: {e}")
                    else:
                        st.warning("Describe el contexto del mensaje.")
            with col_r3:
                if "abg_com_resultado" in st.session_state and st.session_state.abg_com_resultado:
                    st.text_area("Comunicación:", value=st.session_state.abg_com_resultado, height=400, key="abg_com_edit")
                else:
                    st.markdown('<div style="height:300px;display:flex;align-items:center;justify-content:center;color:#c0a880;font-size:.82rem;text-align:center;border:1px dashed rgba(201,150,58,.15);border-radius:8px;flex-direction:column;">✉️<br>La comunicación aparecerá aquí</div>', unsafe_allow_html=True)
        with sub_tabs[3]:
            borradores = st.session_state.get("abg_borradores", [])
            if not borradores:
                st.markdown('<div style="text-align:center;padding:3rem;color:#c0a880;font-size:.85rem;">📁 Aún no hay borradores guardados.</div>', unsafe_allow_html=True)
            else:
                for i, b in enumerate(reversed(borradores)):
                    with st.expander(f"📄 {b['tipo']} — {b['partes'][:40]} ({b['fecha']})"):
                        st.text_area("Contenido:", value=b["contenido"], height=300, key=f"abg_borr_{i}")

        # ═══════════════════════════════════════════════════════════════════════════
    # TAB: CORREOS
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "correos":
        st.markdown('<div class="abg-tab-header">✉️ Redacción de Correos</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Asistencia IA para comunicaciones profesionales</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            # Auto-fill desde causa seleccionada
            casos_opts  = ["(sin causa)"] + [_caso_label(c) for c in st.session_state.abg_casos]
            caso_corr_i = st.selectbox("Vincular a causa", range(len(casos_opts)),
                                       format_func=lambda i: casos_opts[i], key="corr_caso_idx")
            if caso_corr_i > 0:
                c_sel = st.session_state.abg_casos[caso_corr_i - 1]
                cli_em = c_sel.get("cliente", {}).get("email", "")
                cli_nm = c_sel.get("cliente", {}).get("nombre", "")
            else:
                cli_em = ""
                cli_nm = ""

            destinatario = st.text_input("Destinatario", value=cli_nm or "", placeholder="cliente, colega, tribunal…", key="abg_correo_dest")
            email_dest   = st.text_input("Email", value=cli_em or "", placeholder="correo@dominio.com", key="abg_correo_email")
            tono = st.selectbox("Tono", ["Formal", "Cordial", "Firme", "Urgente"], key="abg_correo_tono")
            instrucciones = st.text_area("¿Qué comunicar?",
                height=150,
                placeholder="Ej: Informar al cliente que la audiencia fue fijada para el 15/05/2025 a las 10:00 en el 4° Juzgado Civil. Recordarle que debe traer los documentos. Confirmar asistencia.",
                key="abg_correo_inst")

            if st.button("✉️ Redactar con IA", use_container_width=True, type="primary"):
                if instrucciones and get_llm_fn:
                    prompt = (
                        f"Eres un asistente de abogado. Redacta un correo electrónico profesional en español chileno.\n"
                        f"Destinatario: {destinatario or 'destinatario'}\n"
                        f"Tono: {tono}\n"
                        f"Instrucciones: {instrucciones}\n\n"
                        f"Escribe SOLO el texto del correo (sin explicaciones adicionales). "
                        f"Incluye saludo, cuerpo y despedida. Firma como 'Atte.\\n[Tu nombre]\\n[Tu cargo]'."
                    )
                    with st.spinner("Redactando…"):
                        try:
                            llm = get_llm_fn()
                            st.session_state.abg_correo_result = llm.generate(prompt, system="Eres AntonIA, asistente jurídico para abogados chilenos. Proporciona análisis precisos del Derecho chileno.", max_tokens=800)
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Escribe las instrucciones del correo.")

        with col2:
            if st.session_state.abg_correo_result:
                st.markdown('<div class="abg-section-label">Borrador generado</div>', unsafe_allow_html=True)
                correo_editado = st.text_area("Edita y envía:",
                    value=st.session_state.abg_correo_result, height=340, key="abg_correo_edit")
                if email_dest:
                    asunto = f"Causa {c_sel['rol']}" if caso_corr_i > 0 else "Comunicación de su abogado"
                    mailto = f"mailto:{email_dest}?subject={asunto.replace(' ','%20')}&body={correo_editado[:600].replace(' ','%20').replace(chr(10),'%0A')}"
                    st.markdown(
                        f'<a href="{mailto}" target="_blank"><button style="width:100%;background:#c9963a;'
                        f'color:#fff;border:none;border-radius:6px;padding:.5rem .8rem;cursor:pointer;'
                        f'font-size:.8rem;font-weight:700;margin-top:.4rem;">📧 Abrir en cliente de correo</button></a>',
                        unsafe_allow_html=True)
                else:
                    st.code(correo_editado, language=None)
                    st.caption("Copia el texto. Para abrir en correo, agrega email del cliente en la causa.")
            else:
                st.markdown(
                    '<div style="height:280px;display:flex;align-items:center;justify-content:center;'
                    'color:#c0a880;font-size:.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,.15);border-radius:8px;">'
                    '✉️<br>El borrador del correo<br>aparecerá aquí</div>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: PENDIENTES
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "pendientes":
        st.markdown('<div class="abg-tab-header">📋 Tareas Pendientes</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Gestor de actividades y seguimientos</div>', unsafe_allow_html=True)

        col_add, col_list = st.columns([1, 1.6])
        with col_add:
            nueva_tarea = st.text_input("Nueva tarea", placeholder="Llamar al perito…", key="abg_task_nueva")
            prioridad   = st.selectbox("Prioridad", ["🔴 Alta","🟡 Media","🟢 Baja"], key="abg_task_prio")
            casos_opt_t = ["(sin causa)"] + [_caso_label(c) for c in st.session_state.abg_casos]
            causa_t_idx = st.selectbox("Causa asociada", range(len(casos_opt_t)),
                                       format_func=lambda i: casos_opt_t[i], key="abg_task_causa_idx")
            causa_t     = casos_opt_t[causa_t_idx] if causa_t_idx > 0 else ""
            fecha_venc  = st.date_input("Fecha límite (opcional)", value=None, key="abg_task_fecha")
            if st.button("Agregar", use_container_width=True, type="primary"):
                if nueva_tarea:
                    st.session_state.abg_tasks.append({
                        "texto":    nueva_tarea,
                        "prio":     prioridad,
                        "causa":    causa_t,
                        "done":     False,
                        "fecha":    datetime.date.today().isoformat(),
                        "vence":    fecha_venc.isoformat() if fecha_venc else "",
                    })
                    st.rerun()

        with col_list:
            tasks_pend = [t for t in st.session_state.abg_tasks if not t["done"]]
            tasks_done = [t for t in st.session_state.abg_tasks if t["done"]]
            hoy = datetime.date.today()

            if not tasks_pend:
                st.markdown('<div style="text-align:center;padding:2rem;color:#c0a880;">✅ Sin tareas pendientes.</div>', unsafe_allow_html=True)
            else:
                for i, t in enumerate(tasks_pend):
                    orig_idx = st.session_state.abg_tasks.index(t)
                    col_chk, col_txt = st.columns([0.5, 5])
                    with col_chk:
                        if st.checkbox("", key=f"task_{orig_idx}", value=False):
                            st.session_state.abg_tasks[orig_idx]["done"] = True
                            st.rerun()
                    with col_txt:
                        vence_str = ""
                        if t.get("vence"):
                            dias_v = (datetime.date.fromisoformat(t["vence"]) - hoy).days
                            vence_str = f' · <span style="color:{"#ef4444" if dias_v<=1 else "#fbbf24" if dias_v<=3 else "#22c55e"}">vence en {dias_v}d</span>'
                        st.markdown(
                            f'<div style="padding:.3rem 0;font-size:.8rem;color:#f5f0e8;">'
                            f'{t["prio"]} {t["texto"]}'
                            + (f'<br><span style="font-size:.65rem;color:#c0a880;">{t["causa"]}</span>' if t.get("causa") else "")
                            + vence_str
                            + f'</div>', unsafe_allow_html=True)

            if tasks_done:
                with st.expander(f"Completadas ({len(tasks_done)})"):
                    for t in tasks_done:
                        st.markdown(f'<div style="font-size:.75rem;color:#c0a880;text-decoration:line-through;">{t["texto"]}</div>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: DOCUMENTOS
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "documentos":
        st.markdown('<div class="abg-tab-header">📄 Generación de Documentos</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Escritos jurídicos asistidos por IA</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            tipo_doc = st.selectbox("Tipo de documento", [
                "Carta de notificación extrajudicial",
                "Propuesta de transacción / acuerdo",
                "Poder simple",
                "Contrato de prestación de servicios",
                "Demanda (borrador)",
                "Contestación de demanda (borrador)",
                "Escrito de observaciones",
                "Comunicación a cliente (estado causa)",
                "Otro (describir)",
            ], key="abg_doc_tipo")
            partes_doc = st.text_input("Partes involucradas", key="abg_doc_partes")
            detalle = st.text_area("Detalles del documento", height=150,
                placeholder="Describe hechos, pretensiones, cláusulas especiales…", key="abg_doc_detalle")
            jurisdiccion = st.selectbox("Jurisdicción / Tribunal", [
                "Santiago — Juzgado Civil",
                "Santiago — Juzgado Penal",
                "Santiago — Juzgado Laboral",
                "Santiago — Juzgado Familia",
                "Valparaíso", "Concepción", "Otra (indicar en detalles)",
            ], key="abg_doc_jur")

            if st.button("📄 Generar Borrador", use_container_width=True, type="primary"):
                if detalle and get_llm_fn:
                    prompt = (
                        f"Eres un abogado chileno redactando documentos jurídicos.\n"
                        f"Redacta un borrador de: {tipo_doc}\n"
                        f"Partes: {partes_doc}\n"
                        f"Jurisdicción: {jurisdiccion}\n"
                        f"Detalles: {detalle}\n\n"
                        f"INSTRUCCIONES:\n"
                        f"- Usa terminología jurídica chilena correcta (CPC, CC chileno)\n"
                        f"- Incluye estructura formal con encabezado, cuerpo y cierre\n"
                        f"- Deja campos con [DATO] cuando falte información\n"
                        f"- Anota al final las advertencias o puntos a revisar\n"
                        f"- Este es un BORRADOR para revisión del abogado"
                    )
                    with st.spinner("Generando borrador…"):
                        try:
                            llm = get_llm_fn()
                            st.session_state.abg_doc_result = llm.generate(prompt, system="Eres AntonIA, asistente jurídico para abogados chilenos. Proporciona análisis precisos del Derecho chileno.", max_tokens=1500)
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Agrega los detalles del documento.")

        with col2:
            if st.session_state.abg_doc_result:
                st.markdown('<div class="abg-section-label">Borrador generado</div>', unsafe_allow_html=True)
                doc_edit = st.text_area("Edita el borrador:",
                    value=st.session_state.abg_doc_result, height=420, key="abg_doc_edit")
                st.caption("⚠️ Borrador orientativo. Revisa y adapta antes de presentar.")
            else:
                st.markdown(
                    '<div style="height:350px;display:flex;align-items:center;justify-content:center;'
                    'color:#c0a880;font-size:.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,.15);border-radius:8px;">'
                    '📄<br>El borrador del documento<br>aparecerá aquí</div>', unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB: HONORARIOS
    # ═══════════════════════════════════════════════════════════════════════════
    elif tab == "honorarios":
        st.markdown('<div class="abg-tab-header">💰 Honorarios</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Control de devengamiento y propuestas de honorarios</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            st.markdown('<div class="abg-section-label">Registrar honorario</div>', unsafe_allow_html=True)
            casos_hon = ["(sin causa)"] + [_caso_label(c) for c in st.session_state.abg_casos]
            hon_caso_i = st.selectbox("Causa", range(len(casos_hon)), format_func=lambda i: casos_hon[i], key="abg_hon_ci")
            causa_h   = casos_hon[hon_caso_i] if hon_caso_i > 0 else st.text_input("ROL manual", key="abg_hon_rol_man")
            concepto  = st.text_input("Concepto", placeholder="Audiencia preparatoria", key="abg_hon_concepto")
            monto     = st.number_input("Monto (CLP)", min_value=0, step=10000, key="abg_hon_monto")
            estado_h  = st.selectbox("Estado", ["Propuesto","Aceptado","Devengado","Cobrado","Pagado"], key="abg_hon_estado")

            if st.button("Registrar", use_container_width=True, type="primary"):
                if concepto and monto > 0:
                    st.session_state.abg_honorarios.append({
                        "causa":    causa_h,
                        "concepto": concepto,
                        "monto":    monto,
                        "estado":   estado_h,
                        "fecha":    datetime.date.today().isoformat(),
                    })
                    st.success("✓ Honorario registrado")
                    st.rerun()
                else:
                    st.warning("Completa concepto y monto.")

            st.markdown('<hr style="border-color:rgba(255,255,255,.07);margin:1rem 0;">', unsafe_allow_html=True)
            st.markdown('<div class="abg-section-label">Generar propuesta con IA</div>', unsafe_allow_html=True)
            tipo_causa_h = st.text_input("Tipo de causa", placeholder="Divorcio unilateral, Santiago", key="abg_hon_tipo")
            complejidad  = st.selectbox("Complejidad", ["Baja","Media","Alta","Muy alta"], key="abg_hon_comp")
            svcs         = st.text_area("Servicios incluidos", height=70,
                placeholder="Ej: Tramitación completa hasta sentencia, incluye 3 audiencias", key="abg_hon_svcs")

            if st.button("💰 Generar Propuesta", use_container_width=True):
                if tipo_causa_h and get_llm_fn:
                    prompt = (
                        f"Eres un abogado chileno. Genera propuesta de honorarios para:\n"
                        f"Causa: {tipo_causa_h} | Complejidad: {complejidad} | Servicios: {svcs}\n\n"
                        f"Incluye: 1) Honorario total (UF y CLP) 2) Desglose por etapas "
                        f"3) Forma de pago sugerida 4) Qué incluye/no incluye 5) Observaciones.\n"
                        f"Basado en aranceles referenciales Colegio de Abogados de Chile."
                    )
                    with st.spinner("Generando propuesta…"):
                        try:
                            llm = get_llm_fn()
                            st.session_state.abg_hon_propuesta = llm.generate(prompt, system="Eres AntonIA, asistente jurídico para abogados chilenos. Proporciona análisis precisos del Derecho chileno.", max_tokens=1000)
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")

        with col2:
            hons = st.session_state.abg_honorarios
            if hons:
                total_propuesto = sum(h["monto"] for h in hons if h["estado"] == "Propuesto")
                total_devengado = sum(h["monto"] for h in hons if h["estado"] in ("Devengado","Aceptado"))
                total_cobrado   = sum(h["monto"] for h in hons if h["estado"] == "Cobrado")
                total_pagado    = sum(h["monto"] for h in hons if h["estado"] == "Pagado")
                c1, c2 = st.columns(2)
                c1.metric("Devengado", _fmt_monto(total_devengado))
                c2.metric("Cobrado",   _fmt_monto(total_cobrado))
                c1.metric("Pagado",    _fmt_monto(total_pagado))
                c2.metric("Propuesto", _fmt_monto(total_propuesto))
                st.markdown('<hr style="border-color:rgba(255,255,255,.07);margin:.8rem 0;">', unsafe_allow_html=True)
                for h in reversed(hons):
                    color_map = {"Pagado":"#22c55e","Cobrado":"#3b82f6","Devengado":"#c9963a",
                                 "Aceptado":"#fbbf24","Propuesto":"#a09070"}
                    color = color_map.get(h["estado"], "#a09070")
                    st.markdown(
                        f'<div class="abg-card" style="padding:.55rem .9rem;">'
                        f'<div style="display:flex;justify-content:space-between;">'
                        f'<div style="font-size:.77rem;color:#f5f0e8;">{h["causa"][:30]} — {h["concepto"][:30]}</div>'
                        f'<div style="font-size:.77rem;color:{color};font-weight:700;">{_fmt_monto(h["monto"])}</div>'
                        f'</div>'
                        f'<div style="font-size:.64rem;color:#c0a880;">{h["estado"]} · {h["fecha"]}</div>'
                        f'</div>', unsafe_allow_html=True)
            elif st.session_state.abg_hon_propuesta:
                st.markdown('<div class="abg-section-label">Propuesta generada</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="abg-card" style="font-size:.78rem;color:#e8d8b8;line-height:1.6;">'
                    f'{st.session_state.abg_hon_propuesta.replace(chr(10),"<br>")}</div>',
                    unsafe_allow_html=True)
            else:
                st.markdown(
                    '<div style="text-align:center;padding:3rem 1rem;color:#c0a880;font-size:.85rem;">'
                    '💰 Registra honorarios o genera una propuesta con IA.</div>', unsafe_allow_html=True)

            if st.session_state.abg_hon_propuesta and hons:
                with st.expander("Ver propuesta generada"):
                    st.markdown(
                        f'<div style="font-size:.78rem;color:#e8d8b8;line-height:1.6;">'
                        f'{st.session_state.abg_hon_propuesta.replace(chr(10),"<br>")}</div>',
                        unsafe_allow_html=True)
