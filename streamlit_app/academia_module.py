"""
academia_module.py — AntonIA ENTRENA
Quiz legal infinito con generación de preguntas por IA.

Flujo: elige ramo → aparece tipo → aparece pregunta.
Tipos: Alternativas · V/F · Flashcards · Desarrollo · Caso Práctico
"""

import streamlit as st
import json, random, re

# Banco estático de preguntas (~480 Q&A)
try:
    from banco_preguntas import BANCO_MCQ, BANCO_VF, BANCO_FC
    _BANCO_OK = True
except ImportError:
    BANCO_MCQ = BANCO_VF = BANCO_FC = {}
    _BANCO_OK = False

_GOLD  = "#c9963a"
_DARK  = "#141210"
_CARD  = "#1e1b16"
_CARD2 = "#221e17"
_MUTED = "#a09070"
_WHITE = "#f5f0e8"
_GREEN = "#22c55e"
_RED   = "#ef4444"

CURSOS = [
    # ── Grupo Derecho Civil (5 sub-ramos según malla UCh / PUC / UDP) ──
    {"id": "civil",          "nombre": "Civil I",   "full": "Civil I — Personas y Acto Jurídico",   "icono": "👤", "grupo": "civil"},
    {"id": "bienes",         "nombre": "Civil II",  "full": "Civil II — Bienes y Derechos Reales",  "icono": "🏠", "grupo": "civil"},
    {"id": "obligaciones",   "nombre": "Civil III", "full": "Civil III — Obligaciones y Contratos", "icono": "📝", "grupo": "civil"},
    {"id": "familia",        "nombre": "Civil IV",  "full": "Civil IV — Derecho de Familia",        "icono": "👨‍👩‍👧", "grupo": "civil"},
    {"id": "sucesorio",      "nombre": "Civil V",   "full": "Civil V — Derecho Sucesorio",          "icono": "📜", "grupo": "civil"},
    # ── Otras áreas ──
    {"id": "penal",          "nombre": "Penal",     "full": "Derecho Penal",                        "icono": "🔒", "grupo": "otro"},
    {"id": "procesal",       "nombre": "Procesal",  "full": "Derecho Procesal",                     "icono": "⚖️", "grupo": "otro"},
    {"id": "constitucional", "nombre": "Const.",    "full": "Derecho Constitucional y DDPP",        "icono": "🏛️", "grupo": "otro"},
    {"id": "laboral",        "nombre": "Trabajo",   "full": "Derecho del Trabajo",                  "icono": "👷", "grupo": "otro"},
    {"id": "comercial",      "nombre": "Comercial", "full": "Derecho Comercial",                    "icono": "💼", "grupo": "otro"},
    {"id": "internacional",  "nombre": "Intl.",     "full": "Derecho Internacional",                "icono": "🌐", "grupo": "otro"},
    {"id": "ambiental",      "nombre": "Ambiental", "full": "Derecho Ambiental",                    "icono": "🌿", "grupo": "otro"},
]

TIPOS = [
    {"id": "mcq",        "label": "Alternativas", "icono": "🔘"},
    {"id": "vf",         "label": "V / F",        "icono": "✅"},
    {"id": "flashcard",  "label": "Flashcards",   "icono": "🃏"},
    {"id": "desarrollo", "label": "Desarrollo",   "icono": "✍️"},
    {"id": "caso",       "label": "Caso",         "icono": "⚖️"},
]

# (banco estático importado arriba desde banco_preguntas.py)


# ── Init ──────────────────────────────────────────────────────
def _init():
    defs = {
        "eq_curso":     None,   # ID del curso seleccionado (None = pantalla inicial)
        "eq_tipo":      None,   # ID del tipo seleccionado (None = sin seleccionar)
        "eq_item":      None,   # pregunta activa
        "eq_sel":       None,
        "eq_done":      False,
        "eq_fc_flip":   False,
        # Historial POR (tipo, curso) para evitar repetición: {"mcq__civil": ["t1","t2",...]}
        "eq_hist":      {},
        # Índices del banco ya mostrados: {"mcq__civil": [0,3,7,...]}  ← lista, no set
        "eq_banco_idx": {},
        # Métricas
        "eq_n":         0,
        "eq_ok":        0,
        "eq_racha":     0,
        "eq_racha_max": 0,
        # Desarrollo
        "eq_dev_resp":  "",
        "eq_dev_eval":  "",
        # Caso
        "eq_caso_resps": {},
        "eq_caso_eval":  "",
    }
    for k, v in defs.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ── CSS ───────────────────────────────────────────────────────
