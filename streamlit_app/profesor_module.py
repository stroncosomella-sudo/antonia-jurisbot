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
    font-size: 1.35rem; font-weight: 700;
    color: #f5f0e8; margin-bottom: 0.15rem;
}
.prof-sub {
    font-size: 0.72rem; color: #a09070;
    margin-bottom: 1.2rem; letter-spacing: 0.03em;
}
.prof-card {
    background: #1e1b16;
    border: 1px solid rgba(201,150,58,0.18);
    border-radius: 8px; padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
}
.prof-alumno-btn {
    padding: 0.35rem 0.7rem; border-radius: 20px;
    font-size: 0.68rem; cursor: pointer;
    background: rgba(201,150,58,0.1);
    border: 1px solid rgba(201,150,58,0.2);
    color: #c9963a; display: inline-block;
    margin: 2px;
}
.nota-alta  { color: #22c55e; font-weight: 700; }
.nota-media { color: #fbbf24; font-weight: 700; }
.nota-baja  { color: #ef4444; font-weight: 700; }
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
        ("📝", "evaluaciones",   "Evaluaciones"),
        ("✏️", "nueva_eval",     "Nueva Eval."),
        ("🔬", "investigacion",  "Investigación"),
        ("📋", "asistencia",     "Asistencia"),
        ("💬", "observaciones",  "Observaciones"),
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
                st.markdown(
                    '<div style="height:350px;display:flex;align-items:center;justify-content:center;'
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
