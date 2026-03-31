"""
profesor_module.py — AntonIA · Área Profesores
Herramientas para la gestión académica docente.

Módulos:
  · Evaluaciones   — revisión y retroalimentación con IA
  · Nueva Eval.    — creación de evaluaciones por IA
  · Investigación  — asistente de investigación jurídica
  · Asistencia     — control de asistencia por curso
  · Observaciones  — notas por alumno
  · Recursos       — materiales de preparación de clase
"""

import streamlit as st
import json, datetime, random

_GOLD  = "#c9963a"
_DARK  = "#141210"
_CARD  = "#1e1b16"
_MUTED = "#a09070"
_WHITE = "#f5f0e8"
_GREEN = "#22c55e"
_RED   = "#ef4444"

_CSS = """
<style>
.prof-header {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.6rem; font-weight: 700;
    color: #f5f0e8; margin-bottom: 0.2rem;
}
.prof-sub {
    font-size: 0.92rem; color: #a09070;
    margin-bottom: 1.2rem; letter-spacing: 0.02em;
}
.prof-card {
    background: #1e1b16;
    border: 1px solid rgba(201,150,58,0.18);
    border-radius: 8px; padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    font-size: 0.9rem;
}
.prof-alumno-btn {
    padding: 0.4rem 0.8rem; border-radius: 20px;
    font-size: 0.78rem; cursor: pointer;
    background: rgba(201,150,58,0.1);
    border: 1px solid rgba(201,150,58,0.2);
    color: #c9963a; display: inline-block;
    margin: 2px;
}
.nota-alta  { color: #22c55e; font-weight: 700; font-size: 1rem; }
.nota-media { color: #fbbf24; font-weight: 700; font-size: 1rem; }
.nota-baja  { color: #ef4444; font-weight: 700; font-size: 1rem; }
/* Textos de label generales */
div[data-testid="stMarkdownContainer"] p { font-size: 0.95rem !important; }
div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stTextArea"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSlider"] label { font-size: 0.9rem !important; }
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea { font-size: 0.92rem !important; }
</style>
"""

