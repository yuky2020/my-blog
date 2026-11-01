---
title: "Bluetooth e audio wireless"
description: "L'iPod è nato prima del Bluetooth audio, ma nel 2025 lo si fa suonare in cuffie wireless in due modi: un trasmettitore nel jack o nel dock, oppure una mod interna che prende il line-out e aggiunge un modulo Bluetooth dentro la scocca. Pro, contro, latenza e qualità — e perché per molti il cavo resta la scelta giusta."
slug: "bluetooth-e-wireless-ipod"
date: 2025-10-21T09:00:00+02:00
lastmod: 2025-10-21T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - Audio
keywords:
    - ipod bluetooth
    - ipod wireless mod
    - ipod bluetooth trasmettitore
    - ipod cuffie wireless
image: "cover.png"
toc: true
---

## Tagliare l'ultimo cavo

L'iPod Classic è di un'epoca in cui le cuffie avevano il filo. Ma le cuffie e gli altoparlanti di oggi
sono quasi tutti **Bluetooth**, e far parlare un lettore del 2007 con loro è l'ultima frontiera del
modding. Si può fare, in due modi molto diversi per invasività e risultato. Vale la pena capire i
compromessi prima di scegliere — perché, come vedremo, il wireless ha un costo in qualità e latenza che
non tutti vogliono pagare.

## Via 1: trasmettitore esterno (zero smontaggio)

Il modo più semplice non tocca l'iPod: un piccolo **trasmettitore Bluetooth** che si collega all'uscita.

```text {hl_lines=[2,3]}
Nel jack cuffia   → trasmettitore BT a batteria infilato nel jack (segnale già amplificato)
Nel dock (30 pin) → trasmettitore che prende il LINE-OUT: qualità migliore, nessun rumore d'ampli
```

Il trasmettitore dal **dock/line-out** è la scelta migliore: prende il segnale pulito (vedi il
[capitolo audio]({{< relref "post/audio-e-dac-ipod" >}})) e lo trasmette, senza passare per l'ampli
interno modesto. È reversibile, non richiede aprire nulla, e lo stacchi quando vuoi tornare al cavo. Lo
svantaggio è un oggetto in più da caricare e da appendere all'iPod.

## Via 2: modulo Bluetooth interno (mod spinta)

La versione elegante: un **modulo Bluetooth** montato *dentro* la scocca, alimentato dalla batteria
dell'iPod e collegato al line-out interno. L'iPod resta liscio, senza nulla che sporge, e trasmette da
solo.

```text {hl_lines=[2]}
- Serve spazio interno: più facile dopo la mod flash (il disco tolto libera volume).
- Spesso richiede qualche saldatura (alimentazione + segnale): è l'unica mod "col ferro" della serie.
- Consuma dalla batteria dell'iPod: l'autonomia cala rispetto al cablato.
```

È la mod più ambiziosa del lotto e l'unica dove tocca saldare. Il risultato — un iPod Classic che
trasmette Bluetooth senza accessori esterni — è spettacolare, ma pesa su autonomia e complessità.

## Il prezzo del wireless: latenza e qualità

Qualunque via scegli, il Bluetooth introduce compromessi che il cavo non ha:

```text {hl_lines=[1,2]}
Latenza → ritardo tra immagine e suono (irrilevante per la musica, fastidioso coi video)
Codec   → SBC/AAC comprimono; la "purezza" del line-out si perde un po' nella trasmissione
Batteria→ trasmettere costa energia, su entrambe le vie
```

Per questo molti puristi, dopo aver provato, **tornano al line-out cablato verso un ampli**: è la catena
che suona meglio (vedi di nuovo il [capitolo audio]({{< relref "post/audio-e-dac-ipod" >}})). Il
Bluetooth è comodità, non qualità massima. Scegli in base a cosa ti serve davvero: libertà dal filo, o
l'ultimo grado di fedeltà.

## Conclusione

Il wireless sull'iPod si fa, con un trasmettitore esterno reversibile o con una mod interna da saldatore,
ma sempre al prezzo di un po' di qualità e di latenza — ragione per cui il cavo verso un buon ampli resta
la scelta dei puristi. Con questo si chiude la serie: dalla scelta del modello allo smontaggio, da
batteria, flash e Rockbox fino ad audio, estetica e wireless, un iPod di vent'anni fa è ora un lettore
migliore di quando era nuovo. Se vuoi ripartire dall'inizio o rivedere l'ordine, torna alla
[roadmap della serie]({{< relref "post/modifiche-ipod-la-serie" >}}).
