"""
calculadora_plazos_module.py — AntonIA · Mar.IA Group
Calculadora de plazos legales chilenos.

Calcula vencimiento de plazos procesales y sustantivos considerando:
  · Días hábiles vs corridos
  · Feriados legales chilenos (Ley 2.977 + reformas)
  · Ley 20.886 (tramitación electrónica)
  · Plazos del CPC, CPP, Código del Trabajo
"""
from __future__ import annotations
from datetime import date, timedelta, datetime
from typing import Optional

import streamlit as st

# Tema visual
try:
    import theme
    GOLD = theme.GOLD
except ImportError:
    GOLD = "#c9963a"

# ─── Feriados legales Chile 2025-2027 ──────────────────────
# Fuente: Ley 2.977 + leyes especiales
_FERIADOS_FIJOS = [
    (1, 1),    # Año Nuevo
    (5, 1),    # Día del Trabajo
    (5, 21),   # Día de las Glorias Navales
    (6, 20),   # Día Nacional de los Pueblos Indígenas (aproximado, varía)
    (6, 29),   # San Pedro y San Pablo
    (7, 16),   # Virgen del Carmen
    (8, 15),   # Asunción de la Virgen
    (9, 18),   # Independencia Nacional
    (9, 19),   # Glorias del Ejército
    (10, 12),  # Encuentro de Dos Mundos
    (10, 31),  # Día de las Iglesias Evangélicas
    (11, 1),   # Todos los Santos
    (12, 8),   # Inmaculada Concepción
    (12, 25),  # Navidad
]

# Semana Santa (viernes y sábado) - años 2025-2027
_SEMANA_SANTA = {
    2025: [(4, 18), (4, 19)],  # Viernes Santo y Sábado Santo
    2026: [(4, 3), (4, 4)],
    2027: [(3, 26), (3, 27)],
}

def _es_feriado(d: date) -> bool:
    """Retorna True si la fecha es feriado legal chileno."""
    # Feriados fijos
    if (d.month, d.day) in _FERIADOS_FIJOS:
        return True
    # Semana Santa
    ss = _SEMANA_SANTA.get(d.year, [])
    if (d.month, d.day) in ss:
        return True
    return False


def _es_dia_habil(d: date) -> bool:
    """Un día hábil es lunes a sábado, no feriado (art. 66 CPC)."""
    if d.weekday() == 6:  # domingo
        return False
    if _es_feriado(d):
        return False
    return True


def _sumar_dias_habiles(desde: date, n_dias: int) -> date:
    """Suma n días hábiles a partir de 'desde' (sin contar el día inicial)."""
    actual = desde
    contados = 0
    while contados < n_dias:
        actual += timedelta(days=1)
        if _es_dia_habil(actual):
            contados += 1
    return actual


def _sumar_dias_corridos(desde: date, n_dias: int) -> date:
    """Suma n días corridos. Si vence en feriado, se prorroga al siguiente hábil."""
    vencimiento = desde + timedelta(days=n_dias)
    # Prórroga art. 66 CPC: si vence en feriado, se extiende al día hábil siguiente
    while not _es_dia_habil(vencimiento):
        vencimiento += timedelta(days=1)
    return vencimiento


# ─── Plazos predefinidos ────────────────────────────────────
PLAZOS_CIVILES = [
    {
        "nombre": "Contestación demanda (juicio ordinario)",
        "dias": 15,
        "tipo": "hábiles",
        "fuente": "Art. 258 CPC",
        "nota": "15 días hábiles desde notificación. +3 si notificado fuera de la comuna, +18 si fuera del territorio.",
    },
    {
        "nombre": "Período de prueba (ordinario)",
        "dias": 20,
        "tipo": "hábiles",
        "fuente": "Art. 328 CPC",
        "nota": "20 días hábiles. Puede ampliarse por prueba fuera del territorio.",
    },
    {
        "nombre": "Contestación demanda (juicio sumario)",
        "dias": 5,
        "tipo": "hábiles",
        "fuente": "Art. 683 CPC",
        "nota": "Audiencia al 5° día hábil.",
    },
    {
        "nombre": "Recurso de apelación (sentencia definitiva)",
        "dias": 10,
        "tipo": "hábiles",
        "fuente": "Art. 189 CPC",
        "nota": "10 días hábiles desde notificación.",
    },
    {
        "nombre": "Recurso de apelación (interlocutorias/autos)",
        "dias": 5,
        "tipo": "hábiles",
        "fuente": "Art. 189 CPC",
        "nota": "5 días hábiles desde notificación.",
    },
    {
        "nombre": "Recurso de casación (forma y fondo)",
        "dias": 15,
        "tipo": "hábiles",
        "fuente": "Arts. 770, 776 CPC",
        "nota": "15 días hábiles desde notificación.",
    },
    {
        "nombre": "Recurso de reposición",
        "dias": 5,
        "tipo": "hábiles",
        "fuente": "Art. 181 CPC",
        "nota": "5 días hábiles. Autos y decretos.",
    },
    {
        "nombre": "Prescripción acción ejecutiva",
        "dias": 1095,
        "tipo": "corridos",
        "fuente": "Art. 2515 CC",
        "nota": "3 años desde que la obligación se hizo exigible.",
    },
    {
        "nombre": "Prescripción acción ordinaria",
        "dias": 1825,
        "tipo": "corridos",
        "fuente": "Art. 2515 CC",
        "nota": "5 años desde que la obligación se hizo exigible.",
    },
]

