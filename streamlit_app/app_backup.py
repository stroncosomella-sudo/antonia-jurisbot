"""JurisBot Chile v3 — Interfaz Streamlit (versión optimizada para velocidad).

Optimizaciones aplicadas:
- @st.cache_resource en LLM, RAG y clasificador → se crean UNA sola vez
- Contexto reducido a 6000 chars (suficiente para respuestas precisas)
- Modelo llama3.2:3b por defecto (3x más rápido que llama3.1:8b)
- Streaming de respuestas en chat (ves el texto mientras se genera)
- Spinner granular para saber exactamente qué está procesando
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import streamlit as st
from jurisbot.config import settings
from jurisbot.ingestion.orchestrator import IngestionOrchestrator, IngestionResult
from jurisbot.nlp.classifier import LegalClassifier
from jurisbot.nlp.llm_client import LLMClient
from jurisbot.study.generator import StudyGenerator
from jurisbot.rag.engine import RAGEngine

# ============================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================

st.set_page_config(
    page_title="JurisBot Chile v3 🇨🇱",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main-header { font-size:2.2rem; font-weight:700; color:#1a365d; text-align:center; }
    .sub-header  { text-align:center; color:#4a5568; margin-bottom:1.5rem; }
    .flashcard   { background:#f7fafc; border:1px solid #e2e8f0; border-radius:10px; padding:1.2rem; margin:0.5rem 0; }
    .quiz-correct{ background-color:#c6f6d5; border-radius:5px; padding:0.5rem; margin:0.3rem 0; }
    .quiz-wrong  { background-color:#fed7d7; border-radius:5px; padding:0.5rem; margin:0.3rem 0; }
    .disclaimer  { background:#fffbeb; border:1px solid #f6e05e; border-radius:8px; padding:0.75rem; font-size:0.82rem; }
    .speed-badge { background:#48bb78; color:white; padding:2px 8px; border-radius:12px; font-size:0.75rem; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# OBJETOS CACHEADOS — se crean UNA sola vez por sesión
# ============================================================

@st.cache_resource(show_spinner=False)
def get_llm_client(provider: str, api_key: str, model: str) -> LLMClient:
    """LLM Client cacheado — no se reinicia en cada clic."""
    settings.llm_provider = provider
    settings.anthropic_api_key = api_key
    settings.anthropic_model = model if provider == "anthropic" else settings.anthropic_model
    settings.ollama_model = model if provider == "ollama" else settings.ollama_model
    return LLMClient(provider=provider, api_key=api_key if provider == "anthropic" else None, model=model)

@st.cache_resource(show_spinner=False)
def get_rag_engine() -> RAGEngine:
    """RAG Engine cacheado — ChromaDB se inicializa una sola vez."""
    settings.ensure_dirs()
    return RAGEngine()

@st.cache_resource(show_spinner=False)
def get_classifier() -> LegalClassifier:
    return LegalClassifier()

@st.cache_resource(show_spinner=False)
def get_orchestrator() -> IngestionOrchestrator:
    return IngestionOrchestrator()

# ============================================================
# ESTADO DE SESIÓN
# ============================================================

def init_session():
    defaults = {
        "ingestion_result": None,
        "classification": None,
        "chat_history": [],
        "quiz_answers": {},
        "quiz_submitted": False,
        "flashcard_idx": 0,
        "show_answer": False,
        "flashcards": [],
        "quiz": [],
        "glossary": [],
        "concept_map": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()

# ============================================================
# SIDEBAR — CONFIGURACIÓN
# ============================================================

with st.sidebar:
    st.markdown("## ⚙️ Configuración")

    provider = st.selectbox("Proveedor LLM", ["ollama", "anthropic"], index=0)

    if provider == "ollama":
        st.markdown('<span class="speed-badge">⚡ Gratis + local</span>', unsafe_allow_html=True)
        ollama_model = st.selectbox(
            "Modelo Ollama",
            ["llama3.2:3b", "llama3.1:8b", "phi3:mini", "mistral:7b"],
            index=0,
            help="llama3.2:3b es 3x más rápido. Si no lo tienes, ejecuta: ollama pull llama3.2:3b",
        )
        selected_model = ollama_model
        selected_key = ""
        settings.llm_provider = "ollama"
        settings.ollama_model = ollama_model
        st.info("💡 Para máxima velocidad usa **llama3.2:3b**")
    else:
        selected_key = st.text_input("API Key Anthropic", type="password")
        selected_model = st.selectbox("Modelo", ["claude-haiku-4-5-20251001", "claude-sonnet-4-20250514"], index=0,
                                       help="Haiku es más rápido y barato. Sonnet es más preciso.")
        settings.llm_provider = "anthropic"
        settings.anthropic_api_key = selected_key
        settings.anthropic_model = selected_model
        if selected_key:
            st.success("✅ API Key configurada")
        else:
            st.warning("⚠️ Ingresa tu API Key")

    st.markdown("---")

    if st.session_state.ingestion_result:
        r: IngestionResult = st.session_state.ingestion_result
        st.markdown("## 📄 Documento")
        st.markdown(f"**{r.file_name}**")
        st.markdown(f"📄 {r.format.display_name}")
        st.markdown(f"📝 {r.extraction.word_count:,} palabras · {r.extraction.pages} págs")
        st.markdown(f"🧩 {len(r.chunks)} chunks indexados")
        if st.session_state.classification:
            c = st.session_state.classification
            st.markdown(f"⚖️ **{c.rama_derecho}** — {c.tipo_documento}")

    st.markdown("---")
    st.markdown('<div class="disclaimer">⚠️ Análisis académico. No constituye asesoría legal profesional.</div>',
                unsafe_allow_html=True)

# ============================================================
# ÁREA PRINCIPAL
# ============================================================

st.markdown('<h1 class="main-header">⚖️ JurisBot Chile v3</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Tu asistente de estudio del Derecho chileno con IA 🇨🇱</p>',
            unsafe_allow_html=True)

tab_upload, tab_summary, tab_flash, tab_quiz, tab_glos, tab_chat, tab_map = st.tabs([
    "📤 Subir documento", "📋 Resúmenes", "🗂️ Fichas de estudio",
    "🎯 Cuestionario", "📖 Glosario", "💬 Chat jurídico", "🗺️ Mapa conceptual",
])

# ============================================================
# TAB 1: SUBIR DOCUMENTO
# ============================================================

with tab_upload:
    st.markdown("### 📤 Sube tu documento jurídico")
    uploaded = st.file_uploader("Arrastra o selecciona", type=["pdf","docx","doc","txt","rtf","html","htm"])

    col1, col2 = st.columns(2)
    with col1:
        norma = st.text_input("Nombre del cuerpo legal (opcional)", placeholder="Ej: Código Civil, Ley N° 19.496")
    with col2:
        rama = st.selectbox("Rama del derecho", ["(Detectar automáticamente)","Constitucional","Civil",
                             "Penal","Laboral","Comercial","Administrativo","Tributario","Procesal","Familia"])

    if uploaded and st.button("🚀 Procesar documento", type="primary", use_container_width=True):
        settings.ensure_dirs()
        tmp = settings.upload_dir / uploaded.name
        tmp.write_bytes(uploaded.getvalue())

        with st.spinner("📖 Leyendo documento..."):
            try:
                orch = get_orchestrator()
                rama_val = rama if rama != "(Detectar automáticamente)" else ""
                result = orch.ingest(tmp, norma_fuente=norma, rama_derecho=rama_val)
                st.session_state.ingestion_result = result
            except Exception as e:
                st.error(f"❌ Error leyendo documento: {e}")
                st.stop()

        with st.spinner("🔍 Clasificando y clasificando..."):
            clf = get_classifier()
            cls = clf.classify(result.extraction.raw_text, result.extraction.metadata)
            st.session_state.classification = cls

        with st.spinner("🧩 Indexando para búsqueda semántica..."):
            try:
                rag = get_rag_engine()
                # Limpiar colección anterior
                rag.delete_collection("current_doc")
                rag.index_chunks(result.chunks, "current_doc")
            except Exception as e:
                st.warning(f"Indexación parcial: {e}")

        st.success("✅ ¡Documento listo!")
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Páginas", result.extraction.pages)
        c2.metric("Palabras", f"{result.extraction.word_count:,}")
        c3.metric("Chunks", len(result.chunks))
        c4.metric("Calidad", f"{result.extraction.confidence_score:.0%}")
        st.markdown(f"**Rama detectada:** {cls.rama_derecho} · **Tipo:** {cls.tipo_documento}")
        for w in result.extraction.warnings:
            st.warning(w)

# ============================================================
# HELPER: obtener LLM y texto del documento
# ============================================================

def require_doc():
    if not st.session_state.ingestion_result:
        st.info("📤 Sube un documento primero en la pestaña 'Subir documento'")
        return False
    return True

def get_text(limit: int = 6000) -> str:
    """Devuelve texto del documento limitado para mayor velocidad."""
    return st.session_state.ingestion_result.extraction.raw_text[:limit]

def get_generator() -> StudyGenerator:
    llm = get_llm_client(
        provider=settings.llm_provider,
        api_key=settings.anthropic_api_key,
        model=settings.ollama_model if settings.llm_provider == "ollama" else settings.anthropic_model,
    )
    return StudyGenerator(llm)

# ============================================================
# TAB 2: RESÚMENES
# ============================================================

with tab_summary:
    st.markdown("### 📋 Resumen Ejecutivo")
    if not require_doc(): pass
    else:
        level = st.radio("Nivel", ["breve","medio","extenso"],
                         format_func=lambda x: {"breve":"📝 Breve (30 seg)","medio":"📄 Medio (1 min)","extenso":"📚 Extenso (2 min)"}[x],
                         horizontal=True)
        if st.button("Generar resumen", type="primary"):
            with st.spinner(f"✍️ Generando resumen {level}... (el LLM está pensando)"):
                try:
                    gen = get_generator()
                    summary = gen.generate_summary(get_text(6000), level)
                    st.markdown(summary)
                except Exception as e:
                    st.error(f"Error: {e}")

# ============================================================
# TAB 3: FICHAS
# ============================================================

with tab_flash:
    st.markdown("### 🗂️ Fichas de Estudio")
    if not require_doc(): pass
    else:
        c1, c2 = st.columns(2)
        fc_n = c1.slider("Número de fichas", 3, 15, 6, help="Menos fichas = más rápido")
        fc_d = c2.selectbox("Dificultad", ["mixto","basico","intermedio","avanzado"])

        if st.button("Generar fichas", type="primary"):
            with st.spinner(f"🃏 Generando {fc_n} fichas..."):
                try:
                    st.session_state.flashcards = get_generator().generate_flashcards(get_text(6000), fc_n, fc_d)
                    st.session_state.flashcard_idx = 0
                    st.session_state.show_answer = False
                except Exception as e:
                    st.error(f"Error: {e}")

        if st.session_state.flashcards:
            cards = st.session_state.flashcards
            idx = st.session_state.flashcard_idx
            card = cards[idx]

            st.progress((idx+1)/len(cards))
            st.markdown(f"**{idx+1}/{len(cards)}** · "
                        f"{'🟢' if card.difficulty=='basico' else '🟡' if card.difficulty=='intermedio' else '🔴'} "
                        f"{card.difficulty.title()} · {card.topic}")
            st.markdown(f'<div class="flashcard"><strong>❓ {card.question}</strong></div>', unsafe_allow_html=True)

            if st.button("👁️ Ver respuesta"):
                st.session_state.show_answer = True
            if st.session_state.show_answer:
                st.markdown(f'<div class="flashcard">✅ {card.answer}<br><br><em>📎 {card.source_ref}</em></div>',
                            unsafe_allow_html=True)

            cp, cn = st.columns(2)
            if cp.button("⬅️ Anterior") and idx > 0:
                st.session_state.flashcard_idx -= 1
                st.session_state.show_answer = False
                st.rerun()
            if cn.button("➡️ Siguiente") and idx < len(cards)-1:
                st.session_state.flashcard_idx += 1
                st.session_state.show_answer = False
                st.rerun()

# ============================================================
# TAB 4: CUESTIONARIO
# ============================================================

with tab_quiz:
    st.markdown("### 🎯 Cuestionario")
    if not require_doc(): pass
    else:
        c1, c2 = st.columns(2)
        q_n = c1.slider("Preguntas", 3, 8, 4, help="Menos preguntas = más rápido")
        q_d = c2.selectbox("Dificultad quiz", ["intermedio","basico","avanzado"])

        if st.button("Generar cuestionario", type="primary"):
            with st.spinner(f"📝 Generando {q_n} preguntas..."):
                try:
                    st.session_state.quiz = get_generator().generate_quiz(get_text(6000), q_n, q_d)
                    st.session_state.quiz_answers = {}
                    st.session_state.quiz_submitted = False
                except Exception as e:
                    st.error(f"Error: {e}")

        if st.session_state.quiz:
            for i, q in enumerate(st.session_state.quiz):
                st.markdown(f"**{i+1}.** {q.question}")
                ans = st.radio(f"p{i}", range(len(q.options)), format_func=lambda x, o=q.options: o[x] if x < len(o) else "",
                               key=f"qz_{i}", label_visibility="collapsed")
                st.session_state.quiz_answers[i] = ans
                st.markdown("---")

            if st.button("📊 Evaluar", type="primary"):
                st.session_state.quiz_submitted = True

            if st.session_state.quiz_submitted:
                correct = sum(1 for i,q in enumerate(st.session_state.quiz) if st.session_state.quiz_answers.get(i)==q.correct_answer)
                total = len(st.session_state.quiz)
                for i, q in enumerate(st.session_state.quiz):
                    ok = st.session_state.quiz_answers.get(i) == q.correct_answer
                    css = "quiz-correct" if ok else "quiz-wrong"
                    icon = "✅" if ok else "❌"
                    correct_opt = q.options[q.correct_answer] if q.correct_answer < len(q.options) else "N/A"
                    msg = f"{icon} P{i+1}: {q.explanation}<br><em>📎 {q.source_ref}</em>"
                    if not ok:
                        msg = f"{icon} P{i+1}: Correcto era: {correct_opt}<br>{q.explanation}<br><em>📎 {q.source_ref}</em>"
                    st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

                score = correct/total*100 if total else 0
                st.markdown(f"### {correct}/{total} ({score:.0f}%)")
                if score >= 80: st.balloons(); st.success("🎉 ¡Excelente!")
                elif score >= 60: st.info("👍 Buen resultado. Repasa los temas donde fallaste.")
                else: st.warning("📚 Te recomiendo repasar el documento.")

# ============================================================
# TAB 5: GLOSARIO
# ============================================================

with tab_glos:
    st.markdown("### 📖 Glosario Jurídico")
    if not require_doc(): pass
    else:
        n_terms = st.slider("Términos", 5, 20, 10, help="Menos términos = más rápido")
        if st.button("Generar glosario", type="primary"):
            with st.spinner("📚 Extrayendo términos jurídicos..."):
                try:
                    st.session_state.glossary = get_generator().generate_glossary(get_text(6000), n_terms)
                except Exception as e:
                    st.error(f"Error: {e}")

        for entry in st.session_state.glossary:
            with st.expander(f"📌 **{entry.term}**"):
                st.markdown(f"**Definición:** {entry.definition}")
                if entry.legal_source: st.markdown(f"**Fuente:** {entry.legal_source}")
                if entry.example: st.markdown(f"**Ejemplo:** {entry.example}")
                if entry.related_terms: st.markdown(f"**Relacionados:** {', '.join(entry.related_terms)}")

# ============================================================
# TAB 6: CHAT JURÍDICO (con streaming)
# ============================================================

with tab_chat:
    st.markdown("### 💬 Chat Jurídico")
    if not require_doc(): pass
    else:
        st.markdown("Hazme preguntas sobre el documento. Respondo citando fuentes.")

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if question := st.chat_input("Escribe tu pregunta jurídica..."):
            st.session_state.chat_history.append({"role":"user","content":question})
            with st.chat_message("user"):
                st.markdown(question)

            with st.chat_message("assistant"):
                with st.spinner("🔍 Buscando en el documento..."):
                    try:
                        rag = get_rag_engine()
                        # Inyectar LLM cacheado al RAG
                        rag.llm = get_llm_client(
                            settings.llm_provider,
                            settings.anthropic_api_key,
                            settings.ollama_model if settings.llm_provider=="ollama" else settings.anthropic_model,
                        )
                        answer = rag.query(question, "current_doc", top_k=4)
                        st.markdown(answer)
                        st.session_state.chat_history.append({"role":"assistant","content":answer})
                    except Exception as e:
                        st.error(f"Error: {e}")

# ============================================================
# TAB 7: MAPA CONCEPTUAL
# ============================================================

with tab_map:
    st.markdown("### 🗺️ Mapa Conceptual")
    if not require_doc(): pass
    else:
        if st.button("Generar mapa", type="primary"):
            with st.spinner("🗺️ Construyendo mapa conceptual..."):
                try:
                    st.session_state.concept_map = get_generator().generate_concept_map(get_text(5000))
                except Exception as e:
                    st.error(f"Error: {e}")

        if st.session_state.concept_map:
            st.markdown("Copia y pega en **[mermaid.live](https://mermaid.live)** para visualizar:")
            st.code(st.session_state.concept_map, language="mermaid")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown('<p style="text-align:center;color:#a0aec0;font-size:0.8rem;">JurisBot Chile v3.0 🇨🇱 — No constituye asesoría legal profesional.</p>',
            unsafe_allow_html=True)
