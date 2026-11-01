---
title: "Autenticazione e PAM"
description: "Sotto login, SSH e sudo c'è PAM, il sistema modulare che decide come Linux autentica e quali regole applica: qualità delle password, blocco dopo troppi tentativi, limiti di sessione, secondo fattore. Capire gli stack PAM ti dà il controllo centrale su tutte le autenticazioni del sistema, senza toccare i singoli programmi."
slug: "autenticazione-pam"
date: 2026-02-24T09:00:00+01:00
lastmod: 2026-02-24T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - PAM
keywords:
    - PAM
    - pam_faillock
    - pam_pwquality
    - autenticazione linux
image: "cover.png"
toc: true
links:
  - title: "The Linux-PAM System Administrators' Guide"
    description: "Guida ufficiale alla configurazione degli stack PAM."
    website: https://www.man7.org/linux/man-pages/man8/pam.8.html
  - title: "man 8 pam_faillock"
    description: "Blocco degli account dopo ripetuti fallimenti di autenticazione."
    website: https://man7.org/linux/man-pages/man8/pam_faillock.8.html
---

## Perché conta

`login`, `sshd`, `sudo`, `su`, lo screen lock: tutti devono autenticare un utente, ma nessuno di loro
implementa l'autenticazione. La delegano a **PAM (Pluggable Authentication Modules)**. Questo significa
che puoi cambiare *come* il sistema autentica — imporre password robuste, bloccare dopo troppi
tentativi, aggiungere un secondo fattore — modificando PAM una volta, e la regola vale per tutti i
programmi insieme. È il punto di controllo centrale dell'autenticazione.

## Come è fatto uno stack PAM

I file stanno in `/etc/pam.d/`, uno per servizio (`sshd`, `login`, `sudo`, `common-*` su Debian,
`system-auth` su RHEL). Ogni riga è: **tipo  controllo  modulo  argomenti**.

```text {hl_lines=[2,3,4,5]}
# i quattro TIPI (gruppi di gestione):
auth      → verifica l'identità (password, chiave, token)
account   → l'account è valido/abilitato/non scaduto?
password  → regole per CAMBIARE la password
session   → cosa fare all'apertura/chiusura di sessione (limiti, log, mount)
```

Il **controllo** decide il peso di ogni modulo: `required` (deve passare, ma continua), `requisite`
(deve passare, altrimenti stop), `sufficient` (se passa, basta), `optional`. L'ordine conta: gli stack
si leggono dall'alto in basso.

## Password robuste con pwquality

Il modulo `pam_pwquality` impone requisiti alle nuove password (lunghezza, classi di caratteri, non
basate su parole del dizionario).

```text {hl_lines=[2,3]}
# /etc/security/pwquality.conf
minlen = 14
minclass = 3          # almeno 3 tra: minuscole, maiuscole, cifre, simboli
dictcheck = 1         # rifiuta password basate su parole comuni
retry = 3
```

La logica moderna: **lunghezza > complessità**. Una passphrase lunga batte una password corta e
contorta, ed è più facile da ricordare (quindi non finisce su un post-it).

## Bloccare i bruteforce locali con faillock

`pam_faillock` blocca un account dopo N tentativi falliti — difesa contro il bruteforce di `login`,
`su`, console.

```text {hl_lines=[2,3]}
# /etc/security/faillock.conf
deny = 5              # blocca dopo 5 fallimenti
unlock_time = 900     # per 15 minuti
fail_interval = 900   # conteggiati entro 15 min
```

```bash
faillock --user matteo              # quanti fallimenti ha accumulato
faillock --user matteo --reset      # sblocca manualmente
```

## Limiti di sessione

`pam_limits` (via `/etc/security/limits.conf`) impone tetti alle risorse per utente — una difesa contro
esaurimento di risorse e fork bomb.

```text {hl_lines=[2,3]}
# /etc/security/limits.conf   (dominio  tipo  elemento  valore)
*           hard    nproc     2048      # max processi per utente
*           hard    nofile    8192      # max file aperti
@developers soft    core      0         # niente core dump per il gruppo developers
```

## Secondo fattore (cenno)

PAM è anche dove si innesta la 2FA: `pam_google_authenticator` aggiunge un codice TOTP allo stack
`auth` di `sshd`, così entrare richiede *chiave + codice*. È il modo di combinare l'[SSH a
chiave]({{< relref "post/hardening-ssh" >}}) con un secondo fattore.

## La regola d'oro: non chiuderti fuori

Un errore nello stack `auth` può impedire *qualsiasi* login, incluso root. Testa sempre in una sessione
nuova tenendone una aperta, e sappi dove sono i backup dei file PAM.

```text {hl_lines=[2]}
# rete di sicurezza:
tieni una sessione root aperta mentre modifichi, e un backup: cp -a /etc/pam.d /etc/pam.d.bak
```

## Conclusione

PAM è il punto unico da cui governare qualità password, blocco dopo i fallimenti, limiti di sessione e
secondo fattore — cambi lì, vale per tutti. Chiusi gli accessi (account, permessi, sudo, SSH, PAM),
l'attenzione si sposta su ciò che *gira* sul sistema: i servizi. E in Linux moderno i servizi sono
gestiti da systemd — [servizi e unit]({{< relref "post/systemd-servizi-e-unit" >}}), prossimo capitolo.
