"""
examen_simulado_module.py — AntonIA · Mar.IA Group
Módulo de Examen Simulado con nota 1.0–7.0 (escala chilena).

Flujo:
  1. Configuración: seleccionar ramo, nº de preguntas, tiempo
  2. Examen: cronómetro + preguntas MCQ secuenciales
  3. Resultados: nota, desglose, retroalimentación
"""
from __future__ import annotations
import random
import time
import math
from datetime import datetime
from typing import Optional

import streamlit as st

# Importar bancos de preguntas
try:
    from banco_preguntas import BANCO_MCQ
except ImportError:
    BANCO_MCQ = {}

try:
    from banco_desarrollo import BANCO_DEV
except ImportError:
    BANCO_DEV = {}

# Tema visual
try:
    import theme
    GOLD = theme.GOLD
    DARK = theme.DARK
    CARD = theme.CARD
except ImportError:
    GOLD = "#c9963a"
    DARK = "#141210"
    CARD = "#1e1b16"

# ─── Constantes ────────────────────────────────────────────
RAMOS_DISPONIBLES = {
    "civil":           "Derecho Civil",
    "penal":           "Derecho Penal",
    "procesal":        "Derecho Procesal",
    "constitucional":  "Derecho Constitucional",
    "laboral":         "Derecho Laboral",
    "comercial":       "Derecho Comercial",
    "administrativo":  "Derecho Administrativo",
    "tributario":      "Derecho Tributario",
}

OPCIONES_N_PREGUNTAS = [5, 10, 15, 20]
OPCIONES_TIEMPO = {
    "Sin límite": 0,
    "15 minutos": 15 * 60,
    "30 minutos": 30 * 60,
    "45 minutos": 45 * 60,
    "60 minutos": 60 * 60,
}


def _calcular_nota(correctas: int, total: int) -> float:
    """
    Escala chilena: 60% exigencia → nota 4.0
    Fórmula:
      - Si pct < 60%: nota = 1.0 + (pct / 0.6) * 3.0
      - Si pct >= 60%: nota = 4.0 + ((pct - 0.6) / 0.4) * 3.0
    Rango: 1.0 a 7.0
    """
    if total == 0:
        return 1.0
    pct = correctas / total
    if pct < 0.6:
        nota = 1.0 + (pct / 0.6) * 3.0
    else:
        nota = 4.0 + ((pct - 0.6) / 0.4) * 3.0
    return round(min(7.0, max(1.0, nota)), 1)


def _color_nota(nota: float) -> str:
    if nota >= 5.5:
        return "#22c55e"  # verde
    elif nota >= 4.0:
        return "#eab308"  # amarillo
    else:
        return "#ef4444"  # rojo


def _shuffle_preguntas(ramo: str, n: int) -> list[dict]:
    """Obtiene n preguntas MCQ del ramo, barajadas."""
    pool = BANCO_MCQ.get(ramo, [])
    if not pool:
        return []
    seleccion = random.sample(pool, min(n, len(pool)))
    return seleccion


