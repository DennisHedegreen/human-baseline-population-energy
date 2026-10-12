"""Four-language presentation for the uniform-energy edition."""
LANGUAGES = {"en": "English", "da": "Dansk", "es": "Español", "de": "Deutsch"}
TEXT = {
 "en": {
  "title": "Human Baseline", "subtitle": "Population and energy: start with the scale of the question.",
  "intro": "Human Baseline explores what it would take to make adequate food a reliable foundation for everyone, rather than a constant survival contest. This first tool does one simple calculation: population × your chosen kcal per person per day. Foods, nutrients, prices, production and delivery come later.",
  "view": "View", "explore": "Explore a country", "compare": "Compare countries", "eu": "EU27 overview", "custom": "Custom calculation", "about": "About & sources",
  "country": "Country", "countries": "Countries to compare", "number": "Number of people", "name": "Population name", "custom_name": "Custom population",
  "kcal": "Chosen kcal/person/day", "kcal_help": "A planning assumption you choose, applied equally to every person. 3,000 is an editable example, not a dietary recommendation. Include any desired energy margin in this number; no extra buffer is added.",
  "number_help": "Your own headcount. It is not official statistics and does not inherit a country's age or sex distribution. Zero people gives zero total energy.",
  "day": "Total kcal/day", "month": "Average month · kcal", "year": "Annual · kcal",
  "day_help": "Population multiplied by your chosen kcal/person/day. Everyone is counted, including infants. No separate pregnancy or breastfeeding allowance is added.",
  "month_help": "Daily energy × 365 ÷ 12. This is an average month, not a particular calendar month.", "year_help": "Daily energy × 365. A repeated-day scenario, not a population or food-production forecast.",
  "assumption": "The same figure applies to everyone. Any energy margin is inside your chosen value. This is planned energy volume, not measured individual needs or proof that everyone receives a nutritionally adequate diet.",
  "people": "Population", "children": "Children 0–17", "adults": "Adults 18–70", "older": "Older people 71+", "female": "Female", "male": "Male", "unknown": "Unknown age",
  "people_help": "Recorded population on 1 January 2025. This is a statistical starting point, not a complete count of everyone present who may need food.",
  "age_help": "An age-group subtotal of the official population, not additional people. These demographics describe the population; they do not change the uniform kcal calculation.",
  "sex_help": "The source's reported female/male statistical categories, not a description of every person's gender identity. Subtotals must not be added again to total population.",
  "population_heading": "Who is counted?", "population_note": "Population snapshot: 1 January 2025. Age and source-sex breakdowns are context only in this edition.",
  "table_help": "Each selected country is included once. Every country uses the same chosen kcal value, so differences in energy totals follow differences in population.",
  "select_note": "Choose at least one country to calculate a comparison.", "exact": "Inspect the exact calculation", "download": "Download this scenario · JSON",
  "about_intro": "This is the simple population-and-energy edition of Human Baseline. It helps you explore energy volumes without presenting a selected diet or nutrition model as settled.",
  "method": "Calculation and margin", "method_text": "Daily = headcount × chosen kcal/person/day. Annual = daily × 365. Average month = annual ÷ 12. A higher chosen value gives a larger energy envelope; no additional buffer, waste factor, reserve or population-coverage adjustment is added automatically. Age, sex, pregnancy and breastfeeding do not change this calculation. The chosen number is a scenario input, not a validated allowance for every individual.",
  "sources": "Population source", "source_text": "Eurostat DEMO_PJAN, population on 1 January 2025 by age and reported sex, for the EU27. The preserved response was retrieved on 5 October 2026. The app uses a fixed local capture, not live data fetched on each visit. It checks country coverage, duplicate rows, whole-number counts and age/sex reconciliation. Later revisions do not silently alter this snapshot.",
  "limits": "What this tool does not establish", "limits_text": "Enough kcal in aggregate is not by itself proof of nutritional adequacy, production capacity or fair delivery. Food composition, vitamins, minerals, prices, land, storage, losses and distribution are future layers. Registered population can omit people needing food. Custom calculation uses your own total without inventing demographics. The earlier detailed reference model remains local research and is not bundled in this public edition.",
  "reuse": "Source attribution and reuse", "reuse_text": "Source: Eurostat. Own selection, formatting and calculations by Hedegreen Research. Statistical reuse is subject to Eurostat's published policy and exceptions; this is not an official Eurostat product or an endorsement. The chosen kcal figure is user input, not a value attributed to a nutrition institution.",
  "population_download": "Population by age and sex · CSV", "metadata_download": "Population capture metadata · JSON", "repo": "Source code", "article": "Companion article",
 },
 "da": {
  "title": "Human Baseline", "subtitle": "Befolkning og energi: begynd med spørgsmålets størrelsesorden.",
  "intro": "Human Baseline undersøger, hvad det kræver at gøre tilstrækkelig mad til et stabilt fundament for alle frem for en konstant kamp for overlevelse. Første værktøj laver ét enkelt regnestykke: befolkning × dit valgte kcal-tal pr. person pr. dag. Fødevarer, næring, priser, produktion og levering kommer senere.",
  "view": "Visning", "explore": "Udforsk et land", "compare": "Sammenlign lande", "eu": "EU27-overblik", "custom": "Egen beregning", "about": "Om værktøjet og kilder",
  "country": "Land", "countries": "Lande til sammenligning", "number": "Antal mennesker", "name": "Befolkningens navn", "custom_name": "Egen befolkning",
  "kcal": "Valgte kcal/person/dag", "kcal_help": "En planantagelse, du vælger, og som bruges ens for alle. 3.000 er et redigerbart eksempel, ikke en kostanbefaling. Medregn ønsket energimargin i dette tal; der lægges ingen ekstra buffer til.",
  "number_help": "Dit eget personantal. Det er ikke officiel statistik og arver ikke et lands alders- eller kønsfordeling. Nul personer giver nul samlet energi.",
  "day": "Samlet kcal/dag", "month": "Gennemsnitsmåned · kcal", "year": "Årligt · kcal",
  "day_help": "Befolkning ganget med dit valgte kcal-tal pr. person pr. dag. Alle tælles med, også spædbørn. Ingen særskilte graviditets- eller amningstillæg.",
  "month_help": "Daglig energi × 365 ÷ 12. En gennemsnitsmåned, ikke en bestemt kalendermåned.", "year_help": "Daglig energi × 365. Et scenarie med gentagne dage, ikke en befolknings- eller produktionsprognose.",
  "assumption": "Samme tal gælder for alle. Energimarginen ligger i dit valgte tal. Det er planlagt energimængde, ikke målte individuelle behov eller bevis for, at alle modtager en ernæringsmæssigt tilstrækkelig kost.",
  "people": "Befolkning", "children": "Børn 0–17", "adults": "Voksne 18–70", "older": "Ældre 71+", "female": "Kvinder", "male": "Mænd", "unknown": "Ukendt alder",
  "people_help": "Registreret befolkning 1. januar 2025. Et statistisk udgangspunkt, ikke en fuldstændig optælling af alle tilstedeværende med behov for mad.",
  "age_help": "En aldersgruppes delsum af officiel befolkning, ikke ekstra personer. Demografien beskriver befolkningen, men ændrer ikke det ens kcal-regnestykke.",
  "sex_help": "Kildens registrerede kvinde-/mandekategorier, ikke en beskrivelse af alle menneskers kønsidentitet. Delsummerne må ikke lægges til befolkningstotalen igen.",
  "population_heading": "Hvem tælles med?", "population_note": "Befolkningsudtræk: 1. januar 2025. Alder og kildekøn er kun kontekst i denne udgave.",
  "table_help": "Hvert valgt land medtages én gang. Alle bruger samme valgte kcal-tal, så forskelle i energitotaler følger forskelle i befolkningstal.",
  "select_note": "Vælg mindst ét land for at beregne en sammenligning.", "exact": "Se det præcise regnestykke", "download": "Download dette scenarie · JSON",
  "about_intro": "Dette er Human Baselines enkle befolknings-/energiudgave. Den viser energimængder uden at fremstille en valgt kost eller ernæringsmodel som afgjort.",
  "method": "Beregning og margin", "method_text": "Dagligt = personantal × valgte kcal/person/dag. Årligt = dagligt × 365. Gennemsnitsmåned = årligt ÷ 12. Et højere valgt tal giver en større energiramme; ekstra buffer, spild, reserver eller befolkningsdækning lægges ikke automatisk til. Alder, køn, graviditet og amning ændrer ikke regnestykket. Det valgte tal er scenarieinput, ikke et valideret tillæg for alle individer.",
  "sources": "Befolkningskilde", "source_text": "Eurostat DEMO_PJAN, befolkning 1. januar 2025 efter alder og registreret køn for EU27. Det bevarede svar blev hentet 5. oktober 2026. Appen bruger et fast lokalt udtræk, ikke live-data ved hvert besøg. Den kontrollerer landedækning, dubletter, heltal og afstemning af alder/køn. Senere revisioner ændrer ikke dette udtræk ubemærket.",
  "limits": "Hvad værktøjet ikke fastslår", "limits_text": "Nok kcal samlet beviser ikke i sig selv ernæringsmæssig tilstrækkelighed, produktionskapacitet eller retfærdig levering. Fødevaresammensætning, vitaminer, mineraler, priser, areal, lager, tab og fordeling er senere lag. Registreret befolkning kan udelade personer med behov for mad. Egen beregning bruger dit antal uden opfundet demografi. Den tidligere detaljerede referencemodel bevares som lokal forskning og følger ikke med denne offentlige udgave.",
  "reuse": "Kildeangivelse og genbrug", "reuse_text": "Kilde: Eurostat. Egen udvælgelse, formatering og beregninger ved Hedegreen Research. Statistisk genbrug følger Eurostats offentliggjorte politik og undtagelser; dette er ikke et officielt Eurostat-produkt eller en godkendelse. Kcal-tallet er brugerinput, ikke en værdi tillagt en ernæringsinstitution.",
  "population_download": "Befolkning efter alder og køn · CSV", "metadata_download": "Metadata for befolkningsudtræk · JSON", "repo": "Kildekode", "article": "Tilhørende artikel",
 },
 "es": {
  "title": "Human Baseline", "subtitle": "Población y energía: empezar por la escala de la pregunta.",
  "intro": "Human Baseline investiga cómo hacer de una alimentación suficiente una base fiable para todos, en lugar de una lucha constante por sobrevivir. Esta primera herramienta calcula población × las kcal por persona y día que usted elige. Alimentos, nutrientes, precios, producción y distribución vendrán después.",
  "view": "Vista", "explore": "Explorar un país", "compare": "Comparar países", "eu": "Resumen UE27", "custom": "Cálculo personalizado", "about": "Acerca de y fuentes",
  "country": "País", "countries": "Países para comparar", "number": "Número de personas", "name": "Nombre de la población", "custom_name": "Población personalizada",
  "kcal": "Kcal elegidas/persona/día", "kcal_help": "Una hipótesis elegida por usted, igual para todos. 3.000 es un ejemplo editable, no una recomendación dietética. Incluya el margen energético deseado en esta cifra; no añadimos otro margen.",
  "number_help": "Su propio número de personas, no estadística oficial ni demografía de un país. Cero personas produce cero energía total.",
  "day": "Total kcal/día", "month": "Mes medio · kcal", "year": "Anual · kcal",
  "day_help": "Población × kcal elegidas/persona/día. Se cuentan todos, incluidos bebés. Sin suplementos separados por embarazo o lactancia.",
  "month_help": "Energía diaria × 365 ÷ 12. Mes promedio, no un mes natural concreto.", "year_help": "Energía diaria × 365. Escenario de días repetidos, no previsión de población ni producción.",
  "assumption": "La misma cifra se aplica a todos. El margen energético está en el valor elegido. Es volumen energético previsto, no necesidades individuales medidas ni prueba de una dieta adecuada recibida por todos.",
  "people": "Población", "children": "Niños 0–17", "adults": "Adultos 18–70", "older": "Mayores 71+", "female": "Mujeres", "male": "Hombres", "unknown": "Edad desconocida",
  "people_help": "Población registrada el 1 de enero de 2025. Punto de partida estadístico, no todas las personas presentes que necesitan alimentos.",
  "age_help": "Subtotal por edad, no personas adicionales. La demografía describe la población y no modifica el cálculo uniforme.",
  "sex_help": "Categorías estadísticas femenina/masculina de la fuente, no todas las identidades de género. No sumar de nuevo al total.",
  "population_heading": "¿A quién contamos?", "population_note": "Captura de población: 1 de enero de 2025. Edad y sexo son solo contexto en esta edición.",
  "table_help": "Cada país se incluye una sola vez con las mismas kcal elegidas. Las diferencias energéticas reflejan diferencias de población.",
  "select_note": "Seleccione al menos un país.", "exact": "Examinar el cálculo exacto", "download": "Descargar escenario · JSON",
  "about_intro": "La edición simple de población y energía de Human Baseline explora volúmenes, sin presentar una dieta o modelo nutricional como definitivo.",
  "method": "Cálculo y margen", "method_text": "Diario = personas × kcal elegidas/persona/día. Anual = diario × 365. Mes medio = anual ÷ 12. Una cifra mayor amplía el volumen; no añadimos automáticamente pérdidas, reservas, márgenes ni ajustes de cobertura. Edad, sexo, embarazo y lactancia no cambian el cálculo. La cifra es una hipótesis, no una cantidad validada para cada individuo.",
  "sources": "Fuente de población", "source_text": "Eurostat DEMO_PJAN: población el 1 de enero de 2025 por edad y sexo registrado para UE27, capturada el 5 de octubre de 2026. Se usa una captura local fija, no datos actualizados en cada visita. Se verifican países, duplicados, recuentos enteros y reconciliación por edad/sexo. Revisiones posteriores no alteran silenciosamente esta captura.",
  "limits": "Qué no demuestra", "limits_text": "Suficientes kcal agregadas no prueban calidad nutricional, capacidad productiva ni entrega justa. Composición, vitaminas, minerales, precios, suelo, almacenamiento, pérdidas y distribución son capas posteriores. El registro puede omitir personas. El cálculo personalizado no inventa demografía. El anterior modelo detallado se conserva como investigación local y no se incluye en esta edición pública.",
  "reuse": "Atribución y reutilización", "reuse_text": "Fuente: Eurostat. Selección, formato y cálculos propios de Hedegreen Research. Reutilización estadística sujeta a la política de Eurostat y sus excepciones. No es un producto oficial ni un aval. Las kcal son entrada del usuario, no un valor atribuido a una institución nutricional.",
  "population_download": "Población por edad y sexo · CSV", "metadata_download": "Metadatos de población · JSON", "repo": "Código fuente", "article": "Artículo relacionado",
 },
 "de": {
  "title": "Human Baseline", "subtitle": "Bevölkerung und Energie: mit der Größenordnung beginnen.",
  "intro": "Human Baseline untersucht, wie ausreichende Nahrung für alle zu einer verlässlichen Grundlage statt einem ständigen Überlebenskampf werden könnte. Dieses erste Tool berechnet Bevölkerung × selbst gewählte kcal pro Person und Tag. Lebensmittel, Nährstoffe, Preise, Produktion und Verteilung folgen später.",
  "view": "Ansicht", "explore": "Ein Land erkunden", "compare": "Länder vergleichen", "eu": "EU27-Überblick", "custom": "Eigene Berechnung", "about": "Über das Tool und Quellen",
  "country": "Land", "countries": "Länder zum Vergleich", "number": "Personenzahl", "name": "Name der Bevölkerung", "custom_name": "Eigene Bevölkerung",
  "kcal": "Gewählte kcal/Person/Tag", "kcal_help": "Eine selbst gewählte Planannahme, gleich für alle. 3.000 ist ein bearbeitbares Beispiel, keine Ernährungsempfehlung. Gewünschte Energiereserve in diese Zahl einbeziehen; kein weiterer Puffer wird addiert.",
  "number_help": "Eigene Personenzahl, keine amtliche Statistik oder übernommene Landesdemografie. Null Personen ergibt null Gesamtenergie.",
  "day": "Gesamt kcal/Tag", "month": "Durchschnittsmonat · kcal", "year": "Jährlich · kcal",
  "day_help": "Bevölkerung × gewählte kcal/Person/Tag. Alle zählen mit, auch Säuglinge. Keine gesonderten Schwangerschafts- oder Stillzuschläge.",
  "month_help": "Tagesenergie × 365 ÷ 12. Durchschnittsmonat, kein bestimmter Kalendermonat.", "year_help": "Tagesenergie × 365. Wiederholtes Tagesszenario, keine Bevölkerungs- oder Produktionsprognose.",
  "assumption": "Für alle gilt dieselbe Zahl. Die Energiereserve liegt im gewählten Wert. Geplantes Energievolumen, keine gemessenen Individualbedürfnisse oder nachgewiesene bedarfsgerechte Versorgung aller.",
  "people": "Bevölkerung", "children": "Kinder 0–17", "adults": "Erwachsene 18–70", "older": "Ältere 71+", "female": "Frauen", "male": "Männer", "unknown": "Alter unbekannt",
  "people_help": "Registrierte Bevölkerung am 1. Januar 2025. Statistischer Ausgangspunkt, nicht alle Anwesenden mit Nahrungsbedarf.",
  "age_help": "Altersteilsumme, keine zusätzlichen Personen. Demografie beschreibt die Bevölkerung, verändert aber nicht die einheitliche Berechnung.",
  "sex_help": "Erfasste weibliche/männliche Quellenkategorien, keine vollständige Beschreibung der Geschlechtsidentität. Nicht erneut zur Gesamtsumme addieren.",
  "population_heading": "Wer wird gezählt?", "population_note": "Bevölkerungsstand: 1. Januar 2025. Alter und Quellengeschlecht sind in dieser Ausgabe nur Kontext.",
  "table_help": "Jedes Land zählt einmal mit derselben gewählten kcal-Zahl. Energieunterschiede folgen Bevölkerungsunterschieden.",
  "select_note": "Mindestens ein Land auswählen.", "exact": "Genaue Berechnung prüfen", "download": "Szenario herunterladen · JSON",
  "about_intro": "Die einfache Bevölkerungs- und Energieausgabe von Human Baseline zeigt Größenordnungen, ohne eine Ernährungsweise oder ein Modell als abschließend festzulegen.",
  "method": "Berechnung und Reserve", "method_text": "Täglich = Personen × gewählte kcal/Person/Tag. Jährlich = täglich × 365. Durchschnittsmonat = jährlich ÷ 12. Ein höherer Wert erweitert das Volumen; Verluste, Reserven, Puffer oder zusätzliche Bevölkerungsabdeckung werden nicht automatisch ergänzt. Alter, Geschlecht, Schwangerschaft und Stillen verändern die Berechnung nicht. Die Zahl ist eine Szenarioannahme, kein validierter Wert für jedes Individuum.",
  "sources": "Bevölkerungsquelle", "source_text": "Eurostat DEMO_PJAN: Bevölkerung am 1. Januar 2025 nach Alter und erfasstem Geschlecht für EU27. Gespeicherter Abruf vom 5. Oktober 2026. Fester lokaler Datenstand statt Live-Abfragen bei jedem Besuch. Länderabdeckung, Duplikate, ganzzahlige Werte und Alters-/Geschlechtssummen werden geprüft. Spätere Revisionen verändern den Stand nicht unbemerkt.",
  "limits": "Was das Tool nicht nachweist", "limits_text": "Genügend Gesamt-kcal beweisen weder Nährstoffdeckung noch Produktionskapazität oder gerechte Versorgung. Lebensmittelzusammensetzung, Vitamine, Mineralstoffe, Preise, Flächen, Lagerung, Verluste und Verteilung folgen später. Register können Menschen auslassen. Eigene Berechnungen erfinden keine Demografie. Das frühere Detailmodell bleibt lokale Forschung und wird hier nicht mitveröffentlicht.",
  "reuse": "Quellenangabe und Weiterverwendung", "reuse_text": "Quelle: Eurostat. Eigene Auswahl, Darstellung und Berechnungen durch Hedegreen Research. Statistische Wiederverwendung folgt Eurostats Richtlinie und Ausnahmen. Kein amtliches Produkt oder institutionelles Gütesiegel. Die kcal-Zahl ist eine Nutzereingabe, kein einer Ernährungsinstitution zugeschriebener Wert.",
  "population_download": "Bevölkerung nach Alter und Geschlecht · CSV", "metadata_download": "Metadaten zum Bevölkerungsabruf · JSON", "repo": "Quellcode", "article": "Begleitartikel",
 },
}

