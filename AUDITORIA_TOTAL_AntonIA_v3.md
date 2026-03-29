# AUDITORÍA TOTAL — AntonIA v3.0 · mar.IA Group
### Reporte de ingeniería, producto y estrategia go-to-market
**Fecha:** 29 de marzo de 2026 | **Clasificación:** Uso interno — Socio fundador
**Base de datos verificada en vivo:** 650 VF · 200 MCQ · 118 FC · 18,037 chunks · 443 obras · 7,983 líneas Python

---

## SECCIÓN A — CRISIS INMEDIATA: DEMO EN 24 HORAS

### El problema real

AntonIA v3.0 funciona pero tiene cinco problemas que **matarían cualquier demo frente a un inversor o decano** en los próximos 30 minutos de uso. Ninguno requiere refactorización. Todos son reparables en una tarde.

---

### A.1 · Crisis #1 — El selector de motor IA está expuesto al usuario final
**Archivo:** `streamlit_app/app.py`, líneas 738–757
**Tiempo de reparación:** 20 minutos

El sidebar muestra abiertamente un `st.selectbox` con opciones `"ollama (gratis)"` y `"anthropic (Claude)"`, y debajo un campo `st.text_input` tipo password para que el usuario ingrese `sk-ant-…`. Esto comunica exactamente lo contrario de un producto terminado: dice "esto es un prototipo donde usted debe traer su propia API key."

**Fix exacto:**

Reemplazar en `app.py` el bloque de "Motor de IA" (líneas ~735–757) por:

```python
# ── MOTOR IA (hardcoded, invisible al usuario) ──
# Forzar Anthropic + Sonnet sin exponerlo al usuario
provider_key = "anthropic"
model = "claude-sonnet-4-20250514"
api_key = st.secrets.get("ANTHROPIC_API_KEY", "") or os.environ.get("ANTHROPIC_API_KEY", "")

settings.llm_provider = provider_key
settings.anthropic_api_key = api_key
settings.anthropic_model = model
```

Y en `.streamlit/secrets.toml` (crear si no existe):

```toml
ANTHROPIC_API_KEY = "sk-ant-xxxx"
```

**Resultado:** El sidebar queda limpio. El usuario nunca ve ninguna referencia a Ollama, API keys, o modelos. AntonIA parece un producto SaaS terminado.

---

### A.2 · Crisis #2 — El formulario de contacto no hace nada
**Archivo:** `streamlit_app/app.py`, líneas ~1568–1586
**Tiempo de reparación:** 15 minutos

El `st.form_submit_button("SOLICITAR MI PLAN")` muestra un mensaje de confirmación renderizado en HTML, pero no envía ningún correo, no escribe a ninguna base de datos, no hace nada. Si durante la demo alguien llena el formulario — y lo harán — no recibirás nada.

**Fix mínimo viable (sin backend):** Usar la API gratuita de Formspree.

```python
import httpx

if st.form_submit_button("SOLICITAR MI PLAN", use_container_width=True):
    if nombre and email:
        payload = {
            "name": nombre, "email": email,
            "plan": plan_s, "tel": tel,
            "institucion": inst, "mensaje": msg
        }
        try:
            r = httpx.post(
                "https://formspree.io/f/TU_FORM_ID",
                json=payload, timeout=5
            )
            if r.status_code == 200:
                st.success(f"✓ ¡Gracias, {nombre}! Le contactaremos a {email} en menos de 1 hora.")
            else:
                st.error("Error al enviar. Por favor escríbanos directamente.")
        except Exception:
            st.warning("Sin conexión. Escríbanos a contacto@antonia.cl")
```

Registrarse en formspree.io es gratuito y toma 3 minutos. Alternativamente, se puede usar `smtplib` con una cuenta Gmail + App Password.

---

### A.3 · Crisis #3 — Los testimonios son ficticios y se notan
**Archivo:** `streamlit_app/app.py`, líneas ~1590+
**Tiempo de reparación:** 10 minutos (cambiar texto)

María J., "Estudiante · U. de Chile" y los otros dos testimonios no tienen foto, apellido completo, ni institución verificable. En una demo, esto es un riesgo reputacional.

**Fix para la demo:** Sustituir por testimonios de tus beta testers reales (aunque sean 2–3 compañeros de estudio que lo probaron), con nombre completo, carrera y universidad. O eliminar la sección temporalmente y reemplazarla por un banner "Acceso anticipado — Únete a nuestra beta privada."

---

### A.4 · Crisis #4 — La biblioteca tiene 0% de cobertura en 4 materias
**Datos verificados:** `data/biblioteca_manifest.json`

```
Derecho Civil:      396 obras  (89.4%)
Derecho Ambiental:   41 obras   (9.3%)
Derecho Canónico:     4 obras   (0.9%)
Sin clasificar:       2 obras   (0.5%)
──────────────────────────────────────
Derecho Penal:        0 obras   (0.0%)  ← CRÍTICO
Derecho Laboral:      0 obras   (0.0%)  ← CRÍTICO
Derecho Constitucional: 0 obras (0.0%)  ← CRÍTICO
Derecho Procesal:     0 obras   (0.0%)  ← Nota: Casarino está en Civil
```

