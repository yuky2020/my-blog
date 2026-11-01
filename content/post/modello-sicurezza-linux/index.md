---
title: "Il modello di sicurezza di Linux"
description: "Prima di indurire qualcosa bisogna capire come Linux decide chi può fare cosa: la separazione kernel/userspace, l'identità basata su UID/GID, il controllo d'accesso discrezionale (DAC) dei permessi e il ruolo speciale di root. Da qui nasce ogni altra protezione, e si capisce perché root è sia la chiave che il problema."
slug: "modello-sicurezza-linux"
date: 2026-01-13T09:00:00+01:00
lastmod: 2026-01-13T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Fondamenti
keywords:
    - modello sicurezza linux
    - UID GID
    - DAC
    - kernel userspace
image: "cover.png"
toc: true
links:
  - title: "The Linux Programming Interface"
    description: "Testo di riferimento su processi, credenziali e permessi in Linux."
    website: https://man7.org/tlpi/
  - title: "man 7 credentials"
    description: "La pagina di manuale su UID, GID e credenziali dei processi."
    website: https://man7.org/linux/man-pages/man7/credentials.7.html
---

## Il punto di partenza

Non si indurisce ciò che non si capisce. Prima di toccare SSH, firewall o SELinux conviene avere
chiaro il meccanismo base: *come fa il kernel a decidere se un processo può aprire quel file, uccidere
quel processo, aprire quella porta?* La risposta sta in tre idee — separazione kernel/userspace,
identità numerica, controllo discrezionale — e in un'eccezione che le attraversa tutte: **root**.

## Kernel e userspace: due mondi

Il codice gira in due anelli. Il **kernel** ha accesso diretto all'hardware e alla memoria; le tue
applicazioni girano in **userspace**, isolate, e per fare qualcosa di privilegiato (leggere un file,
usare la rete) devono *chiedere* al kernel tramite una **system call**. È il kernel, a ogni syscall, a
controllare i permessi. Questo confine è la prima barriera di sicurezza: un processo userspace non può
scavalcare il kernel, può solo chiedere — e ricevere un sì o un `EACCES`.

```bash
# Osserva le syscall che un processo esegue (e dove gli viene negato l'accesso)
strace -f -e trace=openat ls /root 2>&1 | grep -i denied
# openat(AT_FDCWD, "/root", ...) = -1 EACCES (Permission denied)
```

## L'identità è un numero

Per Linux non sei "matteo": sei un **UID** (user ID) e uno o più **GID** (group ID). Il nome è solo
un'etichetta leggibile in `/etc/passwd`. Ogni processo porta con sé le credenziali di chi l'ha avviato,
e il kernel usa *quei numeri* per decidere.

```bash
id            # uid=1000(matteo) gid=1000(matteo) groups=1000(matteo),27(sudo),...
ps -eo pid,user,comm | head   # ogni processo ha un proprietario
```

Un dettaglio che conterà per l'hardening: esistono UID bassi (sotto 1000, per convenzione) riservati ai
**account di sistema** dei servizi, e l'UID **0**, che è speciale.

## DAC: il controllo discrezionale

Il modello di default di Linux è il **DAC (Discretionary Access Control)**: ogni risorsa ha un
proprietario, e *il proprietario decide* (a sua discrezione) i permessi. Un file ha un utente, un
gruppo e tre terzine di permessi; il kernel confronta l'UID/GID del processo con quelli del file.

```bash
ls -l /etc/shadow
# -rw-r----- 1 root shadow 1234 ... /etc/shadow
#   ^proprietario root, gruppo shadow: solo loro leggono gli hash delle password
```

"Discrezionale" è anche il suo limite: se sei proprietario puoi aprire un file a tutti, e nessuna
politica di sistema te lo impedisce. È il motivo per cui esistono i controlli **obbligatori (MAC)** —
SELinux, AppArmor — che vedremo più avanti: aggiungono una politica che il proprietario *non* può
scavalcare.

## Root: la chiave e il problema

L'UID **0** (root) è l'eccezione: il kernel, per la maggior parte dei controlli DAC, semplicemente *non
li applica* a root. Root può leggere ogni file, terminare ogni processo, aprire ogni porta. Questo lo
rende insieme indispensabile e il bersaglio numero uno: **compromettere root = compromettere il
sistema**. Tutta la serie, in un certo senso, ruota attorno a una domanda: *come dare il potere di root
il meno possibile, al minor numero di processi, per il minor tempo?*

```text {hl_lines=[2,3]}
Conseguenze pratiche di questo modello (le useremo nei prossimi capitoli):
  - meno processi girano da root, meno vale una loro compromissione  → cap. 9, 16
  - i permessi vanno stretti perché il DAC si fida del proprietario   → cap. 3, 4
  - root va reso irraggiungibile direttamente (sudo, no root via SSH) → cap. 5, 6
  - serve una politica che nemmeno root/owner possa aggirare (MAC)    → cap. 17, 18
```

## Conclusione

Linux decide gli accessi confrontando le credenziali numeriche di un processo con i permessi delle
risorse, al confine del kernel, secondo un modello discrezionale in cui root è l'eccezione totale.
Tenere a mente questo spiega *perché* ogni tecnica di hardening esiste. Il primo posto dove applicarlo
sono gli attori stessi del sistema: gli [utenti, i gruppi e gli
account]({{< relref "post/utenti-gruppi-account" >}}), prossimo capitolo.
