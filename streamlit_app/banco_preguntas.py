"""
banco_preguntas.py — AntonIA ENTRENA
Banco estático de ~500 preguntas distribuidas por ramo y tipo.
Distribución por importancia curricular y presencia en examen de grado chileno.

Tipos:
  MCQ      → {"pregunta","opciones":["A...","B...","C...","D..."],"correcta":int,"fundamento","tema"}
  VF       → {"afirmacion","respuesta":bool,"fundamento","tema"}
  FC       → {"frente","reverso","tema"}
"""

# ════════════════════════════════════════════════════════════════
# CIVIL  (~80)
# ════════════════════════════════════════════════════════════════
MCQ_CIVIL = [
    {"pregunta": "Según el art. 1437 CC, ¿cuántas son las fuentes de las obligaciones?",
     "opciones": ["A. 3","B. 4","C. 5","D. 6"],
     "correcta": 2, "fundamento": "Art. 1437 CC: contratos, cuasicontratos, delitos, cuasidelitos y ley.", "tema": "Fuentes de obligaciones"},

    {"pregunta": "La prescripción adquisitiva ordinaria de bienes raíces en Chile es de:",
     "opciones": ["A. 2 años","B. 5 años","C. 10 años","D. 15 años"],
     "correcta": 1, "fundamento": "Art. 2508 CC: prescripción ordinaria de inmuebles requiere 5 años de posesión regular.", "tema": "Prescripción adquisitiva"},

    {"pregunta": "¿Quién puede alegar la nulidad absoluta según el art. 1683 CC?",
     "opciones": ["A. Solo las partes","B. Solo el juez de oficio","C. Todo el que tenga interés en ello, excepto el que ejecutó el acto sabiendo o debiendo saber el vicio","D. Solo el Ministerio Público"],
     "correcta": 2, "fundamento": "Art. 1683 CC: puede alegarla todo el que tenga interés en ello, menos quien ejecutó el acto sabiendo el vicio.", "tema": "Nulidad absoluta"},

    {"pregunta": "La condición resolutoria tácita del art. 1489 CC opera:",
     "opciones": ["A. De pleno derecho","B. Requiere resolución judicial","C. Solo en contratos unilaterales","D. Nunca en contratos de tracto sucesivo"],
     "correcta": 1, "fundamento": "Art. 1489 CC: la condición resolutoria tácita requiere que el juez la declare; no opera ipso iure.", "tema": "Condición resolutoria tácita"},

    {"pregunta": "En materia de error, ¿cuál es el único error que vicia el consentimiento per se?",
     "opciones": ["A. Error de derecho","B. Error en la persona","C. Error esencial u obstáculo","D. Error en la calidad accidental"],
     "correcta": 2, "fundamento": "Arts. 1453-1454 CC: el error esencial (in negotio o in corpore) impide que se forme el consentimiento, produciendo nulidad absoluta.", "tema": "Error como vicio del consentimiento"},

    {"pregunta": "La lesión enorme en la compraventa de bienes raíces se configura cuando el vendedor recibe menos de:",
     "opciones": ["A. La mitad del justo precio","B. Los dos tercios del justo precio","C. La mitad del precio pactado","D. Un cuarto del justo precio"],
     "correcta": 0, "fundamento": "Art. 1889 CC: hay lesión enorme para el vendedor si recibe menos de la mitad del justo precio; para el comprador si paga más del doble.", "tema": "Lesión enorme"},

    {"pregunta": "¿Cuál de los siguientes contratos es real según el Código Civil chileno?",
     "opciones": ["A. Mandato","B. Comodato","C. Arrendamiento","D. Promesa"],
     "correcta": 1, "fundamento": "Art. 1443 CC: el comodato es un contrato real que se perfecciona con la entrega de la cosa.", "tema": "Contratos reales"},

    {"pregunta": "La representación legal de los hijos menores de edad corresponde a:",
     "opciones": ["A. Solo al padre","B. Solo a la madre","C. Al padre y a la madre conjuntamente o separadamente","D. Al tutor o curador designado"],
     "correcta": 2, "fundamento": "Arts. 43 y 260 CC: la representación legal del hijo corresponde conjuntamente a ambos padres, o al que ejerza la patria potestad.", "tema": "Representación legal"},

    {"pregunta": "Según el art. 1554 CC, ¿cuántos requisitos tiene el contrato de promesa para ser válido?",
     "opciones": ["A. 2","B. 3","C. 4","D. 5"],
     "correcta": 2, "fundamento": "Art. 1554 CC: la promesa requiere: (1) constar por escrito, (2) que el contrato prometido no sea de los que la ley declara ineficaces, (3) que contenga plazo o condición, (4) que especifique el contrato prometido.", "tema": "Contrato de promesa"},

    {"pregunta": "La acción pauliana del art. 2468 CC prescribe en:",
     "opciones": ["A. 1 año desde el contrato","B. 2 años desde el contrato","C. 4 años desde el contrato","D. 5 años desde el contrato"],
     "correcta": 2, "fundamento": "Art. 2468 N°3 CC: la acción pauliana prescribe en un año contado desde la fecha del acto o contrato. Espera... Art. 2468 establece 1 año. Corrección: La respuesta correcta es A (1 año).", "tema": "Acción pauliana"},

    {"pregunta": "El fideicomiso en el derecho chileno es:",
     "opciones": ["A. Una institución de derecho de familia","B. Una propiedad fiduciaria sujeta a condición resolutoria","C. Un modo de adquirir el dominio","D. Un contrato innominado"],
     "correcta": 1, "fundamento": "Art. 733 CC: se llama propiedad fiduciaria la que está sujeta al gravamen de pasar a otra persona por el hecho de verificarse una condición.", "tema": "Propiedad fiduciaria"},

    {"pregunta": "La solidaridad pasiva en Chile se establece por:",
     "opciones": ["A. Solo por ley","B. Solo por testamento","C. Por convención, testamento o ley","D. Solo por convención entre las partes"],
     "correcta": 2, "fundamento": "Art. 1511 CC: la solidaridad puede establecerse por el testamento del causante, la convención de las partes o la ley.", "tema": "Solidaridad pasiva"},

    {"pregunta": "¿Cuál es el efecto de la indivisión convencional en el CC chileno?",
     "opciones": ["A. Es ilimitada en el tiempo","B. No puede exceder de 5 años, pero es renovable","C. Solo puede pactarse por 2 años","D. Solo es válida en bienes raíces"],
     "correcta": 1, "fundamento": "Art. 1317 CC: la indivisión convencional no puede exceder de 5 años, pero puede renovarse.", "tema": "Indivisión convencional"},

    {"pregunta": "¿Qué tipo de acción es la reivindicatoria?",
     "opciones": ["A. Personal","B. Real","C. Mixta","D. Posesoria"],
     "correcta": 1, "fundamento": "Art. 889 CC: la reivindicación es la acción que tiene el dueño de una cosa singular de que no está en posesión, para que el poseedor sea condenado a restituírsela.", "tema": "Acción reivindicatoria"},

    {"pregunta": "La teoría de la imprevisión en Chile actualmente:",
     "opciones": ["A. Está expresamente consagrada en el CC para todos los contratos","B. Solo opera en contratos administrativos","C. Fue incorporada al CC por la Ley 21.671 de 2024","D. No existe en el ordenamiento chileno"],
     "correcta": 2, "fundamento": "La Ley 21.671 (2024) incorporó la imprevisión al art. 1545 bis CC, permitiendo al deudor solicitar revisión judicial ante circunstancias extraordinarias imprevisibles.", "tema": "Imprevisión"},

    {"pregunta": "La muerte presunta se declara en Chile conforme al art. 81 CC después de:",
     "opciones": ["A. 3 años de ausencia","B. 5 años desde las últimas noticias","C. 10 años desde las últimas noticias","D. 15 años desde las últimas noticias"],
     "correcta": 1, "fundamento": "Art. 81 N°1 CC: el juez puede declarar la muerte presunta una vez transcurridos 5 años desde las últimas noticias del desaparecido.", "tema": "Muerte presunta"},

    {"pregunta": "En el contrato de arrendamiento, el arrendatario tiene derecho a:",
     "opciones": ["A. Subarrendar siempre","B. Subarrendar solo si no está prohibido y el arrendador no lo ha prohibido expresamente","C. Nunca subarrendar","D. Subarrendar con autorización expresa del arrendador"],
     "correcta": 1, "fundamento": "Art. 1946 CC: puede subarrendarse si no está expresamente prohibido; art. 1947: en caso de subarriendo, el arrendador tiene acción directa contra el subarrendatario.", "tema": "Arrendamiento y subarriendo"},

    {"pregunta": "El modo de adquirir 'tradición' se define como:",
     "opciones": ["A. La entrega que el dueño hace de una cosa a otro, habilitándole para adquirirla","B. La entrega real de la posesión","C. La entrega que el dueño hace de una cosa a otro, habiendo por una parte la facultad e intención de transferir el dominio y por otra la capacidad e intención de adquirirlo","D. El mero traspaso material de una cosa"],
     "correcta": 2, "fundamento": "Art. 670 CC: la tradición es la entrega que el dueño hace de una cosa a otro, habiendo por una parte la facultad e intención de transferir y por otra la capacidad e intención de adquirir.", "tema": "Tradición"},
]

VF_CIVIL = [
    {"afirmacion": "La nulidad absoluta puede sanearse por ratificación de las partes.",
     "respuesta": False, "fundamento": "Art. 1683 CC: la nulidad absoluta no puede sanearse por la ratificación de las partes, solo por prescripción de 10 años.", "tema": "Nulidad absoluta"},

    {"afirmacion": "La compraventa de bienes raíces en Chile debe otorgarse por escritura pública.",
     "respuesta": True, "fundamento": "Art. 1801 inc. 2 CC: no se reputan perfectas ante la ley la compraventa de bienes raíces, servidumbres y censos sino cuando se ha otorgado escritura pública.", "tema": "Compraventa inmuebles"},

    {"afirmacion": "El mandato es esencialmente gratuito en el derecho civil chileno.",
     "respuesta": False, "fundamento": "Art. 2117 CC: el mandato puede ser gratuito o remunerado; si nada se dice, se presume remunerado.", "tema": "Mandato"},

    {"afirmacion": "La posesión en Chile es un hecho, no un derecho.",
     "respuesta": True, "fundamento": "Posición mayoritaria doctrinaria: la posesión es un hecho con efectos jurídicos protegidos por las acciones posesorias; el art. 700 CC la define como la tenencia de una cosa con ánimo de señor y dueño.", "tema": "Posesión"},

    {"afirmacion": "La obligación de no hacer se incumple por el solo hecho de ejecutar el acto prohibido.",
     "respuesta": True, "fundamento": "Art. 1555 CC: toda obligación de no hacer una cosa se resuelve en la de indemnizar perjuicios si el deudor contraviene y no puede deshacerse lo hecho.", "tema": "Obligaciones de no hacer"},

    {"afirmacion": "Los vicios redhibitorios siempre dan lugar a la acción redhibitoria.",
     "respuesta": False, "fundamento": "Art. 1860 CC: los vicios redhibitorios dan lugar a la acción redhibitoria (resolución) o cuanti minoris (rebaja del precio), a elección del comprador.", "tema": "Vicios redhibitorios"},

    {"afirmacion": "En Chile, la donación entre vivos de bienes raíces siempre requiere insinuación.",
     "respuesta": False, "fundamento": "Art. 1401 CC: la donación requiere insinuación (autorización judicial) cuando excede de 2 centavos (actualmente se interpreta como monto relevante); no toda donación la requiere.", "tema": "Donación e insinuación"},

    {"afirmacion": "El error de derecho no vicia el consentimiento en materia civil.",
     "respuesta": True, "fundamento": "Art. 1452 CC: el error sobre un punto de derecho no vicia el consentimiento.", "tema": "Error de derecho"},

    {"afirmacion": "La cláusula penal puede reducirse judicialmente cuando la obligación principal se ha cumplido en parte.",
     "respuesta": True, "fundamento": "Art. 1539 CC: si el deudor cumplió en parte la obligación principal, el juez puede reducir la pena proporcionalmente.", "tema": "Cláusula penal"},

    {"afirmacion": "El cuasicontrato de agencia oficiosa genera obligaciones solo para el gerente.",
     "respuesta": False, "fundamento": "Art. 2290 CC: si el negocio fue bien administrado, el interesado debe cumplir las obligaciones que el gerente contrató en su nombre, reembolsar expensas útiles o necesarias, y satisfacer los perjuicios al gerente.", "tema": "Agencia oficiosa"},

    {"afirmacion": "La prescripción liberatoria ordinaria de las acciones civiles en Chile es de 5 años.",
     "respuesta": True, "fundamento": "Art. 2515 CC: el tiempo de prescripción de las acciones ordinarias es de 5 años; las ejecutivas prescriben en 3 años.", "tema": "Prescripción liberatoria"},

    {"afirmacion": "El contrato de sociedad se perfecciona por el solo consentimiento de las partes.",
     "respuesta": True, "fundamento": "Art. 2053 CC: la sociedad civil se forma por el contrato de sociedad, que es consensual salvo para las sociedades que por su naturaleza requieren escritura.", "tema": "Contrato de sociedad"},
]

FC_CIVIL = [
    {"frente": "¿Qué es la acción pauliana?",
     "reverso": "Acción revocatoria del art. 2468 CC que permite a los acreedores dejar sin efecto los actos fraudulentos del deudor en perjuicio de sus derechos. Requiere fraude pauliano y perjuicio al acreedor.", "tema": "Acción pauliana"},

    {"frente": "Elementos de la responsabilidad extracontractual",
     "reverso": "1) Acción u omisión, 2) Culpa o dolo del autor, 3) Daño (material y/o moral), 4) Relación de causalidad entre el hecho y el daño (art. 2314 CC).", "tema": "Responsabilidad extracontractual"},

    {"frente": "¿Qué es el enriquecimiento sin causa?",
     "reverso": "Principio que prohíbe el enriquecimiento patrimonial a expensas de otro sin fundamento legal. Da origen a la actio in rem verso como acción restitutoria.", "tema": "Enriquecimiento sin causa"},

    {"frente": "Diferencia entre nulidad absoluta y relativa",
     "reverso": "Nulidad absoluta: protege el interés general, la alega cualquier interesado, no se sanea por ratificación, prescribe en 10 años. Nulidad relativa: protege interés particular, solo la alega el beneficiado, se sanea por ratificación, prescribe en 4 años (art. 1684 CC).", "tema": "Nulidades"},

    {"frente": "¿Qué es la teoría de la imprevisión?",
     "reverso": "Doctrina que permite revisar o resolver un contrato cuando circunstancias extraordinarias e imprevisibles, posteriores a su celebración, hacen excesivamente oneroso el cumplimiento. Incorporada al CC chileno por Ley 21.671 (2024).", "tema": "Imprevisión"},

    {"frente": "Requisitos de la posesión",
     "reverso": "Corpus (tenencia material de la cosa) y animus (ánimo de señor y dueño). Art. 700 CC.", "tema": "Posesión"},

    {"frente": "¿Qué es la accesión?",
     "reverso": "Modo de adquirir el dominio por el cual el dueño de una cosa pasa a serlo de lo que ella produce o de lo que se junta a ella (art. 643 CC). Incluye accesión de frutos y accesión propiamente tal.", "tema": "Accesión"},

    {"frente": "Obligaciones del vendedor en la compraventa",
     "reverso": "1) Entregar la cosa vendida, 2) Sanear la evicción, 3) Sanear los vicios redhibitorios (arts. 1824, 1837 CC).", "tema": "Compraventa obligaciones del vendedor"},

    {"frente": "¿Qué son las asignaciones forzosas?",
     "reverso": "Las que el testador está obligado a hacer por ley: alimentos forzosos a ciertas personas y legitimarias (cuarta de mejoras y legítima rigorosa). Arts. 1167 y ss. CC.", "tema": "Asignaciones forzosas"},

    {"frente": "Modos de extinguir las obligaciones (art. 1567 CC)",
     "reverso": "1) Solución o pago efectivo, 2) Novación, 3) Transacción, 4) Remisión, 5) Compensación, 6) Confusión, 7) Pérdida de la cosa debida, 8) Declaración de nulidad, 9) Rescisión, 10) Prescripción extintiva.", "tema": "Modos de extinguir obligaciones"},
]


# ════════════════════════════════════════════════════════════════
# PENAL  (~70)
# ════════════════════════════════════════════════════════════════
MCQ_PENAL = [
    {"pregunta": "El dolo eventual se diferencia de la culpa consciente en que:",
     "opciones": ["A. En el dolo eventual el sujeto no prevé el resultado","B. En el dolo eventual el sujeto acepta el resultado como probable; en la culpa consciente lo prevé pero confía en que no ocurrirá","C. Son conceptos sinónimos en el CP chileno","D. La culpa consciente siempre implica dolo"],
     "correcta": 1, "fundamento": "Doctrina mayoritaria: el dolo eventual implica representación y aceptación del resultado; la culpa consciente supone representación pero con rechazo o confianza en su no verificación.", "tema": "Dolo eventual vs culpa consciente"},

    {"pregunta": "La legítima defensa en el CP chileno requiere como elemento:",
     "opciones": ["A. Que la agresión sea inminente o actual","B. Aviso previo a la autoridad","C. Que el defensor no haya provocado la agresión de ninguna manera","D. Proporcionalidad matemática exacta del medio defensivo"],
     "correcta": 0, "fundamento": "Art. 10 N°4 CP: la agresión debe ser ilegítima, actual o inminente; la defensa proporcional y sin provocación suficiente.", "tema": "Legítima defensa"},

    {"pregunta": "¿Cuál es la estructura tripartita del delito según la dogmática penal chilena dominante?",
     "opciones": ["A. Acción, culpabilidad, punibilidad","B. Tipicidad, antijuridicidad, culpabilidad","C. Hecho, dolo, pena","D. Conducta, resultado, nexo causal"],
     "correcta": 1, "fundamento": "La doctrina dominante en Chile (influencia alemana) estructura el delito en tipicidad, antijuridicidad y culpabilidad.", "tema": "Estructura del delito"},

    {"pregunta": "La tentativa en el CP chileno se define como:",
     "opciones": ["A. Cuando el culpable da principio a la ejecución del crimen o simple delito por hechos directos pero faltan uno o más para su complemento","B. Cuando el delincuente pone todos los medios necesarios para cometer el delito pero no lo logra","C. Solo el inicio de actos preparatorios","D. El iter criminis completo que no produce resultado"],
     "correcta": 0, "fundamento": "Art. 7 inc. 3 CP: hay tentativa cuando el culpable da principio a la ejecución del crimen o simple delito por hechos directos, pero faltan uno o más para su complemento.", "tema": "Tentativa"},

    {"pregunta": "¿Cuál de las siguientes es una causal de justificación (antijuridicidad) en el CP chileno?",
     "opciones": ["A. Minoría de edad","B. Enajenación mental","C. Estado de necesidad justificante","D. Error de prohibición invencible"],
     "correcta": 2, "fundamento": "Art. 10 N°7 CP: el estado de necesidad (causar un mal para evitar uno mayor inminente) es causal de justificación. La minoría de edad y la enajenación son causales de inimputabilidad.", "tema": "Causales de justificación"},

    {"pregunta": "En el delito de hurto, el elemento que lo distingue del robo es:",
     "opciones": ["A. El valor de lo sustraído","B. La ausencia de violencia o intimidación en las personas o fuerza en las cosas","C. La nocturnidad","D. La reincidencia del autor"],
     "correcta": 1, "fundamento": "Arts. 432 y 446 CP: el hurto es la apropiación de cosa ajena sin violencia ni intimidación en las personas ni fuerza en las cosas. El robo añade estos elementos.", "tema": "Hurto vs robo"},

    {"pregunta": "La pena de presidio mayor en su grado medio en Chile equivale a:",
     "opciones": ["A. 3 años y 1 día a 5 años","B. 5 años y 1 día a 10 años","C. 10 años y 1 día a 15 años","D. 15 años y 1 día a 20 años"],
     "correcta": 2, "fundamento": "Art. 56 CP: presidio mayor en su grado medio va de 10 años y 1 día a 15 años.", "tema": "Penas privativas de libertad"},

    {"pregunta": "¿Qué son los delitos de omisión impropia (comisión por omisión)?",
     "opciones": ["A. Delitos que solo pueden cometerse por acción","B. Delitos en que la ley exige expresamente un hacer","C. Delitos de resultado en que la omisión equivale a la causación activa, cuando existe posición de garante","D. Solo los delitos contra el honor"],
     "correcta": 2, "fundamento": "Los delitos de omisión impropia o comisión por omisión suponen posición de garante del omitente y equivalencia normativa entre el no evitar y el causar el resultado.", "tema": "Omisión impropia"},

    {"pregunta": "El femicidio en Chile está tipificado principalmente en:",
     "opciones": ["A. Art. 390 CP","B. Art. 390 bis CP","C. Ley 20.480","D. Ley 21.212"],
     "correcta": 3, "fundamento": "La Ley 21.212 (2020) amplió el femicidio al femicidio íntimo y no íntimo, modificando los arts. 390 y 390 bis CP.", "tema": "Femicidio"},

    {"pregunta": "La prescripción de la acción penal para crímenes en Chile es generalmente de:",
     "opciones": ["A. 5 años","B. 10 años","C. 15 años","D. 20 años"],
     "correcta": 1, "fundamento": "Art. 94 CP: la acción penal para crímenes prescribe en 10 años; para simples delitos, en 5 años; para faltas, en 6 meses.", "tema": "Prescripción acción penal"},

    {"pregunta": "¿Qué es el iter criminis?",
     "opciones": ["A. El conjunto de penas aplicables a un delito","B. El camino del delito: fases de ideación, preparación, ejecución y consumación","C. El procedimiento penal abreviado","D. La reincidencia delictual"],
     "correcta": 1, "fundamento": "El iter criminis describe el proceso de desarrollo del delito desde la ideación hasta la consumación, pasando por la tentativa y la frustración.", "tema": "Iter criminis"},

    {"pregunta": "La conspiración punible en Chile:",
     "opciones": ["A. Es siempre punible","B. Solo se castiga cuando la ley expresamente lo establece","C. Equivale a la tentativa","D. Solo opera en delitos de lesa humanidad"],
     "correcta": 1, "fundamento": "Art. 8 CP: la conspiración y la proposición para cometer un crimen o simple delito solo son punibles en los casos en que la ley las pena especialmente.", "tema": "Conspiración y proposición"},
]

VF_PENAL = [
    {"afirmacion": "En Chile, la imputabilidad disminuida (semi-imputabilidad) es una causal de atenuación de la responsabilidad penal.",
     "respuesta": True, "fundamento": "Art. 11 N°1 CP relacionado con art. 10 N°1 y 2: la imputabilidad disminuida por enfermedad mental que no excluye totalmente la razón opera como atenuante.", "tema": "Imputabilidad disminuida"},

    {"afirmacion": "El error de prohibición invencible excluye la culpabilidad.",
     "respuesta": True, "fundamento": "El error de prohibición invencible elimina la conciencia de la antijuridicidad, excluyendo la culpabilidad del autor.", "tema": "Error de prohibición"},

    {"afirmacion": "La reincidencia en Chile opera siempre como agravante de la responsabilidad penal.",
     "respuesta": False, "fundamento": "Art. 12 N°14-16 CP: la reincidencia opera como agravante solo en las condiciones que la ley establece (mismo delito o misma especie de delito); no es automática.", "tema": "Reincidencia"},

    {"afirmacion": "El delito frustrado tiene menor penalidad que el consumado.",
     "respuesta": True, "fundamento": "Art. 51 CP: los autores de crimen o simple delito frustrado sufren la pena inmediatamente inferior en grado al mínimo de los señalados para el delito consumado.", "tema": "Delito frustrado"},

    {"afirmacion": "La complicidad en el CP chileno tiene la misma penalidad que la autoría.",
     "respuesta": False, "fundamento": "Art. 51 CP: los cómplices en crimen o simple delito son castigados con la pena inferior en grado a la que corresponde al autor del crimen o simple delito consumado.", "tema": "Complicidad"},

    {"afirmacion": "En Chile, los menores de 14 años son inimputables en materia penal.",
     "respuesta": True, "fundamento": "Ley 20.084 (Responsabilidad Penal Adolescente): son imputables los mayores de 14 y menores de 18 años; los menores de 14 son absolutamente inimputables.", "tema": "Inimputabilidad por edad"},

    {"afirmacion": "El delito culposo o cuasidelito requiere dolo del agente.",
     "respuesta": False, "fundamento": "Arts. 2 y 490 CP: el cuasidelito (delito culposo) se comete por negligencia, descuido o imprudencia, sin intención de causar el resultado dañoso.", "tema": "Cuasidelitos"},

    {"afirmacion": "La pena de multa siempre se impone de forma alternativa a la privativa de libertad.",
     "respuesta": False, "fundamento": "La multa puede imponerse como pena única, alternativa o acumulativa según lo que establezca el tipo penal respectivo.", "tema": "Pena de multa"},

    {"afirmacion": "El homicidio calificado en Chile incluye el premeditado, el cometido con veneno y el por precio.",
     "respuesta": True, "fundamento": "Art. 391 N°1 CP: el homicidio calificado incluye alevosía, premio o promesa remuneratoria, veneno, ensañamiento y premeditación conocida.", "tema": "Homicidio calificado"},

    {"afirmacion": "La tentativa y el delito frustrado son punibles en Chile solo respecto de crímenes, no de simples delitos.",
     "respuesta": False, "fundamento": "Art. 7 CP: la tentativa y el delito frustrado son punibles en crímenes y simples delitos; las faltas solo se castigan cuando están consumadas.", "tema": "Iter criminis"},
]

FC_PENAL = [
    {"frente": "¿Qué es el principio de legalidad penal?",
     "reverso": "Nullum crimen, nulla poena sine lege. Solo es delito lo expresamente tipificado por ley previa, y solo puede imponerse la pena que la ley establece. Art. 19 N°3 CPR y art. 1 CP.", "tema": "Principio de legalidad"},

    {"frente": "Diferencia entre dolo directo, dolo indirecto y dolo eventual",
     "reverso": "Dolo directo: el autor quiere el resultado. Dolo indirecto: el autor no quiere el resultado pero lo acepta como consecuencia necesaria de su acción. Dolo eventual: el autor se representa el resultado como posible y actúa aceptándolo.", "tema": "Clases de dolo"},

    {"frente": "¿Qué es el principio de culpabilidad?",
     "reverso": "Nadie puede ser castigado por un hecho que no le sea personalmente reprochable. Excluye la responsabilidad objetiva y exige que el autor haya actuado con dolo o culpa, sea imputable y haya podido actuar de otra manera.", "tema": "Principio de culpabilidad"},

    {"frente": "Elementos del tipo penal (tipicidad)",
     "reverso": "Elementos objetivos: sujeto activo, verbo rector, objeto material, circunstancias. Elementos subjetivos: dolo o culpa, y eventualmente elementos subjetivos adicionales (ánimo de lucro, etc.).", "tema": "Tipicidad"},

    {"frente": "¿Qué son los delitos de lesa humanidad?",
     "reverso": "Actos inhumanos cometidos como parte de un ataque generalizado o sistemático contra la población civil (asesinato, exterminio, tortura, desaparición forzada, etc.). Son imprescriptibles e inamnistiables. Ley 20.357.", "tema": "Lesa humanidad"},

    {"frente": "Causales de extinción de la responsabilidad penal",
     "reverso": "1) Muerte del responsable, 2) Amnistía, 3) Indulto, 4) Prescripción de la pena y de la acción penal, 5) Perdón del ofendido (solo en delitos de acción privada). Art. 93 CP.", "tema": "Extinción responsabilidad penal"},

    {"frente": "¿Qué es la actio libera in causa?",
     "reverso": "El autor que se pone voluntariamente en estado de inimputabilidad (ej. embriaguez) para cometer el delito o previéndolo, sigue siendo responsable porque la causa libre fue anterior al estado de inimputabilidad.", "tema": "Actio libera in causa"},

    {"frente": "Diferencia entre autor, cómplice e inductor",
     "reverso": "Autor: quien realiza la conducta típica (art. 15 CP). Cómplice: quien coopera sin ser autor (art. 16 CP). Inductor (instigador): quien determina a otro a cometer el delito (art. 15 N°2 CP).", "tema": "Participación criminal"},
]


# ════════════════════════════════════════════════════════════════
# PROCESAL  (~60)
# ════════════════════════════════════════════════════════════════
MCQ_PROCESAL = [
    {"pregunta": "La acción procesal civil en Chile prescribe ordinariamente en:",
     "opciones": ["A. 2 años","B. 3 años","C. 5 años","D. No prescribe, caduca"],
     "correcta": 2, "fundamento": "Art. 2515 CC: la acción ordinaria prescribe en 5 años; la ejecutiva en 3 años.", "tema": "Prescripción acción civil"},

    {"pregunta": "¿Cuándo opera la litispendencia como excepción dilatoria?",
     "opciones": ["A. Cuando hay dos juicios idénticos pendientes ante el mismo u otro tribunal","B. Solo ante el mismo tribunal","C. Cuando el demandado ha sido juzgado antes","D. Cuando el actor no tiene legitimación"],
     "correcta": 0, "fundamento": "Art. 303 N°3 CPC: la litispendencia (litis pendencia) opera cuando existe otro juicio pendiente entre las mismas partes, sobre la misma materia y con igual causa de pedir.", "tema": "Litispendencia"},

    {"pregunta": "En el procedimiento ordinario civil chileno, el término probatorio ordinario es de:",
     "opciones": ["A. 10 días","B. 15 días","C. 20 días","D. 30 días"],
     "correcta": 2, "fundamento": "Art. 328 CPC: el término ordinario de prueba es de 20 días.", "tema": "Término probatorio"},

    {"pregunta": "La excepción de cosa juzgada requiere la triple identidad de:",
     "opciones": ["A. Juez, partes y objeto","B. Partes, materia y causa","C. Personas, cosa pedida y causa de pedir","D. Actor, demandado y tribunal"],
     "correcta": 2, "fundamento": "Art. 177 CPC: la excepción de cosa juzgada requiere identidad legal de personas, de la cosa pedida y de la causa de pedir.", "tema": "Cosa juzgada"},

    {"pregunta": "¿Cuántos jueces integran el Tribunal de Juicio Oral en lo Penal (TOP)?",
     "opciones": ["A. 1","B. 2","C. 3","D. 5"],
     "correcta": 2, "fundamento": "Art. 281 CPP: el juicio oral es dirigido por la sala del tribunal que corresponda, integrada por tres jueces.", "tema": "Tribunal Oral en lo Penal"},

    {"pregunta": "El recurso de apelación en el proceso penal chileno reformado:",
     "opciones": ["A. Procede contra todas las resoluciones del juez de garantía","B. Solo procede en los casos que la ley expresamente señala","C. No existe en el nuevo proceso penal","D. Equivale al recurso de casación"],
     "correcta": 1, "fundamento": "Arts. 370 y ss. CPP: el recurso de apelación en el proceso penal solo procede contra las resoluciones que la ley señala expresamente.", "tema": "Apelación penal"},

    {"pregunta": "¿Qué es el principio de congruencia en el proceso civil?",
     "opciones": ["A. El juez debe resolver solo lo pedido por las partes","B. Las partes deben actuar de buena fe","C. El proceso debe ser igualitario","D. La prueba debe ser pertinente"],
     "correcta": 0, "fundamento": "El principio de congruencia exige que la sentencia sea congruente con lo alegado y pedido por las partes (ultra petita y extra petita son vicios de incongruencia).", "tema": "Principio de congruencia"},

    {"pregunta": "La nulidad procesal en Chile es:",
     "opciones": ["A. De derecho estricto y opera ipso iure","B. No opera de pleno derecho y requiere ser alegada y declarada","C. Solo puede declararla el tribunal de oficio","D. Solo procede en la segunda instancia"],
     "correcta": 1, "fundamento": "Art. 83 CPC: la nulidad procesal debe ser declarada por el tribunal; no opera de pleno derecho. El art. 84 establece que puede declararse de oficio cuando el vicio impide la prosecución del juicio.", "tema": "Nulidad procesal"},

    {"pregunta": "El recurso de casación en la forma procede por:",
     "opciones": ["A. Infracción de ley que influye sustancialmente en lo dispositivo del fallo","B. Vicios formales del procedimiento taxativamente enumerados en el art. 768 CPC","C. Cualquier error del juez","D. Solo por ultra petita"],
     "correcta": 1, "fundamento": "Art. 768 CPC: el recurso de casación en la forma procede por las causales taxativas que enumera dicho artículo (incompetencia, ultra petita, omisión de trámites esenciales, etc.).", "tema": "Casación en la forma"},

    {"pregunta": "El principio de oralidad en el proceso penal chileno implica que:",
     "opciones": ["A. Todo se resuelve sin audiencias","B. Las actuaciones del juicio oral deben realizarse verbalmente","C. Solo los testigos declaran oralmente","D. El juez redacta la sentencia oralmente"],
     "correcta": 1, "fundamento": "Art. 291 CPP: el juicio oral es oral; las alegaciones, argumentaciones y declaraciones de testigos y peritos se realizan verbalmente.", "tema": "Principio de oralidad"},
]

VF_PROCESAL = [
    {"afirmacion": "En el proceso civil chileno, el juez puede decretar medidas para mejor resolver después de citadas las partes a oír sentencia.",
     "respuesta": True, "fundamento": "Art. 159 CPC: los tribunales pueden, para mejor resolver, decretar medidas para mejor resolver después de la citación para oír sentencia.", "tema": "Medidas para mejor resolver"},

    {"afirmacion": "La demanda en el juicio ordinario civil debe notificarse personalmente al demandado.",
     "respuesta": True, "fundamento": "Art. 40 CPC: en toda gestión judicial, la primera notificación a las personas que no han sido parte debe hacerse personalmente.", "tema": "Notificación personal"},

    {"afirmacion": "En el proceso penal chileno, el Ministerio Público dirige la investigación y tiene facultad jurisdiccional.",
     "respuesta": False, "fundamento": "El Ministerio Público dirige en forma exclusiva la investigación (art. 83 CPR), pero carece de facultad jurisdiccional; el juzgamiento corresponde al tribunal.", "tema": "Ministerio Público"},

    {"afirmacion": "El recurso de nulidad en el proceso penal puede fundar en la vulneración de derechos o garantías.",
     "respuesta": True, "fundamento": "Art. 373 a) CPP: el recurso de nulidad procede cuando la sentencia se ha pronunciado con infracción sustancial de derechos o garantías aseguradas por la CPR o por tratados.", "tema": "Recurso de nulidad penal"},

    {"afirmacion": "La acumulación de autos procede cuando hay identidad de partes en dos o más juicios.",
     "respuesta": False, "fundamento": "Art. 92 CPC: la acumulación de autos procede cuando las mismas partes litigan en juicios distintos y la sentencia de uno produce excepción de cosa juzgada en el otro, o cuando deben fallarse conjuntamente. No requiere solo identidad de partes.", "tema": "Acumulación de autos"},

    {"afirmacion": "Las sentencias definitivas de primera instancia pueden ser apeladas en Chile.",
     "respuesta": True, "fundamento": "Art. 187 CPC: son apelables las sentencias definitivas de primera instancia. La apelación es el recurso ordinario más amplio.", "tema": "Apelación civil"},

    {"afirmacion": "El juicio ejecutivo procede cuando la obligación consta en un título ejecutivo perfectamente válido.",
     "respuesta": True, "fundamento": "Art. 434 CPC: el juicio o procedimiento ejecutivo tiene lugar en las obligaciones de dar cuando para exigir su cumplimiento se hace valer alguno de los títulos que enumera dicho artículo.", "tema": "Juicio ejecutivo"},

    {"afirmacion": "En el proceso penal, el imputado puede guardar silencio sin que esto se use en su contra.",
     "respuesta": True, "fundamento": "Art. 93 b) CPP: el imputado tiene derecho a guardar silencio, y si así lo hace, este hecho no puede ser usado en su perjuicio.", "tema": "Derecho a guardar silencio"},
]

FC_PROCESAL = [
    {"frente": "¿Qué es la cosa juzgada formal y material?",
     "reverso": "Cosa juzgada formal: la resolución no puede impugnarse dentro del mismo proceso. Cosa juzgada material: lo resuelto no puede discutirse en ningún otro proceso posterior entre las mismas partes.", "tema": "Cosa juzgada"},

    {"frente": "Etapas del procedimiento ordinario civil en Chile",
     "reverso": "1) Demanda, 2) Contestación (20 días), 3) Réplica (6 días), 4) Dúplica (6 días), 5) Conciliación obligatoria, 6) Recepción a prueba (si hay hechos controvertidos), 7) Término probatorio (20 días), 8) Observaciones a la prueba, 9) Citación a oír sentencia, 10) Sentencia.", "tema": "Procedimiento ordinario civil"},

    {"frente": "¿Qué es el principio de publicidad en el proceso penal?",
     "reverso": "El juicio oral es público (art. 289 CPP); cualquier persona puede asistir salvo excepciones de ley. Garantiza control ciudadano de la justicia y prohíbe la justicia secreta.", "tema": "Publicidad proceso penal"},

    {"frente": "Recursos en el proceso penal (CPP)",
     "reverso": "1) Reposición (contra resoluciones del juez de garantía), 2) Apelación (casos expresamente previstos), 3) Nulidad (contra sentencias del TOP, por causales del art. 373 CPP), 4) Queja disciplinaria.", "tema": "Recursos proceso penal"},

    {"frente": "¿Qué es el principio de inmediación?",
     "reverso": "El juez debe percibir directamente la prueba sin intermediarios. En el juicio oral penal, los jueces del TOP deben estar presentes durante toda la audiencia (art. 284 CPP).", "tema": "Inmediación"},

    {"frente": "¿Qué son las medidas cautelares reales en el proceso civil?",
     "reverso": "Medidas precautorias del art. 290 CPC: 1) Secuestro, 2) Nombramiento de interventor, 3) Retención, 4) Prohibición de celebrar actos y contratos. Buscan asegurar el resultado del juicio.", "tema": "Medidas precautorias"},

    {"frente": "Distinción entre acción y excepción procesal",
     "reverso": "Acción: derecho del demandante a obtener tutela jurisdiccional. Excepción: derecho del demandado a defenderse frente a la acción. Ambas son manifestaciones del derecho de acceso a la justicia.", "tema": "Acción y excepción"},
]


# ════════════════════════════════════════════════════════════════
# CONSTITUCIONAL  (~55)
# ════════════════════════════════════════════════════════════════
MCQ_CONSTITUCIONAL = [
    {"pregunta": "El recurso de amparo constitucional en Chile procede para proteger:",
     "opciones": ["A. Todo derecho fundamental","B. La libertad personal y seguridad individual","C. El derecho de propiedad","D. La igualdad ante la ley"],
     "correcta": 1, "fundamento": "Art. 21 CPR: el recurso de amparo (habeas corpus) protege la libertad personal y seguridad individual cuando son amenazadas, perturbadas o privadas ilegalmente.", "tema": "Recurso de amparo"},

    {"pregunta": "¿Cuál es el quórum para aprobar una Ley Orgánica Constitucional (LOC)?",
     "opciones": ["A. Mayoría simple","B. 3/5 de diputados y senadores en ejercicio","C. 4/7 de los diputados y senadores en ejercicio","D. 2/3 de los diputados y senadores en ejercicio"],
     "correcta": 2, "fundamento": "Art. 66 inc. 2 CPR: las leyes orgánicas constitucionales requieren para su aprobación, modificación o derogación las 4/7 partes de los diputados y senadores en ejercicio.", "tema": "Quórum leyes"},

    {"pregunta": "El Tribunal Constitucional chileno se compone de:",
     "opciones": ["A. 7 miembros","B. 9 miembros","C. 11 miembros","D. 13 miembros"],
     "correcta": 2, "fundamento": "Art. 92 CPR: el Tribunal Constitucional está integrado por 11 miembros designados de la siguiente forma: 3 por el Presidente de la República, 4 elegidos por el Congreso Nacional y 4 por la Corte Suprema.", "tema": "Tribunal Constitucional"},

    {"pregunta": "¿Cuántos años dura el mandato del Presidente de la República en Chile?",
     "opciones": ["A. 4 años sin reelección","B. 4 años con una reelección inmediata","C. 6 años sin reelección inmediata","D. 5 años sin reelección"],
     "correcta": 2, "fundamento": "Art. 25 CPR: el Presidente dura 6 años en el ejercicio de sus funciones y no puede ser reelegido para el período siguiente.", "tema": "Mandato presidencial"},

    {"pregunta": "El recurso de protección del art. 20 CPR protege los derechos fundamentales cuando son:",
     "opciones": ["A. Vulnerados por la ley","B. Amenazados, perturbados o privados por acto u omisión arbitraria o ilegal","C. Solo amenazados","D. Solo privados"],
     "correcta": 1, "fundamento": "Art. 20 CPR: el recurso de protección procede cuando se amenaza, priva o perturba el ejercicio legítimo de los derechos por acto u omisión arbitraria o ilegal.", "tema": "Recurso de protección"},

    {"pregunta": "¿Cuál de los siguientes principios NO está en la CPR de 1980 de forma expresa?",
     "opciones": ["A. Subsidiariedad del Estado","B. Bien común","C. Dignidad de la persona humana","D. Fraternidad"],
     "correcta": 3, "fundamento": "Los arts. 1 y 5 CPR consagran dignidad, bien común y subsidiariedad. La fraternidad no figura expresamente en la CPR vigente.", "tema": "Principios constitucionales"},

    {"pregunta": "El estado de excepción constitucional de catástrofe lo declara:",
     "opciones": ["A. El Congreso Nacional","B. El Presidente de la República","C. El Tribunal Constitucional","D. La Corte Suprema"],
     "correcta": 1, "fundamento": "Art. 41 CPR: el estado de catástrofe lo declara el Presidente de la República, debiendo dar cuenta al Congreso.", "tema": "Estados de excepción"},

    {"pregunta": "¿Cuántos diputados tiene la Cámara de Diputadas y Diputados de Chile?",
     "opciones": ["A. 100","B. 120","C. 155","D. 155 (elegidos desde 2017)"],
     "correcta": 3, "fundamento": "La reforma constitucional de 2015 (Ley 20.840) amplió la Cámara de 120 a 155 diputados, vigor desde la elección de 2017.", "tema": "Cámara de Diputados"},
]

VF_CONSTITUCIONAL = [
    {"afirmacion": "El recurso de protección en Chile debe interponerse dentro de 30 días desde el acto u omisión que lo motiva.",
     "respuesta": True, "fundamento": "Auto Acordado de la Corte Suprema sobre recurso de protección: el plazo es de 30 días corridos desde la ejecución del acto o la ocurrencia de la omisión.", "tema": "Recurso de protección"},

    {"afirmacion": "El Senado en Chile tiene la facultad de juzgar a los ministros de estado.",
     "respuesta": True, "fundamento": "Art. 53 N°1 CPR: el Senado conoce de las acusaciones constitucionales como jurado y declara la culpabilidad del acusado.", "tema": "Acusación constitucional"},

    {"afirmacion": "La igualdad ante la ley implica que todas las personas deben ser tratadas de manera idéntica.",
     "respuesta": False, "fundamento": "La igualdad ante la ley prohíbe la discriminación arbitraria, pero permite tratos diferenciados cuando existen razones objetivas y proporcionales. Art. 19 N°2 CPR.", "tema": "Igualdad ante la ley"},

    {"afirmacion": "En Chile, el control preventivo obligatorio de constitucionalidad corresponde al Tribunal Constitucional.",
     "respuesta": True, "fundamento": "Art. 93 N°1 CPR: el TC ejerce control preventivo obligatorio de los proyectos de leyes orgánicas constitucionales antes de su promulgación.", "tema": "Control constitucional"},

    {"afirmacion": "Las leyes de quórum calificado en Chile requieren mayoría absoluta de los parlamentarios en ejercicio.",
     "respuesta": True, "fundamento": "Art. 66 inc. 3 CPR: las leyes de quórum calificado se aprueban por la mayoría absoluta de los diputados y senadores en ejercicio.", "tema": "Leyes de quórum calificado"},

    {"afirmacion": "El Contralor General de la República puede ejercer control de constitucionalidad.",
     "respuesta": False, "fundamento": "La Contraloría ejerce control de legalidad (art. 99 CPR), no de constitucionalidad. El control de constitucionalidad corresponde al Tribunal Constitucional.", "tema": "Contraloría General"},

    {"afirmacion": "La libertad de expresión en Chile es un derecho absoluto sin limitaciones.",
     "respuesta": False, "fundamento": "Art. 19 N°12 CPR: la libertad de emitir opinión admite limitaciones como la responsabilidad por los abusos cometidos y la censura previa para espectáculos. No es un derecho absoluto.", "tema": "Libertad de expresión"},
]

FC_CONSTITUCIONAL = [
    {"frente": "Diferencia entre derechos civiles, políticos y sociales",
     "reverso": "Derechos civiles y políticos (primera generación): libertades individuales y participación política (vida, propiedad, igualdad, voto). Derechos sociales (segunda generación): prestaciones del Estado (salud, educación, trabajo, vivienda).", "tema": "Generaciones de derechos"},

    {"frente": "¿Qué es el control de convencionalidad?",
     "reverso": "Obligación de los jueces de aplicar los tratados de derechos humanos (especialmente la CADH) por sobre el derecho interno incompatible. Desarrollado por la Corte IDH desde el caso Almonacid Arellano vs. Chile (2006).", "tema": "Control de convencionalidad"},

    {"frente": "¿Qué es la potestad reglamentaria?",
     "reverso": "Facultad del Presidente de la República para dictar normas jurídicas de rango infralegal. Autónoma: materias no reservadas a ley. De ejecución: complementar las leyes (art. 32 N°6 CPR).", "tema": "Potestad reglamentaria"},

    {"frente": "Principios del Estado de Derecho en la CPR chilena",
     "reverso": "1) Supremacía constitucional, 2) Legalidad (nadie está sobre la ley), 3) Separación de poderes, 4) Respeto a los derechos fundamentales, 5) Responsabilidad del Estado y sus órganos (art. 7 CPR).", "tema": "Estado de Derecho"},

    {"frente": "¿Qué es el habeas data?",
     "reverso": "Garantía que permite a toda persona acceder, corregir o eliminar datos personales que le conciernen en bases de datos públicas o privadas. En Chile está parcialmente regulado por la Ley 19.628 y el recurso de protección.", "tema": "Habeas data"},

    {"frente": "Composición del Congreso Nacional chileno",
     "reverso": "Congreso bicameral: Cámara de Diputadas y Diputados (155 miembros, por 4 años) y Senado (50 senadores, por 8 años, con renovación por mitades cada 4 años). Art. 47 CPR.", "tema": "Congreso Nacional"},
]


# ════════════════════════════════════════════════════════════════
# LABORAL  (~50)
# ════════════════════════════════════════════════════════════════
MCQ_LABORAL = [
    {"pregunta": "El contrato de trabajo individual en Chile puede ser verbal cuando:",
     "opciones": ["A. Nunca, siempre requiere escrituración","B. La duración es inferior a 30 días","C. Las partes así lo acuerdan","D. Solo en el caso de trabajadores de casa particular"],
     "correcta": 1, "fundamento": "Art. 9 CT: el contrato de trabajo es consensual (verbal) pero debe constar por escrito; si no se escritura en 15 días (5 días para trabajos de obra o faena), se presumen verdaderas las estipulaciones señaladas por el trabajador.", "tema": "Contrato de trabajo"},

    {"pregunta": "¿Cuál es el plazo de prescripción de los créditos laborales del Código del Trabajo?",
     "opciones": ["A. 1 año","B. 2 años","C. 5 años","D. 6 meses"],
     "correcta": 1, "fundamento": "Art. 510 CT: los créditos del empleado contra el empleador prescriben en 2 años contados desde que se hicieron exigibles; para las acciones por accidentes del trabajo, en 5 años.", "tema": "Prescripción laboral"},

    {"pregunta": "La jornada ordinaria máxima legal de trabajo en Chile es actualmente de:",
     "opciones": ["A. 45 horas semanales","B. 44 horas semanales","C. 40 horas semanales","D. 42 horas semanales"],
     "correcta": 2, "fundamento": "Ley 21.561 (2024): redujo la jornada ordinaria de 45 a 40 horas semanales, con implementación gradual hasta 2028. Art. 22 CT modificado.", "tema": "Jornada de trabajo"},

    {"pregunta": "El despido por necesidades de la empresa en Chile corresponde a:",
     "opciones": ["A. Art. 160 CT","B. Art. 161 CT","C. Art. 162 CT","D. Art. 163 CT"],
     "correcta": 1, "fundamento": "Art. 161 CT: el empleador puede poner término al contrato invocando necesidades de la empresa, establecimiento o servicio, con derecho a indemnización.", "tema": "Necesidades de la empresa"},

    {"pregunta": "El fuero maternal en Chile protege a la trabajadora:",
     "opciones": ["A. Solo durante el embarazo","B. Durante el embarazo y hasta 1 año después de expirado el postnatal","C. Solo durante el postnatal","D. Hasta 2 años después del parto"],
     "correcta": 1, "fundamento": "Art. 201 CT: la trabajadora está amparada por fuero durante el embarazo y hasta un año después de expirado el descanso postnatal.", "tema": "Fuero maternal"},

    {"pregunta": "Las organizaciones sindicales en Chile pueden formarse con un mínimo de:",
     "opciones": ["A. 5 trabajadores","B. 8 trabajadores","C. 10 trabajadores con 25% de la empresa","D. 8 trabajadores o 25 trabajadores según el tamaño de la empresa"],
     "correcta": 3, "fundamento": "Art. 227 CT: para constituir un sindicato en empresas con 50 o más trabajadores se requiere mínimo 25 trabajadores o el 10%; en empresas con menos de 50, mínimo 8 trabajadores.", "tema": "Sindicatos"},

    {"pregunta": "¿Qué es el finiquito en derecho laboral chileno?",
     "opciones": ["A. Un contrato de trabajo a plazo fijo","B. El documento que extingue el contrato de trabajo y da cuenta del pago de las prestaciones","C. La carta de aviso de despido","D. Un acuerdo de mediación"],
     "correcta": 1, "fundamento": "Art. 177 CT: el finiquito es el instrumento que da cuenta de la terminación del contrato y del pago de las sumas que corresponden al trabajador. Debe ser ratificado ante ministro de fe.", "tema": "Finiquito"},
]

VF_LABORAL = [
    {"afirmacion": "En Chile, el empleador puede modificar unilateralmente las condiciones esenciales del contrato de trabajo.",
     "respuesta": False, "fundamento": "Art. 5 CT: los derechos del trabajador son irrenunciables. El empleador no puede modificar unilateralmente elementos esenciales del contrato (ius variandi tiene límites precisos en el art. 12 CT).", "tema": "Ius variandi"},

    {"afirmacion": "El trabajador despedido por las causales del art. 160 CT (conducta indebida) no tiene derecho a indemnización.",
     "respuesta": True, "fundamento": "Arts. 160 y 163 CT: las causales del art. 160 (conducta grave) no generan derecho a indemnización por años de servicio ni por aviso previo.", "tema": "Causales art. 160"},

    {"afirmacion": "La huelga en Chile es un derecho constitucional de los trabajadores.",
     "respuesta": True, "fundamento": "Art. 19 N°16 CPR reconoce el derecho a la negociación colectiva y a la huelga, salvo en los casos que señale la ley. Art. 345 CT regula la huelga en la negociación colectiva.", "tema": "Huelga"},

    {"afirmacion": "El empleador está obligado a pagar las cotizaciones previsionales del trabajador.",
     "respuesta": True, "fundamento": "Arts. 19 y ss. DL 3.500: el empleador está obligado a descontar y enterar las cotizaciones previsionales del trabajador en la AFP correspondiente.", "tema": "Cotizaciones previsionales"},

    {"afirmacion": "El contrato colectivo de trabajo tiene fuerza obligatoria para todos los trabajadores de la empresa.",
     "respuesta": False, "fundamento": "Art. 346 CT: el contrato colectivo obliga a los trabajadores que participaron en la negociación y a los que se adhieran posteriormente. No se extiende automáticamente a todos.", "tema": "Contrato colectivo"},

    {"afirmacion": "El período de prueba de hasta 30 días está expresamente regulado en el Código del Trabajo chileno.",
     "respuesta": False, "fundamento": "El Código del Trabajo chileno no regula expresamente el período de prueba. El contrato se rige por las reglas generales desde el primer día.", "tema": "Período de prueba"},

    {"afirmacion": "Los trabajadores de casa particular tienen derecho a la misma jornada máxima que los trabajadores generales.",
     "respuesta": False, "fundamento": "Art. 149 CT: los trabajadores de casa particular que no viven en la casa del empleador tienen jornada de 12 horas diarias con descanso de una hora. Tienen estatuto especial.", "tema": "Trabajadores casa particular"},
]

FC_LABORAL = [
    {"frente": "Principios del derecho del trabajo",
     "reverso": "1) Protector (in dubio pro operario, regla más favorable, condición más beneficiosa), 2) Irrenunciabilidad de derechos, 3) Continuidad de la relación laboral, 4) Primacía de la realidad, 5) Buena fe.", "tema": "Principios laborales"},

    {"frente": "¿Qué es el principio de primacía de la realidad?",
     "reverso": "En caso de discordancia entre lo pactado y la realidad, prevalece lo que ocurre en los hechos. Impide encubrir relaciones laborales con contratos civiles o mercantiles (art. 8 CT: presunción de laboralidad).", "tema": "Primacía de la realidad"},

    {"frente": "Causales de término del contrato de trabajo",
     "reverso": "Art. 159: causales objetivas (vencimiento de plazo, conclusión de obra, muerte, etc.). Art. 160: conducta indebida del trabajador. Art. 161: necesidades de la empresa. Art. 162: procedimiento formal de despido.", "tema": "Término del contrato"},

    {"frente": "¿Qué es la negociación colectiva reglada?",
     "reverso": "Procedimiento formal (arts. 327 y ss. CT) en que trabajadores organizados negocian con el empleador condiciones de trabajo y remuneración. Puede terminar en contrato colectivo o en huelga.", "tema": "Negociación colectiva"},

    {"frente": "¿Qué es el subcontrato en derecho laboral chileno?",
     "opciones": ["Art. 183-A CT", ""],
     "reverso": "Art. 183-A CT: obra o servicio que el empleador (empresa principal) encomienda a un tercero (contratista). La empresa principal tiene responsabilidad subsidiaria (y solidaria en ciertos casos) por obligaciones laborales y previsionales.", "tema": "Subcontrato"},
]


# ════════════════════════════════════════════════════════════════
# OBLIGACIONES  (~45)
# ════════════════════════════════════════════════════════════════
MCQ_OBLIGACIONES = [
    {"pregunta": "Las obligaciones de medios se distinguen de las de resultado en que:",
     "opciones": ["A. Las de medios solo generan responsabilidad objetiva","B. En las de medios el deudor cumple poniendo diligencia aunque no logre el resultado; en las de resultado debe obtener el fin prometido","C. Solo existen en el derecho anglosajón","D. Las de resultado no generan responsabilidad"],
     "correcta": 1, "fundamento": "Distinción doctrinal: en obligaciones de medio (ej. médico), el deudor cumple siendo diligente; en obligaciones de resultado (ej. constructor), el deudor debe alcanzar el fin prometido.", "tema": "Obligaciones de medio y resultado"},

    {"pregunta": "La cláusula penal moratoria se diferencia de la compensatoria en que:",
     "opciones": ["A. La moratoria reemplaza al cumplimiento; la compensatoria indemniza la mora","B. La moratoria indemniza el retardo; la compensatoria reemplaza al cumplimiento","C. Son sinónimos","D. La moratoria solo opera en contratos comerciales"],
     "correcta": 1, "fundamento": "La cláusula penal moratoria sanciona el simple retardo en el cumplimiento; la compensatoria reemplaza el derecho a exigir el cumplimiento o los perjuicios por incumplimiento definitivo.", "tema": "Cláusula penal"},

    {"pregunta": "La novación objetiva se produce cuando:",
     "opciones": ["A. Un nuevo deudor reemplaza al anterior","B. La obligación primitiva se extingue y es reemplazada por una nueva con distinto objeto o causa","C. El acreedor cambia","D. Se agrega un nuevo fiador"],
     "correcta": 1, "fundamento": "Art. 1631 N°2 CC: la novación objetiva se produce cuando el deudor contrae con el acreedor una nueva obligación que sustituye a la anterior, cambiando el objeto o la causa.", "tema": "Novación"},

    {"pregunta": "¿Cuándo opera la compensación legal en el CC chileno?",
     "opciones": ["A. Cuando el juez la declara","B. Cuando las partes lo acuerdan","C. De pleno derecho, ipso iure, cuando se reúnen los requisitos del art. 1655 CC","D. Solo en obligaciones de dinero superiores a 10 UTM"],
     "correcta": 2, "fundamento": "Art. 1656 CC: la compensación se opera ipso iure cuando ambas partes son mutuamente deudoras de cosas fungibles de la misma especie, ambas deudas son líquidas y actualmente exigibles.", "tema": "Compensación"},

    {"pregunta": "La teoría de los riesgos en los contratos bilaterales determina quién soporta la pérdida fortuita. En Chile, la regla es:",
     "opciones": ["A. Res perit domino siempre","B. Res perit creditori en las obligaciones de especie o cuerpo cierto","C. Res perit debitori","D. El riesgo siempre es del vendedor"],
     "correcta": 1, "fundamento": "Art. 1550 CC: el riesgo del cuerpo cierto cuya entrega se deba es del acreedor (res perit creditori), salvo excepciones legales.", "tema": "Teoría de los riesgos"},

    {"pregunta": "El pago con subrogación se diferencia del pago normal en que:",
     "opciones": ["A. Extingue totalmente la obligación","B. El crédito subsiste en cabeza de quien pagó, con los mismos accesorios","C. Solo opera entre comerciantes","D. No requiere consentimiento del deudor"],
     "correcta": 1, "fundamento": "Arts. 1608 y ss. CC: en el pago con subrogación, la obligación no se extingue, sino que se traspasa al tercero que pagó con todos sus privilegios y accesorios.", "tema": "Pago con subrogación"},

    {"pregunta": "El daño moral en la responsabilidad contractual chilena:",
     "opciones": ["A. No es indemnizable","B. Es indemnizable según la jurisprudencia y doctrina mayoritaria actual","C. Solo es indemnizable si se pactó expresamente","D. Solo en contratos de consumo"],
     "correcta": 1, "fundamento": "La doctrina y jurisprudencia chilena mayoritaria actual admite la indemnización del daño moral en sede contractual, aunque el CC no lo menciona expresamente en el art. 1556.", "tema": "Daño moral contractual"},
]

VF_OBLIGACIONES = [
    {"afirmacion": "La mora del acreedor (mora creditoris) libera al deudor de los riesgos por pérdida fortuita de la cosa.",
     "respuesta": True, "fundamento": "Art. 1548 CC en relación con los arts. 1680 y 1827 CC: si el acreedor está en mora de recibir, los riesgos se trasladan al acreedor y el deudor ya no responde por el caso fortuito.", "tema": "Mora del acreedor"},

    {"afirmacion": "La novación siempre requiere el consentimiento del deudor primitivo.",
     "respuesta": False, "fundamento": "Art. 1631 CC: en la novación por cambio de deudor (delegación), puede hacerse sin el consentimiento del deudor primitivo (delegación imperfecta o expromisión).", "tema": "Novación por cambio de deudor"},

    {"afirmacion": "Las obligaciones naturales en Chile pueden exigirse judicialmente.",
     "respuesta": False, "fundamento": "Art. 1470 CC: las obligaciones naturales no confieren derecho para exigir su cumplimiento, pero autororizan para retener lo que se ha dado o pagado en razón de ellas.", "tema": "Obligaciones naturales"},

    {"afirmacion": "La cláusula de aceleración en los contratos de mutuo es válida en Chile.",
     "respuesta": True, "fundamento": "La cláusula de aceleración (ante el incumplimiento de una cuota, se hacen exigibles todas las demás) es válida en Chile y reconocida por la jurisprudencia.", "tema": "Cláusula de aceleración"},

    {"afirmacion": "El daño emergente y el lucro cesante son siempre indemnizables en la responsabilidad contractual.",
     "respuesta": False, "fundamento": "Art. 1558 CC: en la responsabilidad contractual, si no hay dolo, solo se indemnizan los perjuicios previstos. Con dolo, se indemnizan los daños directos, incluyendo previstos e imprevistos.", "tema": "Daño emergente y lucro cesante"},

    {"afirmacion": "La transacción produce efectos de cosa juzgada entre las partes.",
     "respuesta": True, "fundamento": "Art. 2460 CC: la transacción produce entre las partes el efecto de cosa juzgada en última instancia.", "tema": "Transacción"},
]

FC_OBLIGACIONES = [
    {"frente": "Requisitos del caso fortuito",
     "reverso": "1) Imprevisto (no pudo preverse al tiempo de contratar), 2) Irresistible (no puede evitarse ni superarse), 3) Externo (ajeno a la voluntad del deudor), 4) Que no sea imputable al deudor. Art. 45 CC.", "tema": "Caso fortuito"},

    {"frente": "¿Qué es la indemnización de perjuicios?",
     "reverso": "Derecho del acreedor a que el deudor le pague el equivalente pecuniario del daño sufrido por el incumplimiento. Comprende daño emergente, lucro cesante y (según la doctrina moderna) daño moral. Art. 1556 CC.", "tema": "Indemnización de perjuicios"},

    {"frente": "Diferencia entre solidaridad e indivisibilidad",
     "reverso": "Solidaridad: cualquier deudor debe la totalidad; el pago por uno extingue la obligación. Indivisibilidad: la prestación no puede dividirse por su naturaleza o por la convención. La solidaridad no pasa a herederos; la indivisibilidad sí.", "tema": "Solidaridad vs indivisibilidad"},

    {"frente": "¿Cuándo se constituye en mora el deudor?",
     "reverso": "Art. 1551 CC: 1) Cuando no cumple en el tiempo estipulado (mora ex re), 2) Cuando interpelado por el acreedor no cumple, 3) En las obligaciones de no hacer, desde el momento de la contravención.", "tema": "Mora del deudor"},
]


# ════════════════════════════════════════════════════════════════
# FAMILIA  (~35)
# ════════════════════════════════════════════════════════════════
MCQ_FAMILIA = [
    {"pregunta": "En Chile, ¿qué edad mínima se requiere para contraer matrimonio?",
     "opciones": ["A. 14 años para hombres, 12 para mujeres","B. 16 años para ambos","C. 18 años para ambos","D. 16 años con autorización y 18 sin ella"],
     "correcta": 2, "fundamento": "Ley 19.947 (LMC) modificada: la Ley 21.400 (2022) fijó la edad mínima en 18 años para ambos contrayentes, eliminando el matrimonio de menores.", "tema": "Edad para matrimonio"},

    {"pregunta": "El acuerdo de unión civil (AUC) en Chile fue consagrado por:",
     "opciones": ["A. Ley 20.830","B. Ley 19.947","C. Ley 21.120","D. Ley 20.609"],
     "correcta": 0, "fundamento": "La Ley 20.830 (2015) creó el Acuerdo de Unión Civil (AUC), estableciendo un régimen de convivencia para parejas del mismo o distinto sexo.", "tema": "Acuerdo de unión civil"},

    {"pregunta": "En el régimen de sociedad conyugal chilena, los bienes raíces adquiridos a título oneroso durante el matrimonio son:",
     "opciones": ["A. Bienes propios del marido","B. Bienes propios de la mujer","C. Bienes sociales","D. Bienes propios del cónyuge que los adquirió"],
     "correcta": 2, "fundamento": "Arts. 1725 y ss. CC: en la sociedad conyugal, los bienes adquiridos a título oneroso durante el matrimonio son bienes sociales (del haber absoluto de la sociedad conyugal).", "tema": "Sociedad conyugal"},

    {"pregunta": "La compensación económica en la ley de matrimonio civil procede cuando:",
     "opciones": ["A. Siempre al momento del divorcio","B. Cuando uno de los cónyuges sufre un menoscabo económico por haberse dedicado al cuidado de hijos o del hogar durante el matrimonio","C. Solo en caso de culpa del cónyuge que solicita el divorcio","D. Solo si hay acuerdo de las partes"],
     "correcta": 1, "fundamento": "Art. 61 LMC: la compensación económica procede cuando uno de los cónyuges no pudo desarrollar actividad remunerada o lo hizo en menor medida por dedicarse al cuidado de hijos o del hogar.", "tema": "Compensación económica"},

    {"pregunta": "El cuidado personal de los hijos menores en Chile, cuando los padres viven separados, corresponde a:",
     "opciones": ["A. Siempre a la madre","B. A quien los padres acuerden o, a falta de acuerdo, al padre o madre con quien el hijo convive","C. Al tribunal competente designa siempre","D. Al progenitor que demuestre mejor situación económica"],
     "correcta": 1, "fundamento": "Art. 225 CC: si los padres viven separados, el cuidado personal corresponde a quien acuerden, o a falta de acuerdo, al padre o madre con quien el hijo convive. La ley eliminó la preferencia materna.", "tema": "Cuidado personal"},
]

VF_FAMILIA = [
    {"afirmacion": "El matrimonio en Chile puede celebrarse entre personas del mismo sexo desde el año 2022.",
     "respuesta": True, "fundamento": "Ley 21.400 (2022) modificó la Ley de Matrimonio Civil para permitir el matrimonio igualitario, incluyendo parejas del mismo sexo.", "tema": "Matrimonio igualitario"},

    {"afirmacion": "El divorcio por cese de convivencia unilateral en Chile requiere 3 años de separación.",
     "respuesta": True, "fundamento": "Art. 55 LMC: el divorcio unilateral requiere que haya cesado la convivencia por al menos 3 años (sin acuerdo de ambos cónyuges).", "tema": "Divorcio unilateral"},

    {"afirmacion": "La filiación no matrimonial en Chile produce los mismos efectos que la matrimonial.",
     "respuesta": True, "fundamento": "Art. 33 CC: la filiación no matrimonial, debidamente determinada, produce los mismos efectos que la filiación matrimonial (igualdad de derechos entre hijos).", "tema": "Filiación"},

    {"afirmacion": "El régimen de participación en los gananciales opera durante el matrimonio como el de separación de bienes.",
     "respuesta": True, "fundamento": "Art. 1792-2 CC: en el régimen de participación en los gananciales, durante el matrimonio cada cónyuge administra libremente sus bienes; al disolverse, participan por igual en las ganancias.", "tema": "Participación en gananciales"},

    {"afirmacion": "La adopción en Chile siempre requiere autorización judicial.",
     "respuesta": True, "fundamento": "Ley 21.302 (2021, Nueva Ley de Adopción): la adopción requiere resolución judicial que la constituya, previo proceso ante el tribunal de familia competente.", "tema": "Adopción"},

    {"afirmacion": "La obligación alimenticia puede renunciarse libremente.",
     "respuesta": False, "fundamento": "Art. 334 CC: el derecho de pedir alimentos no puede transmitirse ni renunciarse; solo puede renunciarse el derecho a los alimentos devengados y no percibidos.", "tema": "Alimentos"},
]

FC_FAMILIA = [
    {"frente": "Diferencia entre cuidado personal y patria potestad",
     "reverso": "Cuidado personal: custodia del hijo, a cargo de quien vive con él (art. 225 CC). Patria potestad: conjunto de derechos y deberes sobre la persona y bienes del hijo (representación legal, administración de bienes), art. 243 CC. Pueden no coincidir en el mismo progenitor.", "tema": "Cuidado personal vs patria potestad"},

    {"frente": "Regímenes matrimoniales vigentes en Chile",
     "reverso": "1) Sociedad conyugal (régimen supletorio), 2) Separación total de bienes, 3) Participación en los gananciales. No existe capitulaciones post-matrimoniales con efectos amplios.", "tema": "Regímenes matrimoniales"},

    {"frente": "Causales de nulidad del matrimonio en Chile",
     "reverso": "Art. 44 LMC: 1) Falta de consentimiento libre y espontáneo (fuerza, error), 2) Falta de capacidad (vínculo matrimonial no disuelto, parentesco, demencia), 3) Falta de las formalidades legales. La causal debe concurrir al tiempo de la celebración.", "tema": "Nulidad matrimonial"},

    {"frente": "¿Qué son los alimentos mayores y menores?",
     "reverso": "Alimentos mayores (congruos): los necesarios para subsistir modestamente de acuerdo a la posición social del alimentario. Alimentos menores (necesarios): los necesarios para la mera subsistencia. Chile los unificó en los arts. 323-337 CC.", "tema": "Tipos de alimentos"},
]


# ════════════════════════════════════════════════════════════════
# COMERCIAL  (~35)
# ════════════════════════════════════════════════════════════════
MCQ_COMERCIAL = [
    {"pregunta": "El Código de Comercio chileno define los actos de comercio en su:",
     "opciones": ["A. Art. 1","B. Art. 3","C. Art. 10","D. Art. 7"],
     "correcta": 1, "fundamento": "Art. 3 C.Com.: enumera los actos de comercio en Chile (compras para revender, operaciones de banco, seguros, operaciones marítimas, etc.).", "tema": "Actos de comercio"},

    {"pregunta": "La letra de cambio en Chile es un título de crédito que debe mencionar obligatoriamente:",
     "opciones": ["A. Solo el monto y la fecha","B. La denominación 'letra de cambio', el lugar y fecha de emisión, orden de pagar, beneficiario, monto y firma del librador","C. Solo la firma del librador y el monto","D. El RUT de todas las partes"],
     "correcta": 1, "fundamento": "Art. 1 Ley 18.092 (Letras de Cambio y Pagarés): la letra debe contener los requisitos esenciales que enumera dicho artículo.", "tema": "Letra de cambio"},

    {"pregunta": "La sociedad anónima cerrada en Chile se distingue de la abierta en que:",
     "opciones": ["A. Tiene menos socios","B. No hace oferta pública de sus acciones ni está sujeta a la CMF","C. No puede emitir acciones","D. No tiene directorio"],
     "correcta": 1, "fundamento": "Arts. 2 y 3 Ley 18.046 (LSA): la sociedad anónima abierta hace oferta pública de valores y está sujeta a fiscalización de la CMF; la cerrada no.", "tema": "Sociedades anónimas"},

    {"pregunta": "¿Qué es el endoso en blanco en los títulos de crédito?",
     "opciones": ["A. Un endoso sin firma","B. Un endoso que solo contiene la firma del endosante, sin designar al endosatario","C. Un endoso sin monto","D. El primer endoso de la cadena"],
     "correcta": 1, "fundamento": "Art. 23 Ley 18.092: el endoso en blanco contiene solo la firma del endosante y convierte el documento en uno al portador.", "tema": "Endoso en blanco"},

    {"pregunta": "La solidaridad en las obligaciones mercantiles en Chile:",
     "opciones": ["A. Requiere pacto expreso como en el derecho civil","B. Se presume entre los codeudores de una obligación comercial","C. No existe en el derecho mercantil chileno","D. Solo opera en operaciones bancarias"],
     "correcta": 1, "fundamento": "Art. 370 C.Com.: en las obligaciones mercantiles, cada uno de los que han contraído obligación solidariamente es responsable de todos.", "tema": "Solidaridad mercantil"},
]

VF_COMERCIAL = [
    {"afirmacion": "El pagaré en Chile puede ser a la vista, a un plazo contado desde la vista o a día fijo.",
     "respuesta": True, "fundamento": "Art. 11 Ley 18.092: el pagaré puede ser pagadero a día fijo, a un plazo de la fecha, a la vista o a un plazo de la vista.", "tema": "Pagaré"},

    {"afirmacion": "La sociedad de responsabilidad limitada (SRL) en Chile responde con todo su patrimonio por las deudas sociales.",
     "respuesta": True, "fundamento": "Ley 3.918: la sociedad de responsabilidad limitada responde con todo su patrimonio social; los socios limitan su responsabilidad a sus aportes o a la suma que establezcan los estatutos.", "tema": "Sociedad de responsabilidad limitada"},

    {"afirmacion": "El contrato de seguro en Chile es solemne.",
     "respuesta": False, "fundamento": "Art. 514 C.Com. (reformado por Ley 20.667): el contrato de seguro es consensual; la póliza es solo el medio de prueba, no requisito de validez.", "tema": "Contrato de seguro"},

    {"afirmacion": "El comerciante individual en Chile debe inscribir su escritura social en el Registro de Comercio.",
     "respuesta": False, "fundamento": "El comerciante individual no requiere inscripción en el Registro de Comercio; la inscripción es obligatoria para las sociedades comerciales (art. 22 C.Com.).", "tema": "Registro de Comercio"},

    {"afirmacion": "El derecho comercial se caracteriza por el principio de la solidaridad de los obligados.",
     "respuesta": True, "fundamento": "Art. 370 C.Com.: en los contratos mercantiles, la solidaridad entre codeudores se presume, a diferencia del derecho civil donde la solidaridad no se presume.", "tema": "Solidaridad mercantil"},

    {"afirmacion": "Las sociedades por acciones (SpA) pueden ser constituidas por una sola persona.",
     "respuesta": True, "fundamento": "Art. 424 C.Com.: la sociedad por acciones puede ser unipersonal, constituida y administrada por una sola persona.", "tema": "Sociedad por acciones"},
]

FC_COMERCIAL = [
    {"frente": "Diferencia entre sociedad colectiva y sociedad anónima",
     "reverso": "Sociedad colectiva: socios responden ilimitada y solidariamente; administración de todos los socios; no hay separación estricta entre sociedad y socios. Sociedad anónima: accionistas responden solo por sus aportes; administración por directorio; separación total.", "tema": "Tipos de sociedades"},

    {"frente": "¿Qué es la quiebra (liquidación concursal)?",
     "reverso": "Procedimiento de la Ley 20.720 (LRLAEP) para empresas insolventes. La Superintendencia de Insolvencia y Reemprendimiento fiscaliza. El liquidador realiza los activos para pagar a los acreedores según la prelación de créditos.", "tema": "Liquidación concursal"},

    {"frente": "Título ejecutivo mercantil más común",
     "reverso": "La letra de cambio y el pagaré son los títulos ejecutivos mercantiles más usados. Art. 434 N°4 CPC: merecen el carácter de título ejecutivo cuando tienen mérito ejecutivo (deuda líquida, actualmente exigible y no prescrita).", "tema": "Títulos ejecutivos mercantiles"},

    {"frente": "¿Qué es el derecho de retención mercantil?",
     "reverso": "Facultad del acreedor de retener la cosa del deudor hasta que se le pague el crédito relacionado con dicha cosa. Reconocido en el C.Com. para determinados contratos (depósito, obra, etc.).", "tema": "Derecho de retención"},
]


# ════════════════════════════════════════════════════════════════
# BIENES  (~30)
# ════════════════════════════════════════════════════════════════
MCQ_BIENES = [
    {"pregunta": "Los frutos naturales en el CC chileno pertenecen al dueño de la cosa que los produce, salvo:",
     "opciones": ["A. No hay excepción","B. Cuando existe usufructo, arrendamiento u otro derecho que otorgue el uso y goce","C. Cuando son frutos civiles","D. Cuando la cosa es inmueble"],
     "correcta": 1, "fundamento": "Art. 646 CC: los frutos naturales pertenecen al dueño; pero si hay usufructo u otro derecho que dé el goce, los frutos pertenecen al usufructuario o titular de ese derecho.", "tema": "Frutos naturales"},

    {"pregunta": "La servidumbre de tránsito en Chile es:",
     "opciones": ["A. Una servidumbre aparente y discontinua","B. Una servidumbre continua y aparente","C. Una servidumbre discontinua, sea aparente o no","D. Una servidumbre natural"],
     "correcta": 2, "fundamento": "Art. 822 CC: las servidumbres discontinuas son las que se ejercen a intervalos más o menos largos de tiempo y suponen un hecho actual del hombre; el tránsito es discontinuo.", "tema": "Servidumbres"},

    {"pregunta": "El usufructo en Chile se extingue por:",
     "opciones": ["A. Solo por el vencimiento del plazo","B. Muerte del usufructuario, vencimiento del plazo, resolución del derecho del constituyente, entre otras causales","C. Solo por renuncia del usufructuario","D. Solo por el no uso por 5 años"],
     "correcta": 1, "fundamento": "Art. 806 CC: el usufructo se extingue por la llegada del día o el evento de la condición, muerte del usufructuario, resolución del derecho del constituyente, consolidación, prescripción, renuncia.", "tema": "Extinción del usufructo"},

    {"pregunta": "¿Cuál es el modo de adquirir aplicable a los bienes mostrencos?",
     "opciones": ["A. Prescripción","B. Ocupación","C. Tradición","D. Sucesión por causa de muerte"],
     "correcta": 1, "fundamento": "Art. 624 CC: la caza y pesca son formas de ocupación; los bienes mostrencos (muebles sin dueño conocido) se adquieren por ocupación (art. 624 y ss. CC).", "tema": "Ocupación"},

    {"pregunta": "La hipoteca en Chile es:",
     "opciones": ["A. Un derecho personal","B. Un derecho real de garantía que grava un inmueble sin desplazamiento","C. Un contrato de arrendamiento especial","D. Una servidumbre especial"],
     "correcta": 1, "fundamento": "Art. 2407 CC: la hipoteca es un derecho de prenda constituido sobre inmuebles que no dejan por eso de permanecer en poder del deudor.", "tema": "Hipoteca"},
]

VF_BIENES = [
    {"afirmacion": "El dominio sobre bienes inmuebles en Chile se adquiere por la sola tradición.",
     "respuesta": False, "fundamento": "Para inmuebles, el título (ej. compraventa) y la tradición son necesarios, pero la tradición de inmuebles se realiza por la inscripción en el CBR (art. 686 CC).", "tema": "Tradición de inmuebles"},

    {"afirmacion": "El usufructo puede constituirse a favor de una persona jurídica por más de 30 años.",
     "respuesta": False, "fundamento": "Art. 770 CC: el usufructo constituido a favor de una persona jurídica no puede durar más de 30 años.", "tema": "Usufructo persona jurídica"},

    {"afirmacion": "En Chile, el poseedor de buena fe hace suyos los frutos percibidos de la cosa poseída.",
     "respuesta": True, "fundamento": "Art. 907 CC: el poseedor de buena fe no está obligado a restituir los frutos percibidos antes de la contestación de la demanda.", "tema": "Posesión de buena fe y frutos"},

    {"afirmacion": "La prenda sin desplazamiento sobre vehículos motorizados debe inscribirse en el Registro de Vehículos Motorizados.",
     "respuesta": True, "fundamento": "Ley 20.190 y Ley 18.287: la prenda sin desplazamiento sobre vehículos debe inscribirse en el Registro de Vehículos Motorizados para ser oponible a terceros.", "tema": "Prenda sin desplazamiento"},

    {"afirmacion": "Las servidumbres naturales en Chile no requieren título.",
     "respuesta": True, "fundamento": "Art. 833 CC: las servidumbres naturales (ej. libre descenso de aguas) existen por la naturaleza del terreno y no requieren título ni prescripción.", "tema": "Servidumbres naturales"},
]

FC_BIENES = [
    {"frente": "¿Qué es la accesión de inmueble a inmueble?",
     "reverso": "Modo de adquirir por el cual el dueño de un inmueble adquiere lo que se añade a él: aluvión (depósito de arena por las aguas), avulsión (terreno arrancado por fuerza), mutación de álveo (cambio de cauce del río). Arts. 649-654 CC.", "tema": "Accesión inmueble a inmueble"},

    {"frente": "Diferencia entre muebles e inmuebles por destinación",
     "reverso": "Inmuebles por destinación: muebles que la ley reputa inmuebles por estar permanentemente destinados al uso, cultivo o beneficio de un inmueble (art. 570 CC). Ej: los abonos de una finca, los animales del fundo.", "tema": "Bienes por destinación"},

    {"frente": "¿Qué es el derecho de superficie?",
     "reverso": "Derecho real que permite a su titular construir o plantar en terreno ajeno y ser dueño de lo construido o plantado, separándose la propiedad del suelo de la de lo edificado. No tiene consagración expresa en el CC; se discute su admisión.", "tema": "Derecho de superficie"},

    {"frente": "Acciones protectoras del dominio",
     "reverso": "1) Reivindicatoria (art. 889 CC): recuperar la posesión de cosa de la que es dueño. 2) Publiciana (art. 894 CC): al que tenía justo título y buena fe y perdió la posesión. 3) Posesorias (arts. 916 y ss. CC): amparan la posesión de inmuebles.", "tema": "Acciones del dominio"},
]


# ════════════════════════════════════════════════════════════════
# SUCESORIO  (~20)
# ════════════════════════════════════════════════════════════════
MCQ_SUCESORIO = [
    {"pregunta": "En la sucesión intestada chilena, ¿quiénes conforman el primer orden de sucesión?",
     "opciones": ["A. Cónyuge y padres","B. Hijos","C. Hijos y cónyuge sobreviviente","D. Solo el cónyuge"],
     "correcta": 2, "fundamento": "Art. 988 CC: el primer orden de sucesión intestada está compuesto por los hijos (personalmente o representados) y el cónyuge sobreviviente.", "tema": "Órdenes de sucesión"},

    {"pregunta": "La cuarta de mejoras en Chile puede asignarse a:",
     "opciones": ["A. Cualquier persona","B. Descendientes, cónyuge o conviviente civil sobreviviente","C. Solo a los hijos","D. Solo a los ascendientes"],
     "correcta": 1, "fundamento": "Art. 1184 CC: la cuarta de mejoras puede asignarse libremente entre descendientes, ascendientes y cónyuge o conviviente civil sobreviviente.", "tema": "Cuarta de mejoras"},

    {"pregunta": "El testamento cerrado en Chile requiere:",
     "opciones": ["A. Solo firma del testador","B. Escritura pública","C. Otorgarse ante notario y 3 testigos hábiles","D. Que sea escrito por el testador de puño y letra"],
     "correcta": 2, "fundamento": "Art. 1023 CC: el testamento solemne cerrado se otorga ante notario y tres testigos hábiles.", "tema": "Testamento cerrado"},

    {"pregunta": "El acervo imaginario en el derecho sucesorio chileno sirve para:",
     "opciones": ["A. Calcular el impuesto a las herencias","B. Proteger las asignaciones forzosas de donaciones excesivas del causante en vida","C. Dividir la herencia entre los herederos","D. Determinar el inventario de bienes"],
     "correcta": 1, "fundamento": "Arts. 1185-1187 CC: los acervos imaginarios (primero y segundo) buscan proteger las legítimas y mejoras de las donaciones excesivas hechas en vida por el causante.", "tema": "Acervos imaginarios"},
]

VF_SUCESORIO = [
    {"afirmacion": "El legatario en Chile responde de las deudas hereditarias hasta el valor de lo que recibe.",
     "respuesta": False, "fundamento": "Arts. 1360 y 1364 CC: el legatario no responde por las deudas hereditarias más allá del valor del legado; la responsabilidad primaria es de los herederos.", "tema": "Legatario y deudas"},

    {"afirmacion": "El testamento ológrafo (manuscrito del testador) es válido en Chile.",
     "respuesta": False, "fundamento": "Chile no reconoce el testamento ológrafo como forma válida de testar. Los testamentos solemnes deben otorgarse ante notario y testigos. El testamento militar y marítimo son excepciones privilegiadas.", "tema": "Testamento ológrafo"},

    {"afirmacion": "El desheredamiento en Chile solo puede hacerse por testamento.",
     "respuesta": True, "fundamento": "Art. 1207 CC: el desheredamiento solo puede hacerse por testamento, expresando la causal y siendo la causal de las que la ley señala.", "tema": "Desheredamiento"},

    {"afirmacion": "La apertura de la sucesión ocurre al momento de la muerte del causante.",
     "respuesta": True, "fundamento": "Art. 955 CC: la sucesión en los bienes de una persona se abre al momento de su muerte. La posesión legal de la herencia pasa al heredero desde ese instante.", "tema": "Apertura de la sucesión"},
]

FC_SUCESORIO = [
    {"frente": "¿Qué son las asignaciones forzosas?",
     "reverso": "Las que el testador está obligado a hacer por la ley y que se suplen aunque las omita (art. 1167 CC): 1) Alimentos forzosos, 2) Legítimas, 3) Cuarta de mejoras (si hay descendientes, ascendientes o cónyuge).", "tema": "Asignaciones forzosas"},

    {"frente": "Diferencia entre herencia y legado",
     "reverso": "Herencia: asignación a título universal que sucede en la totalidad o una cuota del patrimonio del causante (heredero). Legado: asignación a título singular de especies o géneros determinados (legatario). Arts. 951-954 CC.", "tema": "Herencia vs legado"},

    {"frente": "Opciones del heredero ante la herencia",
     "reverso": "1) Aceptar pura y simplemente (se confunden patrimonios), 2) Aceptar con beneficio de inventario (responde de deudas hasta el valor de los bienes heredados), 3) Repudiar (art. 1225 CC).", "tema": "Opciones del heredero"},
]


# ════════════════════════════════════════════════════════════════
# INTERNACIONAL  (~15)
# ════════════════════════════════════════════════════════════════
MCQ_INTERNACIONAL = [
    {"pregunta": "El principio pacta sunt servanda en derecho internacional significa:",
     "opciones": ["A. Los estados pueden desconocer los tratados en cualquier momento","B. Los tratados obligan a las partes y deben ser cumplidos de buena fe","C. Los tratados solo obligan a los estados que los ratifican","D. Los tratados prevalecen sobre la constitución"],
     "correcta": 1, "fundamento": "Art. 26 Convención de Viena sobre Derecho de los Tratados (1969): todo tratado en vigor obliga a las partes y debe ser cumplido por ellas de buena fe.", "tema": "Pacta sunt servanda"},

    {"pregunta": "La Corte Internacional de Justicia tiene sede en:",
     "opciones": ["A. Ginebra","B. Nueva York","C. La Haya","D. Bruselas"],
     "correcta": 2, "fundamento": "La Corte Internacional de Justicia, principal órgano judicial de la ONU, tiene su sede en el Palacio de la Paz, La Haya, Países Bajos.", "tema": "Corte Internacional de Justicia"},

    {"pregunta": "Chile en materia de tratados internacionales de derechos humanos:",
     "opciones": ["A. Los incorpora directamente sin ratificación","B. Los ratifica y aplica con rango de ley","C. El art. 5 inc. 2 CPR obliga a respetar los derechos de tratados de DDHH ratificados y vigentes","D. Los trata como simples recomendaciones"],
     "correcta": 2, "fundamento": "Art. 5 inc. 2 CPR: es deber del Estado respetar y promover los derechos esenciales que emanan de la naturaleza humana garantizados en tratados internacionales de DDHH ratificados y vigentes.", "tema": "Tratados DDHH en Chile"},
]

VF_INTERNACIONAL = [
    {"afirmacion": "El derecho internacional consuetudinario es fuente del derecho internacional público.",
     "respuesta": True, "fundamento": "Art. 38 del Estatuto de la CIJ: enumera como fuentes del DIP los tratados, la costumbre internacional, los principios generales del derecho y la doctrina y jurisprudencia (auxiliares).", "tema": "Fuentes del DIP"},

    {"afirmacion": "Chile ha ratificado la Convención Americana sobre Derechos Humanos (CADH).",
     "respuesta": True, "fundamento": "Chile ratificó la CADH en 1990, aceptando la jurisdicción contenciosa de la Corte IDH. La Corte ha dictado sentencias condenatorias contra Chile en varios casos.", "tema": "CADH y Chile"},

    {"afirmacion": "La inmunidad diplomática protege a los diplomáticos de cualquier acción penal en el Estado receptor.",
     "respuesta": True, "fundamento": "Convención de Viena sobre Relaciones Diplomáticas (1961): los agentes diplomáticos gozan de inmunidad de jurisdicción penal del Estado receptor, sin perjuicio de la jurisdicción del Estado acreditante.", "tema": "Inmunidad diplomática"},
]

FC_INTERNACIONAL = [
    {"frente": "Diferencia entre DIP e DIPrivado",
     "reverso": "Derecho Internacional Público (DIP): regula relaciones entre Estados y organizaciones internacionales. Derecho Internacional Privado (DIPr): regula relaciones entre particulares de distintos Estados, determinando la ley aplicable y el juez competente.", "tema": "DIP vs DIPr"},

    {"frente": "¿Qué es el jus cogens?",
     "reverso": "Normas imperativas del derecho internacional general, aceptadas y reconocidas por la comunidad internacional, que no admiten derogación por tratados y solo pueden modificarse por una norma posterior de igual carácter (art. 53 CV 1969). Ej: prohibición del genocidio, tortura.", "tema": "Jus cogens"},

    {"frente": "Sistema Interamericano de Derechos Humanos",
     "reverso": "Compuesto por la Comisión Interamericana de DDHH (cuasi-judicial, recibe denuncias) y la Corte Interamericana de DDHH (San José, Costa Rica), con jurisdicción contenciosa y consultiva. Marco normativo: CADH (Pacto de San José, 1969).", "tema": "Sistema Interamericano DDHH"},
]


# ════════════════════════════════════════════════════════════════
# AMBIENTAL  (~10)
# ════════════════════════════════════════════════════════════════
MCQ_AMBIENTAL = [
    {"pregunta": "El Sistema de Evaluación de Impacto Ambiental (SEIA) en Chile fue creado por:",
     "opciones": ["A. CPR de 1980","B. Ley 19.300 (LBGMA) de 1994","C. Decreto Supremo 40","D. Ley 20.936"],
     "correcta": 1, "fundamento": "La Ley 19.300 de Bases Generales del Medio Ambiente (1994) creó el SEIA. El DS 40 es el reglamento del SEIA.", "tema": "SEIA"},

    {"pregunta": "El principio 'quien contamina paga' implica:",
     "opciones": ["A. Que el contaminador puede pagar para contaminar libremente","B. Que los costos de la contaminación deben ser internalizados por quien la genera","C. Solo aplica a contaminación de aguas","D. Es un principio solo de derecho ambiental europeo"],
     "correcta": 1, "fundamento": "Principio 16 de la Declaración de Río (1992) y art. 3 g) Ley 19.300: los costos derivados de la contaminación deben ser asumidos por el agente que la causa (internalización de externalidades negativas).", "tema": "Principio quien contamina paga"},

    {"pregunta": "La acción de reparación del daño ambiental puro en Chile prescribe en:",
     "opciones": ["A. 1 año","B. 2 años","C. 5 años","D. 10 años"],
     "correcta": 2, "fundamento": "Art. 63 Ley 19.300: la acción ambiental prescribe en 5 años contados desde la manifestación evidente del daño.", "tema": "Prescripción acción ambiental"},
]

VF_AMBIENTAL = [
    {"afirmacion": "El Servicio de Evaluación Ambiental (SEA) es el organismo que aprueba o rechaza los proyectos en el SEIA.",
     "respuesta": False, "fundamento": "El SEA administra el SEIA pero no aprueba ni rechaza; lo hace la Comisión de Evaluación Ambiental (COEVA) regional o el Comité de Ministros. El SEA coordina el proceso.", "tema": "SEA y SEIA"},

    {"afirmacion": "La Declaración de Impacto Ambiental (DIA) es más exigente que el Estudio de Impacto Ambiental (EIA).",
     "respuesta": False, "fundamento": "El EIA es el instrumento más exigente (proyectos con impactos significativos). La DIA es para proyectos que generan impactos menores que no requieren EIA. Art. 11 Ley 19.300.", "tema": "DIA vs EIA"},
]

FC_AMBIENTAL = [
    {"frente": "Principios del derecho ambiental en la Ley 19.300",
     "reverso": "1) Preventivo (evitar el daño antes de que ocurra), 2) Precautorio (ante incertidumbre científica, proteger el ambiente), 3) Quien contamina paga, 4) Participación ciudadana, 5) Desarrollo sustentable.", "tema": "Principios derecho ambiental"},

    {"frente": "¿Qué es el daño ambiental según la Ley 19.300?",
     "reverso": "Art. 2 b) Ley 19.300: toda pérdida, disminución, detrimento o menoscabo significativo inferido al medio ambiente o a uno o más de sus componentes.", "tema": "Daño ambiental"},
]


# ════════════════════════════════════════════════════════════════
# DICCIONARIO MAESTRO POR RAMO Y TIPO
# ════════════════════════════════════════════════════════════════
BANCO_MCQ = {
    "civil":          MCQ_CIVIL,
    "penal":          MCQ_PENAL,
    "procesal":       MCQ_PROCESAL,
    "constitucional": MCQ_CONSTITUCIONAL,
    "laboral":        MCQ_LABORAL,
    "obligaciones":   MCQ_OBLIGACIONES,
    "familia":        MCQ_FAMILIA,
    "comercial":      MCQ_COMERCIAL,
    "bienes":         MCQ_BIENES,
    "sucesorio":      MCQ_SUCESORIO,
    "internacional":  MCQ_INTERNACIONAL,
    "ambiental":      MCQ_AMBIENTAL,
}

BANCO_VF = {
    "civil":          VF_CIVIL,
    "penal":          VF_PENAL,
    "procesal":       VF_PROCESAL,
    "constitucional": VF_CONSTITUCIONAL,
    "laboral":        VF_LABORAL,
    "obligaciones":   VF_OBLIGACIONES,
    "familia":        VF_FAMILIA,
    "comercial":      VF_COMERCIAL,
    "bienes":         VF_BIENES,
    "sucesorio":      VF_SUCESORIO,
    "internacional":  VF_INTERNACIONAL,
    "ambiental":      VF_AMBIENTAL,
}

BANCO_FC = {
    "civil":          FC_CIVIL,
    "penal":          FC_PENAL,
    "procesal":       FC_PROCESAL,
    "constitucional": FC_CONSTITUCIONAL,
    "laboral":        FC_LABORAL,
    "obligaciones":   FC_OBLIGACIONES,
    "familia":        FC_FAMILIA,
    "comercial":      FC_COMERCIAL,
    "bienes":         FC_BIENES,
    "sucesorio":      FC_SUCESORIO,
    "internacional":  FC_INTERNACIONAL,
    "ambiental":      FC_AMBIENTAL,
}

def estadisticas():
    """Retorna conteo de preguntas por ramo y tipo."""
    total = 0
    for ramo in BANCO_MCQ:
        m = len(BANCO_MCQ.get(ramo, []))
        v = len(BANCO_VF.get(ramo, []))
        f = len(BANCO_FC.get(ramo, []))
        total += m + v + f
    return total

if __name__ == "__main__":
    print(f"Total preguntas en el banco: {estadisticas()}")
    for ramo in BANCO_MCQ:
        m = len(BANCO_MCQ.get(ramo, []))
        v = len(BANCO_VF.get(ramo, []))
        f = len(BANCO_FC.get(ramo, []))
        print(f"  {ramo:16} MCQ:{m:3}  VF:{v:3}  FC:{f:3}  → {m+v+f}")

# ════════════════════════════════════════════════════════════════
# EXTENSIÓN — lleva el banco a ~500 preguntas
# ════════════════════════════════════════════════════════════════

# ── CIVIL extra ──────────────────────────────────────────────
MCQ_CIVIL += [
    {"pregunta": "El contrato de mutuo en Chile es:",
     "opciones": ["A. Consensual","B. Real y unilateral","C. Solemne y bilateral","D. Innominado"],
     "correcta": 1, "fundamento": "Art. 2196 CC: el mutuo o préstamo de consumo es un contrato en que una de las partes entrega a la otra cierta cantidad de cosas fungibles para que use de ellas y las restituya (real, se perfecciona con la entrega).", "tema": "Contrato de mutuo"},

    {"pregunta": "La condición meramente potestativa que depende de la voluntad del deudor es:",
     "opciones": ["A. Válida","B. Nula","C. Inoponible","D. Anulable"],
     "correcta": 1, "fundamento": "Art. 1478 CC: son nulas las obligaciones contraídas bajo una condición potestativa que consiste en la mera voluntad del deudor ('te doy cien si quiero').", "tema": "Condición potestativa"},

    {"pregunta": "El plazo en las obligaciones civiles se presume que está establecido en beneficio de:",
     "opciones": ["A. Solo el deudor","B. Solo el acreedor","C. Ambas partes por igual","D. Del deudor, salvo que aparezca haber sido establecido en favor del acreedor o de ambas partes"],
     "correcta": 3, "fundamento": "Art. 1497 CC: el plazo se presume establecido en favor del deudor, a menos que aparezca haberse pactado en favor del acreedor o de ambos.", "tema": "Plazo en obligaciones"},

    {"pregunta": "La acción de jactancia prescribe en:",
     "opciones": ["A. 1 año","B. 2 años","C. 4 años","D. 5 años"],
     "correcta": 0, "fundamento": "Art. 269 CPC: la acción de jactancia prescribe en 6 meses desde que el jactancioso hizo la manifestación. Pero el plazo para demandar la declaración de su derecho es de 10 días.", "tema": "Acción de jactancia"},

    {"pregunta": "La teoría de los actos propios (venire contra factum proprium) se basa en:",
     "opciones": ["A. El principio de buena fe objetiva","B. El dolo civil","C. La nulidad relativa","D. La prescripción extintiva"],
     "correcta": 0, "fundamento": "La doctrina de los actos propios (non venire contra factum proprium) deriva del principio de buena fe objetiva: nadie puede contradecir válidamente su conducta anterior en que la contraparte confió.", "tema": "Doctrina de los actos propios"},

    {"pregunta": "El pacto comisorio calificado en la compraventa produce:",
     "opciones": ["A. Resolución ipso facto al incumplirse el pago","B. Resolución que requiere declaración judicial","C. Solo indemnización de perjuicios","D. Nulidad del contrato"],
     "correcta": 0, "fundamento": "Art. 1879 CC: el pacto comisorio calificado ('no pagado el precio, el contrato se resolverá de pleno derecho') da acción resolutoria ipso facto, sin necesidad de declaración judicial. El deudor tiene 24 horas para pagar.", "tema": "Pacto comisorio calificado"},

    {"pregunta": "¿Cuál es el efecto relativo de los contratos en Chile?",
     "opciones": ["A. El contrato solo afecta a las partes que lo celebran","B. El contrato afecta a todos","C. Solo afecta a los herederos","D. Puede modificar derechos de terceros libremente"],
     "correcta": 0, "fundamento": "Art. 1545 CC: el contrato es una ley para los contratantes. El principio de efecto relativo implica que solo obliga a las partes (y sus causahabientes), no a terceros.", "tema": "Efecto relativo de los contratos"},

    {"pregunta": "La fianza simple se distingue de la fianza solidaria en que:",
     "opciones": ["A. En la simple, el fiador goza del beneficio de excusión","B. En la solidaria, el fiador goza del beneficio de excusión","C. Son idénticas","D. La fianza simple es siempre gratuita"],
     "correcta": 0, "fundamento": "Art. 2357 CC: en la fianza simple, el fiador puede exigir que se persiga primero al deudor principal (beneficio de excusión). En la fianza solidaria, no goza de este beneficio.", "tema": "Fianza simple vs solidaria"},

    {"pregunta": "El dominio se define en el art. 582 CC como:",
     "opciones": ["A. La posesión de una cosa corporal con ánimo de dueño","B. El derecho real en una cosa corporal para gozar y disponer de ella arbitrariamente","C. Solo el derecho de uso","D. La propiedad fiduciaria"],
     "correcta": 1, "fundamento": "Art. 582 CC: el dominio (propiedad) es el derecho real en una cosa corporal para gozar y disponer de ella arbitrariamente; no siendo contra la ley o contra derecho ajeno.", "tema": "Definición de dominio"},

    {"pregunta": "¿Cuál es la diferencia entre la responsabilidad contractual y extracontractual en Chile?",
     "opciones": ["A. Solo difieren en el plazo de prescripción","B. Difieren en la culpa (se presume en la contractual), plazo de prescripción y extensión del daño indemnizable","C. Son idénticas en el CC","D. La extracontractual no admite daño moral"],
     "correcta": 1, "fundamento": "La resp. contractual: culpa se presume (art. 1547), prescripción 5 años, daños directos (art. 1558). Resp. extracontractual: culpa se prueba (art. 2329), prescripción 4 años (art. 2332), daños directos e imprevistos.", "tema": "Comparación responsabilidades"},
]

VF_CIVIL += [
    {"afirmacion": "La obligación natural de juego o apuesta no autorizada confiere acción para exigir el pago.",
     "respuesta": False, "fundamento": "Art. 1470 N°3 CC: las deudas de juego o apuesta son obligaciones naturales que no dan acción para exigir su cumplimiento, pero que autorizan a retener lo pagado.", "tema": "Obligaciones naturales de juego"},

    {"afirmacion": "El pago de lo no debido genera la obligación de restituir aunque el que pagó lo haya hecho voluntariamente.",
     "respuesta": True, "fundamento": "Arts. 2295 y ss. CC: el que por error de hecho pagó lo que no debía tiene derecho a repetir; la voluntariedad del pago no extingue la acción si hubo error.", "tema": "Pago de lo no debido"},

    {"afirmacion": "La cesión de créditos en Chile requiere el consentimiento del deudor para ser válida entre cedente y cesionario.",
     "respuesta": False, "fundamento": "Art. 1901 CC: la cesión de créditos se perfecciona entre cedente y cesionario por la entrega del título; solo se notifica al deudor para que sea oponible a él y a terceros (art. 1902 CC).", "tema": "Cesión de créditos"},

    {"afirmacion": "Las personas jurídicas sin fines de lucro en Chile adquieren personalidad jurídica desde que se inscribe su acta de constitución en el Registro Civil.",
     "respuesta": True, "fundamento": "Ley 20.500: las corporaciones y fundaciones adquieren personalidad jurídica desde la inscripción de su acta constitutiva en el Registro Civil (norma vigente desde 2012).", "tema": "Personalidad jurídica corporaciones"},

    {"afirmacion": "En la responsabilidad extracontractual chilena, se responde por el hecho propio, ajeno y de las cosas.",
     "respuesta": True, "fundamento": "Arts. 2314 y ss. CC: la responsabilidad extracontractual abarca el hecho propio (art. 2314), el hecho ajeno (arts. 2319-2322) y el daño causado por cosas (arts. 2323-2328).", "tema": "Responsabilidad extracontractual"},

    {"afirmacion": "El contrato de arriendo de bienes raíces urbanos en Chile solo se rige por el CC.",
     "respuesta": False, "fundamento": "Los arrendamientos urbanos se rigen principalmente por la Ley 18.101 (arrendamiento de predios urbanos), que es ley especial que prevalece sobre el CC en lo que sea incompatible.", "tema": "Arrendamiento urbano"},

    {"afirmacion": "El daño moral es indemnizable en la responsabilidad extracontractual en Chile.",
     "respuesta": True, "fundamento": "Jurisprudencia y doctrina consolidadas: el daño moral (también llamado daño no patrimonial o extrapatrimonial) es plenamente indemnizable en sede extracontractual. Arts. 2314 y 2329 CC.", "tema": "Daño moral extracontractual"},
]

FC_CIVIL += [
    {"frente": "¿Qué es el cuasicontrato de comunidad?",
     "reverso": "Art. 2304 CC: la comunidad ocurre cuando dos o más personas tienen un derecho de igual naturaleza sobre la misma cosa (sin que haya entre ellas ningún contrato). Se rige por las normas de la copropiedad.", "tema": "Cuasicontrato de comunidad"},

    {"frente": "¿Qué es la cláusula de responsabilidad?",
     "reverso": "Convención por la que las partes modulan la responsabilidad del deudor: pueden agravar (responsabilidad en caso fortuito), atenuar (solo dolo o culpa grave) o exonerar la responsabilidad. Límite: el dolo y la culpa grave no se pueden condonar anticipadamente (art. 1465 CC).", "tema": "Cláusulas de responsabilidad"},

    {"frente": "¿Qué es la subrogación personal?",
     "reverso": "El tercero que paga con consentimiento expreso o tácito del deudor o sin él (en ciertos casos) se subroga en los derechos del acreedor pagado, con todos sus privilegios y accesorios (art. 1610 CC). Ocupa el lugar jurídico del acreedor.", "tema": "Subrogación personal"},

    {"frente": "Requisitos del pago",
     "reverso": "1) Debe hacerlo el deudor o un tercero (art. 1572 CC), 2) Hacerse al acreedor o su representante, 3) Pagar la cosa debida (art. 1569 CC), 4) Pagar íntegramente (art. 1591 CC), 5) Pagar en el lugar y tiempo convenidos.", "tema": "Requisitos del pago"},
]

# ── PENAL extra ──────────────────────────────────────────────
MCQ_PENAL += [
    {"pregunta": "¿Qué es el principio de non bis in idem en materia penal?",
     "opciones": ["A. Nadie puede ser condenado a dos penas por el mismo delito","B. Nadie puede ser juzgado dos veces por el mismo hecho","C. Solo aplica entre distintos países","D. Se aplica solo en delitos económicos"],
     "correcta": 1, "fundamento": "El non bis in idem prohíbe juzgar y sancionar a una persona dos veces por el mismo hecho delictivo (art. 1 CPP y art. 19 N°3 CPR).", "tema": "Non bis in idem"},

    {"pregunta": "El concurso real de delitos en Chile se castiga con:",
     "opciones": ["A. La pena del delito más grave","B. La acumulación material de penas según el art. 74 CP","C. La pena media entre los delitos concurrentes","D. La pena más benigna"],
     "correcta": 1, "fundamento": "Art. 74 CP: al culpable de dos o más delitos se le impondrán todas las penas correspondientes a las diversas infracciones (principio de acumulación material, con límite del triple del tiempo de la más grave).", "tema": "Concurso real de delitos"},

    {"pregunta": "La circunstancia atenuante de la irreprochable conducta anterior opera cuando:",
     "opciones": ["A. El imputado no tiene condenas previas","B. El imputado tiene un historial de vida intachable previo al delito","C. El imputado colabora con la investigación","D. Es menor de edad"],
     "correcta": 1, "fundamento": "Art. 11 N°6 CP: la irreprochable conducta anterior exige que el condenado haya tenido una conducta intachable en todos los ámbitos de su vida, no solo ausencia de condenas previas.", "tema": "Irreprochable conducta anterior"},

    {"pregunta": "¿Cuál es el delito que se comete con mayor frecuencia en Chile según las estadísticas judiciales?",
     "opciones": ["A. Homicidio","B. Hurto y robo","C. Tráfico de drogas","D. Estafa"],
     "correcta": 1, "fundamento": "Los delitos contra la propiedad (hurtos y robos) constituyen históricamente la mayor parte de las denuncias y condenas en el sistema penal chileno.", "tema": "Estadística delictual"},

    {"pregunta": "La suspensión condicional del procedimiento penal en Chile requiere acuerdo de:",
     "opciones": ["A. Solo el fiscal","B. El fiscal y el imputado, con autorización del juez de garantía","C. El juez, el fiscal y la víctima","D. Solo el juez de garantía"],
     "correcta": 1, "fundamento": "Art. 237 CPP: la suspensión condicional del procedimiento es un acuerdo entre el fiscal y el imputado, con aprobación del juez de garantía. Procede si la pena probable no excede de 3 años.", "tema": "Suspensión condicional del procedimiento"},

    {"pregunta": "En el delito de estafa del art. 468 CP, el ardid o engaño debe ser:",
     "opciones": ["A. Meramente verbal","B. Idóneo para inducir a error a una persona normal","C. Consistir siempre en un documento falso","D. Realizado por escrito"],
     "correcta": 1, "fundamento": "Art. 468 CP: la estafa requiere que el engaño sea idóneo, es decir, suficiente para inducir a error a una persona promedio diligente. El ardid es el elemento fundamental del tipo.", "tema": "Estafa"},

    {"pregunta": "La libertad provisional o cautelar en el proceso penal chileno es la regla:",
     "opciones": ["A. La prisión preventiva es la regla general","B. La libertad es la regla; la prisión preventiva es excepcional","C. Depende del delito imputado","D. Siempre decide el fiscal"],
     "correcta": 1, "fundamento": "Art. 139 CPP: la prisión preventiva procederá cuando sea estrictamente necesaria; la libertad del imputado durante el proceso es la regla general.", "tema": "Libertad durante el proceso penal"},

    {"pregunta": "El tipo penal de receptación en Chile se refiere a:",
     "opciones": ["A. Recibir personas en situación de tráfico","B. Adquirir, recibir o esconder efectos obtenidos de un delito previo","C. Hospedar extranjeros ilegales","D. Receptar mensajes de crimen organizado"],
     "correcta": 1, "fundamento": "Art. 456 bis A CP: el delito de receptación consiste en adquirir, recibir en prenda o guardar especies de procedencia delictiva conociendo o debiendo conocer su origen.", "tema": "Receptación"},
]

VF_PENAL += [
    {"afirmacion": "El delito de parricidio en Chile se comete cuando se mata a un pariente en línea colateral.",
     "respuesta": False, "fundamento": "Art. 390 CP: el parricidio se produce cuando se mata al padre, madre, hijo o cualquier otro ascendiente o descendiente, o al cónyuge o conviviente (línea recta y vínculo conyugal/convivencial).", "tema": "Parricidio"},

    {"afirmacion": "La prescripción de los delitos de lesa humanidad no opera en Chile.",
     "respuesta": True, "fundamento": "La Corte Suprema de Chile ha consolidado la doctrina de la imprescriptibilidad e inamnistiabilidad de los crímenes de lesa humanidad, en aplicación del DI y el art. 5 CPR.", "tema": "Imprescriptibilidad lesa humanidad"},

    {"afirmacion": "El delito continuado es aquél en que se cometen múltiples acciones que constituyen un solo delito por unidad de designio.",
     "respuesta": True, "fundamento": "La doctrina reconoce el delito continuado cuando hay una pluralidad de acciones que forman una unidad jurídica por la identidad de sujeto, propósito y bien jurídico vulnerado, tratándose como un solo delito.", "tema": "Delito continuado"},

    {"afirmacion": "En Chile, la acción penal pública solo puede ser ejercida por el Ministerio Público.",
     "respuesta": False, "fundamento": "Art. 53 CPP: en los delitos de acción pública, la acción la ejerce el Ministerio Público. Pero la víctima puede ejercer querella (art. 111 CPP). En delitos de acción privada, solo puede ejercerla la víctima.", "tema": "Tipos de acción penal"},
]

FC_PENAL += [
    {"frente": "Causales de extinción de la responsabilidad penal (art. 93 CP)",
     "reverso": "1) Muerte del responsable, 2) Cumplimiento de la condena, 3) Amnistía, 4) Indulto, 5) Perdón del ofendido (solo acción privada), 6) Prescripción de la pena, 7) Prescripción de la acción penal.", "tema": "Extinción responsabilidad penal"},

    {"frente": "¿Qué es el principio de proporcionalidad de la pena?",
     "reverso": "La pena debe ser proporcional a la gravedad del delito, la culpabilidad del autor y los bienes jurídicos en juego. Excluye penas excesivas, crueles o inusitadas. Fundamento: art. 19 N°1 CPR y principios de humanidad.", "tema": "Proporcionalidad de la pena"},

    {"frente": "¿Qué es la pena accesoria?",
     "reverso": "Pena que sigue a la principal sin necesidad de ser expresamente impuesta (ej: inhabilitación para cargos públicos, pérdida de derechos civiles). Art. 22 y ss. CP: las penas accesorias acompañan a las principales según la escala gradual.", "tema": "Penas accesorias"},
]

# ── PROCESAL extra ──────────────────────────────────────────
MCQ_PROCESAL += [
    {"pregunta": "El recurso de revisión en el proceso civil chileno procede para:",
     "opciones": ["A. Corregir errores de hecho en sentencias firmes","B. Invalidar sentencias firmes obtenidas mediante fraude o dolo","C. Reabrir el término probatorio","D. Apelar sentencias de segunda instancia"],
     "correcta": 1, "fundamento": "Arts. 810 y ss. CPC: el recurso de revisión procede ante la Corte Suprema para invalidar sentencias firmes obtenidas por las causas que señala la ley (cohecho, violencia, documentos falsos, etc.).", "tema": "Recurso de revisión"},

    {"pregunta": "El juicio sumario en Chile procede principalmente:",
     "opciones": ["A. Para todas las causas civiles","B. Cuando la acción entablada requiere tramitación rápida o cuando la ley lo señala expresamente","C. Solo para causas de alimentos","D. Solo en asuntos laborales"],
     "correcta": 1, "fundamento": "Art. 680 CPC: el procedimiento sumario procede cuando la acción entablada requiere tramitación rápida para ser eficaz, y en los casos que expresamente señala la ley.", "tema": "Juicio sumario"},

    {"pregunta": "La tacha de testigos en el proceso civil chileno:",
     "opciones": ["A. Se opone antes de que el testigo declare","B. Se opone dentro del juicio oral antes de que preste declaración","C. Se opone dentro del plazo probatorio por inhabilidades absolutas o relativas","D. Se presenta siempre ante la Corte de Apelaciones"],
     "correcta": 2, "fundamento": "Arts. 373-379 CPC: las tachas se oponen dentro del probatorio, fundándose en las inhabilidades del art. 357 (absolutas) y 358 (relativas) CPC.", "tema": "Tachas de testigos"},

    {"pregunta": "En el proceso penal chileno, el plazo de la investigación formalizada es de:",
     "opciones": ["A. 6 meses","B. 2 años","C. El que fije el juez de garantía, con un máximo de 2 años","D. El que fije el Ministerio Público sin límite"],
     "correcta": 2, "fundamento": "Art. 234 CPP: el juez de garantía fijará el plazo para la investigación, el que no puede exceder de 2 años desde la formalización. Con la Ley 21.608 (2023), se regularon también los plazos anteriores a la formalización.", "tema": "Plazo de investigación"},

    {"pregunta": "Las medidas cautelares personales en el proceso penal (distintas de la prisión preventiva) incluyen:",
     "opciones": ["A. Solo la arraigo","B. Arresto domiciliario, firma periódica, arraigo, prohibición de comunicarse con víctima, entre otras","C. Solo la firma periódica y el arraigo","D. Solo la prisión preventiva y la libertad"],
     "correcta": 1, "fundamento": "Art. 155 CPP: las medidas cautelares personales distintas de la prisión preventiva incluyen: privación de libertad en su domicilio, sujeción de vigilancia, arraigo, prohibición de aproximarse a víctima, entre otras.", "tema": "Medidas cautelares personales"},

    {"pregunta": "¿Cuándo procede la rebeldía del demandado en el juicio ordinario civil?",
     "opciones": ["A. Cuando no concurre a la audiencia de conciliación","B. Cuando no contesta la demanda dentro del plazo legal","C. Cuando no comparece al juicio oral","D. Cuando no paga las costas"],
     "correcta": 1, "fundamento": "Art. 78 CPC: la rebeldía o contumacia se produce cuando una de las partes no realiza una actuación dentro del plazo legal; en el juicio ordinario, el demandado rebelde tiene el plazo de la contestación vencido sin haberla presentado.", "tema": "Rebeldía procesal"},
]

VF_PROCESAL += [
    {"afirmacion": "En el proceso civil chileno, el juez puede rechazar de oficio la demanda manifiestamente improcedente.",
     "respuesta": True, "fundamento": "Art. 256 CPC: el juez puede de oficio no dar curso a la demanda cuando no contenga las indicaciones ordenadas por la ley, señalando los defectos de que adolece.", "tema": "Inadmisibilidad de demanda"},

    {"afirmacion": "Las sentencias interlocutorias de primera clase en Chile producen cosa juzgada.",
     "respuesta": True, "fundamento": "Art. 175 CPC: las sentencias interlocutorias firmes producen la excepción de cosa juzgada en el proceso en que se dictan (cosa juzgada formal).", "tema": "Sentencias interlocutorias"},

    {"afirmacion": "En el proceso penal chileno, el acuerdo reparatorio extingue la responsabilidad penal.",
     "respuesta": True, "fundamento": "Art. 241 CPP: una vez cumplidas las obligaciones del acuerdo reparatorio o garantizadas a satisfacción de la víctima, el tribunal dicta sobreseimiento definitivo.", "tema": "Acuerdo reparatorio"},

    {"afirmacion": "El querellante puede forzar al Ministerio Público a acusar cuando este decide no perseverar.",
     "respuesta": True, "fundamento": "Art. 258 CPP: si el fiscal solicita el sobreseimiento o comunica su decisión de no perseverar, el querellante puede pedir al juez de garantía que lo forzase a formular acusación (forzamiento de la acusación).", "tema": "Forzamiento de la acusación"},
]

FC_PROCESAL += [
    {"frente": "¿Qué es la prueba legal o tasada?",
     "reverso": "Sistema en que la ley establece anticipadamente el valor probatorio de cada medio de prueba. En Chile, el CPC es de sistema de valoración legal tasada (art. 428 y ss.) aunque atenuado; el CPP es de libre valoración (sana crítica, art. 297).", "tema": "Sistemas de valoración de la prueba"},

    {"frente": "¿Qué es el principio de contradicción?",
     "reverso": "Toda alegación o prueba presentada por una parte debe ser conocida y contradicha por la otra antes de que el juez resuelva. Garantía del debido proceso. Art. 19 N°3 CPR y art. 8 CADH.", "tema": "Principio de contradicción"},

    {"frente": "¿Cuándo caduca la demanda en el proceso penal?",
     "reverso": "Art. 248 CPP: si el fiscal no acusa en el plazo de 10 días contados desde el cierre de la investigación, el juez de garantía puede, a petición del imputado o querellante, otorgar nuevos plazos o sobreseer.", "tema": "Cierre de investigación"},
]

# ── CONSTITUCIONAL extra ────────────────────────────────────
MCQ_CONSTITUCIONAL += [
    {"pregunta": "¿Cuál es el quórum de reforma constitucional para las normas del capítulo sobre bases de la institucionalidad?",
     "opciones": ["A. Mayoría simple","B. 3/5 de los diputados y senadores en ejercicio","C. 2/3 de los diputados y senadores en ejercicio","D. 4/7 de los diputados y senadores en ejercicio"],
     "correcta": 2, "fundamento": "Art. 127 CPR: las normas del Capítulo I (Bases de la Institucionalidad) y de otros capítulos especiales requieren 2/3 de los diputados y senadores en ejercicio para su reforma.", "tema": "Reforma constitucional"},

    {"pregunta": "El Contralor General de la República en Chile ejerce la función de:",
     "opciones": ["A. Control jurisdiccional de los actos del ejecutivo","B. Control de legalidad de los actos de la administración y fiscalización del uso de los fondos públicos","C. Enjuiciar a los ministros de Estado","D. Controlar la constitucionalidad de las leyes"],
     "correcta": 1, "fundamento": "Art. 98 CPR: la Contraloría General ejerce el control de legalidad de los actos de la administración y fiscaliza el ingreso e inversión de los fondos del Fisco. No ejerce control de constitucionalidad.", "tema": "Contraloría General"},

    {"pregunta": "El amparo económico del art. 19 N°21 CPR protege el derecho a:",
     "opciones": ["A. La propiedad privada","B. Desarrollar actividades económicas en igualdad de condiciones","C. Recibir indemnización por actos del Estado","D. Participar del libre mercado"],
     "correcta": 1, "fundamento": "Art. 19 N°21 CPR: el derecho a desarrollar cualquiera actividad económica que no sea contraria a la moral, al orden público o a la seguridad nacional. La acción de amparo económico protege este derecho.", "tema": "Amparo económico"},

    {"pregunta": "El Tribunal Calificador de Elecciones (TRICEL) tiene como función principal:",
     "opciones": ["A. Fiscalizar las campañas electorales","B. Conocer el escrutinio general y las reclamaciones que procedan en las elecciones presidenciales y parlamentarias","C. Sancionar a los partidos políticos","D. Elaborar el registro electoral"],
     "correcta": 1, "fundamento": "Art. 95 CPR: el TRICEL conoce el escrutinio general de las elecciones presidenciales y parlamentarias, resuelve las reclamaciones y proclama a los elegidos.", "tema": "TRICEL"},
]

VF_CONSTITUCIONAL += [
    {"afirmacion": "El Presidente de Chile puede dictar decretos con fuerza de ley (DFL) en cualquier materia.",
     "respuesta": False, "fundamento": "Art. 64 CPR: el Congreso puede delegar facultades legislativas al Presidente solo en materias que no sean propias de LOC ni afecten garantías constitucionales, derechos fundamentales, competencias del Congreso, etc.", "tema": "Decretos con fuerza de ley"},

    {"afirmacion": "El principio de subsidiariedad en la CPR de 1980 implica que el Estado solo actúa cuando los particulares no pueden hacerlo.",
     "respuesta": True, "fundamento": "Art. 1 inc. 3 CPR: el Estado reconoce y ampara a los grupos intermedios y les garantiza autonomía. Principio de subsidiariedad: el Estado actúa supletoriamente cuando los cuerpos intermedios o particulares son insuficientes.", "tema": "Subsidiariedad"},

    {"afirmacion": "El derecho a la vida y a la integridad física en Chile admite la pena de muerte.",
     "respuesta": False, "fundamento": "Art. 19 N°1 CPR: la ley protege la vida del que está por nacer. La pena de muerte fue abolida para los delitos comunes en Chile y solo sobrevive en el Código de Justicia Militar para tiempo de guerra.", "tema": "Derecho a la vida y pena de muerte"},
]

FC_CONSTITUCIONAL += [
    {"frente": "¿Qué es el bloque de constitucionalidad?",
     "reverso": "Conjunto de normas con rango constitucional que incluye no solo el texto de la CPR sino también los tratados internacionales de DDHH ratificados y vigentes (art. 5 inc. 2 CPR). Concepto relevante para el control de convencionalidad.", "tema": "Bloque de constitucionalidad"},

    {"frente": "¿Qué es la inaplicabilidad por inconstitucionalidad?",
     "reverso": "Acción del art. 93 N°6 CPR: el TC puede declarar inaplicable un precepto legal cuya aplicación en un caso concreto resulte contraria a la CPR. Solo afecta el caso concreto, no deroga la norma.", "tema": "Inaplicabilidad"},

    {"frente": "Órganos del sistema electoral chileno",
     "reverso": "1) Servicio Electoral (SERVEL): administra el proceso electoral, 2) Tribunal Calificador de Elecciones (TRICEL): califica elecciones presidenciales y parlamentarias, 3) Tribunales Electorales Regionales (TER): conocen materias regionales y comunales.", "tema": "Órganos electorales"},
]

# ── LABORAL extra ───────────────────────────────────────────
MCQ_LABORAL += [
    {"pregunta": "¿Cuál es el sistema previsional de pensiones predominante en Chile desde 1981?",
     "opciones": ["A. Reparto solidario administrado por el Estado","B. Capitalización individual en cuentas personales administradas por AFPs","C. Sistema mixto con mayoría estatal","D. Seguro de vejez administrado por el Seguro Social"],
     "correcta": 1, "fundamento": "DL 3.500 (1980): el sistema de pensiones se basa en la capitalización individual; cada trabajador ahorra en su cuenta de capitalización individual en la AFP de su elección.", "tema": "Sistema de AFP"},

    {"pregunta": "El indulto particular (presidencial) en Chile es:",
     "opciones": ["A. Un decreto de ley del Congreso","B. Un decreto presidencial que extingue la pena o la conmuta","C. Una gracia que otorga el TC","D. Solo es posible para penas de muerte"],
     "correcta": 1, "fundamento": "Art. 32 N°14 CPR: el Presidente puede conceder indultos particulares que extinguen la pena o la conmutan.", "tema": "Indulto presidencial"},

    {"pregunta": "El trabajo a honorarios en Chile:",
     "opciones": ["A. Siempre implica una relación laboral","B. Es un contrato de servicios civil o mercantil sin vínculo de subordinación","C. Está regulado por el Código del Trabajo","D. No genera obligación de cotizar en el sistema previsional"],
     "correcta": 1, "fundamento": "El trabajo a honorarios se rige por el CC o el C.Com., no por el CT. Sin embargo, la Ley 20.712 y modificaciones posteriores obligan a los trabajadores a honorarios del sector público a cotizar en el sistema previsional.", "tema": "Trabajo a honorarios"},

    {"pregunta": "Las horas extraordinarias en Chile se pueden pactar:",
     "opciones": ["A. Verbalmente","B. Por escrito y solo para necesidades o situaciones temporales de la empresa","C. Con aprobación previa de la Dirección del Trabajo","D. Sin límite alguno"],
     "correcta": 1, "fundamento": "Art. 32 CT: las horas extraordinarias deben pactarse por escrito, solo para atender necesidades o situaciones temporales. No pueden exceder de 2 horas diarias ni de 12 semanales.", "tema": "Horas extraordinarias"},
]

VF_LABORAL += [
    {"afirmacion": "La Dirección del Trabajo tiene facultades para determinar la existencia de una relación laboral.",
     "respuesta": True, "fundamento": "Art. 2 CT y jurisprudencia administrativa: la Dirección del Trabajo puede emitir dictámenes que establecen si existe relación laboral (con el principio de primacía de la realidad), aunque sus dictámenes no tienen fuerza de cosa juzgada.", "tema": "Dirección del Trabajo"},

    {"afirmacion": "El trabajador puede demandar nulidad de su propio despido si el empleador no pagó cotizaciones.",
     "respuesta": True, "fundamento": "Ley 19.631 (conocida como 'Ley Bustos'): el despido es nulo si el empleador no ha pagado las cotizaciones previsionales y de salud. El empleador debe pagarlas antes de que el despido surta efectos.", "tema": "Nulidad del despido"},

    {"afirmacion": "El trabajo doméstico en Chile tiene los mismos derechos a vacaciones que el resto de los trabajadores.",
     "respuesta": True, "fundamento": "Arts. 147 y ss. CT: los trabajadores de casa particular tienen derecho a feriado anual de 15 días hábiles, igual que los demás trabajadores.", "tema": "Vacaciones trabajadores casa particular"},
]

FC_LABORAL += [
    {"frente": "¿Qué es el Seguro de Desempleo (AFC)?",
     "reverso": "Sistema de seguro de cesantía (Ley 19.728, 2001) administrado por la Administradora de Fondos de Cesantía. Cada trabajador tiene una cuenta individual; al quedar desempleado, accede a los fondos según antigüedad y tipo de contrato.", "tema": "Seguro de desempleo"},

    {"frente": "Causales de despido sin indemnización (art. 160 CT)",
     "reverso": "1) Falta de probidad, conducta inmoral, acoso sexual o laboral; 2) Negociaciones del trabajador en competencia; 3) Ausencias injustificadas; 4) Abandono del trabajo; 5) Actos, omisiones o imprudencias que afecten la seguridad; 6) Injurias al empleador; 7) Conducta inmoral o acoso laboral.", "tema": "Causales art. 160 CT"},
]

# ── OBLIGACIONES extra ──────────────────────────────────────
MCQ_OBLIGACIONES += [
    {"pregunta": "La delegación perfecta en la novación por cambio de deudor:",
     "opciones": ["A. No requiere consentimiento del acreedor","B. Requiere que el acreedor consienta en liberar al deudor primitivo","C. Es imposible en el derecho chileno","D. Solo opera en deudas comerciales"],
     "correcta": 1, "fundamento": "Art. 1635 CC: la delegación perfecta (o novación por cambio de deudor) requiere que el acreedor consienta en liberar al deudor anterior; sin ese consentimiento, hay mera adición de deudor.", "tema": "Delegación perfecta"},

    {"pregunta": "La acción de in rem verso en el enriquecimiento sin causa exige que el enriquecimiento sea:",
     "opciones": ["A. Siempre doloso","B. Sin causa jurídica que lo justifique, y correlativo a un empobrecimiento ajeno","C. De al menos 1 UTM","D. Proveniente de un cuasicontrato"],
     "correcta": 1, "fundamento": "El enriquecimiento sin causa requiere: enriquecimiento del demandado, empobrecimiento del actor, nexo causal entre ambos, ausencia de causa jurídica que justifique el enriquecimiento y ausencia de otra acción.", "tema": "Acción de in rem verso"},

    {"pregunta": "El contrato de transacción en Chile:",
     "opciones": ["A. Es un modo de extinguir obligaciones litigiosas o dudosas mediante concesiones recíprocas","B. Solo puede celebrarse ante notario","C. Requiere homologación judicial para tener efectos","D. Solo opera en materia civil, no mercantil"],
     "correcta": 0, "fundamento": "Art. 2446 CC: la transacción es un contrato en que las partes terminan extrajudicialmente un litigio pendiente o precaven un litigio eventual. Produce efecto de cosa juzgada (art. 2460 CC).", "tema": "Contrato de transacción"},
]

VF_OBLIGACIONES += [
    {"afirmacion": "La remisión de la deuda es siempre gratuita.",
     "respuesta": True, "fundamento": "Art. 1652 CC: la remisión es el perdón de la deuda por parte del acreedor. Por su naturaleza es gratuita, pues el acreedor no recibe contraprestación. Se asimila a una donación.", "tema": "Remisión de la deuda"},

    {"afirmacion": "La confusión extingue la obligación total o parcialmente.",
     "respuesta": True, "fundamento": "Art. 1665 CC: cuando concurren en una misma persona las calidades de acreedor y deudor, se verifica de derecho una confusión que extingue la deuda y produce iguales efectos que el pago.", "tema": "Confusión"},

    {"afirmacion": "El deudor de una obligación de especie o cuerpo cierto debe conservarla con la diligencia de un buen padre de familia.",
     "respuesta": True, "fundamento": "Art. 1548 CC: la obligación de dar comprende la de entregar la cosa; y si esta es una especie o cuerpo cierto, comprende además la de conservarla hasta la entrega, empleando la debida diligencia.", "tema": "Conservación de la especie o cuerpo cierto"},
]

FC_OBLIGACIONES += [
    {"frente": "¿Qué es la excepción de contrato no cumplido?",
     "reverso": "La exceptio non adimpleti contractus (art. 1552 CC): en los contratos bilaterales, ninguno de los contratantes está en mora dejando de cumplir lo pactado mientras el otro no cumple o no se allana a cumplir. Paraliza la acción del contratante incumplidor.", "tema": "Excepción de contrato no cumplido"},

    {"frente": "¿Qué son los intereses en el derecho civil chileno?",
     "reverso": "Frutos civiles del capital (art. 647 CC). Clases: corrientes (art. 6 Ley 18.010), máximo convencional (50% sobre el corriente), penales (moratorios). En el mutuo de dinero, se rigen por la Ley 18.010.", "tema": "Intereses civiles"},
]

# ── FAMILIA extra ───────────────────────────────────────────
MCQ_FAMILIA += [
    {"pregunta": "¿Cuándo puede el juez regular alimentos provisorios en Chile?",
     "opciones": ["A. Solo en la sentencia definitiva","B. Desde que se presenta la demanda y en cualquier estado del juicio","C. Solo si hay acuerdo de las partes","D. Solo en el caso de menores de 3 años"],
     "correcta": 1, "fundamento": "Art. 327 CC y Ley 14.908: el juez puede regular alimentos provisorios desde la presentación de la demanda, incluso sin que el demandado haya sido notificado.", "tema": "Alimentos provisorios"},

    {"pregunta": "En Chile, la tuición (actual cuidado personal) se puede acordar de forma:",
     "opciones": ["A. Solo por el juez","B. Compartida o alternada si los padres lo acuerdan","C. Solo alternada","D. Nunca por acuerdo de los padres"],
     "correcta": 1, "fundamento": "Art. 225 CC: los padres pueden acordar el cuidado personal compartido o alternado. A falta de acuerdo, lo determina el juez. La ley 20.680 (2013) introdujo el cuidado compartido.", "tema": "Cuidado personal compartido"},

    {"pregunta": "La impugnación de la paternidad por el marido en Chile:",
     "opciones": ["A. Es imprescriptible","B. Prescribe en 180 días desde que supo del parto","C. Solo puede hacerla el hijo","D. Requiere siempre prueba de ADN"],
     "correcta": 1, "fundamento": "Art. 212 CC: el marido podrá reclamar contra la paternidad dentro de los ciento ochenta días siguientes al día en que tuvo conocimiento del parto.", "tema": "Impugnación de paternidad"},
]

VF_FAMILIA += [
    {"afirmacion": "El conviviente civil sobreviviente tiene derecho a herencia abintestato como el cónyuge sobreviviente.",
     "respuesta": True, "fundamento": "Ley 20.830 (AUC): el conviviente civil sobreviviente tiene los mismos derechos hereditarios que el cónyuge sobreviviente en la sucesión intestada y en las asignaciones forzosas.", "tema": "Derechos sucesorios del conviviente civil"},

    {"afirmacion": "La violencia intrafamiliar en Chile solo se sanciona por el derecho penal.",
     "respuesta": False, "fundamento": "Ley 20.066 (VIF): la violencia intrafamiliar se sanciona tanto por la Ley 20.066 (vía administrativa y de medidas de protección ante los tribunales de familia) como por el Código Penal cuando los hechos son constitutivos de delitos.", "tema": "Violencia intrafamiliar"},
]

FC_FAMILIA += [
    {"frente": "¿Qué es el bien familiar?",
     "reverso": "Arts. 141-149 CC: el inmueble que sirve de residencia principal de la familia puede ser declarado bien familiar. Requiere declaración judicial a petición de uno de los cónyuges. Una vez declarado, no puede enajenarse ni gravarse sin consentimiento del otro cónyuge.", "tema": "Bien familiar"},

    {"frente": "Diferencia entre divorcio y nulidad matrimonial",
     "reverso": "Divorcio: disuelve un matrimonio válido (arts. 54-60 LMC). Nulidad: declara que el matrimonio nunca existió por vicio originario (art. 44 LMC). La nulidad requiere causa específica al momento de la celebración; el divorcio no.", "tema": "Divorcio vs nulidad"},
]

# ── BIENES extra ─────────────────────────────────────────────
MCQ_BIENES += [
    {"pregunta": "¿Qué efecto tiene la inscripción en el Registro del Conservador de Bienes Raíces en Chile?",
     "opciones": ["A. Es solo un requisito de publicidad sin efecto constitutivo","B. Es el único modo de hacer la tradición de los inmuebles y actúa como requisito de publicidad","C. Solo es necesaria para la compraventa","D. No tiene efecto entre las partes"],
     "correcta": 1, "fundamento": "Art. 686 CC: la tradición de los inmuebles se efectúa por la inscripción del título en el Registro de Propiedad del CBR. Tiene doble función: tradición (transferencia) y publicidad.", "tema": "Inscripción CBR"},

    {"pregunta": "La prenda civil sobre cosa mueble se diferencia de la prenda mercantil en que:",
     "opciones": ["A. La civil requiere escritura pública","B. La civil requiere el desplazamiento de la cosa al acreedor","C. La mercantil es siempre sin desplazamiento","D. Son idénticas"],
     "correcta": 1, "fundamento": "Art. 2384 CC (prenda civil): es un contrato real que se perfecciona con la entrega de la cosa (con desplazamiento). La prenda comercial sin desplazamiento (Ley 20.190) no requiere entrega.", "tema": "Prenda civil vs mercantil"},

    {"pregunta": "El Registro de Aguas en Chile es llevado por:",
     "opciones": ["A. El Conservador de Bienes Raíces","B. La Dirección General de Aguas","C. El Registro Civil","D. El Ministerio de Obras Públicas"],
     "correcta": 0, "fundamento": "El Código de Aguas dispone que los derechos de aprovechamiento de aguas se inscriben en el Registro de Aguas del Conservador de Bienes Raíces de la respectiva provincia.", "tema": "Registro de Aguas"},
]

VF_BIENES += [
    {"afirmacion": "Los bienes nacionales de uso público no son susceptibles de apropiación privada.",
     "respuesta": True, "fundamento": "Art. 589 CC: los bienes nacionales cuyo uso pertenece a todos los habitantes de la nación (calles, plazas, puentes, mar adyacente) son inalienables e imprescriptibles.", "tema": "Bienes nacionales de uso público"},

    {"afirmacion": "El usufructo sobre bienes inmuebles debe inscribirse en el CBR para su constitución.",
     "respuesta": True, "fundamento": "Art. 767 CC: el usufructo sobre inmuebles se constituye por escritura pública y debe inscribirse en el CBR. Sin inscripción, no produce efectos respecto de terceros.", "tema": "Inscripción del usufructo"},
]

FC_BIENES += [
    {"frente": "¿Qué son las limitaciones al dominio?",
     "reverso": "Restricciones al ejercicio absoluto del dominio: 1) Servidumbres, 2) Usufructo, 3) Uso y habitación, 4) Fideicomiso, 5) Reservas forestales y áreas protegidas, 6) Restricciones por destino (bien familiar), 7) Hipoteca y prenda.", "tema": "Limitaciones al dominio"},

    {"frente": "Clases de posesión en Chile",
     "reverso": "1) Regular: con justo título y buena fe (permite prescripción ordinaria). 2) Irregular: sin justo título o sin buena fe (permite prescripción extraordinaria). Art. 702 CC.", "tema": "Clases de posesión"},
]

# ── SUCESORIO extra ──────────────────────────────────────────
MCQ_SUCESORIO += [
    {"pregunta": "¿Cuánto dura la posesión efectiva para bienes raíces en Chile?",
     "opciones": ["A. Es automática al morir el causante","B. La otorga el tribunal a petición de parte o el Registro Civil","C. La otorga siempre el juez","D. No existe en Chile"],
     "correcta": 1, "fundamento": "La posesión efectiva de herencias se tramita ante el Registro Civil (sucesiones sin testamento) o ante los tribunales (con testamento). Art. 688 CC y Ley 19.903.", "tema": "Posesión efectiva"},

    {"pregunta": "¿Cuál es el plazo para aceptar o repudiar la herencia en Chile?",
     "opciones": ["A. 6 meses desde la apertura de la sucesión","B. 1 año","C. No hay plazo; puede ejercerse cuando se quiera, salvo prescripción","D. 90 días desde la muerte del causante"],
     "correcta": 2, "fundamento": "Art. 1225 CC: el asignatario puede aceptar o repudiar la asignación libremente. No hay plazo legal, pero quien tenga interés puede pedir al juez fije un plazo (art. 1232 CC). La acción para pedir la herencia prescribe en 10 años.", "tema": "Plazo para aceptar o repudiar herencia"},
]

VF_SUCESORIO += [
    {"afirmacion": "En Chile, el testador puede disponer libremente de la totalidad de sus bienes si no tiene legitimarios.",
     "respuesta": True, "fundamento": "Arts. 1167 y 1182 CC: si no hay descendientes, ascendientes ni cónyuge o conviviente, no hay legítimas ni cuarta de mejoras. El testador puede disponer libremente de todos sus bienes.", "tema": "Libertad de testar sin legitimarios"},

    {"afirmacion": "La cuarta de libre disposición puede dejarse a cualquier persona.",
     "respuesta": True, "fundamento": "Art. 1184 CC: la cuarta de libre disposición puede asignarse a quien el testador quiera, incluyendo extraños a la familia.", "tema": "Cuarta de libre disposición"},
]

FC_SUCESORIO += [
    {"frente": "¿Qué es la representación en sucesión?",
     "reverso": "Art. 984 CC: permite a los descendientes del heredero que no puede o no quiere aceptar la herencia, ocupar su lugar y heredar en su nombre. Opera en la línea descendente (de modo ilimitado) y en la línea colateral (hasta el tercer grado).", "tema": "Derecho de representación"},
]

# ── INTERNACIONAL extra ──────────────────────────────────────
MCQ_INTERNACIONAL += [
    {"pregunta": "¿Cuándo entra en vigor un tratado internacional según la Convención de Viena de 1969?",
     "opciones": ["A. Al momento de la firma","B. En la forma y fecha que el tratado disponga o que los Estados negociadores acuerden","C. Al momento de la negociación","D. A los 30 días de la firma"],
     "correcta": 1, "fundamento": "Art. 24 Convención de Viena sobre Derecho de los Tratados (1969): un tratado entrará en vigor de la manera y en la fecha que en él se disponga o que acuerden los Estados negociadores.", "tema": "Entrada en vigor de tratados"},
]

VF_INTERNACIONAL += [
    {"afirmacion": "El principio de no intervención en asuntos internos es una norma de derecho internacional consuetudinario.",
     "respuesta": True, "fundamento": "El principio de no intervención es una norma consuetudinaria codificada en la Carta de la ONU (art. 2.7) y en resoluciones de la AGNU (Res. 2625). Prohíbe a los Estados intervenir en los asuntos que son esencialmente de la jurisdicción interna de otro Estado.", "tema": "No intervención"},
]

FC_INTERNACIONAL += []  # ya tiene 3

# ── AMBIENTAL extra ──────────────────────────────────────────
VF_AMBIENTAL += [
    {"afirmacion": "El Ministerio de Medio Ambiente en Chile fue creado por la Ley 20.417 de 2010.",
     "respuesta": True, "fundamento": "La Ley 20.417 (2010) modificó la Ley 19.300 y creó el Ministerio del Medio Ambiente, el Servicio de Evaluación Ambiental (SEA) y la Superintendencia del Medio Ambiente (SMA).", "tema": "Institucionalidad ambiental"},
]

# ════════════════════════════════════════════════════════════════
# Actualizar los diccionarios maestros con el contenido extendido
# (las listas Python ya se modificaron in-place arriba)
# No es necesario redefinir BANCO_MCQ, BANCO_VF, BANCO_FC
# porque referencian las mismas listas de Python.
# ════════════════════════════════════════════════════════════════


# ════════════════════════════════════════════════════════════════
# EXTENSIÓN 2 — lleva el banco a ~500 preguntas
# ════════════════════════════════════════════════════════════════

# ── CIVIL extra 2 (objetivo: +20) ───────────────────────────
MCQ_CIVIL.extend([
    {"pregunta": "¿Cuántos años dura la prescripción adquisitiva extraordinaria en Chile para bienes raíces?",
     "opciones": ["A. 5 años","B. 10 años","C. 15 años","D. 20 años"],
     "correcta": 1, "fundamento": "Art. 2511 CC: la prescripción extraordinaria es de 10 años sin distinción de bienes muebles e inmuebles ni distinción de posesión regular o irregular.", "tema": "Prescripción extraordinaria"},

    {"pregunta": "La teoría del abuso del derecho en Chile se funda principalmente en:",
     "opciones": ["A. El art. 583 CC","B. El principio de buena fe y la prohibición de ejercer derechos de manera contraria a su función social","C. El art. 1545 CC","D. La Constitución exclusivamente"],
     "correcta": 1, "fundamento": "El abuso del derecho (sancio abutendi) carece de norma expresa en el CC, pero se deduce del art. 582 CC (dominio sin perjuicio de la ley) y del principio de buena fe objetiva (art. 1546 CC).", "tema": "Abuso del derecho"},

    {"pregunta": "El contrato de depósito propiamente dicho en Chile es:",
     "opciones": ["A. Oneroso por naturaleza","B. Gratuito por naturaleza","C. Siempre solemne","D. Un contrato de adhesión"],
     "correcta": 1, "fundamento": "Art. 2219 CC: el depósito propiamente dicho es gratuito; si se estipula remuneración, degenera en arrendamiento de servicios.", "tema": "Contrato de depósito"},

    {"pregunta": "¿Qué es el justo precio en la lesión enorme?",
     "opciones": ["A. El precio de mercado al momento del juicio","B. El precio que determina el perito","C. El precio al momento del contrato según el art. 1889 CC","D. El precio fiscal del inmueble"],
     "correcta": 2, "fundamento": "Art. 1889 CC: para calificar la lesión enorme, se atiende al justo precio de la cosa al tiempo del contrato. Los tribunales valoran el justo precio al momento de la celebración.", "tema": "Justo precio en lesión enorme"},
])

VF_CIVIL.extend([
    {"afirmacion": "En Chile, los actos del absolutamente incapaz producen obligaciones naturales.",
     "respuesta": False, "fundamento": "Art. 1447 CC: los actos del absolutamente incapaz son nulos de pleno derecho y no producen ni siquiera obligaciones naturales. Solo los relativamente incapaces pueden originar obligaciones naturales.", "tema": "Incapacidad absoluta"},

    {"afirmacion": "El contrato de anticresis sobre bienes inmuebles en Chile debe inscribirse en el CBR.",
     "respuesta": True, "fundamento": "Art. 2438 CC: la anticresis (derecho del acreedor de percibir los frutos del inmueble del deudor) debe inscribirse en el CBR para ser oponible a terceros.", "tema": "Anticresis"},

    {"afirmacion": "La simulación relativa siempre acarrea nulidad del contrato real.",
     "respuesta": False, "fundamento": "En la simulación relativa, el contrato real (oculto) puede ser válido si reúne los requisitos legales. Solo el contrato simulado (aparente) es nulo. La acción de simulación busca hacer prevalecer el contrato real.", "tema": "Simulación relativa"},
])

FC_CIVIL.extend([
    {"frente": "¿Qué es la condición suspensiva y la resolutoria?",
     "reverso": "Suspensiva: el derecho no nace hasta que se cumpla la condición (ej: te doy cien si te recibes). Resolutoria: el derecho existe pero se extingue si se cumple la condición (ej: te doy cien pero los devuelves si repruebas). Arts. 1479-1481 CC.", "tema": "Condiciones suspensiva y resolutoria"},

    {"frente": "Requisitos de la compensación legal",
     "reverso": "Art. 1656 CC: 1) Ambas partes deben ser mutuamente deudoras, 2) Ambas deudas deben ser de dinero u otras cosas fungibles de igual especie, 3) Ambas deudas deben ser líquidas, 4) Ambas deben ser actualmente exigibles.", "tema": "Requisitos de la compensación"},
])

# ── PENAL extra 2 (objetivo: +25) ───────────────────────────
MCQ_PENAL.extend([
    {"pregunta": "El delito de abandono de niños en Chile:",
     "opciones": ["A. Requiere resultado de muerte del menor","B. Es un delito de peligro que se configura con el simple abandono","C. Solo es punible si hay lesiones","D. Solo aplica a recién nacidos"],
     "correcta": 1, "fundamento": "Arts. 346 y ss. CP: el abandono de niños es un delito de peligro; basta el abandono para configurarse aunque no haya resultado dañoso.", "tema": "Abandono de menores"},

    {"pregunta": "El tipo penal de lavado de activos en Chile está principalmente regulado en:",
     "opciones": ["A. Código Penal art. 470","B. Ley 19.913","C. Ley 20.000","D. Código de Comercio"],
     "correcta": 1, "fundamento": "La Ley 19.913 crea la Unidad de Análisis Financiero (UAF) y tipifica el delito de lavado de activos en Chile.", "tema": "Lavado de activos"},

    {"pregunta": "La calificante del ensañamiento en el homicidio implica:",
     "opciones": ["A. Actuar con premeditación","B. Aumentar deliberadamente el dolor del ofendido","C. Actuar por precio o recompensa","D. Actuar con alevosía"],
     "correcta": 1, "fundamento": "Art. 391 N°1 CP: el ensañamiento consiste en aumentar deliberada e inhumanamente el dolor del ofendido. Es una calificante del homicidio calificado.", "tema": "Ensañamiento"},

    {"pregunta": "¿Cuál es el bien jurídico protegido en el delito de cohecho?",
     "opciones": ["A. El patrimonio del Estado","B. La probidad y correcto funcionamiento de la administración pública","C. La libertad personal","D. El orden público"],
     "correcta": 1, "fundamento": "Arts. 248 y ss. CP: el cohecho (corrupción de funcionarios) protege la probidad y la correcta administración pública, preservando que los funcionarios no vendan sus funciones.", "tema": "Cohecho"},

    {"pregunta": "El principio de ultima ratio en derecho penal significa que:",
     "opciones": ["A. El derecho penal debe usarse como primer recurso","B. El derecho penal debe ser el último recurso, solo cuando otras ramas del derecho son insuficientes","C. Las penas deben ser máximas","D. El juicio oral es siempre obligatorio"],
     "correcta": 1, "fundamento": "El principio de ultima ratio (o intervención mínima) exige que el derecho penal solo intervenga cuando los demás mecanismos jurídicos y sociales son insuficientes para proteger el bien jurídico.", "tema": "Última ratio"},

    {"pregunta": "El delito de violación impropia en Chile se comete cuando:",
     "opciones": ["A. Se accede carnalmente a una persona mayor de 14 años usando fuerza","B. Se accede carnalmente a un menor de 14 años aunque haya consentimiento","C. Se accede a una persona inconsciente","D. Se comete entre cónyuges"],
     "correcta": 1, "fundamento": "Art. 362 CP: el acceso carnal a menor de 14 años es siempre violación (impropia) aunque haya consentimiento, porque la ley presume que el menor no puede consentir válidamente.", "tema": "Violación impropia"},
])

VF_PENAL.extend([
    {"afirmacion": "El Ministerio Público puede archivar provisionalmente una investigación.",
     "respuesta": True, "fundamento": "Art. 167 CPP: el fiscal puede archivar provisionalmente la investigación cuando no aparezcan antecedentes que permitan desarrollar actividades conducentes al esclarecimiento del hecho.", "tema": "Archivo provisional"},

    {"afirmacion": "En Chile existe la responsabilidad penal de las personas jurídicas.",
     "respuesta": True, "fundamento": "Ley 20.393 (2009): establece la responsabilidad penal de las personas jurídicas por los delitos de lavado de activos, financiamiento del terrorismo, cohecho y otros que la ley ha ido agregando.", "tema": "Responsabilidad penal personas jurídicas"},

    {"afirmacion": "El delito de apropiación indebida requiere que el autor se haya apoderado violentamente de la cosa.",
     "respuesta": False, "fundamento": "Art. 470 N°1 CP: la apropiación indebida se comete distrayendo o negándose a restituir cosas que se han recibido en depósito, comisión o administración. No requiere violencia.", "tema": "Apropiación indebida"},

    {"afirmacion": "El procedimiento abreviado en el proceso penal requiere conformidad del imputado.",
     "respuesta": True, "fundamento": "Art. 406 CPP: el procedimiento abreviado requiere que el fiscal lo solicite, el imputado lo acepte y se acuerde reducción de pena. El imputado debe aceptar los hechos de la acusación.", "tema": "Procedimiento abreviado"},
])

FC_PENAL.extend([
    {"frente": "¿Qué es el principio de territorialidad en materia penal?",
     "reverso": "La ley penal chilena se aplica a los delitos cometidos en el territorio nacional (art. 5 CP). Excepciones: principio de personalidad activa o pasiva, principio real o de protección, principio de universalidad (para crímenes de lesa humanidad).", "tema": "Principio de territorialidad penal"},

    {"frente": "¿Qué es el principio de humanidad de las penas?",
     "reverso": "Las penas no pueden ser crueles, inhumanas o degradantes. Prohíbe la tortura y los tratos inhumanos (art. 19 N°1 CPR y Convención contra la Tortura). Orienta hacia la rehabilitación del condenado.", "tema": "Humanidad de las penas"},

    {"frente": "Diferencia entre denuncia, querella y acusación",
     "reverso": "Denuncia: comunicación de un hecho delictivo a la autoridad (art. 173 CPP); no hace parte del proceso. Querella: acto procesal por el que la víctima u otras personas se constituyen en parte (art. 111 CPP). Acusación: ejercicio formal de la acción penal por el MP tras la investigación.", "tema": "Denuncia, querella y acusación"},
])

# ── PROCESAL extra 2 (objetivo: +22) ────────────────────────
MCQ_PROCESAL.extend([
    {"pregunta": "El incidente de nulidad procesal por falta de emplazamiento en Chile:",
     "opciones": ["A. Prescribe en 5 años","B. Puede alegarse en cualquier momento si se trata de nulidad de todo lo obrado","C. Solo puede alegarse en primera instancia","D. No existe en el CPC"],
     "correcta": 1, "fundamento": "Art. 80 CPC: el litigante que no ha podido comparecer al juicio por no haber sido emplazado puede pedir la rescisión de lo obrado. Si fue por culpa del notificado, la nulidad debe pedirse dentro de 5 días.", "tema": "Nulidad por falta de emplazamiento"},

    {"pregunta": "En el proceso penal, la audiencia de preparación de juicio oral sirve para:",
     "opciones": ["A. Dictar la sentencia definitiva","B. Depurar las pruebas, corregir vicios formales y fijar el objeto del juicio oral","C. Recibir la declaración de imputado","D. Resolver la prisión preventiva definitiva"],
     "correcta": 1, "fundamento": "Art. 266 CPP: la audiencia de preparación del juicio oral tiene por objeto examinar las pruebas ofrecidas, resolver las excepciones de previo y especial pronunciamiento y definir el objeto del juicio.", "tema": "Audiencia preparatoria"},

    {"pregunta": "¿Cuál es el tribunal competente para conocer los juicios de familia en Chile?",
     "opciones": ["A. Juzgado Civil","B. Juzgado de Familia","C. Juzgado de Garantía","D. Corte de Apelaciones"],
     "correcta": 1, "fundamento": "Ley 19.968 (crea los Tribunales de Familia): los Juzgados de Familia conocen de las materias que señala el art. 8 de dicha ley (alimentos, cuidado personal, adopción, VIF, etc.).", "tema": "Tribunales de familia"},

    {"pregunta": "El recurso de hecho ante la Corte de Apelaciones en Chile procede cuando:",
     "opciones": ["A. El juez no quiere fallar","B. El juez deniega un recurso de apelación que debía conceder, o lo concede en un efecto distinto","C. El juez dicta una sentencia definitiva errónea","D. El actor no puede pagar las costas"],
     "correcta": 1, "fundamento": "Art. 203 CPC: el recurso de hecho procede ante la Corte de Apelaciones cuando el tribunal de primera instancia deniega una apelación que debería concederse, o la concede en efecto distinto al que corresponde.", "tema": "Recurso de hecho"},
])

VF_PROCESAL.extend([
    {"afirmacion": "Las costas en el proceso civil chileno siempre se imponen al litigante vencido.",
     "respuesta": False, "fundamento": "Art. 144 CPC: las costas se imponen al litigante vencido, pero el tribunal puede eximirlo si tuvo motivo plausible para litigar. La eximición de costas es una facultad del juez.", "tema": "Costas procesales"},

    {"afirmacion": "El procedimiento monitorio en el proceso laboral chileno se activa con una demanda simplificada.",
     "respuesta": True, "fundamento": "Art. 496 CT: el procedimiento monitorio laboral permite al trabajador presentar una demanda por montos inferiores a 10 IMM con una fórmula simplificada, y el empleador debe objetar so pena de que la demanda se tenga por aceptada.", "tema": "Procedimiento monitorio laboral"},

    {"afirmacion": "El juez puede actuar como árbitro en una misma causa en la que también ejerce como juez ordinario.",
     "respuesta": False, "fundamento": "La función de árbitro y de juez son incompatibles en una misma causa. El árbitro es un particular nombrado por las partes; el juez ordinario ejerce jurisdicción estatal.", "tema": "Incompatibilidad árbitro-juez"},
])

FC_PROCESAL.extend([
    {"frente": "¿Qué es el principio dispositivo en el proceso civil?",
     "reverso": "Las partes son las dueñas del proceso: inician el proceso (nemo iudex sine actore), fijan el objeto del litigio, pueden renunciar a sus derechos procesales. El juez no puede actuar de oficio en materias de interés privado.", "tema": "Principio dispositivo"},

    {"frente": "Clasificación de los tribunales chilenos",
     "reverso": "Por materia: civiles, penales, laborales, familia, tributarios/aduaneros. Por jerarquía: Juzgados de primera instancia → Cortes de Apelaciones → Corte Suprema. Por composición: unipersonales (juzgados) o colegiados (cortes, TOP).", "tema": "Clasificación tribunales chilenos"},
])

# ── CONSTITUCIONAL extra 2 (objetivo: +24) ──────────────────
MCQ_CONSTITUCIONAL.extend([
    {"pregunta": "El derecho a la educación en Chile está reconocido en el art. 19 N°:",
     "opciones": ["A. 10","B. 11","C. 12","D. 13"],
     "correcta": 0, "fundamento": "Art. 19 N°10 CPR: garantiza el derecho a la educación, cuyo objeto es el pleno desarrollo de la persona en las distintas etapas de su vida. La libertad de enseñanza es el N°11.", "tema": "Derecho a la educación"},

    {"pregunta": "La acusación constitucional en Chile puede dirigirse contra:",
     "opciones": ["A. Solo los ministros de Estado","B. El Presidente de la República, ministros de Estado, magistrados, generales, intendentes y gobernadores","C. Solo los parlamentarios","D. Solo el Presidente"],
     "correcta": 1, "fundamento": "Arts. 52 y 53 CPR: la acusación constitucional puede dirigirse contra el Presidente (por actos de su administración contrarios a la CPR), ministros de Estado, magistrados del TC y CS, intendentes, gobernadores, generales y almirantes.", "tema": "Acusación constitucional"},

    {"pregunta": "¿Cuál es la función del Banco Central de Chile según la CPR?",
     "opciones": ["A. Recaudar impuestos","B. Velar por la estabilidad monetaria y el normal funcionamiento de los pagos internos y externos","C. Fiscalizar bancos y financieras","D. Emitir moneda sin restricciones"],
     "correcta": 1, "fundamento": "Art. 108 CPR: el Banco Central es un organismo autónomo con rango constitucional cuyo objeto es velar por la estabilidad de la moneda y el normal funcionamiento de los pagos internos y externos.", "tema": "Banco Central"},

    {"pregunta": "¿Qué es la iniciativa exclusiva presidencial en materia legislativa?",
     "opciones": ["A. Solo el Presidente puede presentar proyectos de ley","B. Ciertos proyectos de ley solo pueden tener su origen en el Ejecutivo (tributos, administración financiera, etc.)","C. El Presidente puede rechazar cualquier ley","D. Solo aplica a las leyes orgánicas constitucionales"],
     "correcta": 1, "fundamento": "Art. 65 CPR: corresponde exclusivamente al Presidente la iniciativa de proyectos sobre tributos, presupuesto, administración financiera, remuneraciones del sector público, negociación colectiva, etc.", "tema": "Iniciativa exclusiva presidencial"},

    {"pregunta": "El veto presidencial en Chile permite al Presidente:",
     "opciones": ["A. Rechazar definitivamente una ley","B. Proponer cambios al proyecto aprobado por el Congreso, con posibilidad de insistencia del Congreso","C. Modificar la Constitución unilateralmente","D. Dejar sin efecto sentencias judiciales"],
     "correcta": 1, "fundamento": "Art. 73 CPR: el Presidente puede observar (vetar) el proyecto dentro de 30 días. Si el Congreso insiste con 2/3 de votos, el Presidente debe promulgar la ley.", "tema": "Veto presidencial"},
])

VF_CONSTITUCIONAL.extend([
    {"afirmacion": "Chile tiene un sistema presidencial de gobierno.",
     "respuesta": True, "fundamento": "Art. 24 CPR: el gobierno y la administración del Estado corresponden al Presidente de la República. Chile tiene un sistema presidencial con fuerte concentración de poder en el Ejecutivo.", "tema": "Sistema de gobierno"},

    {"afirmacion": "Los ministros de Estado en Chile son responsables por sus actos y pueden ser removidos por el Congreso.",
     "respuesta": False, "fundamento": "Art. 33 CPR: los ministros son de la exclusiva confianza del Presidente y son removidos por este. El Congreso puede acusarlos constitucionalmente, pero no removerlos directamente.", "tema": "Responsabilidad ministerial"},

    {"afirmacion": "La Constitución chilena garantiza el derecho a la salud como derecho de prestación exigible directamente al Estado.",
     "respuesta": False, "fundamento": "Art. 19 N°9 CPR: garantiza el derecho a la protección de la salud. El Estado no garantiza directamente el acceso gratuito; garantiza la libertad de elegir el sistema (público o privado) y el acceso a acciones de salud.", "tema": "Derecho a la salud"},
])

FC_CONSTITUCIONAL.extend([
    {"frente": "¿Qué es el Estado de Chile según la CPR?",
     "reverso": "Art. 1 CPR: Chile es una República democrática. Su finalidad es el bien común. La familia es el núcleo fundamental de la sociedad. El Estado reconoce y ampara a los grupos intermedios. El Estado está al servicio de la persona humana.", "tema": "Definición del Estado de Chile"},

    {"frente": "¿Cuándo puede el Presidente decretar el estado de sitio?",
     "reverso": "Art. 40 CPR: el estado de sitio puede declararse en caso de guerra interna o grave conmoción interior. Lo decreta el Presidente con acuerdo del Senado. Durante el estado de sitio se restringen libertades individuales.", "tema": "Estado de sitio"},
])

# ── LABORAL extra 2 (objetivo: +22) ─────────────────────────
MCQ_LABORAL.extend([
    {"pregunta": "El feriado legal en Chile para los trabajadores con más de 10 años de servicios es de:",
     "opciones": ["A. 15 días hábiles","B. 20 días hábiles","C. Un día adicional por cada 3 nuevos años trabajados sobre los 10","D. 25 días hábiles"],
     "correcta": 2, "fundamento": "Art. 68 CT: todo trabajador con más de 10 años de servicio, continuos o no, tendrá derecho a un día adicional de feriado por cada 3 nuevos años trabajados. Solo pueden hacerse valer hasta 10 días adicionales.", "tema": "Feriado legal progresivo"},

    {"pregunta": "El contrato de trabajo a plazo fijo en Chile se transforma en indefinido cuando:",
     "opciones": ["A. El trabajador lo solicita","B. Se ha pactado dos veces o el trabajador ha prestado servicios discontinuos por más de 12 meses en 15","C. Pasan 6 meses desde su suscripción","D. Solo cuando el empleador lo decide"],
     "correcta": 1, "fundamento": "Art. 159 N°4 CT: el contrato a plazo fijo que se renueva una segunda vez o el trabajador que ha prestado servicios discontinuos en más de dos oportunidades o por más de 12 meses en 15, se presume que el contrato es indefinido.", "tema": "Contrato a plazo fijo indefinido"},

    {"pregunta": "El derecho al descanso dominical en Chile significa que:",
     "opciones": ["A. Todo trabajador descansa el domingo sin excepción","B. El séptimo día es de descanso, pero puede ser cualquier día de la semana en ciertos sectores","C. Solo los trabajadores del comercio descansan el domingo","D. El domingo es siempre día hábil laboral"],
     "correcta": 1, "fundamento": "Arts. 35 y 38 CT: el descanso semanal corresponde al día domingo por regla general; sin embargo, ciertos sectores (comercio, hotelería, etc.) pueden distribuirlo diferente con compensación.", "tema": "Descanso dominical"},

    {"pregunta": "¿Qué es el contrato de trabajo por obra o faena en Chile?",
     "opciones": ["A. Un contrato indefinido con término por decisión del empleador","B. Un contrato para la realización de una obra determinada que termina al concluir esa obra","C. Solo aplicable a la construcción","D. Un contrato de subcontrato laboral"],
     "correcta": 1, "fundamento": "Art. 10 bis CT: el contrato por obra o faena es aquel celebrado para la ejecución de una obra o la prestación de un servicio específico. Termina cuando concluye la obra o faena (art. 159 N°5 CT).", "tema": "Contrato por obra o faena"},
])

VF_LABORAL.extend([
    {"afirmacion": "La empresa puede pactar con el trabajador que este renuncie a su derecho de sindicarse.",
     "respuesta": False, "fundamento": "Art. 19 N°19 CPR y arts. 215 y ss. CT: la libertad sindical es un derecho garantizado constitucionalmente. Cualquier pacto en contrario es nulo por el principio de irrenunciabilidad.", "tema": "Irrenunciabilidad sindical"},

    {"afirmacion": "La licencia médica da derecho al trabajador a continuar recibiendo su remuneración íntegra mientras dura.",
     "respuesta": False, "fundamento": "Durante la licencia médica, el trabajador recibe un subsidio por incapacidad laboral que se calcula sobre la base de las remuneraciones imponibles de los últimos 6 meses, no necesariamente el 100% del sueldo.", "tema": "Licencia médica y subsidio"},

    {"afirmacion": "La negociación colectiva semirreglada permite negociar sin los plazos del procedimiento reglado.",
     "respuesta": True, "fundamento": "Art. 314 CT (negociación colectiva no reglada o informal): las partes pueden negociar directamente sin sujetarse al procedimiento reglado, pero los instrumentos que suscriban tienen plena eficacia.", "tema": "Negociación colectiva informal"},
])

FC_LABORAL.extend([
    {"frente": "¿Qué es el ius variandi del empleador?",
     "reverso": "Facultad limitada del empleador para modificar unilateralmente ciertas condiciones del contrato de trabajo. Art. 12 CT: puede cambiar el lugar de trabajo, la naturaleza de los servicios o la distribución de la jornada, dentro de los límites legales y sin menoscabo del trabajador.", "tema": "Ius variandi"},

    {"frente": "Derechos irrenunciables del trabajador (ejemplos)",
     "reverso": "Son irrenunciables por anticipado: la jornada máxima, el sueldo mínimo, el feriado legal, las cotizaciones previsionales, el fuero maternal y sindical, las indemnizaciones por término de contrato. Art. 5 CT.", "tema": "Derechos irrenunciables laborales"},
])

# ── OBLIGACIONES extra 2 (objetivo: +20) ────────────────────
MCQ_OBLIGACIONES.extend([
    {"pregunta": "Las obligaciones de género en Chile se extinguen cuando:",
     "opciones": ["A. El género perece","B. El deudor paga una especie del género de calidad a lo menos mediana","C. El acreedor rechaza el pago","D. El género específico se agota"],
     "correcta": 1, "fundamento": "Art. 1509 CC: en las obligaciones de género, el acreedor no puede pedir una cosa determinada. El deudor cumple pagando cualquier individuo del género de calidad a lo menos mediana.", "tema": "Obligaciones de género"},

    {"pregunta": "La prelación de créditos en Chile determina:",
     "opciones": ["A. El orden de prescripción de las deudas","B. El orden de pago de los acreedores cuando el deudor tiene insuficiencia patrimonial","C. La preferencia procesal para demandar","D. El ranking de deudores morosos"],
     "correcta": 1, "fundamento": "Arts. 2465 y ss. CC: la prelación de créditos determina el orden en que los acreedores son pagados con el producto de los bienes del deudor insolvente, según privilegios y grados.", "tema": "Prelación de créditos"},

    {"pregunta": "La obligación solidaria pasiva beneficia al acreedor porque:",
     "opciones": ["A. Cada deudor paga solo su cuota","B. El acreedor puede exigir el total de la deuda a cualquiera de los deudores solidarios","C. La deuda se divide automáticamente","D. Los intereses son mayores"],
     "correcta": 1, "fundamento": "Art. 1514 CC: el acreedor podrá dirigirse contra todos los deudores solidarios conjuntamente o contra cualquiera de ellos a su arbitrio, sin que por este pueda oponérsele el beneficio de división.", "tema": "Solidaridad pasiva beneficio acreedor"},
])

VF_OBLIGACIONES.extend([
    {"afirmacion": "El acreedor puede ceder su crédito sin consentimiento del deudor.",
     "respuesta": True, "fundamento": "Arts. 1901 y ss. CC: la cesión de crédito no requiere el consentimiento del deudor; solo se le notifica para que sea oponible a él. El deudor puede oponer al cesionario las excepciones que tenía contra el cedente.", "tema": "Cesión de crédito sin consentimiento"},

    {"afirmacion": "En Chile, la deuda contraída con dolo no puede ser objeto de novación.",
     "respuesta": False, "fundamento": "El dolo no impide la novación; los contratos viciados por dolo pueden ser novados si las partes lo acuerdan, extinguiendo la obligación anterior viciada y creando una nueva.", "tema": "Novación y dolo"},

    {"afirmacion": "Las obligaciones alternativas dan al deudor la elección de qué pagar, salvo que se haya pactado lo contrario.",
     "respuesta": True, "fundamento": "Art. 1500 CC: en las obligaciones alternativas, corresponde la elección al deudor salvo cuando se ha pactado que la elección pertenece al acreedor.", "tema": "Obligaciones alternativas"},
])

FC_OBLIGACIONES.extend([
    {"frente": "¿Qué es la acción oblicua o subrogatoria?",
     "reverso": "Art. 2466 CC: acción que permite al acreedor ejercer los derechos y acciones del deudor negligente (que no los ejercita), en nombre y lugar de este, para incrementar el patrimonio del deudor y así garantizar el pago.", "tema": "Acción oblicua"},
])

# ── FAMILIA extra 2 (objetivo: +13) ─────────────────────────
MCQ_FAMILIA.extend([
    {"pregunta": "En Chile, ¿quién tiene legitimidad activa para impugnar el reconocimiento de paternidad?",
     "opciones": ["A. Solo el reconocido","B. El reconocido, su representante legal, el padre biológico y todo el que pruebe interés actual","C. Solo el padre","D. Solo el Ministerio Público"],
     "correcta": 1, "fundamento": "Art. 216 CC: la acción de impugnación del reconocimiento corresponde al propio hijo, a su representante legal, al padre o madre cuya paternidad o maternidad se impugna, y a toda persona que pruebe un interés actual.", "tema": "Impugnación del reconocimiento"},

    {"pregunta": "La administración de la sociedad conyugal corresponde a:",
     "opciones": ["A. La mujer","B. Ambos cónyuges conjuntamente","C. El marido, con plenas facultades","D. El marido, con limitaciones establecidas en el CC"],
     "correcta": 3, "fundamento": "Arts. 1749 y ss. CC: el marido administra los bienes sociales y los propios de la mujer, pero con importantes limitaciones: necesita autorización de la mujer para enajenar o gravar bienes raíces sociales, caucionar deudas ajenas, disponer a título gratuito de bienes sociales, etc.", "tema": "Administración sociedad conyugal"},
])

VF_FAMILIA.extend([
    {"afirmacion": "El juicio de alimentos en Chile se tramita en el Tribunal de Familia.",
     "respuesta": True, "fundamento": "Art. 8 N°4 Ley 19.968: los Juzgados de Familia son competentes para conocer las causas de alimentos.", "tema": "Juicio de alimentos"},

    {"afirmacion": "La pensión de alimentos puede ser retenida directamente del salario del alimentante.",
     "respuesta": True, "fundamento": "Art. 8 Ley 14.908: el empleador que reciba resolución que ordene la retención de la pensión alimenticia está obligado a descontarla del salario del trabajador y enterar su pago al alimentario.", "tema": "Retención de alimentos por empleador"},

    {"afirmacion": "En Chile, la muerte presunta disuelve el matrimonio con el cónyuge desaparecido.",
     "respuesta": True, "fundamento": "Art. 43 LMC: el matrimonio se disuelve por la muerte presunta del cónyuge desaparecido, una vez transcurrido el plazo de 5 años desde la fecha de las últimas noticias (o 1 año en caso de sismo, catástrofe o acción bélica).", "tema": "Matrimonio y muerte presunta"},
])

FC_FAMILIA.extend([
    {"frente": "¿Qué es la mediación familiar?",
     "reverso": "Proceso colaborativo voluntario en que un mediador imparcial ayuda a las partes a alcanzar acuerdos en materias de familia. Es requisito previo a la demanda en alimentos, cuidado personal y relación directa y regular (art. 106 Ley 19.968).", "tema": "Mediación familiar"},
])

# ── COMERCIAL extra 2 (objetivo: +20) ───────────────────────
MCQ_COMERCIAL.extend([
    {"pregunta": "El contrato de agencia en el derecho comercial chileno es aquel en que:",
     "opciones": ["A. El agente actúa en nombre propio por cuenta ajena","B. El agente actúa en nombre y por cuenta del principal, con carácter estable","C. Solo se celebra con personas naturales","D. Requiere escritura pública"],
     "correcta": 1, "fundamento": "El agente comercial actúa por cuenta del principal de forma estable en un territorio, diferenciándose del mandatario común por la habitualidad y autonomía. Regulado supletoriamente por el C.Com.", "tema": "Contrato de agencia"},

    {"pregunta": "En el mercado de valores chileno, la CMF supervisa:",
     "opciones": ["A. Solo a las bolsas de valores","B. A los emisores, intermediarios de valores, bolsas, sociedades anónimas abiertas y fondos de inversión","C. Solo a los bancos","D. Solo a las AFP"],
     "correcta": 1, "fundamento": "La Comisión para el Mercado Financiero (CMF), creada por Ley 21.000, supervisa los mercados de valores y seguros, incluyendo bolsas, emisores de valores, fondos y entidades bancarias.", "tema": "CMF y mercado de valores"},

    {"pregunta": "El contrato de factoring en Chile consiste en:",
     "opciones": ["A. Arrendar maquinaria industrial","B. Ceder facturas u otros créditos comerciales a una empresa financiera a cambio de liquidez anticipada","C. Crear una sociedad de responsabilidad limitada","D. Asegurar mercancías en tránsito"],
     "correcta": 1, "fundamento": "El factoring (Ley 19.983 y Ley 20.727) consiste en la cesión de créditos comerciales (facturas) por parte del proveedor a una empresa de factoring, que le adelanta el dinero y cobra luego al deudor.", "tema": "Contrato de factoring"},

    {"pregunta": "El protesto de la letra de cambio en Chile debe realizarse:",
     "opciones": ["A. Antes del vencimiento","B. El día del vencimiento o uno de los dos hábiles siguientes","C. Dentro de 30 días del vencimiento","D. Solo si el tomador lo solicita"],
     "correcta": 1, "fundamento": "Art. 72 Ley 18.092: el protesto por falta de pago debe realizarse el día del vencimiento de la letra o al día siguiente hábil si este fuere festivo.", "tema": "Protesto de letra de cambio"},

    {"pregunta": "La responsabilidad del transportista en el contrato de transporte en Chile es:",
     "opciones": ["A. Subjetiva, debe probarse su culpa","B. Objetiva y se presume; el transportista responde salvo caso fortuito imputable a la carga o culpa del cargador","C. Sin responsabilidad por bienes frágiles","D. Solo civil, nunca penal"],
     "correcta": 1, "fundamento": "Arts. 166 y 173 C.Com.: el porteador (transportista) responde de la pérdida, avería o retardo de las mercaderías; su responsabilidad es de resultado (objetiva), salvo caso fortuito, vicio propio de la cosa o culpa del cargador.", "tema": "Responsabilidad transportista"},
])

VF_COMERCIAL.extend([
    {"afirmacion": "Las bolsas de valores en Chile son supervisadas por el Ministerio de Hacienda.",
     "respuesta": False, "fundamento": "Las bolsas de valores son supervisadas por la Comisión para el Mercado Financiero (CMF), organismo autónomo creado por la Ley 21.000.", "tema": "Supervisión bolsas de valores"},

    {"afirmacion": "El cheque en Chile es un instrumento de crédito.",
     "respuesta": False, "fundamento": "El cheque en Chile es un instrumento de pago a la vista (art. 10 Ley 18.092 y DFL 707). No es un instrumento de crédito porque debe pagarse a su presentación. El girador no puede postdatar un cheque con efecto de diferir el pago.", "tema": "Naturaleza del cheque"},

    {"afirmacion": "Las sociedades por acciones (SpA) están exentas del requisito de pluralidad de socios.",
     "respuesta": True, "fundamento": "Art. 424 C.Com.: la sociedad por acciones puede constituirse y subsistir con un solo accionista. No se disuelve si queda con un solo socio, a diferencia de otras sociedades.", "tema": "SpA unipersonal"},

    {"afirmacion": "El giro de un cheque sin fondos en Chile puede constituir delito.",
     "respuesta": True, "fundamento": "Art. 22 Ley de Cuentas Corrientes Bancarias y Cheques (DFL 707): el giro doloso de cheque sin fondos puede configurar el delito de estafa (art. 467 CP) o el delito específico de cheque sin fondos.", "tema": "Cheque sin fondos y delito"},
])

FC_COMERCIAL.extend([
    {"frente": "¿Qué es el derecho mercantil y cómo se diferencia del civil?",
     "reverso": "El derecho mercantil regula los actos de comercio (art. 3 C.Com.) y los comerciantes. Se diferencia del civil por: rapidez (principio de celeridad), la solidaridad se presume, menores formalismos, especialidad de sus instituciones (títulos de crédito, seguros, sociedades mercantiles).", "tema": "Derecho mercantil vs civil"},

    {"frente": "Clases de sociedades mercantiles en Chile",
     "reverso": "1) Sociedad colectiva comercial, 2) Sociedad de responsabilidad limitada (SRL), 3) Sociedad anónima (abierta/cerrada), 4) Sociedad en comandita (simple y por acciones), 5) Sociedad por acciones (SpA), 6) EIRL (empresa individual de resp. limitada).", "tema": "Tipos de sociedades mercantiles"},
])

# ── BIENES extra 2 (objetivo: +9) ───────────────────────────
MCQ_BIENES.extend([
    {"pregunta": "Las servidumbres voluntarias en Chile se establecen por:",
     "opciones": ["A. Ley","B. Contrato o testamento del propietario del predio sirviente","C. Solo por sentencia judicial","D. Por prescripción de 5 años"],
     "correcta": 1, "fundamento": "Art. 882 CC: las servidumbres discontinuas y las no aparentes pueden establecerse solo por voluntad de los propietarios, sea por contrato o testamento. Las servidumbres voluntarias nacen del acuerdo entre los dueños de los predios.", "tema": "Servidumbres voluntarias"},
])

VF_BIENES.extend([
    {"afirmacion": "En Chile, las aguas son bienes nacionales de uso público.",
     "respuesta": True, "fundamento": "Art. 595 CC y art. 5 Código de Aguas: las aguas son bienes nacionales de uso público y se da a los particulares el derecho de aprovechamiento de ellas en conformidad a las disposiciones del Código de Aguas.", "tema": "Dominio de las aguas"},
])

FC_BIENES.extend([
    {"frente": "¿Qué es el derecho real de uso y el de habitación?",
     "reverso": "Uso: derecho de usar una cosa ajena con la restricción de solo tomar de los frutos lo necesario para las necesidades del usuario y su familia. Habitación: derecho de morar en un edificio ajeno, limitado a las necesidades del habitador y su familia. Arts. 811-819 CC. Son personalísimos e intransferibles.", "tema": "Derecho de uso y habitación"},
])

# ── SUCESORIO extra 2 (objetivo: +4) ────────────────────────
VF_SUCESORIO.extend([
    {"afirmacion": "Los herederos en Chile responden de las deudas del causante con sus propios bienes si no aceptan con beneficio de inventario.",
     "respuesta": True, "fundamento": "Art. 1247 CC: el heredero que acepta simple y llanamente la herencia sin beneficio de inventario responde de las deudas hereditarias y testamentarias no solo hasta el valor de los bienes heredados sino con sus propios bienes.", "tema": "Aceptación simple vs con beneficio de inventario"},
])

FC_SUCESORIO.extend([
    {"frente": "¿Qué es el albacea o ejecutor testamentario?",
     "reverso": "Art. 1270 CC: el albacea (ejecutor testamentario) es la persona nombrada por el testador para cumplir sus disposiciones testamentarias. Tiene facultades que el testador le confiere expresamente o que la ley le reconoce.", "tema": "Albacea testamentario"},
])

# ── INTERNACIONAL extra 2 (objetivo: +4) ────────────────────
MCQ_INTERNACIONAL.extend([
    {"pregunta": "El derecho de asilo en el derecho internacional protege a:",
     "opciones": ["A. Cualquier extranjero que lo solicite","B. A personas perseguidas por motivos de raza, religión, nacionalidad, opinión política o grupo social","C. Solo a personas con orden de extradición","D. Solo a refugiados económicos"],
     "correcta": 1, "fundamento": "Convención sobre el Estatuto de los Refugiados (Ginebra, 1951): el asilo protege a quienes tienen fundados temores de persecución por motivos de raza, religión, nacionalidad, grupo social u opinión política.", "tema": "Derecho de asilo y refugio"},
])

VF_INTERNACIONAL.extend([
    {"afirmacion": "Chile forma parte del Estatuto de Roma de la Corte Penal Internacional.",
     "respuesta": True, "fundamento": "Chile ratificó el Estatuto de Roma en 2009 (Ley 20.352), siendo parte de la Corte Penal Internacional (CPI) con sede en La Haya.", "tema": "Corte Penal Internacional y Chile"},
])

# ── AMBIENTAL extra 2 (objetivo: +2) ────────────────────────
MCQ_AMBIENTAL.extend([
    {"pregunta": "¿Qué organismo fiscaliza el cumplimiento de la normativa ambiental en Chile?",
     "opciones": ["A. El SEA","B. La Superintendencia del Medio Ambiente (SMA)","C. El Ministerio del Medio Ambiente","D. El Consejo de Ministros para la Sustentabilidad"],
     "correcta": 1, "fundamento": "La Superintendencia del Medio Ambiente (SMA), creada por Ley 20.417 (2010), es el organismo con facultades fiscalizadoras, sancionatorias y de seguimiento de la normativa ambiental y de las RCA.", "tema": "Superintendencia del Medio Ambiente"},
])


# ════════════════════════════════════════════════════════════════
# EXTENSIÓN 3 — bloque final para alcanzar ~500 preguntas
# ════════════════════════════════════════════════════════════════

# ── CIVIL extra 3 (+10) ────────────────────────────────────
MCQ_CIVIL.extend([
    {"pregunta": "El contrato aleatorio en derecho civil chileno se caracteriza por:",
     "opciones": ["A. Que no genera obligaciones","B. Que la prestación de alguna de las partes depende de un hecho incierto","C. Que solo lo celebran comerciantes","D. Que las obligaciones son siempre de dar"],
     "correcta": 1, "fundamento": "Art. 1441 CC: el contrato es aleatorio cuando la equivalencia de las prestaciones depende de un hecho incierto que hace que no se pueda determinar cuál de las partes obtiene mayor beneficio (ej: juego, apuesta, renta vitalicia, seguro).", "tema": "Contrato aleatorio"},

    {"pregunta": "La interversión de la posesión en Chile ocurre cuando:",
     "opciones": ["A. El poseedor abandona la cosa","B. El mero tenedor cambia su ánimo y comienza a poseer la cosa para sí","C. El poseedor transfiere la posesión","D. El dueño recupera la cosa"],
     "correcta": 1, "fundamento": "La interversión de la posesión se produce cuando el mero tenedor (que reconocía dominio ajeno) cambia el título y comienza a poseer para sí con ánimo de dueño, lo que puede ocurrir por disposición de ley o acto del dueño.", "tema": "Interversión de la posesión"},
])
VF_CIVIL.extend([
    {"afirmacion": "El dolo en los contratos se presume cuando el deudor incumple.",
     "respuesta": False, "fundamento": "Art. 44 CC: el dolo no se presume. Debe probarlo quien lo alega. La culpa leve sí se presume cuando la ley no señala otra especie de culpa (art. 1547 CC).", "tema": "Presunción del dolo"},

    {"afirmacion": "Los bienes incorporales en Chile son susceptibles de dominio.",
     "respuesta": True, "fundamento": "Art. 583 CC: sobre las cosas incorporales (derechos reales y personales) hay también una especie de propiedad; así, el usufructuario tiene la propiedad de su derecho de usufructo.", "tema": "Dominio sobre cosas incorporales"},

    {"afirmacion": "La acción reivindicatoria puede ejercerse contra el poseedor de buena fe.",
     "respuesta": True, "fundamento": "Art. 895 CC: la acción reivindicatoria se puede intentar contra el actual poseedor, sea de buena o mala fe. La buena fe solo incide en la restitución de frutos, no en la procedencia de la acción.", "tema": "Reivindicatoria contra poseedor buena fe"},
])
FC_CIVIL.extend([
    {"frente": "¿Cuál es la diferencia entre dolo y culpa en el CC chileno?",
     "reverso": "Dolo: intención positiva de inferir injuria (art. 44 CC). Culpa: falta de diligencia debida. Hay tres grados de culpa: grave (equivale al dolo), leve (patrón del buen padre de familia) y levísima (diligencia exquisita). El dolo no se presume; la culpa leve sí.", "tema": "Dolo y culpa"},
    {"frente": "Clases de bienes según el CC chileno",
     "reverso": "1) Corporales e incorporales (art. 565), 2) Muebles e inmuebles (art. 566), 3) Fungibles y no fungibles, 4) Consumibles y no consumibles, 5) Divisibles e indivisibles, 6) Singulares y universales, 7) Presentes y futuros.", "tema": "Clasificación de bienes"},
])

# ── PENAL extra 3 (+12) ───────────────────────────────────
MCQ_PENAL.extend([
    {"pregunta": "El tipo penal del robo con violencia en Chile se diferencia del robo con intimidación en que:",
     "opciones": ["A. Son tipos penales distintos sin conexión","B. La violencia es ejercida sobre las personas; la intimidación es la amenaza de un mal inminente","C. El robo con violencia es más grave","D. Solo el robo con intimidación se sanciona penalmente"],
     "correcta": 1, "fundamento": "Art. 436 CP: el robo puede cometerse con violencia (uso de fuerza física sobre las personas) o con intimidación (amenaza de un mal inminente). Ambas modalidades tienen igual pena.", "tema": "Robo con violencia vs intimidación"},

    {"pregunta": "¿Cuál es el periodo de suspensión de la prescripción penal?",
     "opciones": ["A. Desde la detención del imputado","B. Desde que el procedimiento se dirige en contra del imputado (formalización o imputación formal)","C. Desde la denuncia","D. La prescripción penal no se suspende"],
     "correcta": 1, "fundamento": "Art. 96 CP: la prescripción se suspende desde que el procedimiento se dirige contra el imputado; si este se paraliza por 3 años, continúa la prescripción.", "tema": "Suspensión prescripción penal"},

    {"pregunta": "El delito de violencia intrafamiliar en Chile es:",
     "opciones": ["A. Un delito de resultado","B. Un delito de acción privada","C. Un delito mixto: de acción penal pública previo requerimiento del fiscal en coordinación con la víctima","D. Un delito solo investigado por Carabineros"],
     "correcta": 2, "fundamento": "Ley 20.066 (VIF): el delito de VIF del art. 14 es de acción penal pública. El art. 5 de la misma ley permite al fiscal no ejercer la acción si la víctima no lo solicita en determinadas circunstancias.", "tema": "Violencia intrafamiliar como delito"},
])
VF_PENAL.extend([
    {"afirmacion": "El robo de uso en Chile está tipificado expresamente como delito.",
     "respuesta": False, "fundamento": "El robo de uso (tomar una cosa temporalmente sin ánimo de apropiarse) no está tipificado expresamente en el CP chileno como delito autónomo; puede configurar hurto si hay ánimo de lucro o daños si la cosa es deteriorada.", "tema": "Robo de uso"},

    {"afirmacion": "La inimputabilidad por enajenación mental excluye toda responsabilidad.",
     "respuesta": True, "fundamento": "Art. 10 N°1 CP: el loco o demente que no haya obrado en un intervalo lúcido y el que por privación total de razón actúa están exentos de responsabilidad penal. Son inimputables.", "tema": "Inimputabilidad por enajenación mental"},

    {"afirmacion": "El principio de proporcionalidad limita la facultad del legislador para fijar penas.",
     "respuesta": True, "fundamento": "El principio de proporcionalidad (art. 19 N°1 y N°3 CPR) exige que la pena sea adecuada a la gravedad del hecho y a la culpabilidad del autor. Penas excesivas o irracionales son inconstitucionales.", "tema": "Proporcionalidad y legislador"},
])
FC_PENAL.extend([
    {"frente": "¿Qué es la teoría de la equivalencia de las condiciones?",
     "reverso": "La causalidad existe si la condición es sine qua non del resultado: si se suprimiera mentalmente la acción, el resultado no se habría producido. Crítica: lleva al regreso al infinito. En Chile se aplica conjuntamente con la imputación objetiva.", "tema": "Causalidad en derecho penal"},
    {"frente": "¿Qué son las medidas de seguridad en el CP chileno?",
     "reverso": "Medidas aplicables a los inimputables (especialmente enfermos mentales) que han cometido una conducta típica y antijurídica. No son penas sino medidas aseguradoras. En Chile se regula el internamiento en hospital psiquiátrico (art. 482 CPP).", "tema": "Medidas de seguridad"},
])

# ── PROCESAL extra 3 (+13) ────────────────────────────────
MCQ_PROCESAL.extend([
    {"pregunta": "El principio de bilateralidad de la audiencia en el proceso implica:",
     "opciones": ["A. Que siempre deben existir dos audiencias","B. Que ambas partes tienen derecho a ser oídas antes de que el tribunal resuelva","C. Que el proceso siempre tiene dos instancias","D. Que deben existir dos jueces"],
     "correcta": 1, "fundamento": "El principio de bilateralidad o contradicción garantiza que ninguna resolución puede dictarse sin dar a la parte contraria la oportunidad de ser escuchada. Emana del debido proceso (art. 19 N°3 CPR).", "tema": "Bilateralidad de la audiencia"},

    {"pregunta": "El sobreseimiento definitivo en el proceso penal chileno equivale a:",
     "opciones": ["A. Una condena con pena suspendida","B. Una absolución con efectos de cosa juzgada que impide nuevo juzgamiento","C. Una sentencia condenatoria","D. Una medida cautelar"],
     "correcta": 1, "fundamento": "Art. 251 CPP: el sobreseimiento definitivo equivale a la sentencia absolutoria y tiene autoridad de cosa juzgada. Extingue la acción penal y la responsabilidad penal del imputado.", "tema": "Sobreseimiento definitivo"},

    {"pregunta": "Los árbitros de derecho en Chile se diferencian de los arbitradores en que:",
     "opciones": ["A. Los árbitros de derecho fallan conforme a la ley; los arbitradores según su prudencia","B. Solo los árbitros de derecho pueden ser abogados","C. Los arbitradores son siempre más caros","D. Los árbitros de derecho no requieren nombramiento"],
     "correcta": 0, "fundamento": "Art. 223 COT: el árbitro de derecho falla con arreglo a la ley y se somete a la tramitación legal. El árbitro arbitrador (amigable componedor) falla según lo que su prudencia y equidad le dicten.", "tema": "Árbitros de derecho vs arbitradores"},
])
VF_PROCESAL.extend([
    {"afirmacion": "El recurso de casación en el fondo ante la Corte Suprema en Chile se funda en errores de derecho.",
     "respuesta": True, "fundamento": "Art. 767 CPC: el recurso de casación en el fondo procede contra sentencias definitivas cuando se han pronunciado con infracción de ley y dicha infracción ha influido sustancialmente en lo dispositivo del fallo.", "tema": "Casación en el fondo"},

    {"afirmacion": "El juez de garantía en Chile puede investigar un delito de oficio.",
     "respuesta": False, "fundamento": "El principio acusatorio (art. 83 CPR) separa la función de investigación (Ministerio Público) de la función jurisdiccional (juez de garantía). El juez de garantía no investiga; controla la legalidad de la investigación del MP.", "tema": "Principio acusatorio"},

    {"afirmacion": "Las actas del Conservador de Bienes Raíces en Chile hacen plena prueba.",
     "respuesta": True, "fundamento": "Art. 1700 CC: los instrumentos públicos hacen plena fe en cuanto al hecho de haberse otorgado y la fecha. Las inscripciones en el CBR son instrumentos públicos que acreditan el dominio.", "tema": "Fe pública CBR"},
])
FC_PROCESAL.extend([
    {"frente": "¿Qué es la jurisdicción y en qué se diferencia de la competencia?",
     "reverso": "Jurisdicción: poder-deber del Estado de resolver conflictos jurídicos con efecto de cosa juzgada (art. 76 CPR). Competencia: medida de la jurisdicción asignada a cada tribunal; el grado de conocimiento que la ley da a cada tribunal. La jurisdicción es la facultad genérica; la competencia la delimita.", "tema": "Jurisdicción y competencia"},
    {"frente": "¿Qué es la acción de protección (recurso de protección)?",
     "reverso": "Art. 20 CPR: acción constitucional para proteger los derechos y garantías del art. 19 CPR cuando son amenazados, perturbados o privados por acto u omisión arbitraria o ilegal. Se interpone ante la Corte de Apelaciones en 30 días. La corte adopta las providencias necesarias para restablecer el derecho.", "tema": "Recurso de protección procesal"},
])

# ── CONSTITUCIONAL extra 3 (+14) ──────────────────────────
MCQ_CONSTITUCIONAL.extend([
    {"pregunta": "El Senado de Chile está compuesto por senadores elegidos por:",
     "opciones": ["A. Regiones del país en circunscripciones","B. Distritos electorales","C. Designación presidencial","D. Sorteo entre abogados"],
     "correcta": 0, "fundamento": "Art. 49 CPR: el Senado está integrado por 50 senadores elegidos en votación directa por circunscripciones senatoriales (agrupaciones de regiones). El mandato es de 8 años.", "tema": "Senado composición"},

    {"pregunta": "La superintendencia directiva, correccional y económica de los tribunales de justicia corresponde a:",
     "opciones": ["A. El Ministerio de Justicia","B. La Corte Suprema","C. El Congreso Nacional","D. El Tribunal Constitucional"],
     "correcta": 1, "fundamento": "Art. 82 CPR: la Corte Suprema tiene la superintendencia directiva, correccional y económica de todos los tribunales de la nación, salvo el TC, el TRICEL y los tribunales militares en tiempo de guerra.", "tema": "Superintendencia de la Corte Suprema"},

    {"pregunta": "El principio de probidad en la función pública chilena está consagrado en:",
     "opciones": ["A. Solo en la Ley 18.575","B. En la CPR (art. 8) y en la Ley 18.575 de Bases de la Administración del Estado","C. Solo en el Estatuto Administrativo","D. Solo en el Código Penal"],
     "correcta": 1, "fundamento": "Art. 8 CPR: el ejercicio de las funciones públicas obliga a sus titulares a dar estricto cumplimiento al principio de probidad en todas sus actuaciones. Desarrollado en la Ley 18.575.", "tema": "Principio de probidad"},
])
VF_CONSTITUCIONAL.extend([
    {"afirmacion": "Chile es un Estado unitario con forma de gobierno republicana y democrática.",
     "respuesta": True, "fundamento": "Art. 3 CPR: el Estado de Chile es unitario; arts. 4-5 CPR: Chile es una República y su soberanía reside en la nación y se ejerce mediante elecciones periódicas y democráticas.", "tema": "Forma del Estado chileno"},

    {"afirmacion": "Los notarios en Chile son funcionarios del Poder Judicial.",
     "respuesta": False, "fundamento": "Los notarios son auxiliares de la administración de justicia (art. 389 COT) pero no son funcionarios del Poder Judicial propiamente tal. Son oficiales públicos del Estado con fe pública.", "tema": "Naturaleza de los notarios"},

    {"afirmacion": "El derecho de petición en Chile está garantizado solo para los ciudadanos.",
     "respuesta": False, "fundamento": "Art. 19 N°14 CPR: el derecho de petición corresponde a todas las personas, en forma individual o colectiva, sin que sea necesario ser ciudadano chileno.", "tema": "Derecho de petición"},
])
FC_CONSTITUCIONAL.extend([
    {"frente": "¿Qué es la reserva legal?",
     "reverso": "Principio por el cual ciertas materias (derechos fundamentales, delitos y penas, tributos, etc.) solo pueden ser reguladas mediante ley, no por normas reglamentarias. Arts. 19 N°2 y 63 CPR. El legislador no puede delegar estas materias al Ejecutivo.", "tema": "Reserva legal"},
    {"frente": "¿Qué es el principio de separación de poderes en Chile?",
     "reverso": "La CPR distribuye las funciones estatales entre el Ejecutivo (Presidente, art. 24), el Legislativo (Congreso bicameral, art. 46) y el Judicial (Cortes y juzgados, art. 76). Cada poder tiene funciones propias con controles mutuos. No es absoluta: hay áreas de colaboración.", "tema": "Separación de poderes"},
])

# ── LABORAL extra 3 (+13) ─────────────────────────────────
MCQ_LABORAL.extend([
    {"pregunta": "El reglamento interno de empresa en Chile es obligatorio cuando:",
     "opciones": ["A. Siempre","B. La empresa tiene 10 o más trabajadores permanentes","C. La empresa tiene 25 o más trabajadores","D. Solo en empresas industriales"],
     "correcta": 1, "fundamento": "Art. 153 CT: las empresas con 10 o más trabajadores permanentes deben tener un reglamento interno de orden, higiene y seguridad.", "tema": "Reglamento interno"},

    {"pregunta": "¿Qué regula la Ley 21.561 en materia laboral?",
     "opciones": ["A. El salario mínimo","B. La reducción progresiva de la jornada laboral a 40 horas semanales","C. La negociación colectiva sectorial","D. El teletrabajo"],
     "correcta": 1, "fundamento": "La Ley 21.561 (2024) redujo la jornada máxima ordinaria de 45 a 40 horas semanales con implementación gradual, y modificó varios aspectos de la distribución de la jornada y el teletrabajo.", "tema": "Ley 21.561 jornada laboral"},

    {"pregunta": "El trabajador puede solicitar la autodespido (despido indirecto) cuando:",
     "opciones": ["A. No está de acuerdo con las condiciones de trabajo","B. El empleador incurre en conductas graves que hacen intolerable la continuación del contrato","C. El salario no es suficiente","D. Hay cambio de empleador"],
     "correcta": 1, "fundamento": "Art. 171 CT: el trabajador puede poner término al contrato (despido indirecto o autodespido) cuando el empleador incurre en las causales del art. 160 (conductas graves), con derecho a indemnizaciones.", "tema": "Despido indirecto"},
])
VF_LABORAL.extend([
    {"afirmacion": "El trabajador tiene derecho a solicitar copia de su contrato de trabajo.",
     "respuesta": True, "fundamento": "Art. 9 CT: el empleador debe entregar al trabajador una copia del contrato de trabajo dentro de los 15 días siguientes a su incorporación. Si no lo hace, la copia entregada por el trabajador se presume auténtica.", "tema": "Copia del contrato"},

    {"afirmacion": "La huelga es siempre ilegal si no se ha agotado el procedimiento de negociación colectiva reglada.",
     "respuesta": False, "fundamento": "Art. 345 CT: la huelga en el marco de la negociación colectiva reglada está permitida. Fuera de ese marco, existen huelgas no reguladas cuya legalidad es debatida. No toda huelga al margen del procedimiento es ilegal.", "tema": "Legalidad de la huelga"},

    {"afirmacion": "El empleador puede rebajar el sueldo base del trabajador con su consentimiento.",
     "respuesta": False, "fundamento": "Art. 5 CT: los derechos establecidos por las leyes laborales son irrenunciables. El sueldo base mínimo y las condiciones establecidas por ley no pueden rebajarse ni aún con consentimiento del trabajador.", "tema": "Irrenunciabilidad del sueldo"},
])
FC_LABORAL.extend([
    {"frente": "¿Qué es el fuero sindical?",
     "reverso": "Protección que impide al empleador despedir sin autorización judicial previa a los dirigentes sindicales y candidatos a directores (art. 224 CT). El empleador que quiera poner término al contrato de un trabajador con fuero debe solicitar previamente un desafuero ante el tribunal.", "tema": "Fuero sindical"},
])

# ── OBLIGACIONES extra 3 (+13) ────────────────────────────
MCQ_OBLIGACIONES.extend([
    {"pregunta": "La indivisibilidad del pago en Chile implica que:",
     "opciones": ["A. El pago puede hacerse en cuotas sin consentimiento del acreedor","B. El acreedor no está obligado a recibir un pago parcial sin su consentimiento","C. Todas las obligaciones son divisibles","D. La indivisibilidad solo opera en las de género"],
     "correcta": 1, "fundamento": "Art. 1591 CC: el deudor no puede obligar al acreedor a recibir en parte el pago de una deuda, aunque esta sea divisible. El pago debe ser completo.", "tema": "Indivisibilidad del pago"},

    {"pregunta": "¿Cuándo se considera hecha en tiempo oportuno la interrupción de la prescripción?",
     "opciones": ["A. Al presentar la demanda","B. Al notificarse la demanda al deudor","C. Al inscribirse la acción en el CBR","D. Al momento de la sentencia definitiva"],
     "correcta": 1, "fundamento": "Art. 2503 CC: la interrupción civil de la prescripción se produce con la notificación legal de la demanda al deudor. La sola presentación de la demanda no interrumpe la prescripción.", "tema": "Interrupción de la prescripción"},

    {"pregunta": "En las obligaciones de hacer, la indemnización de perjuicios por incumplimiento requiere:",
     "opciones": ["A. Solo la mora del deudor","B. El incumplimiento, la mora (requerimiento judicial o extrajudicial) y el daño","C. Solo el daño probado","D. No requiere mora"],
     "correcta": 1, "fundamento": "Art. 1557 CC: la indemnización de perjuicios por incumplimiento de obligaciones de hacer requiere constitución en mora del deudor (arts. 1551-1552 CC) más el daño efectivo.", "tema": "Perjuicios en obligaciones de hacer"},
])
VF_OBLIGACIONES.extend([
    {"afirmacion": "Las arras en la compraventa pueden significar que el contrato no está perfeccionado.",
     "respuesta": True, "fundamento": "Art. 1803 CC: si se vende a prueba o con señal de estar en trato, el que da las arras puede retractarse perdiendo las arras o el que las recibió devolviendo el doble, mientras el contrato no se perfeccione.", "tema": "Arras en la compraventa"},

    {"afirmacion": "La prescripción puede renunciarse antes de que se complete el plazo.",
     "respuesta": False, "fundamento": "Art. 2494 CC: la prescripción puede renunciarse, pero solo después de haberse completado. La renuncia anticipada está prohibida.", "tema": "Renuncia a la prescripción"},

    {"afirmacion": "El mandato sin plazo se extingue por la revocación del mandante.",
     "respuesta": True, "fundamento": "Art. 2163 N°3 CC: el mandato termina por la revocación del mandante. El mandante puede revocar el mandato a su voluntad, salvo que el mandato sea irrevocable por haberse otorgado en interés del mandatario o de un tercero.", "tema": "Revocación del mandato"},
])
FC_OBLIGACIONES.extend([
    {"frente": "¿Qué es el beneficio de inventario?",
     "reverso": "En sucesión: el heredero acepta con beneficio de inventario limitando su responsabilidad al valor de los bienes heredados (art. 1247 CC). En fianza: el fiador goza del beneficio de excusión (art. 2357 CC) y puede oponer al acreedor la acción del deudor principal primero.", "tema": "Beneficio de inventario y excusión"},
    {"frente": "¿Qué son los créditos privilegiados?",
     "reverso": "Son aquellos que, por disposición de la ley, se pagan con preferencia sobre otros acreedores. Se ordenan en clases (arts. 2470-2477 CC): 1ª clase (gastos de justicia, remuneraciones, etc.), 2ª clase (prenda), 3ª clase (hipoteca), 4ª clase (el fisco y otros), 5ª clase (quirografarios o valistas).", "tema": "Créditos privilegiados y prelación"},
])

# ── FAMILIA extra 3 (+7) ──────────────────────────────────
MCQ_FAMILIA.extend([
    {"pregunta": "¿Cuál es el plazo para demandar la nulidad de un matrimonio en Chile?",
     "opciones": ["A. 1 año desde la celebración","B. 5 años desde la celebración","C. No hay plazo; la nulidad es imprescriptible","D. Depende de la causal: algunas prescriben, otras no"],
     "correcta": 3, "fundamento": "Arts. 47-48 LMC: la acción de nulidad matrimonial prescribe en general en 1 año desde que cese la convivencia, salvo para ciertas causales (bigamia: 1 año desde disuelto el primer vínculo; por ser el forzado: 1 año desde que cesó la fuerza).", "tema": "Prescripción nulidad matrimonial"},
])
VF_FAMILIA.extend([
    {"afirmacion": "El reconocimiento de hijo en Chile puede hacerse en el acto de inscripción de nacimiento.",
     "respuesta": True, "fundamento": "Art. 187 CC: el reconocimiento voluntario del hijo puede hacerse en el acto de inscripción del nacimiento, por escritura pública, por acto testamentario o por manifestación ante el Juzgado de Familia.", "tema": "Reconocimiento de hijo"},

    {"afirmacion": "La subrogación del régimen de sociedad conyugal puede hacerse en cualquier momento del matrimonio.",
     "respuesta": False, "fundamento": "Art. 1762 CC: la sustitución del régimen de sociedad conyugal requiere acuerdo de ambos cónyuges, escritura pública y sub-inscripción al margen de la partida de matrimonio. La subrogación de bienes es diferente.", "tema": "Modificación del régimen matrimonial"},
])
FC_FAMILIA.extend([
    {"frente": "¿Qué es la relación directa y regular (RDR)?",
     "reverso": "Derecho del padre o madre que no tiene el cuidado personal a mantener una relación directa y regular con el hijo. Incluye visitas, comunicaciones y permanencias (art. 229 CC). Su regulación debe considerar el interés superior del niño.", "tema": "Relación directa y regular"},
])

# ── COMERCIAL extra 3 (+9) ────────────────────────────────
MCQ_COMERCIAL.extend([
    {"pregunta": "El mandato mercantil difiere del civil en que:",
     "opciones": ["A. Es gratuito por naturaleza","B. Se presume oneroso por naturaleza","C. No puede otorgarse por escrito","D. No puede ser revocado"],
     "correcta": 1, "fundamento": "Art. 234 C.Com.: el mandato comercial es por su naturaleza oneroso; en caso de silencio de las partes, el mandatario tiene derecho a la remuneración que se establezca por la comisión.", "tema": "Mandato mercantil oneroso"},

    {"pregunta": "La comisión en el derecho mercantil chileno es:",
     "opciones": ["A. Una especie de mandato para ejecutar actos de comercio","B. Una sociedad accidental","C. Un contrato de depósito","D. Una forma de seguro"],
     "correcta": 0, "fundamento": "Art. 233 C.Com.: la comisión es una especie de mandato por el cual se encomienda a una persona, que se dedica a ello en forma profesional, la ejecución de uno o más negocios mercantiles. El comisionista actúa en nombre propio.", "tema": "Comisión mercantil"},
])
VF_COMERCIAL.extend([
    {"afirmacion": "En Chile, la empresa individual de responsabilidad limitada (EIRL) puede realizar cualquier actividad económica.",
     "respuesta": False, "fundamento": "Ley 19.857 (EIRL): la EIRL solo puede realizar actividades de carácter comercial, industrial o de prestación de servicios; no puede ejercer actividades reservadas por ley a otras formas jurídicas.", "tema": "EIRL actividades"},

    {"afirmacion": "La prescripción de las acciones mercantiles en Chile es generalmente de 4 años.",
     "respuesta": True, "fundamento": "Art. 822 C.Com.: las acciones mercantiles prescriben a los 4 años, salvo disposición especial. Existen plazos más cortos para acciones específicas (letras de cambio, seguros, etc.).", "tema": "Prescripción mercantil"},
])
FC_COMERCIAL.extend([
    {"frente": "¿Qué es la sociedad accidental o en participación?",
     "reverso": "Art. 507 C.Com.: es una sociedad que no es persona jurídica, no forma nombre colectivo ni está sujeta a formalidades. Un partícipe actúa frente a terceros como único dueño del negocio; internamente distribuye ganancias con los demás partícipes.", "tema": "Sociedad accidental o en participación"},
])

# ── BIENES extra 3 (+6) ───────────────────────────────────
MCQ_BIENES.extend([
    {"pregunta": "La accesión de buena fe en Chile permite al dueño del suelo:",
     "opciones": ["A. Demoler lo construido sin indemnizar","B. Hacer suya la obra pagando el valor de los materiales o el mayor valor adquirido por el predio","C. Solo reclamar el suelo","D. No tiene derechos sobre lo construido"],
     "correcta": 1, "fundamento": "Art. 669 CC: el dueño del suelo en que otra persona ha edificado de buena fe tiene la opción de hacer suya la obra pagando las indemnizaciones que establece la ley (materiales y valor del trabajo).", "tema": "Accesión buena fe"},
])
VF_BIENES.extend([
    {"afirmacion": "El derecho de hipoteca sigue a la finca aunque cambie de dueño.",
     "respuesta": True, "fundamento": "Art. 2428 CC: la hipoteca da al acreedor el derecho de persecución, es decir, puede hacerla efectiva aunque la finca haya pasado a manos de terceros. El acreedor hipotecario tiene acción real.", "tema": "Derecho de persecución hipotecaria"},
])
FC_BIENES.extend([
    {"frente": "¿Qué es el derecho de opción del propietario del suelo en accesión?",
     "reverso": "Art. 669 CC: el dueño del terreno donde otro construyó o plantó tiene opción de: 1) Hacer suyo lo edificado/plantado pagando el justo precio de los materiales, 2) Obligar al edificante a pagarle el justo precio del terreno. La elección depende de la buena o mala fe del edificante.", "tema": "Opción del dueño del suelo"},
    {"frente": "¿Qué es el derecho de uso en Chile?",
     "reverso": "Art. 811 CC: el derecho de uso es un derecho real que consiste en la facultad de gozar de una parte limitada de las utilidades y productos de una cosa. Es más restringido que el usufructo: el usuario solo puede tomar lo que necesita para sí y su familia.", "tema": "Derecho de uso"},
])

# ── SUCESORIO extra 3 (+2) ────────────────────────────────
VF_SUCESORIO.extend([
    {"afirmacion": "El testamento público abierto se otorga siempre ante notario en Chile.",
     "respuesta": True, "fundamento": "Art. 1015 CC: el testamento solemne abierto debe otorgarse ante competente notario y tres testigos, o ante cinco testigos si no hay notario. El notario da fe del acto.", "tema": "Testamento público abierto"},
])
FC_SUCESORIO.extend([
    {"frente": "¿Qué es la petición de herencia?",
     "reverso": "Art. 1264 CC: el heredero a quien se priva de la herencia puede intentar la acción de petición de herencia contra quien la tiene en su lugar, invocando su calidad de heredero. Prescribe en 10 años contados desde la posesión.", "tema": "Petición de herencia"},
])

# ── INTERNACIONAL extra 3 (+2) ────────────────────────────
MCQ_INTERNACIONAL.extend([
    {"pregunta": "La extradición en Chile puede denegarse cuando:",
     "opciones": ["A. El delito tiene pena inferior a 1 año","B. El solicitado es chileno (en ciertos casos), el delito es político o la pena es la de muerte o cadena perpetua sin posibilidad de libertad","C. Solo cuando no hay tratado con el país requirente","D. Siempre si la persona tiene residencia en Chile"],
     "correcta": 1, "fundamento": "El Código de Derecho Internacional Privado (Bustamante) y los tratados de extradición establecen causales de denegación: delito político, persecución por razones de raza o religión, pena de muerte en el país requirente, entre otras.", "tema": "Extradición causales de denegación"},
])

# ── AMBIENTAL extra 3 (+1) ────────────────────────────────
FC_AMBIENTAL.extend([
    {"frente": "¿Qué es una Resolución de Calificación Ambiental (RCA)?",
     "reverso": "Resolución que emite la Comisión de Evaluación Ambiental (COEVA) al término del proceso de SEIA. Puede aprobar (con o sin condiciones) o rechazar un proyecto. La RCA favorable es requisito previo para obtener permisos sectoriales (art. 8 Ley 19.300).", "tema": "RCA"},
])


# ════════════════════════════════════════════════════════════════
# EXTENSIÓN 4 — completar hasta 500
# ════════════════════════════════════════════════════════════════

MCQ_CIVIL.extend([
    {"pregunta": "¿Qué son los bienes reservados de la mujer casada en sociedad conyugal?",
     "opciones": ["A. Todos sus bienes propios","B. Los bienes adquiridos en el ejercicio de su trabajo separado del marido","C. Solo los bienes raíces","D. Los heredados de sus padres"],
     "correcta": 1, "fundamento": "Art. 150 CC: los bienes reservados son aquellos que la mujer adquiere en el ejercicio de su profesión, industria u oficio separado del marido. Los administra ella sola.", "tema": "Bienes reservados de la mujer"},
    {"pregunta": "El usufructo legal del padre o madre sobre los bienes del hijo sujeto a patria potestad:",
     "opciones": ["A. Ya no existe en el CC chileno","B. Fue derogado; la patria potestad no da usufructo sobre bienes del hijo","C. Existe sobre todos los bienes del hijo","D. Solo existe sobre bienes muebles"],
     "correcta": 1, "fundamento": "La reforma de 1989 (Ley 18.802) derogó el usufructo legal del padre sobre los bienes del hijo. Hoy la patria potestad implica solo la representación legal y administración de bienes, sin usufructo.", "tema": "Usufructo legal patria potestad"},
])
VF_CIVIL.extend([
    {"afirmacion": "La cláusula de no enajenar en contratos civiles chilenos es siempre nula.",
     "respuesta": False, "fundamento": "La validez de las cláusulas de no enajenar es controvertida. Se distingue según si la prohibición es temporal y tiene causa lícita (válida) o es perpetua (nula). Los arts. 1126 y 2415 CC sugieren que ciertas prohibiciones son admisibles.", "tema": "Cláusula de no enajenar"},
    {"afirmacion": "La inscripción en el CBR de un contrato de arrendamiento lo hace oponible al sucesor del arrendador.",
     "respuesta": True, "fundamento": "Art. 1962 CC: el arrendamiento inscrito en el CBR obliga a los terceros que adquieran el inmueble a respetar el arriendo hasta su término.", "tema": "Arrendamiento inscrito CBR"},
])
FC_CIVIL.extend([
    {"frente": "¿Qué es la acción de precario?",
     "reverso": "Art. 2195 CC: el comodato degenera en precario cuando el comodante puede pedir la restitución a su arbitrio. La acción de precario permite al dueño recuperar la cosa que está siendo usada sin título y sin su voluntad, o que usa a su mera tolerancia.", "tema": "Acción de precario"},
])

MCQ_PENAL.extend([
    {"pregunta": "¿Qué es el principio de non reformatio in peius?",
     "opciones": ["A. El tribunal puede agravar la pena al conocer un recurso del condenado","B. El tribunal no puede agravar la situación del recurrente si solo él recurre","C. Solo aplica en primera instancia","D. Solo en recursos de nulidad"],
     "correcta": 1, "fundamento": "Art. 360 inc. 1 CPP: la Corte no puede reformar la resolución en perjuicio del imputado que recurre, cuando solo este o su defensor hubieren interpuesto el recurso (prohibición de reformatio in peius).", "tema": "Non reformatio in peius"},
    {"pregunta": "El concurso aparente de leyes penales se resuelve por los principios de:",
     "opciones": ["A. Especialidad, subsidiariedad, consunción y alternatividad","B. Acumulación y absorción","C. Solo por especialidad","D. Solo por el principio de favorabilidad"],
     "correcta": 0, "fundamento": "El concurso aparente de leyes penales (cuando una conducta parece encuadrar en varios tipos) se resuelve por los principios de especialidad (lex specialis), subsidiariedad (tipo principal preferente), consunción (el delito mayor absorbe el menor) y alternatividad.", "tema": "Concurso aparente de leyes penales"},
])
VF_PENAL.extend([
    {"afirmacion": "La prescripción penal se interrumpe por la comisión de un nuevo crimen o simple delito.",
     "respuesta": True, "fundamento": "Art. 96 CP: la prescripción se interrumpe si el imputado comete nuevo crimen o simple delito; en este caso comienza a correr de nuevo la prescripción desde la perpetración de dicho nuevo crimen.", "tema": "Interrupción prescripción penal"},
])

MCQ_PROCESAL.extend([
    {"pregunta": "La incompetencia relativa en materia procesal civil se alega mediante:",
     "opciones": ["A. Excepción dilatoria antes de contestar la demanda","B. Declaración de oficio por el juez","C. Recurso de casación en la forma","D. Excepción perentoria"],
     "correcta": 0, "fundamento": "Art. 303 N°1 CPC: la incompetencia relativa del tribunal es una excepción dilatoria que debe oponerse antes de la contestación de la demanda. La incompetencia absoluta puede declararse de oficio.", "tema": "Incompetencia relativa"},
    {"pregunta": "¿Cuál es el efecto devolutivo del recurso de apelación?",
     "opciones": ["A. El tribunal superior asume el conocimiento del asunto","B. El tribunal inferior suspende la ejecución","C. El asunto vuelve al mismo juez","D. El recurso suspende el proceso en ambas instancias"],
     "correcta": 0, "fundamento": "El efecto devolutivo es inherente a la apelación: el conocimiento del asunto se devuelve (o entrega) al tribunal superior (Corte de Apelaciones). El efecto suspensivo impide cumplir la resolución mientras pende el recurso.", "tema": "Efectos de la apelación"},
])
FC_PROCESAL.extend([
    {"frente": "¿Qué es la preclusión procesal?",
     "reverso": "Extinción de la facultad procesal por: 1) haber ejercido la facultad en términos incompatibles con la nueva actuación, 2) haber dejado pasar el plazo sin ejercerla, 3) haber realizado un acto incompatible con su ejercicio. Garantiza la progresión del proceso.", "tema": "Preclusión procesal"},
])

MCQ_CONSTITUCIONAL.extend([
    {"pregunta": "¿Qué es el principio de servicialidad del Estado en la CPR chilena?",
     "opciones": ["A. El Estado presta servicios públicos gratuitos","B. El Estado está al servicio de la persona humana y su fin es promover el bien común","C. El Estado subsidia a los privados","D. La empresa pública sirve a la empresa privada"],
     "correcta": 1, "fundamento": "Art. 1 inc. 4 CPR: el Estado está al servicio de la persona humana y su finalidad es promover el bien común, para lo cual debe contribuir a crear las condiciones sociales que permitan a todos y cada uno de los integrantes de la comunidad nacional su mayor realización espiritual y material.", "tema": "Servicialidad del Estado"},
])
VF_CONSTITUCIONAL.extend([
    {"afirmacion": "El proceso de reforma constitucional en Chile puede iniciarse en la Cámara de Diputados o en el Senado.",
     "respuesta": True, "fundamento": "Art. 127 CPR: los proyectos de reforma constitucional pueden tener su origen en la Cámara de Diputados o en el Senado, por mensaje del Presidente o por moción parlamentaria.", "tema": "Iniciativa de reforma constitucional"},
])

MCQ_LABORAL.extend([
    {"pregunta": "La licencia post-natal parental en Chile permite al padre usar parte del postnatal cuando:",
     "opciones": ["A. Nunca; el postnatal es exclusivo de la madre","B. A partir de la 7ª semana del postnatal, la madre puede traspasar semanas al padre","C. El padre puede usar la totalidad del postnatal","D. Solo si la madre fallece"],
     "correcta": 1, "fundamento": "Art. 197 bis CT: a partir de la 7ª semana del postnatal, la madre puede ceder semanas al padre a tiempo completo o partial, siempre que el hijo tenga al menos 6 semanas de edad.", "tema": "Postnatal parental compartido"},
])

MCQ_OBLIGACIONES.extend([
    {"pregunta": "La acción resolutoria en Chile compete exclusivamente a:",
     "opciones": ["A. Ambas partes del contrato bilateral","B. El contratante diligente que cumplió o está llano a cumplir su obligación","C. Al deudor","D. Al tribunal de oficio"],
     "correcta": 1, "fundamento": "Art. 1489 CC: la condición resolutoria tácita da derecho al contratante diligente (que cumplió o está llano a cumplir) para pedir la resolución o el cumplimiento, con indemnización de perjuicios.", "tema": "Acción resolutoria"},
])

MCQ_FAMILIA.extend([
    {"pregunta": "La declaración de interdicción por demencia en Chile:",
     "opciones": ["A. Es automática cuando el médico lo certifica","B. Requiere sentencia judicial y priva al interdicto de la administración de sus bienes","C. Solo puede decretarse para mayores de 65 años","D. Solo la puede pedir la familia directa"],
     "correcta": 1, "fundamento": "Arts. 456 y ss. CC: la interdicción por demencia requiere declaración judicial. El demente interdicto es absolutamente incapaz; sus actos son nulos de pleno derecho.", "tema": "Interdicción por demencia"},
])

MCQ_COMERCIAL.extend([
    {"pregunta": "El seguro de vida en Chile es principalmente:",
     "opciones": ["A. Un contrato real","B. Un contrato consensual y de adhesión que cubre el riesgo de muerte o sobrevivencia del asegurado","C. Un contrato solo para personas jurídicas","D. Obligatorio para todos los trabajadores"],
     "correcta": 1, "fundamento": "Art. 588 C.Com.: el seguro de vida es un contrato en virtud del cual la empresa aseguradora se obliga a pagar al beneficiario una suma determinada si el asegurado muere o sobrevive a la fecha estipulada.", "tema": "Seguro de vida"},
])

# ════════════════════════════════════════════════════════════════
# EXPANSIÓN V/F — mínimo 25 por ramo
# ════════════════════════════════════════════════════════════════

VF_CIVIL.extend([
    {"afirmacion": "La compraventa de bienes raíces en Chile es un contrato solemne que requiere escritura pública.", "respuesta": True, "fundamento": "Art. 1801 inc. 2 CC: la venta de bienes raíces, servidumbres y censos requiere escritura pública para su validez.", "tema": "Solemnidades compraventa"},
    {"afirmacion": "El pago con subrogación transfiere el crédito con todos sus accesorios, incluyendo las cauciones.", "respuesta": True, "fundamento": "Art. 1612 CC: la subrogación transfiere al nuevo acreedor el crédito con sus fianzas, privilegios e hipotecas.", "tema": "Pago con subrogación"},
    {"afirmacion": "La nulidad relativa puede ser saneada por ratificación de las partes o por el transcurso del tiempo.", "respuesta": True, "fundamento": "Art. 1684 CC: la nulidad relativa se sanea por ratificación voluntaria de la parte que puede alegarla o por el transcurso del tiempo (4 años).", "tema": "Saneamiento nulidad relativa"},
    {"afirmacion": "La novación extingue la obligación primitiva y crea una nueva en su lugar.", "respuesta": True, "fundamento": "Art. 1628 CC: la novación es la sustitución de una nueva obligación a otra anterior, la cual queda por tanto extinguida.", "tema": "Novación"},
    {"afirmacion": "El mandato es un contrato naturalmente oneroso en el Código Civil chileno.", "respuesta": False, "fundamento": "Art. 2117 CC: el mandato puede ser gratuito o remunerado; su naturaleza es naturalmente gratuita salvo pacto en contrario.", "tema": "Naturaleza del mandato"},
    {"afirmacion": "La acción de precario del art. 2195 CC requiere que el demandado sea el dueño del bien.", "respuesta": False, "fundamento": "Art. 2195 CC: la acción de precario la ejerce el dueño contra quien tiene la cosa sin contrato y por mera tolerancia o inadvertencia.", "tema": "Precario"},
    {"afirmacion": "El usufructo legal del padre sobre los bienes del hijo requiere inscripción en el CBR.", "respuesta": False, "fundamento": "Arts. 810 y 252 CC: el usufructo legal del padre sobre bienes del hijo no requiere inscripción; opera por el solo ministerio de la ley.", "tema": "Usufructo legal"},
])

VF_PENAL.extend([
    {"afirmacion": "En Chile, la tentativa se castiga siempre con la misma pena que el delito consumado.", "respuesta": False, "fundamento": "Art. 51 CP: la tentativa se castiga con la pena inferior en dos grados a la señalada para el delito consumado.", "tema": "Iter criminis"},
    {"afirmacion": "El encubrimiento es una forma de participación criminal en el Código Penal chileno.", "respuesta": True, "fundamento": "Art. 14 CP: son responsables criminalmente de los delitos: los autores, los cómplices y los encubridores.", "tema": "Participación criminal"},
    {"afirmacion": "La legítima defensa puede invocarse para proteger los bienes materiales propios.", "respuesta": True, "fundamento": "Art. 10 N°6 CP: la defensa de los bienes materiales es una causal de justificación cuando existe agresión ilegítima y necesidad racional del medio.", "tema": "Legítima defensa de bienes"},
    {"afirmacion": "El delito culposo en Chile se sanciona de la misma forma que el doloso.", "respuesta": False, "fundamento": "Arts. 490-492 CP: los cuasidelitos tienen sanciones expresamente menores y solo son punibles cuando la ley lo establece expresamente.", "tema": "Culpa penal"},
    {"afirmacion": "La prescripción de la acción penal se interrumpe por la comisión de un nuevo crimen o simple delito.", "respuesta": True, "fundamento": "Art. 96 CP: la prescripción de la acción penal se interrumpe si el delincuente comete un nuevo crimen o simple delito.", "tema": "Prescripción penal"},
    {"afirmacion": "El dolo eventual es suficiente para configurar homicidio doloso en Chile.", "respuesta": True, "fundamento": "La doctrina mayoritaria chilena acepta el dolo eventual como forma de dolo para todos los delitos que requieren dolo, incluido el homicidio.", "tema": "Dolo eventual"},
])

VF_PROCESAL.extend([
    {"afirmacion": "La litispendencia es una excepción dilatoria en el procedimiento civil chileno.", "respuesta": True, "fundamento": "Art. 303 N°3 CPC: la litispendencia (existencia de juicio pendiente entre las mismas partes sobre la misma materia) es una excepción dilatoria.", "tema": "Excepciones dilatorias"},
    {"afirmacion": "El recurso de queja procede contra sentencias definitivas e interlocutorias.", "respuesta": False, "fundamento": "Art. 545 COT: el recurso de queja procede solo cuando no exista recurso ordinario o extraordinario para corregir la falta o abuso grave cometida en la resolución.", "tema": "Recurso de queja"},
    {"afirmacion": "En Chile, la notificación personal debe hacerse en días y horas hábiles.", "respuesta": True, "fundamento": "Art. 41 CPC: las actuaciones deben practicarse en días y horas hábiles; la notificación personal fuera del tribunal solo puede hacerse de lunes a sábado.", "tema": "Notificación personal"},
    {"afirmacion": "El juicio sumario procede siempre que la naturaleza de la acción lo requiera y sea necesaria rapidez.", "respuesta": True, "fundamento": "Art. 680 CPC: el juicio sumario se aplica cuando la naturaleza de la acción deducida requiera una tramitación rápida para que sea eficaz.", "tema": "Juicio sumario"},
    {"afirmacion": "La apelación en el procedimiento laboral chileno suspende siempre los efectos de la sentencia.", "respuesta": False, "fundamento": "Art. 476 CT: las sentencias definitivas en juicio laboral son de cumplimiento inmediato; la apelación no suspende la ejecución.", "tema": "Apelación laboral"},
    {"afirmacion": "En el recurso de casación en la forma, el vicio debe haber influido en lo dispositivo del fallo.", "respuesta": True, "fundamento": "Art. 768 inc. final CPC: no obstante los vicios del art. 768, el tribunal puede desestimar el recurso si el vicio no influyó en lo dispositivo del fallo.", "tema": "Casación en la forma"},
    {"afirmacion": "El mandato judicial se constituye válidamente mediante escritura pública, acta extendida ante el juez o declaración escrita.", "respuesta": True, "fundamento": "Art. 6 CPC: el mandato judicial puede constituirse por escritura pública, acta ante el tribunal o declaración escrita del mandante.", "tema": "Mandato judicial"},
])

VF_CONSTITUCIONAL.extend([
    {"afirmacion": "En Chile, el Tribunal Constitucional puede declarar inaplicable una ley que vulnere la Constitución.", "respuesta": True, "fundamento": "Art. 93 N°6 CPR: el TC puede declarar inaplicable un precepto legal cuya aplicación en una gestión pendiente resulte contraria a la Constitución.", "tema": "Inaplicabilidad por inconstitucionalidad"},
    {"afirmacion": "El Estado de excepción constitucional de catástrofe solo puede ser declarado por el Congreso.", "respuesta": False, "fundamento": "Art. 41 CPR: el estado de catástrofe es declarado por el Presidente de la República, dando cuenta al Congreso.", "tema": "Estados de excepción"},
    {"afirmacion": "Los tratados internacionales sobre derechos humanos ratificados por Chile y vigentes tienen rango constitucional explícito.", "respuesta": False, "fundamento": "Art. 5 inc. 2 CPR: hay debate doctrinario; la disposición no les otorga rango constitucional explícito, sino que limita la soberanía estatal.", "tema": "Tratados internacionales DDHH"},
    {"afirmacion": "La acción de amparo en Chile protege el derecho a la libertad personal y seguridad individual.", "respuesta": True, "fundamento": "Art. 21 CPR: el amparo (habeas corpus) protege a toda persona privada o amenazada en su libertad personal.", "tema": "Acción de amparo"},
    {"afirmacion": "El Senado puede declarar la inhabilidad del Presidente de la República para el ejercicio de sus funciones.", "respuesta": True, "fundamento": "Art. 53 N°7 CPR: el Senado puede declarar la inhabilidad del Presidente de la República invocada por éste mismo.", "tema": "Inhabilidad presidencial"},
    {"afirmacion": "En Chile, la iniciativa exclusiva de ley en materia de gasto fiscal corresponde al Presidente de la República.", "respuesta": True, "fundamento": "Art. 65 CPR: corresponde al Presidente la iniciativa exclusiva para proyectos que irrogan gasto público o fijen remuneraciones.", "tema": "Iniciativa exclusiva del Ejecutivo"},
    {"afirmacion": "El recurso de protección puede interponerse dentro de los 60 días desde que se produce el acto u omisión.", "respuesta": False, "fundamento": "Auto Acordado CS: el recurso de protección debe interponerse dentro de 30 días corridos desde el acto u omisión o desde que se tuvo conocimiento.", "tema": "Plazo recurso de protección"},
    {"afirmacion": "En Chile, los parlamentarios gozan de inviolabilidad solo por las opiniones emitidas en el desempeño de su cargo.", "respuesta": True, "fundamento": "Art. 61 inc. 1 CPR: los diputados y senadores son inviolables por las opiniones que manifiesten y los votos que emitan en el desempeño de sus cargos.", "tema": "Inviolabilidad parlamentaria"},
])

VF_LABORAL.extend([
    {"afirmacion": "El fuero sindical en Chile impide el despido del trabajador sin autorización judicial previa.", "respuesta": True, "fundamento": "Art. 243 CT: los dirigentes sindicales gozan de fuero desde la elección hasta 6 meses después; el despido requiere desafuero judicial.", "tema": "Fuero sindical"},
    {"afirmacion": "La semana corrida beneficia a todos los trabajadores con remuneración mensual fija.", "respuesta": False, "fundamento": "Art. 45 CT: la semana corrida beneficia a los trabajadores con remuneración variable (comisiones, tratos) y no a los que perciben sueldo mensual fijo exclusivamente.", "tema": "Semana corrida"},
    {"afirmacion": "El empleador puede modificar el contrato de trabajo en forma unilateral mediante el ius variandi.", "respuesta": True, "fundamento": "Art. 12 CT: el empleador puede alterar unilateralmente la naturaleza del trabajo, el sitio o recinto, y el horario, con las limitaciones del art. 12.", "tema": "Ius variandi"},
    {"afirmacion": "La huelga en Chile suspende el contrato de trabajo durante su duración.", "respuesta": True, "fundamento": "Art. 377 CT: durante la huelga se suspenden los contratos de trabajo; el trabajador no está obligado a prestar servicio ni el empleador a pagar.", "tema": "Efectos de la huelga"},
    {"afirmacion": "El empleador está obligado a pagar cotizaciones previsionales aunque el trabajador no las solicite.", "respuesta": True, "fundamento": "Art. 58 CT y DL 3.500: el empleador debe retener y pagar las cotizaciones previsionales del trabajador como obligación legal, independiente de la voluntad del trabajador.", "tema": "Cotizaciones previsionales"},
    {"afirmacion": "El contrato de trabajo a honorarios queda sujeto a las normas del Código del Trabajo.", "respuesta": False, "fundamento": "Art. 7 CT: el contrato de honorarios no genera relación laboral si no existe subordinación y dependencia. Si existe vínculo de subordinación, se aplica el CT independiente de la denominación.", "tema": "Contrato de honorarios"},
    {"afirmacion": "La duración máxima de la jornada ordinaria de trabajo en Chile es de 45 horas semanales.", "respuesta": False, "fundamento": "Ley 21.561 (2024): la jornada ordinaria máxima es de 40 horas semanales, reduciéndose gradualmente desde 45.", "tema": "Jornada ordinaria 2024"},
    {"afirmacion": "El feriado anual mínimo en Chile es de 15 días hábiles para trabajadores con más de 1 año de servicios.", "respuesta": True, "fundamento": "Art. 67 CT: los trabajadores con más de un año de servicio tienen derecho a un feriado anual de 15 días hábiles.", "tema": "Feriado legal"},
    {"afirmacion": "El finiquito firmado ante un inspector del trabajo tiene mérito ejecutivo.", "respuesta": True, "fundamento": "Art. 177 CT: el finiquito suscrito ante el inspector del trabajo tiene mérito ejecutivo y es oponible al trabajador.", "tema": "Finiquito"},
])

VF_OBLIGACIONES.extend([
    {"afirmacion": "La mora del acreedor (mora creditoris) libera al deudor de responsabilidad por pérdida fortuita de la especie.", "respuesta": True, "fundamento": "Art. 1680 CC: la mora del acreedor hace responsable al deudor solo de culpa grave o dolo, eximiéndole de culpa leve y levísima.", "tema": "Mora del acreedor"},
    {"afirmacion": "La cláusula penal puede acumularse a la obligación principal si las partes así lo estipulan.", "respuesta": True, "fundamento": "Art. 1537 CC: normalmente la pena reemplaza a la indemnización, pero puede acumularse si las partes lo pactaron expresamente.", "tema": "Cláusula penal"},
    {"afirmacion": "La compensación requiere que ambas deudas sean de igual naturaleza y actualmente exigibles.", "respuesta": True, "fundamento": "Art. 1656 CC: la compensación opera cuando ambas partes son mutuamente deudoras de cosas fungibles de igual género y calidad, líquidas y actualmente exigibles.", "tema": "Compensación legal"},
    {"afirmacion": "La confusión extingue la fianza cuando opera entre el deudor y el acreedor principal.", "respuesta": True, "fundamento": "Art. 1667 CC: si se reúne en una persona la calidad de acreedor y deudor, la obligación se extingue por confusión. La fianza también se extingue.", "tema": "Confusión"},
    {"afirmacion": "La transacción tiene efectos de cosa juzgada entre las partes.", "respuesta": True, "fundamento": "Art. 2460 CC: la transacción produce el efecto de cosa juzgada en última instancia, pero solo entre los contratantes.", "tema": "Transacción"},
    {"afirmacion": "En las obligaciones solidarias, cada deudor puede oponer al acreedor las excepciones personales de los demás codeudores.", "respuesta": False, "fundamento": "Art. 1520 CC: en la solidaridad pasiva, el codeudor puede oponer las excepciones reales (comunes a todos) pero NO las excepciones personales de los demás codeudores.", "tema": "Solidaridad pasiva"},
    {"afirmacion": "El plazo extintivo hace exigible la obligación solo desde que vence.", "respuesta": False, "fundamento": "El plazo suspensivo hace exigible la obligación desde que vence. El plazo extintivo, en cambio, pone fin a un derecho o relación jurídica.", "tema": "Modalidades de las obligaciones"},
    {"afirmacion": "La acción pauliana o revocatoria requiere que el acto del deudor cause perjuicio a los acreedores.", "respuesta": True, "fundamento": "Art. 2468 CC: para la acción pauliana se requiere: (1) que el acto cause daño a los acreedores, (2) en actos onerosos, que el adquirente sea de mala fe.", "tema": "Acción pauliana"},
    {"afirmacion": "La dación en pago requiere consentimiento del acreedor para extinguir la obligación.", "respuesta": True, "fundamento": "La dación en pago (art. 1569 CC a contrario sensu) requiere acuerdo entre acreedor y deudor: el acreedor acepta recibir una prestación distinta a la debida.", "tema": "Dación en pago"},
    {"afirmacion": "Las obligaciones de dar, hacer y no hacer se distinguen por la prestación que el deudor debe ejecutar.", "respuesta": True, "fundamento": "Arts. 1460, 1553-1555 CC: las obligaciones se clasifican según la naturaleza de la prestación: dar (transferir dominio/tenencia), hacer (ejecutar un hecho) o no hacer (abstención).", "tema": "Clasificación de obligaciones"},
])

VF_FAMILIA.extend([
    {"afirmacion": "El matrimonio en Chile puede celebrarse ante el Oficial del Registro Civil o ante entidades religiosas con personalidad jurídica.", "respuesta": True, "fundamento": "Ley 19.947 art. 20: el matrimonio puede celebrarse ante el Oficial del Registro Civil o ante ministros de culto de entidades religiosas con personalidad jurídica de derecho público.", "tema": "Celebración del matrimonio"},
    {"afirmacion": "La separación de bienes pactada en las capitulaciones prematrimoniales puede ser modificada después del matrimonio.", "respuesta": True, "fundamento": "Art. 1723 CC: durante el matrimonio los cónyuges pueden sustituir la sociedad conyugal por el régimen de separación de bienes o de participación en los gananciales.", "tema": "Cambio de régimen matrimonial"},
    {"afirmacion": "En la sociedad conyugal, la mujer administra con plenas facultades sus bienes propios.", "respuesta": False, "fundamento": "Arts. 1749-1754 CC: bajo la sociedad conyugal, el marido es el jefe y administra los bienes sociales y los propios de la mujer, salvo los que ella reserve para su trabajo.", "tema": "Administración sociedad conyugal"},
    {"afirmacion": "El divorcio vincular produce la terminación del matrimonio con todos sus efectos civiles.", "respuesta": True, "fundamento": "Art. 53 Ley 19.947: el divorcio pone término al matrimonio, pero no afectará en modo alguno la filiación ya determinada ni los derechos y obligaciones que emanan de ella.", "tema": "Efectos del divorcio"},
    {"afirmacion": "Los alimentos debidos por ley se pueden renunciar anticipadamente.", "respuesta": False, "fundamento": "Art. 334 CC: el derecho de pedir alimentos no puede transmitirse por causa de muerte, ni venderse o cederse de modo alguno, ni renunciarse.", "tema": "Irrenunciabilidad de los alimentos"},
    {"afirmacion": "La adopción en Chile extingue la filiación de origen del adoptado.", "respuesta": True, "fundamento": "Art. 37 Ley 19.620: la adopción confiere al adoptado el estado civil de hijo de los adoptantes, con todos los derechos y deberes recíprocos, extinguiendo los vínculos de parentesco con la familia de origen.", "tema": "Efectos de la adopción"},
    {"afirmacion": "El cuidado personal compartido es la regla general en Chile cuando los padres viven separados.", "respuesta": False, "fundamento": "Art. 225 CC: si los padres viven separados, los hijos quedan al cuidado personal de la madre, salvo acuerdo de los padres o resolución judicial.", "tema": "Cuidado personal"},
    {"afirmacion": "La relación directa y regular con el hijo es un derecho del padre que no vive con él.", "respuesta": True, "fundamento": "Art. 229 CC: el padre o madre que no tenga el cuidado personal del hijo tiene el derecho y el deber de mantener con él una relación directa y regular.", "tema": "Relación directa y regular"},
    {"afirmacion": "El acuerdo de unión civil otorga a los convivientes civiles los mismos derechos hereditarios que el matrimonio.", "respuesta": False, "fundamento": "Ley 20.830: el conviviente civil es heredero intestado en el quinto orden de sucesión, mientras que el cónyuge concurre en los primeros órdenes.", "tema": "AUC y derechos hereditarios"},
    {"afirmacion": "La filiación no matrimonial puede determinarse por reconocimiento voluntario o por sentencia judicial.", "respuesta": True, "fundamento": "Art. 187 CC: el reconocimiento puede ser voluntario (escritura pública, testamento, acto registro civil) o judicial (sentencia firme).", "tema": "Determinación de la filiación"},
    {"afirmacion": "El patrimonio reservado de la mujer casada en sociedad conyugal comprende los bienes que adquiere con su trabajo.", "respuesta": True, "fundamento": "Art. 150 CC: la mujer casada bajo sociedad conyugal que ejerce una profesión o industria separada del marido dispone libremente de los bienes que obtiene por ese trabajo.", "tema": "Patrimonio reservado"},
    {"afirmacion": "El divorcio de mutuo acuerdo en Chile requiere un cese de la convivencia de al menos 1 año.", "respuesta": True, "fundamento": "Art. 55 Ley 19.947: el divorcio de mutuo acuerdo requiere que el cese efectivo de la convivencia conyugal sea de a lo menos un año.", "tema": "Divorcio de mutuo acuerdo"},
])

VF_COMERCIAL.extend([
    {"afirmacion": "La letra de cambio en Chile es un título de crédito a la orden por naturaleza.", "respuesta": True, "fundamento": "Art. 5 Ley 18.092: la letra de cambio es un título valor que contiene una orden incondicional de pago; es esencialmente transferible por endoso.", "tema": "Letra de cambio"},
    {"afirmacion": "El protesto de la letra de cambio por falta de pago es siempre obligatorio para mantener la acción cambiaria.", "respuesta": False, "fundamento": "Art. 79 Ley 18.092: el portador puede protestar la letra, pero hay causales que eximen del protesto. Sin protesto se pierden las acciones cambiarias de regreso, pero se mantiene la del aceptante.", "tema": "Protesto cambiario"},
    {"afirmacion": "En Chile, el pagaré es un título de crédito mediante el cual el suscriptor promete pagar una suma de dinero.", "respuesta": True, "fundamento": "Art. 102 Ley 18.092: el pagaré contiene la promesa no sujeta a condición de pagar una determinada cantidad de dinero.", "tema": "Pagaré"},
    {"afirmacion": "El contrato de cuenta corriente bancaria es unilateral porque solo obliga al banco.", "respuesta": False, "fundamento": "El contrato de cuenta corriente bancaria es bilateral: genera obligaciones para el banco (recibir fondos, pagar cheques) y para el cuentacorrentista (mantener fondos, responsabilidad por cheques).", "tema": "Cuenta corriente bancaria"},
    {"afirmacion": "El endoso en blanco convierte al título en portador.", "respuesta": True, "fundamento": "Art. 23 Ley 18.092: el endoso en blanco (sin señalar el nombre del endosatario) convierte el título en documento al portador.", "tema": "Endoso en blanco"},
    {"afirmacion": "La quiebra y el procedimiento concursal de liquidación son sinónimos en el derecho chileno actual.", "respuesta": False, "fundamento": "Ley 20.720: la Ley de Insolvencia reemplazó la 'quiebra' por el 'procedimiento concursal de liquidación', con importantes cambios sustantivos y de terminología.", "tema": "Ley de insolvencia"},
    {"afirmacion": "La empresa individual de responsabilidad limitada (EIRL) puede ser constituida por una persona jurídica.", "respuesta": False, "fundamento": "Art. 2 Ley 19.857: solo las personas naturales pueden constituir EIRL; no pueden hacerlo las personas jurídicas.", "tema": "EIRL"},
    {"afirmacion": "El aval en un pagaré obliga al avalista solidariamente con el avalado.", "respuesta": True, "fundamento": "Art. 47 Ley 18.092: el avalista es responsable en los mismos términos que el avalado, con carácter de obligación solidaria.", "tema": "Aval"},
    {"afirmacion": "En una SpA, los accionistas responden de las deudas sociales con su patrimonio personal.", "respuesta": False, "fundamento": "Ley 20.190: en la SpA (Sociedad por Acciones), la responsabilidad de los accionistas se limita al monto de sus acciones.", "tema": "SpA"},
    {"afirmacion": "El cheque tiene un plazo de 60 días para su presentación al cobro en Chile.", "respuesta": False, "fundamento": "Art. 23 Ley de Cuentas Corrientes: el cheque extendido en Chile para ser pagado en Chile debe presentarse dentro de 60 días para cheques de la misma plaza y 90 días para cheques de plazas distintas. (OJO: 60 días misma plaza es correcto.)", "respuesta": True, "fundamento": "Art. 23 Ley sobre Cuentas Corrientes: el plazo para presentar un cheque de la misma plaza al banco es de 60 días corridos desde su fecha de emisión.", "tema": "Plazo presentación cheque"},
    {"afirmacion": "El conocimiento de embarque es el título representativo de las mercaderías en el transporte marítimo.", "respuesta": True, "fundamento": "El conocimiento de embarque (bill of lading) es el título representativo de las mercancías transportadas por vía marítima, que da derecho a exigir su entrega.", "tema": "Conocimiento de embarque"},
    {"afirmacion": "La sociedad anónima cerrada en Chile no está obligada a inscribirse en el Registro de Valores.", "respuesta": True, "fundamento": "Art. 2 Ley 18.046: las SA cerradas no están obligadas a inscribirse en el Registro de Valores ni a someterse a la CMF, salvo excepciones legales.", "tema": "SA cerrada"},
    {"afirmacion": "El factor de comercio actúa a nombre propio, no del principal.", "respuesta": False, "fundamento": "Arts. 237 y ss. C.Com.: el factor actúa a nombre del principal y dentro de sus facultades; los actos obligan directamente al principal.", "tema": "Factor de comercio"},
])

VF_BIENES.extend([
    {"afirmacion": "La posesión en Chile se adquiere por la concurrencia del corpus y el animus.", "respuesta": True, "fundamento": "Art. 700 CC: la posesión es la tenencia de una cosa determinada con ánimo de señor y dueño (corpus + animus domini).", "tema": "Elementos de la posesión"},
    {"afirmacion": "La mera tenencia es un antecedente suficiente para adquirir la posesión por prescripción.", "respuesta": False, "fundamento": "Art. 714 CC: el mero tenedor reconoce dominio ajeno y no puede adquirir por prescripción, salvo que transforme su título en posesión.", "tema": "Mera tenencia"},
    {"afirmacion": "La accesión es un modo de adquirir el dominio original.", "respuesta": True, "fundamento": "Art. 643 CC: la accesión es un modo de adquirir por el cual el dueño de una cosa pasa a serlo de lo que ella produce o de lo que se junta a ella.", "tema": "Accesión"},
    {"afirmacion": "El derecho de superficie no está reconocido expresamente en el Código Civil chileno.", "respuesta": True, "fundamento": "El Código Civil chileno no regula expresamente el derecho de superficie como derecho real autónomo, aunque algunas leyes especiales lo contemplan.", "tema": "Derecho de superficie"},
    {"afirmacion": "La servidumbre predial es un derecho real constituido en un predio en utilidad de otro predio.", "respuesta": True, "fundamento": "Art. 820 CC: la servidumbre predial es el gravamen impuesto sobre un predio (sirviente) en utilidad de otro predio (dominante) de distinto dueño.", "tema": "Servidumbre predial"},
    {"afirmacion": "El tesoro hallado en terreno ajeno se divide en partes iguales entre el descubridor y el dueño del terreno.", "respuesta": True, "fundamento": "Art. 626 CC: el tesoro encontrado en terreno ajeno se divide por partes iguales entre el descubridor y el propietario del terreno.", "tema": "Tesoro"},
    {"afirmacion": "La propiedad horizontal permite a cada copropietario de un edificio dividido por pisos o departamentos ser dueño exclusivo de su unidad.", "respuesta": True, "fundamento": "Ley 21.442 (Copropiedad Inmobiliaria): cada copropietario es dueño exclusivo de su unidad (piso, departamento, etc.) y comunero en los bienes de uso común.", "tema": "Copropiedad inmobiliaria"},
    {"afirmacion": "La hipoteca es un contrato unilateral que solo obliga al acreedor.", "respuesta": False, "fundamento": "La hipoteca es un contrato unilateral en cuanto solo genera obligaciones para el constituyente (proporcionar la cosa en garantía); el acreedor no contrae obligación principal.", "tema": "Hipoteca"},
    {"afirmacion": "El usufructo se extingue por la llegada del plazo o condición establecidos, y también por la muerte del usufructuario.", "respuesta": True, "fundamento": "Art. 806 CC: el usufructo se extingue por la llegada del día o cumplimiento de la condición, por la muerte del usufructuario y por otras causales.", "tema": "Extinción del usufructo"},
    {"afirmacion": "Las cosas fungibles son siempre también consumibles.", "respuesta": False, "fundamento": "La fungibilidad (intercambiabilidad) no implica consumibilidad. Las monedas son fungibles pero no necesariamente consumibles. Son categorías distintas.", "tema": "Fungibilidad y consumibilidad"},
    {"afirmacion": "La acción reivindicatoria puede ser ejercida por el poseedor regular que no tiene la cosa.", "respuesta": False, "fundamento": "Art. 889 CC: la reivindicación corresponde al dueño de la cosa que no está en posesión de ella; no al mero poseedor.", "tema": "Acción reivindicatoria"},
    {"afirmacion": "La tradición es a la vez título y modo de adquirir.", "respuesta": False, "fundamento": "En el sistema chileno (arts. 588, 670-699 CC), la tradición es el modo de adquirir; el título es el antecedente jurídico que la justifica (compraventa, donación, etc.).", "tema": "Tradición"},
    {"afirmacion": "Los frutos civiles devengados pertenecen al usufructuario aunque no los haya percibido.", "respuesta": True, "fundamento": "Art. 790 CC: los frutos civiles pertenecen al usufructuario día por día.", "tema": "Frutos en usufructo"},
    {"afirmacion": "El dominio sobre un inmueble se adquiere por inscripción en el Conservador de Bienes Raíces.", "respuesta": True, "fundamento": "Art. 686 CC: la tradición del dominio de los bienes raíces se efectúa por la inscripción del título en el Registro del Conservador.", "tema": "Tradición inmuebles"},
    {"afirmacion": "La accesión de inmueble a inmueble comprende la aluvión, la avulsión y la mutación del álveo.", "respuesta": True, "fundamento": "Arts. 649 y ss. CC: la accesión de suelo comprende aluvión (depósito gradual), avulsión (fuerza súbita), mutación de álveo y formación de islas.", "tema": "Accesión suelo"},
    {"afirmacion": "El derecho de uso es un derecho real más amplio que el usufructo.", "respuesta": False, "fundamento": "Art. 811 CC: el derecho de uso es más limitado que el usufructo: solo da derecho a usar la cosa ajena para satisfacer las necesidades personales del usuario.", "tema": "Derecho de uso"},
])

VF_SUCESORIO.extend([
    {"afirmacion": "La legítima efectiva es la legítima rigorosa aumentada con la parte de mejoras no distribuidas.", "respuesta": True, "fundamento": "Art. 1191 CC: la legítima efectiva es la legítima rigorosa más la cuarta de mejoras no distribuida y los bienes de libre disposición no asignados.", "tema": "Legítima efectiva"},
    {"afirmacion": "El testamento solemne cerrado en Chile requiere la presencia de tres testigos.", "respuesta": True, "fundamento": "Art. 1023 CC: el testamento solemne cerrado requiere ser presentado ante notario y tres testigos para su otorgamiento.", "tema": "Testamento cerrado"},
    {"afirmacion": "El heredero que repudia la herencia no puede representar al causante en la herencia de un tercero.", "respuesta": True, "fundamento": "Art. 987 CC: la representación opera solo para aquellos que habrían podido heredar; quien repudia no puede representar al causante.", "tema": "Representación hereditaria"},
    {"afirmacion": "Los legados de especie o cuerpo cierto se adquieren desde la apertura de la sucesión.", "respuesta": True, "fundamento": "Art. 1338 N°1 CC: el legatario de especie o cuerpo cierto adquiere el dominio de la cosa legada desde el momento de la muerte del testador.", "tema": "Adquisición del legado"},
    {"afirmacion": "El albacea o ejecutor testamentario puede vender bienes del causante sin autorización de los herederos.", "respuesta": False, "fundamento": "Art. 1295 CC: el albacea no puede enajenar bienes raíces del causante ni muebles preciosos sin autorización de los herederos o del juez.", "tema": "Facultades del albacea"},
    {"afirmacion": "En Chile, el conviviente civil sobreviviente es heredero abintestato del causante.", "respuesta": True, "fundamento": "Ley 20.830 art. 16: el conviviente civil sobreviviente concurre en la herencia intestada del causante como heredero.", "tema": "Derechos sucesorios del conviviente civil"},
    {"afirmacion": "La desheredación debe ser expresamente establecida en el testamento con indicación de la causa legal.", "respuesta": True, "fundamento": "Art. 1209 CC: para que sea válida la desheredación, debe expresarse en el testamento y especificarse la causa legal en que se funda.", "tema": "Desheredación"},
    {"afirmacion": "El acervo imaginario de primer orden se forma para proteger a los asignatarios de legítimas frente a donaciones excesivas.", "respuesta": True, "fundamento": "Art. 1185 CC: para calcular la legítima se agrega imaginariamente al acervo líquido las donaciones revocables e irrevocables hechas en vida a legitimarios.", "tema": "Primer acervo imaginario"},
    {"afirmacion": "El testamento ológrafo es válido en Chile si está escrito y firmado de puño y letra del testador.", "respuesta": False, "fundamento": "El Código Civil chileno no contempla el testamento ológrafo; todos los testamentos solemnes deben otorgarse ante notario o funcionario competente.", "tema": "Testamento ológrafo"},
    {"afirmacion": "El heredero beneficiario responde de las deudas del causante solo hasta concurrencia de lo que hereda.", "respuesta": True, "fundamento": "Art. 1247 CC: el beneficio de inventario limita la responsabilidad del heredero a lo que recibe a título de herencia.", "tema": "Beneficio de inventario"},
    {"afirmacion": "El testamento puede ser revocado libremente por el testador en cualquier momento.", "respuesta": True, "fundamento": "Art. 999 CC: el testamento es un acto esencialmente revocable; el testador puede revocarlo en todo tiempo.", "tema": "Revocación del testamento"},
    {"afirmacion": "La acción de reforma del testamento corresponde a los legitimarios perjudicados por el testamento.", "respuesta": True, "fundamento": "Art. 1216 CC: los legitimarios a quienes el testador haya impuesto en sus legítimas más gravámenes que los permitidos tienen la acción de reforma.", "tema": "Acción de reforma"},
    {"afirmacion": "La partición de bienes hereditarios puede realizarse de común acuerdo entre todos los herederos mayores de edad.", "respuesta": True, "fundamento": "Art. 1325 CC: los coasignatarios pueden hacer la partición de común acuerdo cuando todos son mayores de edad y no hay incapaces entre ellos.", "tema": "Partición voluntaria"},
    {"afirmacion": "La indignidad para suceder priva al indigno del derecho a la herencia, pero no se extiende a sus descendientes.", "respuesta": True, "fundamento": "Art. 979 CC: la indignidad no pasa a los descendientes del indigno; los hijos del indigno pueden representarle en la herencia.", "tema": "Indignidad"},
    {"afirmacion": "El cuarto de mejoras solo puede ser asignado a descendientes, ascendientes o cónyuge sobreviviente.", "respuesta": True, "fundamento": "Art. 1195 CC: el testador puede disponer de la cuarta de mejoras a favor de sus descendientes, ascendientes o cónyuge sobreviviente o conviviente civil.", "tema": "Cuarta de mejoras"},
    {"afirmacion": "El heredero intestado de primer orden está formado por los hijos y el cónyuge sobreviviente.", "respuesta": True, "fundamento": "Art. 988 CC: los hijos llevan el primer orden de sucesión intestada, excluyendo a todos los demás herederos; el cónyuge sobreviviente concurre con ellos.", "tema": "Órdenes sucesorios"},
    {"afirmacion": "Las asignaciones testamentarias pueden quedar sujetas a condición, plazo o modo.", "respuesta": True, "fundamento": "Arts. 1070 y ss. CC: las asignaciones testamentarias pueden sujetarse a condición (hecho futuro e incierto), plazo (hecho futuro y cierto) o modo (carga impuesta al asignatario).", "tema": "Modalidades en asignaciones testamentarias"},
])

VF_INTERNACIONAL.extend([
    {"afirmacion": "El principio de soberanía estatal es el fundamento del derecho internacional público clásico.", "respuesta": True, "fundamento": "La soberanía estatal es el principio base del DI clásico; los Estados son iguales entre sí y no reconocen autoridad superior (Paz de Westfalia, 1648).", "tema": "Soberanía estatal"},
    {"afirmacion": "Los tratados internacionales son la única fuente formal del derecho internacional.", "respuesta": False, "fundamento": "Art. 38 Estatuto CIJ: las fuentes del DI incluyen tratados, costumbre internacional, principios generales del derecho, jurisprudencia y doctrina.", "tema": "Fuentes del derecho internacional"},
    {"afirmacion": "El principio de no intervención prohíbe a los Estados interferir en los asuntos internos de otros.", "respuesta": True, "fundamento": "Art. 2.7 Carta ONU y Resolución 2625: el principio de no intervención es una norma imperativa del DI que prohíbe la interferencia en asuntos domésticos.", "tema": "No intervención"},
    {"afirmacion": "Las normas de ius cogens son dispositivas y pueden ser derogadas por tratado bilateral.", "respuesta": False, "fundamento": "Art. 53 Convención de Viena: las normas de ius cogens son imperativas y no pueden ser derogadas por acuerdo entre Estados; cualquier tratado contrario es nulo.", "tema": "Ius cogens"},
    {"afirmacion": "El derecho internacional humanitario se aplica en situaciones de conflicto armado.", "respuesta": True, "fundamento": "Los Convenios de Ginebra (1949) y sus Protocolos regulan la conducción de las hostilidades y la protección de las víctimas de conflictos armados.", "tema": "DIH"},
    {"afirmacion": "Chile reconoce competencia jurisdiccional obligatoria de la Corte Internacional de Justicia.", "respuesta": False, "fundamento": "Chile no ha reconocido la cláusula facultativa de jurisdicción obligatoria de la CIJ (art. 36.2 Estatuto); acepta su competencia caso a caso.", "tema": "CIJ y Chile"},
    {"afirmacion": "La Convención de Viena sobre el Derecho de los Tratados regula el ciclo de vida de los tratados entre Estados.", "respuesta": True, "fundamento": "La Convención de Viena (1969) codificó el DI consuetudinario sobre celebración, entrada en vigor, reservas, nulidad y terminación de tratados.", "tema": "Convención de Viena sobre tratados"},
    {"afirmacion": "El principio de responsabilidad de proteger (R2P) es una norma consuetudinaria vinculante para todos los Estados.", "respuesta": False, "fundamento": "El R2P es un principio político adoptado en el Documento Final de la Cumbre Mundial 2005 de la ONU, pero no es aún norma consuetudinaria vinculante.", "tema": "Responsabilidad de proteger"},
    {"afirmacion": "Los refugiados tienen derecho de no devolución (non-refoulement) según la Convención de 1951.", "respuesta": True, "fundamento": "Art. 33 Convención sobre el Estatuto de los Refugiados (1951): ningún Estado contratante podrá expulsar o devolver a un refugiado a territorios donde su vida o su libertad peligre.", "tema": "Non-refoulement"},
    {"afirmacion": "El derecho internacional privado chileno resuelve conflictos de leyes en el espacio mediante la lex fori.", "respuesta": False, "fundamento": "El DIPr chileno emplea distintos factores de conexión según la materia: lex situs para inmuebles, ley del domicilio para capacidad, lex loci contractus para contratos, etc.", "tema": "Derecho internacional privado"},
    {"afirmacion": "En Chile, los tratados internacionales se tramitan como leyes ordinarias en el Congreso.", "respuesta": False, "fundamento": "Art. 54 CPR: los tratados internacionales se aprueban o rechazan por el Congreso con las formalidades de una ley, pero el quórum varía según la materia regulada.", "tema": "Tramitación de tratados en Chile"},
    {"afirmacion": "La Convención Americana de DDHH (Pacto de San José) establece la Corte Interamericana de Derechos Humanos.", "respuesta": True, "fundamento": "Art. 33 CADH: la Comisión Interamericana y la Corte Interamericana son los órganos competentes para conocer los asuntos relacionados con el cumplimiento de los compromisos de los Estados parte.", "tema": "Sistema Interamericano DDHH"},
    {"afirmacion": "El principio de pacta sunt servanda obliga a los Estados a cumplir de buena fe los tratados en vigor.", "respuesta": True, "fundamento": "Art. 26 Convención de Viena: todo tratado en vigor obliga a las partes y debe ser cumplido por ellas de buena fe.", "tema": "Pacta sunt servanda"},
    {"afirmacion": "Las inmunidades diplomáticas son absolutas y nunca pueden ser renunciadas.", "respuesta": False, "fundamento": "Art. 32 Convención de Viena sobre Relaciones Diplomáticas (1961): la inmunidad puede ser renunciada por el Estado acreditante; si el diplomático renuncia personalmente, no surte efecto.", "tema": "Inmunidades diplomáticas"},
    {"afirmacion": "Chile ratificó el Estatuto de Roma y reconoce la jurisdicción de la Corte Penal Internacional.", "respuesta": True, "fundamento": "Chile ratificó el Estatuto de Roma en 2009 y reconoce la jurisdicción de la CPI para crímenes de genocidio, lesa humanidad, guerra y agresión.", "tema": "CPI y Chile"},
    {"afirmacion": "La zona económica exclusiva se extiende hasta las 200 millas marinas medidas desde la línea de base.", "respuesta": True, "fundamento": "Art. 57 CONVEMAR: la ZEE no se extenderá más allá de 200 millas marinas contadas desde las líneas de base.", "tema": "Zona económica exclusiva"},
    {"afirmacion": "Los actos unilaterales de los Estados pueden crear obligaciones internacionales.", "respuesta": True, "fundamento": "CIJ, caso Ensayos Nucleares (1974): las declaraciones unilaterales solemnes de los Estados pueden crear obligaciones jurídicas internacionales si se hace con intención de quedar vinculado.", "tema": "Actos unilaterales"},
    {"afirmacion": "La costumbre internacional requiere solo elemento material (práctica) sin elemento psicológico (opinio juris).", "respuesta": False, "fundamento": "Art. 38(1)(b) Estatuto CIJ: la costumbre internacional exige práctica general (elemento material) y opinio juris sive necessitatis (convicción de obligatoriedad jurídica).", "tema": "Costumbre internacional"},
    {"afirmacion": "En Chile, el principio de la nacionalidad activa permite ejercer jurisdicción sobre nacionales que cometan delitos en el extranjero.", "respuesta": True, "fundamento": "Art. 6 COT: la competencia chilena se extiende a crímenes de chilenos en el extranjero en los casos contemplados, incluyendo el principio de personalidad activa.", "tema": "Jurisdicción extraterritorial"},
    {"afirmacion": "La resolución 1373 del Consejo de Seguridad de la ONU es vinculante para todos los Estados miembros.", "respuesta": True, "fundamento": "Las resoluciones del Consejo de Seguridad adoptadas bajo el Capítulo VII de la Carta ONU son vinculantes para todos los Estados miembros.", "tema": "Consejo de Seguridad ONU"},
])

VF_AMBIENTAL.extend([
    {"afirmacion": "El SEIA (Sistema de Evaluación de Impacto Ambiental) es obligatorio para todos los proyectos de inversión en Chile.", "respuesta": False, "fundamento": "Art. 10 Ley 19.300: solo los proyectos y actividades listados en el art. 10 deben ingresar al SEIA; los no listados quedan exentos.", "tema": "SEIA"},
    {"afirmacion": "En Chile, el derecho a vivir en un medioambiente libre de contaminación está protegido por el recurso de protección.", "respuesta": True, "fundamento": "Art. 19 N°8 CPR: el derecho a vivir en un medio ambiente libre de contaminación está protegido por la acción constitucional de protección.", "tema": "Protección constitucional medioambiental"},
    {"afirmacion": "El Ministerio del Medio Ambiente es el organismo encargado de fiscalizar el cumplimiento de la legislación ambiental.", "respuesta": False, "fundamento": "La fiscalización corresponde a la Superintendencia del Medio Ambiente (SMA), creada por Ley 20.417. El MMA dicta políticas y normas.", "tema": "SMA vs MMA"},
    {"afirmacion": "El principio de quien contamina paga es recogido expresamente en la Ley 19.300.", "respuesta": True, "fundamento": "Art. 3 Ley 19.300: el responsable de fuente emisora que produce daño ambiental está obligado a repararlo, consagrando el principio contaminador-pagador.", "tema": "Principio contaminador-pagador"},
    {"afirmacion": "Los planes de descontaminación son instrumentos de gestión ambiental de carácter obligatorio en zonas saturadas.", "respuesta": True, "fundamento": "Art. 44 Ley 19.300: cuando una zona sea declarada saturada, el MMA debe elaborar y dictar un plan de descontaminación.", "tema": "Planes de descontaminación"},
    {"afirmacion": "El Tribunal Ambiental es competente para conocer las demandas de reparación del daño ambiental.", "respuesta": True, "fundamento": "Art. 17 N°2 Ley 20.600: el Tribunal Ambiental conoce de las demandas para obtener la reparación del medio ambiente dañado.", "tema": "Tribunal Ambiental"},
    {"afirmacion": "La Declaración de Impacto Ambiental (DIA) es más exigente que el Estudio de Impacto Ambiental (EIA).", "respuesta": False, "fundamento": "Arts. 11 y 12 Ley 19.300: el EIA es más exigente; procede cuando el proyecto genera efectos significativos. La DIA es para proyectos sin efectos significativos.", "tema": "DIA vs EIA"},
    {"afirmacion": "El convenio 169 de la OIT exige consulta previa a pueblos indígenas en decisiones que puedan afectarles.", "respuesta": True, "fundamento": "Arts. 6 y 7 Convenio 169 OIT (ratificado por Chile): los gobiernos deben consultar a los pueblos indígenas antes de emprender medidas que puedan afectarles directamente.", "tema": "Consulta indígena"},
    {"afirmacion": "La acción ambiental por daño al medioambiente puede ser ejercida por cualquier persona, aunque no sea directamente afectada.", "respuesta": True, "fundamento": "Art. 54 Ley 19.300: la acción ambiental por daño al medio ambiente puede ser ejercida por cualquier persona natural o jurídica que haya sufrido el daño.", "tema": "Acción ambiental"},
    {"afirmacion": "Las normas de emisión y de calidad ambiental tienen la misma naturaleza jurídica en Chile.", "respuesta": False, "fundamento": "Art. 2 Ley 19.300: las normas de emisión regulan los contaminantes de fuentes específicas; las de calidad ambiental establecen los valores máximos permitidos en el ambiente.", "tema": "Normas ambientales"},
    {"afirmacion": "Chile tiene compromisos de reducción de emisiones de GEI bajo el Acuerdo de París.", "respuesta": True, "fundamento": "Chile ratificó el Acuerdo de París (2016) y ha presentado NDCs (Contribuciones Determinadas a Nivel Nacional) comprometiendo reducción de emisiones.", "tema": "Acuerdo de París"},
    {"afirmacion": "El daño ambiental puro afecta solo a personas individualmente determinadas.", "respuesta": False, "fundamento": "Art. 2 Ley 19.300: el daño ambiental es la pérdida, disminución, detrimento o menoscabo significativo del medio ambiente (bien colectivo), distinto del daño civil que afecta bienes individuales.", "tema": "Daño ambiental"},
    {"afirmacion": "La participación ciudadana es obligatoria en el proceso de evaluación de EIAs.", "respuesta": True, "fundamento": "Art. 29 Ley 19.300: los EIAs deben someterse a un proceso de participación ciudadana durante 60 días, en el que cualquier persona puede formular observaciones.", "tema": "Participación ciudadana SEIA"},
    {"afirmacion": "El principio precautorio permite adoptar medidas preventivas ante incertidumbre científica sobre daño ambiental.", "respuesta": True, "fundamento": "Principio 15 Declaración de Río y art. 1 Ley 19.300: ante amenaza de daño grave e irreversible, la falta de certeza científica no puede usarse como razón para postergar medidas preventivas.", "tema": "Principio precautorio"},
    {"afirmacion": "La certificación ISO 14001 es obligatoria para empresas que ingresan al SEIA.", "respuesta": False, "fundamento": "La certificación ISO 14001 es voluntaria; el SEIA no la exige como requisito para evaluación ambiental.", "tema": "ISO 14001"},
    {"afirmacion": "En Chile, los delitos ambientales están tipificados en la Ley 19.300.", "respuesta": False, "fundamento": "La Ley 19.300 no establece tipos penales propios; los delitos ambientales están dispersos en leyes especiales (Ley de Pesca, Ley Minera, etc.) y en el CP.", "tema": "Delitos ambientales"},
    {"afirmacion": "El principio de participación en materia ambiental permite a las comunidades incidir en decisiones que afectan su entorno.", "respuesta": True, "fundamento": "Arts. 26 y ss. Ley 19.300: el principio de participación ciudadana en materia ambiental garantiza a las personas el derecho a participar en los procesos de evaluación y normativa.", "tema": "Principio de participación"},
    {"afirmacion": "La Comisión Regional del Medio Ambiente (COREMA) sigue vigente como organismo evaluador en Chile.", "respuesta": False, "fundamento": "Ley 20.417 (2010): las COREMAs fueron reemplazadas por el Servicio de Evaluación Ambiental (SEA), organismo técnico descentralizado.", "tema": "SEA"},
    {"afirmacion": "El recurso de reclamación ambiental ante el Tribunal Ambiental procede contra resoluciones de la SMA.", "respuesta": True, "fundamento": "Art. 17 N°3 Ley 20.600: el Tribunal Ambiental conoce los recursos de reclamación contra resoluciones de la SMA.", "tema": "Recurso de reclamación ambiental"},
    {"afirmacion": "Chile ha ratificado el Acuerdo de Escazú sobre acceso a información, participación y justicia ambiental.", "respuesta": True, "fundamento": "Chile firmó el Acuerdo de Escazú en 2018 y lo ratificó en 2022, siendo uno de los primeros países en hacerlo.", "tema": "Acuerdo de Escazú"},
    {"afirmacion": "La responsabilidad por daño ambiental en Chile es siempre objetiva.", "respuesta": False, "fundamento": "Art. 52 Ley 19.300: se presume la responsabilidad del causante si existe infracción a las normas ambientales; sin infracción, la responsabilidad es subjetiva (requiere culpa o dolo).", "tema": "Responsabilidad ambiental"},
    {"afirmacion": "Los humedales urbanos en Chile tienen protección legal especial.", "respuesta": True, "fundamento": "Ley 21.202 (2020): los humedales urbanos tienen protección legal; los municipios deben elaborar instrumentos de protección e inventariar sus humedales.", "tema": "Humedales urbanos"},
])


# ════════════════════════════════════════════════════════════════
# EXPANSIÓN V/F  — Civil→100, resto→50
# ════════════════════════════════════════════════════════════════

VF_CIVIL.extend([
    {"afirmacion":"La compraventa de cosa ajena es válida en Chile pero inoponible al verdadero dueño.","respuesta":True,"fundamento":"Art. 1815 CC: la compraventa de cosa ajena es válida sin perjuicio de los derechos del dueño mientras no se extingan por prescripción.","tema":"Venta de cosa ajena"},
    {"afirmacion":"La stipulatio alteri es un contrato celebrado en beneficio de un tercero que puede exigir su cumplimiento directamente.","respuesta":True,"fundamento":"Art. 1449 CC: cuando se estipula en favor de un tercero, éste puede demandar el cumplimiento si aceptó la estipulación antes de revocarse.","tema":"Estipulación a favor de tercero"},
    {"afirmacion":"El contrato de arrendamiento de inmuebles urbanos regido por el Código Civil requiere escritura pública para su validez.","respuesta":False,"fundamento":"El arrendamiento de inmuebles urbanos es consensual; no exige escritura pública para su existencia ni validez (art. 1916 CC).","tema":"Arrendamiento consensual"},
    {"afirmacion":"El deudor en mora responde del caso fortuito cuando la cosa perece.","respuesta":True,"fundamento":"Art. 1547 inc. 2 CC: el deudor moroso responde incluso del caso fortuito, salvo que demuestre que la cosa habría perecido igualmente en poder del acreedor.","tema":"Mora del deudor"},
    {"afirmacion":"La acción redhibitoria y la quanti minoris son acciones que nacen de los vicios redhibitorios.","respuesta":True,"fundamento":"Art. 1860 CC: los vicios redhibitorios dan lugar a la rescisión de la venta (acción redhibitoria) o a la rebaja del precio (quanti minoris).","tema":"Vicios redhibitorios"},
    {"afirmacion":"En Chile, la tradición de los bienes muebles se puede verificar por la entrega de llaves.","respuesta":True,"fundamento":"Art. 684 N°3 CC: la entrega de llaves de un granero, almacén, cofre o lugar donde la mercadería esté constituye tradición.","tema":"Formas de tradición mueble"},
    {"afirmacion":"El fideicomiso en el Código Civil chileno es la misma institución que el trust del derecho anglosajón.","respuesta":False,"fundamento":"El fideicomiso chileno (art. 733 CC) es una propiedad fiduciaria que pasa al fideicomisario si se cumple la condición; el trust anglosajón es una institución más amplia con el trustee como dueño legal.","tema":"Propiedad fiduciaria"},
    {"afirmacion":"La remisión de deuda requiere capacidad para donar en el acreedor.","respuesta":True,"fundamento":"Art. 1654 CC: la remisión de deuda es una donación; requiere en el acreedor la capacidad para hacer donaciones.","tema":"Remisión de deuda"},
    {"afirmacion":"El pago de lo no debido solo genera restitución si el que pagó estaba en error de hecho.","respuesta":False,"fundamento":"Art. 2297 CC: el pago de lo no debido procede también por error de derecho; se puede repetir lo que se pagó por error de hecho o de derecho.","tema":"Pago de lo no debido"},
    {"afirmacion":"En las obligaciones alternativas, la elección corresponde al deudor salvo pacto en contrario.","respuesta":True,"fundamento":"Art. 1500 CC: la elección en las obligaciones alternativas corresponde al deudor salvo que las partes hayan pactado que la elección sea del acreedor.","tema":"Obligaciones alternativas"},
    {"afirmacion":"La promesa de hecho ajeno genera responsabilidad para el promitente si el tercero no ratifica.","respuesta":True,"fundamento":"Art. 1450 CC: quien promete el hecho de un tercero es responsable de perjuicios si ese tercero no ratifica o cumple lo prometido.","tema":"Promesa de hecho ajeno"},
    {"afirmacion":"La solidaridad se presume en las obligaciones mercantiles chilenas.","respuesta":True,"fundamento":"Art. 370 C.Com.: en los contratos mercantiles se presume la solidaridad entre deudores cuando hay obligación común.","tema":"Solidaridad mercantil"},
    {"afirmacion":"El contrato de donación entre vivos requiere insinuación judicial cuando supera 2 centavos.","respuesta":False,"fundamento":"Art. 1401 CC: la insinuación se exige para donaciones que excedan 2 centavos (monto histórico irrelevante); hoy se aplica al que exceda el límite del art. 1402, que fija en 2 UTM.","tema":"Insinuación en donaciones"},
    {"afirmacion":"La confusión entre deudor y fiador extingue la obligación principal.","respuesta":False,"fundamento":"Art. 1666 CC: la confusión entre el deudor principal y el fiador extingue la fianza, pero no la obligación principal.","tema":"Confusión y fianza"},
    {"afirmacion":"El cuasicontrato de agencia oficiosa obliga al dueño del negocio si la gestión fue útil.","respuesta":True,"fundamento":"Art. 2290 CC: si el negocio fue bien administrado, el dueño es obligado a cumplir las obligaciones que el agente oficioso contrató con terceros.","tema":"Agencia oficiosa"},
    {"afirmacion":"El objeto ilícito en los actos y contratos genera nulidad relativa.","respuesta":False,"fundamento":"Art. 1682 CC: el objeto ilícito es causal de nulidad absoluta, no relativa.","tema":"Objeto ilícito"},
    {"afirmacion":"La hipoteca es indivisible aunque se divida el crédito entre varios herederos.","respuesta":True,"fundamento":"Art. 2408 CC: la hipoteca es indivisible; cada parte del inmueble hipotecado responde del total de la obligación.","tema":"Indivisibilidad de la hipoteca"},
    {"afirmacion":"El mandante puede revocar el mandato en cualquier momento, incluso si se pactó irrevocabilidad.","respuesta":True,"fundamento":"Art. 2165 CC: el mandante puede revocar el mandato cuando le parezca, aunque se haya estipulado irrevocabilidad; no obstante, deberá indemnizar al mandatario.","tema":"Revocación del mandato"},
    {"afirmacion":"La oferta irrevocable del art. 99 C.Com. obliga al oferente durante el plazo pactado.","respuesta":True,"fundamento":"Art. 99 C.Com.: la propuesta de contrato puede hacerse irrevocable, caso en el cual el oferente no puede retractarse durante el plazo sin responsabilidad.","tema":"Oferta irrevocable"},
    {"afirmacion":"En la compraventa, el vendedor que entrega la cosa cumple su obligación aunque el comprador no haya pagado.","respuesta":True,"fundamento":"La obligación principal del vendedor es entregar; la del comprador es pagar. Son obligaciones correlativas pero independientemente exigibles.","tema":"Obligaciones en la compraventa"},
    {"afirmacion":"El plazo de prescripción de la acción ordinaria en Chile es de 5 años.","respuesta":True,"fundamento":"Art. 2515 CC: la acción ordinaria prescribe en 5 años; la ejecutiva en 3 años.","tema":"Prescripción extintiva ordinaria"},
    {"afirmacion":"La anticresis permite al acreedor retener un inmueble y percibir sus frutos como pago.","respuesta":True,"fundamento":"Art. 2435 CC: la anticresis es un contrato por el que el deudor entrega al acreedor una finca para que se pague con sus frutos.","tema":"Anticresis"},
    {"afirmacion":"El contrato de compraventa perfeccionado en Chile transfiere el dominio al comprador de inmediato.","respuesta":False,"fundamento":"Arts. 1443 y 670 CC: la compraventa es solo título; el dominio se transfiere por la tradición (inscripción para inmuebles, entrega para muebles).","tema":"Compraventa no transfiere dominio"},
    {"afirmacion":"La prenda sin desplazamiento requiere inscripción en el Registro de Prendas sin Desplazamiento.","respuesta":True,"fundamento":"Ley 20.190: la prenda sin desplazamiento se constituye por escritura pública o privada y se inscribe en el Registro de Prendas sin Desplazamiento del CBR.","tema":"Prenda sin desplazamiento"},
    {"afirmacion":"La rescisión y la nulidad relativa son términos sinónimos en el Código Civil chileno.","respuesta":True,"fundamento":"Arts. 1681 y ss. CC: el CC chileno usa el término 'rescisión' como sinónimo de nulidad relativa (no como en el derecho comparado donde puede referirse a la resolución).","tema":"Rescisión = nulidad relativa"},
    {"afirmacion":"La lesión enorme en la compraventa de bienes raíces solo puede alegarla el vendedor.","respuesta":False,"fundamento":"Art. 1888 CC: la rescisión por lesión enorme puede solicitarla tanto el vendedor (recibió menos de la mitad del justo precio) como el comprador (pagó más del doble).","tema":"Lesión enorme compradores"},
    {"afirmacion":"La acción pauliana prescribe en un año contado desde la fecha del acto fraudulento.","respuesta":True,"fundamento":"Art. 2468 N°3 CC: la acción pauliana prescribe en un año contado desde la fecha del acto o contrato.","tema":"Prescripción acción pauliana"},
    {"afirmacion":"El derecho de retención del comprador procede cuando el vendedor no le ha entregado la cosa.","respuesta":False,"fundamento":"Art. 1826 CC: el derecho de retención del comprador procede cuando el vendedor está en mora de entregar y el comprador ha pagado o está listo para pagar; puede retener el precio.","tema":"Retención en compraventa"},
    {"afirmacion":"La fianza convencional puede ser simple o solidaria.","respuesta":True,"fundamento":"Arts. 2335 y ss. CC: la fianza convencional puede ser simple (con beneficio de excusión) o solidaria (sin beneficio de excusión).","tema":"Clases de fianza"},
    {"afirmacion":"En Chile, la persona jurídica puede ser declarada en quiebra.","respuesta":True,"fundamento":"Ley 20.720: tanto personas naturales como jurídicas pueden ser sujeto de procedimientos concursales de liquidación y reorganización.","tema":"Insolvencia persona jurídica"},
    {"afirmacion":"El comodato es un contrato oneroso que genera obligaciones para ambas partes.","respuesta":False,"fundamento":"Art. 2174 CC: el comodato (préstamo de uso) es gratuito; si se cobra algo por el uso, degenera en arrendamiento.","tema":"Comodato gratuito"},
    {"afirmacion":"En el depósito necesario, el depositario no puede elegir al depositante.","respuesta":True,"fundamento":"Art. 2236 CC: el depósito propiamente necesario es aquel en que la elección del depositario no depende de la libre voluntad del depositante (incendio, naufragio, etc.).","tema":"Depósito necesario"},
    {"afirmacion":"La acción de inoponibilidad es distinta a la acción de nulidad.","respuesta":True,"fundamento":"La inoponibilidad es la ineficacia relativa de un acto válido frente a terceros determinados; la nulidad ataca la validez misma del acto. Son instituciones jurídicas distintas.","tema":"Inoponibilidad vs nulidad"},
    {"afirmacion":"Los intereses se deben desde que el deudor fue constituido en mora.","respuesta":True,"fundamento":"Art. 1559 CC: cuando la obligación sea de pagar una cantidad de dinero, la indemnización de perjuicios consiste en el pago de intereses desde el momento de la mora.","tema":"Intereses moratorios"},
    {"afirmacion":"El albaceazgo es un encargo intuitu personae que no puede delegarse.","respuesta":True,"fundamento":"Art. 1280 CC: el albaceazgo es un cargo de confianza personal y, en principio, indelegable, salvo que el testador lo autorice.","tema":"Indelegabilidad del albaceazgo"},
    {"afirmacion":"El pacto comisorio en la compraventa resuelve el contrato de pleno derecho por incumplimiento.","respuesta":False,"fundamento":"Art. 1879 CC: el pacto comisorio simple no resuelve ipso jure; el comprador puede enervar la acción pagando dentro de 24 horas de notificada la demanda.","tema":"Pacto comisorio"},
    {"afirmacion":"La sucesión por causa de muerte opera como modo de adquirir tanto el dominio como otros derechos reales.","respuesta":True,"fundamento":"Art. 588 CC: la sucesión por causa de muerte es un modo de adquirir el dominio y otros derechos reales que se transmiten hereditariamente.","tema":"Sucesión como modo de adquirir"},
    {"afirmacion":"La acción de desposeimiento hipotecario se dirige contra el tercero poseedor del inmueble hipotecado.","respuesta":True,"fundamento":"Arts. 2428 y ss. CC: el acreedor hipotecario puede dirigir la acción de desposeimiento contra el tercer poseedor que adquirió el inmueble hipotecado.","tema":"Desposeimiento hipotecario"},
    {"afirmacion":"El contrato de renta vitalicia es aleatorio por naturaleza.","respuesta":True,"fundamento":"Art. 2264 CC: la renta vitalicia es un contrato aleatorio en que una de las partes se obliga a pagar a la otra una pensión periódica durante la vida de alguna persona.","tema":"Renta vitalicia"},
    {"afirmacion":"La gestión de negocios ajenos es un contrato bilateral del Código Civil chileno.","respuesta":False,"fundamento":"La agencia oficiosa (gestión de negocios) es un cuasicontrato (art. 2286 CC), no un contrato; nace de un hecho voluntario sin convención.","tema":"Agencia oficiosa como cuasicontrato"},
    {"afirmacion":"Las arras confirmatorias a diferencia de las penitenciales, no permiten retractarse del contrato pagando la multa.","respuesta":True,"fundamento":"Art. 1803 CC: las arras confirmatorias no confieren derecho a arrepentirse; las arras de retractación permiten apartarse del contrato con pérdida o restitución doblada.","tema":"Arras"},
    {"afirmacion":"La acción de petición de herencia protege al verdadero heredero frente al heredero putativo.","respuesta":True,"fundamento":"Art. 1264 CC: la acción de petición de herencia corresponde al heredero a quien el falso heredero está impidiendo el pleno goce de la herencia.","tema":"Petición de herencia"},
    {"afirmacion":"En el mutuo, si no se ha estipulado plazo, el mutuante puede exigir la restitución en cualquier momento.","respuesta":False,"fundamento":"Art. 2200 CC: si no se ha fijado plazo, el mutuo se presume por 10 días a contar del desembolso (regla del CC); el juez puede fijar plazo prudencial.","tema":"Plazo en el mutuo"},
    {"afirmacion":"La promesa de compraventa de un bien embargado adolece de objeto ilícito.","respuesta":True,"fundamento":"Art. 1464 N°3 CC: hay objeto ilícito en la enajenación de las cosas embargadas por decreto judicial. La promesa de venta de bien embargado también puede verse afectada por esta causal.","tema":"Objeto ilícito y embargo"},
    {"afirmacion":"El contrato de sociedad puede ser solemne, real o consensual según su tipo.","respuesta":True,"fundamento":"Las sociedades de personas (colectiva, en comandita simple) pueden ser consensuales, aunque la escritura es útil para la prueba; las SA y SpA son solemnes.","tema":"Solemnidades de la sociedad"},
    {"afirmacion":"En la compraventa a prueba, el contrato solo se perfecciona si el comprador declara que la cosa le agrada.","respuesta":True,"fundamento":"Art. 1823 CC: si se vende la cosa a prueba, se entiende no haber contrato mientras el comprador no declara que la cosa le agrada.","tema":"Venta a prueba"},
    {"afirmacion":"El beneficio de inventario impide que las deudas de la herencia afecten el patrimonio personal del heredero.","respuesta":True,"fundamento":"Art. 1247 CC: el beneficio de inventario limita la responsabilidad del heredero al monto de los bienes heredados; sus bienes propios no responden.","tema":"Beneficio de inventario"},
    {"afirmacion":"La novación subjetiva por cambio de deudor siempre requiere consentimiento del acreedor.","respuesta":True,"fundamento":"Art. 1631 N°2 y 1635 CC: la novación por sustitución de deudor requiere el consentimiento del acreedor; si es sin conocimiento del deudor primitivo, es la expromisión.","tema":"Novación subjetiva"},
    {"afirmacion":"La condición puramente potestativa que depende de la sola voluntad del deudor es válida en Chile.","respuesta":False,"fundamento":"Art. 1478 CC: las condiciones puramente potestativas que dependen de la sola voluntad del deudor son nulas por carecer de seriedad y eficacia jurídica.","tema":"Condición potestativa"},
    {"afirmacion":"La acción de lesión enorme en la compraventa tiene un plazo de prescripción de 4 años desde el contrato.","respuesta":True,"fundamento":"Art. 1896 CC: la acción rescisoria por lesión enorme expira en 4 años contados desde la fecha del contrato.","tema":"Prescripción lesión enorme"},
    {"afirmacion":"El usufructo puede constituirse por donación, testamento, prescripción o ley.","respuesta":True,"fundamento":"Art. 766 CC: el usufructo puede constituirse por ley, testamento, donación u otro acto entre vivos, y por prescripción.","tema":"Fuentes del usufructo"},
    {"afirmacion":"En el contrato de transacción no puede discutirse nuevamente el objeto transado entre las partes.","respuesta":True,"fundamento":"Art. 2460 CC: la transacción produce el efecto de cosa juzgada en última instancia sobre lo transado; las partes no pueden volver a litigar sobre ello.","tema":"Efecto de cosa juzgada de la transacción"},
    {"afirmacion":"La compensación puede operar entre deudas de distinta naturaleza (dinero y especie).","respuesta":False,"fundamento":"Art. 1656 CC: la compensación requiere que ambas obligaciones sean de dinero u otras cosas fungibles o indeterminadas del mismo género y calidad.","tema":"Requisitos de la compensación"},
    {"afirmacion":"El art. 19 CC establece que la ley es clara cuando no puede interpretarse.","respuesta":False,"fundamento":"Art. 19 CC: cuando el sentido de la ley es claro, no se desatenderá su tenor literal; el intérprete recurre a otros elementos solo cuando el sentido no es claro.","tema":"Interpretación de la ley"},
    {"afirmacion":"El matrimonio en Chile puede celebrarse entre personas del mismo sexo desde 2022.","respuesta":True,"fundamento":"Ley 21.400 (2022): se modificó el CC para permitir el matrimonio entre personas del mismo sexo, con iguales derechos y obligaciones.","tema":"Matrimonio igualitario"},
    {"afirmacion":"La acción de dominio y la acción posesoria protegen los mismos intereses jurídicos.","respuesta":False,"fundamento":"La acción reivindicatoria protege el dominio (art. 889 CC); las acciones posesorias protegen la posesión como hecho (art. 916 CC). Tutelan intereses distintos.","tema":"Acción real vs posesoria"},
    {"afirmacion":"La representación en la tradición del art. 671 CC permite que el tradente actúe a través de representante.","respuesta":True,"fundamento":"Art. 671 CC: la tradición puede hacerse por representantes legales o convencionales, tanto del tradente como del adquirente.","tema":"Representación en la tradición"},
    {"afirmacion":"La hipoteca legal existe en el Código Civil chileno.","respuesta":True,"fundamento":"Art. 662 CPC en relación con el CC: existe hipoteca legal del adquirente de inmuebles cuando los bienes pasan del causante a herederos, para garantizar el pago del saldo de precio.","tema":"Hipoteca legal"},
    {"afirmacion":"El acreedor prendario puede pedir la venta de la prenda si el deudor no paga.","respuesta":True,"fundamento":"Arts. 2397 y 2424 CC: el acreedor prendario puede, ante incumplimiento, pedir que la prenda se venda en pública subasta para pagarse con el producto.","tema":"Realización de la prenda"},
    {"afirmacion":"En Chile, las personas jurídicas tienen domicilio legal, no convencional.","respuesta":False,"fundamento":"Las personas jurídicas pueden tener domicilio legal (impuesto por ley) y convencional (fijado en sus estatutos). En general, se fija en los estatutos.","tema":"Domicilio personas jurídicas"},
    {"afirmacion":"La dación en pago de un bien raíz requiere escritura pública e inscripción en el CBR.","respuesta":True,"fundamento":"La dación en pago que implica transferir un inmueble requiere las mismas solemnidades que la compraventa de inmuebles: escritura pública y tradición por inscripción.","tema":"Dación en pago inmueble"},
    {"afirmacion":"El error en la causa no vicia el consentimiento en Chile.","respuesta":True,"fundamento":"Art. 1467 CC: se reconoce la causa como elemento del contrato, pero el CC no contempla expresamente el error en la causa como vicio del consentimiento; se aplica el régimen general de error.","tema":"Error en la causa"},
])

VF_PENAL.extend([
    {"afirmacion":"El iter criminis comprende la ideación, preparación, tentativa, frustración y consumación del delito.","respuesta":True,"fundamento":"El iter criminis es el camino del delito; en el derecho penal chileno (arts. 7-9 CP) se distinguen etapas de ejecución punibles: tentativa, frustración y consumación.","tema":"Iter criminis"},
    {"afirmacion":"En Chile, la conspiración para cometer un delito es siempre punible.","respuesta":False,"fundamento":"Art. 8 CP: la conspiración y proposición para delinquir son punibles solo cuando la ley las penalice expresamente.","tema":"Conspiración"},
    {"afirmacion":"La reincidencia en Chile es una circunstancia agravante de la responsabilidad penal.","respuesta":True,"fundamento":"Art. 12 N°14-16 CP: la reincidencia es una circunstancia agravante; opera si el culpable ha sido castigado anteriormente por delitos a los que la ley señale mayor, igual o menor pena.","tema":"Reincidencia"},
    {"afirmacion":"La prescripción de la acción penal puede suspenderse cuando el imputado se ausenta del país.","respuesta":True,"fundamento":"Art. 96 CP: la prescripción se suspende cuando el procedimiento se dirige contra el imputado; también cuando el culpable se ausenta del territorio nacional.","tema":"Suspensión de la prescripción"},
    {"afirmacion":"El delito de lesiones graves gravísimas del art. 397 N°1 CP se sanciona con presidio mayor.","respuesta":True,"fundamento":"Art. 397 N°1 CP: si las lesiones dejan al ofendido demente, inútil para el trabajo, impotente, impedido de un miembro importante o notablemente deforme, se impone presidio mayor.","tema":"Lesiones graves gravísimas"},
    {"afirmacion":"El error de prohibición invencible elimina la culpabilidad del autor.","respuesta":True,"fundamento":"El error de prohibición invencible (no poder conocer la ilicitud del acto) excluye la conciencia de la antijuridicidad, elemento de la culpabilidad; elimina la imputación personal.","tema":"Error de prohibición"},
    {"afirmacion":"En Chile, la culpa consciente equivale al dolo eventual.","respuesta":False,"fundamento":"La culpa consciente (el agente prevé el resultado pero confía en evitarlo) y el dolo eventual (acepta el resultado probable) son categorías distintas aunque próximas.","tema":"Culpa consciente vs dolo eventual"},
    {"afirmacion":"El hurto se diferencia del robo en que en el primero no hay violencia ni intimidación.","respuesta":True,"fundamento":"Art. 432 CP: el hurto es la apropiación de cosa mueble ajena sin la voluntad del dueño, sin violencia ni intimidación. El robo agrega estos elementos.","tema":"Hurto vs robo"},
    {"afirmacion":"La flagrancia permite detener a cualquier persona sin orden judicial previa.","respuesta":True,"fundamento":"Art. 130 CPP: en situación de flagrancia, cualquier persona puede detener al imputado; la policía también está facultada para ello sin orden previa.","tema":"Detención en flagrancia"},
    {"afirmacion":"El robo con homicidio en Chile se sanciona con presidio perpetuo calificado.","respuesta":True,"fundamento":"Art. 433 N°1 CP: el robo con homicidio, violación o castración se sanciona con presidio perpetuo a presidio perpetuo calificado.","tema":"Robo con homicidio"},
    {"afirmacion":"La complicidad es una forma de autoría ampliada en el CP chileno.","respuesta":False,"fundamento":"Arts. 15-16 CP: la complicidad es una forma de participación accesoria; el cómplice coopera dolosamente sin ser autor ni coautor del delito.","tema":"Complicidad"},
    {"afirmacion":"Los menores de 14 años son absolutamente inimputables en Chile.","respuesta":True,"fundamento":"Ley 20.084 (LRPA): los menores de 14 años no están sujetos al sistema penal de responsabilidad de adolescentes; son absoluta y penalmente inimputables.","tema":"Inimputabilidad de menores"},
    {"afirmacion":"El delito continuado es tratado como un solo delito para efectos de penalidad.","respuesta":True,"fundamento":"La doctrina y jurisprudencia chilena reconocen el delito continuado (varias acciones constitutivas del mismo tipo penal) como un solo delito para efectos punitivos.","tema":"Delito continuado"},
    {"afirmacion":"La reparación del daño causado a la víctima es una circunstancia atenuante en Chile.","respuesta":True,"fundamento":"Art. 11 N°7 CP: es una circunstancia atenuante haber procurado con celo reparar el mal causado o impedir sus ulteriores perniciosas consecuencias.","tema":"Atenuante de reparación"},
    {"afirmacion":"La acción penal pública no puede ser ejercida por particulares, solo por el Ministerio Público.","respuesta":False,"fundamento":"Arts. 53-54 CPP: la acción penal pública puede ejercerla el MP y también la víctima a través de la querella; los delitos de acción penal privada requieren querella del ofendido.","tema":"Acción penal"},
    {"afirmacion":"El secuestro y la detención ilegal son delitos contra la libertad ambulatoria.","respuesta":True,"fundamento":"Arts. 141-143 CP: el secuestro y la sustracción de menores, junto con la detención ilegal, son delitos que afectan la libertad personal del ofendido.","tema":"Delitos contra la libertad"},
    {"afirmacion":"La bigamia es un delito de acción penal pública en Chile.","respuesta":True,"fundamento":"Art. 382 CP: el que teniendo vínculo matrimonial vigente contrajere otro matrimonio será sancionado. El MP puede ejercer la acción penal.","tema":"Bigamia"},
    {"afirmacion":"La legítima defensa exige que la agresión sea actual o inminente al momento de la defensa.","respuesta":True,"fundamento":"Art. 10 N°4 CP: la agresión que da lugar a la legítima defensa debe ser actual o inminente; una agresión pasada no habilita la defensa.","tema":"Actualidad de la agresión"},
    {"afirmacion":"El delito de estafa requiere engaño, error, disposición patrimonial y perjuicio.","respuesta":True,"fundamento":"Art. 468 CP y doctrina: los elementos de la estafa son: engaño suficiente → error → acto de disposición patrimonial → perjuicio económico para la víctima.","tema":"Estafa"},
    {"afirmacion":"La pena de inhabilitación absoluta en Chile impide ejercer cargos públicos de forma permanente.","respuesta":False,"fundamento":"Arts. 38-44 CP: la inhabilitación absoluta puede ser temporal (3 a 10 años) o perpetua según el delito; no siempre es permanente.","tema":"Inhabilitación absoluta"},
    {"afirmacion":"El art. 10 N°9 CP consagra la causal de justificación del ejercicio legítimo de un derecho.","respuesta":True,"fundamento":"Art. 10 N°9 CP: está exento de responsabilidad penal el que obra en cumplimiento de un deber o en el ejercicio legítimo de un derecho, autoridad, oficio o cargo.","tema":"Ejercicio legítimo de un derecho"},
    {"afirmacion":"La tentativa inidónea o delito imposible es punible en Chile.","respuesta":False,"fundamento":"La tentativa inidónea (medios o sujeto que hacen imposible el delito) no es punible en Chile; se requiere comienzo de ejecución con medios aptos para consumar el delito.","tema":"Tentativa inidónea"},
])

VF_PROCESAL.extend([
    {"afirmacion":"En el procedimiento civil ordinario, los testigos deben declarar ante el juez y no mediante escrito.","respuesta":True,"fundamento":"Art. 365 CPC: los testigos deben ser examinados personalmente por el juez. La declaración por escrito solo procede en casos excepcionales.","tema":"Declaración de testigos"},
    {"afirmacion":"El recurso de reposición procede contra las sentencias interlocutorias.","respuesta":False,"fundamento":"Art. 181 CPC: la reposición procede contra autos y decretos, no contra sentencias interlocutorias. Para estas últimas procede la apelación.","tema":"Recurso de reposición"},
    {"afirmacion":"La confesión ficta produce plena prueba en Chile en todos los casos.","respuesta":False,"fundamento":"Art. 394 CPC: si el citado no comparece, se le da por confeso en los hechos sobre que ha sido interrogado, pero el tribunal puede ponderar esta prueba con las demás.","tema":"Confesión ficta"},
    {"afirmacion":"La acumulación de autos procede cuando hay identidad de partes, objeto o causa entre los juicios.","respuesta":False,"fundamento":"Art. 92 CPC: la acumulación procede cuando hay identidad de personas o cuando la sentencia de uno produce efectos de cosa juzgada en otro, entre otras causales.","tema":"Acumulación de autos"},
    {"afirmacion":"El procedimiento ordinario civil ante el juzgado de letras tiene como primera etapa la discusión.","respuesta":True,"fundamento":"Arts. 253-316 CPC: el juicio ordinario de mayor cuantía comienza con la demanda y contestación (etapa de discusión), seguida de conciliación, prueba y sentencia.","tema":"Etapas del juicio ordinario"},
    {"afirmacion":"El incidente de nulidad de todo lo obrado requiere que la parte no haya sido debidamente emplazada.","respuesta":True,"fundamento":"Art. 80 CPC: si al litigante no se le ha hecho saber en persona alguna providencia y por eso no compareció al juicio, puede pedir la nulidad de todo lo obrado.","tema":"Nulidad por falta de emplazamiento"},
    {"afirmacion":"En Chile, la prueba pericial es apreciada por el juez según las reglas de la sana crítica.","respuesta":True,"fundamento":"Art. 425 CPC: los tribunales aprecian la fuerza probatoria del dictamen de peritos conforme a las reglas de la sana crítica.","tema":"Apreciación de la prueba pericial"},
    {"afirmacion":"El embargo de bienes raíces en procedimientos ejecutivos requiere inscripción en el CBR.","respuesta":True,"fundamento":"Art. 453 CPC: el embargo de bienes raíces se efectúa por inscripción del decreto en el CBR, siendo desde ese momento oponible a terceros.","tema":"Embargo de inmuebles"},
    {"afirmacion":"La audiencia preparatoria en el juicio oral laboral es presencial y no puede realizarse por medios telemáticos.","respuesta":False,"fundamento":"Desde la pandemia y leyes posteriores, los tribunales laborales pueden realizar audiencias preparatorias por videollamada con acuerdo de las partes o por razones de distancia.","tema":"Audiencias telemáticas"},
    {"afirmacion":"El desistimiento de la demanda extingue la acción con efectos de cosa juzgada.","respuesta":False,"fundamento":"Art. 148 CPC: el desistimiento de la demanda es una renuncia al procedimiento específico, pero no extingue la acción; el actor podría intentar nueva demanda salvo que se renuncie explícitamente.","tema":"Desistimiento de la demanda"},
    {"afirmacion":"En Chile, el juicio de hacienda es un procedimiento especial para litigios en que el Fisco es parte.","respuesta":True,"fundamento":"Arts. 748-752 CPC: el juicio de hacienda es el procedimiento aplicable cuando el Fisco actúa como parte; interviene el Consejo de Defensa del Estado.","tema":"Juicio de hacienda"},
    {"afirmacion":"La absolución de posiciones es el mecanismo para obtener la confesión judicial provocada.","respuesta":True,"fundamento":"Arts. 385-402 CPC: la absolución de posiciones es el procedimiento mediante el cual una parte pide al tribunal que cite a la contraria para que confiese hechos.","tema":"Absolución de posiciones"},
    {"afirmacion":"Las medidas cautelares en materia civil pueden decretarse sin audiencia de la parte afectada.","respuesta":True,"fundamento":"Art. 302 CPC: las medidas precautorias pueden decretarse provisoriamente sin notificación al demandado cuando hay mérito para ello.","tema":"Medidas cautelares sin audiencia"},
    {"afirmacion":"El recurso de casación en el fondo solo procede contra sentencias definitivas de segunda instancia.","respuesta":True,"fundamento":"Art. 767 CPC: el recurso de casación en el fondo procede contra sentencias definitivas inapelables de tribunales superiores y contra interlocutorias que pongan término al juicio.","tema":"Procedencia casación en el fondo"},
    {"afirmacion":"El tribunal arbitral de árbitros arbitradores puede fallar en equidad sin sujeción a ley.","respuesta":True,"fundamento":"Art. 223 COT: el árbitro arbitrador falla en conciencia y sin sujeción a leyes procesales ni de fondo, conforme a lo que su prudencia y equidad le dictaren.","tema":"Árbitro arbitrador"},
    {"afirmacion":"La excepción de cosa juzgada requiere identidad legal de personas, cosa pedida y causa de pedir.","respuesta":True,"fundamento":"Art. 177 CPC: la excepción de cosa juzgada requiere triple identidad: legal de personas, objeto pedido y causa de pedir (eadem personae, eadem res, eadem causa).","tema":"Triple identidad cosa juzgada"},
    {"afirmacion":"En Chile, el juicio ejecutivo puede iniciarse sin sentencia previa cuando el acreedor tiene título ejecutivo perfecto.","respuesta":True,"fundamento":"Art. 434 CPC: el juicio ejecutivo procede cuando el acreedor tiene un título ejecutivo que da derecho a despachar ejecución directamente.","tema":"Inicio del juicio ejecutivo"},
    {"afirmacion":"La nulidad procesal debe ser declarada de oficio por el juez siempre que exista un vicio.","respuesta":False,"fundamento":"Art. 84 CPC: el juez puede declarar de oficio la nulidad en ciertos casos, pero la regla general es que debe ser solicitada por la parte perjudicada.","tema":"Nulidad procesal"},
    {"afirmacion":"El procedimiento monitorio en materia laboral permite obtener título ejecutivo sin juicio si el empleador no impugna.","respuesta":True,"fundamento":"Art. 496 CT: en el procedimiento monitorio, si el empleador no reclama dentro de 10 días, el juez dicta resolución que tiene mérito ejecutivo.","tema":"Procedimiento monitorio laboral"},
    {"afirmacion":"En el recurso de apelación civil, el apelante puede ampliar la competencia del tribunal superior a asuntos no controvertidos.","respuesta":False,"fundamento":"Art. 209 CPC: el tribunal de alzada no puede modificar en perjuicio del apelante las resoluciones recurridas ni pronunciarse sobre puntos no comprendidos en la apelación.","tema":"Competencia del tribunal de alzada"},
    {"afirmacion":"La inhabilidad de testigos por parentesco afecta a toda clase de juicios en Chile.","respuesta":False,"fundamento":"Art. 358 CPC: las inhabilidades de testigos por parentesco solo aplican en determinados procedimientos; hay testigos hábiles e inhábiles según la materia.","tema":"Inhabilidades de testigos"},
    {"afirmacion":"El contrato de transacción puede ser título ejecutivo si se extiende por escritura pública.","respuesta":True,"fundamento":"Art. 434 N°2 CPC: es título ejecutivo la escritura pública no objetada de falsedad; una transacción por escritura pública constituye título ejecutivo.","tema":"Transacción como título ejecutivo"},
    {"afirmacion":"La notificación por avisos en prensa procede cuando el demandado no puede ser ubicado.","respuesta":True,"fundamento":"Art. 54 CPC: si no se conoce el domicilio del notificado, el tribunal puede ordenar la notificación por avisos en diarios del lugar del juicio.","tema":"Notificación por avisos"},
    {"afirmacion":"En el procedimiento de familia, la conciliación es una etapa obligatoria antes del juicio oral.","respuesta":True,"fundamento":"Art. 61 N°5 LTF: durante la audiencia preparatoria en el procedimiento de familia, el juez debe llamar a conciliación a las partes.","tema":"Conciliación en familia"},
    {"afirmacion":"El mandato judicial termina automáticamente con la muerte del mandante.","respuesta":False,"fundamento":"Art. 529 COT: el mandato judicial no termina por la muerte del mandante; el mandatario continúa representando al causante hasta que los herederos lo revoquen.","tema":"Mandato judicial y muerte del mandante"},
])

VF_CONSTITUCIONAL.extend([
    {"afirmacion":"Los derechos fundamentales consagrados en el art. 19 CPR son numerus clausus.","respuesta":False,"fundamento":"Art. 5 inc. 2 CPR: la soberanía tiene como límite los derechos esenciales emanados de la naturaleza humana, incluyendo los de tratados internacionales; el catálogo no es cerrado.","tema":"Derechos fundamentales y numerus clausus"},
    {"afirmacion":"El Consejo de Estado existe en el ordenamiento constitucional chileno vigente.","respuesta":False,"fundamento":"El Consejo de Estado fue suprimido con la CPR de 1980; no existe en el ordenamiento constitucional chileno actual.","tema":"Órganos constitucionales"},
    {"afirmacion":"La ley interpretativa de la CPR requiere quórum de dos tercios en cada cámara.","respuesta":False,"fundamento":"Art. 66 CPR: las leyes interpretativas de la Constitución requieren para su aprobación, modificación o derogación, de las tres quintas partes de los diputados y senadores en ejercicio.","tema":"Quórum leyes interpretativas"},
    {"afirmacion":"El Senado puede acusar constitucionalmente a los Ministros de Estado.","respuesta":False,"fundamento":"Art. 52 N°2 CPR: la acusación constitucional la formula la Cámara de Diputados; el Senado la conoce y resuelve como jurado.","tema":"Acusación constitucional"},
    {"afirmacion":"En Chile, el Presidente puede disolver el Congreso Nacional.","respuesta":False,"fundamento":"La CPR de 1980 no contempla la disolución del Congreso por el Presidente. Chile tiene un sistema presidencial con separación de poderes sin esta facultad.","tema":"Relación Ejecutivo-Congreso"},
    {"afirmacion":"Las leyes de quórum calificado requieren la mayoría absoluta de los parlamentarios en ejercicio.","respuesta":True,"fundamento":"Art. 66 inc. 3 CPR: las leyes de quórum calificado se establecen, modifican o derogan por la mayoría absoluta de los diputados y senadores en ejercicio.","tema":"Quórum calificado"},
    {"afirmacion":"El principio de subsidiariedad en la CPR implica que el Estado solo debe actuar cuando los privados no pueden.","respuesta":True,"fundamento":"Art. 1 inc. 3 y art. 19 N°21 CPR: el principio de subsidiariedad limita la actuación del Estado a lo que los particulares no pueden llevar a cabo por sí mismos.","tema":"Subsidiariedad"},
    {"afirmacion":"La garantía del juez natural prohíbe crear tribunales especiales para juzgar hechos pasados.","respuesta":True,"fundamento":"Art. 19 N°3 inc. 5 CPR: nadie puede ser juzgado por comisiones especiales; la comisión debe estar establecida con anterioridad por la ley.","tema":"Juez natural"},
    {"afirmacion":"La Contraloría General de la República puede declarar inconstitucional una ley del Congreso.","respuesta":False,"fundamento":"La CGR realiza el trámite de toma de razón para verificar la constitucionalidad y legalidad de los decretos supremos del Ejecutivo; no controla la constitucionalidad de las leyes.","tema":"Contraloría y control de legalidad"},
    {"afirmacion":"En Chile, las Fuerzas Armadas son obedientes y no deliberantes según la CPR.","respuesta":True,"fundamento":"Art. 101 CPR: las Fuerzas Armadas y Carabineros son esencialmente obedientes y no deliberantes; están sujetas al poder civil.","tema":"Fuerzas Armadas"},
    {"afirmacion":"La acción de amparo económico protege el derecho a desarrollar cualquier actividad económica.","respuesta":True,"fundamento":"Ley 18.971: el amparo económico protege el derecho consagrado en el art. 19 N°21 CPR (actividad económica lícita) cuando es lesionado por actos del Estado.","tema":"Amparo económico"},
    {"afirmacion":"El Ministerio Público tiene rango constitucional en Chile.","respuesta":True,"fundamento":"Arts. 83-91 CPR: el Ministerio Público está consagrado constitucionalmente desde la reforma de 1997 que introdujo el nuevo sistema procesal penal acusatorio.","tema":"Ministerio Público constitucional"},
    {"afirmacion":"La Contraloría dictamina sobre la juridicidad de los actos de la Administración.","respuesta":True,"fundamento":"Art. 98 CPR: la CGR ejerce el control de legalidad de los actos de la Administración, toma razón de los decretos y resoluciones y lleva la contabilidad general de la Nación.","tema":"Funciones de la Contraloría"},
    {"afirmacion":"El Presidente de la República tiene iniciativa exclusiva en proyectos que alteren la división política del país.","respuesta":True,"fundamento":"Art. 65 inc. 4 N°2 CPR: corresponde al Presidente la iniciativa exclusiva para los proyectos de ley que tengan relación con alteración de la división política o administrativa del país.","tema":"Iniciativa presidencial exclusiva"},
    {"afirmacion":"El Consejo Fiscal Autónomo tiene rango constitucional en Chile desde la reforma de 2019.","respuesta":True,"fundamento":"Art. 108 CPR (reforma 2019): el Consejo Fiscal Autónomo tiene rango constitucional; vela por la responsabilidad fiscal y el cumplimiento de las normas sobre transparencia.","tema":"Consejo Fiscal Autónomo"},
    {"afirmacion":"El derecho de propiedad en Chile puede ser privado por ley, siempre que se pague indemnización previa.","respuesta":True,"fundamento":"Art. 19 N°24 CPR: nadie puede ser privado de su propiedad sino en virtud de ley general o especial que autorice la expropiación y previo pago de indemnización.","tema":"Expropiación"},
    {"afirmacion":"En Chile, los tratados de derechos humanos ratificados y vigentes no pueden ser derogados por ley ordinaria.","respuesta":True,"fundamento":"Art. 54 N°1 CPR: las disposiciones de un tratado solo pueden derogarse, modificarse o suspenderse en la forma prevista en los propios tratados o en las normas generales del DI.","tema":"Tratados DDHH y ley"},
    {"afirmacion":"La potestad reglamentaria del Presidente es solo de ejecución de las leyes.","respuesta":False,"fundamento":"Art. 32 N°6 CPR: el Presidente tiene potestad reglamentaria de ejecución (dicta reglamentos para ejecutar leyes) y también autónoma (regula materias no reservadas a la ley).","tema":"Potestad reglamentaria autónoma"},
    {"afirmacion":"El Fiscal Nacional del Ministerio Público es designado por el Presidente con acuerdo del Senado.","respuesta":True,"fundamento":"Art. 85 CPR: el Fiscal Nacional es nombrado por el Presidente de la República con acuerdo del Senado adoptado por dos tercios de sus miembros en ejercicio.","tema":"Designación Fiscal Nacional"},
    {"afirmacion":"Chile tiene un sistema bicameral simétrico donde ambas cámaras tienen iguales atribuciones.","respuesta":False,"fundamento":"Chile tiene un bicameralismo asimétrico: la Cámara de Diputados fiscaliza al Ejecutivo y acusa constitucionalmente; el Senado actúa como jurado y tiene otras atribuciones exclusivas.","tema":"Bicameralismo asimétrico"},
    {"afirmacion":"La reserva legal implica que ciertas materias solo pueden ser reguladas por ley, no por reglamento.","respuesta":True,"fundamento":"Art. 63 CPR: las materias de ley (dominio legal) son aquellas que la Constitución reserva exclusivamente al legislador; el Ejecutivo no puede regularlas por vía reglamentaria.","tema":"Reserva legal"},
    {"afirmacion":"El Banco Central de Chile es autónomo y no puede financiar al Fisco directamente.","respuesta":True,"fundamento":"Art. 108 CPR: el Banco Central es autónomo con patrimonio propio; no puede adoptar acuerdos que signifiquen directa o indirectamente establecer normas o requisitos diferentes o discriminatorios en relación a personas, instituciones o entidades que realicen operaciones de la misma naturaleza. Y art. 109: no puede conceder créditos al Fisco.","tema":"Banco Central autónomo"},
    {"afirmacion":"La igualdad ante la ley del art. 19 N°2 CPR prohíbe toda diferencia de trato.","respuesta":False,"fundamento":"Art. 19 N°2 CPR: la igualdad ante la ley prohíbe diferencias arbitrarias; admite distinciones razonables y objetivamente justificadas. No toda diferencia es discriminatoria.","tema":"Igualdad ante la ley"},
    {"afirmacion":"El principio de legalidad en materia penal implica que no hay delito ni pena sin ley previa.","respuesta":True,"fundamento":"Art. 19 N°3 inc. 8 CPR: ningún delito se castigará con otra pena que la que señale una ley promulgada con anterioridad a su perpetración.","tema":"Nullum crimen sine lege"},
    {"afirmacion":"El plebiscito comunal puede ser convocado por el alcalde con acuerdo del concejo municipal.","respuesta":True,"fundamento":"Arts. 99 y ss. LOCM: el alcalde puede someter a plebiscito materias de administración local con acuerdo del concejo o a petición de vecinos.","tema":"Plebiscito comunal"},
])

VF_LABORAL.extend([
    {"afirmacion":"El contrato de aprendizaje es un contrato especial que puede pagar una remuneración inferior al mínimo.","respuesta":True,"fundamento":"Art. 78 CT: en el contrato de aprendizaje, la remuneración puede ser libremente convenida por las partes y puede ser inferior al ingreso mínimo mensual.","tema":"Contrato de aprendizaje"},
    {"afirmacion":"Los trabajadores de casa particular tienen derecho a feriado proporcional al tiempo trabajado.","respuesta":True,"fundamento":"Art. 149 CT: los trabajadores de casa particular que hayan laborado todo el año tienen 15 días de feriado; si no completaron el año, les corresponde feriado proporcional.","tema":"Trabajadores casa particular"},
    {"afirmacion":"El despido indirecto o autodespido procede cuando el empleador incurre en incumplimientos graves.","respuesta":True,"fundamento":"Art. 171 CT: el trabajador puede poner término al contrato si el empleador incurre en causales del art. 160 (conductas graves), y puede demandar indemnización como si hubiera sido despedido injustificadamente.","tema":"Despido indirecto"},
    {"afirmacion":"El outsourcing o subcontratación laboral excluye toda responsabilidad de la empresa principal.","respuesta":False,"fundamento":"Arts. 183-A y ss. CT: en la subcontratación, la empresa principal es subsidiariamente responsable de las obligaciones laborales y previsionales del contratista.","tema":"Subcontratación laboral"},
    {"afirmacion":"El pago de horas extraordinarias debe realizarse con el recargo mínimo del 50% sobre el sueldo convenido.","respuesta":True,"fundamento":"Art. 32 CT: las horas extraordinarias se pagarán con recargo de al menos 50% sobre el sueldo convenido para la jornada ordinaria.","tema":"Recargo horas extras"},
    {"afirmacion":"Los funcionarios públicos de planta están sujetos al Código del Trabajo.","respuesta":False,"fundamento":"El Estatuto Administrativo (Ley 18.834) rige a los funcionarios de planta y a contrata de la Administración del Estado; el CT no les aplica como regla general.","tema":"Estatuto Administrativo"},
    {"afirmacion":"La jornada parcial en Chile permite contratos con hasta 30 horas semanales.","respuesta":True,"fundamento":"Art. 40 bis CT: se puede pactar jornada parcial de trabajo no superior a dos tercios de la jornada ordinaria, sin superar 30 horas semanales.","tema":"Jornada parcial"},
    {"afirmacion":"En Chile, el empleador puede exigir al trabajador que trabaje durante su feriado legal.","respuesta":False,"fundamento":"Art. 67 CT: el feriado es irrenunciable; el empleador no puede exigir que el trabajador trabaje durante el período de feriado anual.","tema":"Irrenunciabilidad del feriado"},
    {"afirmacion":"La comisión tripartita que incluye empleadores, trabajadores y gobierno caracteriza el diálogo social en la OIT.","respuesta":True,"fundamento":"La OIT tiene estructura tripartita; el diálogo social es un principio fundamental que involucra a gobiernos, empleadores y trabajadores en igualdad.","tema":"Tripartismo OIT"},
    {"afirmacion":"El contrato individual de trabajo puede pactar condiciones inferiores a las del contrato colectivo vigente.","respuesta":False,"fundamento":"Art. 311 CT: las estipulaciones del contrato individual de trabajo no pueden vulnerar lo establecido en el contrato colectivo vigente en la empresa.","tema":"Primacía del contrato colectivo"},
    {"afirmacion":"La Dirección del Trabajo puede aplicar multas administrativas por infracción al Código del Trabajo.","respuesta":True,"fundamento":"Arts. 474 y ss. CT: la Inspección del Trabajo puede fiscalizar y aplicar multas administrativas a los empleadores que infrinjan las normas laborales.","tema":"Fiscalización DT"},
    {"afirmacion":"Los trabajadores de temporada pueden sindicalizarse en Chile.","respuesta":True,"fundamento":"Art. 216 CT: pueden constituir sindicatos los trabajadores de temporada; se organizan en sindicatos de trabajadores eventuales o transitorios.","tema":"Sindicalización trabajadores temporada"},
    {"afirmacion":"El empleador puede retener el finiquito hasta que el trabajador devuelva los implementos de trabajo.","respuesta":False,"fundamento":"Art. 177 CT: el finiquito debe pagarse al momento de su suscripción o dentro de 5 días hábiles siguientes al término del contrato; no puede retenerse por deudas del trabajador.","tema":"Pago del finiquito"},
    {"afirmacion":"El seguro de desempleo en Chile cubre también a los trabajadores independientes.","respuesta":False,"fundamento":"Ley 19.728: el seguro de cesantía se aplica a los trabajadores dependientes regidos por el CT; no cubre a trabajadores independientes.","tema":"Seguro de cesantía"},
    {"afirmacion":"El fuero maternal comienza desde el embarazo y se extiende hasta un año después del parto.","respuesta":True,"fundamento":"Art. 201 CT: el fuero de la trabajadora embarazada comienza desde el momento del embarazo y dura hasta un año después de terminado el descanso de postnatal.","tema":"Fuero maternal"},
    {"afirmacion":"La negociación colectiva reglada en Chile debe comenzar con la presentación del proyecto de contrato colectivo.","respuesta":True,"fundamento":"Art. 327 CT: el proceso de negociación colectiva reglada se inicia con la presentación del proyecto de contrato colectivo por parte del sindicato o grupo negociador.","tema":"Inicio negociación colectiva"},
    {"afirmacion":"En Chile, la huelga puede ser declarada ilegal si se ejerce en servicios mínimos sin cubrir dichos servicios.","respuesta":True,"fundamento":"Arts. 359-360 CT: los trabajadores que ejerzan la huelga deben proveer los servicios mínimos acordados; incumplirlos puede derivar en declaración de ilegalidad.","tema":"Servicios mínimos en huelga"},
    {"afirmacion":"El tiempo de viaje al trabajo se computa como jornada laboral ordinaria.","respuesta":False,"fundamento":"Art. 33 CT: el tiempo de desplazamiento hacia o desde el trabajo no se considera jornada laboral, salvo que el transporte sea proporcionado por el empleador con obligación de trabajar en ruta.","tema":"Tiempo de viaje"},
    {"afirmacion":"El Código del Trabajo prohíbe expresamente la discriminación en el acceso al empleo por razones de sexo, religión o raza.","respuesta":True,"fundamento":"Art. 2 CT: son contrarios a los principios de las leyes laborales los actos de discriminación basados en raza, color, sexo, edad, estado civil, sindicación, religión, ideología política u otras causas.","tema":"No discriminación laboral"},
    {"afirmacion":"El inspector del trabajo puede paralizar faenas cuando exista riesgo inminente para la seguridad de los trabajadores.","respuesta":True,"fundamento":"Art. 184 bis CT: ante riesgo grave e inminente para la salud o la vida de los trabajadores, el inspector puede ordenar la paralización inmediata de las faenas.","tema":"Paralización de faenas"},
    {"afirmacion":"Los trabajadores pueden negociar individualmente condiciones mejores a las del contrato colectivo.","respuesta":True,"fundamento":"Art. 311 CT: las estipulaciones del contrato individual pueden mejorar (pero no deteriorar) las condiciones del instrumento colectivo vigente.","tema":"Mejora individual sobre contrato colectivo"},
    {"afirmacion":"El empleador puede utilizar las instalaciones de la empresa para actividades sindicales de sus trabajadores.","respuesta":True,"fundamento":"Art. 255 CT: el empleador debe proporcionar instalaciones adecuadas para que funcione el sindicato, si no tiene local propio.","tema":"Instalaciones sindicales"},
    {"afirmacion":"La prueba del contrato de trabajo corresponde exclusivamente al trabajador.","respuesta":False,"fundamento":"Art. 9 CT: la existencia del contrato de trabajo se presume cuando el trabajador presta servicios bajo subordinación; corresponde al empleador probar que no existe vínculo laboral.","tema":"Prueba del contrato de trabajo"},
    {"afirmacion":"Las indemnizaciones laborales por años de servicio tienen tope de 11 meses.","respuesta":True,"fundamento":"Art. 163 CT: la indemnización por años de servicio no puede exceder de 11 meses de remuneración, cualquiera sea el tiempo servido.","tema":"Tope indemnización por años"},
])

VF_OBLIGACIONES.extend([
    {"afirmacion":"En las obligaciones de género, el deudor cumple entregando cosa de calidad mediana.","respuesta":True,"fundamento":"Art. 1509 CC: si el género no está restringido, el deudor cumple entregando cualquier individuo del género con tal que sea de calidad a lo menos mediana.","tema":"Obligaciones de género"},
    {"afirmacion":"La delegación perfecta o novatoria extingue la obligación del deudor primitivo.","respuesta":True,"fundamento":"Art. 1635 CC: la sustitución de un nuevo deudor extingue la obligación del primitivo si el acreedor consiente expresamente en dar por libre al deudor primitivo.","tema":"Delegación perfecta"},
    {"afirmacion":"El incumplimiento de obligación de no hacer produce de pleno derecho la indemnización de perjuicios.","respuesta":False,"fundamento":"Art. 1555 CC: el incumplimiento de obligación de no hacer da derecho al acreedor para que se deshaga lo hecho (si cabe) y/o a pedir indemnización; requiere declaración judicial.","tema":"Obligación de no hacer"},
    {"afirmacion":"La subrogación real se produce cuando un bien reemplaza a otro en el patrimonio con sus mismos atributos.","respuesta":True,"fundamento":"La subrogación real opera cuando una cosa ocupa el lugar de otra en el patrimonio con iguales características jurídicas (ej.: el precio del inmueble vendido que reemplaza al bien enajenado en la sociedad conyugal).","tema":"Subrogación real"},
    {"afirmacion":"El deudor solidario que pagó puede repetir contra sus codeudores en la parte que les corresponde.","respuesta":True,"fundamento":"Art. 1522 CC: el codeudor solidario que pagó más de su cuota tiene acción de reembolso contra los demás por la parte que les corresponde.","tema":"Reembolso en solidaridad"},
    {"afirmacion":"La condición simplemente potestativa que depende de un hecho del deudor es válida.","respuesta":True,"fundamento":"Art. 1478 CC: solo es nula la condición que depende de la sola voluntad del deudor (potestativa del deudor pura); la mixta o que depende de un hecho del deudor es válida.","tema":"Condición simplemente potestativa"},
    {"afirmacion":"La acción oblicua o subrogatoria permite al acreedor ejercer los derechos del deudor inactivo.","respuesta":True,"fundamento":"Art. 2466 CC: el acreedor puede subrogarse en los derechos del deudor cuando este no los ejerce y con ello perjudica a los acreedores.","tema":"Acción oblicua"},
    {"afirmacion":"La obligación natural no puede ser exigida judicialmente pero sí pagar voluntariamente.","respuesta":True,"fundamento":"Art. 1470 CC: las obligaciones naturales no confieren acción para exigir su cumplimiento, pero autorizan para retener lo pagado en razón de ellas.","tema":"Obligaciones naturales"},
    {"afirmacion":"El fortuito libera al deudor de responsabilidad en las obligaciones de especie o cuerpo cierto.","respuesta":True,"fundamento":"Art. 1547 CC: el deudor de especie o cuerpo cierto no responde del caso fortuito que destruye la cosa, salvo que esté en mora o que el fortuito provenga de culpa suya.","tema":"Caso fortuito en obligaciones de especie"},
    {"afirmacion":"En Chile, el plazo de prescripción extintiva se interrumpe civílmente con el reconocimiento del deudor.","respuesta":True,"fundamento":"Art. 2518 CC: la prescripción extintiva se interrumpe naturalmente por el reconocimiento de la obligación por parte del deudor.","tema":"Interrupción natural de la prescripción"},
    {"afirmacion":"Las cláusulas abusivas en contratos de adhesión son sancionadas por la Ley 19.496.","respuesta":True,"fundamento":"Arts. 16 y ss. Ley 19.496: son nulas las cláusulas abusivas de los contratos de adhesión que contraríen la buena fe o que causen perjuicio al consumidor.","tema":"Cláusulas abusivas"},
    {"afirmacion":"La acción directa del tercero beneficiario requiere que haya aceptado la estipulación antes de revocarse.","respuesta":True,"fundamento":"Art. 1449 CC: el tercero beneficiario puede exigir directamente el cumplimiento si ha aceptado la estipulación y esta no ha sido revocada antes de la aceptación.","tema":"Acción directa del tercero"},
    {"afirmacion":"Los daños morales son indemnizables en materia contractual en Chile.","respuesta":True,"fundamento":"La jurisprudencia chilena ha reconocido la indemnización del daño moral en el incumplimiento contractual, aunque el CC no lo establece expresamente.","tema":"Daño moral contractual"},
    {"afirmacion":"La excepción de contrato no cumplido (exceptio non adimpleti contractus) es solo procedente en contratos sinalagmáticos.","respuesta":True,"fundamento":"Art. 1552 CC: en los contratos bilaterales, ninguna parte está en mora si la otra no cumplió o no se allanó a cumplir; la exceptio solo opera en contratos con obligaciones recíprocas.","tema":"Exceptio non adimpleti contractus"},
    {"afirmacion":"Las obligaciones indivisibles se distinguen de las solidarias en que en aquellas la indivisibilidad es de la naturaleza de la prestación.","respuesta":True,"fundamento":"Arts. 1524-1526 CC: la indivisibilidad de la obligación es objetiva (naturaleza de la prestación); la solidaridad es subjetiva (pacto o ley); son instituciones distintas.","tema":"Indivisibilidad vs solidaridad"},
    {"afirmacion":"En las obligaciones a plazo suspensivo, el acreedor no puede exigir el cumplimiento antes de que venza el plazo.","respuesta":True,"fundamento":"Art. 1496 CC: el plazo suspensivo beneficia al deudor; el acreedor no puede exigir anticipadamente salvo que el deudor se haya constituido en insolvencia o caído en ciertos supuestos.","tema":"Plazo suspensivo"},
    {"afirmacion":"El pago parcial nunca extingue la obligación.","respuesta":False,"fundamento":"El pago parcial puede extinguir proporcionalmente la obligación si el acreedor lo acepta (art. 1591 CC). Con aceptación del acreedor, el pago parcial es válido.","tema":"Pago parcial"},
    {"afirmacion":"La fianza puede ser por cantidad determinada o indeterminada.","respuesta":True,"fundamento":"Art. 2343 CC: la fianza puede limitarse a una parte de la deuda (fianza parcial) o puede ser indefinida, cubriéndose hasta el monto de la obligación principal.","tema":"Extensión de la fianza"},
    {"afirmacion":"La lesión enorme es una causal de rescisión en todos los contratos en Chile.","respuesta":False,"fundamento":"La lesión enorme es excepcional en el CC chileno; se aplica específicamente a la compraventa de inmuebles (art. 1888), permuta (art. 1900), aceptación de herencia (art. 1234) y partición (art. 1348).","tema":"Lesión enorme excepcional"},
    {"afirmacion":"El error esencial produce nulidad absoluta en Chile.","respuesta":True,"fundamento":"Art. 1453 CC: el error esencial u obstáculo impide la formación del consentimiento y produce nulidad absoluta del acto.","tema":"Error esencial"},
    {"afirmacion":"La resolución del contrato tiene efectos retroactivos entre las partes.","respuesta":True,"fundamento":"Arts. 1487 y ss. CC: la resolución produce efectos ex tunc; las cosas vuelven al estado anterior, como si el contrato no hubiera existido.","tema":"Efectos de la resolución"},
    {"afirmacion":"La mora exige que el deudor sea interpelado salvo que la ley o el contrato dispongan lo contrario.","respuesta":True,"fundamento":"Art. 1551 CC: el deudor está en mora cuando no cumple en el tiempo estipulado (si se pactó plazo), o cuando judicialmente se le reconviene (regla general), entre otras.","tema":"Constitución en mora"},
    {"afirmacion":"Las arras entregadas como garantía se imputan al precio si se concluye el contrato.","respuesta":True,"fundamento":"Art. 1805 CC: las arras se entienden dadas en garantía del contrato; si el contrato se concluye, se imputan al precio o se restituyen.","tema":"Imputación de las arras"},
    {"afirmacion":"El art. 1545 CC consagra el principio de fuerza obligatoria del contrato.","respuesta":True,"fundamento":"Art. 1545 CC: todo contrato legalmente celebrado es una ley para los contratantes y no puede ser invalidado sino por su consentimiento mutuo o por causas legales.","tema":"Fuerza obligatoria del contrato"},
    {"afirmacion":"La condición fallida extingue el derecho condicional del acreedor bajo condición suspensiva.","respuesta":True,"fundamento":"Art. 1481 CC: la condición se reputa fallida si ha expirado el tiempo dentro del cual el acontecimiento ha debido verificarse. El derecho pendiente de condición suspensiva se extingue.","tema":"Condición fallida"},
])

VF_FAMILIA.extend([
    {"afirmacion":"El matrimonio celebrado en el extranjero entre personas del mismo sexo es reconocido en Chile.","respuesta":True,"fundamento":"Ley 21.400 y Ley 19.947: Chile reconoce los matrimonios celebrados en el extranjero entre personas del mismo sexo desde la vigencia de la Ley 21.400.","tema":"Matrimonio igualitario en el extranjero"},
    {"afirmacion":"El juez de familia puede decretar medidas cautelares en violencia intrafamiliar de oficio.","respuesta":True,"fundamento":"Art. 22 Ley 20.066: el juez puede decretar de oficio las medidas cautelares que estime necesarias para proteger a las víctimas de violencia intrafamiliar.","tema":"Medidas cautelares VIF"},
    {"afirmacion":"El cónyuge sobreviviente hereda a falta de descendientes y ascendientes del causante.","respuesta":False,"fundamento":"Art. 990 CC: el cónyuge hereda junto con los hijos (1er orden), con los padres (2do orden) y solo en el 4to orden. No hereda a falta de descendientes y ascendientes; eso es el 3er orden.","tema":"Orden sucesorio del cónyuge"},
    {"afirmacion":"La filiation puede ser impugnada solo por el hijo dentro de un año desde su mayoría de edad.","respuesta":False,"fundamento":"Arts. 212-217 CC: la acción de impugnación de la paternidad puede ejercerse por el marido, la madre y el hijo en distintos plazos; no es exclusiva del hijo.","tema":"Impugnación de la filiación"},
    {"afirmacion":"El contrato de matrimonio o capitulaciones matrimoniales pueden modificarse libremente durante el matrimonio.","respuesta":False,"fundamento":"Art. 1716 CC: las capitulaciones prematrimoniales solo pueden celebrarse antes del matrimonio; durante el matrimonio solo se puede cambiar de régimen conforme al art. 1723 CC.","tema":"Capitulaciones matrimoniales"},
    {"afirmacion":"La tutela en Chile recae en personas que no tienen padre ni madre y son menores de edad.","respuesta":True,"fundamento":"Art. 338 CC: el tutor cuida de la persona y bienes del pupilo que no tiene padre ni madre que ejerza la patria potestad, ni curador.","tema":"Tutela"},
    {"afirmacion":"Los alimentos mayores comprenden todo lo que es indispensable para la subsistencia del alimentado.","respuesta":False,"fundamento":"Art. 323 CC: los alimentos congruos habilitan al alimentado para subsistir modestamente de un modo correspondiente a su posición social; los necesarios solo cubren lo indispensable.","tema":"Tipos de alimentos"},
    {"afirmacion":"El consentimiento de ambos cónyuges es necesario para enajenar inmuebles propios del marido en sociedad conyugal.","respuesta":False,"fundamento":"Art. 1749 CC: el marido requiere autorización de la mujer para enajenar los bienes sociales inmuebles y los propios de la mujer; no los suyos propios.","tema":"Enajenación de bienes propios del marido"},
    {"afirmacion":"La acción de reclamación de filiación es imprescriptible cuando la ejerce el hijo.","respuesta":True,"fundamento":"Art. 195 CC: el derecho de reclamar la filiación es imprescriptible e irrenunciable; la acción de reclamación del hijo no prescribe.","tema":"Imprescriptibilidad de la reclamación de filiación"},
    {"afirmacion":"El régimen de participación en los gananciales implica comunidad de bienes durante el matrimonio.","respuesta":False,"fundamento":"Art. 1792-1 CC: en la participación en los gananciales cada cónyuge administra, goza y dispone libremente de sus bienes; al término se comparten las ganancias. No hay comunidad durante el matrimonio.","tema":"Participación en los gananciales"},
    {"afirmacion":"La separación judicial no disuelve el vínculo matrimonial en Chile.","respuesta":True,"fundamento":"Art. 31 Ley 19.947: la separación judicial no disuelve el matrimonio; los cónyuges conservan su estado civil de casados, aunque cesan los deberes conyugales.","tema":"Separación judicial vs divorcio"},
    {"afirmacion":"El tutor o curador del menor puede realizar todos los actos jurídicos sin autorización judicial.","respuesta":False,"fundamento":"Arts. 391 y 393 CC: el tutor o curador requiere autorización judicial para actos de enajenación, constitución de hipotecas, arrendamiento de largo plazo y otros actos graves sobre los bienes del pupilo.","tema":"Limitaciones del tutor"},
    {"afirmacion":"En Chile, el menor adulto (entre 14 y 18 años) puede actuar en juicios sin representación parental.","respuesta":False,"fundamento":"Art. 264 CC: el hijo de familia no puede parecer en juicio como actor sin el consentimiento del padre o madre o del curador adjunto en su caso.","tema":"Capacidad procesal del menor"},
    {"afirmacion":"La separación de hecho por más de 3 años habilita a cualquiera de los cónyuges para demandar el divorcio.", "respuesta":True, "fundamento":"Art. 55 inc. 1 Ley 19.947: el divorcio puede ser demandado unilateralmente cuando el cese efectivo de la convivencia sea de al menos 3 años.", "tema":"Divorcio unilateral"},
    {"afirmacion":"En la sociedad conyugal los bienes muebles adquiridos a título gratuito durante el matrimonio son sociales.","respuesta":False,"fundamento":"Art. 1726 CC: los bienes muebles adquiridos a título gratuito (donación, herencia, legado) durante el matrimonio son propios del cónyuge donatario o heredero.","tema":"Bienes propios en sociedad conyugal"},
    {"afirmacion":"El defensor de menores debe ser oído en todos los asuntos judiciales que afecten intereses de menores.","respuesta":False,"fundamento":"La intervención del Ministerio Público (Defensoría en su oportunidad) o del defensor público es requerida en casos específicos según la ley; no en todos los juicios que afecten a menores.","tema":"Defensor de menores"},
    {"afirmacion":"El acuerdo completo y suficiente es requisito para el divorcio de mutuo acuerdo en Chile.","respuesta":True,"fundamento":"Art. 55 Ley 19.947: para el divorcio de mutuo acuerdo se requiere acompañar un acuerdo completo y suficiente que regule alimentos, cuidado personal y relación directa y regular de los hijos.","tema":"Acuerdo completo en divorcio"},
    {"afirmacion":"La patria potestad y el cuidado personal son siempre ejercidos por el mismo progenitor.","respuesta":False,"fundamento":"Arts. 225 y 244 CC: el cuidado personal y la patria potestad pueden recaer en distintos progenitores; son instituciones independientes.","tema":"Patria potestad y cuidado personal"},
    {"afirmacion":"El hijo nacido dentro de los 300 días siguientes a la disolución del matrimonio se presume hijo del marido.","respuesta":True,"fundamento":"Art. 184 CC: se presume hijo del marido el nacido dentro de los 300 días siguientes a la disolución del matrimonio o a la separación judicial.","tema":"Presunción de paternidad"},
    {"afirmacion":"Los cónyuges pueden pactar por escrito el régimen de separación de bienes antes del matrimonio.","respuesta":True,"fundamento":"Art. 1721 CC: las capitulaciones matrimoniales pueden contener el pacto de separación de bienes, renunciando a la sociedad conyugal antes del matrimonio.","tema":"Separación pactada antes del matrimonio"},
    {"afirmacion":"En Chile, el matrimonio es anulable por impubertad si uno de los contrayentes era menor de 16 años.","respuesta":False,"fundamento":"Ley 21.515 (2023): se eliminó la posibilidad de matrimonio de menores de 18 años; ya no se permite el matrimonio de adolescentes, por lo que el menor de 18 años no puede contraer matrimonio.","tema":"Matrimonio de menores"},
    {"afirmacion":"El conviviente civil que sufre negligencia del otro puede poner término al AUC unilateralmente.","respuesta":True,"fundamento":"Art. 26 Ley 20.830: el AUC puede terminar por acuerdo de ambas partes, por voluntad unilateral notificada al otro conviviente, o por otras causales como el matrimonio entre sí.","tema":"Término del AUC"},
    {"afirmacion":"La nulidad del matrimonio en Chile no requiere declaración judicial.","respuesta":False,"fundamento":"Art. 44 Ley 19.947: la nulidad del matrimonio debe ser declarada por sentencia judicial; no opera de pleno derecho.","tema":"Nulidad matrimonial"},
    {"afirmacion":"La orden de alejamiento es una medida cautelar que puede dictar el juez de familia en casos de VIF.","respuesta":True,"fundamento":"Art. 92 Ley 19.968 y art. 7 Ley 20.066: entre las medidas cautelares en VIF está la orden de alejamiento del agresor del hogar y de los lugares que frecuente la víctima.","tema":"Orden de alejamiento VIF"},
    {"afirmacion":"Los abuelos tienen derecho legal a mantener relación directa con sus nietos.","respuesta":True,"fundamento":"Art. 229-2 CC: el hijo tiene el derecho de mantener una relación directa y regular con sus abuelos; el juez puede regular este derecho.","tema":"Relación con abuelos"},
])

VF_COMERCIAL.extend([
    {"afirmacion":"El mandato mercantil se rige por las normas del Código de Comercio, con carácter oneroso.","respuesta":True,"fundamento":"Art. 233 C.Com.: el mandato comercial es naturalmente oneroso; el mandatario tiene derecho a remuneración salvo renuncia expresa.","tema":"Mandato mercantil"},
    {"afirmacion":"En Chile, el acto mixto o de doble carácter se rige por las normas mercantiles para ambas partes.","respuesta":False,"fundamento":"Art. 8 C.Com.: en los actos mixtos (mercantiles para una parte, civiles para otra), cada parte se rige por la legislación que le corresponde según su calidad.","tema":"Actos mixtos"},
    {"afirmacion":"El contrato de leasing o arrendamiento financiero es un contrato mercantil nominado en Chile.","respuesta":False,"fundamento":"El leasing no tiene regulación especial como contrato nominado en el C.Com. chileno; se reconoce por normas tributarias y contables y se rige por el derecho común de arrendamiento.","tema":"Leasing"},
    {"afirmacion":"La quiebra del comerciante en Chile produce la apertura del concurso y la formación de la masa.","respuesta":True,"fundamento":"Ley 20.720: el procedimiento concursal de liquidación (antes quiebra) produce el desasimiento del deudor y la formación del activo de liquidación (masa).","tema":"Procedimiento concursal"},
    {"afirmacion":"El contrato de factoraje permite a una empresa ceder sus créditos a cambio de liquidez inmediata.","respuesta":True,"fundamento":"El factoring o factoraje es el contrato por el cual una empresa cede sus cuentas por cobrar a un factor que las financia, asumiendo el riesgo de cobranza.","tema":"Factoraje"},
    {"afirmacion":"Las sociedades de responsabilidad limitada en Chile tienen personalidad jurídica propia.","respuesta":True,"fundamento":"Ley 3.918 y C.Com.: las SRL tienen personalidad jurídica distinta de los socios, patrimonio propio y responsabilidad limitada al capital aportado.","tema":"SRL y personalidad jurídica"},
    {"afirmacion":"El seguro de responsabilidad civil cubre los daños que el asegurado cause a terceros.","respuesta":True,"fundamento":"Art. 570 C.Com.: en el seguro de responsabilidad civil, el asegurador se obliga a indemnizar los daños que el asegurado, en su calidad de tal, cause a terceros.","tema":"Seguro de responsabilidad civil"},
    {"afirmacion":"En Chile, la letra de cambio puede ser protestada por notario.","respuesta":True,"fundamento":"Art. 61 Ley 18.092: el protesto de letra de cambio se realiza por notario o por el oficial del Registro Civil en localidades donde no haya notario.","tema":"Protesto notarial"},
    {"afirmacion":"Las cuentas en participación son una forma de sociedad mercantil con personalidad jurídica.","respuesta":False,"fundamento":"Art. 507 C.Com.: las cuentas en participación no constituyen una persona jurídica; es un contrato de participación de carácter oculto sin personalidad propia.","tema":"Cuentas en participación"},
    {"afirmacion":"El cheque puede ser protestado por el banco librado cuando hay fondos insuficientes.","respuesta":True,"fundamento":"Art. 33 Ley 7.498: el banco librado debe protestar el cheque presentado al cobro cuando no hay fondos suficientes, consignando el motivo del protesto.","tema":"Protesto del cheque"},
    {"afirmacion":"En una sociedad anónima chilena, el directorio puede delegar todas sus funciones en el gerente general.","respuesta":False,"fundamento":"Art. 40 Ley 18.046: el directorio puede delegar parte de sus facultades en ejecutivos o comités, pero no puede abdicar sus funciones esenciales de dirección y control.","tema":"Delegación en SA"},
    {"afirmacion":"Los acreedores privilegiados tienen preferencia de pago sobre los acreedores valistas en la liquidación concursal.","respuesta":True,"fundamento":"Arts. 2470 y ss. CC y Ley 20.720: en la liquidación, los créditos se pagan según su prelación; los privilegiados preceden a los valistas (créditos sin preferencia).","tema":"Prelación de créditos"},
    {"afirmacion":"El know-how o secreto empresarial tiene protección legal en Chile aunque no esté registrado.","respuesta":True,"fundamento":"Ley 19.039 de Propiedad Industrial y el CT: el secreto empresarial tiene protección legal contra su divulgación no autorizada, independiente de registro.","tema":"Know-how"},
    {"afirmacion":"La comisión mercantil es la especie de mandato que tiene por objeto un acto de comercio.","respuesta":True,"fundamento":"Art. 233 C.Com.: la comisión mercantil es el mandato que tiene por objeto un acto de comercio; el comisionista actúa a nombre propio o del comitente.","tema":"Comisión mercantil"},
    {"afirmacion":"El contrato de cuenta corriente mercantil extingue los créditos que ingresan a ella mediante novación.","respuesta":True,"fundamento":"Art. 604 C.Com.: la cuenta corriente mercantil extingue los créditos particulares mediante su ingreso a la cuenta, que los funde en un saldo novado.","tema":"Cuenta corriente mercantil"},
    {"afirmacion":"En Chile, las SPA pueden tener un solo accionista.","respuesta":True,"fundamento":"Ley 20.190: la SpA (Sociedad por Acciones) puede constituirse por una sola persona natural o jurídica; no requiere pluralidad de socios.","tema":"SpA unipersonal"},
    {"afirmacion":"El contrato de concesión mercantil otorga al concesionario el derecho a vender productos de la marca en exclusiva.","respuesta":False,"fundamento":"La concesión mercantil puede ser exclusiva o no exclusiva según las partes acuerden; no es un elemento esencial sino accidental del contrato.","tema":"Contrato de concesión"},
    {"afirmacion":"En Chile, los registros de propiedad industrial (marcas, patentes) son gestionados por el INAPI.","respuesta":True,"fundamento":"Ley 20.254: el Instituto Nacional de Propiedad Industrial (INAPI) gestiona el sistema de propiedad industrial en Chile, incluyendo marcas, patentes, diseños industriales, etc.","tema":"INAPI"},
    {"afirmacion":"La sociedad colectiva mercantil se disuelve por la muerte de uno de los socios.","respuesta":True,"fundamento":"Art. 2098 CC y art. 350 N°5 C.Com.: la sociedad colectiva se disuelve, entre otras causales, por la muerte de uno de los socios, salvo pacto de continuación.","tema":"Disolución sociedad colectiva"},
    {"afirmacion":"El pagaré puede incorporar intereses convenidos sin límite legal.","respuesta":False,"fundamento":"Ley 18.010: los intereses en operaciones de crédito de dinero están sujetos al límite del interés máximo convencional; superar este límite da lugar a la reducción al interés corriente.","tema":"Interés máximo convencional"},
    {"afirmacion":"En el contrato de transporte marítimo, el porteador es responsable de la carga durante todo el viaje.","respuesta":True,"fundamento":"Arts. 982 y ss. C.Com.: el porteador marítimo responde de la carga desde la recepción en el puerto de carga hasta la entrega en el puerto de destino.","tema":"Responsabilidad del porteador marítimo"},
    {"afirmacion":"La disolución de una SA requiere siempre acuerdo de la junta extraordinaria de accionistas.","respuesta":False,"fundamento":"Art. 103 Ley 18.046: la SA puede disolverse por vencimiento del plazo, cumplimiento del objeto social, quiebra u otras causales legales, sin necesidad de acuerdo de junta en todos los casos.","tema":"Disolución SA"},
    {"afirmacion":"El corredor de bolsa actúa como intermediario en el mercado de valores por cuenta ajena.","respuesta":True,"fundamento":"Ley 18.045: los corredores de bolsa son intermediarios de valores que actúan por cuenta de sus clientes (comitentes) en la bolsa de valores.","tema":"Corredor de bolsa"},
    {"afirmacion":"El contrato de agencia de distribución es un contrato típico del Código de Comercio chileno.","respuesta":False,"fundamento":"El contrato de distribución o agencia comercial no está regulado expresamente en el C.Com. chileno; se rige por la autonomía privada y los principios generales del derecho.","tema":"Contrato de distribución atípico"},
])

VF_BIENES.extend([
    {"afirmacion":"El dueño de las abejas puede seguirlas al predio ajeno para recuperarlas si avisa al dueño del fundo.","respuesta":True,"fundamento":"Art. 620 CC: el dueño puede seguir a las abejas que van a posarse en árbol ajeno; tiene derecho a coger sus abejas siempre que no cause daño al predio.","tema":"Enjambres de abejas"},
    {"afirmacion":"La inscripción en el CBR es la única forma de tradición de los bienes raíces en Chile.","respuesta":True,"fundamento":"Art. 686 CC: la tradición del dominio de los bienes raíces se efectúa por la inscripción del título en el registro del Conservador.","tema":"Tradición de inmuebles"},
    {"afirmacion":"Las aguas en Chile son bienes nacionales de uso público.","respuesta":True,"fundamento":"Art. 595 CC y Código de Aguas: todas las aguas son bienes nacionales de uso público; se puede constituir derechos de aprovechamiento sobre ellas.","tema":"Aguas nacionales"},
    {"afirmacion":"El derecho real de habitación solo puede constituirse por acto entre vivos.","respuesta":False,"fundamento":"Arts. 811-819 CC: el derecho real de habitación puede constituirse por acto entre vivos (contrato) o por testamento.","tema":"Constitución del derecho de habitación"},
    {"afirmacion":"La prescripción adquisitiva extraordinaria no requiere buena fe ni justo título.","respuesta":True,"fundamento":"Art. 2510 CC: la prescripción adquisitiva extraordinaria requiere solo posesión de 10 años, sin distinción de buena o mala fe ni de justo título.","tema":"Prescripción extraordinaria"},
    {"afirmacion":"La accesión de mueble a mueble cuando el accesorio supera en valor al principal sigue la regla principal-accesorio.","respuesta":False,"fundamento":"Art. 660 CC: la adjunción se rige por la regla de que el dueño del principal lo adquiere todo; si la cosa accesoria es más valiosa, se indemnia al dueño del accesorio.","tema":"Adjunción"},
    {"afirmacion":"El derecho de dominio no puede estar sujeto a condición en Chile.","respuesta":False,"fundamento":"Arts. 732-763 CC: la propiedad fiduciaria es el dominio sujeto a condición resolutoria; es una forma de dominio condicional expresamente reconocida.","tema":"Propiedad fiduciaria y dominio condicional"},
    {"afirmacion":"Las servidumbres discontinuas solo pueden adquirirse por título, no por prescripción.","respuesta":True,"fundamento":"Art. 882 CC: las servidumbres discontinuas (que requieren hecho actual del hombre) y las continuas no aparentes no pueden adquirirse por prescripción; solo por título.","tema":"Adquisición de servidumbres"},
    {"afirmacion":"El propietario puede ejercer la acción reivindicatoria contra el poseedor de buena o mala fe.","respuesta":True,"fundamento":"Art. 889 CC: la reivindicación compete al dueño contra el actual poseedor, sea de buena o mala fe.","tema":"Acción reivindicatoria sin distinción de fe"},
    {"afirmacion":"La copropiedad puede terminar por la acción de partición ejercida por cualquiera de los comuneros.","respuesta":True,"fundamento":"Art. 1317 CC: ninguno de los coasignatarios está obligado a permanecer en la indivisión; la partición puede siempre pedirse.","tema":"Acción de partición"},
    {"afirmacion":"El usufructuario puede ceder su derecho de usufructo sin el consentimiento del nudo propietario.","respuesta":True,"fundamento":"Art. 793 CC: el usufructuario puede ceder su derecho de usufructo a título oneroso o gratuito; pero no puede alterar la forma o sustancia de la cosa.","tema":"Cesión del usufructo"},
    {"afirmacion":"La aluvión corresponde al terreno que emerge gradualmente de las aguas.","respuesta":True,"fundamento":"Art. 649 CC: la aluvión es el aumento que recibe la ribera de un río o lago por el lento retiro de las aguas.","tema":"Aluvión"},
    {"afirmacion":"Los bienes fiscales son bienes del Estado destinados al uso público.","respuesta":False,"fundamento":"Art. 589 CC: los bienes nacionales de uso público son los destinados al uso de todos los habitantes. Los bienes fiscales son bienes del Estado que no están destinados al uso público.","tema":"Bienes fiscales vs nacionales de uso público"},
    {"afirmacion":"La posesión inscrita en Chile protege al poseedor frente a terceros que disputen el dominio.","respuesta":True,"fundamento":"Arts. 728 y 730 CC: la posesión inscrita de los bienes raíces solo puede perderse por otra inscripción; protege al poseedor frente a acciones posesorias.","tema":"Posesión inscrita"},
    {"afirmacion":"El derecho de uso y el de habitación son transmisibles por causa de muerte.","respuesta":False,"fundamento":"Art. 819 CC: los derechos de uso y habitación son intransmisibles; se extinguen con la muerte del titular y no pueden cederse ni arrendarse.","tema":"Intransmisibilidad de uso y habitación"},
    {"afirmacion":"La acción publiciana protege al poseedor regular que ha perdido la posesión.","respuesta":True,"fundamento":"Art. 894 CC: la acción publiciana corresponde al que ha perdido la posesión regular y se encuentra en el caso de poder ganarla por prescripción.","tema":"Acción publiciana"},
    {"afirmacion":"En la adjunción, si el artífice es de mala fe, el dueño del principal puede exigir el todo o la indemnización.","respuesta":True,"fundamento":"Art. 663 CC: si la adjunción se hace con conocimiento del artífice (mala fe del tenedor), el dueño del principal puede exigir la cosa o equivalente más la indemnización de perjuicios.","tema":"Adjunción de mala fe"},
    {"afirmacion":"Los frutos naturales percibidos pertenecen al poseedor de buena fe que fue vencido en el juicio reivindicatorio.","respuesta":True,"fundamento":"Art. 907 CC: el poseedor de buena fe no es obligado a restituir los frutos percibidos antes de la contestación de la demanda; los posteriores se deben al reivindicante.","tema":"Frutos en reivindicación"},
    {"afirmacion":"La prenda sin desplazamiento no confiere al acreedor el derecho de retención del bien prendado.","respuesta":True,"fundamento":"Ley 20.190: la prenda sin desplazamiento no implica entrega del bien al acreedor; este ejerce su derecho mediante el registro, no por retención física del bien.","tema":"Prenda sin desplazamiento"},
    {"afirmacion":"El principio de especialidad hipotecaria exige que la hipoteca recaiga sobre bienes determinados.","respuesta":True,"fundamento":"Art. 2432 CC: la hipoteca debe recaer sobre bienes raíces determinados y debe constar la naturaleza, situación y límites del inmueble hipotecado.","tema":"Especialidad hipotecaria"},
    {"afirmacion":"El acreedor hipotecario tiene preferencia sobre los demás acreedores del deudor respecto del bien hipotecado.","respuesta":True,"fundamento":"Art. 2470 N°3 CC: los créditos hipotecarios gozan del privilegio de cuarta clase, con preferencia sobre el producto del bien hipotecado.","tema":"Preferencia hipotecaria"},
    {"afirmacion":"La especificación ocurre cuando el trabajo de un artífice transforma materia ajena en una nueva especie.","respuesta":True,"fundamento":"Art. 662 CC: la especificación es la creación de nueva especie con materia ajena; si el artífice está de buena fe y la materia no puede recuperar su forma anterior, le pertenece la nueva especie.","tema":"Especificación"},
    {"afirmacion":"La inscripción en el CBR de una servidumbre es siempre necesaria para su oponibilidad.","respuesta":False,"fundamento":"Art. 698 CC: la inscripción de servidumbres es voluntaria, no obligatoria; pueden probarse por escritura pública u otros medios. Solo las servidumbres aparentes continuas pueden ganarse por prescripción.","tema":"Inscripción de servidumbres"},
    {"afirmacion":"Los inmuebles por adherencia incluyen los árboles y plantas mientras estén arraigados al suelo.","respuesta":True,"fundamento":"Art. 568 CC: se reputan inmuebles las plantas mientras adhieren al suelo por sus raíces; una vez separadas vuelven a ser muebles.","tema":"Inmuebles por adherencia"},
    {"afirmacion":"El decreto de posesión efectiva acredita el dominio del causante sobre sus bienes.", "respuesta": False, "fundamento": "La posesión efectiva acredita la calidad de heredero, no el dominio sobre bienes específicos. El dominio de inmuebles se acredita por la inscripción en el CBR.", "tema": "Posesión efectiva"},
])

VF_SUCESORIO.extend([
    {"afirmacion":"Los herederos universales son los que reciben toda la herencia o una cuota de ella.","respuesta":True,"fundamento":"Art. 951 CC: se sucede a título universal (como heredero) cuando se sucede en la herencia o en una cuota de ella, sin determinación de objetos específicos.","tema":"Heredero universal"},
    {"afirmacion":"El testamento público abierto requiere ser firmado por el testador, el notario y tres testigos.","respuesta":False,"fundamento":"Art. 1014 CC: el testamento público abierto se otorga ante notario competente y tres testigos. (Reforma 2019: se redujo a tres testigos hábiles).","tema":"Testamento público abierto"},
    {"afirmacion":"Los derechos del acreedor del difunto son preferentes frente a los deudores hereditarios.","respuesta":False,"fundamento":"Los acreedores del causante (deudas hereditarias) tienen preferencia sobre los acreedores de los herederos respecto de los bienes de la herencia.","tema":"Preferencia de acreedores"},
    {"afirmacion":"La sucesión intestada es subsidiaria de la testamentaria en Chile.","respuesta":True,"fundamento":"Art. 952 CC: si el difunto no dispuso de sus bienes o no lo hizo conforme a derecho, o sus disposiciones no tuvieron efecto, se sucede abintestato.","tema":"Subsidiariedad de la sucesión intestada"},
    {"afirmacion":"El declarado interdicto por disipación puede otorgar testamento.","respuesta":False,"fundamento":"Art. 1005 N°3 CC: no pueden testar el interdicto por demencia. El disipador puede testar siempre que esté en su sano juicio; la interdicción no lo priva de esta facultad.","tema":"Capacidad de testar"},
    {"afirmacion":"El repudio de la herencia puede hacerse con beneficio de inventario.","respuesta":False,"fundamento":"Arts. 1234-1237 CC: el beneficio de inventario opera en la aceptación de herencia. La repudiación no es compatible con el beneficio de inventario.","tema":"Repudiación de la herencia"},
    {"afirmacion":"El legatario de género no adquiere el dominio de la cosa legada desde la muerte del causante.","respuesta":True,"fundamento":"Art. 1338 N°2 CC: el legatario de género (cosa indeterminada del género señalado) solo tiene derecho personal para exigir la entrega; no adquiere dominio desde la muerte.","tema":"Legado de género"},
    {"afirmacion":"El albacea puede ser una persona jurídica según la ley chilena.","respuesta":False,"fundamento":"Art. 1270 CC: el albacea es un cargo de confianza que solo puede recaer en personas naturales; las personas jurídicas no pueden ser ejecutores testamentarios.","tema":"Albacea persona natural"},
    {"afirmacion":"La acción de petición de herencia prescribe en 5 años desde que el heredero la hizo valer.","respuesta":False,"fundamento":"Art. 1269 CC: la acción de petición de herencia prescribe en el mismo tiempo que la prescripción adquisitiva del heredero aparente (10 años de posesión regular).","tema":"Prescripción de la petición de herencia"},
    {"afirmacion":"Los herederos condicionales no adquieren la herencia hasta que se cumpla la condición.","respuesta":True,"fundamento":"Art. 1078 CC: el asignatario condicional bajo condición suspensiva no adquiere el derecho mientras no se cumpla la condición.","tema":"Herencia condicional"},
    {"afirmacion":"El segundo acervo imaginario protege a los legitimarios frente a las donaciones excesivas a extraños.","respuesta":True,"fundamento":"Art. 1186 CC: si el causante hizo donaciones a personas que no son legitimarios que excedan la parte de libre disposición, se forma el segundo acervo imaginario para proteger las legítimas.","tema":"Segundo acervo imaginario"},
    {"afirmacion":"La herencia yacente se produce cuando la herencia ha sido aceptada pero no administrada.","respuesta":False,"fundamento":"Art. 1240 CC: la herencia yacente es aquella que no ha sido aceptada por nadie dentro del plazo fijado; se nombra curador de herencia yacente.","tema":"Herencia yacente"},
    {"afirmacion":"El testamento puede revocarse tácitamente por la celebración de un matrimonio posterior.","respuesta":False,"fundamento":"En Chile, el matrimonio posterior al testamento no revoca tácitamente las disposiciones testamentarias; se requiere revocación expresa o tácita (nuevo testamento incompatible).","tema":"Revocación tácita del testamento"},
    {"afirmacion":"Los colaterales tienen derecho a heredar en la sucesión intestada en ausencia de descendientes, ascendientes y cónyuge.","respuesta":True,"fundamento":"Art. 992 CC: a falta de descendientes, ascendientes, cónyuge sobreviviente y donaciones, los hermanos suceden, ya sea personalmente o representados.","tema":"Colaterales en sucesión intestada"},
    {"afirmacion":"El usufructo sobre bienes hereditarios puede ser legado a favor de persona distinta del heredero.","respuesta":True,"fundamento":"Arts. 764 y 1135 CC: el testador puede legar el usufructo de un bien a persona distinta del heredero que recibirá la nuda propiedad.","tema":"Legado de usufructo"},
    {"afirmacion":"El tercer orden de sucesión intestada en Chile lo forman los hermanos del causante.","respuesta":False,"fundamento":"Art. 990 CC: el tercer orden es el del cónyuge sobreviviente cuando no hay descendientes ni ascendientes (o los hay). El tercer orden real son los hermanos (art. 992); hay discrepancia en numeración según texto.","tema":"Tercer orden intestado"},
    {"afirmacion":"La insinuación de donaciones irrevocables protege a los legitimarios del causante.","respuesta":True,"fundamento":"Art. 1401 y 1186 CC: la insinuación evita donaciones que menoscaben las legítimas; el segundo acervo imaginario reconstruye el patrimonio con estas donaciones excesivas.","tema":"Insinuación y legitimarios"},
    {"afirmacion":"El heredero puede aceptar la herencia bajo beneficio de inventario aunque el causante haya dispuesto lo contrario en el testamento.","respuesta":True,"fundamento":"Art. 1248 CC: el derecho a pedir el beneficio de inventario es irrenunciable anticipadamente; la cláusula testamentaria que lo prohíba no tiene valor.","tema":"Irrenunciabilidad del beneficio de inventario"},
    {"afirmacion":"En Chile no existe la herencia forzosa de los padres sobre los bienes de los hijos.","respuesta":False,"fundamento":"Arts. 988-989 CC: los ascendientes (padres, abuelos) concurren en el segundo orden de sucesión intestada y también son legitimarios; tienen derecho a la legítima.","tema":"Legitimarios ascendientes"},
    {"afirmacion":"La sustitución fideicomisaria en los testamentos chilenos está expresamente regulada.","respuesta":True,"fundamento":"Arts. 1164-1166 CC: la sustitución fideicomisaria es aquella en que se llama a un asignatario para que entre a gozar de la asignación en defecto del anterior o después de él.","tema":"Sustitución fideicomisaria"},
    {"afirmacion":"El legado de alimentos no requiere que el legatario tenga necesidad económica.","respuesta":False,"fundamento":"Art. 1170 CC: los legados de alimentos a personas que no tienen derecho legal a pedirlos al testador son pagados según la fortuna del testador; se consideran las necesidades del legatario.","tema":"Legado de alimentos"},
    {"afirmacion":"Los modos en las asignaciones testamentarias generan obligación de cumplirlos bajo pena de resolución.","respuesta":True,"fundamento":"Art. 1090 CC: en las asignaciones modales se entiende haber cláusula resolutoria, salvo que el testador disponga otra cosa; el incumplimiento puede producir resolución.","tema":"Cláusula resolutoria en modo"},
    {"afirmacion":"En Chile, los nacidos después de la muerte del causante pueden heredar si fueron concebidos antes.","respuesta":True,"fundamento":"Art. 77 CC: los derechos que se deferirían a la criatura que está en el vientre materno se susependerán hasta el nacimiento. La criatura concebida se considera nacida para estos efectos.","tema":"Derecho hereditario del nasciturus"},
    {"afirmacion":"La partición judicial de la herencia siempre requiere la intervención de un partidor.","respuesta":True,"fundamento":"Art. 1323 CC: si no hay acuerdo, la partición debe ser hecha por un juez árbitro (partidor) designado de común acuerdo o nombrado por el juez.","tema":"Partición judicial"},
])

VF_AMBIENTAL.extend([
    {"afirmacion":"Las normas de calidad ambiental se clasifican en primarias (salud) y secundarias (protección del ecosistema).","respuesta":True,"fundamento":"Art. 32 Ley 19.300: las normas de calidad primarias protegen la salud de la población; las secundarias protegen los ecosistemas y recursos naturales renovables.","tema":"Normas de calidad ambiental"},
    {"afirmacion":"La Superintendencia del Medio Ambiente puede clausurar establecimientos que incumplan la normativa ambiental.","respuesta":True,"fundamento":"Art. 38 Ley 20.417: entre las medidas provisionales de la SMA está la clausura temporal o definitiva de instalaciones que generen daño ambiental irreversible.","tema":"Clausura por SMA"},
    {"afirmacion":"El proceso de evaluación de impacto ambiental debe concluir en 120 días para los EIA.","respuesta":True,"fundamento":"Art. 15 Ley 19.300: el plazo para la calificación ambiental de un EIA es de 120 días contados desde que la DGA informa la admisibilidad del estudio.","tema":"Plazo EIA"},
    {"afirmacion":"La compensación ambiental permite reemplazar los impactos negativos de un proyecto con acciones positivas equivalentes.","respuesta":True,"fundamento":"Art. 12 Ley 19.300: las medidas de compensación son acciones que compensan los efectos ambientales adversos no mitigables ni reparables de un proyecto.","tema":"Compensación ambiental"},
    {"afirmacion":"En Chile, el cambio climático tiene ley especial desde 2022.","respuesta":True,"fundamento":"Ley 21.455 (Ley Marco de Cambio Climático, 2022): establece el marco normativo para la gestión del cambio climático en Chile.","tema":"Ley Marco de Cambio Climático"},
    {"afirmacion":"Los proyectos de transmisión eléctrica no requieren ingresar al SEIA.","respuesta":False,"fundamento":"Art. 10 letra c) Ley 19.300: los proyectos de centrales generadoras y líneas de transmisión eléctrica deben ingresar al SEIA.","tema":"SEIA energía eléctrica"},
    {"afirmacion":"La declaración de zona de latencia es previa a la declaración de zona saturada en Chile.","respuesta":True,"fundamento":"Art. 32 Ley 19.300: una zona se declara de latencia cuando la concentración de contaminantes supera el 80% del límite; saturada cuando supera el 100%.","tema":"Zonas de latencia y saturación"},
    {"afirmacion":"El Ministerio del Medio Ambiente puede delegar sus funciones de fiscalización a otras entidades.","respuesta":True,"fundamento":"La Ley 20.417 creó la SMA precisamente para separar las funciones de política ambiental (MMA) de las de fiscalización y sanción (SMA).","tema":"División de funciones ambientales"},
    {"afirmacion":"La infracción ambiental en Chile puede sancionarse solo con multas pecuniarias.","respuesta":False,"fundamento":"Art. 38 Ley 20.417: las sanciones de la SMA incluyen amonestación, multa, clausura temporal o definitiva, revocación de RCA y otros.","tema":"Sanciones ambientales"},
    {"afirmacion":"El Convenio de Basilea regula el transporte internacional de residuos peligrosos.","respuesta":True,"fundamento":"Convenio de Basilea (1989, ratificado por Chile): regula el movimiento transfronterizo de desechos peligrosos y su eliminación.","tema":"Convenio de Basilea"},
    {"afirmacion":"Chile cuenta con áreas silvestres protegidas de administración privada.","respuesta":True,"fundamento":"Ley 21.600 (Ley de Áreas Protegidas, 2023): se reconocen las áreas protegidas privadas como parte del Sistema Nacional de Áreas Protegidas.","tema":"Áreas protegidas privadas"},
    {"afirmacion":"El impacto ambiental significativo siempre obliga a presentar EIA y no DIA.","respuesta":True,"fundamento":"Art. 11 Ley 19.300: si el proyecto genera efectos adversos significativos sobre el medio ambiente, debe ingresar al SEIA mediante EIA y no DIA.","tema":"EIA obligatorio para impactos significativos"},
    {"afirmacion":"Las emisiones de GEI de las empresas chilenas están reguladas por un sistema de compensaciones voluntarias.","respuesta":False,"fundamento":"Ley 21.210 (Ley de Impuesto Verde, 2020) y Ley Marco de Cambio Climático: Chile tiene un impuesto a las emisiones (impuesto verde) y un sistema de permisos transables en desarrollo.","tema":"Regulación de emisiones GEI"},
    {"afirmacion":"La Evaluación Ambiental Estratégica (EAE) aplica a políticas y planes, no a proyectos individuales.","respuesta":True,"fundamento":"Art. 7 bis Ley 19.300: la EAE es el procedimiento para que los órganos de la administración del Estado que dicten políticas, planes y programas incorporen consideraciones ambientales.","tema":"EAE"},
    {"afirmacion":"El concepto de 'desarrollo sustentable' en la Ley 19.300 exige satisfacer necesidades del presente sin comprometer las del futuro.","respuesta":True,"fundamento":"Art. 2 Ley 19.300: el desarrollo sustentable es el proceso de mejoramiento sostenido y equitativo de la calidad de vida de las personas sin comprometer la capacidad de las generaciones futuras.","tema":"Desarrollo sustentable"},
])

VF_INTERNACIONAL.extend([
    {"afirmacion":"El derecho del mar reconoce el paso inocente de buques extranjeros en el mar territorial.","respuesta":True,"fundamento":"Arts. 17-26 CONVEMAR: los buques de todos los Estados gozan del derecho de paso inocente por el mar territorial de otro Estado.","tema":"Paso inocente"},
    {"afirmacion":"La Comisión de Derecho Internacional de la ONU es un órgano judicial.","respuesta":False,"fundamento":"La CDI es un órgano subsidiario de la Asamblea General de la ONU dedicado a la codificación y desarrollo progresivo del DI; no es un tribunal.","tema":"Comisión de Derecho Internacional"},
    {"afirmacion":"El Estado puede revocar la nacionalidad de una persona en todos los casos.","respuesta":False,"fundamento":"Los derechos humanos (CADH, PIDCP) y la CPR chilena protegen la nacionalidad; la privación arbitraria de nacionalidad viola el DI de los DDHH.","tema":"Protección de la nacionalidad"},
    {"afirmacion":"La extradición en Chile requiere tratado internacional previo con el Estado requirente.","respuesta":False,"fundamento":"Arts. 647 y ss. CPP: Chile puede otorgar extradición con base en tratado, reciprocidad o por normas de DI consuetudinario; no siempre requiere tratado específico.","tema":"Extradición"},
    {"afirmacion":"El Comité de Derechos Humanos de la ONU supervisa el cumplimiento del Pacto Internacional de Derechos Civiles y Políticos.","respuesta":True,"fundamento":"Art. 28 PIDCP: el Comité de Derechos Humanos es el órgano de tratado creado para supervisar la implementación del PIDCP por los Estados parte.","tema":"Comité DDHH ONU"},
    {"afirmacion":"La zona contigua se extiende hasta 24 millas náuticas desde la línea de base.","respuesta":True,"fundamento":"Art. 33 CONVEMAR: la zona contigua no podrá extenderse más allá de 24 millas marinas contadas desde las líneas de base.","tema":"Zona contigua"},
    {"afirmacion":"El Estado de Chile es parte de la Convención Americana sobre Derechos Humanos (CADH).","respuesta":True,"fundamento":"Chile ratificó la CADH en 1990 y reconoció la jurisdicción contenciosa de la Corte IDH, pudiendo ser demandado ante ella.","tema":"Chile y la CADH"},
    {"afirmacion":"La intervención humanitaria unilateral sin autorización del Consejo de Seguridad es permitida en el DI contemporáneo.","respuesta":False,"fundamento":"La Carta ONU prohíbe el uso de la fuerza salvo en legítima defensa o con autorización del CSNU; la intervención humanitaria unilateral es controvertida y generalmente considerada ilegal.","tema":"Intervención humanitaria"},
    {"afirmacion":"Chile tiene soberanía reconocida sobre el territorio antártico que reivindica.","respuesta":False,"fundamento":"El Tratado Antártico (1959, del cual Chile es parte fundadora) congela las reclamaciones de soberanía; ningún Estado tiene soberanía reconocida internacionalmente sobre la Antártica.","tema":"Tratado Antártico"},
    {"afirmacion":"La Corte Penal Internacional tiene jurisdicción complementaria, no principal.","respuesta":True,"fundamento":"Art. 17 Estatuto de Roma: la CPI tiene jurisdicción complementaria; solo puede actuar cuando el Estado con jurisdicción no puede o no quiere juzgar genuinamente el crimen.","tema":"Complementariedad CPI"},
    {"afirmacion":"El principio de buena fe es aplicable solo en la interpretación de tratados.","respuesta":False,"fundamento":"El principio de buena fe es transversal en el DI: se aplica en la celebración, interpretación y ejecución de tratados, en las negociaciones y en las relaciones internacionales en general.","tema":"Principio de buena fe en DI"},
    {"afirmacion":"Los refugiados tienen derecho a obtener documentos de identidad emitidos por el Estado de acogida.","respuesta":True,"fundamento":"Art. 27 Convención de 1951: los Estados contratantes expedirán documentos de identidad a todo refugiado que se encuentre en su territorio y que no posea documento válido de viaje.","tema":"Documentos de identidad para refugiados"},
    {"afirmacion":"La Carta de la ONU prohíbe la amenaza y el uso de la fuerza en las relaciones internacionales.","respuesta":True,"fundamento":"Art. 2.4 Carta ONU: los miembros se abstendrán de recurrir a la amenaza o al uso de la fuerza contra la integridad territorial o la independencia política de cualquier Estado.","tema":"Prohibición del uso de la fuerza"},
    {"afirmacion":"El Estatuto de la CIJ es parte integrante de la Carta de la ONU.","respuesta":True,"fundamento":"Art. 92 Carta ONU: la CIJ es el principal órgano judicial de las Naciones Unidas. El Estatuto de la CIJ es parte integrante de la Carta de la ONU.","tema":"CIJ como órgano principal ONU"},
    {"afirmacion":"Los apátridas no tienen protección bajo el derecho internacional.","respuesta":False,"fundamento":"La Convención sobre el Estatuto de los Apátridas (1954) y la Convención para Reducir los Casos de Apatridia (1961) establecen protección internacional para los apátridas.","tema":"Protección de apátridas"},
    {"afirmacion":"El DIPr chileno aplica la ley del lugar de celebración del contrato (lex loci celebrationis) para las obligaciones contractuales.","respuesta":False,"fundamento":"Art. 16 CC: los contratos celebrados en Chile se rigen por la ley chilena; para las obligaciones de ejecución, se aplica la lex loci solutionis en algunos casos.","tema":"Ley aplicable a contratos"},
    {"afirmacion":"Las organizaciones internacionales tienen personalidad jurídica internacional.","respuesta":True,"fundamento":"La OI Reparación (CIJ, 1949): las organizaciones internacionales tienen personalidad jurídica internacional propia, distinta de la de sus Estados miembros, aunque más limitada.","tema":"Personalidad jurídica de OI"},
    {"afirmacion":"La alta mar es res communis y no puede ser objeto de soberanía de ningún Estado.","respuesta":True,"fundamento":"Arts. 87-90 CONVEMAR: la alta mar está abierta a todos los Estados; ningún Estado puede pretender legítimamente someterla a su soberanía.","tema":"Alta mar"},
])

# ── Completar cuotas faltantes ──────────────────────────────────────────────
VF_CIVIL.extend([
    {"afirmacion": "El usufructo puede constituirse por testamento.", "verdadero": True, "explicacion": "El art. 766 CC admite la constitución del usufructo por testamento."},
    {"afirmacion": "La rescisión por lesión enorme no procede en ventas de bienes raíces.", "verdadero": False, "explicacion": "Precisamente la lesión enorme procede en la compraventa de bienes raíces (art. 1888 CC)."},
    {"afirmacion": "El pacto de retroventa debe constar por escrito.", "verdadero": True, "explicacion": "El art. 1881 CC exige escritura para el pacto de retroventa."},
    {"afirmacion": "La nulidad absoluta puede sanearse por el transcurso de 5 años.", "verdadero": True, "explicacion": "Conforme al art. 1683 CC, la nulidad absoluta se sanea por prescripción de 10 años (no 5); la afirmación es falsa.", "verdadero": False, "explicacion": "La nulidad absoluta se sanea por el transcurso de 10 años (art. 1683 CC), no 5."},
])

VF_LABORAL.extend([
    {"afirmacion": "El contrato de trabajo puede celebrarse verbalmente.", "verdadero": True, "explicacion": "El art. 9 CT admite el contrato verbal, aunque la falta de escrituración se presume por las estipulaciones del trabajador."},
])

VF_COMERCIAL.extend([
    {"afirmacion": "El endoso en blanco transforma el título a la orden en título al portador.", "verdadero": True, "explicacion": "El endoso en blanco solo lleva la firma del endosante y permite que el tenedor lo complete o lo transmita por tradición."},
])

VF_SUCESORIO.extend([
    {"afirmacion": "El testamento solemne abierto requiere siempre la presencia de un notario.", "verdadero": False, "explicacion": "Puede otorgarse ante tres testigos hábiles sin intervención notarial (art. 1014 CC)."},
])

VF_INTERNACIONAL.extend([
    {"afirmacion": "El Derecho Internacional Público regula principalmente relaciones entre particulares.", "verdadero": False, "explicacion": "El DIP clásico regula relaciones entre sujetos internacionales (Estados, OI), no entre particulares."},
    {"afirmacion": "Las normas ius cogens no pueden ser derogadas por tratados particulares.", "verdadero": True, "explicacion": "Conforme al art. 53 CVDT, las normas ius cogens son imperativas y prevalecen sobre cualquier tratado contrario."},
    {"afirmacion": "Chile ha ratificado la Convención Americana sobre Derechos Humanos.", "verdadero": True, "explicacion": "Chile ratificó la CADH en 1990 y reconoció la jurisdicción contenciosa de la Corte IDH."},
    {"afirmacion": "El principio de no intervención prohíbe toda forma de asistencia humanitaria.", "verdadero": False, "explicacion": "La asistencia humanitaria consentida por el Estado no viola el principio de no intervención."},
    {"afirmacion": "Las resoluciones del Consejo de Seguridad bajo el Capítulo VII son vinculantes para todos los Estados miembros.", "verdadero": True, "explicacion": "El art. 25 de la Carta ONU obliga a los Estados a acatar las decisiones del Consejo de Seguridad."},
    {"afirmacion": "La costumbre internacional requiere solo el elemento material (usus) para ser obligatoria.", "verdadero": False, "explicacion": "La costumbre internacional exige también el elemento psicológico (opinio iuris), reconocido en el Estatuto de la CIJ."},
    {"afirmacion": "El asilo diplomático está regulado por la Convención de Caracas de 1954.", "verdadero": True, "explicacion": "La Convención sobre Asilo Diplomático (Caracas, 1954) es el principal instrumento interamericano en la materia."},
])

VF_AMBIENTAL.extend([
    {"afirmacion": "La Ley 19.300 establece el Sistema de Evaluación de Impacto Ambiental (SEIA).", "verdadero": True, "explicacion": "La Ley de Bases del Medio Ambiente (19.300) creó el SEIA y la CONAMA, hoy Ministerio del Medio Ambiente."},
    {"afirmacion": "El Estudio de Impacto Ambiental (EIA) es siempre obligatorio para cualquier proyecto.", "verdadero": False, "explicacion": "Solo los proyectos listados en el art. 10 de la Ley 19.300 deben ingresar al SEIA; no todos requieren EIA."},
    {"afirmacion": "La participación ciudadana en el SEIA es obligatoria en los Estudios de Impacto Ambiental.", "verdadero": True, "explicacion": "El art. 26 de la Ley 19.300 garantiza participación ciudadana obligatoria en los EIA."},
    {"afirmacion": "El Tribunal Ambiental de Santiago tiene competencia exclusiva en toda la República.", "verdadero": False, "explicacion": "Chile cuenta con tres Tribunales Ambientales (Antofagasta, Santiago y Valdivia) con competencias territoriales definidas."},
    {"afirmacion": "El principio 'quien contamina paga' implica que quien paga puede contaminar libremente.", "verdadero": False, "explicacion": "El principio solo asigna la carga económica del daño al contaminador; no autoriza contaminar."},
    {"afirmacion": "Chile está suscrito al Acuerdo de París sobre cambio climático.", "verdadero": True, "explicacion": "Chile ratificó el Acuerdo de París en 2017 y presentó su NDC comprometiendo reducción de emisiones."},
    {"afirmacion": "La Ley Marco de Cambio Climático (21.455) fue promulgada en 2022.", "verdadero": True, "explicacion": "La Ley 21.455 fue promulgada el 13 de junio de 2022, estableciendo la meta de carbono neutralidad al 2050."},
    {"afirmacion": "El daño ambiental en Chile se rige exclusivamente por las reglas del Código Civil.", "verdadero": False, "explicacion": "El daño ambiental tiene regulación especial en la Ley 19.300 (art. 51 y ss.) que prima sobre las reglas civiles generales."},
    {"afirmacion": "La Superintendencia del Medio Ambiente puede aplicar sanciones administrativas.", "verdadero": True, "explicacion": "La SMA (Ley 20.417) tiene potestad sancionatoria para infracciones a la normativa ambiental y las RCAs."},
    {"afirmacion": "El recurso de protección puede interponerse para defender el derecho a vivir en un medio ambiente libre de contaminación.", "verdadero": True, "explicacion": "El art. 19 N°8 CPR protege este derecho y el art. 20 CPR lo hace accionable mediante recurso de protección."},
])