PLAZOS_LABORALES = [
    {
        "nombre": "Demanda por despido injustificado",
        "dias": 60,
        "tipo": "hábiles",
        "fuente": "Art. 168 CT",
        "nota": "60 días hábiles desde separación. Suspensión por reclamo administrativo (máx. 90 días corridos).",
    },
    {
        "nombre": "Demanda tutela laboral",
        "dias": 60,
        "tipo": "hábiles",
        "fuente": "Art. 486 CT",
        "nota": "60 días hábiles desde la vulneración o desde el despido.",
    },
    {
        "nombre": "Recurso de nulidad laboral",
        "dias": 10,
        "tipo": "hábiles",
        "fuente": "Art. 477 CT",
        "nota": "10 días hábiles desde notificación de la sentencia.",
    },
    {
        "nombre": "Contestación demanda laboral",
        "dias": 0,
        "tipo": "hábiles",
        "fuente": "Art. 452 CT",
        "nota": "Hasta la audiencia preparatoria. Se recomienda presentar con antelación.",
    },
    {
        "nombre": "Jornada semanal máxima (Ley 21.561)",
        "dias": 0,
        "tipo": "corridos",
        "fuente": "Ley 21.561 (40 horas)",
        "nota": "Reducción gradual: 44h (2024), 42h (2025), 40h (2028). Consulte régimen transitorio.",
    },
    {
        "nombre": "Aviso de despido anticipado",
        "dias": 30,
        "tipo": "corridos",
        "fuente": "Art. 162 CT",
        "nota": "30 días corridos de aviso. Puede sustituirse con indemnización de un mes.",
    },
]

PLAZOS_PENALES = [
    {
        "nombre": "Recurso de nulidad penal",
        "dias": 10,
        "tipo": "corridos",
        "fuente": "Art. 372 CPP",
        "nota": "10 días corridos desde notificación de la sentencia definitiva.",
    },
    {
        "nombre": "Recurso de apelación penal (auto de apertura)",
        "dias": 5,
        "tipo": "corridos",
        "fuente": "Art. 366 CPP",
        "nota": "5 días corridos.",
    },
    {
        "nombre": "Plazo investigación (con formalización)",
        "dias": 730,
        "tipo": "corridos",
        "fuente": "Art. 247 CPP",
        "nota": "Máximo 2 años desde formalización. Juez puede fijar plazo menor.",
    },
    {
        "nombre": "Detención: control de legalidad",
        "dias": 1,
        "tipo": "corridos",
        "fuente": "Art. 131 CPP",
        "nota": "Debe ser puesto a disposición del juez dentro de 24 horas.",
    },
    {
        "nombre": "Prisión preventiva — revisión",
        "dias": 180,
        "tipo": "corridos",
        "fuente": "Art. 145 CPP",
        "nota": "Revisable de oficio cada 6 meses.",
    },
    {
        "nombre": "Prescripción acción penal (crimen)",
        "dias": 3650,
        "tipo": "corridos",
        "fuente": "Art. 94 CP",
        "nota": "10 años para crímenes. 5 años simples delitos. 6 meses faltas.",
    },
]