COUNTRY_NAMES = {
 "da": "Østrig|Belgien|Bulgarien|Kroatien|Cypern|Tjekkiet|Danmark|Estland|Finland|Frankrig|Tyskland|Grækenland|Ungarn|Irland|Italien|Letland|Litauen|Luxembourg|Malta|Nederlandene|Polen|Portugal|Rumænien|Slovakiet|Slovenien|Spanien|Sverige".split("|"),
 "es": "Austria|Bélgica|Bulgaria|Croacia|Chipre|Chequia|Dinamarca|Estonia|Finlandia|Francia|Alemania|Grecia|Hungría|Irlanda|Italia|Letonia|Lituania|Luxemburgo|Malta|Países Bajos|Polonia|Portugal|Rumanía|Eslovaquia|Eslovenia|España|Suecia".split("|"),
 "de": "Österreich|Belgien|Bulgarien|Kroatien|Zypern|Tschechien|Dänemark|Estland|Finnland|Frankreich|Deutschland|Griechenland|Ungarn|Irland|Italien|Lettland|Litauen|Luxemburg|Malta|Niederlande|Polen|Portugal|Rumänien|Slowakei|Slowenien|Spanien|Schweden".split("|"),
}


def number(value, locale, decimals=0):
    result = f"{value:,.{decimals}f}".replace(",", " ")
    return result if locale == "en" else result.replace(".", ",")


def compact(value, locale):
    scales = {"en": ("billion", "trillion"), "da": ("mia.", "billioner"),
              "es": ("mil millones", "billones"), "de": ("Milliarden", "Billionen")}
    if value >= 1e12:
        return "≈ " + number(value / 1e12, locale, 2) + " " + scales[locale][1]
    if value >= 1e9:
        return "≈ " + number(value / 1e9, locale, 2) + " " + scales[locale][0]
    return number(value, locale, 0)
