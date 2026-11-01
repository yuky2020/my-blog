---
title: "Rockbox: il firmware libero"
description: "Rockbox è un sistema operativo open source che gira sull'iPod al posto (o accanto) a quello Apple: suona FLAC e Opus, ha un equalizzatore vero, gapless, temi, perfino giochi, e non ti obbliga a iTunes — copi la musica trascinandola. Come installarlo senza rischi, convivere col firmware Apple, e cosa cambia davvero."
slug: "rockbox-firmware-alternativo"
date: 2025-09-16T09:00:00+02:00
lastmod: 2025-09-16T09:00:00+02:00
categories:
    - Making
tags:
    - iPod
    - Modding
    - Software
    - Audio
keywords:
    - rockbox
    - rockbox ipod
    - firmware alternativo ipod
    - ipod flac
    - rockbox installazione
image: "cover.png"
toc: true
links:
  - title: "Rockbox — Sito ufficiale"
    description: "Download, manuale e lista dei dispositivi supportati."
    website: https://www.rockbox.org/
  - title: "Rockbox Utility"
    description: "Installer grafico che automatizza bootloader, firmware e font."
    website: https://www.rockbox.org/wiki/RockboxUtility
---

## Cos'è e perché cambia l'iPod

Rockbox è un **firmware libero** che sostituisce il software di bordo dell'iPod. Non è un tweak: è un
intero sistema operativo open source, sviluppato da vent'anni per i lettori musicali, che trasforma
cosa l'iPod *sa fare*. Il firmware Apple è elegante ma chiuso e limitato ai formati e alle funzioni che
Apple decise nel 2007. Rockbox apre tutto.

## Cosa sblocca, concretamente

```text {hl_lines=[1,3]}
Formati: FLAC, Opus, OGG, WavPack, ALAC… (niente più conversione a AAC)
Audio: equalizzatore parametrico vero, crossfeed, replaygain, gapless perfetto
Libertà: copi la musica trascinando file (USB mass storage), senza iTunes
Extra: temi grafici, testi, registratore, perfino Doom e giochi
```

Le due cose che fanno la differenza per chi ascolta sul serio: **gapless** (gli album dal vivo e i
concept non hanno più il buco tra una traccia e l'altra) e l'**equalizzatore** completo, che il firmware
Apple non ha mai avuto a questo livello.

## Convive con Apple: non devi scegliere

Il punto rassicurante: Rockbox **non cancella** il firmware Apple. Si installa accanto, e un
**bootloader** ti fa scegliere all'accensione (o fa partire Apple se tieni premuto un tasto). Hai il
meglio di entrambi: Rockbox per ascoltare, firmware Apple quando ti serve iTunes o il dock di un'auto
che si aspetta un iPod "vero".

```text
Accensione normale            → parte Rockbox
Tieni premuto MENU all'avvio  → parte il firmware originale Apple
```

## Installazione con Rockbox Utility

Il modo semplice e sicuro è l'installer ufficiale **Rockbox Utility**, che fa tutto il lavoro:

```text {hl_lines=[2,3]}
1. Fai prima un ripristino pulito dell'iPod da iTunes (parti da firmware Apple sano).
2. Avvia Rockbox Utility → rileva l'iPod → "Installazione completa".
   Installa bootloader + firmware Rockbox + font + tema predefinito.
3. Scollega in sicurezza e riavvia: parte Rockbox.
```

L'**installazione completa** è l'opzione giusta per il primo giro: evita di dimenticare i font (senza i
quali Rockbox parte con testo minuscolo) o il bootloader.

## Copiare la musica senza iTunes

Con Rockbox, l'iPod monta come un **disco USB normale**. Copi la musica come su una chiavetta:

```text
1. Collega l'iPod: appare come unità di massa.
2. Trascina cartelle di musica dove vuoi (es. in /Music).
3. In Rockbox: "Aggiorna database" per indicizzare, oppure sfoglia direttamente le cartelle.
```

Niente libreria iTunes, niente sincronizzazione: i file sono tuoi e li organizzi come preferisci. Per
chi è passato dallo streaming al possesso dei file, è metà del fascino.

## Attenzione e ripensamenti

```text {hl_lines=[2]}
- Rockbox è reversibile: Rockbox Utility ha anche "Disinstalla" e torni ad Apple pulito.
- L'interfaccia è funzionale, non lussuosa: chi vuole "l'iPod originale" potrebbe preferire Apple.
- Su schede enormi (capitolo 5) la prima scansione del database è lunga: è normale.
```

Non c'è rischio di "brickare" l'iPod con la procedura ufficiale: il bootloader è pensato proprio per
poter sempre tornare indietro.

## Conclusione

Rockbox trasforma l'iPod da lettore chiuso a lettore aperto: formati liberi, equalizzatore vero,
gapless, musica copiata senza iTunes — e tutto reversibile, accanto al firmware Apple. Ora che il
software non limita più l'audio, resta la catena fisica del suono: il chip, l'uscita e come tirarne
fuori il meglio. È il [capitolo sull'audio]({{< relref "post/audio-e-dac-ipod" >}}).