PLAZOS_CONSTITUCIONAL = [
    {
        "nombre": "Recurso de protección",
        "dias": 30,
        "tipo": "corridos",
        "fuente": "Auto Acordado CS",
        "nota": "30 días corridos desde acto u omisión. Plazo fatal.",
    },
    {
        "nombre": "Recurso de amparo (habeas corpus)",
        "dias": 0,
        "tipo": "corridos",
        "fuente": "Art. 21 CPR",
        "nota": "Sin plazo legal expreso. Debe interponerse mientras subsista la privación.",
    },
    {
        "nombre": "Inaplicabilidad ante TC",
        "dias": 0,
        "tipo": "corridos",
        "fuente": "Art. 93 Nº6 CPR",
        "nota": "Mientras gestión esté pendiente. No tiene plazo fijo.",
    },
]

CATEGORIAS_PLAZOS = {
    "Civil y Procesal": PLAZOS_CIVILES,
    "Laboral": PLAZOS_LABORALES,
    "Penal": PLAZOS_PENALES,
    "Constitucional": PLAZOS_CONSTITUCIONAL,
}

# ─── CSS ───────────────────────────────────────────────────
_CSS = f"""
<style>
.plazos-header {{
    text-align: center;
    padding: 1rem 0 0.5rem;
}}
.plazos-header h2 {{
    font-family: 'Playfair Display', serif;
    color: #1a1813;
    font-size: 1.5rem;
    margin: 0;
}}
.plazos-header .sub {{
    color: #9a8e7e;
    font-size: 0.8rem;
    margin-top: 0.3rem;
}}
.plazo-result {{
    background: #ffffff;
    border: 1px solid #e2dbd0;
    border-top: 3px solid {GOLD};
    border-radius: 0 0 12px 12px;
    padding: 1.8rem;
    margin: 1rem 0;
    box-shadow: 0 2px 16px rgba(20,18,10,0.06);
    text-align: center;
}}
.plazo-vencimiento {{
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #1a1813;
    margin: 0.5rem 0;
}}
.plazo-detalle {{
    color: #5a4e3e;
    font-size: 0.85rem;
    line-height: 1.6;
}}
.plazo-fuente {{
    font-size: 0.75rem;
    color: {GOLD};
    font-weight: 600;
    margin-top: 0.5rem;
}}
.plazo-card {{
    background: #ffffff;
    border: 1px solid #e2dbd0;
    border-left: 3px solid {GOLD};
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.2rem;
    margin: 0.5rem 0;
    cursor: pointer;
    transition: box-shadow 0.2s;
}}
.plazo-card:hover {{
    box-shadow: 0 2px 12px rgba(201,150,58,0.15);
}}
.plazo-card .name {{
    font-weight: 600;
    color: #1a1813;
    font-size: 0.88rem;
}}
.plazo-card .meta {{
    font-size: 0.75rem;
    color: #9a8e7e;
    margin-top: 0.25rem;
}}
.plazo-warning {{
    background: rgba(239,68,68,0.06);
    border: 1px solid rgba(239,68,68,0.15);
    border-radius: 8px;
    padding: 0.8rem;
    margin-top: 0.8rem;
    font-size: 0.78rem;
    color: #b91c1c;
}}
</style>
"""