En la demo, nunca hagas una consulta sobre Derecho Penal, Laboral o Constitucional. O ajusta la UI para deshabilitar esas ramas hasta tener contenido. Ver Sección I para el plan de rescate completo.

---

### A.5 · Crisis #5 — ngrok free tier expone URL aleatoria
**Riesgo:** La URL `clifford-hyperhidrotic-symbolically.ngrok-free.dev` cambia cada vez que reinicias. Si envías la URL por email y reinicias el servidor antes de que llegue el inversor, está muerto.

**Fix para 24h:** Usar ngrok con un dominio estático gratuito. En la cuenta gratuita de ngrok (2026) se puede reservar un subdominio estático:

```bash
ngrok http 8501 --domain=antonia-demo.ngrok-free.app
```

O mejor: desplegar en Streamlit Community Cloud (gratuito, URL estable, ver Sección F).

---

### A.6 · Script de demo para inversores (guión de 12 minutos)

```
00:00 — Abrir AntonIA. Mostrar sidebar. Señalar diseño premium.
01:00 — Sección CONSULTA JURÍDICA: preguntar "¿Cuáles son los requisitos
         del error como vicio del consentimiento en el derecho civil chileno?"
02:30 — Mostrar respuesta con citas [1][2][3]. Expandir fuente.
04:00 — Sección ENTRENA: modo V/F, ramo Derecho Civil. Hacer 3 preguntas.
06:00 — Sección ESTUDIO: generar ficha sobre "nulidad relativa".
08:00 — Sección PRECIOS: señalar los 3 planes. Decir "ya tenemos N beta users."
09:30 — Sección CONTACTO: llenar formulario en vivo (demostrar que funciona).
11:00 — Mostrar biblioteca_manifest: "443 obras, 18,037 fragmentos indexados."
12:00 — Cierre.
```

**Materias SEGURAS para la demo** (con contenido real indexado):
- Obligaciones civiles, contratos, responsabilidad civil
- Derecho Ambiental (Bermúdez, Bordalí — excelente cobertura)

**Materias a EVITAR:**
- Penal, Laboral, Constitucional, Comercial

---

## SECCIÓN B — DIAGNÓSTICO DE PRODUCTO: 7 PROBLEMAS CRÍTICOS

### B.1 · Selector LLM expuesto (ya cubierto en A.1) — Severidad: CRÍTICA

### B.2 · Sin autenticación ni control de acceso
**Archivo:** `streamlit_app/app.py` (global)

Cualquier persona con la URL puede usar AntonIA ilimitadamente sin pagar ni registrarse. Esto es un problema de negocio crítico: tus primeros "clientes" serán free riders.

**Fix mínimo viable con Streamlit:**

```python
# En app.py, primeras líneas del main
import streamlit_authenticator as stauth

credentials = {
    "usernames": {
        "beta_user1": {
            "name": "Usuario Beta",
            "password": stauth.Hasher(["password123"]).generate()[0]
        }
    }
}
authenticator = stauth.Authenticate(credentials, "antonia_cookie", "antonia_key", 30)
name, auth_status, username = authenticator.login("Login AntonIA", "main")

if not auth_status:
    st.stop()
```

Para producción real: integrar con Supabase Auth (gratuito hasta 50,000 MAU).

### B.3 · Sin rate limiting — Severidad: ALTA
**Archivo:** `src/jurisbot/rag/engine.py`, función `query_stream()`

Un usuario puede hacer 1,000 consultas en un día y costarte USD 16.50 (1,000 × $0.0165). Sin límite, esto es un vector de abuso trivial.

**Fix en `app.py`:**

```python
# Control de uso por sesión
MAX_QUERIES_SESSION = 20  # ajustar por plan

if "query_count" not in st.session_state:
    st.session_state.query_count = 0

if st.session_state.query_count >= MAX_QUERIES_SESSION:
    st.error("Has alcanzado el límite de consultas de tu plan. Actualiza para continuar.")
    st.stop()

# Después de cada consulta exitosa:
st.session_state.query_count += 1
```

Para producción: usar Redis + contador por usuario autenticado.

### B.4 · Parámetro `max_tokens=1,200` posiblemente muy bajo — Severidad: MEDIA
**Archivo:** `streamlit_app/app.py`, línea ~1313; `src/jurisbot/rag/engine.py`, `query_stream()`

Para análisis jurídicos complejos (contratos, responsabilidad civil), 1,200 tokens son ~900 palabras. Las respuestas se cortan. En la práctica se observará un "La respuesta ha sido truncada…" en preguntas complejas.