# ─── CSS del módulo ────────────────────────────────────────
_CSS = f"""
<style>
.exam-header {{
    text-align: center;
    padding: 1rem 0 0.5rem;
}}
.exam-header h2 {{
    font-family: 'Playfair Display', serif;
    color: #1a1813;
    font-size: 1.5rem;
    margin: 0;
}}
.exam-header .sub {{
    color: #9a8e7e;
    font-size: 0.8rem;
    margin-top: 0.3rem;
}}
.exam-config-card {{
    background: #ffffff;
    border: 1px solid #e2dbd0;
    border-top: 3px solid {GOLD};
    border-radius: 0 0 12px 12px;
    padding: 1.8rem;
    max-width: 560px;
    margin: 1rem auto;
    box-shadow: 0 2px 16px rgba(20,18,10,0.06);
}}
.exam-timer {{
    text-align: center;
    font-family: 'Courier New', monospace;
    font-size: 1.4rem;
    font-weight: 700;
    padding: 0.5rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}}
.exam-timer.warning {{
    color: #ef4444;
    background: rgba(239,68,68,0.08);
}}
.exam-timer.normal {{
    color: #1a1813;
    background: rgba(201,150,58,0.08);
}}
.exam-q-card {{
    background: #ffffff;
    border: 1px solid #e2dbd0;
    border-left: 3px solid {GOLD};
    border-radius: 0 10px 10px 0;
    padding: 1.5rem;
    margin: 0.8rem 0;
    box-shadow: 0 1px 8px rgba(20,18,10,0.04);
}}
.exam-q-num {{
    font-size: 0.72rem;
    font-weight: 700;
    color: {GOLD};
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.5rem;
}}
.exam-q-text {{
    font-size: 0.95rem;
    color: #1a1813;
    line-height: 1.6;
    margin-bottom: 1rem;
}}
.exam-result-card {{
    background: #ffffff;
    border: 1px solid #e2dbd0;
    border-radius: 12px;
    padding: 2rem;
    max-width: 640px;
    margin: 1rem auto;
    text-align: center;
    box-shadow: 0 4px 24px rgba(20,18,10,0.08);
}}
.exam-nota {{
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 700;
    margin: 0.5rem 0;
}}
.exam-desglose {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    margin-top: 1.5rem;
}}
.exam-desglose .stat {{
    background: #faf8f4;
    border-radius: 8px;
    padding: 1rem;
}}
.exam-desglose .stat-val {{
    font-size: 1.5rem;
    font-weight: 700;
    color: #1a1813;
}}
.exam-desglose .stat-label {{
    font-size: 0.72rem;
    color: #9a8e7e;
    margin-top: 0.3rem;
}}
.exam-retro-correct {{
    background: rgba(34,197,94,0.06);
    border-left: 3px solid #22c55e;
    border-radius: 0 8px 8px 0;
    padding: 1rem;
    margin: 0.5rem 0;
}}
.exam-retro-wrong {{
    background: rgba(239,68,68,0.06);
    border-left: 3px solid #ef4444;
    border-radius: 0 8px 8px 0;
    padding: 1rem;
    margin: 0.5rem 0;
}}
</style>
"""


# ─── Renderizador principal ──────────────────────────────
def render_examen_simulado():
    """Punto de entrada del módulo Examen Simulado."""
    st.markdown(_CSS, unsafe_allow_html=True)

    # Inicializar estado
    if "exam_fase" not in st.session_state:
        st.session_state.exam_fase = "config"  # config → examen → resultados

    fase = st.session_state.exam_fase

    if fase == "config":
        _fase_configuracion()
    elif fase == "examen":
        _fase_examen()
    elif fase == "resultados":
        _fase_resultados()


