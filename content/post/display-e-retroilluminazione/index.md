---
title: "Display e retroilluminazione"
description: "Lo schermo è la mod più delicata: un cavo flat fragilissimo, un pannello che si crepa se premi nel punto sbagliato, e la retroilluminazione che con gli anni ingiallisce. Quando vale la pena cambiarlo, come riconoscere un display rotto da uno solo spento, e la procedura con le accortezze che evitano di trasformare una riparazione in due."
slug: "display-e-retroilluminazione"
date: 2025-10-14T09:00:00+02:00
lastmod: 2025-10-14T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - DIY
keywords:
    - display ipod classic
    - schermo ipod rotto
    - retroilluminazione ipod
    - sostituire display ipod
image: "cover.png"
toc: true
---

## La mod più delicata

Lascio lo schermo verso la fine perché è la riparazione dove è più facile fare danni. Il display
dell'iPod è collegato da un **cavo flat sottilissimo**, il pannello si **crepa** se lo pieghi o premi nel
punto sbagliato, e — a differenza di batteria o flash — un errore qui può rompere il pezzo nuovo mentre
lo monti. Non è difficile *concettualmente*; richiede mani ferme e il rispetto di poche regole precise.

## Prima: è davvero il display il problema?

Metà delle "sostituzioni schermo" non servono. Distingui il guasto:

```text {hl_lines=[2,3]}
Schermo nero ma l'iPod "suona"   → spesso è la retroilluminazione o il cavo, NON il pannello
Crepe / macchie di inchiostro    → pannello rotto, va sostituito
Righe / aree morte               → pannello danneggiato, va sostituito
Immagine ok ma buio              → retroilluminazione (backlight) debole o cavo allentato
```

Se l'iPod risponde ai comandi e riproduce musica ma lo schermo è buio, prova prima a **ricollegare il
cavo del display**: a volte si è solo allentato. Cambiare il pannello quando il problema era il cavo è
lavoro (e rischio) sprecato.

## La retroilluminazione che ingiallisce

Un difetto tipico dell'età: la luce di fondo diventa fioca o vira al giallo. Nei Classic la
retroilluminazione fa parte del modulo display, quindi si risolve col ricambio del pannello completo. Su
Rockbox puoi almeno **alzare la luminosità e il timeout** del backlight per compensare un pannello un
po' stanco, guadagnando tempo prima di mettere mano al ferro.

## La procedura, con le accortezze che contano

Con l'iPod aperto e la batteria scollegata:

```text {hl_lines=[2,5]}
1. Il display è sotto la logic board: devi sollevare la board per accedervi.
   NON tirarla: è ancora legata da cavi: muovila con delicatezza.
2. Scollega il cavo flat del display (linguetta, mai strappare).
3. Il pannello è nel suo telaio: estrailo senza premere sulla superficie vetrata.
4. Monta il nuovo nello stesso verso, ricollega il flat finché è ben inserito.
5. Prima di richiudere, riconnetti la batteria e ACCENDI: verifica immagine e luce.
```

Il punto 5 è d'oro: scoprire ora che il flat non fa contatto costa dieci secondi; scoprirlo a iPod
chiuso significa riaprire tutto.

## Il cavo flat: il nemico numero uno

Il cavo del display è il componente più fragile dell'intero iPod. Due regole salvano il lavoro:

```text {hl_lines=[1,2]}
- Non piegarlo ad angolo vivo: le piste interne si spezzano e il pannello resta nero.
- Inseriscilo dritto e a fondo nel connettore, poi chiudi la linguetta: mai di sbieco.
```

Se dopo il montaggio lo schermo resta nero o a righe, nove volte su dieci è il flat mal inserito o
pizzicato, non il pannello difettoso. Riapri con calma e ricontrolla il connettore prima di dare la
colpa al ricambio.

## Conclusione

Lo schermo è la mod da affrontare con più calma: distingui prima un pannello rotto da un semplice cavo
allentato, solleva la logic board senza strappare, e verifica l'immagine prima di richiudere. Fatta
questa, l'iPod è completo dentro e fuori — resta un'ultima frontiera, tagliare l'ultimo cavo rimasto e
mandare la musica senza fili: [Bluetooth e audio wireless]({{< relref "post/bluetooth-e-wireless-ipod" >}}),
capitolo finale.