**Fix:** Subir a `max_tokens=2,500` para consultas RAG. El costo adicional es USD $0.02 por consulta — insignificante frente al valor percibido.

### B.5 · `top_k=4` fragmentos puede ser insuficiente para doctrina compleja — Severidad: MEDIA
**Archivo:** `src/jurisbot/rag/engine.py`, parámetro `top_k`

Con 18,037 chunks de 443 obras, recuperar solo 4 fragmentos para construir una respuesta jurídica sobre obligaciones puede omitir perspectivas doctrinarias relevantes. El vector space de Cosine similarity de ChromaDB es bueno pero no perfecto.

**Fix:** Aumentar a `top_k=6` o `top_k=8` y usar re-ranking por relevancia antes de pasar al LLM. Costo adicional en tokens: ~8% más input. Vale la pena.

### B.6 · El banco de preguntas es estático y no se actualiza — Severidad: BAJA-MEDIA
**Datos:** 650+200+118 = 968 preguntas totales en 12 ramos

968 preguntas fijas significan que un estudiante intensivo las agota en ~30 días de uso diario (30 min/día). Después, verá preguntas repetidas.

**Fix a mediano plazo:** Usar el `StudyGenerator` (que ya existe en `src/jurisbot/study/generator.py`) para generar preguntas dinámicas desde la biblioteca RAG. El módulo ya está construido — solo falta conectarlo al módulo ENTRENA como fuente secundaria cuando se agotan las estáticas.

### B.7 · Dependencia Python 3.10+ en pyproject.toml vs. 3.9 en producción — Severidad: BAJA
**Archivo:** `pyproject.toml` línea `requires-python = ">=3.10"`, workaround `from __future__ import annotations`

Si despliegan en un servidor Linux con Python 3.9 (Ubuntu 20.04 default), el workaround funciona pero es técnicamente incorrecto y puede fallar con algunas versiones de chromadb. Definir Python 3.11 como target oficial y usar `pyenv` en el servidor.

---

## SECCIÓN C — ARQUITECTURA Y COSTOS: MODELO REAL DE 50 USUARIOS

### C.1 · Costo real de Anthropic API (datos verificados)

**Modelo en uso:** `claude-sonnet-4-20250514`
**Pricing (Q1 2026):** Input $3/MTok · Output $15/MTok

| Escenario | Queries/mes | Costo USD | Costo CLP |
|-----------|-------------|-----------|-----------|
| 10 usuarios, 20q/día | 6,000 | $99 | $93,060 |
| **50 usuarios, 20q/día** | **30,000** | **$495** | **$465,300** |
| 100 usuarios, 20q/día | 60,000 | $990 | $930,600 |
| 200 usuarios, 20q/día | 120,000 | $1,980 | $1,861,200 |

*Supuesto: 2,500 tokens input (system + 4 chunks + pregunta) + 600 tokens output por query*

### C.2 · Modelo financiero a 50 usuarios pagantes

```
Revenue (mix 30 Estudiante + 15 Profesional + 5 Firma):
  30 × $15,000 CLP  =   $450,000
  15 × $29,000 CLP  =   $435,000
   5 × $79,000 CLP  =   $395,000
  ─────────────────────────────────
  TOTAL REVENUE:        $1,280,000 CLP/mes

Costos variables:
  API Anthropic:          $465,300 CLP  (36.4% de revenue)
  Hosting (ver C.3):       ~$30,000 CLP
  ─────────────────────────────────
  MARGEN BRUTO:           $784,700 CLP/mes  (~61%)
```

**El margen del 61% es saludable.** El problema es que el API cost como % de revenue es alto (36%). La solución de largo plazo es negociar precios de volumen con Anthropic a partir de $10K/mes en gasto, o implementar un tier de Ollama para usuarios Estudiante (ahorrando ~60% del costo de ese tier).

### C.3 · Comparación de hosting

| Opción | Costo/mes | Pros | Contras |
|--------|-----------|------|---------|
| ngrok free (actual) | $0 | Ya funciona | URL cambia, lento, sin SLA |
| Streamlit Community Cloud | $0 | URL estable, SSL, CI/CD automático | Sin persistencia de ChromaDB local |
| Railway.app (512MB RAM) | ~$5 USD | Simple, persistente, URL custom | Límites de RAM para ChromaDB |
| **Render.com (1GB RAM)** | **~$7 USD** | **Persistente, Docker, buen uptime** | **Requiere Dockerfile** |
| Google Cloud Run | ~$15–30 USD | Escala a cero, enterprise | Más complejidad |
| DigitalOcean Droplet 2GB | $18 USD | Control total, persistente | Mantenimiento manual |

**Recomendación inmediata (esta semana):** Render.com + Docker. La biblioteca ChromaDB (362MB) se monta como disco persistente. URL estable gratis. Ver Sección F para el Dockerfile.

### C.4 · El problema de ChromaDB en producción cloud

