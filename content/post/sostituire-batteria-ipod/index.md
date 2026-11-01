---
title: "Sostituire la batteria"
description: "Una batteria iPod di vent'anni è al 30% della sua capacità o si è gonfiata. Cambiarla è la mod col miglior rapporto fatica-risultato: niente saldatore, solo un connettore da sfilare. E togliendo il disco meccanico per mettere flash, nel guscio ci sta una batteria enorme: giorni di autonomia invece di ore."
slug: "sostituire-batteria-ipod"
date: 2025-08-26T09:00:00+02:00
lastmod: 2025-08-26T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - DIY
keywords:
    - batteria ipod
    - sostituire batteria ipod classic
    - ipod batteria gonfia
    - ipod autonomia
image: "cover.png"
toc: true
links:
  - title: "iFixit — Sostituzione batteria iPod Classic"
    description: "Guida con foto e codici dei ricambi compatibili."
    website: https://www.ifixit.com/Guide/iPod+Classic+Battery+Replacement/599
---

## Il primo pezzo da cambiare

La batteria è l'unico componente dell'iPod che muore *sempre*. Le celle agli ioni di litio perdono
capacità con gli anni anche da ferme, e dopo quindici-vent'anni una batteria originale regge una
frazione del tempo di un tempo — o peggio, si **gonfia**, spingendo sul retro della scocca fino a
deformarla. È il primo pezzo da cambiare, ed è anche il più semplice: nessuna saldatura, solo un
connettore.

> La batteria gonfia è un rischio concreto: il litio gonfio può incendiarsi se forato. Se la tua è
> gonfia, maneggiala con delicatezza, non pungerla né piegarla, e smaltiscila nel contenitore pile,
> mai nei rifiuti comuni.

## Scegliere la batteria giusta

Le batterie di ricambio per iPod sono tutte di terze parti (le originali Apple non si trovano più
nuove). Due cose contano: **capacità** e **spessore**.

```text {hl_lines=[2,4]}
iPod "thin" (col disco da 1 piatto)  → c'è spazio per ~650-850 mAh
iPod "thick" (disco da 2 piatti)     → guscio più profondo: ci sta una batteria più grossa
Se metti flash e TOGLI il disco      → si libera moltissimo spazio: batterie 2000-3000 mAh
```

La sinergia più importante di questa serie: **flash + batteria grossa**. Tolto il disco meccanico
(capitolo 4), nel guscio di un Classic "thick" entra una batteria da **~2500-3000 mAh**, contro i
~600 di fabbrica. Significa passare da ore a **giorni** di riproduzione.

## Lo scambio, passo per passo

Con l'iPod già aperto (vedi il [teardown]({{< relref "post/aprire-ipod-teardown" >}})):

```text
1. Individua il connettore della batteria sulla logic board (piccolo, bianco o nero).
2. Sollevalo dritto con l'unghia o uno spudger di plastica: viene su senza forza.
3. La batteria è fissata con biadesivo leggero: scollala facendo leva PIATTA, non di punta.
4. Posiziona la nuova, ricollega il connettore premendo finché non scatta.
5. Non incollare la nuova finché non hai verificato che l'iPod accende e carica.
```

Nessuno stadio richiede il saldatore: le batterie di ricambio arrivano già col cavetto e il connettore
pronti.

## Il primo avvio: non fidarti subito

Una batteria nuova va **ciclata** prima di dare numeri affidabili sull'autonomia:

```text {hl_lines=[2]}
1. Carica completa (fino a batteria piena, un paio d'ore).
2. Usa fino allo spegnimento, poi ricarica piena: così l'indicatore si calibra.
3. Solo dal secondo-terzo ciclo l'autonomia misurata è quella vera.
```

Se con Rockbox installato (capitolo 6), puoi leggere la tensione reale della batteria dal menu di
debug — utile per capire se una cella è buona o difettosa.

## Gestire il connettore senza romperlo

Il connettore della batteria è il punto fragile. Due regole:

- **Sollevalo dritto**, mai di sbieco: i pin si piegano.
- Se è duro, fai leva **sotto il connettore**, non tirando il cavetto (il cavo si stacca dalla saldatura
  interna della batteria e la rovini).

## Conclusione

Cambiare la batteria è la mod che ridà vita vera a un iPod stanco, e non richiede né saldatore né
coraggio — solo un connettore da sfilare con criterio. Ma il suo pieno potenziale si libera insieme alla
mod successiva: togliere il disco meccanico apre lo spazio per la batteria grossa *e* elimina l'unico
pezzo rumoroso e fragile rimasto. È il passaggio a [memoria flash]({{< relref "post/da-hdd-a-storage-flash" >}}),
prossimo capitolo.
