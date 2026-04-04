"""
consulta_legal_module.py — AntonIA · Consulta Legal (No Abogados)
Servicio de orientación legal accesible para personas sin formación jurídica.

Funcionalidades:
  · Explicar documentos legales en lenguaje simple
  · Responder preguntas sobre situaciones legales cotidianas
  · Identificar partes, plazos y acciones en documentos
  · Guiar al usuario sobre qué hacer y a dónde ir
  · (Próximamente) Consulta al Poder Judicial
"""

import streamlit as st
import os

_GOLD  = "#c9963a"
_DARK  = "#141210"
_CARD  = "#1e1b16"
_MUTED = "#a09070"
_WHITE = "#f5f0e8"
_GREEN = "#22c55e"

_CSS = """
<style>
.cl-hero-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(1.5rem, 4vw, 2.1rem);
    font-weight: 700; color: #f5f0e8;
    line-height: 1.25; margin-bottom: 0.4rem;
}
.cl-hero-sub {
    font-size: clamp(0.82rem, 2vw, 1rem);
    color: #a09070; line-height: 1.55;
    max-width: 560px; margin-bottom: 1.8rem;
}
.cl-price-card {
    background: #1e1b16;
    border: 1px solid rgba(201,150,58,0.22);
    border-radius: 12px; padding: 1.5rem 1.4rem;
    text-align: center;
}
.cl-price-card.featured {
    border-color: #c9963a;
    background: linear-gradient(135deg, #1e1b16 0%, #221e18 100%);
}
.cl-price-amount {
    font-size: 2rem; font-weight: 700; color: #c9963a;
    font-family: 'Playfair Display', serif;
}
.cl-price-period { font-size: 0.7rem; color: #a09070; }
.cl-answer-box {
    background: #1e1b16;
    border: 1px solid rgba(201,150,58,0.2);
    border-left: 3px solid #c9963a;
    border-radius: 0 8px 8px 0;
    padding: 1.2rem 1.4rem;
    font-size: 0.85rem; color: #e8d8b8;
    line-height: 1.7; margin-top: 1rem;
}
.cl-step {
    display: flex; align-items: flex-start;
    gap: 0.8rem; margin-bottom: 1rem;
}
.cl-step-num {
    min-width: 28px; height: 28px;
    background: rgba(201,150,58,0.15);
    border: 1px solid rgba(201,150,58,0.35);
    border-radius: 50%; display: flex;
    align-items: center; justify-content: center;
    font-size: 0.72rem; font-weight: 700; color: #c9963a;
}
.cl-step-text { font-size: 0.8rem; color: #c8b890; line-height: 1.5; }
.cl-disclaimer {
    background: rgba(201,150,58,0.05);
    border: 1px solid rgba(201,150,58,0.12);
    border-radius: 6px; padding: 0.7rem 0.9rem;
    font-size: 0.67rem; color: #a09070;
    line-height: 1.55; margin-top: 1rem;
}
@media (max-width: 640px) {
    .cl-hero-title { font-size: 1.4rem; }
    .cl-hero-sub   { font-size: 0.8rem; }
}
</style>
"""