def _init():
    defaults = {
        "prof_tab":     "evaluaciones",
        # Cursos
        "prof_cursos":  ["Civil I — Personas", "Civil III — Obligaciones", "Derecho Penal I"],
        "prof_curso_sel": None,
        # Nómina de alumnos (por curso)
        "prof_nominas": {},   # {curso: [{"nombre":"...", "asistencias": [...], "notas": [...], "obs": "..."}]}
        # Evaluaciones creadas
        "prof_evals":   [],
        # Resultados de IA
        "prof_eval_result":      "",
        "prof_rubrica_result":   "",
        "prof_investigacion_result": "",
        "prof_recursos_result":  "",
        # Libro de Notas: {curso: [{nombre, notas:[{eval,ponderacion,nota}], promedio}]}
        "prof_libro_notas": {},
        # Banco de Preguntas: [{pregunta, alternativas, respuesta_correcta, ramo, dificultad}]
        "prof_banco": [],
        "prof_banco_gen_result": "",
        # Examen Oral
        "prof_oral_result": "",
        "prof_oral_qa": [],   # [{"pregunta": str, "respuesta_esperada": str, "tiempo": str}]
        # Planificador de Clase
        "prof_plan_result": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def _get_nomina(curso: str) -> list:
    nom = st.session_state.prof_nominas
    if curso not in nom:
        nom[curso] = []
    return nom[curso]

def _nota_class(n: float) -> str:
    if n >= 5.0:  return "nota-alta"
    if n >= 4.0:  return "nota-media"
    return "nota-baja"


# ═══════════════════════════════════════════════════════════════════
def render_profesor(get_llm_fn=None):
    """Renderiza el área completa de Profesores."""
    _init()
    st.markdown(_CSS, unsafe_allow_html=True)

    TABS = [
        ("📝", "evaluaciones",   "Evalúa"),
        ("✏️", "nueva_eval",     "Crea Eval."),
        ("🎙️", "oral",          "Examen Oral"),
        ("🗓️", "plan_clase",    "Plan de Clase"),
        ("📊", "notas",          "Libro Notas"),
        ("🗂",  "banco",         "Banco Preg."),
        ("📈", "rendimiento",    "Rendimiento"),
        ("🔬", "investigacion",  "Investigación"),
        ("📋", "asistencia",     "Asistencia"),
        ("💬", "observaciones",  "Obs. Alumnos"),
        ("📚", "recursos",       "Recursos"),
    ]

    tab_cols = st.columns(len(TABS))
    for col, (icon, tid, label) in zip(tab_cols, TABS):
        active = st.session_state.prof_tab == tid
        with col:
            if active:
                st.markdown(
                    f'<div style="text-align:center;padding:0.4rem 0;'
                    f'border-bottom:2px solid {_GOLD};color:{_GOLD};'
                    f'font-size:0.72rem;font-weight:700;text-transform:uppercase;">'
                    f'{icon} {label}</div>',
                    unsafe_allow_html=True)
            else:
                if st.button(f"{icon} {label}", key=f"prof_t_{tid}",
                             use_container_width=True):
                    st.session_state.prof_tab = tid
                    st.rerun()

    st.markdown('<hr style="border-color:rgba(201,150,58,0.15);margin:0.8rem 0 1.2rem;">', unsafe_allow_html=True)

    tab = st.session_state.prof_tab

    # ── EVALUACIONES ───────────────────────────────────────────────
    if tab == "evaluaciones":
        st.markdown('<div class="prof-header">Revisión de Evaluaciones</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Retroalimentación y corrección asistida por IA</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            alumno_eval  = st.text_input("Nombre del alumno", key="prof_ev_alumno")
            ramo_eval    = st.selectbox("Ramo", [
                "Civil I — Personas y Acto Jurídico",
                "Civil II — Bienes",
                "Civil III — Obligaciones",
                "Civil IV — Familia",
                "Civil V — Sucesorio",
                "Penal", "Procesal", "Constitucional",
                "Laboral", "Comercial", "Internacional",
            ], key="prof_ev_ramo")
            tipo_eval    = st.selectbox("Tipo de evaluación", [
                "Prueba escrita (desarrollo)",
                "Caso práctico",
                "Ensayo",
                "Informe de lectura",
                "Examen oral (transcripción)",
                "Control de lectura",
            ], key="prof_ev_tipo")
            pauta        = st.text_area("Pauta / criterios de evaluación",
                height=80,
                placeholder="Ej: 4 puntos por identificar correctamente los elementos del acto jurídico; 3 puntos por análisis de requisitos de existencia; 3 puntos por aplicación al caso concreto.",
                key="prof_ev_pauta")
            respuesta    = st.text_area("Respuesta del alumno",
                height=180,
                placeholder="Pega aquí la respuesta del alumno…",
                key="prof_ev_respuesta")
            nota_max     = st.number_input("Nota máxima", value=7.0, step=0.5, key="prof_ev_max")

            if st.button("🤖 Revisar con IA", use_container_width=True, type="primary"):
                if respuesta and get_llm_fn:
                    prompt = (
                        f"Eres un profesor de Derecho chileno evaluando una prueba escrita.\n"
                        f"Ramo: {ramo_eval}\n"
                        f"Tipo: {tipo_eval}\n"
                        f"Pauta: {pauta or 'Evalúa calidad jurídica, uso correcto de terminología y coherencia argumentativa.'}\n"
                        f"Nota máxima: {nota_max}\n\n"
                        f"RESPUESTA DEL ALUMNO:\n{respuesta}\n\n"
                        f"INSTRUCCIONES DE REVISIÓN:\n"
                        f"1. Asigna una nota en escala 1-{nota_max}\n"
                        f"2. Lista los aciertos (qué hizo bien)\n"
                        f"3. Lista los errores o aspectos a mejorar\n"
                        f"4. Señala errores jurídicos graves si los hay\n"
                        f"5. Escribe comentarios de retroalimentación constructiva (2-3 párrafos)\n"
                        f"6. Sugiere bibliografía para reforzar los puntos débiles\n"
                        f"Usa nomenclatura jurídica chilena."
                    )
                    with st.spinner("Revisando con IA…"):
                        try:
                            llm = get_llm_fn()
                            resp = llm.generate(prompt, system=" ", max_tokens=1200)
                            st.session_state.prof_eval_result = resp
                            # Guardar en nómina si hay nombre
                            if alumno_eval and st.session_state.prof_curso_sel:
                                nomina = _get_nomina(st.session_state.prof_curso_sel)
                                for al in nomina:
                                    if al["nombre"].lower() == alumno_eval.lower():
                                        al["notas"].append({
                                            "eval": tipo_eval,
                                            "fecha": datetime.date.today().isoformat(),
                                            "retroalimentacion": resp[:200],
                                        })
                                        break
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Pega la respuesta del alumno.")

        with col2:
            if st.session_state.prof_eval_result:
                st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Retroalimentación generada</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="prof-card" style="font-size:0.78rem;color:#e8d8b8;line-height:1.65;max-height:500px;overflow-y:auto;">'
                    f'{st.session_state.prof_eval_result.replace(chr(10),"<br>")}</div>',
                    unsafe_allow_html=True)
                if alumno_eval:
                    st.caption(f"📎 Retroalimentación para: {alumno_eval}")
            else:
                st.markdown(
                    '<div style="height:300px;display:flex;align-items:center;justify-content:center;'
                    'color:#a09070;font-size:0.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                    '📝<br>La retroalimentación de IA<br>aparecerá aquí</div>',
                    unsafe_allow_html=True)

    # ── NUEVA EVALUACIÓN ───────────────────────────────────────────
    elif tab == "nueva_eval":
        st.markdown('<div class="prof-header">Crear Evaluación</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Genera evaluaciones con IA adaptadas al programa</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            ramo_ne  = st.selectbox("Ramo", [
                "Civil I — Personas y Acto Jurídico",
                "Civil II — Bienes y Derechos Reales",
                "Civil III — Obligaciones y Contratos",
                "Civil IV — Derecho de Familia",
                "Civil V — Derecho Sucesorio",
                "Derecho Penal",
                "Derecho Procesal",
                "Derecho Constitucional y DDPP",
                "Derecho del Trabajo",
                "Derecho Comercial",
            ], key="prof_ne_ramo")
            tipo_ne  = st.selectbox("Tipo de evaluación", [
                "Control de lectura (alternativas)",
                "Caso práctico",
                "Prueba de desarrollo (3 preguntas)",
                "Examen final (5 preguntas)",
                "Ejercicio de análisis jurisprudencial",
                "Ensayo (con instrucciones y pauta)",
            ], key="prof_ne_tipo")
            nivel    = st.selectbox("Nivel", ["1° año","2° año","3° año","4° año","5° año / Egresados"], key="prof_ne_nivel")
            temas    = st.text_area("Temas / unidades a evaluar",
                height=80,
                placeholder="Ej: Capacidad, voluntad, objeto y causa del acto jurídico. Vicios del consentimiento.",
                key="prof_ne_temas")
            dificultad = st.selectbox("Dificultad", ["Básica","Intermedia","Avanzada"], key="prof_ne_dif")
            n_preg   = st.slider("N° preguntas / ítems", 3, 20, 8, key="prof_ne_n")

            if st.button("✏️ Generar Evaluación", use_container_width=True, type="primary"):
                if temas and get_llm_fn:
                    prompt = (
                        f"Eres un profesor de {ramo_ne} en una facultad de Derecho chilena.\n"
                        f"Crea una evaluación del tipo: {tipo_ne}\n"
                        f"Nivel: {nivel}\n"
                        f"Temas: {temas}\n"
                        f"Dificultad: {dificultad}\n"
                        f"N° de ítems: {n_preg}\n\n"
                        f"INSTRUCCIONES:\n"
                        f"- Basa las preguntas en el Derecho chileno vigente\n"
                        f"- Usa casos prácticos realistas cuando corresponda\n"
                        f"- Si es de alternativas, incluye 4 opciones por pregunta con la respuesta correcta indicada\n"
                        f"- Si es de desarrollo, incluye una pauta de corrección\n"
                        f"- Varía la dificultad dentro del nivel solicitado\n"
                        f"- Al final incluye la pauta completa con puntajes"
                    )
                    with st.spinner("Creando evaluación…"):
                        try:
                            llm = get_llm_fn()
                            resp = llm.generate(prompt, system=" ", max_tokens=2000)
                            st.session_state.prof_rubrica_result = resp
                            st.session_state.prof_evals.append({
                                "ramo":    ramo_ne,
                                "tipo":    tipo_ne,
                                "temas":   temas[:80],
                                "fecha":   datetime.date.today().isoformat(),
                                "nivel":   nivel,
                            })
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Indica los temas a evaluar.")

        with col2:
            if st.session_state.prof_rubrica_result:
                st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Evaluación generada</div>', unsafe_allow_html=True)
                eval_edit = st.text_area("Edita y copia:",
                    value=st.session_state.prof_rubrica_result,
                    height=440, key="prof_eval_edit")
                st.caption("Revisa y ajusta antes de usar con alumnos.")
            else:
                # ── Panel de casos del banco según ramo seleccionado ─────────
                _ramo_a_rama = {
                    "Civil I — Personas y Acto Jurídico":   ("civil", ["Personas y Familia"]),
                    "Civil II — Bienes y Derechos Reales":  ("civil", ["Bienes y Derechos Reales"]),
                    "Civil III — Obligaciones y Contratos": ("civil", ["Obligaciones y Contratos","Contratos y Cuasicontratos"]),
                    "Civil IV — Derecho de Familia":        ("civil", ["Personas y Familia"]),
                    "Civil V — Derecho Sucesorio":          ("civil", ["Sucesiones"]),
                    "Derecho Penal":                        ("penal", None),
                    "Derecho Procesal":                     ("procesal", None),
                    "Derecho Constitucional y DDPP":        ("constitucional", None),
                    "Derecho del Trabajo":                  ("laboral", None),
                    "Derecho Comercial":                    ("civil", ["Contratos y Cuasicontratos"]),
                }
                try:
                    from casos_banco import CASOS as _CB
                    _rama_info = _ramo_a_rama.get(ramo_ne, ("civil", None))
                    _rama_key, _subtemas = _rama_info
                    if _subtemas:
                        _casos_ramo = [c for c in _CB if c["rama"] == _rama_key and c["subtema"] in _subtemas]
                        if not _casos_ramo:
                            _casos_ramo = [c for c in _CB if c["rama"] == _rama_key]
                    else:
                        _casos_ramo = [c for c in _CB if c["rama"] == _rama_key]

                    if _casos_ramo:
                        st.markdown(
                            f'<div style="font-size:0.68rem;color:#c9963a;text-transform:uppercase;'
                            f'letter-spacing:0.06em;margin-bottom:0.6rem;">'
                            f'📂 Casos del banco · {ramo_ne.split("—")[-1].strip() if "—" in ramo_ne else ramo_ne}'
                            f' ({len(_casos_ramo)} disponibles)</div>', unsafe_allow_html=True)

                        _dif_color = {"básico":"#2e9055","intermedio":"#c9963a","avanzado":"#a83232"}
                        for _c in _casos_ramo[:8]:
                            _dc = _dif_color.get(_c["dificultad"], "#888")
                            with st.expander(f"#{_c['id']} · {_c['titulo']}", expanded=False):
                                st.markdown(
                                    f'<span style="font-size:0.67rem;color:{_dc};font-weight:700;">'
                                    f'{_c["dificultad"]}</span> &nbsp; '
                                    f'<span style="font-size:0.67rem;color:#9a8a6a;">{_c["subtema"]}</span>',
                                    unsafe_allow_html=True)
                                st.markdown(f"**Hechos:** {_c['hechos']}")
                                st.markdown(
                                    f'<div style="font-style:italic;background:rgba(201,150,58,0.07);'
                                    f'padding:0.4rem 0.6rem;border-radius:4px;font-size:0.82rem;">'
                                    f'❓ {_c["pregunta"]}</div>', unsafe_allow_html=True)
                                st.markdown(f"📌 *Fundamento:* `{_c['fundamento']}`")
                                if st.button("📋 Usar como base de evaluación",
                                             key=f"ne_usar_{_c['id']}",
                                             use_container_width=True):
                                    _plantilla = (
                                        f"CASO PRÁCTICO\n\n"
                                        f"**{_c['titulo']}**\n\n"
                                        f"HECHOS:\n{_c['hechos']}\n\n"
                                        f"PREGUNTAS:\n1. {_c['pregunta']}\n"
                                        f"2. Fundamente su respuesta citando el articulado aplicable.\n"
                                        f"3. ¿Qué acción(es) procesales proceden? Señale tribunal competente.\n\n"
                                        f"PAUTA DE CORRECCIÓN:\n{_c['respuesta']}\n"
                                        f"Base normativa: {_c['fundamento']}"
                                    )
                                    st.session_state.prof_rubrica_result = _plantilla
                                    st.rerun()

                        if len(_casos_ramo) > 8:
                            st.markdown(
                                f'<div style="font-size:0.72rem;color:#9a8a6a;margin-top:0.3rem;">'
                                f'Mostrando 8 de {len(_casos_ramo)}. Filtra por dificultad en el Banco de Preguntas.</div>',
                                unsafe_allow_html=True)
                    else:
                        st.markdown(
                            '<div style="height:300px;display:flex;align-items:center;justify-content:center;'
                            'color:#a09070;font-size:0.82rem;text-align:center;'
                            'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                            '✏️<br>La evaluación generada<br>aparecerá aquí</div>',
                            unsafe_allow_html=True)
                except ImportError:
                    st.markdown(
                        '<div style="height:300px;display:flex;align-items:center;justify-content:center;'
                        'color:#a09070;font-size:0.82rem;text-align:center;'
                        'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                        '✏️<br>La evaluación generada<br>aparecerá aquí</div>',
                        unsafe_allow_html=True)

        # Historial de evaluaciones creadas
        if st.session_state.prof_evals:
            st.markdown('<hr style="border-color:rgba(255,255,255,0.07);margin:1rem 0;">', unsafe_allow_html=True)
            st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.4rem;">Evaluaciones creadas esta sesión</div>', unsafe_allow_html=True)
            for ev in reversed(st.session_state.prof_evals):
                st.markdown(f'<div style="font-size:0.73rem;color:#c8b890;padding:0.2rem 0;">• {ev["ramo"]} — {ev["tipo"]} ({ev["nivel"]}) · {ev["fecha"]}</div>', unsafe_allow_html=True)

    # ── INVESTIGACIÓN ──────────────────────────────────────────────
    elif tab == "investigacion":
        st.markdown('<div class="prof-header">Asistente de Investigación</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Apoyo para preparación de clases e investigación jurídica</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            tipo_inv = st.selectbox("¿Qué necesitas?", [
                "Resumen del estado del arte (doctrina y jurisprudencia)",
                "Bibliografía recomendada sobre un tema",
                "Comparativo Derecho chileno vs. comparado",
                "Esquema de clase (con puntos clave)",
                "Puntos de debate / casos polémicos",
                "Historia legislativa de una norma",
                "Análisis de un fallo reciente",
            ], key="prof_inv_tipo")
            tema_inv = st.text_area("Tema de investigación",
                height=100,
                placeholder="Ej: La buena fe objetiva en los contratos según el CC chileno y su recepción jurisprudencial reciente.",
                key="prof_inv_tema")
            prof_inv = st.text_input("Enfoque o nivel de profundidad", placeholder="Para 3° año, énfasis en jurisprudencia reciente", key="prof_inv_prof")

            if st.button("🔬 Investigar con IA", use_container_width=True, type="primary"):
                if tema_inv and get_llm_fn:
                    prompt = (
                        f"Eres un investigador y profesor de Derecho chileno.\n"
                        f"Tarea: {tipo_inv}\n"
                        f"Tema: {tema_inv}\n"
                        f"Enfoque: {prof_inv or 'nivel universitario avanzado'}\n\n"
                        f"Usa fuentes del Derecho chileno (CC, CPP, CPP, CCo, leyes especiales, jurisprudencia CS). "
                        f"Cita autores chilenos relevantes. Sé preciso y académico. "
                        f"Si mencionas jurisprudencia, indica tribunal, año y número si es posible."
                    )
                    with st.spinner("Investigando…"):
                        try:
                            llm = get_llm_fn()
                            resp = llm.generate(prompt, system=" ", max_tokens=1800)
                            st.session_state.prof_investigacion_result = resp
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Escribe el tema de investigación.")

        with col2:
            if st.session_state.prof_investigacion_result:
                st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Resultado</div>', unsafe_allow_html=True)
                inv_edit = st.text_area("",
                    value=st.session_state.prof_investigacion_result,
                    height=450, key="prof_inv_edit", label_visibility="collapsed")
                st.caption("⚠️ Verifica las citas y referencias antes de publicar.")
            else:
                st.markdown(
                    '<div style="height:350px;display:flex;align-items:center;justify-content:center;'
                    'color:#a09070;font-size:0.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                    '🔬<br>El resultado de la investigación<br>aparecerá aquí</div>',
                    unsafe_allow_html=True)

    # ── ASISTENCIA ─────────────────────────────────────────────────
    elif tab == "asistencia":
        st.markdown('<div class="prof-header">Control de Asistencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Registro por clase y alumno</div>', unsafe_allow_html=True)

        # Selección de curso
        col_curso, col_fecha = st.columns([2, 1])
        with col_curso:
            curso_sel = st.selectbox("Curso", st.session_state.prof_cursos, key="prof_asis_curso")
            st.session_state.prof_curso_sel = curso_sel
        with col_fecha:
            fecha_clase = st.date_input("Fecha de clase", value=datetime.date.today(), key="prof_asis_fecha")

        nomina = _get_nomina(curso_sel)

        # Agregar alumno
        col_add, _ = st.columns([2, 2])
        with col_add:
            nuevo_alumno = st.text_input("Agregar alumno a la nómina", key="prof_nuevo_alumno")
            if st.button("+ Agregar", key="prof_btn_add_alumno"):
                if nuevo_alumno and not any(a["nombre"].lower() == nuevo_alumno.lower() for a in nomina):
                    nomina.append({"nombre": nuevo_alumno, "asistencias": [], "notas": [], "obs": ""})
                    st.session_state.prof_nominas[curso_sel] = nomina
                    st.rerun()

        if not nomina:
            st.info("Agrega alumnos a la nómina del curso.")
        else:
            st.markdown(f'<div style="font-size:0.68rem;color:#a09070;margin-bottom:0.6rem;">Clase: {fecha_clase.isoformat()} · {len(nomina)} alumnos</div>', unsafe_allow_html=True)

            fecha_str = fecha_clase.isoformat()
            col_names, col_asis, col_obs = st.columns([3, 1, 2])
            col_names.markdown('<div style="font-size:0.65rem;color:#a09070;font-weight:700;text-transform:uppercase;">Alumno</div>', unsafe_allow_html=True)
            col_asis.markdown('<div style="font-size:0.65rem;color:#a09070;font-weight:700;text-transform:uppercase;">Asiste</div>', unsafe_allow_html=True)
            col_obs.markdown('<div style="font-size:0.65rem;color:#a09070;font-weight:700;text-transform:uppercase;">Nota rápida</div>', unsafe_allow_html=True)

            for i, alumno in enumerate(nomina):
                col_n, col_a, col_o = st.columns([3, 1, 2])
                with col_n:
                    pct = 0
                    if alumno["asistencias"]:
                        pct = int(sum(1 for a in alumno["asistencias"] if a["presente"]) / len(alumno["asistencias"]) * 100)
                    color_pct = _GREEN if pct >= 75 else (_MUTED if pct >= 50 else _RED)
                    st.markdown(
                        f'<div style="font-size:0.78rem;color:#f5f0e8;padding:0.4rem 0;">'
                        f'{alumno["nombre"]}'
                        f'<span style="font-size:0.62rem;color:{color_pct};margin-left:8px;">{pct}% asis.</span>'
                        f'</div>', unsafe_allow_html=True)
                with col_a:
                    already = next((a for a in alumno["asistencias"] if a["fecha"] == fecha_str), None)
                    val = already["presente"] if already else True
                    new_val = st.checkbox("", value=val, key=f"asis_{i}_{fecha_str}")
                    if already:
                        already["presente"] = new_val
                    else:
                        alumno["asistencias"].append({"fecha": fecha_str, "presente": new_val})
                with col_o:
                    nota_r = st.text_input("", key=f"obs_r_{i}", label_visibility="collapsed",
                                           placeholder="observación…")

            total_presentes = sum(1 for a in nomina if any(
                x["fecha"] == fecha_str and x["presente"]
                for x in a["asistencias"]))
            st.markdown(
                f'<div style="font-size:0.7rem;color:#a09070;margin-top:0.8rem;">'
                f'Presentes: {total_presentes}/{len(nomina)}</div>',
                unsafe_allow_html=True)

    # ── OBSERVACIONES ──────────────────────────────────────────────
    elif tab == "observaciones":
        st.markdown('<div class="prof-header">Observaciones por Alumno</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Seguimiento individual del progreso académico</div>', unsafe_allow_html=True)

        curso_sel_obs = st.selectbox("Curso", st.session_state.prof_cursos, key="prof_obs_curso")
        nomina = _get_nomina(curso_sel_obs)

        if not nomina:
            st.info(f"No hay alumnos en {curso_sel_obs}. Agrégatelos en la pestaña **Asistencia**.")
        else:
            alumno_sel = st.selectbox("Alumno", [a["nombre"] for a in nomina], key="prof_obs_alumno_sel")
            alumno_data = next((a for a in nomina if a["nombre"] == alumno_sel), None)

            if alumno_data:
                col1, col2 = st.columns([1, 1.3])
                with col1:
                    # Estadísticas
                    asis = alumno_data["asistencias"]
                    if asis:
                        pct = int(sum(1 for a in asis if a["presente"]) / len(asis) * 100)
                    else:
                        pct = 0
                    color_pct = _GREEN if pct >= 75 else (_MUTED if pct >= 50 else _RED)

                    st.markdown(f"""
                    <div class="prof-card">
                      <div style="font-size:0.7rem;color:#a09070;font-weight:700;text-transform:uppercase;margin-bottom:0.5rem;">Resumen</div>
                      <div style="font-size:0.82rem;color:#f5f0e8;">{alumno_sel}</div>
                      <div style="font-size:0.72rem;color:{color_pct};margin-top:4px;">Asistencia: {pct}% ({len(asis)} clases)</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Observaciones
                    obs_text = st.text_area("Observaciones del profesor",
                        value=alumno_data.get("obs", ""),
                        height=180,
                        placeholder="Ej: Muestra buena comprensión de la teoría del acto jurídico. Debe trabajar la redacción jurídica. Recomendar tutorías.",
                        key=f"obs_text_{alumno_sel}")

                    if st.button("💾 Guardar observaciones", use_container_width=True, type="primary"):
                        idx = next(i for i, a in enumerate(nomina) if a["nombre"] == alumno_sel)
                        st.session_state.prof_nominas[curso_sel_obs][idx]["obs"] = obs_text
                        st.success("✓ Guardado")

                    if st.button("🤖 Generar retroalimentación personalizada", use_container_width=True):
                        if obs_text and get_llm_fn:
                            prompt = (
                                f"Eres un profesor de Derecho chileno. "
                                f"Basándote en estas observaciones sobre {alumno_sel}:\n"
                                f"{obs_text}\n\n"
                                f"Redacta un comentario de retroalimentación constructiva y motivador (3-4 párrafos) "
                                f"que puedas compartir con el alumno. "
                                f"Destaca fortalezas, señala áreas de mejora con estrategias concretas, "
                                f"y sugiere recursos bibliográficos específicos."
                            )
                            with st.spinner("Generando retroalimentación…"):
                                try:
                                    llm = get_llm_fn()
                                    resp = llm.generate(prompt, system=" ", max_tokens=600)
                                    st.session_state[f"retro_{alumno_sel}"] = resp
                                except Exception as e:
                                    st.error(f"Error: {e}")

                with col2:
                    retro_key = f"retro_{alumno_sel}"
                    if retro_key in st.session_state and st.session_state[retro_key]:
                        st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Retroalimentación para el alumno</div>', unsafe_allow_html=True)
                        st.markdown(
                            f'<div class="prof-card" style="font-size:0.78rem;color:#e8d8b8;line-height:1.65;">'
                            f'{st.session_state[retro_key].replace(chr(10),"<br>")}</div>',
                            unsafe_allow_html=True)
                    elif alumno_data.get("notas"):
                        st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Evaluaciones registradas</div>', unsafe_allow_html=True)
                        for n in reversed(alumno_data["notas"]):
                            st.markdown(f"""
                            <div class="prof-card" style="padding:0.55rem 0.9rem;">
                              <div style="font-size:0.73rem;color:#c9963a;">{n.get('eval','—')}</div>
                              <div style="font-size:0.68rem;color:#a09070;">{n.get('fecha','')}</div>
                              <div style="font-size:0.72rem;color:#e8d8b8;margin-top:4px;">{n.get('retroalimentacion','')}</div>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown(
                            '<div style="height:200px;display:flex;align-items:center;justify-content:center;'
                            'color:#a09070;font-size:0.82rem;text-align:center;'
                            'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                            '💬<br>Escribe observaciones y genera<br>retroalimentación personalizada</div>',
                            unsafe_allow_html=True)

    # ── RECURSOS ───────────────────────────────────────────────────
    elif tab == "recursos":
        st.markdown('<div class="prof-header">Recursos y Preparación de Clase</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Materiales didácticos asistidos por IA</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            tipo_rec = st.selectbox("¿Qué material necesitas?", [
                "Esquema de clase (diapositivas / pizarrón)",
                "Caso práctico para discutir en clases",
                "Preguntas socráticas (para provocar debate)",
                "Línea de tiempo histórica de la norma",
                "Comparativo internacional (3 países)",
                "Resumen ejecutivo para alumnos",
                "Ejercicios de aplicación (con soluciones)",
                "Glossario del tema",
            ], key="prof_rec_tipo")
            tema_rec = st.text_area("Tema de la clase",
                height=80,
                placeholder="Ej: Nulidad absoluta y relativa en el Código Civil chileno: diferencias, efectos y saneamiento.",
                key="prof_rec_tema")
            nivel_rec = st.selectbox("Nivel del curso", ["1° año","2° año","3° año","4° año","5° año"], key="prof_rec_nivel")
            duracion  = st.selectbox("Duración estimada de la clase", ["45 min","90 min","2 horas"], key="prof_rec_dur")

            if st.button("📚 Generar Material", use_container_width=True, type="primary"):
                if tema_rec and get_llm_fn:
                    prompt = (
                        f"Eres un profesor de Derecho chileno preparando material para una clase.\n"
                        f"Solicitud: {tipo_rec}\n"
                        f"Tema: {tema_rec}\n"
                        f"Nivel: {nivel_rec}\n"
                        f"Duración de clase: {duracion}\n\n"
                        f"Crea el material en base al Derecho chileno vigente. "
                        f"Usa lenguaje apropiado para el nivel. "
                        f"Si incluyes casos, úsalos basados en situaciones chilenas reales o plausibles. "
                        f"El material debe ser directamente usable en clase."
                    )
                    with st.spinner("Generando material…"):
                        try:
                            llm = get_llm_fn()
                            resp = llm.generate(prompt, system=" ", max_tokens=1800)
                            st.session_state.prof_recursos_result = resp
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Escribe el tema de la clase.")

        with col2:
            if st.session_state.prof_recursos_result:
                st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.5rem;">Material generado</div>', unsafe_allow_html=True)
                rec_edit = st.text_area("",
                    value=st.session_state.prof_recursos_result,
                    height=450, key="prof_rec_edit", label_visibility="collapsed")
            else:
                st.markdown(
                    '<div style="height:350px;display:flex;align-items:center;justify-content:center;'
                    'color:#a09070;font-size:0.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                    '📚<br>El material de clase<br>aparecerá aquí</div>',
                    unsafe_allow_html=True)

    # ── LIBRO DE NOTAS ──────────────────────────────────────────────
    elif tab == "notas":
        st.markdown('<div class="prof-header">📊 Libro de Notas</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Registro de calificaciones por alumno y curso · Analytics de rendimiento</div>', unsafe_allow_html=True)

        cursos_disp = st.session_state.prof_cursos
        if not cursos_disp:
            st.info("Agrega cursos en la pestaña Asistencia primero.")
        else:
            curso_n = st.selectbox("Curso", cursos_disp, key="notas_curso_sel")
            libro   = st.session_state.prof_libro_notas
            if curso_n not in libro:
                libro[curso_n] = []
            alumnos_n = libro[curso_n]

            # Agregar alumno
            with st.expander("➕ Agregar / Configurar alumno"):
                col_an, col_ag = st.columns([2,1])
                with col_an:
                    nuevo_al = st.text_input("Nombre", key="notas_nuevo_al", placeholder="Ana García López")
                with col_ag:
                    if st.button("Agregar", key="notas_add_al"):
                        if nuevo_al and nuevo_al not in [a["nombre"] for a in alumnos_n]:
                            alumnos_n.append({"nombre": nuevo_al, "notas": [], "promedio": 0.0})
                            st.rerun()

            if not alumnos_n:
                st.markdown('<div style="text-align:center;color:#a09070;padding:2rem;">Agrega alumnos para comenzar el libro de notas.</div>', unsafe_allow_html=True)
            else:
                # Tabla de notas editable
                st.markdown("#### Ingresar calificaciones")
                col_al_sel, col_ev_n, col_pond, col_nota_v, col_add_n = st.columns([2, 2, 1, 1, 1])
                with col_al_sel:
                    al_sel = st.selectbox("Alumno", [a["nombre"] for a in alumnos_n], key="notas_al_sel")
                with col_ev_n:
                    ev_nombre = st.text_input("Evaluación", placeholder="Prueba 1, Control...", key="notas_ev_nombre")
                with col_pond:
                    ev_pond = st.number_input("Ponder. %", 0, 100, 25, key="notas_pond")
                with col_nota_v:
                    nota_val = st.number_input("Nota (1-7)", 1.0, 7.0, 5.0, step=0.1, key="notas_nota")
                with col_add_n:
                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("✓", key="notas_add_nota"):
                        for a in alumnos_n:
                            if a["nombre"] == al_sel:
                                a["notas"].append({"eval": ev_nombre, "ponderacion": ev_pond, "nota": nota_val})
                                # Recalcular promedio ponderado
                                total_p = sum(n["ponderacion"] for n in a["notas"])
                                if total_p > 0:
                                    a["promedio"] = sum(n["nota"] * n["ponderacion"] for n in a["notas"]) / total_p
                                break
                        st.rerun()

                # Mostrar libro completo
                st.markdown("---")
                st.markdown("#### Resumen del curso")
                col_headers = st.columns([3, 1, 1, 1])
                col_headers[0].markdown("**Alumno**")
                col_headers[1].markdown("**Evaluaciones**")
                col_headers[2].markdown("**Promedio**")
                col_headers[3].markdown("**Estado**")

                promedios = []
                for a in alumnos_n:
                    prom = a.get("promedio", 0.0)
                    promedios.append(prom)
                    estado = "✅ Aprobado" if prom >= 4.0 else ("⚠️ En riesgo" if prom >= 3.5 else "❌ Reprobado")
                    cols = st.columns([3, 1, 1, 1])
                    cols[0].write(a["nombre"])
                    cols[1].write(len(a["notas"]))
                    nota_color = "#22c55e" if prom >= 5 else ("#fbbf24" if prom >= 4 else "#ef4444")
                    cols[2].markdown(f'<span style="font-weight:700;color:{nota_color}">{prom:.1f}</span>', unsafe_allow_html=True)
                    cols[3].write(estado)

                if promedios:
                    st.markdown("---")
                    prom_curso = sum(promedios) / len(promedios)
                    aprobados = sum(1 for p in promedios if p >= 4.0)
                    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                    col_m1.metric("Promedio del curso", f"{prom_curso:.1f}")
                    col_m2.metric("Alumnos aprobados", f"{aprobados}/{len(promedios)}")
                    col_m3.metric("Nota más alta", f"{max(promedios):.1f}")
                    col_m4.metric("Nota más baja", f"{min(promedios):.1f}")

    # ── BANCO DE PREGUNTAS ──────────────────────────────────────────
    elif tab == "banco":
        st.markdown('<div class="prof-header">🗂 Banco de Preguntas</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Crea, organiza y genera preguntas de examen con IA</div>', unsafe_allow_html=True)

        banco = st.session_state.prof_banco
        tab_b1, tab_b2, tab_b3, tab_b4 = st.tabs(["🤖 Generar con IA", "➕ Agregar manual", "📋 Ver banco", "📦 Pre-cargado"])

        with tab_b1:
            col_bgen1, col_bgen2 = st.columns([1, 1.4])
            with col_bgen1:
                ramo_banco = st.selectbox("Ramo", [
                    "Civil I — Personas", "Civil II — Bienes", "Civil III — Obligaciones",
                    "Civil IV — Familia", "Civil V — Sucesorio", "Penal", "Procesal",
                    "Constitucional", "Laboral", "Comercial",
                ], key="banco_ramo")
                tema_banco = st.text_input("Tema específico", placeholder="Ej: nulidad del acto jurídico", key="banco_tema")
                n_pregs    = st.slider("N° de preguntas", 1, 10, 5, key="banco_n")
                dif_banco  = st.select_slider("Dificultad", ["Básica", "Intermedia", "Avanzada"], value="Intermedia", key="banco_dif")
                tipo_banco = st.radio("Tipo", ["Alternativas (4 opciones)", "Verdadero/Falso", "Desarrollo breve"], key="banco_tipo", horizontal=True)
                if st.button("🤖 Generar preguntas", use_container_width=True, key="banco_gen_btn"):
                    if get_llm_fn and tema_banco:
                        llm = get_llm_fn()
                        prompt = (
                            f"Eres profesor de Derecho chileno. Genera {n_pregs} preguntas de examen.\n"
                            f"Ramo: {ramo_banco} | Tema: {tema_banco} | Dificultad: {dif_banco} | Tipo: {tipo_banco}\n\n"
                            f"Formato requerido para CADA pregunta:\n"
                            f"PREGUNTA N°X:\n[texto de la pregunta]\n"
                            f"{'A) ... B) ... C) ... D) ...' if 'Alternativas' in tipo_banco else ''}\n"
                            f"RESPUESTA CORRECTA: [respuesta]\n"
                            f"FUNDAMENTO: [artículo o norma chilena que la sustenta]\n"
                            f"---\n"
                            f"Genera preguntas rigurosas, con terminología jurídica correcta, basadas en el Código Civil, "
                            f"CPP, CT u otras normas chilenas según corresponda."
                        )
                        with st.spinner("Generando preguntas…"):
                            try:
                                resultado = llm.generate(prompt, system=" ", max_tokens=1500)
                                st.session_state.prof_banco_gen_result = resultado
                            except Exception as e:
                                st.error(f"Error: {e}")
            with col_bgen2:
                if st.session_state.prof_banco_gen_result:
                    st.markdown('<div style="font-size:0.68rem;color:#a09070;margin-bottom:0.4rem;">Preguntas generadas</div>', unsafe_allow_html=True)
                    st.text_area("", value=st.session_state.prof_banco_gen_result,
                                 height=420, key="banco_result_edit", label_visibility="collapsed")
                    if st.button("📥 Guardar todo en el banco", key="banco_save_all"):
                        # Parse simplificado: guardar el bloque completo como entrada
                        banco.append({
                            "ramo": ramo_banco, "tema": tema_banco,
                            "dificultad": dif_banco, "tipo": tipo_banco,
                            "contenido": st.session_state.prof_banco_gen_result,
                            "n_pregs": n_pregs,
                        })
                        st.session_state.prof_banco_gen_result = ""
                        st.success(f"✓ Guardado en el banco ({n_pregs} preguntas de {ramo_banco})")
                        st.rerun()

        with tab_b2:
            col_bm1, col_bm2 = st.columns(2)
            with col_bm1:
                ramo_man = st.selectbox("Ramo", [
                    "Civil I", "Civil II", "Civil III", "Civil IV", "Civil V",
                    "Penal", "Procesal", "Constitucional", "Laboral", "Comercial",
                ], key="banco_man_ramo")
                dif_man = st.selectbox("Dificultad", ["Básica", "Intermedia", "Avanzada"], key="banco_man_dif")
            with col_bm2:
                tipo_man = st.selectbox("Tipo", ["Alternativas", "V/F", "Desarrollo"], key="banco_man_tipo")
            pregunta_man = st.text_area("Pregunta", height=80, key="banco_man_preg")
            resp_man = st.text_input("Respuesta correcta", key="banco_man_resp")
            fund_man = st.text_input("Fundamento normativo", placeholder="Ej: Art. 1437 CC", key="banco_man_fund")
            if st.button("➕ Agregar al banco", key="banco_add_man"):
                if pregunta_man and resp_man:
                    banco.append({
                        "ramo": ramo_man, "dificultad": dif_man, "tipo": tipo_man,
                        "contenido": f"PREGUNTA:\n{pregunta_man}\nRESPUESTA: {resp_man}\nFUNDAMENTO: {fund_man}",
                        "n_pregs": 1,
                    })
                    st.success("✓ Pregunta agregada al banco")
                    st.rerun()

        with tab_b3:
            if not banco:
                st.markdown('<div style="text-align:center;color:#a09070;padding:2rem;">El banco está vacío. Genera o agrega preguntas.</div>', unsafe_allow_html=True)
            else:
                st.markdown(f"**{sum(e.get('n_pregs',1) for e in banco)} preguntas** en {len(banco)} grupos")
                for i, entrada in enumerate(banco):
                    with st.expander(f"📋 {entrada['ramo']} — {entrada.get('tema','Manual')} ({entrada.get('n_pregs',1)} preg.) · {entrada['dificultad']}"):
                        st.text(entrada["contenido"][:600] + ("..." if len(entrada["contenido"]) > 600 else ""))
                        if st.button("🗑 Eliminar", key=f"banco_del_{i}"):
                            banco.pop(i)
                            st.rerun()

        with tab_b4:
            # ── Banco Pre-cargado (evaluaciones_banco.py) ─────────────────────
            try:
                from evaluaciones_banco import EVALUACIONES, get_evaluaciones, RAMAS as EB_RAMAS, TIPOS, NIVELES
                _eb_ok = True
            except ImportError:
                _eb_ok = False

            if not _eb_ok:
                st.warning("No se encontró evaluaciones_banco.py")
            else:
                st.markdown(
                    '<div style="font-size:0.78rem;color:#6a5a3a;margin-bottom:0.8rem;">'
                    f'<strong>{len(EVALUACIONES)} preguntas pre-cargadas</strong> con fundamento en derecho chileno. '
                    'Filtra y agrega las que necesites a tu banco personal.</div>',
                    unsafe_allow_html=True)

                col_pb1, col_pb2, col_pb3 = st.columns(3)
                with col_pb1:
                    pb_rama = st.selectbox("Rama", ["Todas"] + sorted(EB_RAMAS), key="pb_rama")
                with col_pb2:
                    pb_tipo = st.selectbox("Tipo", ["Todos"] + sorted(TIPOS), key="pb_tipo")
                with col_pb3:
                    pb_nivel = st.selectbox("Nivel", ["Todos"] + NIVELES, key="pb_nivel")

                # Filtrar
                ev_filtradas = EVALUACIONES
                if pb_rama != "Todas":
                    ev_filtradas = [e for e in ev_filtradas if e["rama"] == pb_rama]
                if pb_tipo != "Todos":
                    ev_filtradas = [e for e in ev_filtradas if e["tipo"] == pb_tipo]
                if pb_nivel != "Todos":
                    ev_filtradas = [e for e in ev_filtradas if e["nivel"] == pb_nivel]

                st.markdown(
                    f'<div style="font-size:0.75rem;color:#9a8a6a;margin-bottom:0.6rem;">'
                    f'{len(ev_filtradas)} preguntas visibles</div>', unsafe_allow_html=True)

                # Mostrar en expanders con botón "Agregar al banco"
                _tipo_icon = {
                    "definicion": "📖", "verdadero_falso": "✅",
                    "caso_practico": "⚖️", "desarrollo": "📝", "comparacion": "🔄",
                }
                _nivel_label = {
                    "pregrado_basico": "Pregrado básico",
                    "pregrado_avanzado": "Pregrado avanzado",
                    "posgrado": "Postgrado",
                }
                for ev in ev_filtradas[:60]:  # limitar a 60 en pantalla para performance
                    icon = _tipo_icon.get(ev["tipo"], "❓")
                    nivel_str = _nivel_label.get(ev["nivel"], ev["nivel"])
                    with st.expander(
                        f'{icon} #{ev["id"]} · {ev["subtema"]} · {nivel_str} · {ev["puntos"]} pts',
                        expanded=False
                    ):
                        st.markdown(f'**Enunciado:** {ev["enunciado"]}')
                        st.markdown(f'**Pauta:** {ev["pauta"]}')
                        st.markdown(
                            f'`{ev["tipo"]}` · `{ev["tiempo_estimado"]}` · `{ev["puntos"]} puntos`')
                        if st.button(
                            "📥 Agregar a mi banco", key=f"pb_add_{ev['id']}",
                            help="Agrega esta pregunta a tu banco personal"
                        ):
                            # Verificar que no esté ya en el banco
                            ya_agregado = any(
                                e.get("_precargado_id") == ev["id"]
                                for e in st.session_state.prof_banco
                            )
                            if ya_agregado:
                                st.info("Ya está en tu banco.")
                            else:
                                st.session_state.prof_banco.append({
                                    "ramo": ev["rama"].capitalize(),
                                    "tema": ev["subtema"],
                                    "dificultad": nivel_str,
                                    "tipo": ev["tipo"],
                                    "contenido": (
                                        f"PREGUNTA:\n{ev['enunciado']}\n\n"
                                        f"PAUTA DE CORRECCIÓN:\n{ev['pauta']}\n\n"
                                        f"Tiempo estimado: {ev['tiempo_estimado']} · "
                                        f"{ev['puntos']} puntos"
                                    ),
                                    "n_pregs": 1,
                                    "_precargado_id": ev["id"],
                                })
                                st.success(f"✓ Pregunta #{ev['id']} agregada al banco")
                                st.rerun()

                if len(ev_filtradas) > 60:
                    st.info(f"Mostrando 60 de {len(ev_filtradas)} preguntas. Usa los filtros para ver más.")

    # ── RENDIMIENTO ─────────────────────────────────────────────────
    elif tab == "rendimiento":
        st.markdown('<div class="prof-header">📈 Dashboard de Rendimiento</div>', unsafe_allow_html=True)
        st.markdown('<div class="prof-sub">Analytics de asistencia, notas y participación por curso</div>', unsafe_allow_html=True)

        cursos_r = st.session_state.prof_cursos
        if not cursos_r:
            st.info("Configura cursos y alumnos en Asistencia y Libro de Notas primero.")
        else:
            curso_r = st.selectbox("Curso a analizar", cursos_r, key="rend_curso")
            libro_r = st.session_state.prof_libro_notas.get(curso_r, [])
            nomina_r = st.session_state.prof_nominas.get(curso_r, [])

            if not libro_r and not nomina_r:
                st.markdown('<div style="text-align:center;color:#a09070;padding:2rem;">Sin datos aún. Registra notas y asistencia primero.</div>', unsafe_allow_html=True)
            else:
                # Métricas globales
                promedios_r = [a.get("promedio", 0.0) for a in libro_r if a.get("promedio", 0.0) > 0]

                col_r1, col_r2, col_r3, col_r4 = st.columns(4)
                if promedios_r:
                    prom_gral = sum(promedios_r) / len(promedios_r)
                    aprobados_r = sum(1 for p in promedios_r if p >= 4.0)
                    col_r1.metric("Promedio del curso", f"{prom_gral:.1f}")
                    col_r2.metric("Tasa de aprobación", f"{aprobados_r}/{len(promedios_r)}")
                else:
                    col_r1.metric("Promedio del curso", "—")
                    col_r2.metric("Tasa de aprobación", "—")

                if nomina_r:
                    # Calcular asistencia promedio
                    asist_pcts = []
                    for al in nomina_r:
                        asis = al.get("asistencias", [])
                        if asis:
                            pct = sum(1 for a in asis if a) / len(asis) * 100
                            asist_pcts.append(pct)
                    if asist_pcts:
                        prom_asist = sum(asist_pcts) / len(asist_pcts)
                        col_r3.metric("Asistencia promedio", f"{prom_asist:.0f}%")
                col_r4.metric("Total alumnos", len(libro_r) or len(nomina_r))

                # Tabla de riesgo académico
                st.markdown("---")
                st.markdown("#### 🚨 Alumnos en Riesgo Académico")
                en_riesgo = [a for a in libro_r if a.get("promedio", 0) < 4.0 and a.get("promedio", 0) > 0]
                if en_riesgo:
                    for a in en_riesgo:
                        prom_a = a.get("promedio", 0)
                        brecha = 4.0 - prom_a
                        col_riesgo1, col_riesgo2, col_riesgo3 = st.columns([3, 1, 2])
                        col_riesgo1.write(a["nombre"])
                        col_riesgo1.progress(min(prom_a / 7.0, 1.0))
                        col_riesgo2.markdown(f'<span style="color:#ef4444;font-weight:700">{prom_a:.1f}</span>', unsafe_allow_html=True)
                        col_riesgo3.write(f"Necesita +{brecha:.1f} puntos para aprobar")
                else:
                    st.success("✅ No hay alumnos en riesgo académico en este curso.")

                # Análisis IA del curso
                st.markdown("---")
                st.markdown("#### 🤖 Análisis Diagnóstico del Curso")
                if get_llm_fn and st.button("Generar diagnóstico del curso", key="rend_diag"):
                    resumen_datos = f"Curso: {curso_r}\n"
                    if promedios_r:
                        resumen_datos += f"Promedio: {prom_gral:.1f} | Aprobados: {aprobados_r}/{len(promedios_r)}\n"
                        resumen_datos += f"Notas individuales: {', '.join(str(round(p,1)) for p in sorted(promedios_r))}\n"
                    if en_riesgo:
                        resumen_datos += f"Alumnos en riesgo: {len(en_riesgo)}\n"
                    llm_r = get_llm_fn()
                    prompt_r = (
                        f"Eres un coordinador académico de una Facultad de Derecho chilena.\n"
                        f"Analiza estos datos del curso:\n{resumen_datos}\n\n"
                        f"Genera:\n"
                        f"1. DIAGNÓSTICO general del rendimiento del curso (2-3 párrafos)\n"
                        f"2. ÁREAS DE MEJORA identificadas\n"
                        f"3. ACCIONES CONCRETAS recomendadas para el profesor (3-5 acciones)\n"
                        f"4. ALERTA si la tasa de reprobación supera el 30%\n"
                        f"Responde en español formal académico."
                    )
                    with st.spinner("Analizando rendimiento…"):
                        try:
                            diag = llm_r.generate(prompt_r, system=" ", max_tokens=800)
                            st.markdown(diag)
                        except Exception as e:
                            st.error(f"Error: {e}")
