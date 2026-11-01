---
title: "systemd: servizi e unit"
description: "systemd governa cosa parte all'avvio e cosa resta in ascolto: ogni servizio di troppo è superficie d'attacco in più. Capire le unit, enable/disable/mask e come leggere lo stato è il prerequisito per ridurre ciò che gira e, nel capitolo successivo, per metterlo in gabbia. I comandi che contano per l'hardening."
slug: "systemd-servizi-e-unit"
date: 2026-03-03T09:00:00+01:00
lastmod: 2026-03-03T09:00:00+01:00
categories:
    - Security
    - DevOps
tags:
    - Linux
    - Hardening
    - systemd
keywords:
    - systemd
    - unit file
    - systemctl
    - disable mask
image: "cover.png"
toc: true
links:
  - title: "man 1 systemctl"
    description: "Il comando per controllare lo stato del sistema e dei servizi."
    website: https://man7.org/linux/man-pages/man1/systemctl.1.html
  - title: "man 5 systemd.unit"
    description: "Struttura e direttive comuni dei file unit."
    website: https://man7.org/linux/man-pages/man5/systemd.unit.5.html
---

## Perché conta

Ogni servizio attivo è una porta potenziale: ascolta su una socket, gira con certi privilegi, ha un
suo codice con sue vulnerabilità. Il principio della **superficie minima** dice: ciò che non gira non
può essere attaccato. Prima di indurire i servizi, bisogna *vederli* e *spegnere quelli che non
servono*. È il lavoro di systemd, il gestore di servizi (e molto altro) di Linux moderno.

## Vedere cosa gira e cosa ascolta

```bash
systemctl list-units --type=service --state=running   # servizi attivi ORA
systemctl list-unit-files --state=enabled              # cosa parte al boot
systemd-analyze blame                                  # cosa rallenta l'avvio (e cosa c'è)
ss -tulpn                                               # porte in ascolto + processo (vedi cap. 12)
```

La domanda da farsi su ogni voce: *mi serve davvero?* Un server web non ha bisogno di un server di
stampa, un demo Bluetooth, un resolver mDNS. Ogni "no" è superficie d'attacco rimossa.

## Anatomia di una unit

Una unit di servizio è un file `.ini`. Quelle del sistema stanno in `/usr/lib/systemd/system/`; le tue
personalizzazioni in `/etc/systemd/system/` (che ha la precedenza).

```text {hl_lines=[6,9]}
# /etc/systemd/system/myapp.service
[Unit]
Description=La mia applicazione
After=network-online.target

[Service]
ExecStart=/usr/local/bin/myapp --config /etc/myapp.yml
User=myapp                 # NON girare da root: account dedicato (vedi cap. 2)
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Due righe pesano per la sicurezza: `User=myapp` (il servizio gira con un account non privilegiato, non
root) e tutto ciò che aggiungeremo nel prossimo capitolo per sandboxarlo.

## enable, disable, mask

```bash
systemctl stop  cups.service          # fermalo ora
systemctl disable cups.service        # non parte più al boot
systemctl mask cups.service           # lo "blinda": non può essere avviato in alcun modo
```

La differenza che conta: **disable** toglie l'avvio automatico ma qualcosa può ancora avviarlo (una
dipendenza, un socket). **mask** crea un link a `/dev/null`: il servizio è *impossibile* da avviare
finché non lo smaschera. Per i servizi che vuoi davvero fuori gioco, `mask` è la scelta sicura.

## Socket e timer: attivazione pigra

systemd può tenere un servizio *spento* e avviarlo solo alla prima connessione (socket activation), o
su schedule (timer, il moderno sostituto di cron). Dal lato sicurezza: un servizio attivato on-demand
non è un processo che gira e aspetta di essere attaccato per ore inutili.

```bash
systemctl list-timers                 # i job schedulati (al posto di crontab)
systemctl list-sockets
```

## Il riflesso dell'hardening

```text {hl_lines=[1,3]}
Checklist su ogni servizio:
  1. serve? NO  → stop + disable + mask
  2. serve? SÌ  → gira da account dedicato (User=), non root?
  3. serve? SÌ  → è sandboxato? (prossimo capitolo)
  4. serve? SÌ  → ascolta solo dove deve? (0.0.0.0 vs 127.0.0.1 → cap. 12)
```

## Conclusione

Vedere i servizi, spegnere e `mask`are l'inutile, far girare il resto da account dedicati: così si
riduce la superficie prima ancora di indurire. Ma i servizi che *devono* restare attivi vanno messi in
gabbia, perché anche un servizio non-root può fare danni se compromesso. systemd offre un sandboxing
potente e sottovalutato: è il [prossimo capitolo]({{< relref "post/systemd-hardening-servizi" >}}).
