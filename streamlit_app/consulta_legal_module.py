"""
consulta_legal_module.py — AntonIA · Consulta Legal para Ciudadanos
Asesoría jurídica basada en el Derecho chileno vigente.
Sin alucinaciones — sin inventar normas — sin reemplazar al abogado.
"""
import streamlit as st
from pathlib import Path

_GOLD = "#c9963a"
_DARK = "#141210"

_CSS = ('<style>'
'.cl-header{font-family:"Playfair Display",serif;font-size:1.8rem;font-weight:700;color:#f5f0e8;margin-bottom:.2rem;}'
'.cl-sub{font-size:1rem;color:#a08050;margin-bottom:1.2rem;}'
'.cl-disclaimer{background:rgba(201,150,58,.08);border:1px solid rgba(201,150,58,.25);border-radius:8px;padding:.7rem 1rem;font-size:.78rem;color:#9a8a6a;line-height:1.6;margin-bottom:1.2rem;}'
'</style>')

_SYSTEM_CONSULTA = (
    "Eres AntonIA, asistente de consulta legal para ciudadanos chilenos. "
    "Respondes preguntas legales basadas EXCLUSIVAMENTE en el Derecho chileno vigente. "
    "Eres claro, preciso y accesible: no usas jerga técnica innecesaria, explicas los conceptos clave. "
    "REGLAS CRÍTICAS: "
    "1. NUNCA inventes normas, artículos, fechas ni sentencias — si no sabes, lo dices claramente. "
    "2. SIEMPRE indica qué ley o artículo aplica cuando lo sabes con certeza. "
    "3. SIEMPRE concluye si la situación requiere un abogado o no. "
    "4. NO das consejos específicos de estrategia legal — describes el marco normativo aplicable. "
    "5. Usas español chileno natural, sin rebuscamiento. "
    "TEMAS QUE MANEJAS: contratos, arrendamiento, trabajo, familia, herencias, "
    "consumidor, multas, deudas, accidentes, delitos comunes, trámites estatales."
)

_TOPICS = [
    "🏠 Arrendamiento y vivienda",
    "💼 Laboral y despidos",
    "👨‍👩‍👧 Familia y divorcio",
    "📋 Contratos",
    "🛒 Derechos del consumidor",
    "⚖️ Deudas y cobranzas",
    "🚗 Accidentes y seguros",
    "📜 Herencias y testamentos",
    "🏛️ Trámites con el Estado",
    "🔒 Privacidad y datos",
    "💊 Salud y negligencia médica",
    "🌐 Otro tema legal",
]