def _css():
    st.markdown(f"""<style>
    .eq-card {{
        background:{_CARD};border:1.5px solid rgba(201,150,58,0.22);
        border-radius:14px;padding:1.6rem 1.8rem;margin:0.8rem 0 1.2rem;
    }}
    .eq-num {{
        font-size:0.62rem;font-weight:700;color:{_MUTED};
        text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.7rem;
    }}
    .eq-pregunta {{font-size:1.05rem;font-weight:700;color:{_WHITE};line-height:1.55;}}
    .eq-op  {{background:{_CARD2};border:1.5px solid rgba(201,150,58,0.15);border-radius:10px;
               padding:0.75rem 1rem;margin:0.4rem 0;color:{_WHITE};font-size:0.9rem;}}
    .eq-ok  {{background:#052e16!important;border-color:{_GREEN}!important;color:{_GREEN}!important;font-weight:700;}}
    .eq-mal {{background:#2d0a0a!important;border-color:{_RED}!important;color:#f87171!important;}}
    .eq-neu {{opacity:0.4;}}
    .eq-fund {{
        background:rgba(201,150,58,0.07);border-left:3px solid {_GOLD};
        border-radius:0 8px 8px 0;padding:0.85rem 1.1rem;
        font-size:0.85rem;color:#d4c5a0;margin-top:1rem;line-height:1.6;
    }}
    .eq-fc {{
        background:linear-gradient(135deg,{_CARD2},{_CARD});
        border:2px solid rgba(201,150,58,0.3);border-radius:16px;
        min-height:200px;display:flex;flex-direction:column;
        justify-content:center;align-items:center;
        text-align:center;padding:2rem;margin:0.8rem 0;
    }}
    .eq-score {{
        display:flex;align-items:center;gap:1.5rem;
        padding:0.6rem 1.1rem;background:{_CARD};border-radius:10px;margin-bottom:1rem;
    }}
    .eq-sn  {{font-weight:800;font-size:1.05rem;color:{_WHITE};}}
    .eq-sl  {{color:{_MUTED};font-size:0.68rem;text-transform:uppercase;letter-spacing:0.05em;}}
    .eq-curso-pill button {{border-radius:20px!important;}}
    </style>""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────
def _full(cid):
    return next((c["full"] for c in CURSOS if c["id"] == cid), cid.title())

def _icon(cid):
    return next((c["icono"] for c in CURSOS if c["id"] == cid), "⚖️")

def _hkey():
    return f"{st.session_state.eq_tipo}__{st.session_state.eq_curso}"

def _hist_get():
    return st.session_state.eq_hist.get(_hkey(), [])

def _hist_add(tema: str):
    k = _hkey()
    hist = dict(st.session_state.eq_hist)
    h = list(hist.get(k, []))
    h.append(str(tema)[:120])
    # Mantener últimas 60 entradas por (tipo, curso)
    if len(h) > 60:
        h = h[-60:]
    hist[k] = h
    # Reasignar el dict completo para que Streamlit detecte el cambio
    st.session_state.eq_hist = hist

def _hist_str():
    h = _hist_get()
    return "; ".join(h) if h else "ninguno"

def _parse_json(txt):
    try:
        return json.loads(txt)
    except Exception:
        m = re.search(r'\{[\s\S]*\}', txt)
        if m:
            try:
                return json.loads(m.group())
            except Exception:
                pass
    return None

def _reset_item():
    st.session_state.eq_item       = None
    st.session_state.eq_sel        = None
    st.session_state.eq_done       = False
    st.session_state.eq_fc_flip    = False
    st.session_state.eq_dev_resp   = ""
    st.session_state.eq_dev_eval   = ""
    st.session_state.eq_caso_resps = {}
    st.session_state.eq_caso_eval  = ""
    # Asegurar que eq_banco_idx existe
    if "eq_banco_idx" not in st.session_state:
        st.session_state.eq_banco_idx = {}


# ── Detección de repetición ───────────────────────────────────
def _es_repetida(item, tipo) -> bool:
    hist = _hist_get()
    if len(hist) < 2:
        return False
    if tipo == "mcq":
        txt = item.get("pregunta", "")[:100].lower()
    elif tipo == "vf":
        txt = item.get("afirmacion", "")[:100].lower()
    elif tipo == "flashcard":
        txt = item.get("frente", "")[:100].lower()
    else:
        txt = item.get("pregunta", item.get("titulo", ""))[:100].lower()
    for pasado in hist[-12:]:
        palabras = [p for p in pasado.lower().split() if len(p) > 4]
        if palabras and sum(1 for p in palabras if p in txt) / len(palabras) > 0.45:
            return True
    return False


# ── Generadores IA ────────────────────────────────────────────
def _gen(tipo, llm):
    cid    = st.session_state.eq_curso
    nombre = _full(cid)
    prev   = _hist_str()

    prompts = {
        "mcq": f"""Eres un profesor de derecho chileno.
Genera UNA pregunta de alternativas (4 opciones) sobre {nombre} para universitarios en Chile.
TEMAS YA USADOS — PROHIBIDO REPETIR: {prev}
Elige un tema completamente distinto. Varía entre: definiciones, requisitos, efectos, plazos, artículos, distinciones doctrinarias.
Responde SOLO con JSON, sin texto adicional:
{{"pregunta":"...","opciones":["A. ...","B. ...","C. ...","D. ..."],"correcta":0,"fundamento":"cita artículo o autor chileno","tema":"tema breve"}}
"correcta" es índice entero (0=A,1=B,2=C,3=D).""",

        "vf": f"""Eres un profesor de derecho chileno.
Genera UNA afirmación Verdadero/Falso sobre {nombre} para universitarios en Chile.
TEMAS YA USADOS — PROHIBIDO REPETIR: {prev}
Elige un tema distinto. Alterna deliberadamente entre verdaderas y falsas.
Responde SOLO con JSON, sin texto adicional:
{{"afirmacion":"...","respuesta":true,"fundamento":"cita artículo o autor chileno","tema":"tema breve"}}""",

        "flashcard": f"""Eres un profesor de derecho chileno.
Genera UNA flashcard sobre {nombre} para memorizar conceptos clave.
TEMAS YA USADOS — PROHIBIDO REPETIR: {prev}
Rota entre: definiciones, elementos, plazos, requisitos, diferencias entre figuras, artículos clave.
Responde SOLO con JSON, sin texto adicional:
{{"frente":"pregunta o concepto (máx 15 palabras)","reverso":"respuesta precisa con fundamento legal chileno","tema":"tema breve"}}""",

        "desarrollo": f"""Eres un profesor de derecho chileno.
Genera UNA pregunta de desarrollo para examen de {nombre} en Chile.
TEMAS YA USADOS — PROHIBIDO REPETIR: {prev}
Elige un tema distinto que exija análisis jurídico profundo.
Responde SOLO con JSON, sin texto adicional:
{{"pregunta":"texto completo de la pregunta","tema":"tema breve"}}""",

        "caso": f"""Eres un profesor de derecho chileno.
Genera UN caso práctico de {nombre} con 3 preguntas de análisis jurídico.
CASOS YA USADOS — PROHIBIDO REPETIR: {prev}
Crea un caso distinto con nombres ficticios y hechos específicos. Aplica derecho chileno vigente.
Responde SOLO con JSON, sin texto adicional:
{{"titulo":"título breve","enunciado":"hechos del caso en 4-6 líneas","preguntas":["p1","p2","p3"],"tema":"tema breve"}}""",
    }

    for intento in range(3):
        try:
            resp = llm.complete(prompts[tipo])
            item = _parse_json(resp)
            if item:
                if len(_hist_get()) > 3 and _es_repetida(item, tipo) and intento < 2:
                    continue  # reintentar con el mismo prompt (LLM elegirá diferente)
                return item
        except Exception:
            break
    return None

def _fallback(tipo, cid):
    """
    Devuelve una pregunta del banco estático usando rotación estricta:
    no repite hasta agotar TODAS las preguntas del banco para ese (tipo, curso).
    Usa lista serializable (no set) y normaliza claves inconsistentes del banco.
    """
    banco_map = {"mcq": BANCO_MCQ, "vf": BANCO_VF, "flashcard": BANCO_FC}
    banco = banco_map.get(tipo, {}).get(cid, [])
    if not banco:
        return None

    k = f"{tipo}__{cid}"  # clave explícita, no depende de session_state

    # Leer lista de usados (lista serializable, no set)
    banco_idx = dict(st.session_state.eq_banco_idx)
    usados = list(banco_idx.get(k, []))

    # Convertir a set solo para la búsqueda rápida, sin guardarlo
    usados_set = set(usados)
    disponibles = [i for i in range(len(banco)) if i not in usados_set]
    if not disponibles:
        # Banco agotado → reiniciar rotación completa (barajar para evitar mismo orden)
        usados = []
        usados_set = set()
        disponibles = list(range(len(banco)))
        random.shuffle(disponibles)

    idx = random.choice(disponibles)
    usados.append(idx)

    # Reasignar el dict completo para que Streamlit detecte el cambio
    banco_idx[k] = usados
    st.session_state.eq_banco_idx = banco_idx

    # Devolver COPIA del item para evitar mutaciones al banco en memoria
    item = dict(banco[idx])

    # Normalizar campos: algunos items usan "verdadero"/"explicacion"
    # en vez de "respuesta"/"fundamento" (inconsistencia del banco)
    if tipo == "vf":
        if "verdadero" in item and "respuesta" not in item:
            item["respuesta"] = item.pop("verdadero")
        if "explicacion" in item and "fundamento" not in item:
            item["fundamento"] = item.pop("explicacion")
        # Garantizar que "fundamento" siempre existe
        if "fundamento" not in item:
            item["fundamento"] = item.get("explicacion", "")

    return item


# ── Score bar ─────────────────────────────────────────────────
def _score_bar():
    n  = st.session_state.eq_n
    ok = st.session_state.eq_ok
    r  = st.session_state.eq_racha
    if n == 0:
        return
    pct   = int(ok / n * 100)
    color = _GREEN if pct >= 60 else (_GOLD if pct >= 40 else _RED)
    fuego = "🔥 " if r >= 3 else ""
    st.markdown(f"""
    <div class="eq-score">
      <div><div class="eq-sn" style="color:{color}">{ok}/{n}</div><div class="eq-sl">correctas</div></div>
      <div><div class="eq-sn">{pct}%</div><div class="eq-sl">precisión</div></div>
      <div><div class="eq-sn" style="color:{_GOLD if r>=3 else _WHITE}">{fuego}{r}</div><div class="eq-sl">racha</div></div>
    </div>""", unsafe_allow_html=True)


# ── ensure item ───────────────────────────────────────────────
def _ensure_item(tipo, llm) -> bool:
    if st.session_state.eq_item is not None:
        return True
    cid = st.session_state.eq_curso
    with st.spinner("Generando pregunta..."):
        # Para tipos con banco estático (mcq, vf, flashcard):
        #   → SIEMPRE usar el banco primero (rotación garantizada, 0 repeticiones)
        #   → LLM solo si el banco está vacío para ese ramo
        # Para desarrollo y caso (sin banco):
        #   → LLM primero; sin fallback de banco
        if tipo in ("mcq", "vf", "flashcard"):
            item = _fallback(tipo, cid)
            if item is None and llm:
                item = _gen(tipo, llm)
        else:
            item = _gen(tipo, llm) if llm else None

        if item is None:
            st.warning("Sin preguntas disponibles para este ramo y tipo.")
            return False
    st.session_state.eq_item = item
    st.rerun()
    return False


# ── MCQ ───────────────────────────────────────────────────────
def _render_mcq(llm):
    if not _ensure_item("mcq", llm):
        return
    item = st.session_state.eq_item
    sel  = st.session_state.eq_sel
    done = st.session_state.eq_done
    n    = st.session_state.eq_n + 1

    st.markdown(f"""<div class="eq-card">
      <div class="eq-num">#{n} · Alternativas · {_full(st.session_state.eq_curso)}</div>
      <div class="eq-pregunta">{item['pregunta']}</div>
    </div>""", unsafe_allow_html=True)

    for i, op in enumerate(item["opciones"]):
        if done:
            cls = "eq-op eq-ok" if i == item["correcta"] else ("eq-op eq-mal" if i == sel else "eq-op eq-neu")
            st.markdown(f'<div class="{cls}">{op}</div>', unsafe_allow_html=True)
        else:
            if st.button(op, key=f"eq_op_{i}", use_container_width=True):
                st.session_state.eq_sel  = i
                st.session_state.eq_done = True
                st.session_state.eq_n   += 1
                if i == item["correcta"]:
                    st.session_state.eq_ok    += 1
                    st.session_state.eq_racha += 1
                    st.session_state.eq_racha_max = max(st.session_state.eq_racha, st.session_state.eq_racha_max)
                else:
                    st.session_state.eq_racha = 0
                st.rerun()

    if done:
        if sel == item["correcta"]:
            st.success("✓ ¡Correcto!")
        else:
            st.error(f"✗ Era: **{item['opciones'][item['correcta']]}**")
        st.markdown(f'<div class="eq-fund">📖 {item["fundamento"]}</div>', unsafe_allow_html=True)
        if st.button("→ Siguiente pregunta", type="primary", use_container_width=True):
            _hist_add(item.get("pregunta", item.get("tema", ""))[:120])
            _reset_item()
            st.rerun()


# ── V/F ───────────────────────────────────────────────────────
def _render_vf(llm):
    if not _ensure_item("vf", llm):
        return
    item = st.session_state.eq_item
    sel  = st.session_state.eq_sel
    done = st.session_state.eq_done
    n    = st.session_state.eq_n + 1

    st.markdown(f"""<div class="eq-card">
      <div class="eq-num">#{n} · Verdadero / Falso · {_full(st.session_state.eq_curso)}</div>
      <div class="eq-pregunta">{item['afirmacion']}</div>
    </div>""", unsafe_allow_html=True)

    if not done:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Verdadero", use_container_width=True, type="primary"):
                _reg_vf(True, item)
        with c2:
            if st.button("❌ Falso", use_container_width=True):
                _reg_vf(False, item)
    else:
        ok = sel == item["respuesta"]
        lbl = "Verdadero" if item["respuesta"] else "Falso"
        if ok:
            st.success(f"✓ ¡Correcto! Es **{lbl}**")
        else:
            st.error(f"✗ Era **{lbl}**")
        st.markdown(f'<div class="eq-fund">📖 {item["fundamento"]}</div>', unsafe_allow_html=True)
        if st.button("→ Siguiente afirmación", type="primary", use_container_width=True):
            _hist_add(item.get("afirmacion", item.get("tema", ""))[:120])
            _reset_item()
            st.rerun()

def _reg_vf(resp, item):
    st.session_state.eq_sel  = resp
    st.session_state.eq_done = True
    st.session_state.eq_n   += 1
    if resp == item["respuesta"]:
        st.session_state.eq_ok    += 1
        st.session_state.eq_racha += 1
        st.session_state.eq_racha_max = max(st.session_state.eq_racha, st.session_state.eq_racha_max)
    else:
        st.session_state.eq_racha = 0
    st.rerun()


# ── Flashcard ─────────────────────────────────────────────────
def _render_flashcard(llm):
    if not _ensure_item("flashcard", llm):
        return
    item = st.session_state.eq_item
    flip = st.session_state.eq_fc_flip
    n    = st.session_state.eq_n + 1

    if not flip:
        st.markdown(f"""<div class="eq-fc">
          <div style="font-size:0.7rem;color:{_MUTED};text-transform:uppercase;
                      letter-spacing:0.1em;margin-bottom:1rem;">#{n} · {_full(st.session_state.eq_curso)}</div>
          <div style="font-size:1.25rem;font-weight:800;color:{_WHITE};line-height:1.4;">{item['frente']}</div>
        </div>""", unsafe_allow_html=True)
        if st.button("👁 Ver respuesta", type="primary", use_container_width=True):
            st.session_state.eq_fc_flip = True
            st.session_state.eq_n      += 1
            st.rerun()
    else:
        st.markdown(f"""<div class="eq-fc" style="border-color:rgba(34,197,94,0.4);">
          <div style="font-size:0.7rem;color:#86efac;text-transform:uppercase;
                      letter-spacing:0.1em;margin-bottom:1rem;">Respuesta</div>
          <div style="font-size:0.95rem;color:{_WHITE};line-height:1.7;">{item['reverso']}</div>
        </div>""", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✓ La sabía", type="primary", use_container_width=True):
                st.session_state.eq_ok    += 1
                st.session_state.eq_racha += 1
                st.session_state.eq_racha_max = max(st.session_state.eq_racha, st.session_state.eq_racha_max)
                _hist_add(item.get("frente", item.get("tema", ""))[:120])
                _reset_item()
                st.rerun()
        with c2:
            if st.button("✗ A repasar", use_container_width=True):
                st.session_state.eq_racha = 0
                _hist_add(item.get("frente", item.get("tema", ""))[:120])
                _reset_item()
                st.rerun()


# ── Desarrollo ────────────────────────────────────────────────
def _render_desarrollo(llm):
    if not _ensure_item("desarrollo", llm):
        return
    item     = st.session_state.eq_item
    pregunta = item.get("pregunta", str(item)) if isinstance(item, dict) else str(item)
    n        = st.session_state.eq_n + 1

    st.markdown(f"""<div class="eq-card">
      <div class="eq-num">#{n} · Desarrollo · {_full(st.session_state.eq_curso)}</div>
      <div class="eq-pregunta">✍️ {pregunta}</div>
    </div>""", unsafe_allow_html=True)

    resp = st.text_area("Tu respuesta", value=st.session_state.eq_dev_resp,
                        height=220, key="eq_dev_txt",
                        placeholder="Desarrolla con fundamento legal. Cita artículos y autores...")
    st.session_state.eq_dev_resp = resp

    c1, c2 = st.columns([3, 1])
    with c1:
        evaluar = st.button("🤖 Evaluar con IA", type="primary",
                            disabled=len(resp.strip()) < 40, use_container_width=True)
    with c2:
        if st.button("→ Otra", use_container_width=True):
            _hist_add(item.get("tema", pregunta[:60]))
            _reset_item()
            st.rerun()

    if len(resp.strip()) < 40 and resp.strip():
        st.caption("Escribe al menos 40 caracteres.")

    if evaluar and llm and len(resp.strip()) >= 40:
        _hist_add(item.get("tema", pregunta[:60]))
        st.session_state.eq_n += 1
        with st.spinner("Evaluando..."):
            try:
                prompt = f"""Eres un profesor de derecho chileno evaluando una respuesta de examen.

PREGUNTA: {pregunta}

RESPUESTA:
{resp}

Evalúa brevemente (máx 250 palabras):
• Nota del 1.0 al 7.0
• Qué está bien (2 puntos)
• Qué mejorar (2 puntos)
• Norma o doctrina clave que faltó"""
                st.session_state.eq_dev_eval = llm.complete(prompt)
            except Exception as e:
                st.session_state.eq_dev_eval = f"Error: {e}"

    if st.session_state.eq_dev_eval:
        st.markdown(f'<div class="eq-fund">{st.session_state.eq_dev_eval}</div>', unsafe_allow_html=True)
        if st.button("→ Nueva pregunta", use_container_width=True):
            _reset_item()
            st.rerun()


# ── Caso Práctico ─────────────────────────────────────────────
def _render_caso(llm):
    if not _ensure_item("caso", llm):
        return
    item  = st.session_state.eq_item
    resps = st.session_state.eq_caso_resps
    n     = st.session_state.eq_n + 1

    st.markdown(f"""<div class="eq-card">
      <div class="eq-num">#{n} · Caso Práctico · {_full(st.session_state.eq_curso)}</div>
      <div style="font-size:0.8rem;font-weight:700;color:{_GOLD};margin-bottom:0.6rem;">{item.get('titulo','Caso')}</div>
      <div class="eq-pregunta" style="font-weight:400;font-size:0.92rem;color:#d4c5a0;">{item['enunciado']}</div>
    </div>""", unsafe_allow_html=True)

    for i, preg in enumerate(item["preguntas"]):
        st.markdown(f"**{i+1}. {preg}**")
        resps[i] = st.text_area(f"r{i}", value=resps.get(i, ""), height=90,
                                key=f"eq_caso_r{i}", label_visibility="collapsed",
                                placeholder="Tu respuesta...")
    st.session_state.eq_caso_resps = resps

    total = sum(len(r) for r in resps.values())
    c1, c2 = st.columns([3, 1])
    with c1:
        evaluar = st.button("🤖 Evaluar caso", type="primary",
                            disabled=total < 80, use_container_width=True)
    with c2:
        if st.button("→ Otro caso", use_container_width=True):
            _hist_add(item.get("tema", item.get("titulo", "")[:50]))
            _reset_item()
            st.rerun()

    if evaluar and llm and total >= 80:
        _hist_add(item.get("tema", item.get("titulo", "")[:50]))
        st.session_state.eq_n += 1
        with st.spinner("Analizando el caso..."):
            try:
                txt = "\n".join([f"P{i+1}: {item['preguntas'][i]}\nR: {resps.get(i,'')}"
                                  for i in range(len(item["preguntas"]))])
                prompt = f"""Evalúa este caso práctico de derecho chileno.
CASO: {item.get('titulo','')}
{item['enunciado']}

RESPUESTAS:
{txt}

Entrega nota global 1-7, análisis por pregunta, normas clave. Máx 300 palabras."""
                st.session_state.eq_caso_eval = llm.complete(prompt)
            except Exception as e:
                st.session_state.eq_caso_eval = f"Error: {e}"

    if st.session_state.eq_caso_eval:
        st.markdown(f'<div class="eq-fund">{st.session_state.eq_caso_eval}</div>', unsafe_allow_html=True)
        if st.button("→ Nuevo caso", use_container_width=True):
            _reset_item()
            st.rerun()


# ═══════════════════════════════════════════════════════════════
# RENDER PRINCIPAL
# ═══════════════════════════════════════════════════════════════
def render_academia(llm_client=None):
    _init()
    _css()
    st.session_state["_llm_client"] = llm_client

    # ── Header ──────────────────────────────────────────────────
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:0.8rem;margin-bottom:1.4rem;">
      <div style="background:linear-gradient(135deg,#2a241a,#1e1b16);
                  border:1px solid rgba(201,150,58,0.3);border-radius:12px;
                  padding:0.8rem 1.3rem;flex:1;">
        <span style="font-size:0.58rem;font-weight:700;color:rgba(201,150,58,0.5);
                     text-transform:uppercase;letter-spacing:0.12em;">AntonIA · Mar.IA Group</span><br>
        <span style="font-size:1.5rem;font-weight:900;color:{_WHITE};">🧠 ENTRENA</span>
        <span style="font-size:0.8rem;color:{_MUTED};margin-left:0.7rem;">Quiz legal infinito</span>
      </div>
    </div>""", unsafe_allow_html=True)

    # ── Score bar ────────────────────────────────────────────────
    _score_bar()

    # ── CSS responsive (móvil + desktop) ────────────────────────
    st.markdown("""
    <style>
    /* Botones de ramo más compactos en móvil */
    @media (max-width: 640px) {
        div[data-testid="column"] > div > div > div > button {
            font-size: 0.68rem !important;
            padding: 0.35rem 0.2rem !important;
            min-height: 2.4rem !important;
        }
        /* Ocultar texto largo, mostrar solo ícono en pantallas muy pequeñas */
        .ramo-label-full { display: none; }
        .ramo-label-short { display: inline; }
    }
    @media (min-width: 641px) {
        .ramo-label-full { display: inline; }
        .ramo-label-short { display: none; }
    }
    /* Ancla para scroll */
    #paso-tipo { scroll-margin-top: 80px; }
    #paso-quiz { scroll-margin-top: 80px; }
    </style>
    """, unsafe_allow_html=True)

    # ── PASO 1: Selección de ramo ────────────────────────────────
    cid = st.session_state.eq_curso

    # Grupo Derecho Civil
    civil_cursos = [c for c in CURSOS if c.get("grupo") == "civil"]
    otro_cursos  = [c for c in CURSOS if c.get("grupo") == "otro"]

    st.markdown(f"""
    <div style='font-size:0.62rem;color:{_MUTED};text-transform:uppercase;
                letter-spacing:0.1em;margin-bottom:0.4rem;font-weight:700;'>① Elige el ramo</div>
    <div style='font-size:0.7rem;color:{_GOLD};font-weight:600;margin-bottom:0.3rem;'>
        📚 Derecho Civil
    </div>""", unsafe_allow_html=True)

    # Fila Civil — 5 columnas
    civil_cols = st.columns(len(civil_cursos))
    for i, c in enumerate(civil_cursos):
        with civil_cols[i]:
            act = cid == c["id"]
            label = f"{c['icono']} {c['nombre']}\n{c['full'].split('—')[1].strip() if '—' in c['full'] else ''}"
            if st.button(f"{c['icono']} {c['nombre']}", key=f"eq_c_civil_{c['id']}",
                         use_container_width=True, type="primary" if act else "secondary",
                         help=c["full"]):
                if not act:
                    st.session_state.eq_curso = c["id"]
                    st.session_state.eq_tipo  = None
                    _reset_item()
                    st.rerun()

    st.markdown(f"""
    <div style='font-size:0.7rem;color:{_MUTED};font-weight:600;
                margin:0.6rem 0 0.3rem;'>
        🏛️ Otras áreas
    </div>""", unsafe_allow_html=True)

    # Fila otras áreas — 7 columnas (responsive: 4 en móvil vía CSS)
    otro_cols = st.columns(len(otro_cursos))
    for i, c in enumerate(otro_cursos):
        with otro_cols[i]:
            act = cid == c["id"]
            if st.button(f"{c['icono']} {c['nombre']}", key=f"eq_c_otro_{c['id']}",
                         use_container_width=True, type="primary" if act else "secondary",
                         help=c["full"]):
                if not act:
                    st.session_state.eq_curso = c["id"]
                    st.session_state.eq_tipo  = None
                    _reset_item()
                    st.rerun()

    # Si no hay ramo seleccionado, mostrar instrucción
    if not cid:
        st.markdown(f"""
        <div style="margin-top:1.5rem;text-align:center;color:{_MUTED};font-size:0.85rem;
                    padding:1rem;border:1px dashed rgba(201,150,58,0.2);border-radius:8px;">
            👆 Selecciona un ramo para comenzar
        </div>""", unsafe_allow_html=True)
        return

    # ── Banner ramo activo ────────────────────────────────────────
    curso_activo = next((c for c in CURSOS if c["id"] == cid), None)
    if curso_activo:
        st.markdown(f"""
        <div id="paso-tipo" style="margin:0.8rem 0 0.6rem;padding:0.6rem 1rem;
                  background:rgba(201,150,58,0.08);border-left:3px solid {_GOLD};
                  border-radius:0 8px 8px 0;display:flex;align-items:center;gap:0.5rem;">
          <span style="font-size:1.1rem;">{curso_activo['icono']}</span>
          <div>
            <div style="font-size:0.65rem;color:{_MUTED};text-transform:uppercase;
                        letter-spacing:0.08em;">Ramo seleccionado</div>
            <div style="font-size:0.9rem;font-weight:700;color:{_WHITE};">{curso_activo['full']}</div>
          </div>
        </div>""", unsafe_allow_html=True)

    # ── PASO 2: Selección de tipo ─────────────────────────────────
    tid = st.session_state.eq_tipo
    st.markdown(f"""
    <div style='font-size:0.62rem;color:{_MUTED};text-transform:uppercase;
                letter-spacing:0.1em;margin-bottom:0.5rem;font-weight:700;'>
        ② Tipo de pregunta
    </div>""", unsafe_allow_html=True)

    tcols = st.columns(len(TIPOS))
    for i, t in enumerate(TIPOS):
        with tcols[i]:
            act = tid == t["id"]
            if st.button(f"{t['icono']} {t['label']}", key=f"eq_t_{t['id']}",
                         use_container_width=True, type="primary" if act else "secondary"):
                if not act:
                    st.session_state.eq_tipo = t["id"]
                    _reset_item()
                    st.rerun()

    # Si no hay tipo, flecha animada indicando que hay que elegir
    if not tid:
        st.markdown(f"""
        <div id="paso-tipo-hint" style="margin-top:1rem;text-align:center;
                  color:{_GOLD};font-size:0.85rem;animation:pulse 1.5s infinite;">
            👆 Elige el tipo de pregunta para comenzar
        </div>
        <style>
        @keyframes pulse {{
            0%,100% {{ opacity:1; }} 50% {{ opacity:0.4; }}
        }}
        </style>""", unsafe_allow_html=True)
        return

    # ── PASO 3: Quiz ─────────────────────────────────────────────
    st.markdown(f"""
    <div id="paso-quiz" style="margin:0.5rem 0;">
        <hr style='border-color:rgba(201,150,58,0.15);margin:0.5rem 0;'>
    </div>""", unsafe_allow_html=True)

    if   tid == "mcq":        _render_mcq(llm_client)
    elif tid == "vf":         _render_vf(llm_client)
    elif tid == "flashcard":  _render_flashcard(llm_client)
    elif tid == "desarrollo": _render_desarrollo(llm_client)
    elif tid == "caso":       _render_caso(llm_client)