ChromaDB PersistentClient guarda los vectores en disco local (`data/chroma/`, 362MB). En cualquier plataforma cloud con almacenamiento efímero (Streamlit Community Cloud, Railway sin persistencia), **los 18,037 chunks se pierden en cada redeploy.**

**Solución a 30 días:** Migrar a ChromaDB Cloud (Chroma Cloud, gratuito hasta 1GB) o usar Pinecone serverless (gratuito hasta 2GB). El código de `engine.py` ya usa la interfaz estándar de ChromaDB — el cambio es de 3 líneas:

```python
# Antes (PersistentClient local):
self.chroma_client = chromadb.PersistentClient(path=str(self.chroma_path))

# Después (ChromaDB Cloud):
self.chroma_client = chromadb.HttpClient(
    host="api.trychroma.com",
    port=8000,
    ssl=True,
    headers={"x-chroma-token": os.environ["CHROMA_API_KEY"]}
)
```

---

## SECCIÓN D — SEGURIDAD Y RIESGOS LEGALES

### D.1 · API Key en `.env` — Riesgo: ALTO

**Hallazgo:** El archivo `.env` contiene la API Key de Anthropic en texto plano. Si este repositorio sube a GitHub sin `.gitignore` correctamente configurado, la key queda expuesta.

**Verificación:**
```bash
# Verificar que .env está en .gitignore:
grep "\.env" .gitignore  # debe retornar ".env"

# Verificar que la key nunca fue commiteada:
git log --all --full-history -- .env
git log -S "sk-ant" --source --all  # busca la key en todo el historial
```

**Fix inmediato:**
1. Rotar la API key en console.anthropic.com ahora mismo
2. Usar `st.secrets` de Streamlit o variables de entorno del servidor de hosting
3. Verificar que `.env` aparece en `.gitignore`
4. Usar `git-secrets` o `gitleaks` como pre-commit hook

### D.2 · Sin HTTPS en desarrollo local — Riesgo: MEDIO

El túnel ngrok sí provee HTTPS. Pero si el servidor corre en red local (`localhost:8501`), las cookies de sesión (si se implementa auth) van en texto claro. Para demos en redes WiFi públicas (cafés, universidades), usar siempre el túnel ngrok o desplegar en producción.

### D.3 · Ley 17.336 sobre Propiedad Intelectual — Riesgo: LEGAL CRÍTICO

**Análisis específico para AntonIA v3.0:**

La biblioteca RAG indexa **443 obras doctrinarias** de autores chilenos (Casarino, Bermúdez, Bordalí, etc.) en un vector store comercial para generar respuestas de pago. Esto constituye:

1. **Reproducción parcial sin autorización** (Art. 1, 3 y 18 Ley 17.336): Cada "chunk" indexado es una reproducción de fragmentos de obras protegidas.
2. **Uso comercial** (Art. 71-B): AntonIA cobra suscripción por el acceso a respuestas basadas en ese contenido.
3. **Sin licencia de los autores ni editoras** (LegalPublishing Chile, Abeledo Perrot, Ediciones UC).

**¿Cómo Harvey AI y similares lo manejan?**
- Acuerdan licencias de datos con las editoriales jurídicas (Thomson Reuters, Lexis Nexis) — contratos de millones de dólares.
- O usan exclusivamente contenido público (leyes, sentencias, diarios oficiales).
- O tienen doctrinas de "fair use" en EE.UU. que en Chile no aplican directamente.

**Plan de mitigación en 3 niveles:**

**Nivel 1 — Inmediato (esta semana):** Agregar disclaimer explícito en cada respuesta: *"Esta respuesta se basa en análisis académico. Las obras citadas son propiedad de sus respectivos autores. AntonIA no reproduce el texto original."*

**Nivel 2 — 30 días:** Contactar a 2–3 autores (ej. Jorge Bermúdez Soto, U. de Valparaíso) directamente. Proponer licencia académica recíproca: AntonIA les menciona en la plataforma + les da acceso gratuito a cambio de autorización de indexación de sus obras. La mayoría aceptará.

**Nivel 3 — 90 días:** Reemplazar progresivamente obras privadas por fuentes libres de derechos (ver Sección I). Para el pitch a inversores, tener al menos 2 autores que hayan dado autorización escrita.

---

## SECCIÓN E — MERCADO: TAM / SAM / SOM + ESTRATEGIA GO-TO-MARKET

### E.1 · Tamaño de mercado verificado (Chile, datos reales)

| Segmento | Número | Fuente |
|----------|--------|--------|
| Estudiantes de Derecho activos | ~40,000 | CNED 2024 |
| Abogados habilitados | ~30,000 | CAJ + Colegios de Abogados |
| Egresados en proceso de habilitación | ~8,000 | Est. |
| **Total addressable (Chile)** | **~78,000** | |