def _fase_configuracion():
    """Pantalla de configuración del examen."""
    st.markdown(
        '<div class="exam-header">'
        '<h2>Examen Simulado</h2>'
        '<div class="sub">Evalúa tus conocimientos con nota en escala 1.0 – 7.0</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="exam-config-card">', unsafe_allow_html=True)

    # Filtrar ramos disponibles (solo los que tienen preguntas MCQ)
    ramos_con_preguntas = {k: v for k, v in RAMOS_DISPONIBLES.items() if k in BANCO_MCQ and len(BANCO_MCQ[k]) >= 5}

    if not ramos_con_preguntas:
        st.warning("No hay ramos con suficientes preguntas para generar un examen. Se necesitan al menos 5 preguntas MCQ por ramo.")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    ramo_seleccionado = st.selectbox(
        "Selecciona el ramo",
        options=list(ramos_con_preguntas.keys()),
        format_func=lambda x: ramos_con_preguntas[x],
        key="exam_ramo_select"
    )

    max_preguntas = len(BANCO_MCQ.get(ramo_seleccionado, []))
    opciones_n = [n for n in OPCIONES_N_PREGUNTAS if n <= max_preguntas]
    if not opciones_n:
        opciones_n = [max_preguntas]

    n_preguntas = st.selectbox(
        "Número de preguntas",
        options=opciones_n,
        index=min(1, len(opciones_n) - 1),
        key="exam_n_select"
    )

    tiempo_label = st.selectbox(
        "Tiempo límite",
        options=list(OPCIONES_TIEMPO.keys()),
        index=0,
        key="exam_tiempo_select"
    )
    tiempo_segundos = OPCIONES_TIEMPO[tiempo_label]

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        if st.button("Comenzar Examen", use_container_width=True, key="exam_start_btn", type="primary"):
            # Preparar preguntas
            preguntas = _shuffle_preguntas(ramo_seleccionado, n_preguntas)
            if len(preguntas) < n_preguntas:
                st.warning(f"Solo hay {len(preguntas)} preguntas disponibles para este ramo.")

            st.session_state.exam_preguntas = preguntas
            st.session_state.exam_respuestas = [None] * len(preguntas)
            st.session_state.exam_ramo = ramo_seleccionado
            st.session_state.exam_ramo_nombre = RAMOS_DISPONIBLES.get(ramo_seleccionado, ramo_seleccionado)
            st.session_state.exam_tiempo_limite = tiempo_segundos
            st.session_state.exam_inicio = time.time()
            st.session_state.exam_idx = 0
            st.session_state.exam_fase = "examen"
            st.rerun()


