"""
banco_desarrollo.py — Preguntas de desarrollo para ENTRENA (AntonIA)
Organizadas por curso. Formato: {"pregunta": str, "tema": str, "pauta": str}
"""
from __future__ import annotations

BANCO_DEV: dict[str, list[dict]] = {

    # ── CIVIL I — PERSONAS Y ACTO JURÍDICO ──────────────────────────────
    "civil": [
        {
            "pregunta": "Explique la teoría de las nulidades en el Código Civil chileno. Distinga entre nulidad absoluta y relativa, señalando causales, titulares de la acción y efectos de cada una.",
            "tema": "Nulidades — Acto Jurídico",
            "pauta": "Nulidad absoluta (art. 1682 CC): causales (objeto/causa ilícita, falta de requisitos de existencia), cualquier interesado puede alegarla, irratificable, prescripción 10 años. Nulidad relativa: incapacidad relativa, vicios del consentimiento, solo el afectado, ratificable, prescripción 4 años.",
        },
        {
            "pregunta": "¿Qué es la representación en el derecho civil chileno? Explique sus clases y efectos jurídicos.",
            "tema": "Representación — Acto Jurídico",
            "pauta": "Concepto (art. 1448 CC). Legal (padres, tutores, curadores) y voluntaria (mandato). Efectos: el acto produce efectos directamente en el representado como si lo hubiere celebrado él mismo. Requisitos: que el representante actúe a nombre del representado y dentro de los poderes.",
        },
        {
            "pregunta": "Desarrolle el concepto de condición en el derecho de obligaciones. Clasifique las condiciones y explique los efectos de la condición suspensiva pendiente, cumplida y fallida.",
            "tema": "Modalidades — Condición",
            "pauta": "Condición: hecho futuro e incierto. Clasificación: suspensiva/resolutoria; potestativa/casual/mixta; positiva/negativa; determinada/indeterminada. Condición suspensiva: pendiente → obligación no nace, hay derecho eventual; cumplida → nace la obligación; fallida → se extingue el derecho.",
        },
        {
            "pregunta": "Analice la rescisión por lesión enorme en el contrato de compraventa. ¿En qué consiste? ¿Cuándo procede? ¿Qué opciones tiene el comprador y el vendedor?",
            "tema": "Compraventa — Lesión Enorme",
            "pauta": "Arts. 1888-1896 CC. Vendedor: precio < mitad del justo precio. Comprador: precio > doble del justo precio. Solo inmuebles. Opciones: comprador puede completar justo precio; vendedor puede restituir el exceso. Acción prescribe en 4 años.",
        },
        {
            "pregunta": "Explique la distinción entre derechos reales y derechos personales en el Código Civil chileno. Dé tres ejemplos de cada uno y señale las diferencias en cuanto a su objeto, contenido y acción que los protege.",
            "tema": "Clasificación de Derechos",
            "pauta": "Reales (art. 577 CC): sobre cosa sin respecto a determinada persona. Ejemplos: dominio, hipoteca, usufructo. Acción real. Personales: exigir de persona determinada. Ejemplos: crédito mutuo, arriendo, precio compraventa. Acción personal. Diferencias: número (numerus clausus real, abiertos personales), oponibilidad erga omnes vs inter partes.",
        },
        {
            "pregunta": "¿Qué es el dolo en materia contractual? Distinga el dolo como vicio del consentimiento, el dolo en el cumplimiento y el dolo como elemento del delito civil.",
            "tema": "Dolo — Contratos",
            "pauta": "Dolo como vicio: maquinación fraudulenta que induce a contratar (art. 1458 CC). Debe ser principal y obra de la otra parte. Efectos: nulidad relativa + indemnización. Dolo en cumplimiento: agrava la responsabilidad contractual (art. 1558 CC), no se puede condonar anticipadamente. Dolo delictual: elemento del ilícito (art. 2284 CC).",
        },
        {
            "pregunta": "Explique la responsabilidad contractual en el Código Civil. ¿Cuáles son sus elementos? Analice en particular la importancia de la distinción entre obligaciones de medio y de resultado.",
            "tema": "Responsabilidad Contractual",
            "pauta": "Elementos: incumplimiento, imputabilidad (culpa o dolo), daño, nexo causal. Culpa: se presume en responsabilidad contractual (art. 1547 CC). Obligaciones de medio: el deudor se obliga a actuar diligentemente (ej: médico). Obligaciones de resultado: el deudor garantiza el resultado (ej: transportista). Relevancia en distribución de la carga de la prueba.",
        },
        {
            "pregunta": "Desarrolle el régimen de la copropiedad en Chile. ¿Cómo se forma? ¿Cómo se administra? ¿Cómo se liquida?",
            "tema": "Copropiedad",
            "pauta": "Art. 2304 y ss. CC. Formación: por acto voluntario o sucesión. Administración: cuotaspartes, actos de administración con mayoría, enajenación de cuota propia sin necesidad de acuerdo. Liquidación: cualquier comunero puede pedir la partición (art. 1317 CC), acción imprescriptible. Partición judicial o extrajudicial.",
        },
        {
            "pregunta": "Analice los efectos de la declaración de nulidad del matrimonio. Distinga entre el matrimonio nulo de buena fe (putativo) y el matrimonio nulo de mala fe.",
            "tema": "Nulidad Matrimonial",
            "pauta": "Nulidad matrimonial (LMC art. 44 ss.). Matrimonio putativo (art. 51 LMC): cuando al menos uno actuó de buena fe y con justa causa de error, produce efectos civiles hasta la sentencia de nulidad. Mala fe: no produce efectos desde el principio. Efectos: disolución vínculo, liquidación de bienes si hubo buena fe.",
        },
        {
            "pregunta": "Explique el principio de autonomía de la voluntad y sus limitaciones en el derecho civil chileno actual.",
            "tema": "Autonomía de la Voluntad",
            "pauta": "Principio: las partes pueden crear derechos y obligaciones (art. 1545 CC). Limitaciones: orden público, buenas costumbres, ley imperativa (art. 1461 CC). En contratos de adhesión: Ley 19.496 limita cláusulas abusivas. Tendencia doctrinaria a reconocer mayor intervención estatal para proteger partes débiles.",
        },
    ],

    # ── BIENES Y DERECHOS REALES ─────────────────────────────────────────
    "bienes": [
        {
            "pregunta": "Explique el sistema registral chileno de bienes raíces. ¿Qué función cumple la inscripción en el Conservador de Bienes Raíces? ¿Es la inscripción un modo de adquirir?",
            "tema": "Sistema Registral — Bienes Raíces",
            "pauta": "CBR: tres registros (Propiedad, Hipotecas, Interdicciones). Funciones: publicidad, tradición de inmuebles (art. 686 CC), requisito de posesión inscrita. No es modo de adquirir per se: es la tradición quien transfiere el dominio. La inscripción es el modo de efectuar la tradición de inmuebles.",
        },
        {
            "pregunta": "Analice la posesión en el derecho civil chileno. ¿Cuáles son sus elementos? ¿Qué ventajas otorga la posesión y cómo se adquiere, conserva y pierde?",
            "tema": "Posesión",
            "pauta": "Posesión (art. 700 CC): corpus + animus. Ventajas: presunción de dominio, prescripción adquisitiva, acciones posesorias. Adquisición: aprehensión o inscripción. Conservación: se mantiene el animus. Pérdida: enajenación, abandono, pérdida de la cosa. Posesión regular e irregular.",
        },
        {
            "pregunta": "Explique el usufructo como derecho real. ¿Cómo se constituye? ¿Cuáles son los derechos y obligaciones del usufructuario y del nudo propietario?",
            "tema": "Usufructo",
            "pauta": "Usufructo (art. 764 CC): usar y gozar la cosa sin alterar su forma y sustancia. Constitución: ley, testamento, convención, prescripción. Usufructuario: derechos de uso y goce, obligaciones de inventario, caución, conservación. Nudo propietario: conserva el dominio desnudo, puede enajenarlo. Extinción: cumplimiento del plazo, muerte del usufructuario, consolidación.",
        },
        {
            "pregunta": "Desarrolle las acciones posesorias. ¿Qué son? ¿Cuáles existen? ¿Cuáles son sus requisitos y plazos?",
            "tema": "Acciones Posesorias",
            "pauta": "Arts. 916 ss. CC. Protegen la posesión sin discutir el dominio. Tipos: amparo (perturbación), restitución (despojo), restablecimiento (despojo violento), querella de obra ruinosa, denuncia de obra nueva. Requisitos: posesión tranquila y no interrumpida de al menos 1 año. Plazo: 1 año para amparo y restitución; 6 meses para restablecimiento.",
        },
        {
            "pregunta": "Explique el concepto de tradición y sus requisitos. ¿Cómo se efectúa la tradición de bienes muebles, inmuebles y créditos?",
            "tema": "Tradición — Modo de Adquirir",
            "pauta": "Tradición (art. 670 CC): entrega que hace el dueño de una cosa con intención de transferir y el que la recibe con intención de adquirir. Requisitos: dos personas, consentimiento sin vicios, título traslaticio. Muebles: entrega real o ficta. Inmuebles: inscripción en CBR (art. 686). Créditos: entrega del título y notificación al deudor (art. 699).",
        },
    ],

    # ── OBLIGACIONES Y CONTRATOS ─────────────────────────────────────────
    "obligaciones": [
        {
            "pregunta": "Analice la teoría del riesgo en el derecho civil chileno. ¿Quién soporta el riesgo de la especie o cuerpo cierto que perece fortuitamente antes de la entrega?",
            "tema": "Teoría del Riesgo",
            "pauta": "Art. 1550 CC: el riesgo es del acreedor (res perit creditori) en los contratos bilaterales. El acreedor debe pagar el precio aunque la cosa haya perecido. Excepciones: si el deudor estaba en mora, si hubo pacto en contrario. Crítica doctrinal al sistema del Código que sigue el derecho romano.",
        },
        {
            "pregunta": "Explique el pago con subrogación. ¿En qué casos opera legalmente? ¿Cuál es su efecto?",
            "tema": "Modos de Extinción — Subrogación",
            "pauta": "Subrogación (art. 1608-1613 CC): sustitución de una persona en los derechos de otra. Legal: pago por tercero con consentimiento expreso/tácito del deudor, pago por acreedor hipotecario a otro preferente, pago del deudor solidario. Efectos: el tercero que paga queda en el lugar del acreedor con todos sus derechos, privilegios y garantías.",
        },
        {
            "pregunta": "Desarrolle la excepción de contrato no cumplido (mora purga la mora). ¿Cuándo procede? ¿Cuál es su fundamento y efectos?",
            "tema": "Mora — Incumplimiento",
            "pauta": "Art. 1552 CC: en contratos bilaterales, ninguna de las partes está en mora mientras la otra no cumpla o no se allane a cumplir. Fundamento: reciprocidad e interdependencia de obligaciones. Efectos: enerva la acción de cumplimiento forzado o resolución mientras no se acredite el propio cumplimiento o allanamiento. No impide la acción, solo la excepción.",
        },
        {
            "pregunta": "¿Qué es la acción pauliana o revocatoria? ¿Cuáles son sus requisitos según el Código Civil? Explique cómo opera en actos gratuitos y onerosos.",
            "tema": "Acción Pauliana",
            "pauta": "Art. 2468 CC: permite a los acreedores revocar actos fraudulentos del deudor realizados en perjuicio de sus derechos. Requisitos: fraude (mala fe del deudor), daño al acreedor (perjuicio), causalidad. Actos gratuitos: basta la mala fe del deudor. Actos onerosos: también se requiere la mala fe del tercero adquirente. La acción prescribe en 1 año desde el conocimiento del fraude.",
        },
        {
            "pregunta": "Explique las obligaciones de género. ¿Cómo se cumplen? ¿Qué sucede si el género perece? Contraste con las obligaciones de especie o cuerpo cierto.",
            "tema": "Clasificación de Obligaciones",
            "pauta": "Obligaciones de género (art. 1508 CC): tienen por objeto indeterminados individuos de una clase o género. El género no perece (genus nunquam perit). El deudor cumple eligiendo individuos de calidad a lo menos mediana. Contraste con especie o cuerpo cierto: objeto determinado individualmente, perece con el deudor si el perecimiento es fortuito (con excepciones en mora).",
        },
    ],

    # ── FAMILIA ─────────────────────────────────────────────────────────
    "familia": [
        {
            "pregunta": "Explique los regímenes matrimoniales vigentes en Chile. ¿Cuáles son? ¿Cómo se elige entre ellos? ¿Cuándo y cómo puede cambiarse el régimen?",
            "tema": "Regímenes Matrimoniales",
            "pauta": "Tres regímenes: sociedad conyugal (supletorio), separación total de bienes, participación en los gananciales (Ley 19.335). Elección: al contraer matrimonio. Cambio: por mutuo acuerdo ante notario, liquidando el régimen anterior, inscribiéndolo al margen de la partida de matrimonio (art. 1723 CC). Solo puede cambiarse una vez durante el matrimonio.",
        },
        {
            "pregunta": "Analice el principio del interés superior del niño en el derecho de familia chileno. ¿Cómo se aplica en materias de cuidado personal, relación directa y regular, y alimentos?",
            "tema": "Interés Superior del Niño",
            "pauta": "Principio rector (art. 222 CC, Convención ONU Derechos del Niño, art. 16 Ley 19.968). En cuidado personal: juez evalúa vinculación afectiva, idoneidad parental, bienestar del menor. En visitas: garantiza contacto con ambos padres. En alimentos: la necesidad del menor prevalece sobre otras consideraciones. El juez puede apartarse del acuerdo de las partes si no protege al niño.",
        },
        {
            "pregunta": "Desarrolle los derechos y obligaciones derivados de la patria potestad. ¿A quién corresponde? ¿Cómo se suspende o termina?",
            "tema": "Patria Potestad",
            "pauta": "Patria potestad (art. 243 CC): conjunto de derechos y obligaciones que corresponden al padre o madre sobre los bienes de los hijos no emancipados. Comprende: representación legal, administración de bienes, usufructo legal. Corresponde a ambos padres. Suspensión: por larga ausencia, demencia, interdicción. Extinción: emancipación (legal, judicial o voluntaria). Arts. 243-296 CC.",
        },
        {
            "pregunta": "Explique el divorcio en Chile desde la Ley 19.947. ¿Cuáles son las causales? ¿Qué es el divorcio sanción y el divorcio remedio? ¿Qué efectos produce el divorcio?",
            "tema": "Divorcio — Ley de Matrimonio Civil",
            "pauta": "Ley 19.947. Divorcio sanción (art. 54 LMC): falta grave imputable al otro cónyuge (adulterio, maltrato, abandono, condena por delito). Divorcio remedio: por mutuo acuerdo tras 1 año de cese (art. 55 inc. 1) o unilateral tras 3 años (art. 55 inc. 3). Efectos: disuelve el matrimonio, termina la sociedad conyugal, puede fijarse compensación económica (arts. 61-66 LMC).",
        },
        {
            "pregunta": "¿Qué es la compensación económica en el divorcio o nulidad? ¿Cuáles son sus requisitos y cómo se determina su monto?",
            "tema": "Compensación Económica",
            "pauta": "Arts. 61-66 LMC. Procede cuando un cónyuge no desarrolló actividad remunerada o lo hizo en menor medida por dedicarse al hogar o crianza de hijos. Requisitos: menoscabo económico, divorcio o nulidad, cónyuge que no trabajó o trabajó menos. Factores del monto: duración del matrimonio, situación patrimonial de ambos, edad del beneficiado. Puede fijarse como capital, renta o especie.",
        },
    ],

    # ── SUCESORIO ────────────────────────────────────────────────────────
    "sucesorio": [
        {
            "pregunta": "Explique los órdenes sucesorios en la sucesión intestada chilena. ¿Cómo se distribuye la herencia en el primero y segundo órdenes? ¿Qué es el derecho de representación?",
            "tema": "Órdenes Sucesorios Intestados",
            "pauta": "1° orden: hijos (y cónyuge). 2° orden: ascendientes y cónyuge (si no hay hijos). 3°: hermanos. 4°: otros colaterales. 5°: Fisco. Primer orden: hijos por partes iguales, cónyuge recibe el doble de un hijo (o mínimo de 1/4 parte). Representación (art. 984 CC): los descendientes de una persona que no puede o no quiere suceder ocupan su lugar.",
        },
        {
            "pregunta": "Analice las asignaciones forzosas del Código Civil. ¿Qué son? ¿Cuáles son? ¿Qué acciones protegen al legitimario cuando el testador las vulnera?",
            "tema": "Asignaciones Forzosas — Legítimas",
            "pauta": "Arts. 1167-1216 CC. Asignaciones forzosas: alimentos debidos por ley, legítimas, cuarta de mejoras. Legitimarios: hijos, ascendientes, cónyuge. Mitad legitimaria se divide en legítimas rigorosas. Acciones: reforma del testamento (art. 1216, prescripción 4 años); acción de colación; acción de inoficiosa donación si se vulnera la legítima con donaciones.",
        },
        {
            "pregunta": "Explique el testamento. ¿Cuáles son sus clases? ¿Cuáles son los requisitos del testamento solemne abierto otorgado ante notario?",
            "tema": "Testamento — Formalidades",
            "pauta": "Testamento: acto unilateral, personalísimo, mortis causa, solemne, esencialmente revocable. Clases: solemnes (abierto ante notario o tres testigos; cerrado) y menos solemnes (verbal, militar, marítimo). Testamento solemne abierto ante notario (art. 1014): ante notario competente + tres testigos hábiles; se escribe en libro de protocolos; firma el testador, notario y testigos; se lee en alta voz.",
        },
        {
            "pregunta": "¿Qué es la partición de bienes hereditarios? ¿Quiénes intervienen? ¿Cómo se lleva a cabo la partición judicial?",
            "tema": "Partición de Bienes",
            "pauta": "Partición: división del haber hereditario entre los herederos (arts. 1317-1353 CC). El testador puede hacerla en el testamento; herederos de común acuerdo; judicial con árbitro partidor. Partición judicial: árbitro de derecho nombrado de común acuerdo o por el juez. Tramitación ante árbitro como juicio ordinario. El laudo y la ordenata son las resoluciones finales que adjudican los bienes.",
        },
        {
            "pregunta": "Explique las donaciones entre vivos como título gratuito. ¿Cuáles son sus requisitos? ¿Qué es la insinuación? ¿Cómo afectan a las legítimas?",
            "tema": "Donaciones entre Vivos",
            "pauta": "Donación (art. 1386 CC): acto por el que una persona transfiere parte de su patrimonio a otra de forma gratuita. Requisitos: capacidad, objeto lícito, causa gratuita, aceptación. Insinuación (art. 1401): autorización judicial para donaciones que excedan 2 centavos (actualmente de cuantía relevante). Afectación a legítimas: donaciones excesivas reducen la legítima, acción de inoficiosa donación (art. 1187 CC).",
        },
    ],

    # ── PENAL ────────────────────────────────────────────────────────────
    "penal": [
        {
            "pregunta": "Desarrolle la estructura del delito según la doctrina finalista. Explique tipicidad, antijuridicidad y culpabilidad, mencionando las causales de exclusión de cada estrato.",
            "tema": "Estructura del Delito — Finalismo",
            "pauta": "Tipicidad: adecuación del hecho al tipo penal. Causas de atipicidad: ausencia de tipo, error de tipo. Antijuridicidad: contrariedad con el ordenamiento jurídico. Causas de justificación: legítima defensa, estado de necesidad, cumplimiento del deber. Culpabilidad: reprochabilidad al autor. Causas de inculpabilidad: inimputabilidad, error de prohibición invencible, exigibilidad.",
        },
        {
            "pregunta": "Explique el principio de legalidad en materia penal (nullum crimen nulla poena sine lege). ¿Cuáles son sus corolarios? ¿Cuál es su consagración en la Constitución y el Código Penal?",
            "tema": "Principio de Legalidad",
            "pauta": "Art. 19 N°3 inc. 8 y 9 CPR; art. 18 CP. Corolarios: lex scripta (solo ley puede tipificar), lex previa (irretroactividad, salvo ley más favorable), lex stricta (prohibición de analogía in malam partem), lex certa (determinación del tipo). Garantía del ciudadano frente al poder punitivo del Estado.",
        },
        {
            "pregunta": "Analice las circunstancias atenuantes de responsabilidad penal en Chile. Nombre y explique al menos cinco del artículo 11 del Código Penal.",
            "tema": "Atenuantes — Art. 11 CP",
            "pauta": "Art. 11 CP: 1° conducta anterior irreprochable; 2° arrebato u obcecación; 3° provocación suficiente; 4° vindicación próxima de ofensa; 5° entregarse a la justicia; 6° confesión; 7° reparar el mal; 8° y 9° edad (menor de 18/mayor de 70). Efectos en la determinación de la pena: permiten bajar el grado de la pena (arts. 67-68 CP).",
        },
        {
            "pregunta": "Explique la autoría y participación criminal en el Código Penal chileno. ¿Cómo define la ley a los autores, cómplices e inductores? ¿Qué diferencias penológicas existen?",
            "tema": "Autoría y Participación",
            "pauta": "Art. 15 CP: son autores quienes toman parte en la ejecución, fuerzan o inducen, o cooperan por actos sin los cuales no se hubiere efectuado. Art. 16 CP: cómplices, cooperan por otros actos. Inductores en art. 15 N°2. Penas: autores reciben la pena del delito; cómplices la inmediatamente inferior en grado; encubridores la siguiente.",
        },
        {
            "pregunta": "Desarrolle el delito culposo o cuasidelito en el derecho penal chileno. ¿Cuál es la diferencia con el dolo? ¿Cuál es la estructura del tipo culposo y cómo se determina la infracción al deber de cuidado?",
            "tema": "Culpa — Delito Culposo",
            "pauta": "Cuasidelito: falta de cuidado, sin intención de dañar (arts. 2 y 490 CP). Diferencia con dolo: en el doloso hay representación del resultado y voluntad; en el culposo hay infracción a deber de cuidado sin querer el resultado. El deber de cuidado se determina ex ante por el estándar del hombre prudente en esa situación. Imprudencia, negligencia, impericia.",
        },
    ],

    # ── PROCESAL ─────────────────────────────────────────────────────────
    "procesal": [
        {
            "pregunta": "Explique los principios del proceso civil en Chile. Señale cuáles son y cómo se manifiestan en el CPC.",
            "tema": "Principios del Proceso Civil",
            "pauta": "Principio dispositivo: las partes inician y configuran el proceso; el juez no puede actuar de oficio salvo excepciones. Contradicción: toda parte debe tener oportunidad de defenderse. Igualdad de armas. Escrituración e inmediación (reforma). Preclusión. Concentración. Publicidad. Principio de bilateralidad de la audiencia (art. 19 N°3 CPR).",
        },
        {
            "pregunta": "Analice las medidas cautelares en el proceso civil. ¿Cuáles son las precautorias del CPC? ¿Qué requisitos deben concurrir para que el juez las conceda?",
            "tema": "Medidas Cautelares Civiles",
            "pauta": "Arts. 290-302 CPC. Medidas: secuestro, nombramiento de interventor, retención de bienes, prohibición de celebrar actos y contratos. Requisitos: (1) verosimilitud del derecho (fumus boni iuris); (2) peligro en la demora (periculum in mora); (3) caución si el juez lo exige. Pueden pedirse antes o durante el juicio. Son esencialmente provisionales.",
        },
        {
            "pregunta": "Explique el proceso monitorio laboral. ¿Cuándo procede? ¿Qué sucede si el demandado no responde o responde tardíamente?",
            "tema": "Procedimiento Monitorio Laboral",
            "pauta": "Art. 496-502 CT. Procede para demandas de hasta 10 ingresos mínimos mensuales. Presentada la demanda, el juez si la estima fundada, dicta sentencia de plano. Si el demandado no reclama en 10 días, la sentencia queda firme. Si reclama, se celebra audiencia única. Si no comparece el demandado, se tiene por confeso o la sentencia queda firme. Procedimiento rápido para cobros de menor cuantía.",
        },
        {
            "pregunta": "Desarrolle la prueba testimonial en el proceso civil. ¿Cuándo es admisible? ¿Quiénes son inhábiles para ser testigos? ¿Cómo se valora?",
            "tema": "Prueba Testimonial Civil",
            "pauta": "Arts. 356-384 CPC. La prueba de testigos no es admisible para acreditar obligaciones que deban constar por escrito (art. 1708-1709 CC). Inhabilidades absolutas: dementes, menores de 14, sordos sin comunicarse, condenados por perjurio. Relativas: cónyuge, parientes cercanos, amigos íntimos, dependientes. Valoración: el juez aprecia según sana crítica o conforme a reglas legales (2 testigos contestes = plena prueba bajo ciertas condiciones).",
        },
        {
            "pregunta": "Explique el recurso de casación en el fondo en Chile. ¿Cuándo procede? ¿Ante qué tribunal? ¿Cuál es la causal y qué implica la infracción de ley?",
            "tema": "Casación en el Fondo",
            "pauta": "Arts. 767-785 CPC. Procede contra sentencias definitivas e interlocutorias de segunda instancia cuando se han pronunciado con infracción de ley y esa infracción ha influido sustancialmente en el dispositivo del fallo. Tribunal: Corte Suprema (Sala Civil). Causal única: infracción de ley (derecho sustantivo o procesal con trascendencia en el fallo). Efectos: si se acoge, la CS invalida el fallo y dicta sentencia de reemplazo.",
        },
    ],

    # ── CONSTITUCIONAL ───────────────────────────────────────────────────
    "constitucional": [
        {
            "pregunta": "Explique el principio de supremacía constitucional en Chile. ¿Cómo se garantiza? Mencione los mecanismos de control de constitucionalidad.",
            "tema": "Supremacía Constitucional",
            "pauta": "Art. 6 y 7 CPR. Supremacía: la CPR está en la cúspide del ordenamiento. Mecanismos: (1) Tribunal Constitucional: control preventivo (art. 93 N°1-5) y represivo (inaplicabilidad art. 93 N°6, inconstitucionalidad N°7); (2) Recurso de protección y amparo para garantías individuales; (3) Control de legalidad de la Contraloría (toma de razón). Vinculatoriedad de la CPR para todos los órganos del Estado.",
        },
        {
            "pregunta": "Desarrolle los estados de excepción constitucional en Chile. ¿Cuáles son? ¿Cómo se declaran? ¿Qué derechos pueden limitarse en cada uno?",
            "tema": "Estados de Excepción",
            "pauta": "Arts. 39-45 CPR. Tipos: estado de asamblea (guerra externa), estado de sitio (guerra interna, conmoción interior grave), estado de emergencia (calamidades, daño o peligro para seguridad nacional), estado de catástrofe (calamidad pública). Declaración: Presidente con acuerdo del Congreso (asamblea, sitio) o solo (emergencia, catástrofe). Derechos que pueden limitarse varían según el estado.",
        },
        {
            "pregunta": "Analice la acción de protección. ¿Qué derechos protege? ¿Cuáles son sus características procesales? ¿Cuál es la diferencia con la acción de amparo?",
            "tema": "Acciones Constitucionales",
            "pauta": "Art. 20 CPR. Protege derechos del art. 19 excepto los expresamente excluidos. Características: acción informal, sin plazo de prescripción (Auto Acordado: 30 días), ante CA del domicilio del afectado, tramitación breve, el tribunal puede dictar medidas cautelares de inmediato. Diferencia con amparo (art. 21): el amparo solo protege libertad personal y seguridad individual frente a detenciones ilegales; el recurso de protección cubre un catálogo más amplio.",
        },
        {
            "pregunta": "Explique el principio de reserva legal en materia de derechos fundamentales. ¿Cómo opera? ¿Puede el reglamento regular derechos fundamentales?",
            "tema": "Reserva Legal — Derechos Fundamentales",
            "pauta": "Arts. 19 y 63 CPR. Solo la ley puede regular el ejercicio de los derechos fundamentales. El reglamento puede regular los detalles de ejecución pero no la sustancia. La CPR distingue entre reserva legal absoluta (solo ley de quórum calificado o más puede regular) y reserva legal relativa (ley puede autorizar al ejecutivo). La potestad reglamentaria del Presidente (art. 32 N°6) solo puede ejecutar y complementar la ley, no restringir derechos sin base legal.",
        },
        {
            "pregunta": "Desarrolle la responsabilidad del Estado en Chile. ¿Qué normas la consagran? ¿Qué es la falta de servicio? ¿Cuáles son sus requisitos?",
            "tema": "Responsabilidad del Estado",
            "pauta": "Art. 38 inc. 2 CPR; arts. 4 y 42 LOCBGAE (Ley 18.575). Falta de servicio: el órgano del Estado no funciona debiendo hacerlo, funciona mal o tardíamente. Requisitos: falta del servicio, daño al particular, nexo causal. Responsabilidad directa, no subsidiaria. Plazo prescripción: 4 años. No aplica a actos del legislador ni del poder judicial (salvo error judicial art. 19 N°7 i CPR).",
        },
    ],

    # ── LABORAL ─────────────────────────────────────────────────────────
    "laboral": [
        {
            "pregunta": "Explique los principios del derecho del trabajo. ¿Cuáles son los más importantes? ¿Cómo se manifiestan en el Código del Trabajo?",
            "tema": "Principios del Derecho Laboral",
            "pauta": "Protector (pro operario): in dubio pro operario, norma más favorable, condición más beneficiosa. Irrenunciabilidad (art. 5 CT): derechos mínimos son irrenunciables durante la vigencia del contrato. Continuidad: preferir la subsistencia del contrato. Primacía de la realidad: la situación fáctica prevalece sobre las formas. Buena fe laboral.",
        },
        {
            "pregunta": "Analice el contrato colectivo de trabajo y la negociación colectiva en Chile. ¿Qué es? ¿Quiénes pueden negociar? ¿Cuál es el procedimiento reglado?",
            "tema": "Negociación Colectiva",
            "pauta": "Arts. 303 y ss. CT. Negociación colectiva: proceso de negociación entre empleador y sindicato para regular condiciones de trabajo. Titularidad sindical (Ley 20.940): solo sindicatos pueden negociar colectivamente (eliminado el grupo negociador). Etapas: presentación del proyecto, respuesta del empleador, mediación, huelga. El instrumento colectivo tiene fuerza vinculante y es ley entre las partes.",
        },
        {
            "pregunta": "Explique el concepto de despido y las causales del artículo 160 del Código del Trabajo. ¿Cuáles no dan derecho a indemnización? ¿Cuáles sí?",
            "tema": "Terminación del Contrato — Causales",
            "pauta": "Art. 160 CT: causales de caducidad (no dan derecho a indemnización): conductas indebidas (art. 160 N°1), negociaciones incompatibles, ausencias injustificadas, abandono, actos graves. Art. 161 CT: necesidades de la empresa, jubilación → sí dan derecho a indemnización por años de servicio (art. 163 CT). Art. 163 bis: despido cuando empleador es deudor en procedimiento concursal.",
        },
        {
            "pregunta": "Desarrolle el procedimiento de tutela de derechos fundamentales en el proceso laboral. ¿Qué derechos protege? ¿Cómo funciona? ¿Qué se puede obtener?",
            "tema": "Tutela Laboral",
            "pauta": "Arts. 485-495 CT. Protege derechos fundamentales del trabajador vulnerados por el empleador: dignidad, vida privada, libertad de conciencia, libertad sindical, no discriminación. Procedimiento: denuncia ante Juzgado Laboral, la carga de la prueba se invierte (el empleador debe probar que su actuación no vulneró derechos). Medidas: reintegro, indemnización especial (de 6 a 11 remuneraciones), medidas de reparación.",
        },
        {
            "pregunta": "¿Qué son las horas extraordinarias? ¿Cuáles son sus límites legales? ¿Cómo se calculan y cuándo prescriben los créditos laborales?",
            "tema": "Jornada Laboral — Horas Extraordinarias",
            "pauta": "Arts. 30-32 CT. Horas extra: exceso sobre 45 horas semanales (jornada ordinaria máxima). Requisitos: pacto escrito, situaciones temporales, máx. 2 horas diarias y 12 semanales. Recargo: mínimo 50% sobre sueldo base para jornada ordinaria. Prescripción de créditos laborales: 2 años desde que se hicieron exigibles (art. 510 CT). Acción especial de nulidad del despido: 60 días desde notificación.",
        },
    ],
}