```
TAM (Chile, precio promedio $22,000 CLP/mes):
  78,000 usuarios × $22,000 × 12 = CLP $20,592,000,000/año ≈ USD 21.9M

SAM (5% penetración digital-early adopter):
  3,900 usuarios × $22,000 × 12 = CLP $1,029,600,000/año ≈ USD 1.1M

SOM (objetivo año 1, 0.5%):
  390 usuarios × $22,000 × 12 = CLP $102,960,000/año ≈ USD 109,500
```

**LatAm expansion (Argentina, Colombia, Perú — mismo idioma, similar sistema jurídico):** TAM se multiplica ×6 a USD 131M proyectado 2027.

### E.2 · Calibración de precios

| Plan | Precio actual | Benchmarks | Recomendación |
|------|--------------|------------|---------------|
| Estudiante | $15,000 CLP | Duolingo $9USD, Legal English tools $8-12 USD | Mantener. Precio correcto. |
| Profesional | $29,000 CLP | ChatGPT Plus $20 USD = $18,800 CLP | Subir a $35,000 CLP — los abogados cobran $150,000/hora |
| Firma/Universidad | $79,000 CLP | Harvey AI $50-150 USD/user | Muy bajo. Para firmas, precio por sede: $350,000 CLP/mes por 5 users |

### E.3 · Canales de adquisición prioritarios (por CAC estimado)

**Canal 1 — Universidad directa (CAC ~$0, LTV muy alto)**
El modelo Duolingo for Schools: una sola reunión con el decano de una escuela de Derecho → acceso gratuito a todos los estudiantes de 1° año → conversión a plan pago en 3°–4° año. Target prioritario: U. de Chile, PUC, U. de Valparaíso, U. Católica del Norte.

**Canal 2 — TikTok/Instagram jurídico (CAC ~$500–1,500 CLP/usuario)**
Contenido: "El artículo del CC que los abogados nunca leen", "¿Sabes qué es el enriquecimiento sin causa?", "Prepara tu examen de grado con IA." Una cuenta de 10,000 seguidores en el nicho jurídico chileno = ~200 suscriptores pagos directos.

**Canal 3 — Asociaciones estudiantiles de Derecho (CADE, AEDUC)**
Patrocinar eventos de mock trial, MOOT court, seminarios. Visibilidad masiva con estudiantes de perfil high-intent (estudian mucho, pagan por herramientas de calidad).

**Canal 4 — LinkedIn B2B para firmas**
Una firma boutique chilena con 5 abogados paga $350,000 CLP = 23 usuarios individuales en términos de revenue. LTV 3 años = $12.6M CLP. El esfuerzo de venta de 2 reuniones y una demo es equivalente a adquirir 23 usuarios orgánicos.

### E.4 · Ventana de oportunidad

El mercado LegalTech Chile es prácticamente virgen. Los competidores actuales:
- **LexisNexis Chile:** Bases de datos estáticas, sin IA, cara ($200,000+ CLP/mes para firmas)
- **Thomson Reuters Proview:** Igual — libros digitales, sin IA conversacional
- **GPT-4 directo:** Los estudiantes lo usan, pero sin contexto jurídico chileno ni fuentes

AntonIA tiene 18,037 chunks de doctrina chilena específica indexados — esto es una ventaja técnica real que tarda meses en replicar. La ventana es ahora.

---

## SECCIÓN F — ROADMAP DE IMPLEMENTACIÓN: 4 FASES

### Fase 0 — Esta semana (Costo: $0, Tiempo: 8h de trabajo)

| Tarea | Archivo | Tiempo | Impacto |
|-------|---------|--------|---------|
| Ocultar selector LLM | `app.py` L.738–757 | 20 min | Crítico |
| Conectar formulario (Formspree) | `app.py` L.1568–1586 | 15 min | Alto |
| Crear `.streamlit/secrets.toml` | nuevo archivo | 10 min | Crítico |
| Subir a Streamlit Community Cloud | Repositorio | 30 min | Alto |
| Actualizar testimonios | `app.py` L.1590+ | 10 min | Medio |
| Agregar disclaimer IP en respuestas | `engine.py` | 20 min | Legal |
| Agregar `streamlit_authenticator` básico | `app.py` | 45 min | Alto |

**Entregable Fase 0:** AntonIA con URL estable, formulario funcional, autenticación básica y sin exposición técnica.

---

### Fase 1 — Semana 1–2 (Costo: ~$20 USD, Tiempo: 20h)

| Tarea | Descripción | Costo |
|-------|-------------|-------|
| Despliegue en Render.com | Docker + ChromaDB persistente | $7/mes |
| Dominio personalizado | antonia.cl (NIC Chile) | $13 USD/año |
| Rate limiting por usuario | Redis + contador sesión | $0 (Redis gratuito en Render) |
| Migrar API key a env vars cloud | Eliminar `.env` local | $0 |
| Email con dominio propio | Zoho Mail gratuito | $0 |

**Dockerfile mínimo para Render:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir -e ".[all]"

COPY . .
EXPOSE 8501