def _fase_examen():
    """Pantalla del examen en curso."""
    preguntas = st.session_state.get("exam_preguntas", [])
    respuestas = st.session_state.get("exam_respuestas", [])
    idx = st.session_state.get("exam_idx", 0)
    tiempo_limite = st.session_state.get("exam_tiempo_limite", 0)
    inicio = st.session_state.get("exam_inicio", time.time())
    ramo_nombre = st.session_state.get("exam_ramo_nombre", "")

    if not preguntas:
        st.error("No se encontraron preguntas. Vuelve a configurar el examen.")
        if st.button("Volver", key="exam_volver_err"):
            st.session_state.exam_fase = "config"
            st.rerun()
        return

    total = len(preguntas)
    transcurrido = time.time() - inicio

    # Timer
    if tiempo_limite > 0:
        restante = max(0, tiempo_limite - transcurrido)
        mins = int(restante // 60)
        secs = int(restante % 60)
        timer_class = "warning" if restante < 120 else "normal"
        st.markdown(
            f'<div class="exam-timer {timer_class}">'
            f'{ramo_nombre} — Pregunta {idx + 1} de {total} — '
            f'Tiempo: {mins:02d}:{secs:02d}'
            f'</div>',
            unsafe_allow_html=True
        )
        # Si se acabó el tiempo, finalizar
        if restante <= 0:
            st.session_state.exam_fase = "resultados"
            st.session_state.exam_fin = time.time()
            st.rerun()
            return
    else:
        st.markdown(
            f'<div class="exam-timer normal">'
            f'{ramo_nombre} — Pregunta {idx + 1} de {total} — Sin límite de tiempo'
            f'</div>',
            unsafe_allow_html=True
        )

    # Barra de progreso
    st.progress((idx) / total, text=f"{idx}/{total} respondidas")

    # Pregunta actual
    p = preguntas[idx]
    pregunta_text = p.get("pregunta", "Pregunta no disponible")
    opciones = p.get("opciones", [])

    st.markdown(
        f'<div class="exam-q-card">'
        f'<div class="exam-q-num">Pregunta {idx + 1}</div>'
        f'<div class="exam-q-text">{pregunta_text}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # Opciones como radio buttons
    letras = ["A", "B", "C", "D"]
    opciones_display = [f"{letras[i]}. {op}" for i, op in enumerate(opciones)]

    # Valor previo si ya respondió esta pregunta
    prev_answer = respuestas[idx]
    default_idx = prev_answer if prev_answer is not None else None

    seleccion = st.radio(
        "Selecciona tu respuesta:",
        options=list(range(len(opciones))),
        format_func=lambda i: opciones_display[i],
        index=default_idx,
        key=f"exam_radio_{idx}",
        label_visibility="collapsed"
    )

    # Navegación
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if idx > 0:
            if st.button("← Anterior", key="exam_prev", use_container_width=True):
                # Guardar respuesta actual
                st.session_state.exam_respuestas[idx] = seleccion
                st.session_state.exam_idx = idx - 1
                st.rerun()

    with col2:
        # Mapa de preguntas
        respondidas = sum(1 for r in respuestas if r is not None)
        st.markdown(
            f'<div style="text-align:center;color:#9a8e7e;font-size:0.78rem;padding-top:0.5rem;">'
            f'{respondidas} de {total} respondidas'
            f'</div>',
            unsafe_allow_html=True
        )

    with col3:
        if idx < total - 1:
            if st.button("Siguiente →", key="exam_next", use_container_width=True):
                st.session_state.exam_respuestas[idx] = seleccion
                st.session_state.exam_idx = idx + 1
                st.rerun()
        else:
            if st.button("Finalizar Examen", key="exam_finish", use_container_width=True, type="primary"):
                st.session_state.exam_respuestas[idx] = seleccion
                st.session_state.exam_fin = time.time()
                st.session_state.exam_fase = "resultados"
                st.rerun()

    # Mapa rápido de navegación
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown(
        '<div style="font-size:0.72rem;color:#9a8e7e;text-align:center;margin-bottom:0.4rem;">'
        'Navegación rápida</div>',
        unsafe_allow_html=True
    )
    n_cols = min(total, 10)
    rows_needed = math.ceil(total / n_cols)
    for row in range(rows_needed):
        start = row * n_cols
        end = min(start + n_cols, total)
        cols = st.columns(n_cols)
        for j, col in enumerate(cols):
            q_idx = start + j
            if q_idx < total:
                answered = respuestas[q_idx] is not None
                label = f"{'✓' if answered else ''}{q_idx + 1}"
                if col.button(label, key=f"exam_nav_{q_idx}", use_container_width=True):
                    st.session_state.exam_respuestas[idx] = seleccion
                    st.session_state.exam_idx = q_idx
                    st.rerun()


def _fase_resultados():
    """Pantalla de resultados del examen."""
    preguntas = st.session_state.get("exam_preguntas", [])
    respuestas = st.session_state.get("exam_respuestas", [])
    ramo_nombre = st.session_state.get("exam_ramo_nombre", "")
    inicio = st.session_state.get("exam_inicio", 0)
    fin = st.session_state.get("exam_fin", time.time())

    total = len(preguntas)
    correctas = 0
    detalles = []

    for i, p in enumerate(preguntas):
        resp_usuario = respuestas[i] if i < len(respuestas) else None
        correcta_idx = p.get("correcta", -1)
        es_correcta = resp_usuario == correcta_idx

        if es_correcta:
            correctas += 1

        detalles.append({
            "num": i + 1,
            "pregunta": p.get("pregunta", ""),
            "opciones": p.get("opciones", []),
            "correcta_idx": correcta_idx,
            "resp_usuario": resp_usuario,
            "es_correcta": es_correcta,
            "explicacion": p.get("explicacion", p.get("pauta", "")),
        })

    nota = _calcular_nota(correctas, total)
    color = _color_nota(nota)
    pct = round((correctas / total) * 100) if total > 0 else 0
    tiempo_total = int(fin - inicio)
    mins = tiempo_total // 60
    secs = tiempo_total % 60

    # Resultado principal
    st.markdown(
        f'<div class="exam-result-card">'
        f'<div style="font-size:0.78rem;color:#9a8e7e;text-transform:uppercase;letter-spacing:0.1em;">'
        f'Resultado — {ramo_nombre}</div>'
        f'<div class="exam-nota" style="color:{color};">{nota}</div>'
        f'<div style="font-size:0.85rem;color:#5a4e3e;">Escala 1.0 – 7.0 · Exigencia 60%</div>'
        f'<div class="exam-desglose">'
        f'<div class="stat"><div class="stat-val">{correctas}/{total}</div>'
        f'<div class="stat-label">Correctas</div></div>'
        f'<div class="stat"><div class="stat-val">{pct}%</div>'
        f'<div class="stat-label">Aprobación</div></div>'
        f'<div class="stat"><div class="stat-val">{mins}:{secs:02d}</div>'
        f'<div class="stat-label">Tiempo</div></div>'
        f'</div></div>',
        unsafe_allow_html=True
    )

    # Retroalimentación pregunta por pregunta
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown(
        '<div style="font-family:\'Playfair Display\',serif;font-size:1.1rem;'
        'font-weight:600;color:#1a1813;margin-bottom:0.8rem;">'
        'Retroalimentación</div>',
        unsafe_allow_html=True
    )

    letras = ["A", "B", "C", "D"]
    for d in detalles:
        css_class = "exam-retro-correct" if d["es_correcta"] else "exam-retro-wrong"
        icono = "✓" if d["es_correcta"] else "✗"
        color_ico = "#22c55e" if d["es_correcta"] else "#ef4444"

        resp_text = "Sin respuesta"
        if d["resp_usuario"] is not None and d["resp_usuario"] < len(d["opciones"]):
            resp_text = f'{letras[d["resp_usuario"]]}. {d["opciones"][d["resp_usuario"]]}'

        correcta_text = ""
        if d["correcta_idx"] < len(d["opciones"]):
            correcta_text = f'{letras[d["correcta_idx"]]}. {d["opciones"][d["correcta_idx"]]}'

        explicacion_html = ""
        if d["explicacion"]:
            from utils.llm_resilient import safe_html_text
            explicacion_html = (
                f'<div style="font-size:0.78rem;color:#5a4e3e;margin-top:0.5rem;'
                f'padding-top:0.5rem;border-top:1px solid rgba(0,0,0,0.06);">'
                f'<strong>Explicación:</strong> {safe_html_text(d["explicacion"])}</div>'
            )

        st.markdown(
            f'<div class="{css_class}">'
            f'<div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.3rem;">'
            f'<span style="color:{color_ico};font-weight:700;font-size:1.1rem;">{icono}</span>'
            f'<span style="font-size:0.78rem;font-weight:600;color:#1a1813;">Pregunta {d["num"]}</span>'
            f'</div>'
            f'<div style="font-size:0.85rem;color:#1a1813;margin-bottom:0.4rem;">{safe_html_text(d["pregunta"])}</div>'
            f'<div style="font-size:0.78rem;color:#5a4e3e;">'
            f'Tu respuesta: <strong>{safe_html_text(resp_text)}</strong></div>',
            unsafe_allow_html=True
        )

        if not d["es_correcta"]:
            st.markdown(
                f'<div style="font-size:0.78rem;color:#22c55e;margin-top:0.2rem;">'
                f'Respuesta correcta: <strong>{safe_html_text(correcta_text)}</strong></div>',
                unsafe_allow_html=True
            )

        if explicacion_html:
            st.markdown(explicacion_html, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # Botones finales
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Repetir Examen", key="exam_repetir", use_container_width=True):
            st.session_state.exam_fase = "config"
            # Limpiar estado anterior
            for k in list(st.session_state.keys()):
                if k.startswith("exam_") and k != "exam_fase":
                    del st.session_state[k]
            st.rerun()
    with col2:
        if st.button("Volver al Inicio", key="exam_home", use_container_width=True):
            st.session_state.exam_fase = "config"
            for k in list(st.session_state.keys()):
                if k.startswith("exam_"):
                    del st.session_state[k]
            st.session_state.nav = "HOME"
            st.rerun()