def render_consulta_legal(get_llm_fn=None):
    """Renderiza el módulo de Consulta Legal para ciudadanos."""
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── VIDEO DE PRESENTACIÓN ────────────────────────────────────
    _vid_cl = Path(__file__).parent / "static" / "promo_consulta.mp4"
    if _vid_cl.exists() and not st.session_state.get("cl_promo_seen", False):
        st.markdown(
            '<div style="background:#04030e;padding:28px 20px 0;text-align:center;border-bottom:1px solid rgba(201,150,58,.2);">'
            '<p style="font-family:Inter,sans-serif;font-size:.72rem;color:#c9963a;text-transform:uppercase;letter-spacing:.2em;font-weight:700;margin-bottom:10px;">💬 Respuestas Legales Reales. En Segundos.</p>'
            '</div>', unsafe_allow_html=True)
        try:
            st.video(str(_vid_cl), autoplay=True, muted=True)
        except TypeError:
            st.video(str(_vid_cl))
        st.markdown(
            '<div style="padding:20px;text-align:center;background:linear-gradient(180deg,#04030e,#0d0b09);">'
            '<p style="font-family:\'Playfair Display\',serif;font-size:1.3rem;font-weight:800;color:#f5f0e8;margin-bottom:8px;">Por primera vez, el Derecho chileno está en tus manos.</p>'
            '<p style="font-size:.88rem;color:rgba(240,232,218,.78);line-height:1.8;max-width:600px;margin:0 auto 16px;">'
            '✦ Contratos · Despidos · Arriendos · Familia · Derechos del consumidor<br>'
            '✦ Sin citas · Sin esperas · Sin honorarios por consulta<br>'
            '✦ Basado en la ley chilena vigente · Sin alucinaciones</p>'
            '<p style="font-size:.78rem;color:rgba(201,150,58,.6);font-style:italic;">No reemplaza a tu abogado — te prepara para hablar con él de igual a igual.</p>'
            '</div>', unsafe_allow_html=True)
        if st.button("Hacer mi consulta →", type="primary", use_container_width=False, key="cl_promo_btn"):
            st.session_state.cl_promo_seen = True
            st.rerun()
        st.stop()
    # ── FIN VIDEO ────────────────────────────────────────────────

    # ── INICIALIZAR ESTADO ───────────────────────────────────────
    if "cl_history" not in st.session_state:
        st.session_state.cl_history = []
    if "cl_topic" not in st.session_state:
        st.session_state.cl_topic = None

    # ── HEADER ──────────────────────────────────────────────────
    st.markdown('<div class="cl-header">💬 Consulta Legal</div>', unsafe_allow_html=True)
    st.markdown('<div class="cl-sub">Respuestas basadas en el Derecho chileno vigente · Sin honorarios por consulta</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="cl-disclaimer">'
        '⚠️ <strong>Importante:</strong> AntonIA entrega información jurídica general. '
        'No reemplaza la asesoría de un abogado. Para situaciones urgentes o complejas, '
        'consulta con un profesional del Derecho.'
        '</div>', unsafe_allow_html=True)

    # ── SELECTOR DE TEMA (primera vez) ──────────────────────────
    if not st.session_state.cl_history:
        st.markdown('<div style="font-size:.78rem;color:rgba(201,150,58,.8);text-transform:uppercase;letter-spacing:.1em;font-weight:700;margin-bottom:.6rem;">¿Sobre qué tema es tu consulta?</div>', unsafe_allow_html=True)
        topic_cols = st.columns(4)
        for i, topic in enumerate(_TOPICS):
            col = topic_cols[i % 4]
            if col.button(topic, key=f"cl_topic_{i}", use_container_width=True):
                st.session_state.cl_topic = topic
                intro_msg = f"Quiero hacer una consulta sobre: {topic}"
                st.session_state.cl_history.append({"role": "user", "content": intro_msg})
                st.rerun()

    # ── HISTORIAL DE MENSAJES ────────────────────────────────────
    for msg in st.session_state.cl_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ── RESPUESTA PENDIENTE ──────────────────────────────────────
    if (st.session_state.cl_history and
            st.session_state.cl_history[-1]["role"] == "user" and
            get_llm_fn):
        with st.chat_message("assistant"):
            with st.spinner("Analizando tu consulta…"):
                try:
                    history_ctx = "\n".join(
                        f"{'Ciudadano' if m['role'] == 'user' else 'AntonIA'}: {m['content']}"
                        for m in st.session_state.cl_history[-8:]
                    )
                    prompt_cl = f"Conversación:\n{history_ctx}"
                    llm = get_llm_fn()
                    resp_cl = llm.generate(prompt_cl, system=_SYSTEM_CONSULTA, max_tokens=1400)
                    st.markdown(resp_cl)
                    st.session_state.cl_history.append({"role": "assistant", "content": resp_cl})
                except Exception as e:
                    st.error(f"Error al conectar: {e}")

    # ── INPUT ────────────────────────────────────────────────────
    if st.session_state.cl_history or st.session_state.cl_topic:
        if user_cl := st.chat_input("Escribe tu consulta legal…"):
            st.session_state.cl_history.append({"role": "user", "content": user_cl})
            st.rerun()

    # ── CONTROLES ────────────────────────────────────────────────
    if st.session_state.cl_history:
        col_x1, col_x2 = st.columns([5, 1])
        with col_x2:
            if st.button("Nueva consulta", key="cl_clear", use_container_width=True):
                st.session_state.cl_history = []
                st.session_state.cl_topic = None
                st.rerun()
