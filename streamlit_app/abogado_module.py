"""
abogado_module.py — AntonIA · Área Abogados
Herramientas de gestión profesional para abogados.

Módulos:
  · Casos          — cartera de causas con notas
  · Cronómetro     — registro de horas por causa
  · Plazos         — calendario de vencimientos
  · Correos        — redacción asistida por IA
  · Pendientes     — gestor de tareas
  · Documentos     — generación de escritos jurídicos
  · Honorarios     — seguimiento y propuestas de honorarios
"""

import streamlit as st
import json, time, datetime
from pathlib import Path

_GOLD  = "#c9963a"
_DARK  = "#141210"
_CARD  = "#1e1b16"
_CARD2 = "#221e17"
_MUTED = "#a09070"
_WHITE = "#f5f0e8"
_GREEN = "#22c55e"
_RED   = "#ef4444"
_BLUE  = "#3b82f6"

# ─── Estilos comunes ───────────────────────────────────────────────
_CSS = """
<style>
.abg-tab-header {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 1.35rem; font-weight: 700;
    color: #f5f0e8; margin-bottom: 0.15rem;
}
.abg-tab-sub {
    font-size: 0.72rem; color: #a09070;
    margin-bottom: 1.2rem; letter-spacing: 0.03em;
}
.abg-card {
    background: #1e1b16;
    border: 1px solid rgba(201,150,58,0.18);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
}
.abg-card-title {
    font-size: 0.82rem; font-weight: 700;
    color: #f5f0e8; margin-bottom: 0.2rem;
}
.abg-badge {
    display: inline-block;
    padding: 1px 8px; border-radius: 20px;
    font-size: 0.62rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.06em;
}
.badge-activo   { background: rgba(34,197,94,0.15);  color: #22c55e; }
.badge-pendiente{ background: rgba(251,191,36,0.15); color: #fbbf24; }
.badge-cerrado  { background: rgba(160,144,112,0.15);color: #a09070; }
.abg-timer-display {
    font-family: 'Courier New', monospace;
    font-size: 3.2rem; font-weight: 700;
    color: #c9963a; text-align: center;
    letter-spacing: 0.08em; padding: 1.5rem 0;
}
.abg-plazo-urgent {
    border-left: 3px solid #ef4444 !important;
}
.abg-plazo-warning {
    border-left: 3px solid #fbbf24 !important;
}
.abg-plazo-ok {
    border-left: 3px solid #22c55e !important;
}
@media (max-width: 640px) {
    .abg-timer-display { font-size: 2rem; }
}
</style>
"""

