---
title: "Click wheel e pulsanti"
description: "La ghiera è l'anima dell'iPod — e dopo vent'anni spesso 'scrolla' male o fa doppio click. È un ricambio da pochi euro, sostituibile senza saldare, e cambiarla fa tornare l'iPod reattivo come nuovo. Come funziona il click wheel capacitivo, perché smette di rispondere bene, e lo scambio passo per passo."
slug: "click-wheel-e-pulsanti"
date: 2025-09-30T09:00:00+02:00
lastmod: 2025-09-30T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - DIY
keywords:
    - click wheel ipod
    - ghiera ipod
    - ipod ghiera non funziona
    - sostituire click wheel
image: "cover.png"
toc: true
---

## L'anima dell'iPod

Il **click wheel** è ciò che ha reso l'iPod l'iPod: scorri col pollice e la lista vola, un gesto che
nessun touchscreen ha mai eguagliato per la musica. Ma è anche una delle parti che invecchia peggio.
Dopo vent'anni di pollici, la ghiera comincia a "saltare", a non registrare lo scorrimento, o a fare
doppi click sui tasti. La buona notizia: è un ricambio economico e lo cambi senza saldatore.

## Come funziona (e perché si rovina)

Il click wheel non ha parti che girano: è una superficie **capacitiva**. Sotto la plastica c'è un
reticolo di elettrodi che sente dove tocca il dito, come un trackpad circolare. I quattro tasti
(menu, play, avanti, indietro) e il bottone centrale sono invece **contatti meccanici**.

```text {hl_lines=[2,3]}
Scrolling      → sensore capacitivo (sente la posizione del dito)
Tasti e centro → interruttori meccanici a membrana (click fisico)
```

Due cose lo rovinano: lo **sporco e il grasso** che si infilano sotto la plastica e disturbano il
sensore capacitivo, e l'**usura dei contatti meccanici** dei tasti, che iniziano a fare falsi contatti o
doppi click.

## Prima di cambiarlo: pulizia e taratura

Spesso non serve nemmeno il ricambio:

```text {hl_lines=[2]}
1. Pulisci la superficie con un panno appena umido di alcol isopropilico (non bagnare i bordi).
2. Se usi Rockbox, c'è un menu di debug che mostra i valori grezzi della ghiera:
   serve a capire se il sensore risponde o se è davvero morto.
3. Un reset (MENU + centrale tenuti premuti) a volte ripristina una ghiera "impazzita".
```

Se dopo la pulizia lo scrolling è ancora irregolare o i tasti fanno doppio click, è ora del ricambio.

## Lo scambio

Il click wheel è un pezzo del **frontale**: arriva come assieme (ghiera + cavo flat) già pronto, da
pochi euro. Con l'iPod aperto (vedi il [teardown]({{< relref "post/aprire-ipod-teardown" >}})):

```text
1. Scollega il cavo flat del click wheel dalla logic board (linguetta nera, sfila piano).
2. Il click wheel è incollato al frontale con biadesivo: scaldalo leggermente (phon tiepido)
   e stacca la ghiera facendo leva PIATTA dal bordo.
3. Rimuovi i residui di adesivo dal frontale.
4. Applica il nuovo (porta già il suo biadesivo), premi uniforme, ricollega il flat.
```

Nessuna saldatura: tutto a connettore e adesivo. L'unico punto delicato è staccare la vecchia ghiera
senza piegare il frontale — scaldare l'adesivo è la chiave.

## Il bottone centrale

Il **tasto centrale** è spesso quello che cede per primo (è il più usato). Alcuni ricambi lo includono
nell'assieme ghiera; altri lo hanno separato. Se solo il centrale fa i capricci e il resto va, cerca un
ricambio che comprenda la membrana centrale — eviti di buttare una ghiera ancora buona.

## Conclusione

Il click wheel è il gesto che definisce l'iPod, ed è un ricambio da pochi euro che ridà reattività da
primo giorno — spesso basta perfino una pulizia. Rimessa a nuovo l'interazione, la mod successiva è la
più vistosa di tutte: cambiare la **scocca**, per un iPod che sembra uscito di fabbrica in un colore che
Apple non ha mai venduto. È la [nuova scocca]({{< relref "post/scocca-e-colori-custom" >}}), prossimo capitolo.