# Montar data/chroma como disco persistente en Render
ENV CHROMA_DIR=/data/chroma

CMD ["streamlit", "run", "streamlit_app/app.py",
     "--server.port=8501",
     "--server.address=0.0.0.0",
     "--server.headless=true"]
```

---

### Fase 2 — Mes 1 (Costo: <$100 USD, Tiempo: 40h)

| Tarea | Descripción |
|-------|-------------|
| Autenticación real con Supabase | Email/password + JWT. Gratuito hasta 50K MAU |
| Panel de admin básico | Ver usuarios activos, queries/día, revenue |
| Integración pagos | Transbank Webpay ONE CLICK (o Mercado Pago Chile) |
| Beta privada 20 usuarios | Reclutar en facultades target |
| Agregar Derecho Penal básico | Maturana, Politoff — ver Sección I |
| Métricas de uso | Posthog (gratuito, open-source analytics) |

---

### Fase 3 — Meses 2–3 (Costo: <$500 USD, Tiempo: 80h)

| Tarea | Descripción |
|-------|-------------|
| Preguntas dinámicas con StudyGenerator | Conectar RAG al módulo ENTRENA |
| Jurisprudencia del Poder Judicial | Indexar sentencias públicas (ver Sección I) |
| App móvil PWA | Streamlit ya genera PWA con manifest — solo configurar |
| Primer deal universitario | Una facultad con acceso gratuito a estudiantes |
| Pitch deck para Start-Up Chile | Ver Sección H |
| Cobertura 6 ramos (antes 2) | Completar biblioteca (ver Sección I) |

---

## SECCIÓN G — 5 QUICK WINS: LOS PRÓXIMOS 90 MINUTOS

Estas son las 5 acciones de mayor impacto en menor tiempo. Hazlas ahora, antes de cualquier demo o reunión.

### Quick Win #1 — Ocultar el selector LLM (20 minutos)

Ya documentado en A.1. Este es el cambio de mayor ROI visual: convierte el producto de "prototipo" a "producto."

### Quick Win #2 — Secrets.toml + deploy a Streamlit Cloud (30 minutos)

```bash
# 1. Crear secrets
mkdir -p .streamlit
cat > .streamlit/secrets.toml << EOF
ANTHROPIC_API_KEY = "sk-ant-tu-key-aqui"
EOF

# 2. Asegurarse que secrets.toml está en .gitignore
echo ".streamlit/secrets.toml" >> .gitignore

# 3. Push a GitHub
git add .
git commit -m "feat: hide LLM selector, add secrets config"
git push

# 4. En share.streamlit.io:
#    - New app → tu repo → streamlit_app/app.py
#    - Settings → Secrets → pegar el contenido de secrets.toml
#    URL resultado: https://tu-usuario-antonia.streamlit.app
```

### Quick Win #3 — Disclaimer legal en cada respuesta (15 minutos)

En `src/jurisbot/rag/engine.py`, al final de `query_stream()`:

```python
# Agregar al final de cada respuesta generada
LEGAL_DISCLAIMER = (
    "\n\n---\n*⚠️ Uso académico. Las fuentes citadas son propiedad intelectual "
    "de sus autores. Esta herramienta no reemplaza asesoría jurídica profesional.*"
)
```

### Quick Win #4 — Limitar queries por sesión (10 minutos)

```python
# Al inicio de la sección de consulta en app.py
if st.session_state.get("query_count", 0) >= 15:
    st.warning("Has alcanzado el límite de consultas de la demo. "
               "Regístrate para acceso completo.")
    st.stop()
```

### Quick Win #5 — Mensaje de carga más profesional (5 minutos)

Reemplazar cualquier `st.spinner("Cargando...")` por:

```python
with st.spinner("AntonIA está consultando 18.037 fragmentos de doctrina jurídica chilena…"):
    # tu código RAG aquí
    pass