# ── Inicialización de estado ───────────────────────────────────────
def _init():
    defaults = {
        "abg_tab":        "casos",
        # Casos
        "abg_casos":      [],
        "abg_caso_sel":   None,
        # Cronómetro
        "abg_timer_on":   False,
        "abg_timer_start": None,
        "abg_timer_caso": "",
        "abg_timer_acum": {},   # {caso_id: segundos}
        # Plazos
        "abg_plazos":     [],
        # Pendientes
        "abg_tasks":      [],
        # Honorarios
        "abg_honorarios": [],
        # Correos / Documentos — resultado IA
        "abg_correo_result":   "",
        "abg_doc_result":      "",
        "abg_hon_propuesta":   "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

# ── Helpers ───────────────────────────────────────────────────────
def _fmt_seconds(s: int) -> str:
    h, rem = divmod(int(s), 3600)
    m, sec = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{sec:02d}"

def _dias_para(fecha_str: str) -> int:
    try:
        d = datetime.date.fromisoformat(fecha_str)
        return (d - datetime.date.today()).days
    except Exception:
        return 9999


# ═══════════════════════════════════════════════════════════════════
def render_abogado(get_llm_fn=None):
    """Renderiza el área completa de Abogados."""
    _init()
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Tabs visuales ──────────────────────────────────────────────
    TABS = [
        ("📁", "casos",       "Casos"),
        ("⏱️", "cronometro",  "Cronómetro"),
        ("📅", "plazos",      "Plazos"),
        ("✉️", "correos",     "Correos"),
        ("✅", "pendientes",  "Pendientes"),
        ("📄", "documentos",  "Documentos"),
        ("💰", "honorarios",  "Honorarios"),
    ]

    tab_cols = st.columns(len(TABS))
    for col, (icon, tid, label) in zip(tab_cols, TABS):
        active = st.session_state.abg_tab == tid
        with col:
            if active:
                st.markdown(
                    f'<div style="text-align:center;padding:0.4rem 0;'
                    f'border-bottom:2px solid {_GOLD};color:{_GOLD};'
                    f'font-size:0.72rem;font-weight:700;text-transform:uppercase;'
                    f'letter-spacing:0.04em;">{icon} {label}</div>',
                    unsafe_allow_html=True)
            else:
                if st.button(f"{icon} {label}", key=f"abg_t_{tid}",
                             use_container_width=True):
                    st.session_state.abg_tab = tid
                    st.rerun()

    st.markdown('<hr style="border-color:rgba(201,150,58,0.15);margin:0.8rem 0 1.2rem;">', unsafe_allow_html=True)

    tab = st.session_state.abg_tab

    # ── CASOS ──────────────────────────────────────────────────────
    if tab == "casos":
        st.markdown('<div class="abg-tab-header">Cartera de Causas</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Registro y seguimiento de causas activas</div>', unsafe_allow_html=True)

        col_form, col_list = st.columns([1, 1.6])

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
                notas    = st.text_area("Notas iniciales", key="abg_caso_notas", height=80)

                if st.button("Guardar Causa", use_container_width=True, type="primary"):
                    if rol and partes:
                        nuevo = {
                            "id":       f"caso_{len(st.session_state.abg_casos)+1}",
                            "rol":      rol,
                            "tribunal": tribunal,
                            "partes":   partes,
                            "materia":  materia,
                            "estado":   estado.lower(),
                            "notas":    notas,
                            "horas":    0.0,
                            "fecha":    datetime.date.today().isoformat(),
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
                    '<div style="text-align:center;padding:3rem 1rem;'
                    'color:#a09070;font-size:0.85rem;">'
                    '📁 Aún no hay causas registradas.<br>'
                    '<span style="font-size:0.72rem;">Agrega tu primera causa a la izquierda.</span>'
                    '</div>', unsafe_allow_html=True)
            else:
                for c in reversed(casos):
                    badge_cls = {"activo":"badge-activo","pendiente":"badge-pendiente","cerrado":"badge-cerrado"}.get(c["estado"],"badge-pendiente")
                    horas_str = f"{st.session_state.abg_timer_acum.get(c['id'],0)/3600:.1f}h"
                    st.markdown(f"""
                    <div class="abg-card">
                      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                        <div class="abg-card-title">{c['rol']} — {c['partes'][:40]}</div>
                        <span class="abg-badge {badge_cls}">{c['estado']}</span>
                      </div>
                      <div style="font-size:0.68rem;color:#a09070;margin-top:4px;">
                        {c['materia']} · {c['tribunal'][:35]} · ⏱ {horas_str}
                      </div>
                      {"<div style='font-size:0.72rem;color:#c8b890;margin-top:6px;'>"+c['notas'][:80]+"…</div>" if c.get('notas') else ""}
                    </div>
                    """, unsafe_allow_html=True)

    # ── CRONÓMETRO ─────────────────────────────────────────────────
    elif tab == "cronometro":
        st.markdown('<div class="abg-tab-header">Cronómetro de Horas</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Registro de tiempo facturable por causa</div>', unsafe_allow_html=True)

        # Selección de causa
        casos_ids = [f"{c['rol']} — {c['partes'][:30]}" for c in st.session_state.abg_casos]
        casos_ids_raw = [c['id'] for c in st.session_state.abg_casos]

        if not casos_ids:
            st.info("Primero registra una causa en la pestaña **Casos**.")
        else:
            sel_display = st.selectbox("Causa activa", ["— selecciona —"] + casos_ids, key="abg_crono_sel")
            caso_idx    = casos_ids.index(sel_display) if sel_display in casos_ids else -1
            caso_id     = casos_ids_raw[caso_idx] if caso_idx >= 0 else ""

        # Display del cronómetro
        on    = st.session_state.abg_timer_on
        start = st.session_state.abg_timer_start
        elapsed = int(time.time() - start) if on and start else 0
        acum    = st.session_state.abg_timer_acum.get(
            st.session_state.abg_timer_caso, 0)

        total_seg = acum + elapsed
        st.markdown(
            f'<div class="abg-timer-display">{_fmt_seconds(total_seg)}</div>',
            unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            if not on:
                if st.button("▶  Iniciar", use_container_width=True, type="primary",
                             disabled=not (casos_ids and caso_id)):
                    st.session_state.abg_timer_on    = True
                    st.session_state.abg_timer_start  = time.time()
                    st.session_state.abg_timer_caso   = caso_id
                    st.rerun()
            else:
                if st.button("⏸  Pausar", use_container_width=True):
                    prev = st.session_state.abg_timer_acum.get(caso_id, 0)
                    st.session_state.abg_timer_acum[caso_id] = prev + elapsed
                    st.session_state.abg_timer_on    = False
                    st.session_state.abg_timer_start  = None
                    st.rerun()
        with col2:
            if st.button("⏹  Reiniciar", use_container_width=True):
                st.session_state.abg_timer_on    = False
                st.session_state.abg_timer_start  = None
                if caso_id:
                    st.session_state.abg_timer_acum[caso_id] = 0
                st.rerun()
        with col3:
            st.button("🔄  Actualizar", use_container_width=True,
                      on_click=lambda: None)  # solo fuerza rerun

        # Resumen horas por causa
        if st.session_state.abg_timer_acum:
            st.markdown('<hr style="border-color:rgba(255,255,255,0.07);margin:1rem 0;">', unsafe_allow_html=True)
            st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.6rem;">Acumulado por causa</div>', unsafe_allow_html=True)
            for c in st.session_state.abg_casos:
                seg = st.session_state.abg_timer_acum.get(c['id'], 0)
                if seg > 0:
                    st.markdown(
                        f'<div class="abg-card" style="padding:0.55rem 0.9rem;">'
                        f'<span style="font-size:0.75rem;color:#f5f0e8;">{c["rol"]}</span>'
                        f'<span style="float:right;font-family:monospace;color:#c9963a;font-size:0.82rem;">'
                        f'{_fmt_seconds(seg)}</span></div>',
                        unsafe_allow_html=True)

    # ── PLAZOS ─────────────────────────────────────────────────────
    elif tab == "plazos":
        st.markdown('<div class="abg-tab-header">Agenda de Plazos</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Vencimientos procesales y audiencias</div>', unsafe_allow_html=True)

        col_form, col_list = st.columns([1, 1.6])

        with col_form:
            with st.expander("➕ Nuevo Plazo", expanded=True):
                desc   = st.text_input("Descripción", placeholder="Contestación demanda", key="abg_pl_desc")
                fecha  = st.date_input("Fecha límite", value=datetime.date.today() + datetime.timedelta(days=7), key="abg_pl_fecha")
                causa  = st.text_input("Causa / ROL", key="abg_pl_causa")
                tipo   = st.selectbox("Tipo", ["Procesal","Audiencia","Escrito","Notificación","Otro"], key="abg_pl_tipo")
                alerta = st.selectbox("Alerta anticipada", ["1 día antes","3 días antes","7 días antes"], key="abg_pl_alerta")

                if st.button("Agregar Plazo", use_container_width=True, type="primary"):
                    if desc and fecha:
                        st.session_state.abg_plazos.append({
                            "desc":   desc,
                            "fecha":  fecha.isoformat(),
                            "causa":  causa,
                            "tipo":   tipo,
                            "alerta": alerta,
                            "done":   False,
                        })
                        st.success("✓ Plazo agregado")
                        st.rerun()
                    else:
                        st.warning("Completa descripción y fecha.")

        with col_list:
            plazos = sorted(
                [p for p in st.session_state.abg_plazos if not p.get("done")],
                key=lambda x: x["fecha"])

            if not plazos:
                st.markdown(
                    '<div style="text-align:center;padding:3rem 1rem;color:#a09070;font-size:0.85rem;">'
                    '📅 Sin plazos pendientes.</div>', unsafe_allow_html=True)
            else:
                hoy = datetime.date.today()
                for i, p in enumerate(plazos):
                    dias = _dias_para(p["fecha"])
                    if dias < 0:
                        cls, color, txt = "abg-plazo-urgent", _RED, f"Venció hace {-dias}d"
                    elif dias == 0:
                        cls, color, txt = "abg-plazo-urgent", _RED, "HOY"
                    elif dias <= 3:
                        cls, color, txt = "abg-plazo-warning", "#fbbf24", f"En {dias} día{'s' if dias != 1 else ''}"
                    else:
                        cls, color, txt = "abg-plazo-ok", _GREEN, f"En {dias} días"

                    col_pl, col_btn = st.columns([5, 1])
                    with col_pl:
                        st.markdown(f"""
                        <div class="abg-card {cls}" style="margin-bottom:0.4rem;">
                          <div style="display:flex;justify-content:space-between;">
                            <div class="abg-card-title">{p['desc']}</div>
                            <span style="font-size:0.7rem;color:{color};font-weight:700;">{txt}</span>
                          </div>
                          <div style="font-size:0.67rem;color:#a09070;margin-top:3px;">
                            {p['tipo']} · {p['fecha']} · {p.get('causa','') or 'Sin causa'}
                          </div>
                        </div>
                        """, unsafe_allow_html=True)
                    with col_btn:
                        orig_idx = st.session_state.abg_plazos.index(p)
                        if st.button("✓", key=f"pl_done_{orig_idx}", help="Marcar cumplido"):
                            st.session_state.abg_plazos[orig_idx]["done"] = True
                            st.rerun()

    # ── CORREOS ────────────────────────────────────────────────────
    elif tab == "correos":
        st.markdown('<div class="abg-tab-header">Redacción de Correos</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Asistencia IA para comunicaciones profesionales</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        with col1:
            destinatario = st.text_input("Destinatario", placeholder="colega, cliente, tribunal, contraparte…", key="abg_correo_dest")
            tono = st.selectbox("Tono", ["Formal", "Cordial", "Firme", "Urgente"], key="abg_correo_tono")
            instrucciones = st.text_area("¿Qué comunicar?",
                height=150,
                placeholder="Ej: Informar al cliente que la audiencia fue fijada para el 15/05/2025 a las 10:00 en el 4° Juzgado Civil. Recordarle que debe traer los documentos que se le indicaron. Confirmar asistencia.",
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
                            resp = llm.generate(prompt, system=" ", max_tokens=800)
                            st.session_state.abg_correo_result = resp
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible en este contexto.")
                else:
                    st.warning("Escribe las instrucciones del correo.")

        with col2:
            if st.session_state.abg_correo_result:
                st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.4rem;">Borrador generado</div>', unsafe_allow_html=True)
                correo_editado = st.text_area("Edita y copia el correo:",
                    value=st.session_state.abg_correo_result,
                    height=350, key="abg_correo_edit")
                if st.button("📋 Copiar al portapapeles", use_container_width=True):
                    st.code(correo_editado, language=None)
                    st.info("Selecciona el texto de arriba para copiarlo.")
            else:
                st.markdown(
                    '<div style="height:280px;display:flex;align-items:center;justify-content:center;'
                    'color:#a09070;font-size:0.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                    '✉️<br>El borrador del correo<br>aparecerá aquí</div>',
                    unsafe_allow_html=True)

    # ── PENDIENTES ─────────────────────────────────────────────────
    elif tab == "pendientes":
        st.markdown('<div class="abg-tab-header">Tareas Pendientes</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Gestor de actividades y seguimientos</div>', unsafe_allow_html=True)

        col_add, col_list = st.columns([1, 1.6])

        with col_add:
            nueva_tarea = st.text_input("Nueva tarea", placeholder="Llamar al perito…", key="abg_task_nueva")
            prioridad   = st.selectbox("Prioridad", ["🔴 Alta","🟡 Media","🟢 Baja"], key="abg_task_prio")
            causa_t     = st.text_input("Causa asociada (opcional)", key="abg_task_causa")
            if st.button("Agregar", use_container_width=True, type="primary"):
                if nueva_tarea:
                    st.session_state.abg_tasks.append({
                        "texto":    nueva_tarea,
                        "prio":     prioridad,
                        "causa":    causa_t,
                        "done":     False,
                        "fecha":    datetime.date.today().isoformat(),
                    })
                    st.rerun()

        with col_list:
            tasks_pend = [t for t in st.session_state.abg_tasks if not t["done"]]
            tasks_done = [t for t in st.session_state.abg_tasks if t["done"]]

            if not tasks_pend:
                st.markdown('<div style="text-align:center;padding:2rem;color:#a09070;font-size:0.85rem;">✅ Sin tareas pendientes.</div>', unsafe_allow_html=True)
            else:
                for i, t in enumerate(tasks_pend):
                    orig_idx = st.session_state.abg_tasks.index(t)
                    col_chk, col_txt = st.columns([0.5, 5])
                    with col_chk:
                        if st.checkbox("", key=f"task_{orig_idx}", value=False):
                            st.session_state.abg_tasks[orig_idx]["done"] = True
                            st.rerun()
                    with col_txt:
                        st.markdown(
                            f'<div style="padding:0.3rem 0;font-size:0.8rem;color:#f5f0e8;">'
                            f'{t["prio"]} {t["texto"]}'
                            + (f'<br><span style="font-size:0.65rem;color:#a09070;">{t["causa"]}</span>' if t.get("causa") else "")
                            + f'</div>', unsafe_allow_html=True)

            if tasks_done:
                with st.expander(f"Completadas ({len(tasks_done)})"):
                    for t in tasks_done:
                        st.markdown(f'<div style="font-size:0.75rem;color:#a09070;text-decoration:line-through;">{t["texto"]}</div>', unsafe_allow_html=True)

    # ── DOCUMENTOS ─────────────────────────────────────────────────
    elif tab == "documentos":
        st.markdown('<div class="abg-tab-header">Generación de Documentos</div>', unsafe_allow_html=True)
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
            detalle = st.text_area("Detalles del documento",
                height=150,
                placeholder="Describe los hechos relevantes, pretensiones, cláusulas especiales, etc.",
                key="abg_doc_detalle")
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
                        f"- Deja campos de completar con [DATO] cuando falta información\n"
                        f"- Anota al final las advertencias o puntos a revisar con el cliente\n"
                        f"- Este es un BORRADOR, el abogado debe revisarlo y ajustarlo"
                    )
                    with st.spinner("Generando borrador…"):
                        try:
                            llm = get_llm_fn()
                            resp = llm.generate(prompt, system=" ", max_tokens=1500)
                            st.session_state.abg_doc_result = resp
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Agrega los detalles del documento.")

        with col2:
            if st.session_state.abg_doc_result:
                st.markdown('<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.4rem;">Borrador generado</div>', unsafe_allow_html=True)
                doc_edit = st.text_area("Edita el borrador:",
                    value=st.session_state.abg_doc_result,
                    height=420, key="abg_doc_edit")
                st.caption("⚠️ Este borrador es orientativo. Revisa y adapta antes de presentar.")
            else:
                st.markdown(
                    '<div style="height:350px;display:flex;align-items:center;justify-content:center;'
                    'color:#a09070;font-size:0.82rem;text-align:center;'
                    'border:1px dashed rgba(201,150,58,0.15);border-radius:8px;">'
                    '📄<br>El borrador del documento<br>aparecerá aquí</div>',
                    unsafe_allow_html=True)

    # ── HONORARIOS ─────────────────────────────────────────────────
    elif tab == "honorarios":
        st.markdown('<div class="abg-tab-header">Honorarios</div>', unsafe_allow_html=True)
        st.markdown('<div class="abg-tab-sub">Control de devengamiento y propuestas de honorarios</div>', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1.3])

        with col1:
            st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.6rem;">Registrar honorario</div>', unsafe_allow_html=True)
            causa_h    = st.text_input("Causa / ROL", key="abg_hon_causa")
            concepto   = st.text_input("Concepto", placeholder="Audiencia preparatoria", key="abg_hon_concepto")
            monto      = st.number_input("Monto (CLP)", min_value=0, step=10000, key="abg_hon_monto")
            estado_h   = st.selectbox("Estado", ["Propuesto","Aceptado","Devengado","Cobrado","Pagado"], key="abg_hon_estado")

            if st.button("Registrar", use_container_width=True, type="primary"):
                if causa_h and concepto and monto > 0:
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
                    st.warning("Completa todos los campos.")

            st.markdown('<hr style="border-color:rgba(255,255,255,0.07);margin:1rem 0;">', unsafe_allow_html=True)

            # Propuesta de honorarios con IA
            st.markdown('<div style="font-size:0.7rem;font-weight:700;color:#a09070;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.6rem;">Generar propuesta con IA</div>', unsafe_allow_html=True)
            tipo_causa_h = st.text_input("Tipo de causa", placeholder="Divorcio unilateral, Santiago", key="abg_hon_tipo")
            complejidad  = st.selectbox("Complejidad", ["Baja","Media","Alta","Muy alta"], key="abg_hon_comp")
            experiencia  = st.text_area("Servicios incluidos",
                height=80,
                placeholder="Ej: Tramitación completa hasta sentencia, incluye 3 audiencias y recursos",
                key="abg_hon_svcs")

            if st.button("💰 Generar Propuesta", use_container_width=True):
                if tipo_causa_h and get_llm_fn:
                    prompt = (
                        f"Eres un abogado chileno con experiencia en honorarios profesionales.\n"
                        f"Genera una propuesta de honorarios para:\n"
                        f"Tipo de causa: {tipo_causa_h}\n"
                        f"Complejidad: {complejidad}\n"
                        f"Servicios: {experiencia}\n\n"
                        f"Incluye:\n"
                        f"1. Honorario total sugerido (en UF y CLP aproximado)\n"
                        f"2. Desglose por etapas procesales\n"
                        f"3. Forma de pago sugerida\n"
                        f"4. Qué está incluido y qué no\n"
                        f"5. Observaciones\n"
                        f"Basa los montos en aranceles referenciales del Colegio de Abogados de Chile y práctica habitual del mercado."
                    )
                    with st.spinner("Generando propuesta…"):
                        try:
                            llm = get_llm_fn()
                            resp = llm.generate(prompt, system=" ", max_tokens=1000)
                            st.session_state.abg_hon_propuesta = resp
                        except Exception as e:
                            st.error(f"Error: {e}")
                elif not get_llm_fn:
                    st.warning("LLM no disponible.")
                else:
                    st.warning("Describe el tipo de causa.")

        with col2:
            # Resumen financiero
            hons = st.session_state.abg_honorarios
            if hons:
                total_propuesto = sum(h["monto"] for h in hons if h["estado"] == "Propuesto")
                total_devengado = sum(h["monto"] for h in hons if h["estado"] in ("Devengado","Aceptado"))
                total_cobrado   = sum(h["monto"] for h in hons if h["estado"] == "Cobrado")
                total_pagado    = sum(h["monto"] for h in hons if h["estado"] == "Pagado")

                c1, c2 = st.columns(2)
                c1.metric("Devengado", f"${total_devengado:,.0f}")
                c2.metric("Cobrado",   f"${total_cobrado:,.0f}")
                c1.metric("Pagado",    f"${total_pagado:,.0f}")
                c2.metric("Propuesto", f"${total_propuesto:,.0f}")

                st.markdown('<hr style="border-color:rgba(255,255,255,0.07);margin:0.8rem 0;">', unsafe_allow_html=True)
                for h in reversed(hons):
                    color_map = {
                        "Pagado":"#22c55e","Cobrado":"#3b82f6",
                        "Devengado":"#c9963a","Aceptado":"#fbbf24","Propuesto":"#a09070"
                    }
                    color = color_map.get(h["estado"], "#a09070")
                    st.markdown(f"""
                    <div class="abg-card" style="padding:0.55rem 0.9rem;">
                      <div style="display:flex;justify-content:space-between;">
                        <div style="font-size:0.77rem;color:#f5f0e8;">{h['causa']} — {h['concepto'][:35]}</div>
                        <div style="font-size:0.77rem;color:{color};font-weight:700;">${h['monto']:,.0f}</div>
                      </div>
                      <div style="font-size:0.64rem;color:#a09070;">{h['estado']} · {h['fecha']}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                if st.session_state.abg_hon_propuesta:
                    st.markdown(
                        '<div style="font-size:0.68rem;color:#a09070;text-transform:uppercase;'
                        'letter-spacing:0.06em;margin-bottom:0.4rem;">Propuesta generada</div>',
                        unsafe_allow_html=True)
                    st.markdown(
                        f'<div class="abg-card" style="font-size:0.78rem;color:#e8d8b8;line-height:1.6;">'
                        f'{st.session_state.abg_hon_propuesta.replace(chr(10),"<br>")}</div>',
                        unsafe_allow_html=True)
                else:
                    st.markdown(
                        '<div style="text-align:center;padding:3rem 1rem;color:#a09070;font-size:0.85rem;">'
                        '💰 Registra honorarios o genera una propuesta con IA.</div>',
                        unsafe_allow_html=True)

            if st.session_state.abg_hon_propuesta and hons:
                with st.expander("Ver propuesta de honorarios generada"):
                    st.markdown(
                        f'<div style="font-size:0.78rem;color:#e8d8b8;line-height:1.6;">'
                        f'{st.session_state.abg_hon_propuesta.replace(chr(10),"<br>")}</div>',
                        unsafe_allow_html=True)