# ─── Días de la semana y meses en español ──────────────────
_DIAS_ES = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
_MESES_ES = [
    "", "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

def _fecha_es(d: date) -> str:
    """Formatea fecha en español: 'lunes 5 de mayo de 2026'"""
    dia_sem = _DIAS_ES[d.weekday()]
    return f"{dia_sem} {d.day} de {_MESES_ES[d.month]} de {d.year}"


# ─── Renderizador principal ──────────────────────────────
def render_calculadora_plazos():
    """Punto de entrada del módulo Calculadora de Plazos."""
    st.markdown(_CSS, unsafe_allow_html=True)

    st.markdown(
        '<div class="plazos-header">'
        '<h2>Calculadora de Plazos Legales</h2>'
        '<div class="sub">Plazos procesales y sustantivos del derecho chileno · Feriados actualizados</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Tabs: Calcular plazo / Tabla de plazos
    tab1, tab2 = st.tabs(["Calcular Plazo", "Tabla de Plazos"])

    with tab1:
        _tab_calcular()

    with tab2:
        _tab_tabla()


def _tab_calcular():
    """Tab de cálculo de plazo."""
    col1, col2 = st.columns(2)

    with col1:
        modo = st.radio(
            "Modo de cálculo",
            ["Plazo predefinido", "Plazo personalizado"],
            key="plazo_modo",
            horizontal=True
        )

    with col2:
        fecha_inicio = st.date_input(
            "Fecha de inicio (notificación / hecho)",
            value=date.today(),
            key="plazo_fecha"
        )

    if modo == "Plazo predefinido":
        categoria = st.selectbox(
            "Categoría",
            options=list(CATEGORIAS_PLAZOS.keys()),
            key="plazo_cat"
        )
        plazos_cat = CATEGORIAS_PLAZOS[categoria]
        plazo_nombres = [p["nombre"] for p in plazos_cat]
        plazo_idx = st.selectbox(
            "Plazo",
            options=range(len(plazo_nombres)),
            format_func=lambda i: plazo_nombres[i],
            key="plazo_sel"
        )
        plazo = plazos_cat[plazo_idx]
        n_dias = plazo["dias"]
        tipo = plazo["tipo"]
        fuente = plazo["fuente"]
        nota = plazo.get("nota", "")
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            n_dias = st.number_input("Número de días", min_value=1, max_value=3650, value=15, key="plazo_n_dias")
        with col_b:
            tipo = st.selectbox("Tipo de días", ["hábiles", "corridos"], key="plazo_tipo")
        fuente = ""
        nota = ""

    if st.button("Calcular Vencimiento", key="plazo_calc_btn", type="primary", use_container_width=True):
        if n_dias == 0:
            st.info(f"Este plazo no tiene un número fijo de días. {nota}")
            return

        if tipo == "hábiles":
            vencimiento = _sumar_dias_habiles(fecha_inicio, n_dias)
        else:
            vencimiento = _sumar_dias_corridos(fecha_inicio, n_dias)

        # Días naturales hasta vencimiento
        dias_naturales = (vencimiento - fecha_inicio).days

        st.markdown(
            f'<div class="plazo-result">'
            f'<div style="font-size:0.75rem;color:#9a8e7e;text-transform:uppercase;letter-spacing:0.1em;">Vencimiento</div>'
            f'<div class="plazo-vencimiento">{_fecha_es(vencimiento)}</div>'
            f'<div class="plazo-detalle">'
            f'{n_dias} días {tipo} desde {_fecha_es(fecha_inicio)}<br>'
            f'({dias_naturales} días naturales en total)'
            f'</div>',
            unsafe_allow_html=True
        )

        if fuente:
            st.markdown(f'<div class="plazo-fuente">{fuente}</div>', unsafe_allow_html=True)
        if nota:
            st.markdown(f'<div style="font-size:0.78rem;color:#5a4e3e;margin-top:0.5rem;">{nota}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Advertencia sobre feriados en el camino
        feriados_en_rango = []
        check = fecha_inicio
        while check <= vencimiento:
            if _es_feriado(check):
                feriados_en_rango.append(check)
            check += timedelta(days=1)

        if feriados_en_rango:
            feriados_str = ", ".join(f"{_fecha_es(f)}" for f in feriados_en_rango[:5])
            if len(feriados_en_rango) > 5:
                feriados_str += f" y {len(feriados_en_rango) - 5} más"
            st.markdown(
                f'<div class="plazo-warning">'
                f'Feriados en el período: {feriados_str}'
                f'</div>',
                unsafe_allow_html=True
            )

        # Disclaimer
        st.markdown(
            '<div style="font-size:0.68rem;color:#9a8e7e;text-align:center;margin-top:1rem;padding:0.8rem;'
            'border-top:1px solid #e2dbd0;">'
            'Esta calculadora es una herramienta de referencia. Verifique siempre los plazos con la '
            'normativa vigente y la jurisprudencia aplicable. Los feriados pueden variar por decretos especiales.</div>',
            unsafe_allow_html=True
        )


def _tab_tabla():
    """Tab con tabla de referencia de plazos."""
    for cat_nombre, plazos in CATEGORIAS_PLAZOS.items():
        st.markdown(
            f'<div style="font-family:\'Playfair Display\',serif;font-size:1.05rem;'
            f'font-weight:600;color:#1a1813;margin:1.2rem 0 0.5rem;'
            f'padding-bottom:0.3rem;border-bottom:2px solid {GOLD};">'
            f'{cat_nombre}</div>',
            unsafe_allow_html=True
        )

        for p in plazos:
            dias_text = f'{p["dias"]} días {p["tipo"]}' if p["dias"] > 0 else "Sin plazo fijo"
            st.markdown(
                f'<div class="plazo-card">'
                f'<div class="name">{p["nombre"]}</div>'
                f'<div class="meta">{dias_text} · {p["fuente"]}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