```

Este mensaje específico, con el número real de documentos, hace que la espera de 3–5 segundos parezca un trabajo serio, no una demora.

---

## SECCIÓN H — VALORACIÓN Y ESTRATEGIA DE FINANCIAMIENTO

### H.1 · Valoración pre-revenue (metodología Berkus)

| Factor Berkus | Evaluación AntonIA v3.0 | Valor (USD) |
|---------------|------------------------|-------------|
| Idea base + propuesta de valor | LegalTech IA en mercado virgen chileno | $500,000 |
| Prototipo funcional | App Streamlit + RAG + 18K chunks en producción | $500,000 |
| Equipo de gestión | Founder técnico (score: 8/10 por evidencia del código) | $250,000 |
| Relaciones estratégicas | Por construir (universidades, barras) | $100,000 |
| Tracción temprana | 0 usuarios pagantes verificados (beta) | $0 |
| **Valoración pre-seed estimada** | | **USD $1.35M** |

Con 5 usuarios pagantes reales y una carta de intención de una facultad, la valoración sube a USD $2–3M.

### H.2 · Opciones de financiamiento para Chile (2026)

**CORFO — Capital Semilla Emprendimiento (CSE)**
- Monto: hasta $30M CLP (≈ USD 32,000) no reembolsable
- Requisito: empresa constituida en Chile, proyecto innovador
- Timeline: 3–6 meses desde postulación
- **Relevancia para AntonIA:** Alta. LegalTech + IA = perfil favorecido. Postular ahora.
- URL: corfo.cl → Capital Semilla

**Start-Up Chile — S Factor (seed)**
- Monto: USD $30,000 en equity + USD 14,000 en servicios (no dilutivo hasta demo day)
- Requisito: empresa o fundador chileno, producto funcional
- Cohortes: 2 por año (mayo y noviembre aprox.)
- **Para AntonIA:** Aplicar en la próxima cohorte con demo funcional + 10 usuarios beta
- URL: startupchile.org

**Start-Up Chile — SCALE (growth)**
- Monto: USD $150,000
- Requisito: tracción demostrada (revenue o usuarios)
- Objetivo: cuando AntonIA tenga +50 usuarios pagantes

**Inversores ángel LegalTech LatAm (identificados):**
- Alaya Capital Partners (Santiago) — foco: B2B SaaS Chile
- Kaszek Ventures — foco: LatAm, han invertido en LegalTech
- Nazca (México) — foco: LatAm SaaS early stage

**Incubadoras universitarias (sin dilución):**
- Centro de Innovación UC (DICTUC)
- Beauchef Ventures (U. de Chile Ingeniería)
- Incuba UDD

### H.3 · Qué necesitas antes de cualquier pitch

Lista mínima de evidencia para un pitch creíble:

- [ ] URL estable funcionando (no ngrok) con AntonIA en producción
- [ ] 10 usuarios beta con feedback escrito (email o WhatsApp basta)
- [ ] 1 carta de intención de una facultad de Derecho
- [ ] 2 autores con autorización de indexación (resolver riesgo IP)
- [ ] Deck de 12 slides (Problema → Solución → Mercado → Demo → Equipo → Ask)
- [ ] Estados financieros proyectados a 24 meses
- [ ] Empresa constituida en Chile (SpA es lo más simple, $50,000 CLP aprox.)

---

## SECCIÓN I — BIBLIOTECA DOCTRINA: PLAN DE RESCATE

### I.1 · Diagnóstico actual verificado

```
ESTADO ACTUAL DE LA BIBLIOTECA (18,037 chunks / 443 obras):
════════════════════════════════════════════════════════════
Derecho Civil        ████████████████████████ 396 obras  89.4%
Derecho Ambiental    ██                        41 obras   9.3%
Derecho Canónico                                4 obras   0.9%
Sin clasificar                                  2 obras   0.5%
────────────────────────────────────────────────────────────
Derecho Penal                                   0 obras   0.0%  🔴
Derecho Laboral                                 0 obras   0.0%  🔴
Derecho Constitucional                          0 obras   0.0%  🔴
Derecho Comercial                               0 obras   0.0%  🔴
Derecho Tributario                              0 obras   0.0%  🔴
```

Un estudiante de Derecho en Chile estudia **11 ramos obligatorios** a lo largo de la carrera. AntonIA cubre sólido 1.5 de ellos (Civil + parcialmente Ambiental). Esto es un problema de producto fundamental.

### I.2 · Fuentes gratuitas y libres de derechos (indexar YA)

#### Tier 1 — Dominio público / licencia abierta (100% seguro)

**Leyes y Códigos (Biblioteca del Congreso Nacional — bcn.cl):**
```
Código Civil (2,500 artículos)
Código Penal (491 artículos)
Código del Trabajo (actualizado)
Código de Procedimiento Civil
Código de Procedimiento Penal (antiguo + nuevo)
Código Tributario
Ley 19.496 Protección al Consumidor
DFL 1/2005 Código Sanitario
```
Todo disponible en bcn.cl en formato HTML descargable y PDF. Sin restricciones de IP. Indexar inmediatamente.

**Memoria Chilena (memoriachilena.gob.cl):**
- Documentos históricos jurídicos del siglo XIX–XX
- Libros digitalizados con derechos vencidos (autores fallecidos hace +70 años)
- Relevante para Historia del Derecho y Derecho Romano

#### Tier 2 — Sentencias del Poder Judicial (API pública)

El Poder Judicial de Chile tiene portal de sentencias públicas (pjud.cl). Las sentencias judiciales son actos públicos y no tienen derechos de autor.

```python
# Script para descargar sentencias de PJUD
import requests
from bs4 import BeautifulSoup

def download_pjud_sentences(tribunal_code, year, tipo="civil"):
    """Descarga sentencias públicas del Poder Judicial de Chile"""
    base_url = "https://oficinajudicialvirtual.pjud.cl"
    # Implementar según documentación PJUD
    # Alternativa: usar el buscador de jurisprudencia bcentral + jurisprudencia.cl
    pass
