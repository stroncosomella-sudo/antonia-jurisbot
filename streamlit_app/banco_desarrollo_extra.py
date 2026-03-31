"""
banco_desarrollo_extra.py — Preguntas de desarrollo adicionales (AntonIA)
Doctrina 2025 + derecho chileno clásico avanzado. 150 preguntas.
"""
from __future__ import annotations

BANCO_DEV_EXTRA: dict[str, list[dict]] = {

    # ── CIVIL (20) ────────────────────────────────────────────────────────
    "civil": [
        {
            "pregunta": "Analice la acción pauliana en el derecho civil chileno. ¿Cuáles son sus elementos? Distinga el consilium fraudis del eventus damni y señale qué efectos produce la acción respecto del tercero adquirente.",
            "tema": "Acción Pauliana",
            "pauta": "Art. 2468 CC. Requisitos: (1) acto del deudor que perjudique a los acreedores (eventus damni); (2) consilium fraudis: conocimiento del mal estado de los negocios, no requiere dolo, basta la ciencia del perjuicio. Tercero a título oneroso: debe acreditarse mala fe de ambas partes. Tercero a título gratuito: procede sin exigir mala fe (art. 2468 N°1). Efecto: inoponibilidad relativa del acto frente al acreedor accionante; no nulidad. Prescripción: 1 año desde el acto fraudulento (art. 2468 N°3).",
        },
        {
            "pregunta": "¿Reconoce el derecho civil chileno la teoría de la imprevisión? Exponga las posiciones de Abeliuk, Barros Bourie y la jurisprudencia de la Corte Suprema. ¿Qué soluciones existen ante el desequilibrio sobrevenido de un contrato?",
            "tema": "Teoría de la Imprevisión",
            "pauta": "CC chileno no la consagra expresamente; art. 1545 (fuerza obligatoria) es el obstáculo principal. Abeliuk: niega su procedencia general, solo cabría resolución por caso fortuito. Barros: admite la teoría por vía de buena fe (art. 1546) y analogía con excesiva onerosidad. CS: posición mayoritaria rechaza la imprevisión; fallos aislados la acogen vía buena fe objetiva. Soluciones prácticas: renegociación convencional, cláusulas de hardship, resolución por imposibilidad sobrevenida parcial.",
        },
        {
            "pregunta": "Desarrolle la responsabilidad civil médica en Chile. ¿Es una obligación de medios o de resultado? ¿Cómo se prueba el nexo causal? ¿Qué rol juega la lex artis?",
            "tema": "Responsabilidad Civil Médica",
            "pauta": "Regla general: obligación de medios (el médico no garantiza la curación, sino diligencia conforme a la lex artis). Excepción: cirugías estéticas o procedimientos donde el resultado es prometido → obligación de resultado. Carga de la prueba: el paciente debe acreditar la culpa médica (falta a la lex artis) y el nexo causal. Nexo causal es el elemento más difícil: se admite la pérdida de una chance como daño indemnizable (doctrina francesa recibida en Chile). Responsabilidad del establecimiento hospitalario: falta de servicio (art. 38 CPR para hospitales públicos; art. 2329 CC para privados).",
        },
        {
            "pregunta": "¿Procede el daño moral en la responsabilidad contractual? Trace la evolución jurisprudencial de la Corte Suprema chilena y señale los requisitos actuales para su procedencia.",
            "tema": "Daño Moral Contractual",
            "pauta": "Posición tradicional (hasta ~2000): el daño moral es exclusivo de la responsabilidad extracontractual; en contratos solo se indemnizan los perjuicios patrimoniales (art. 1556 CC). Evolución: CS desde 2000 en adelante ha reconocido el daño moral contractual cuando existe un vínculo de afectación personal intensa (contratos intuito personae, contratos de transporte aéreo, turismo, servicios médicos). Requisito: el daño moral debe ser probado y debe tener relación directa con el incumplimiento (art. 1558 CC — causalidad adecuada). Barros Bourie y Domínguez Hidalgo: lo avalan como daño resarcible por principio de reparación integral.",
        },
        {
            "pregunta": "Explique la simulación absoluta y relativa en el derecho civil chileno. ¿Cuáles son sus efectos entre las partes y frente a terceros? ¿Qué acciones proceden?",
            "tema": "Simulación",
            "pauta": "Simulación: divergencia consciente entre voluntad real y declarada. Absoluta: el acto aparente no corresponde a ninguna realidad jurídica (ej: venta ficticia para defraudar acreedores). Relativa: oculta un acto real distinto (ej: donación disfrazada de compraventa). Entre las partes: prima la voluntad real (art. 1560 CC). Frente a terceros de buena fe: el acto simulado es oponible; solo los de mala fe no pueden prevalerse de él. Acción de simulación: declarativa, imprescriptible entre partes; prescripción de la acción de perjuicios respecto de terceros.",
        },
        {
            "pregunta": "Distinga la acción reivindicatoria de la acción publiciana. ¿Cuáles son los requisitos de cada una? ¿Cuándo procede la publiciana respecto de un poseedor regular?",
            "tema": "Acciones Reales",
            "pauta": "Acción reivindicatoria (art. 889 CC): titular es el dueño que no posee; se dirige contra el poseedor no dueño; requiere acreditar dominio. Acción publiciana (art. 894 CC): titular es el poseedor regular que perdió la posesión antes de completar la prescripción; se dirige contra otro poseedor de peor derecho (irregular o con menor tiempo). Requisitos publiciana: posesión regular, pérdida antes de completar prescripción, demandado es poseedor de peor derecho. No procede contra el dueño ni contra poseedor con igual o mejor derecho.",
        },
        {
            "pregunta": "¿En qué consiste el enriquecimiento sin causa? Señale sus elementos y la acción in rem verso. ¿Cuándo no procede esta acción?",
            "tema": "Enriquecimiento Sin Causa",
            "pauta": "Enriquecimiento sin causa: ventaja patrimonial obtenida a expensas de otra persona sin fundamento jurídico. Elementos: (1) enriquecimiento del demandado; (2) empobrecimiento correlativo del demandante; (3) relación causal entre ambos; (4) ausencia de causa jurídica que justifique el traspaso. Acción in rem verso: restitutoria, solo hasta el monto del enriquecimiento. No procede: si existe acción contractual o cuasicontractual disponible (subsidiariedad); si el empobrecimiento fue voluntario con conocimiento de la falta de causa.",
        },
        {
            "pregunta": "Analice el contrato de transacción. ¿Cuál es su naturaleza jurídica? ¿Qué efectos produce? ¿En qué se diferencia de una sentencia judicial?",
            "tema": "Contrato de Transacción",
            "pauta": "Transacción (art. 2446 CC): contrato por el cual las partes terminan extrajudicialmente un litigio pendiente o precaven uno eventual, haciéndose concesiones recíprocas. Naturaleza: contrato bilateral, oneroso, conmutativo. Efecto principal: produce cosa juzgada (art. 2460 CC) — equivalente jurisdiccional. Diferencia con sentencia: la transacción es título ejecutivo solo si consta en escritura pública (art. 434 N°2 CPC). La sentencia es res judicata formal; la transacción es res judicata convencional. Solo puede rescindirse por dolo, violencia o lesión enorme si recae sobre inmuebles.",
        },
        {
            "pregunta": "Desarrolle la extinción del mandato por revocación y renuncia. ¿Qué responsabilidad asume el mandatario que actúa después de extinguido el mandato? ¿Puede el mandante revocar en cualquier momento?",
            "tema": "Extinción del Mandato",
            "pauta": "Art. 2163 CC: causales de extinción del mandato incluyen revocación (acto unilateral del mandante, art. 2165) y renuncia (acto unilateral del mandatario, art. 2167). Revocación: el mandante puede revocar cuando quiera (principio de libre revocabilidad); mandato irrevocable es válido solo si existe interés del mandatario o de un tercero (doctrina). Renuncia: el mandatario debe dar aviso con tiempo razonable para que el mandante adopte precauciones. Actuación post-extinción sin aviso: el mandatario responde de todos los perjuicios causados (art. 2173 CC). Terceros de buena fe protegidos mientras ignoran la extinción.",
        },
        {
            "pregunta": "¿Qué es la vicios redhibitorios? Distíngalos del saneamiento de evicción. ¿Cuáles son las acciones del comprador en cada caso y cuál es el plazo para ejercerlas?",
            "tema": "Vicios Redhibitorios y Evicción",
            "pauta": "Vicios redhibitorios (arts. 1857-1870 CC): defectos ocultos de la cosa vendida que la hacen inútil o disminuyen su utilidad. Requisitos: existir al tiempo de la venta, ser ocultos, graves. Acciones: acción redhibitoria (resolución) o quanti minoris (rebaja del precio). Plazo: 6 meses en muebles, 1 año en inmuebles (art. 1866 CC). Evicción (arts. 1837-1856 CC): el vendedor debe amparar al comprador frente a turbaciones de derecho de terceros. Acción de saneamiento: el comprador notifica al vendedor del juicio; si pierde, demanda saneamiento. Diferencia clave: vicios = defectos materiales; evicción = problemas de derecho sobre la cosa.",
        },
        {
            "pregunta": "Explique la responsabilidad por el hecho ajeno en el Código Civil chileno. ¿Quiénes responden? ¿Cuál es la naturaleza de esta responsabilidad y cómo puede eximirse el responsable?",
            "tema": "Responsabilidad por Hecho Ajeno",
            "pauta": "Arts. 2319-2328 CC. Responden: padres por hijos menores (art. 2319); tutores y curadores por pupilos (art. 2319); empleadores por dependientes en ejercicio de sus funciones (art. 2320); dueños de establecimientos por dependientes (art. 2320 inc. final). Fundamento: culpa in eligendo o in vigilando presumida. Carácter: presunción de culpa simplemente legal → admite prueba en contrario. Exención: acreditar que con la diligencia debida no se pudo impedir el daño (art. 2320 inc. final). El tercero civilmente responsable tiene acción de repetición contra el autor directo.",
        },
        {
            "pregunta": "Analice el contrato de fianza. Explique el beneficio de excusión, el beneficio de división y la subrogación del fiador que paga.",
            "tema": "Contrato de Fianza",
            "pauta": "Fianza (art. 2335 CC): obligación accesoria por la que un tercero garantiza el cumplimiento de la obligación principal. Beneficio de excusión (art. 2357 CC): el fiador puede exigir que primero se persiga al deudor principal; excepciones: fiador solidario, renuncia expresa, insolvencia del deudor. Beneficio de división (art. 2367 CC): si hay varios fiadores, cada uno responde solo por su cuota, salvo solidaridad. Subrogación (art. 2370 CC): el fiador que paga se subroga en todos los derechos del acreedor contra el deudor principal, incluyendo garantías, preferencias y acciones.",
        },
        {
            "pregunta": "¿Qué es la lesión enorme en el derecho chileno? ¿En qué contratos procede? ¿Qué opciones tienen las partes cuando se declara?",
            "tema": "Lesión Enorme",
            "pauta": "Lesión enorme (arts. 1888-1896 CC): desequilibrio grave entre las prestaciones de un contrato. Solo procede en compraventa de inmuebles (no muebles, no permutas). Vendedor lesionado: precio < mitad del justo precio. Comprador lesionado: precio > doble del justo precio. Opciones: la parte no lesionada puede evitar la rescisión completando el justo precio (vendedor) o devolviendo el exceso (comprador), con deducción/adición de una décima parte. Prescripción: 4 años desde la celebración. No procede si el inmueble ha sido enajenado a tercero.",
        },
        {
            "pregunta": "Desarrolle la teoría del riesgo en los contratos bilaterales chilenos. ¿Qué sucede con la obligación del comprador si la especie perece por caso fortuito antes de la entrega?",
            "tema": "Teoría del Riesgo",
            "pauta": "Art. 1550 CC: el riesgo de la especie o cuerpo cierto cuya entrega se deba es siempre a cargo del acreedor (comprador), aunque no se le haya entregado. Esto significa que si la cosa perece por caso fortuito antes de la entrega, el comprador igual debe pagar el precio (res perit creditori). Excepción: mora del vendedor invierte el riesgo. Crítica doctrinaria: la regla es contraria al derecho comparado (en Francia y Alemania el riesgo pasa solo con la entrega). Claro Solar la critica; Meza Barros la defiende como coherente con el título-modo.",
        },
        {
            "pregunta": "Explique el contrato de comodato. ¿Cuáles son las obligaciones del comodatario? ¿Responde de la culpa levísima? ¿Cuándo puede retener la cosa?",
            "tema": "Comodato",
            "pauta": "Comodato (art. 2174 CC): contrato real, gratuito, unilateral, por el que se entrega una cosa para su uso con obligación de restituirla. Obligaciones del comodatario: usar la cosa conforme al contrato o a su naturaleza; conservarla con el mayor cuidado (culpa levísima, art. 2178, porque el contrato cede en su sola utilidad); restituirla en el plazo convenido. Retención: el comodatario puede retener la cosa si el comodante le adeuda perjuicios causados por la mala calidad de la cosa, salvo que el comodante sea el dueño bona fide ignorante del defecto.",
        },
        {
            "pregunta": "¿Qué es la condición resolutoria ordinaria? ¿En qué se diferencia de la condición resolutoria tácita? ¿Requiere sentencia judicial para operar?",
            "tema": "Condición Resolutoria",
            "pauta": "Condición resolutoria ordinaria: condición expresamente pactada cuyo cumplimiento extingue el derecho. Opera ipso iure al cumplirse (no requiere declaración judicial). Resolución de pleno derecho. Condición resolutoria tácita (art. 1489 CC): va envuelta en todo contrato bilateral; supone el incumplimiento de una de las partes. Requiere sentencia judicial que la declare (el contrato subsiste hasta esa declaración). Consecuencia práctica: en la ordinaria, la restitución de prestaciones opera automáticamente; en la tácita, la parte cumplidora elige entre cumplimiento forzado o resolución, ambos con indemnización.",
        },
        {
            "pregunta": "Analice la acción de nulidad absoluta. ¿Quiénes pueden alegarla? ¿Puede el juez declararla de oficio? ¿En qué casos se sanea?",
            "tema": "Nulidad Absoluta",
            "pauta": "Art. 1682 CC: causales de nulidad absoluta: objeto ilícito, causa ilícita, falta de requisitos esenciales (consentimiento, objeto, causa), incapacidad absoluta. Titulares: cualquier persona que tenga interés en ello, incluso el Ministerio Público. El juez puede y debe declararla de oficio cuando aparece de manifiesto en el acto o contrato (art. 1683). No se sanea por ratificación, pero sí por prescripción extintiva de 10 años desde la celebración del acto (art. 1683 in fine). No puede alegarse por quien ejecutó el acto sabiendo o debiendo saber el vicio (art. 1683 — nemo auditur).",
        },
        {
            "pregunta": "¿Qué es el pago con subrogación? Distinga la subrogación legal de la convencional. ¿Qué derechos adquiere el tercero que paga?",
            "tema": "Pago con Subrogación",
            "pauta": "Subrogación (art. 1608 CC): el tercero que paga se subroga en todos los derechos del acreedor contra el deudor. Legal (art. 1610): opera por ministerio de la ley en los casos taxativos (acreedor hipotecario que paga a otro acreedor preferente; fiador; heredero beneficiario; etc.). Convencional (art. 1611): el acreedor la otorga expresamente al tercero que paga con dinero propio, con formalidades de la cesión de crédito. El subrogado adquiere el crédito con todos sus accesorios: hipotecas, prendas, fianzas, privilegios. Diferencia con cesión de crédito: la subrogación requiere pago efectivo; la cesión es un acto traslativo de dominio.",
        },
        {
            "pregunta": "Desarrolle la responsabilidad extracontractual por daño puramente económico (pure economic loss). ¿Es indemnizable en el derecho chileno? Señale la posición de Barros Bourie y la jurisprudencia.",
            "tema": "Daño Puramente Económico",
            "pauta": "Daño puramente económico: perjuicio patrimonial que no deriva de lesión a la persona o a bienes propios del demandante (ej: pérdida de negocios por daño a infraestructura de tercero). Derecho comparado: algunos sistemas lo limitan por razones de política (floodgates). Barros Bourie (Tratado de Responsabilidad Extracontractual, 2006): en Chile no existe regla de exclusión; el art. 2314 CC es una cláusula general que admite cualquier daño con nexo causal suficientemente directo. CS: tiende a aceptarlo cuando el nexo causal es directo y el daño es cierto, aunque exige mayor rigor probatorio en la causalidad.",
        },
        {
            "pregunta": "Explique el mutuo (préstamo de consumo) y el mutuo hipotecario. ¿Cuál es la naturaleza del mutuo? ¿Cuándo nace la obligación del mutuario?",
            "tema": "Mutuo y Mutuo Hipotecario",
            "pauta": "Mutuo (art. 2196 CC): contrato real, unilateral, gratuito en su versión civil (oneroso con pacto de intereses). Se perfecciona con la entrega de la cosa fungible; el mutuario adquiere dominio y debe restituir otro tanto de la misma calidad y cantidad. Mutuo hipotecario: mutuo garantizado con hipoteca; puede ser bancario (regido también por Ley General de Bancos). Obligación del mutuario: nace desde la entrega (contrato real). Prepago: Ley 18.010 regula intereses y prepago en operaciones de crédito de dinero; el deudor puede prepagar con comisión máxima del 1,5% del capital. Interés máximo convencional: 1,5 veces el interés corriente.",
        },
    ],

    # ── PENAL (20) ────────────────────────────────────────────────────────
    "penal": [
        {
            "pregunta": "¿Qué es la autoría mediata? Explique el instrumento doloso no cualificado y el instrumento que actúa sin dolo. ¿Cómo responde el 'hombre de atrás' en Chile?",
            "tema": "Autoría Mediata",
            "pauta": "Autoría mediata: el 'hombre de atrás' controla el hecho a través de un instrumento humano. Instrumento sin dolo: el ejecutor desconoce el tipo penal (ej: mensajero que transporta droga sin saberlo); el autor mediato tiene dominio de la situación. Instrumento doloso no cualificado: el ejecutor actúa con dolo pero carece del elemento especial del tipo (ej: extraneus que actúa como instrumento del intraneus en delito especial). En Chile: no existe consagración expresa de autoría mediata en el CP, pero la doctrina (Cury, Mañalich) la admite por interpretación de 'autor' en art. 14 CP. La CS la ha reconocido en delitos de funcionarios.",
        },
        {
            "pregunta": "Analice los delitos de omisión impropia en el derecho penal chileno. ¿Cuáles son las fuentes de la posición de garante? ¿Está codificada la cláusula de equivalencia?",
            "tema": "Omisión Impropia — Posición de Garante",
            "pauta": "Omisión impropia (comisión por omisión): quien tiene posición de garante y omite, responde como si hubiera causado activamente el resultado. Fuentes de la posición de garante: (1) ley (padres respecto de hijos menores); (2) contrato (niñera, guardavidas); (3) conducta precedente peligrosa (injerencia). Chile: CP no contempla cláusula general de equivalencia como el §13 StGB alemán. Solución dogmática: la doctrina chilena (Politoff, Matus, Ramírez) aplica los mismos criterios vía interpretación; la CS acepta la posición de garante en casos de homicidio por omisión de cuidadores.",
        },
        {
            "pregunta": "Desarrolle la tentativa inidónea (delito imposible) en el derecho penal chileno. ¿Es punible? ¿Cuál es la posición del CP y la doctrina?",
            "tema": "Tentativa Inidónea — Delito Imposible",
            "pauta": "Tentativa inidónea: el sujeto intenta cometer un delito con medios absolutamente inidóneos (ej: disparar con pistola descargada creyéndola cargada). Art. 7 CP chileno: define tentativa como el que 'da principio a la ejecución del crimen o simple delito por hechos directos'. La doctrina mayoritaria (Cury) considera que la tentativa inidónea no es punible en Chile porque no hay peligro real para el bien jurídico. Posición objetiva: sin idoneidad no hay injusto. Posición subjetiva (minoría): punible porque revela voluntad criminal. CS: en general exige idoneidad mínima del medio para condenar por tentativa.",
        },
        {
            "pregunta": "¿Qué es el error de prohibición? Distíngalo del error de tipo. ¿Cuáles son sus efectos sobre la culpabilidad en el sistema chileno?",
            "tema": "Error de Prohibición",
            "pauta": "Error de tipo (art. 1 CP): recae sobre los elementos del tipo objetivo; excluye el dolo (invencible) o lo atenúa (vencible → culpa si el tipo admite forma culposa). Error de prohibición: el sujeto conoce los hechos pero cree erróneamente que su conducta es lícita (cree que está justificado). Invencible: excluye la culpabilidad completamente. Vencible: atenúa la pena (art. 11 N°1 CP — eximente incompleta de error de prohibición). Chile: dogma finalista (Cury, Garrido Montt) lo ubica en la culpabilidad como error sobre la antijuridicidad de la conducta, no sobre el dolo.",
        },
        {
            "pregunta": "Desarrolle la responsabilidad penal de las personas jurídicas en Chile. ¿Qué modificó la Ley 21595 a la Ley 20393? ¿Cuáles son los elementos del modelo de prevención del delito?",
            "tema": "Responsabilidad Penal Personas Jurídicas",
            "pauta": "Ley 20393 (2009): establece responsabilidad penal de PJ por lavado de activos, financiamiento del terrorismo y cohecho. Ley 21595 (2023) reforma el criterio de imputación: reemplaza 'en beneficio o interés de la persona jurídica' por 'en el marco de sus actividades' — amplía significativamente el ámbito. Ley 21459 (2022): agrega delitos informáticos al catálogo (art. 21). Modelo de prevención (art. 4): debe contener identificación de actividades riesgosas, protocolos de prevención, canal de denuncias, sanciones internas. Certificación del modelo: atenúa la responsabilidad. Sanciones: multa, disolución, prohibición de contratar con Estado.",
        },
        {
            "pregunta": "Analice el femicidio en el Código Penal chileno. ¿Cuál es su tipo objetivo? ¿Cómo se relaciona con el parricidio? ¿Qué es el femicidio íntimo y el femicidio ampliado?",
            "tema": "Femicidio",
            "pauta": "Femicidio íntimo (art. 390 bis CP, incorporado por Ley 21212 de 2020): homicidio de la mujer por quien es o fue su cónyuge, conviviente, o con quien tuvo relación de pareja. Tipo objetivo: matar a una mujer en contexto de relación de pareja o ex pareja. Femicidio no íntimo (art. 390 ter CP): matar a una mujer por razón de género, aunque no exista relación de pareja (ej: acoso previo). Pena: presidio mayor en su grado máximo a presidio perpetuo calificado. Relación con parricidio: el femicidio íntimo es lex specialis respecto del parricidio cuando la víctima es mujer y el vínculo es de pareja.",
        },
        {
            "pregunta": "Explique el concurso aparente de leyes penales. Describa los principios de especialidad, subsidiariedad, consunción y alternatividad, con ejemplos.",
            "tema": "Concurso Aparente de Leyes",
            "pauta": "Concurso aparente: varios tipos penales parecen aplicables, pero solo uno rige. Especialidad: la ley especial desplaza a la general (lex specialis derogat generali); ej: femicidio vs homicidio. Subsidiariedad: una ley se aplica solo en defecto de otra; expresa (texto legal) o tácita (ej: tentativa cede ante el delito consumado). Consunción: el hecho más grave absorbe al menos grave cuando éste es típicamente acompañante (ej: homicidio consume las lesiones previas necesarias). Alternatividad (discutida): dos leyes tienen el mismo injusto pero distinta pena; se aplica la más favorable. En Chile: el principio más invocado en jurisprudencia es especialidad.",
        },
        {
            "pregunta": "Desarrolle el iter criminis en el delito de estafa. Señale cada etapa y cuándo se consuma. ¿Es punible la tentativa de estafa?",
            "tema": "Estafa — Iter Criminis",
            "pauta": "Estafa (art. 468-473 CP): tipo que requiere engaño → error → disposición patrimonial perjudicial → perjuicio. Iter criminis: actos preparatorios (impunes salvo preparación especial); tentativa: cuando el agente ha desplegado el engaño pero la víctima aún no ha incurrido en error o no ha dispuesto; frustración: el agente realizó todo lo necesario pero no obtuvo el perjuicio por causas ajenas; consumación: cuando se produce el perjuicio patrimonial efectivo. Punibilidad de la tentativa: sí, conforme a las reglas generales del art. 7 CP (presidio menor en su grado mínimo a presidio mayor en su grado mínimo, según cuantía).",
        },
        {
            "pregunta": "¿Qué es el estado de necesidad exculpante? Distíngalo del estado de necesidad justificante. ¿Qué requisitos exige cada uno?",
            "tema": "Estado de Necesidad",
            "pauta": "Estado de necesidad justificante (art. 10 N°7 CP): el mal causado es menor que el evitado; la conducta es lícita (no hay injusto). Requisitos: mal grave, actual o inminente, no evitable de otro modo, el mal causado sea menor. Estado de necesidad exculpante: el mal causado es igual o mayor que el evitado, pero el sujeto actuó bajo presión insoportable; el injusto existe pero la culpabilidad se excluye o disminuye. Chile: el art. 10 N°11 CP (introducido 2010) consagra la exculpación por miedo insuperable, pero el estado de necesidad exculpante stricto sensu se aplica vía exigibilidad disminuida o eximente incompleta (art. 11 N°1).",
        },
        {
            "pregunta": "Analice los delitos informáticos de la Ley 21459. ¿Cuáles son las 8 figuras? ¿Qué bien jurídico protegen? ¿Qué novedades introdujo respecto de la Ley 19.223?",
            "tema": "Delitos Informáticos — Ley 21459",
            "pauta": "Ley 21459 (junio 2022) reemplaza Ley 19.223. Bien jurídico: integridad, confidencialidad y disponibilidad de sistemas y datos informáticos. Figuras: (1) acceso ilícito a sistemas; (2) interceptación ilícita; (3) ataque a la integridad de datos; (4) ataque a la integridad de sistemas (sabotaje); (5) abuso de dispositivos; (6) falsificación informática; (7) fraude informático; (8) espionaje informático. Novedades: adapta Convenio de Budapest; amplía sujeto activo; aumenta penas; art. 21 extiende aplicación de Ley 20393 de personas jurídicas a estos delitos. Agravante: comisión por organización criminal.",
        },
        {
            "pregunta": "¿Qué son las penas sustitutivas a la privación de libertad? Señale las que contempla la Ley 18.216 y cuáles son los requisitos para acceder a cada una.",
            "tema": "Penas Sustitutivas — Ley 18.216",
            "pauta": "Ley 18.216 (texto refundido DL 1094): penas sustitutivas principales: (1) remisión condicional (pena ≤ 3 años, sin condenas anteriores o con condena ≤ 2 años): el condenado queda en libertad con supervisión; (2) reclusión parcial (pena ≤ 3 años): cumple en domicilio o establecimiento; (3) libertad vigilada (pena 3-5 años): supervisión intensa; (4) libertad vigilada intensiva (pena 5-10 años para ciertos delitos); (5) expulsión del territorio (extranjeros sin arraigo). Requisitos generales: pena en los rangos legales, ausencia de condenas anteriores (o en los plazos), pronóstico favorable. Juez valora circunstancias del caso.",
        },
        {
            "pregunta": "Explique la actio libera in causa. ¿Cómo responde penalmente quien se pone voluntariamente en estado de inimputabilidad?",
            "tema": "Actio Libera in Causa",
            "pauta": "Actio libera in causa: el sujeto se coloca voluntariamente en estado de inimputabilidad (ebriedad, drogadicción) para cometer el delito o previendo que en ese estado lo cometería. El momento relevante de imputación se retrotrae al acto libre previo (cuando decidió embriagarse). Si fue dolosa: responde por el delito doloso. Si fue culposa: responde por cuasidelito si el tipo admite forma culposa. Chile: CP exime de responsabilidad al enajenado mental (art. 10 N°1) y al que actúa privado de razón (art. 10 N°1). La alic permite imputar porque el acto libre anterior es la causa determinante del resultado.",
        },
        {
            "pregunta": "Analice la violación en el derecho penal chileno. ¿Cuál es el bien jurídico? ¿Cuándo hay 'violación por sorpresa'? ¿Qué modificó la Ley 21.675?",
            "tema": "Delitos Sexuales — Violación",
            "pauta": "Violación (art. 361 CP): acceso carnal mediante fuerza, intimidación o privación de sentido de la víctima, o cuando ésta es menor de 14 años (art. 362 CP). Bien jurídico: libertad e indemnidad sexual. 'Violación por sorpresa' o 'stealthing': retirar el preservativo sin consentimiento — debatido si cabe en el tipo actual. Ley 21.675 (2024 — Ley de VIF y violencia sexual): introduce el modelo de consentimiento afirmativo 'solo sí es sí' para efectos del tipo penal; amplía la definición de ausencia de consentimiento. Implicancia: la ausencia de resistencia no equivale a consentimiento; la victima puede haber consentido inicialmente y retractarse.",
        },
        {
            "pregunta": "Desarrolle el principio de proporcionalidad de las penas. ¿Es un control constitucional del legislador penal? ¿Qué ha dicho el Tribunal Constitucional chileno?",
            "tema": "Proporcionalidad de las Penas",
            "pauta": "Proporcionalidad: las penas deben ser adecuadas a la gravedad del injusto y la culpabilidad del autor. Fundamento constitucional: arts. 19 N°1 (dignidad), 19 N°3 (debido proceso), principio de racionalidad del legislador. TC chileno: ha declarado inaplicable normas que establecen penas desproporcionadas en relación al bien jurídico (ej: casos de tráfico de drogas con cantidades mínimas). Control del legislador: el TC puede declarar inconstitucional una ley penal que imponga penas manifiestamente desproporcionadas (art. 93 N°6-7 CPR). Doctrina: Cury y Garrido Montt reconocen que la proporcionalidad es un principio rector del sistema punitivo.",
        },
        {
            "pregunta": "Explique el cohecho en sus formas activa y pasiva. ¿Cuáles son los elementos del tipo? Distíngalo del tráfico de influencias.",
            "tema": "Cohecho y Tráfico de Influencias",
            "pauta": "Cohecho pasivo (art. 248 CP): el funcionario público que solicita o acepta un beneficio económico para realizar u omitir un acto de su cargo. Cohecho activo (art. 250 CP): el particular que ofrece o da el beneficio. Elemento: relación entre el beneficio y el acto funcional del cargo. Tráfico de influencias (arts. 240 bis y ss. CP): el particular o funcionario que, invocando influencias reales o simuladas, solicita o acepta beneficios para influir en una decisión de otro funcionario. Diferencia: en el cohecho hay un acuerdo directo funcionario-particular sobre el acto de cargo; en el tráfico, el influenciador no tiene competencia directa sobre ese acto.",
        },
        {
            "pregunta": "¿Qué es la participación criminal del extraneus en un delito especial? ¿Puede el extraneus ser autor o solo partícipe? ¿Cómo se resuelve en el CP chileno?",
            "tema": "Participación en Delito Especial",
            "pauta": "Delito especial propio: solo puede ser autor quien reúne la calidad especial exigida (ej: funcionario público en el cohecho pasivo). Extraneus: quien carece de la calidad especial. Teoría de la ruptura del título de imputación: el extraneus no puede ser autor ni coautor del delito especial; solo puede ser cómplice o instigador (inductor) con pena atenuada. Teoría de la unidad del título: el extraneus puede ser partícipe del delito especial del intraneus con la pena del tipo especial. CP chileno (arts. 15, 16): la doctrina mayoritaria (Mañalich, Cury) aplica ruptura del título; la CS ha oscilado entre ambas teorías.",
        },
        {
            "pregunta": "Desarrolle el cuasidelito (delito culposo) en el derecho penal chileno. ¿Cuál es la estructura del tipo imprudente? ¿Cómo se determina la infracción al deber de cuidado?",
            "tema": "Cuasidelito — Delito Culposo",
            "pauta": "Cuasidelito (arts. 2 y 490-492 CP): el que por imprudencia, negligencia o impericia causa un resultado típico sin intención. Estructura: acción imprudente + resultado + nexo causal + infracción al deber de cuidado. Deber de cuidado: determinado ex ante por el estándar del hombre prudente en la misma situación (hombre medio del sector); se incumple cuando el autor se aparta de lo que ese estándar exige. Clases de culpa: imprudencia (actuar sin precaución), negligencia (omitir diligencia debida), impericia (actuar sin la técnica necesaria). Punibilidad: solo los cuasidelitos expresamente señalados por la ley son punibles (art. 10 N°13 CP — limitación).",
        },
        {
            "pregunta": "Analice las medidas de seguridad en el derecho penal chileno. ¿A quiénes se les aplican? ¿Cuál es la diferencia entre pena y medida de seguridad?",
            "tema": "Medidas de Seguridad",
            "pauta": "Medidas de seguridad: reacciones penales aplicables a quienes son inimputables (enajenados mentales, art. 10 N°1 CP) o semi-imputables. No son penas porque no se fundan en culpabilidad sino en peligrosidad. Art. 455 CPP: el juez puede aplicar medidas de seguridad al enajenado mental absuelto: internación en establecimiento psiquiátrico, tratamiento ambulatorio. Duración: no puede exceder la pena máxima del delito imputado (principio de proporcionalidad); el tribunal revisa periódicamente. Diferencia con pena: la pena es retributiva y presupone culpabilidad; la medida es preventiva y presupone peligrosidad.",
        },
        {
            "pregunta": "Explique el concurso de delitos (ideal, medial y real) en el Código Penal chileno. ¿Cuál es la regla de determinación de la pena en cada caso?",
            "tema": "Concurso de Delitos",
            "pauta": "Concurso ideal (art. 75 CP): un solo hecho constituye dos o más delitos; se aplica la pena mayor asignada al delito más grave. Concurso medial (art. 75 CP): un delito es el medio necesario para cometer otro; misma regla que el ideal. Concurso real (art. 74 CP): dos o más hechos independientes que constituyen delitos distintos; se aplican todas las penas, acumulación material. Excepción al concurso real: si la acumulación resulta en una pena superior a la del delito más grave + 6 grados, el tribunal puede aplicar la del más grave aumentada en un grado (principio de absorción modificada). Límite de la pena: art. 76 CP — el doble de la más grave no puede exceder 30 años.",
        },
        {
            "pregunta": "¿Qué es la reincidencia en el derecho penal chileno? ¿Cuándo es agravante genérica? Distinga reincidencia propia e impropia.",
            "tema": "Reincidencia",
            "pauta": "Reincidencia propia (art. 12 N°15 CP): el que ha sido condenado anteriormente por delito de la misma especie. Reincidencia impropia (art. 12 N°16 CP): condenas anteriores por cualquier delito, siendo el nuevo de distinta especie. Requisitos comunes: sentencia ejecutoriada anterior; que el nuevo delito sea cometido después de esa condena. Efecto: agravante genérica que el tribunal debe considerar al determinar la pena. Prescripción de la agravante: transcurridos 10 años desde la condena anterior, no se considera la reincidencia. Doble valoración prohibida: no puede agravarse dos veces por el mismo hecho.",
        },
    ],

    # ── PROCESAL (15) ─────────────────────────────────────────────────────
    "procesal": [
        {
            "pregunta": "Analice el principio de congruencia procesal. ¿Qué es la ultra petita y la extra petita? ¿Cuál es el recurso para impugnar una sentencia que los incurre?",
            "tema": "Congruencia Procesal — Ultra y Extra Petita",
            "pauta": "Congruencia (art. 160 CPC): la sentencia debe pronunciarse sobre todo lo pedido (no más, no menos, no distinto). Ultra petita: la sentencia otorga más de lo pedido. Extra petita: se pronuncia sobre asuntos no planteados. Infra petita: omite pronunciarse sobre algo pedido (ultra petita pasiva). Recurso: casación en la forma (art. 768 N°4 CPC) por ultra petita. En el proceso penal: principio de congruencia entre la acusación y la sentencia (art. 341 CPP); la condena no puede exceder los hechos de la acusación ni imputar delito distinto.",
        },
        {
            "pregunta": "Explique el litisconsorcio activo y pasivo. ¿Cuándo es necesario y cuándo facultativo? ¿Qué efectos produce sobre la tramitación del proceso?",
            "tema": "Litisconsorcio",
            "pauta": "Litisconsorcio activo: varios demandantes; pasivo: varios demandados. Necesario: cuando la ley o la naturaleza de la relación jurídica exige que todos los interesados participen en el proceso (ej: nulidad de contrato en que intervinieron tres partes). Facultativo: cuando los litisconsortes podrían demandar separadamente pero eligen hacerlo juntos por conexión. Efectos: en el litisconsorcio necesario, la sentencia es ineficaz si no se notifica a todos; en el facultativo, los actos de uno no benefician ni perjudican a los demás salvo excepciones.",
        },
        {
            "pregunta": "¿Qué es la tercería de dominio y la tercería de posesión en el juicio ejecutivo? ¿Quién puede interponerlas y cuáles son sus efectos?",
            "tema": "Tercerías en el Juicio Ejecutivo",
            "pauta": "Tercería de dominio (art. 518 N°1 CPC): deducida por quien alega ser dueño del bien embargado. Efecto: suspende el procedimiento de apremio (embargo) mientras se resuelve. Debe acreditar dominio. Tercería de posesión (art. 521 CPC): quien alega ser poseedor del bien embargado. Tramitación: incidente separado. Diferencia: la de dominio exige acreditar título de dominio; la de posesión solo requiere probar posesión material. Ambas son tercerías excluyentes (pretenden excluir el bien del embargo). También existen tercerías de prelación (pagar antes) y de pago (pagar proporcionalmente).",
        },
        {
            "pregunta": "Desarrolle la prueba pericial. ¿Cómo se designa el perito? ¿Puede impugnarse el informe? ¿Cómo se valora conforme a la sana crítica?",
            "tema": "Prueba Pericial",
            "pauta": "Arts. 409-425 CPC (proceso civil); arts. 314-322 CPP (penal). Civil: las partes proponen peritos; si no hay acuerdo, los designa el tribunal. El informe se agrega a los autos; las partes pueden objetar por falta de fundamentación o por vicios formales. Valoración: sana crítica (en proceso reformado) o prueba legal (CPC antiguo). La sana crítica exige que el tribunal explique en la sentencia por qué acoge o rechaza el informe pericial, con referencia a lógica, experiencia y ciencia. Proceso penal: la parte adversa puede contrainterrogar al perito en el juicio oral; el tribunal valora su credibilidad holísticamente.",
        },
        {
            "pregunta": "¿Qué es el exequatur? ¿Cuáles son sus requisitos en Chile? ¿Qué tribunal lo concede y qué efecto tiene?",
            "tema": "Exequatur",
            "pauta": "Exequatur: procedimiento para reconocer y ejecutar en Chile resoluciones judiciales extranjeras (arts. 242-251 CPC). Tribunal competente: Corte Suprema (sala civil). Requisitos: (1) la resolución no sea contraria al orden público chileno; (2) el demandado haya sido legalmente notificado en el extranjero; (3) que la resolución esté ejecutoriada según la ley del país de origen; (4) reciprocidad (si existe tratado, se aplica el tratado). Tramitación: solicitud ante la CS, vista a la parte contraria y al Ministerio Público Judicial; resolución. Efecto: una vez concedido, la resolución extranjera se ejecuta como si fuera una sentencia nacional.",
        },
        {
            "pregunta": "Analice la prueba ilícita en el proceso penal chileno. ¿Cuál es la regla de exclusión? ¿Existen excepciones?",
            "tema": "Prueba Ilícita — Proceso Penal",
            "pauta": "Art. 276 CPP: el juez de garantía en la audiencia de preparación del juicio oral debe excluir la prueba obtenida con infracción sustancial de garantías fundamentales. Art. 277 CPP: el auto de apertura del juicio oral solo incluye la prueba no excluida. Efecto: la prueba ilícita no puede ser presentada ni valorada en el juicio. Regla del árbol envenenado (frutos): la prueba derivada de la ilícita también se excluye. Excepciones aceptadas por la CS: descubrimiento inevitable (la prueba habría sido obtenida de todas formas por medios lícitos); fuente independiente; buena fe del funcionario policial. Recurso si no se excluye: nulidad del juicio oral (art. 373 letra a CPP).",
        },
        {
            "pregunta": "Explique la nulidad procesal. ¿Cuáles son sus causales? ¿Qué es el principio de trascendencia? ¿Cómo se sanea?",
            "tema": "Nulidad Procesal",
            "pauta": "Nulidad procesal (art. 83 CPC): sanción que priva de efectos a los actos del proceso realizados con vicios que causan perjuicio. Principios: (1) trascendencia: no hay nulidad sin perjuicio (pas de nullité sans grief); (2) convalidación: la parte perjudicada que no alega oportunamente, sanea el vicio; (3) propósito reparatorio: la nulidad busca proteger a la parte perjudicada, no castigar. Saneamiento: por ratificación expresa o tácita (proseguir sin alegar), por transcurso del plazo para reclamar, o porque la irregularidad no causó perjuicio. En proceso penal: la nulidad del juicio oral procede por las causales taxativas del art. 374 CPP.",
        },
        {
            "pregunta": "¿Qué es la cosa juzgada? Distinga sus elementos subjetivos y objetivos. ¿Qué es la cosa juzgada formal vs. material?",
            "tema": "Cosa Juzgada",
            "pauta": "Cosa juzgada: efecto de las sentencias definitivas e interlocutorias firmes que impide revisar lo resuelto. Formal: la sentencia no puede modificarse dentro del mismo proceso (preclusión). Material: lo resuelto no puede ser objeto de nuevo juicio (ne bis in idem). Elementos: (1) identidad legal de personas (eadem personae); (2) identidad de la cosa pedida (eadem res); (3) identidad de la causa de pedir (eadem causa petendi). Acción de cosa juzgada (art. 175 CPC): para exigir el cumplimiento de lo resuelto. Excepción de cosa juzgada (art. 177 CPC): para impedir un nuevo juicio sobre lo mismo.",
        },
        {
            "pregunta": "Desarrolle el juicio ejecutivo chileno. ¿Cuáles son los títulos ejecutivos? ¿Qué excepciones puede oponer el ejecutado?",
            "tema": "Juicio Ejecutivo",
            "pauta": "Títulos ejecutivos (art. 434 CPC): sentencia firme, copia autorizada de escritura pública, acta de avenimiento, instrumento privado reconocido judicialmente, letra de cambio y pagaré con protesto, otros que la ley señale. Requisitos del título: obligación líquida, actualmente exigible, no prescrita. Cuaderno ejecutivo: requerimiento de pago + embargo si no paga. Excepciones (art. 464 CPC): incompetencia, falta de personería, ineptitud del líbelo, falta de mérito ejecutivo, pago, prescripción, cosa juzgada, compensación, entre otras. Plazo: 4 días para oponer excepciones. Si no hay excepciones: sentencia de remate.",
        },
        {
            "pregunta": "¿Qué es el recurso de casación en la forma? ¿Cuáles son sus causales? ¿Cuándo se declara de oficio?",
            "tema": "Casación en la Forma",
            "pauta": "Art. 768 CPC: procede contra sentencias definitivas e interlocutorias de primera o segunda instancia cuando se fundan en alguna de las causales taxativas. Causales principales: incompetencia del tribunal; ultra petita; falta de firma; falta de pronunciamiento sobre puntos controvertidos; ultra petita; haber sido pronunciada por menos jueces que el quórum legal; vicios de procedimiento que anulan el proceso. El tribunal ad quem (Corte de Apelaciones o CS) puede casar de oficio si advierte un vicio que funde la casación aunque no haya sido invocado por el recurrente (art. 775 CPC). Efecto si se acoge: anulación de la sentencia y reenvío.",
        },
        {
            "pregunta": "Analice la formalización de la investigación en el proceso penal acusatorio. ¿Qué efectos produce? ¿Puede el imputado solicitar que se ponga término a la investigación?",
            "tema": "Formalización de la Investigación",
            "pauta": "Formalización (art. 229 CPP): comunicación del fiscal al imputado, en presencia del juez de garantía, de que se desarrolla una investigación en su contra por uno o más delitos determinados. Efectos: (1) suspende la prescripción; (2) el fiscal debe investigar dentro de plazo (art. 247 CPP, máximo 2 años); (3) el imputado queda facultado para ejercer sus derechos de defensa. Si el fiscal no cierra la investigación en el plazo: el imputado o el juez pueden solicitar el sobreseimiento definitivo (art. 247 inc. final CPP). La formalización no implica condena ni presunción de culpabilidad.",
        },
        {
            "pregunta": "Desarrolle el procedimiento abreviado en el proceso penal chileno. ¿Cuándo procede? ¿Cuál es la diferencia con el juicio oral?",
            "tema": "Procedimiento Abreviado",
            "pauta": "Arts. 406-415 CPP. Procede cuando: (1) el fiscal solicita pena no superior a 5 años de privación de libertad; (2) el imputado acepta los hechos de la acusación y consiente en el procedimiento. No requiere juicio oral. El juez de garantía resuelve en audiencia. Garantías: el juez debe verificar que la aceptación sea libre e informada; no puede imponer pena mayor que la solicitada por el fiscal; si absuelve, no puede imputar mayor pena en un juicio posterior. Diferencia con juicio oral: no hay tribunal de juicio oral, no hay producción oral de prueba, el juez valora los antecedentes del fiscal. Crítica: tensión con el principio nemo tenetur.",
        },
        {
            "pregunta": "¿Qué es el amparo ante el juez de garantía (art. 95 CPP)? ¿En qué se diferencia del recurso de amparo constitucional (art. 21 CPR)?",
            "tema": "Amparo Legal vs. Constitucional",
            "pauta": "Amparo legal (art. 95 CPP): acción ante el juez de garantía para impugnar la legalidad de una privación de libertad (detención o arresto). No requiere formalidades; basta comparecer. El juez puede ordenar la libertad o mejorar las condiciones de la detención. Amparo constitucional (art. 21 CPR — hábeas corpus): ante la Corte de Apelaciones; protege la libertad personal frente a actos ilegales o arbitrarios de cualquier autoridad o particular. Diferencias: el art. 95 CPP es específico para imputados en proceso penal; el constitucional es más amplio. Ambos pueden ejercerse simultáneamente.",
        },
        {
            "pregunta": "Explique el recurso de nulidad penal. ¿Cuáles son sus causales? ¿Ante qué tribunal se interpone? ¿Qué sucede si se acoge?",
            "tema": "Recurso de Nulidad Penal",
            "pauta": "Arts. 372-387 CPP. Recurso ordinario contra la sentencia del juicio oral. Causales: (a) infracción sustancial de garantías constitucionales o de tratados (art. 373 letra a); (b) errónea aplicación del derecho con influencia sustancial en el fallo (art. 373 letra b); (c) causales absolutas de nulidad del juicio oral (art. 374, ej: prueba ilícita, falta de quórum del tribunal). Tribunal: letra a y b → CS; causales art. 374 → CA respectiva. Efecto si se acoge: invalidación del juicio y la sentencia; se ordena nuevo juicio oral ante tribunal no inhabilitado. Excepción: si la causal es errónea aplicación del derecho, la CS puede dictar sentencia de reemplazo (art. 385 CPP).",
        },
        {
            "pregunta": "¿Qué son las medidas cautelares reales en el proceso civil? Señale las precautorias del CPC y los requisitos para que el tribunal las conceda.",
            "tema": "Medidas Cautelares Civiles",
            "pauta": "Arts. 290-302 CPC. Medidas precautorias: (1) retención de bienes (dinero u otros); (2) nombramiento de interventor; (3) prohibición de celebrar actos y contratos; (4) secuestro (entrega a un tercero). Requisitos: (1) verosimilitud del derecho (fumus boni iuris) — demostrar que la demanda tiene mérito; (2) peligro en la demora (periculum in mora) — riesgo de que sin la medida el juicio sea ilusorio; (3) caución si el tribunal lo exige (art. 298 CPC). Pueden pedirse antes de la demanda (medidas prejudiciales precautorias) con obligación de demandar en 10 días. Son esencialmente provisionales y revocables.",
        },
    ],

    # ── TECNOLOGÍA Y DERECHO (15) ─────────────────────────────────────────
    "tecnologia_derecho": [
        {
            "pregunta": "Analice la responsabilidad civil por daños causados por sistemas de inteligencia artificial autónomos. ¿Qué normas chilenas aplicarían? ¿Es suficiente el régimen actual frente al Boletín 16821-19?",
            "tema": "IA y Responsabilidad Civil",
            "pauta": "Art. 2329 CC: responsabilidad por el que tiene bajo su cuidado cosa que por su naturaleza puede causar daño. LPDC arts. 44-49: responsabilidad por productos defectuosos (defecto = uso razonablemente esperado no satisfecho al momento de circulación). Boletín 16821-19: clasifica sistemas de IA en riesgo inaceptable, alto riesgo y limitado. Problema: la IA autónoma actúa sin control humano directo; Torres Mac-Pherson (RChDT 2025) distingue daños simples (imputables al operador/desarrollador) y complejos (requieren régimen especial de responsabilidad objetiva). Laguna normativa: Chile no tiene estatuto específico de responsabilidad por IA; aplicar analogía con actividades peligrosas.",
        },
        {
            "pregunta": "Explique el funcionamiento jurídico de los contratos inteligentes (smart contracts) en blockchain y los principales conflictos que generan con el derecho civil chileno.",
            "tema": "Smart Contracts y Derecho Civil",
            "pauta": "Smart contract: protocolo autoejectable codificado en blockchain que se activa automáticamente al cumplirse la condición programada (if-then). Conflictos con el CC: (1) irrevocabilidad vs. condición resolutoria tácita (art. 1489 CC); (2) inmutabilidad del blockchain vs. derecho al olvido en datos personales; (3) dependencia del oráculo para hechos externos — fallo del oráculo genera incerteza; (4) asimetría informativa extrema entre desarrollador y usuario consumidor (Calderón Marenco, RChDT 2025). El PE europeo propuso personería electrónica (2017) pero fue rechazada por el CESE por riesgo moral. En Chile no existe regulación específica; rigen reglas generales del CC.",
        },
        {
            "pregunta": "Desarrolle la responsabilidad penal de las personas jurídicas por delitos informáticos según la Ley 20393 modificada por Ley 21595 y la Ley 21459. ¿Qué es la 'irresponsabilidad organizada'?",
            "tema": "Responsabilidad Penal Corporativa — Delitos Informáticos",
            "pauta": "Ley 21459 (junio 2022): art. 21 extiende la Ley 20393 a las personas jurídicas respecto de los 8 delitos informáticos (acceso ilícito, interceptación, sabotaje, espionaje, fraude, etc.). Ley 21595 (2023): modifica criterio de imputación de 'en beneficio o interés' a 'en el marco de su actividad' — amplía notablemente el ámbito de aplicación. 'Irresponsabilidad organizada' (Schünemann, 1979): en estructuras corporativas complejas la responsabilidad individual se diluye: nadie es responsable porque cada uno decide solo una parte pequeña. Solución: modelo de prevención del delito (art. 4 Ley 20393): identificación de riesgos, protocolos, canal de denuncias, sanciones internas. La certificación del modelo atenúa la responsabilidad de la PJ.",
        },
        {
            "pregunta": "¿Cuál es el contenido de los neuroderechos constitucionales en Chile? Analice la Ley 21383, el Boletín 13828-19 y el caso Girardi con Emotiv Inc.",
            "tema": "Neuroderechos Constitucionales",
            "pauta": "Ley 21383 (2021): primera constitución del mundo en proteger explícitamente la actividad cerebral; reforma art. 19 N°1 CPR → 'la ley protegerá la actividad cerebral y la información proveniente de ella'. Boletín 13828-19 (en tramitación): reconoce cuatro neuroderechos: libertad cognitiva, privacidad mental, integridad mental, identidad personal. Caso Girardi con Emotiv Inc. (CS, rol 105.065-2023): ex-senador obtuvo protección judicial frente a empresa de neurotecnología que recopilaba datos cerebrales; CS revocó la CA Santiago y acogió el recurso de protección. Silva Boggiano & Marchant (RChDT 2025): el deber de información de la LPDC (art. 3 b) es insuficiente para neurotecnologías por la asimetría técnica extrema entre empresa y usuario.",
        },
        {
            "pregunta": "Analice el reconocimiento en Chile de divorcios no judiciales extranjeros según la sentencia CS rol N° 195.161-2023. ¿Qué es el 'equivalente jurisdiccional'? ¿Cuáles son las críticas doctrinarias?",
            "tema": "Divorcios No Judiciales — Reconocimiento Internacional",
            "pauta": "Art. 83 inc. 3° LMC: 'En ningún caso tendrá valor en Chile el divorcio que no haya sido declarado por resolución judicial'. CS rol N°195.161-2023 (4 jun 2024): concedió exequatur a divorcio administrativo colombiano otorgado mediante escritura pública notarial ante notario en Cartagena de Indias. La CS construyó el concepto de 'equivalente jurisdiccional': la escritura pública de divorcio cumple la misma función social que una sentencia judicial, aunque no lo sea formalmente. Cornejo Aguilera (RChDP 2025) critica: (1) genera 'divorcios claudicantes' — válidos en Colombia pero cuestionables en Chile; (2) no aplicable a chilenos (art. 15 CC); (3) no aplicable si los cónyuges tuvieron domicilio en Chile en los 3/5 años anteriores (art. 83 LMC). Laguna normativa: el LMC no contempla esta situación.",
        },
        {
            "pregunta": "¿Qué es la metapericia como prueba atípica en el proceso penal chileno? Distíngala del metaperitaje y de la prueba metapericial. ¿Es admisible?",
            "tema": "Metapericia — Prueba Atípica Procesal",
            "pauta": "Cáceres-Muñoz (UdeC 2025) distingue tres conceptos confundidos por la CS chilena: metapericia = concepto abstracto (representación mental del fenómeno); metaperitaje = actividad concreta de revisión del peritaje original; prueba metapericial = instrumento procesal por el que se introduce el metaperitaje al proceso. La CS chilena (rol N°32047-2024) usa los tres términos como sinónimos. La prueba metapericial es una prueba atípica y compleja (no contemplada en numerus clausus del CPP), pero es admisible por los principios de tutela judicial efectiva y debido proceso (art. 19 N°3 CPR). Admisibilidad: el juez de garantía puede admitirla en la audiencia de preparación si cumple los requisitos de pertinencia, utilidad y licitud (art. 276 CPP).",
        },
        {
            "pregunta": "Analice el consentimiento sexual como thema probandum en el proceso penal. ¿Cuáles son sus características? ¿Qué dificultades probatorias genera?",
            "tema": "Consentimiento Sexual — Prueba Penal",
            "pauta": "Ezurmendia-Álvarez (UdeC 2025) identifica las características del consentimiento sexual: (a) objeto sexual específico; (b) libre y exento de vicios; (c) contextual; (d) dinámico y continuo; (e) esencialmente retractable; (f) unilateral; (g) específico. Modelo afirmativo 'solo sí es sí': SOA 2003 (UK), LO 10/2022 España, Ley 21.675 Chile. Problema probatorio central: el thema probandum es un estado mental (la voluntad de la víctima al momento de los hechos), que raramente deja evidencia objetiva; los delitos ocurren en contextos de intimidad. Injusticia epistémica: los estereotipos sexuales y los 'libretos sexuales' culturales sesgan el razonamiento probatorio de jueces y jurados. Casos complejos: retractación post-coital y stealthing.",
        },
        {
            "pregunta": "¿Cómo se resuelve la tensión entre el derecho al olvido y la inmutabilidad del blockchain en materia de datos personales?",
            "tema": "Datos Personales — Blockchain y Derecho al Olvido",
            "pauta": "Derecho al olvido (GDPR art. 17; Ley 19.628 Chile — en reforma): la persona tiene derecho a solicitar la supresión de sus datos personales. Blockchain: su naturaleza técnica es inmutable (hash previo enlazado con el siguiente); borrar un dato quiebra la cadena. Tensión: los smart contracts y los registros blockchain con datos personales no pueden cumplir el derecho al olvido. Soluciones técnicas: datos off-chain (solo el hash en el blockchain, el dato real en servidor convencional borrable); cifrado con destrucción de clave (el dato queda ilegible aunque permanezca); tokenización. Problema legal: ¿el dato cifrado ilegible equivale al borrado para efectos del GDPR? El RGPD europeo y la doctrina aún debaten este punto.",
        },
        {
            "pregunta": "Analice la calificación jurídica de la relación de trabajo entre los conductores de Uber/Rappi y la plataforma. ¿Cuál es la posición de la Dirección del Trabajo en Chile?",
            "tema": "Plataformas Digitales y Relación Laboral",
            "pauta": "Criterio de laboralidad: subordinación y dependencia (art. 7 CT). Elemento clave: ¿el trabajador está sometido al poder de dirección, control y disciplina del empleador? Plataformas argumentan: independencia del conductor (elige horario, acepta o rechaza pedidos, usa su propio vehículo). Dirección del Trabajo: Ordinario N°1388/2017 reconoció indicios de laboralidad en algunas plataformas (control por rating, algoritmos de asignación, tarifas unilaterales). Ley de plataformas digitales pendiente en Chile (al 2025): busca un estatuto sui generis. Derecho comparado: Tribunal Supremo del Reino Unido (Uber BV v Aslam, 2021) declaró a los conductores 'workers' con derechos mínimos. En Chile la tendencia jurisprudencial es reconocer laboralidad cuando el algoritmo controla efectivamente la prestación.",
        },
        {
            "pregunta": "Desarrolle la titularidad de los derechos de autor sobre obras generadas por inteligencia artificial. ¿Puede la IA ser titular? ¿Qué dice la Ley 17.336?",
            "tema": "IA y Derechos de Autor",
            "pauta": "Ley 17.336 (Propiedad Intelectual chilena): el autor es la persona natural que crea la obra. No reconoce titularidad a entes no humanos. IA generativa: la obra generada por IA plantea tres posibilidades de titularidad: (1) el programador de la IA (creador del sistema); (2) el usuario que diseñó el prompt (autor instrumental); (3) nadie — la obra cae en dominio público. OMPI (2023): posición mayoritaria es que la IA no puede ser titular; los derechos recaen en el ser humano con rol creativo. En Chile: el Departamento de Propiedad Intelectual (DIBAM) exige autoría humana. Problema práctico: con prompts básicos, la contribución humana es mínima; con prompts elaborados, puede reconocerse.",
        },
        {
            "pregunta": "¿Qué normas penales chilenas aplican al acoso y hostigamiento digital? Analice los tipos de la Ley 21459 y otros instrumentos legales.",
            "tema": "Acoso Digital — Derecho Penal",
            "pauta": "Ley 21459 contempla: acceso ilícito a sistemas (art. 2), interceptación de comunicaciones privadas (art. 3), fraude informático (art. 7). Acoso en redes: puede configurar amenazas (art. 296 CP), injurias/calumnias (arts. 413 y 412 CP) o el delito de acoso sexual (art. 494 ter CP). Ley 21.400 (2022): incorpora el delito de difusión no consentida de imágenes íntimas (art. 161-C CP — 'revenge porn'). Ciberacoso escolar: regulado en Ley 20.536. Gap normativo: Chile carece de un tipo específico de 'ciberacoso' o 'stalking' digital como el que existe en Alemania (§238 StGB) o España (art. 172 ter CP). Proyecto de ley de acoso digital (Boletín 14.305) en tramitación al 2025.",
        },
        {
            "pregunta": "¿Cuándo se perfecciona un contrato celebrado por medios electrónicos en Chile? ¿Qué ley lo regula? ¿Cómo opera la firma electrónica?",
            "tema": "Contratación Electrónica",
            "pauta": "Ley 19.799 (2002): regula los documentos y firmas electrónicas. Perfeccionamiento: según las reglas generales del CC (art. 1545) — la aceptación produce efectos desde que el oferente toma conocimiento de ella (teoría del conocimiento). Excepción: en contratos entre presentes electrónicos (chat en tiempo real), la aceptación opera en el momento en que es enviada. Firma electrónica simple: cualquier símbolo o proceso electrónico. Firma electrónica avanzada: basada en certificado digital; tiene el mismo valor que la firma manuscrita (art. 3 Ley 19.799). Documentos electrónicos: tienen el mismo valor probatorio que los documentos escritos (art. 5 Ley 19.799). LPDC aplica plenamente al e-commerce.",
        },
        {
            "pregunta": "Desarrolle el deepfake como problema jurídico. ¿Qué tipos penales y civiles aplican en Chile cuando se usa deepfake para difamar o crear pornografía no consensual?",
            "tema": "Deepfakes — Responsabilidad Civil y Penal",
            "pauta": "Deepfake: video o imagen hiperrealista generado por IA que muestra a una persona realizando acciones que no realizó. Tipos penales aplicables: (1) calumnias (art. 412 CP) o injurias (art. 413 CP) si se atribuyen hechos falsos deshonrosos; (2) difusión no consensual de imágenes íntimas (art. 161-C CP — Ley 21.400) si el deepfake tiene contenido sexual; (3) amenazas o extorsión si se usa para coaccionar. Responsabilidad civil extracontractual: daño moral por vulneración al honor, imagen e intimidad (art. 2314 CC). Derecho a la imagen (Ley 19.628): uso no autorizado de la imagen de una persona genera responsabilidad. Gap: Chile no tipifica expresamente el deepfake difamatorio.",
        },
        {
            "pregunta": "Analice el tratamiento masivo de datos personales (big data) y sus implicancias para la Ley 19.628 en reforma. ¿Cuáles son las bases legales para tratar datos sin consentimiento?",
            "tema": "Big Data y Datos Personales",
            "pauta": "Ley 19.628 (1999) en reforma (Proyecto de Ley de Datos Personales, Boletín 11144): adapta el estándar GDPR al derecho chileno. Principios: licitud, finalidad, proporcionalidad, calidad de los datos, seguridad. Bases legales de tratamiento (además del consentimiento): (1) cumplimiento de obligación legal; (2) ejecución de contrato; (3) interés vital del titular; (4) interés legítimo del responsable (siempre que no prevalezcan los derechos del titular). Big data: el tratamiento masivo y analítico de datos anonimizados genera tensión con el principio de finalidad (los datos se usan para fines distintos al original). El proyecto de reforma establece el derecho a no ser objeto de decisiones automatizadas con efectos significativos (equivalente al art. 22 GDPR).",
        },
        {
            "pregunta": "¿Cuál es la naturaleza jurídica de las criptomonedas en el derecho civil chileno? ¿Son bienes? ¿Pueden ser objeto de dominio, prenda, embargo?",
            "tema": "Criptomonedas — Naturaleza Jurídica",
            "pauta": "Chile no tiene ley que defina la naturaleza de las criptomonedas. Análisis civilístico: ¿son cosas corporales o incorporales? No tienen soporte material propio → son incorporales. ¿Son derechos reales o personales? No recaen sobre personas determinadas → podrían asimilarse a derechos reales sobre cosa incorporal (cuestionado). Postura dominante: las criptomonedas son bienes incorporales susceptibles de apropiación privada (art. 565 CC), comerciables y transferibles. Consecuencias prácticas: pueden ser objeto de prenda (Ley 20.190 — prenda sin desplazamiento); pueden embargarse como especie determinada o como equivalente en dinero. CMF reconoce ciertos tokens como valores mobiliarios (art. 3 Ley 18.045). No son moneda de curso legal.",
        },
    ],
}
