# Lingua dell'interfaccia del sito

Type: grilling
Status: resolved

## Question

Il sito ha `languageCode = "en-us"` e una sola lingua `en`. Con i post in italiano, l'interfaccia
(date, "min read", "Related content", indice) resta in inglese. Lasciare così, passare il sito a
`it`, oppure aggiungere `it` come seconda lingua? Ognuna ha effetti diversi su URL, feed RSS e
sui post esistenti in inglese.

## Answer

Resolved 2026-10-08 (default prudente). Si lascia `languageCode = "en-us"`: cambiarlo o aggiungere
`it` toccherebbe URL, RSS e i ~40 post inglesi esistenti, fuori dallo scopo della serie.
Conseguenza accettata: l'interfaccia (date, "min read", "Related") resta in inglese sui post
italiani. Rivedibile in futuro come iniziativa a sé.
