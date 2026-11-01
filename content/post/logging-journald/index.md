---
title: "Logging e journald"
description: "I log raccontano cosa fa il sistema, ma solo se sono persistenti, protetti e, idealmente, spediti altrove: un attaccante che prende root cancella i log locali per nascondersi. journald, log persistenti, interrogazioni efficaci con journalctl e l'inoltro a un collettore remoto perché le prove sopravvivano a chi vuole cancellarle."
slug: "logging-journald"
date: 2026-05-26T09:00:00+02:00
lastmod: 2026-05-26T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Logging
keywords:
    - journald
    - journalctl
    - log persistenti
    - log remoti
image: "cover.png"
toc: true
links:
  - title: "man 1 journalctl"
    description: "Interrogare il journal di systemd."
    website: https://man7.org/linux/man-pages/man1/journalctl.1.html
  - title: "man 5 journald.conf"
    description: "Configurazione di persistenza, dimensione e inoltro del journal."
    website: https://man7.org/linux/man-pages/man5/journald.conf.5.html
---

## Perché conta

[auditd]({{< relref "post/auditd" >}}) cattura gli eventi di sicurezza; **journald** raccoglie tutto il
resto — messaggi dei servizi, del kernel, del boot, delle sessioni. Ma un log serve a qualcosa solo se
ci sarà quando ne avrai bisogno. Due problemi ricorrenti: i log non sono persistenti (spariscono al
riavvio), oppure un attaccante che ottiene root li cancella per nascondere le proprie tracce — di
solito il log tampering è una delle prime mosse dopo una compromissione. Hardening del logging significa
renderli **persistenti, protetti e fuori portata**.

## Rendere il journal persistente

Per default alcuni sistemi tengono il journal solo in memoria (si perde al reboot). Si rende
persistente scrivendolo su disco:

```text {hl_lines=[2,4,5]}
# /etc/systemd/journald.conf
[Journal]
Storage=persistent          # scrive in /var/log/journal (sopravvive ai riavvii)
SystemMaxUse=2G             # tetto allo spazio usato
MaxRetentionSec=1month     # quanto conservare
```
```bash
mkdir -p /var/log/journal && systemctl restart systemd-journald
journalctl --disk-usage          # quanto occupa il journal
```

## journalctl: interrogare bene

```bash
journalctl -u sshd -e                      # log del servizio sshd, dalla fine
journalctl -p err -b                        # solo errori, dal boot corrente
journalctl --since "2026-05-26 00:00" --until "2026-05-26 12:00"
journalctl _UID=1000                        # tutto ciò che riguarda un certo utente
journalctl -f                               # segui in tempo reale (come tail -f)
journalctl -k                               # messaggi del kernel (dmesg)
```

I campi strutturati (`_UID=`, `_PID=`, `_SYSTEMD_UNIT=`) sono il vantaggio di journald rispetto ai
vecchi file di testo: filtri su metadati, non con grep fragile.

## Proteggere i log dal tampering

I log *locali* sono sotto il controllo di chi ha root sulla macchina — quindi di un attaccante che ha
vinto. La difesa è **spedirli altrove**, su un host che l'attaccante non controlla, in tempo reale:

```text {hl_lines=[2,3]}
Opzioni per i log remoti (centralizzazione):
  - systemd-journal-remote/-upload : journald → host raccoglitore via HTTPS
  - rsyslog/syslog-ng → un server syslog o un SIEM centrale
  - append-only sul collettore: i log, una volta spediti, non si riscrivono
```

Il principio è lo stesso dell'[audit trail immutabile nel cloud]({{< relref
"post/logging-e-audit-trail" >}}): chi compromette la macchina può ripulire i log locali, ma non quelli
già arrivati su un sistema separato. Senza inoltro remoto, l'indagine su una macchina compromessa parte
da prove potenzialmente già cancellate.

## Segnali da cercare nei log

```bash
journalctl -u sshd | grep -iE 'failed|invalid user'    # tentativi SSH falliti
journalctl _COMM=sudo                                   # usi di sudo
journalctl -p warning -b | head                         # anomalie recenti
```

Questi grep manuali vanno bene per un controllo occasionale; su scala, i log centralizzati alimentano
regole di detection automatiche (un SIEM) — ma è un tema a sé.

## Conclusione

Rendere il journal persistente, interrogarlo per campi con `journalctl`, e soprattutto **inoltrarlo a
un collettore remoto** perché sopravviva a chi vuole cancellarlo: così i log restano prove affidabili.
Log e audit dicono cosa è *successo*; resta da sapere se qualcosa è *cambiato* in silenzio — se un
binario di sistema è stato sostituito. È l'[integrità dei file con AIDE]({{< relref
"post/integrita-file-aide" >}}), prossimo capitolo.
