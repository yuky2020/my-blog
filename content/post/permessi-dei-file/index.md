---
title: "I permessi dei file"
description: "rwx per utente, gruppo e altri: è il cuore del controllo d'accesso di Linux, e capirlo a fondo — notazione ottale, chmod, chown, umask — evita gli errori che aprono dati a chi non dovrebbe. Perché un permesso di troppo su un file di configurazione o una chiave privata vale una compromissione."
slug: "permessi-dei-file"
date: 2026-01-27T09:00:00+01:00
lastmod: 2026-01-27T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Permessi
keywords:
    - permessi file linux
    - chmod ottale
    - umask
    - chown
image: "cover.png"
toc: true
links:
  - title: "man 1 chmod"
    description: "Cambiare i permessi, notazione simbolica e ottale."
    website: https://man7.org/linux/man-pages/man1/chmod.1.html
  - title: "man 2 umask"
    description: "La maschera che determina i permessi di default dei nuovi file."
    website: https://man7.org/linux/man-pages/man2/umask.2.html
---

## Perché conta

Il [DAC di Linux]({{< relref "post/modello-sicurezza-linux" >}}) si regge sui permessi dei file. Un
permesso troppo largo è una fuga di dati silenziosa: una chiave SSH privata leggibile dal gruppo, un
file di configurazione con una password del database aperto a tutti, uno script modificabile da chi
non dovrebbe. Nessun alert suona — finché qualcuno non ne approfitta. Padroneggiare i permessi è
l'abilità più elementare e più sbagliata dell'amministrazione.

## Leggere `ls -l`

```text
-rw-r-----  1  matteo  devs   1240  gen 10 12:00  config.yml
│└┬┘└┬┘└┬┘   │    │      │
│ │  │  └ altri: ---     │      │
│ │  └── gruppo: r--     │      └ gruppo proprietario
│ └───── utente: rw-     └ utente proprietario
└ tipo: - file, d dir, l link
```

Tre terzine: **utente** (owner), **gruppo**, **altri**. Ogni terzina è `r` (lettura), `w`
(scrittura), `x` (esecuzione). Il kernel sceglie *una sola* terzina: se sei l'owner usa la prima; se no
ma sei nel gruppo, la seconda; altrimenti la terza. Non si sommano.

## L'ottale, velocemente

Ogni terzina è un numero: `r=4`, `w=2`, `x=1`, sommati.

```text {hl_lines=[2,5]}
rwx = 7   r-x = 5   r-- = 4
rw- = 6   -wx = 3   -w- = 2

644 = rw-r--r--   (file leggibile da tutti, scrivibile dall'owner)
600 = rw-------   (solo l'owner: giusto per chiavi e segreti)
755 = rwxr-xr-x   (eseguibile/dir accessibile a tutti)
750 = rwxr-x---   (owner pieno, gruppo esegue, altri niente)
```

## chmod e chown in pratica

```bash
chmod 600 ~/.ssh/id_ed25519          # chiave privata: solo tu (SSH lo pretende)
chmod 644 /etc/motd                  # leggibile da tutti, scrivibile solo da root
chmod -R u=rwX,g=rX,o= /srv/app      # X = esegui solo se è dir o già eseguibile
chown -R appuser:appgrp /srv/app     # proprietario utente:gruppo
```

La `X` maiuscola è un trucco utile: applica `x` alle directory (che vanno attraversate) ma non ai file
di dati, evitando di rendere eseguibile per errore un file di testo.

## umask: i permessi di default

Quando crei un file, i suoi permessi sono `666 & ~umask` (per i file) e `777 & ~umask` (per le dir).
La umask *sottrae* permessi.

```bash
umask                 # tipico: 0022  → i nuovi file nascono 644, le dir 755
umask 027             # più stretto: file 640, dir 750 (gli "altri" non leggono)
```

Impostare `umask 027` per gli account di sistema e i servizi fa sì che i file nuovi non siano leggibili
dal mondo per default — una difesa passiva che non richiede di ricordarsi `chmod` ogni volta.

## I file che DEVONO essere stretti

```bash
# audit rapido dei permessi su file sensibili
stat -c '%a %U:%G %n' /etc/shadow /etc/gshadow        # atteso: 640 o 000, root
stat -c '%a %U:%G %n' ~/.ssh/id_* 2>/dev/null         # atteso: 600
find / -xdev -type f -perm -0002 2>/dev/null          # file scrivibili da TUTTI (world-writable): da indagare
find /etc -type f -perm -0004 -name '*.key' 2>/dev/null  # chiavi leggibili da altri: male
```

I **world-writable** (`-perm -0002`) sono il sospetto classico: un file che chiunque può modificare è
un file di cui non puoi fidarti — soprattutto se è uno script eseguito da root.

## Conclusione

I permessi rwx, letti bene e stretti dove serve (600 per i segreti, umask 027 come default), chiudono
la fuga di dati più banale e più comune. Restano tre bit che cambiano le regole del gioco e sono
sorgente di vulnerabilità gravi quando usati male: SUID, SGID e lo sticky bit. Sono il prossimo
capitolo, [i permessi speciali]({{< relref "post/permessi-speciali-suid-sgid" >}}).