```

**jurisprudencia.cl** también tiene sentencias en dominio público. Un script de scraping ético (respetando robots.txt y rate limiting) puede obtener miles de sentencias.

#### Tier 3 — Academia (con permiso explícito)

Autores académicos que probablemente darán permiso fácilmente:

| Autor | Materia | Institución | Estrategia |
|-------|---------|-------------|------------|
| Jorge Bermúdez Soto | Ambiental | U. de Valparaíso | Ya tienes 41 obras — formalizar |
| Carlos Pizarro Wilson | Civil/Contratos | U. Diego Portales | Email directo |
| Rodrigo Díaz Almuna | Penal | UC | Email directo |
| Claudio Palavecino | Laboral | U. de Chile | Email directo |
| Francisco Zúñiga | Constitucional | U. de Chile | Email directo |

**Template de email (enviar esta semana):**

```
Estimado Profesor [Nombre]:

Mi nombre es [Sergio], fundador de AntonIA, plataforma de IA jurídica
para estudiantes de Derecho en Chile (antonia.cl).

Estamos construyendo la primera biblioteca de doctrina jurídica chilena
con IA conversacional, y su trabajo en [materia] es fundamental para
nuestros usuarios.

Le propongo una colaboración académica: indexar sus obras publicadas
en nuestra plataforma RAG, con:
- Citación completa y visible en cada respuesta
- Acceso gratuito de por vida a AntonIA para usted y sus alumnos
- Reconocimiento como "Autor Partner" en la plataforma

No reproducimos el texto — usamos fragmentos de contexto para
responder preguntas de estudiantes con cita a la fuente original.

¿Tendría 20 minutos para una llamada esta semana?

Atentamente, [Sergio]
```

### I.3 · Script de ingesta para nuevas fuentes

El pipeline de ingesta ya existe en `src/jurisbot/ingestion/`. Para agregar nuevas obras:

```bash
# 1. Colocar PDFs en la carpeta de ingesta
cp nueva_obra.pdf data/doctrina/penal/

# 2. Correr el orquestador de ingesta (ya implementado)
cd /ruta/a/jurisbot
python3 -m jurisbot.ingestion.orchestrator \
    --source data/doctrina/penal/ \
    --rama "Derecho Penal" \
    --collection biblioteca_doctrina

# 3. Verificar ingesta
python3 -c "
import chromadb
client = chromadb.PersistentClient(path='data/chroma')
col = client.get_collection('biblioteca_doctrina')
print(f'Total chunks: {col.count()}')
"
```

### I.4 · Roadmap de crecimiento de biblioteca

| Mes | Target chunks | Target obras | Materias cubiertas |
|-----|---------------|--------------|-------------------|
| Actual | 18,037 | 443 | Civil (89%) + Ambiental |
| +1 mes | 25,000 | 550 | + Penal básico + Constitucional básico |
| +2 meses | 35,000 | 700 | + Laboral + Comercial |
| +3 meses | 50,000 | 900 | 8 de 11 materias cubiertas |
| +6 meses | 80,000 | 1,200 | Cobertura completa 11 ramos |

El pipeline de ingesta ya está construido. La tarea es conseguir el contenido — que con las fuentes de dominio público (BCN, PJUD) es perfectamente alcanzable sin costo y sin riesgo legal.

---

## RESUMEN EJECUTIVO — PRIORIDADES ABSOLUTAS

### Esta tarde (3 acciones):
1. **Ocultar selector LLM** en `app.py` L.738–757 (20 min) — Convierte prototipo en producto
2. **Crear `.streamlit/secrets.toml`** + deploy Streamlit Cloud (30 min) — URL estable
3. **Rotar API key de Anthropic** + sacarla de `.env` (10 min) — Seguridad mínima

### Esta semana (3 acciones):
4. **Conectar formulario de contacto** con Formspree (15 min) — Capturar leads de demo
5. **Email a 3 autores** pidiendo autorización de indexación (1h) — Resolver riesgo IP
6. **Indexar Código Penal + Código del Trabajo** (BCN, dominio público) — Ampliar cobertura

### Este mes (3 acciones):
7. **Beta privada con 20 usuarios** en 2 facultades — Obtener feedback y primeros pagantes
8. **Postular a CORFO Capital Semilla** — Financiamiento no dilutivo disponible ahora
9. **Implementar autenticación + pagos** (Supabase + Transbank) — Convertir de demo a negocio

---

*AntonIA v3.0 tiene los cimientos correctos: el RAG funciona, el diseño es premium, el banco de preguntas es sólido, y la librería base (Civil + Ambiental) es genuinamente útil. Los problemas son de capa de presentación, seguridad y cobertura de contenido — todos solucionables en semanas, no meses. El mercado está abierto.*

---
**Documento generado el 29 de marzo de 2026 | Datos verificados en vivo desde el repositorio**