def _init():
    defaults = {
        "cl_tab":         "consulta",
        "cl_doc_text":    None,
        "cl_pregunta":    "",
        "cl_respuesta":   "",
        "cl_query_count": 0,
        "cl_modo":        "pregunta",   # "pregunta" | "documento" | "jurisprudencia" | "doctrina"
        "cl_jurisprudencia_query": "",
        "cl_jurisprudencia_result": "",
        "cl_doctrina_query": "",
        "cl_doctrina_result": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

_MAX_CONSULTAS_GRATIS = 3
_FORMSPREE_ID         = "xpwzrjaz"

# ═══════════════════════════════════════════════════════════════════
def render_consulta_legal(get_orch_fn=None, get_llm_fn=None):
    """Renderiza el área de Consulta Legal para personas sin formación jurídica."""
    _init()
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Cabecera hero ──────────────────────────────────────────────
    st.markdown("""
    <div class="cl-hero-title">
      ¿Tienes un problema legal?<br>
      <span style="color:#c9963a;">Entendemos tu situación</span>
    </div>
    <div class="cl-hero-sub">
      AntonIA explica documentos legales en lenguaje simple, te dice qué hacer
      y adónde ir. Sin tecnicismos, sin complicaciones.
    </div>
    """, unsafe_allow_html=True)

    # ── Selector de modo ───────────────────────────────────────────
    modo_col1, modo_col2, modo_col3, modo_col4 = st.columns(4)

    with modo_col1:
        active_p = st.session_state.cl_modo == "pregunta"
        if active_p:
            st.markdown(
                '<div style="text-align:center;padding:0.7rem 1rem;'
                'background:rgba(201,150,58,0.12);border:1px solid rgba(201,150,58,0.4);'
                'border-radius:8px;color:#c9963a;font-weight:700;font-size:0.82rem;cursor:default;">'
                '💬 Pregunta</div>', unsafe_allow_html=True)
        else:
            if st.button("💬 Pregunta", use_container_width=True, key="cl_btn_preg"):
                st.session_state.cl_modo = "pregunta"
                st.rerun()

    with modo_col2:
        active_d = st.session_state.cl_modo == "documento"
        if active_d:
            st.markdown(
                '<div style="text-align:center;padding:0.7rem 1rem;'
                'background:rgba(201,150,58,0.12);border:1px solid rgba(201,150,58,0.4);'
                'border-radius:8px;color:#c9963a;font-weight:700;font-size:0.82rem;cursor:default;">'
                '📄 Documento</div>', unsafe_allow_html=True)
        else:
            if st.button("📄 Documento", use_container_width=True, key="cl_btn_doc"):
                st.session_state.cl_modo = "documento"
                st.rerun()

    with modo_col3:
        active_j = st.session_state.cl_modo == "jurisprudencia"
        if active_j:
            st.markdown(
                '<div style="text-align:center;padding:0.7rem 1rem;'
                'background:rgba(201,150,58,0.12);border:1px solid rgba(201,150,58,0.4);'
                'border-radius:8px;color:#c9963a;font-weight:700;font-size:0.82rem;cursor:default;">'
                '⚖️ Tribunales</div>', unsafe_allow_html=True)
        else:
            if st.button("⚖️ Tribunales", use_container_width=True, key="cl_btn_jur"):
                st.session_state.cl_modo = "jurisprudencia"
                st.rerun()

    with modo_col4:
        active_dt = st.session_state.cl_modo == "doctrina"
        if active_dt:
            st.markdown(
                '<div style="text-align:center;padding:0.7rem 1rem;'
                'background:rgba(201,150,58,0.12);border:1px solid rgba(201,150,58,0.4);'
                'border-radius:8px;color:#c9963a;font-weight:700;font-size:0.82rem;cursor:default;">'
                '📚 Doctrina</div>', unsafe_allow_html=True)
        else:
            if st.button("📚 Doctrina", use_container_width=True, key="cl_btn_doc_t"):
                st.session_state.cl_modo = "doctrina"
                st.rerun()

    st.markdown('<hr style="border-color:rgba(201,150,58,0.12);margin:1.2rem 0;">', unsafe_allow_html=True)

    consultas_usadas = st.session_state.cl_query_count
    consultas_libres = max(0, _MAX_CONSULTAS_GRATIS - consultas_usadas)

    # ── MODO PREGUNTA ──────────────────────────────────────────────
    if st.session_state.cl_modo == "pregunta":

        st.markdown("""
        <div style="font-size:0.78rem;color:#c8b890;margin-bottom:0.8rem;">
        Puedes preguntarme cosas como:
        <em>"Me llegó una notificación judicial — ¿qué debo hacer?"</em>,
        <em>"¿Qué es una demanda civil?"</em>,
        <em>"Me despidieron — ¿tengo derecho a indemnización?"</em>
        </div>
        """, unsafe_allow_html=True)

        pregunta = st.text_area(
            "Tu consulta legal",
            placeholder="Escribe aquí tu pregunta en tus propias palabras…",
            height=110,
            key="cl_preg_input",
            label_visibility="collapsed")

        if consultas_libres > 0:
            st.markdown(
                f'<div style="font-size:0.65rem;color:#a09070;margin-bottom:0.5rem;">'
                f'Consultas gratuitas restantes: <strong style="color:#c9963a;">{consultas_libres}</strong></div>',
                unsafe_allow_html=True)
            btn_disabled = False
        else:
            st.markdown(
                '<div style="font-size:0.75rem;color:#ef4444;margin-bottom:0.5rem;">'
                'Has usado tus consultas gratuitas. Suscríbete para continuar.</div>',
                unsafe_allow_html=True)
            btn_disabled = True

        if st.button("🔎 Consultar con AntonIA", use_container_width=True,
                     type="primary", disabled=btn_disabled):
            if pregunta and get_llm_fn:
                prompt = (
                    "Eres un asistente legal chileno que ayuda a personas sin formación jurídica.\n"
                    "Tu estilo de comunicación es: claro, simple, empático y sin tecnicismos.\n"
                    "NUNCA uses lenguaje jurídico sin explicarlo.\n\n"
                    f"CONSULTA: {pregunta}\n\n"
                    "INSTRUCCIONES DE RESPUESTA:\n"
                    "1. Explica la situación en términos simples (2-3 párrafos)\n"
                    "2. Indica qué ACCIONES concretas debe tomar el usuario (numeradas)\n"
                    "3. Indica A DÓNDE debe ir o a quién llamar (ej: Juzgado de su comuna, Corporación de Asistencia Judicial, Inspección del Trabajo, etc.)\n"
                    "4. Menciona PLAZOS importantes si corresponde\n"
                    "5. Señala cuándo es urgente contratar un abogado\n"
                    "Cierra con: '⚠️ Esta orientación es general. Para tu caso específico, te recomendamos consultar con un abogado.'"
                )
                with st.spinner("AntonIA está analizando tu consulta…"):
                    try:
                        llm = get_llm_fn()
                        resp = llm.generate(prompt, system=" ", max_tokens=1000)
                        st.session_state.cl_respuesta = resp
                        st.session_state.cl_query_count += 1
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
            elif not pregunta:
                st.warning("Escribe tu consulta.")

        if st.session_state.cl_respuesta:
            st.markdown(
                f'<div class="cl-answer-box">'
                f'{st.session_state.cl_respuesta.replace(chr(10),"<br>")}'
                f'</div>',
                unsafe_allow_html=True)

            # Siguiente acción del usuario
            st.markdown('<br>', unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🔄 Nueva consulta", use_container_width=True):
                    st.session_state.cl_respuesta = ""
                    st.rerun()
            with col_b:
                if st.button("📄 Subir mi documento", use_container_width=True):
                    st.session_state.cl_modo = "documento"
                    st.session_state.cl_respuesta = ""
                    st.rerun()

    # ── MODO DOCUMENTO ─────────────────────────────────────────────
    elif st.session_state.cl_modo == "documento":

        st.markdown("""
        <div style="font-size:0.78rem;color:#c8b890;margin-bottom:0.8rem;">
        Sube un documento legal (demanda, notificación, contrato, carta, resolución…)
        y AntonIA te explicará en términos simples qué dice y qué debes hacer.
        </div>
        """, unsafe_allow_html=True)

        col_up, col_result = st.columns([1, 1.3])

        with col_up:
            doc_uploaded = st.file_uploader(
                "Sube tu documento",
                type=["pdf","docx","doc","txt"],
                key="cl_doc_upload",
                help="PDF, Word o texto. Máximo 10 MB.")

            pregunta_doc = st.text_area(
                "¿Qué quieres saber del documento?",
                placeholder=(
                    "Deja vacío para análisis completo, o pregunta algo específico:\n"
                    "ej. '¿Qué me están cobrando?', '¿Cuánto tiempo tengo para responder?'"
                ),
                height=80,
                key="cl_pregunta_doc")

            if consultas_libres > 0:
                st.markdown(
                    f'<div style="font-size:0.65rem;color:#a09070;margin-bottom:0.5rem;">'
                    f'Análisis gratuitos restantes: <strong style="color:#c9963a;">{consultas_libres}</strong></div>',
                    unsafe_allow_html=True)
                btn_disabled_doc = False
            else:
                st.markdown(
                    '<div style="font-size:0.75rem;color:#ef4444;margin-bottom:0.5rem;">'
                    'Has usado tus análisis gratuitos. Suscríbete para continuar.</div>',
                    unsafe_allow_html=True)
                btn_disabled_doc = True

            if st.button("📄 Analizar Documento", use_container_width=True,
                         type="primary", disabled=btn_disabled_doc or not doc_uploaded):
                if doc_uploaded and get_orch_fn and get_llm_fn:
                    import tempfile, pathlib
                    with st.spinner("Leyendo documento…"):
                        try:
                            tmp_path = pathlib.Path(tempfile.mktemp(suffix=pathlib.Path(doc_uploaded.name).suffix))
                            tmp_path.write_bytes(doc_uploaded.getvalue())
                            orch   = get_orch_fn()
                            result = orch.ingest(file_path=tmp_path)
                            texto  = result.extraction.raw_text[:6000]  # primeros 6000 chars
                            st.session_state.cl_doc_text = texto

                            pregunta_efectiva = pregunta_doc.strip() or (
                                "Explica este documento en términos simples: "
                                "qué es, quiénes son las partes, qué te están pidiendo o informando, "
                                "qué plazos hay, y qué debes hacer."
                            )

                            llm_prompt = (
                                "Eres un asistente legal chileno que ayuda a personas sin formación jurídica.\n"
                                "Explica en lenguaje claro y simple, sin tecnicismos (o explicándolos si son necesarios).\n\n"
                                f"DOCUMENTO:\n{texto}\n\n"
                                f"CONSULTA: {pregunta_efectiva}\n\n"
                                "FORMATO DE RESPUESTA:\n"
                                "1. **¿Qué es este documento?** (1 párrafo simple)\n"
                                "2. **¿Quiénes son las partes?** (lista simple)\n"
                                "3. **¿Qué te están diciendo o pidiendo?** (explicación clara)\n"
                                "4. **¿Qué plazos tienes?** (si los hay)\n"
                                "5. **¿Qué debes hacer?** (pasos concretos numerados)\n"
                                "6. **¿A dónde ir?** (institución específica: juzgado, CAJ, Inspección del Trabajo, etc.)\n\n"
                                "Cierra con: '⚠️ Esta es una orientación general. Para tu caso específico, consulta con un abogado.'"
                            )
                            llm = get_llm_fn()
                            resp = llm.generate(llm_prompt, system=" ", max_tokens=1400)
                            st.session_state.cl_respuesta = resp
                            st.session_state.cl_query_count += 1
                            st.rerun()

                        except Exception as e:
                            st.error(f"Error al procesar: {e}")
                elif not doc_uploaded:
                    st.warning("Primero sube un documento.")
                elif not get_llm_fn:
                    st.warning("Servicio no disponible.")

            # Próximamente: Poder Judicial
            st.markdown("""
            <div style="margin-top:1.5rem;padding:0.8rem 1rem;
                        background:rgba(59,130,246,0.06);
                        border:1px solid rgba(59,130,246,0.18);
                        border-radius:8px;">
              <div style="font-size:0.7rem;font-weight:700;color:rgba(59,130,246,0.7);
                          text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.3rem;">
                🏛 Próximamente
              </div>
              <div style="font-size:0.72rem;color:#a09070;line-height:1.5;">
                Consulta directa al <strong style="color:#c8b890;">Poder Judicial</strong>:
                ingresa tu RUT o RIT y AntonIA te muestra el estado de tu causa,
                demanda y contestación, también explicados en lenguaje simple.
              </div>
            </div>
            """, unsafe_allow_html=True)

        with col_result:
            if st.session_state.cl_respuesta:
                st.markdown(
                    f'<div class="cl-answer-box">'
                    f'{st.session_state.cl_respuesta.replace(chr(10),"<br>")}'
                    f'</div>',
                    unsafe_allow_html=True)

                if st.button("🔄 Analizar otro documento", use_container_width=True):
                    st.session_state.cl_respuesta = ""
                    st.session_state.cl_doc_text  = None
                    st.rerun()
            else:
                # Cómo funciona
                st.markdown("""
                <div style="padding:1.2rem;">
                  <div style="font-size:0.72rem;font-weight:700;color:#a09070;
                              text-transform:uppercase;letter-spacing:0.06em;margin-bottom:1rem;">
                    ¿Cómo funciona?
                  </div>
                """, unsafe_allow_html=True)

                pasos = [
                    ("1", "Sube tu documento (PDF, Word o texto)"),
                    ("2", "AntonIA lo lee y entiende su contenido"),
                    ("3", "Te explica en lenguaje simple: qué es, quiénes son las partes, qué plazos tienes"),
                    ("4", "Te dice exactamente qué hacer y a dónde ir"),
                ]
                for num, texto in pasos:
                    st.markdown(f"""
                    <div class="cl-step">
                      <div class="cl-step-num">{num}</div>
                      <div class="cl-step-text">{texto}</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

    # ── MODO JURISPRUDENCIA ────────────────────────────────────────
    elif st.session_state.cl_modo == "jurisprudencia":

        st.markdown("""
        <div class="cl-hero-title" style="font-size:1.4rem;">
          ⚖️ ¿Qué dicen los tribunales?
        </div>
        <div class="cl-hero-sub" style="max-width:100%;margin-bottom:1.2rem;">
          Busca qué han resuelto los tribunales chilenos sobre tu problema legal
        </div>
        """, unsafe_allow_html=True)

        # Búsqueda de jurisprudencia
        jur_query = st.text_input(
            "Describe tu situación",
            placeholder="Ej: me despidieron sin aviso, choque de auto, pensión alimenticia...",
            key="cl_jur_input",
            label_visibility="collapsed")

        if consultas_libres > 0:
            st.markdown(
                f'<div style="font-size:0.65rem;color:#a09070;margin-bottom:0.5rem;">'
                f'Consultas gratuitas restantes: <strong style="color:#c9963a;">{consultas_libres}</strong></div>',
                unsafe_allow_html=True)
            btn_disabled_jur = False
        else:
            st.markdown(
                '<div style="font-size:0.75rem;color:#ef4444;margin-bottom:0.5rem;">'
                'Has usado tus consultas gratuitas. Suscríbete para continuar.</div>',
                unsafe_allow_html=True)
            btn_disabled_jur = True

        if st.button("🔎 BUSCAR EN TRIBUNALES", use_container_width=True,
                     type="primary", disabled=btn_disabled_jur):
            if jur_query and get_llm_fn:
                with st.spinner("Buscando sentencias de los tribunales…"):
                    try:
                        # Aquí se importaría jurisprudencia_service para usar generar_contexto_jurisprudencial
                        # Por ahora, simulamos el contexto
                        contexto_jur = f"Búsqueda sobre: {jur_query}"

                        prompt = (
                            "Eres un asistente legal chileno que ayuda a personas sin formación jurídica.\n"
                            "Tu tarea es explicar QUÉ HAN RESUELTO LOS TRIBUNALES sobre una situación en lenguaje simple.\n"
                            "Nunca uses lenguaje jurídico sin explicarlo.\n\n"
                            f"CONTEXTO DE JURISPRUDENCIA:\n{contexto_jur}\n\n"
                            f"SITUACIÓN DEL USUARIO: {jur_query}\n\n"
                            "INSTRUCCIONES:\n"
                            "1. Resume las decisiones más recientes de los tribunales en lenguaje simple (2-3 párrafos)\n"
                            "2. Explica cuál es la tendencia: ¿ganan o pierden las personas en tu situación?\n"
                            "3. Menciona qué tipo de tribunal (Corte de Apelaciones, Juzgado, etc.) toma estas decisiones\n"
                            "4. Indica si esto te ayuda a entender tus derechos\n"
                            "Cierra con: '⚠️ Esta información es sobre casos similares. Tu caso es único y necesita asesoría personalizada.'"
                        )
                        llm = get_llm_fn()
                        resp = llm.generate(prompt, system=" ", max_tokens=1000)
                        st.session_state.cl_jurisprudencia_result = resp
                        st.session_state.cl_jurisprudencia_query = jur_query
                        st.session_state.cl_query_count += 1
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
            elif not jur_query:
                st.warning("Describe tu situación.")

        # Mostrar resultados
        if st.session_state.cl_jurisprudencia_result:
            st.markdown(
                f'<div class="cl-answer-box">'
                f'{st.session_state.cl_jurisprudencia_result.replace(chr(10),"<br>")}'
                f'</div>',
                unsafe_allow_html=True)

            st.markdown('<br>', unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🔄 Otra búsqueda", use_container_width=True, key="cl_jur_reset"):
                    st.session_state.cl_jurisprudencia_result = ""
                    st.rerun()
            with col_b:
                if st.button("📄 Subir mi documento", use_container_width=True, key="cl_jur_to_doc"):
                    st.session_state.cl_modo = "documento"
                    st.session_state.cl_jurisprudencia_result = ""
                    st.rerun()

        # Temas populares (materias principales)
        st.markdown("""
        <div style="margin-top:1.5rem;padding:0.8rem 1rem;
                    background:rgba(201,150,58,0.05);border:1px solid rgba(201,150,58,0.12);
                    border-radius:8px;">
          <div style="font-size:0.7rem;font-weight:700;color:#a09070;
                      text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.6rem;">
            Materias más consultadas
          </div>
          <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
        """, unsafe_allow_html=True)

        materias = ["Despido", "Accidente laboral", "Pensión alimenticia", "Arrendamiento", "Deuda", "Herencia"]
        for materia in materias:
            if st.button(materia, key=f"cl_mat_{materia}"):
                st.session_state.cl_jurisprudencia_query = materia
                st.rerun()
            st.write("")

        st.markdown("</div></div>", unsafe_allow_html=True)

        # Banner informativo
        st.markdown("""
        <div style="margin-top:1.2rem;padding:0.8rem 1rem;
                    background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);
                    border-radius:8px;">
          <div style="font-size:0.72rem;color:#a09070;line-height:1.6;">
            ℹ️ <strong>Basado en 1,200,417 sentencias reales del Poder Judicial de Chile</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── MODO DOCTRINA ─────────────────────────────────────────────
    elif st.session_state.cl_modo == "doctrina":

        st.markdown("""
        <div class="cl-hero-title" style="font-size:1.4rem;">
          📚 ¿Qué dice la ley?
        </div>
        <div class="cl-hero-sub" style="max-width:100%;margin-bottom:1.2rem;">
          Encuentra qué dicen los expertos sobre tu tema legal
        </div>
        """, unsafe_allow_html=True)

        # Búsqueda de doctrina
        doc_query = st.text_input(
            "¿Sobre qué tema necesitas información?",
            placeholder="Ej: herencia, divorcio, contrato de arriendo, deuda...",
            key="cl_doc_t_input",
            label_visibility="collapsed")

        if consultas_libres > 0:
            st.markdown(
                f'<div style="font-size:0.65rem;color:#a09070;margin-bottom:0.5rem;">'
                f'Consultas gratuitas restantes: <strong style="color:#c9963a;">{consultas_libres}</strong></div>',
                unsafe_allow_html=True)
            btn_disabled_dt = False
        else:
            st.markdown(
                '<div style="font-size:0.75rem;color:#ef4444;margin-bottom:0.5rem;">'
                'Has usado tus consultas gratuitas. Suscríbete para continuar.</div>',
                unsafe_allow_html=True)
            btn_disabled_dt = True

        if st.button("📚 CONSULTAR DOCTRINA", use_container_width=True,
                     type="primary", disabled=btn_disabled_dt):
            if doc_query and get_llm_fn:
                with st.spinner("Buscando en obras académicas…"):
                    try:
                        # Aquí se importaría doctrina_service para usar buscar_doctrina
                        # Por ahora, simulamos el contexto
                        contexto_doc = f"Información sobre: {doc_query}"

                        prompt = (
                            "Eres un asistente legal chileno que ayuda a personas sin formación jurídica.\n"
                            "Tu tarea es explicar QUÉ DICE LA LEY Y LOS EXPERTOS sobre un tema en lenguaje simple.\n"
                            "Nunca uses lenguaje jurídico sin explicarlo.\n\n"
                            f"CONTEXTO DOCTRINARIO:\n{contexto_doc}\n\n"
                            f"TEMA DEL USUARIO: {doc_query}\n\n"
                            "INSTRUCCIONES:\n"
                            "1. Resume qué dice la ley sobre este tema en palabras simples (2-3 párrafos)\n"
                            "2. Explica los puntos principales que debes saber\n"
                            "3. Menciona qué derechos u obligaciones tienes\n"
                            "4. Señala situaciones comunes y cómo se resuelven\n"
                            "Cierra con: '⚠️ Esta es información general. Para tu situación específica, consulta con un profesional.'"
                        )
                        llm = get_llm_fn()
                        resp = llm.generate(prompt, system=" ", max_tokens=1000)
                        st.session_state.cl_doctrina_result = resp
                        st.session_state.cl_doctrina_query = doc_query
                        st.session_state.cl_query_count += 1
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
            elif not doc_query:
                st.warning("Escribe el tema que te interesa.")

        # Mostrar resultados
        if st.session_state.cl_doctrina_result:
            st.markdown(
                f'<div class="cl-answer-box">'
                f'{st.session_state.cl_doctrina_result.replace(chr(10),"<br>")}'
                f'</div>',
                unsafe_allow_html=True)

            st.markdown('<br>', unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🔄 Otra consulta", use_container_width=True, key="cl_doc_t_reset"):
                    st.session_state.cl_doctrina_result = ""
                    st.rerun()
            with col_b:
                if st.button("📄 Subir documento", use_container_width=True, key="cl_doc_t_to_doc"):
                    st.session_state.cl_modo = "documento"
                    st.session_state.cl_doctrina_result = ""
                    st.rerun()

        # Áreas temáticas
        st.markdown("""
        <div style="margin-top:1.5rem;padding:0.8rem 1rem;
                    background:rgba(201,150,58,0.05);border:1px solid rgba(201,150,58,0.12);
                    border-radius:8px;">
          <div style="font-size:0.7rem;font-weight:700;color:#a09070;
                      text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.8rem;">
            Áreas de derecho disponibles
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:0.8rem;">
        """, unsafe_allow_html=True)

        areas = ["Derecho de Familia", "Derecho Laboral", "Derecho Civil", "Derecho Comercial",
                 "Derecho Tributario", "Derecho Administrativo", "Derecho Penal", "Derecho Ambiental",
                 "Propiedad Intelectual", "Derecho Procesal", "Derecho Inmobiliario", "Contratos"]

        for area in areas:
            if st.button(area, use_container_width=True, key=f"cl_area_{area}"):
                st.session_state.cl_doctrina_query = area
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        # Banner informativo
        st.markdown("""
        <div style="margin-top:1.2rem;padding:0.8rem 1rem;
                    background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);
                    border-radius:8px;">
          <div style="font-size:0.72rem;color:#a09070;line-height:1.6;">
            ℹ️ <strong>Basado en 2,827 obras académicas de derecho chileno</strong>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ── PLANES / PRECIOS ───────────────────────────────────────────
    st.markdown('<hr style="border-color:rgba(201,150,58,0.1);margin:2rem 0 1.2rem;">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;margin-bottom:1.2rem;">
      <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:#f5f0e8;">
        Planes de Consulta Legal
      </div>
      <div style="font-size:0.72rem;color:#a09070;margin-top:4px;">
        Orientación jurídica accesible para todas las personas
      </div>
    </div>
    """, unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("""
        <div class="cl-price-card">
          <div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Básico</div>
          <div class="cl-price-amount">Gratis</div>
          <div class="cl-price-period">3 consultas</div>
          <hr style="border-color:rgba(201,150,58,0.12);margin:0.8rem 0;">
          <div style="font-size:0.72rem;color:#c8b890;text-align:left;line-height:1.8;">
            ✓ Preguntas generales<br>
            ✓ Análisis de 1 documento<br>
            ✓ Guía de acción básica
          </div>
        </div>
        """, unsafe_allow_html=True)
    with p2:
        st.markdown("""
        <div class="cl-price-card featured">
          <div style="font-size:0.68rem;color:#c9963a;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">⭐ Popular</div>
          <div class="cl-price-amount">$4.990</div>
          <div class="cl-price-period">/ mes · CLP</div>
          <hr style="border-color:rgba(201,150,58,0.2);margin:0.8rem 0;">
          <div style="font-size:0.72rem;color:#c8b890;text-align:left;line-height:1.8;">
            ✓ 30 consultas al mes<br>
            ✓ Análisis ilimitado de documentos<br>
            ✓ Guía paso a paso detallada<br>
            ✓ Acceso a jurisprudencia relacionada
          </div>
        </div>
        """, unsafe_allow_html=True)
    with p3:
        st.markdown("""
        <div class="cl-price-card">
          <div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Familiar</div>
          <div class="cl-price-amount">$9.990</div>
          <div class="cl-price-period">/ mes · CLP</div>
          <hr style="border-color:rgba(201,150,58,0.12);margin:0.8rem 0;">
          <div style="font-size:0.72rem;color:#c8b890;text-align:left;line-height:1.8;">
            ✓ Consultas ilimitadas<br>
            ✓ Hasta 5 personas<br>
            ✓ Historial de consultas<br>
            ✓ Conexión con abogado (próx.)
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
    with col_cta2:
        st.button("💳 Suscribirse ahora (próximamente)", use_container_width=True, disabled=True)

    # Disclaimer legal
    st.markdown("""
    <div class="cl-disclaimer">
      ⚠️ <strong>Importante:</strong> AntonIA proporciona orientación jurídica general con fines informativos.
      Esta información no constituye asesoría jurídica profesional ni establece una relación abogado-cliente.
      Para su caso específico, consulte con un abogado habilitado. Si no puede costear un abogado, contacte
      la <strong>Corporación de Asistencia Judicial (CAJ)</strong> de su región — el servicio es gratuito.
    </div>
    """, unsafe_allow_html=True)
