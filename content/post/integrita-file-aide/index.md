---
title: "Integrità dei file con AIDE"
description: "Una delle mosse classiche di un attaccante è sostituire un binario di sistema o aggiungere una backdoor: modifiche silenziose che nessun log applicativo racconta. AIDE crea una fotografia crittografica dei file critici e segnala ogni scostamento. Come costruire la baseline, controllare, e perché il database di riferimento va tenuto al sicuro."
slug: "integrita-file-aide"
date: 2026-06-02T09:00:00+02:00
lastmod: 2026-06-02T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Integrità
keywords:
    - AIDE
    - file integrity monitoring
    - baseline
    - rootkit
image: "cover.png"
toc: true
links:
  - title: "AIDE — Advanced Intrusion Detection Environment"
    description: "Documentazione del tool di controllo dell'integrità dei file."
    website: https://aide.github.io/
  - title: "man 1 aide"
    description: "Uso del comando aide per inizializzare e verificare il database."
    website: https://man7.org/linux/man-pages/man1/aide.1.html
---

## Perché conta

Dopo aver ottenuto accesso, un attaccante spesso vuole *restare* e *nascondersi*: sostituisce un binario
di sistema con una versione con backdoor, aggiunge una chiave SSH in un `authorized_keys`, modifica un
file di configurazione, pianta un rootkit. Sono modifiche silenziose: nessun log applicativo le
racconta, i file sembrano normali. Il **file integrity monitoring** risponde a una domanda che nessun
altro strumento pone: *questo file è ancora quello che mi aspetto, o è stato cambiato?* **AIDE** lo fa
confrontando lo stato attuale con una **baseline** crittografica.

## Come funziona

AIDE calcola, per ogni file sorvegliato, un'impronta (hash, più attributi: permessi, owner, dimensione,
timestamp) e la salva in un **database di riferimento**. A ogni controllo successivo ricalcola e
confronta: qualsiasi scostamento — un binario cambiato, un permesso allargato, un file nuovo in un
percorso di sistema — viene segnalato.

```mermaid
flowchart LR
    B[Baseline:<br/>hash dei file "sani"] --> C{Confronto<br/>periodico}
    S[Stato attuale<br/>dei file] --> C
    C -->|identici| OK[Nessun allarme]
    C -->|differenze| AL[Report: cosa è<br/>cambiato/aggiunto/rimosso]
    style AL fill:#fde2e4,stroke:#e63946
```

## Baseline e controlli

```bash
apt install aide          # oppure: dnf install aide
# 1. definisci COSA sorvegliare in /etc/aide/aide.conf (binari, /etc, boot, ...)
# 2. crea la baseline su un sistema che consideri SANO (es. appena installato e indurito)
aideinit                  # Debian/Ubuntu     (aide --init su altre distro)
mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db

# 3. controllo periodico: confronta lo stato attuale con la baseline
aide --check
# AIDE found differences between database and filesystem!!
# changed: /usr/bin/ssh    ← un binario di sistema modificato = allarme rosso
```

Cosa sorvegliare: binari (`/usr/bin`, `/usr/sbin`, `/bin`, `/sbin`), `/etc`, i file di boot, i moduli
kernel. Cosa *escludere*: directory che cambiano continuamente in modo legittimo (`/var/log`, `/proc`,
cache), altrimenti ogni report è pieno di rumore.

## Il punto critico: proteggere la baseline

Il database di riferimento è il tallone d'Achille: se un attaccante può modificarlo, aggiorna la
baseline dopo aver piazzato la backdoor e AIDE non segnala più nulla. Perciò la baseline va tenuta
**fuori portata**.

```text {hl_lines=[2,3,4]}
Proteggere il database AIDE:
  - copiarlo su supporto a sola lettura o host separato dopo ogni aggiornamento legittimo
  - firmarlo / verificarne l'hash da una fonte fidata
  - eseguire il check da un contesto che l'attaccante non controlla, se possibile
  - aggiornare la baseline SOLO dopo cambiamenti legittimi noti (es. dopo gli update)
```

## Automatizzare e distinguere il rumore

Un controllo AIDE schedulato (timer systemd o cron) invia un report periodico. La sfida è distinguere i
cambiamenti **legittimi** (un aggiornamento di pacchetti cambia molti binari — tutto normale) da quelli
**sospetti**. Per questo il controllo va fatto *dopo* gli aggiornamenti pianificati, aggiornando la
baseline, così che fuori da quelle finestre ogni cambiamento sia davvero anomalo.

## Conclusione

AIDE fotografa crittograficamente i file critici e segnala ogni scostamento — binari sostituiti,
backdoor, permessi allargati — purché la baseline sia tenuta al sicuro e aggiornata solo dopo i
cambiamenti legittimi. Finora abbiamo protetto il sistema "piatto"; i prossimi capitoli guardano
all'isolamento e al kernel. Primo: i [namespaces e l'isolamento]({{< relref
"post/namespaces-e-isolamento" >}}), fondamento dei container.
