---
title: "Audio, DAC e line-out"
description: "L'iPod ha un segreto che gli audiofili conoscono: l'uscita del dock (line-out) salta l'amplificatore interno e dà un segnale pulito a volume fisso, pronto per un ampli esterno. Qui entra il chip Wolfson, la differenza tra cuffia e line-out, e perché un iPod Video più un piccolo DAC/ampli batte molti lettori moderni."
slug: "audio-e-dac-ipod"
date: 2025-09-23T09:00:00+02:00
lastmod: 2025-09-23T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - Audio
keywords:
    - ipod line out
    - wolfson dac ipod
    - ipod audiofilo
    - ipod dac ampli
    - ipod qualità audio
image: "cover.png"
toc: true
links:
  - title: "Rockbox — Sound Settings"
    description: "Documentazione di equalizzatore, crossfeed e replaygain."
    website: https://www.rockbox.org/manual.shtml
---

## L'iPod come sorgente seria

C'è una ragione per cui gli iPod Video e i Classic sono rimasti oggetti di culto tra gli audiofili e
non si sono svalutati: come **sorgente digitale**, sono ottimi. Il file sta lì, il chip lo converte in
analogico, e c'è un modo per prendere quel segnale *prima* che l'iPod lo rovini amplificandolo per una
cuffia. Quel modo è il **line-out**, ed è la chiave di questo capitolo.

## Line-out contro uscita cuffia

L'iPod ha due uscite, e la differenza è enorme per la qualità:

```text {hl_lines=[2,3]}
Jack cuffia (in alto)  → segnale già amplificato dall'ampli interno (modesto), volume regolabile
Line-out (dal dock)    → segnale "puro" a volume fisso, PRIMA dell'ampli interno
```

Il line-out esce dai pin del **connettore dock a 30 pin** in basso. Un cavo o un dock "LOD" (Line-Out
Dock) prende quel segnale e lo porta a un jack. Collegato a un **ampli per cuffie** o a un impianto, usi
l'iPod solo come fonte pulita e lasci l'amplificazione a un circuito migliore del minuscolo ampli
interno. È così che un iPod diventa una sorgente "da impianto".

## Il chip Wolfson e cosa aspettarsi

Come visto nel [capitolo sulla scelta del modello]({{< relref "post/scegliere-ipod-da-moddare" >}}), i
Video 5/5.5 gen e i Classic 6ª gen usano un DAC **Wolfson**, apprezzato per un suono "caldo". Ma fissiamo
le aspettative:

```text {hl_lines=[2]}
- La differenza tra chip Wolfson e Cirrus è reale ma sottile.
- Contano molto di più: la qualità dei file, le cuffie, e l'ampli a valle.
- Il line-out annulla gran parte delle differenze d'ampli: conta soprattutto il DAC + ciò che collegli.
```

In pratica: non comprare un iPod *solo* per il chip. Ma se parti da un Video 5.5 Wolfson, hai una
sorgente eccellente da cui partire.

## Il software che migliora il suono: Rockbox

Con [Rockbox]({{< relref "post/rockbox-firmware-alternativo" >}}) installato, hai strumenti audio che il
firmware Apple non dà:

```text {hl_lines=[1,2,3]}
ReplayGain  → normalizza il volume tra brani diversi senza comprimere la dinamica
EQ parametrico → correggi la risposta delle TUE cuffie, banda per banda
Crossfeed   → riduce la "separazione innaturale" dei canali in cuffia
Gapless     → nessun silenzio tra tracce legate (album dal vivo, concept)
```

ReplayGain in particolare risolve il fastidio classico della libreria mista: brani masterizzati a volumi
diversi che ti costringono a correggere di continuo.

## La catena consigliata

Mettendo insieme i pezzi, la catena "audiofila da iPod" è:

```text
File lossless (FLAC/ALAC)  →  iPod con Rockbox  →  line-out dal dock  →  ampli/DAC portatile  →  buone cuffie
```

Ogni anello conta, ma il salto più grande rispetto all'"iPod + cuffiette dal jack" è aggiungere il
**line-out verso un ampli esterno**: supera il limite dell'ampli interno, che è il vero collo di
bottiglia del suono in cuffia.

## Conclusione

Il segreto audio dell'iPod è il line-out dal dock: un segnale pulito, a monte dell'ampli interno, pronto
per un amplificatore serio — e con Rockbox ci aggiungi EQ, ReplayGain e gapless. Sistemato cosa l'iPod fa
*suonare*, le prossime mod guardano a come lo si *usa e si tiene in mano*: la [ghiera e i
pulsanti]({{< relref "post/click-wheel-e-pulsanti" >}}), prossimo capitolo.
