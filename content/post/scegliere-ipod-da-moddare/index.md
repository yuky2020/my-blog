---
title: "Quale iPod moddare"
description: "Non tutti gli iPod sono uguali davanti a un cacciavite. Il Classic si apre e si aggiorna all'infinito, il Video è il preferito degli audiofili, il Mini è minuscolo ma modificabilissimo, il Nano quasi per niente. Guida ai modelli, al chip audio che conta, e a come leggere il numero di generazione prima di comprare."
slug: "scegliere-ipod-da-moddare"
date: 2025-08-12T09:00:00+02:00
lastmod: 2025-08-12T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - Hardware
keywords:
    - ipod classic
    - ipod video 5.5
    - ipod mini
    - quale ipod comprare
    - wolfson dac
image: "cover.png"
toc: true
links:
  - title: "everymac — Specifiche di ogni iPod"
    description: "Database con tutte le generazioni, capacità e numeri di modello."
    website: https://everymac.com/systems/apple/ipod/
  - title: "iFixit — Guide iPod"
    description: "Teardown e guide di riparazione per ciascun modello."
    website: https://www.ifixit.com/Device/iPod
---

## La scelta che condiziona tutto

Prima di comprare qualsiasi attrezzo, scegli il modello. Un iPod sbagliato rende metà delle mod di
questa serie impossibili o inutili: alcuni non si aprono senza romperli, altri hanno la memoria
saldata, altri ancora hanno un chip audio che nessun upgrade migliora. La domanda giusta non è "quale
iPod è più bello", ma **"quale accetta le mod che voglio fare"**.

## I quattro candidati

```text {hl_lines=[2,3]}
Classic (6ª/6.5ª/7ª gen, 2007-2009) → il campione del modding: si apre, accetta flash enorme, batterie grosse
Video (5ª/5.5ª gen, 2005-2006)       → il preferito degli audiofili (chip Wolfson), schermo a colori, ottimo con Rockbox
Mini (1ª/2ª gen, 2004-2005)          → piccolo, in alluminio, CF/SD facilissima; batteria piccola
Nano / Touch                         → memoria saldata, poco o nulla da moddare (salta questi)
```

Se vuoi **massima capacità e autonomia**, prendi un **Classic**. Se vuoi **la migliore qualità audio
di fabbrica**, prendi un **Video 5.5ª gen**. Se vuoi un oggetto tascabile e un progetto rapido, il
**Mini**. Il Nano e il Touch, per questa serie, lasciali stare.

## Il dettaglio che gli audiofili cercano: il chip audio

Non tutti gli iPod suonano uguale, e la differenza è nel DAC (il convertitore digitale-analogico):

- **iPod Video 5ª/5.5ª gen e Classic 6ª gen** → chip **Wolfson** (WM87xx), considerato caldo e musicale.
- **Classic 6.5ª e 7ª gen** → chip **Cirrus Logic**, più neutro.

Non è una differenza enorme, e Rockbox più un buon ampli contano di più del chip. Ma se parti da zero e
l'audio è la tua priorità, un **Video 5.5ª gen** è la scelta classica. Ne riparliamo nel
[capitolo sull'audio]({{< relref "post/audio-e-dac-ipod" >}}).

## Leggere il modello prima di comprare

Gli annunci dell'usato sono pieni di descrizioni sbagliate. Verifica tu:

```text
1. Gira l'iPod: sul retro c'è "Model Axxxx" inciso piccolo.
   A1136 = Video 5/5.5 gen · A1238 = Classic 6/6.5/7 gen · A1051/A1137 = Mini
2. Capacità: 30/60/80/120/160 GB indica la generazione (i tagli grossi = più recenti).
3. Spesso (thick) = disco da 80GB a doppio piatto: più spazio dentro per una batteria grossa.
```

Lo spessore conta per il modding: un Classic "thick" da 160 GB (6ª gen) ha **più volume interno**, quindi
ci stanno batterie più capienti dopo aver tolto il disco. È spesso il modello più ambito.

## Cosa accettare "rotto" nell'usato

Compra pure un iPod descritto come guasto, se il difetto è uno di questi — sono proprio ciò che andrai
a sistemare:

```text {hl_lines=[2,3]}
"batteria dura poco"        → la cambi tu (capitolo 3)
"fa rumore / si blocca"     → disco meccanico morente: lo butti e metti flash (capitolo 4)
"icona cartella/triste"     → quasi sempre disco morto: idem
"ghiera non risponde bene"  → click wheel da 5 euro (capitolo 8)
```

Evita invece chi ha **schermo rotto a macchie** (costa di più da trovare), **scocca gonfia** (batteria
già esplosa dentro, possibile danno), o **ossido da liquidi** sulla logic board.

## Conclusione

Classic per capacità e autonomia, Video 5.5 per l'audio, Mini per il progetto tascabile. Un iPod
"guasto" per batteria o disco è l'affare migliore: quei guasti sono il punto di partenza di questa
serie. Scelto il paziente, il primo gesto è imparare ad **aprirlo senza rovinare i bordi** —
[il teardown]({{< relref "post/aprire-ipod-teardown" >}}), prossimo capitolo.
