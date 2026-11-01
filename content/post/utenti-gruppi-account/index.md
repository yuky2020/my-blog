---
title: "Utenti, gruppi e account"
description: "Ogni account è una potenziale via d'ingresso: gli account di servizio senza login, le password deboli, gli account dimenticati che restano attivi. Come leggere passwd e shadow, distinguere gli account di sistema da quelli umani, bloccare ciò che non deve accedere e tenere pulito l'elenco di chi può entrare."
slug: "utenti-gruppi-account"
date: 2026-01-20T09:00:00+01:00
lastmod: 2026-01-20T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Account
keywords:
    - etc passwd
    - etc shadow
    - account di sistema
    - nologin
image: "cover.png"
toc: true
links:
  - title: "man 5 passwd"
    description: "Formato del file degli account di sistema."
    website: https://man7.org/linux/man-pages/man5/passwd.5.html
  - title: "man 5 shadow"
    description: "Formato del file degli hash e delle policy di scadenza password."
    website: https://man7.org/linux/man-pages/man5/shadow.5.html
---

## Il problema

Ogni account che può autenticarsi è una porta. Molte di queste porte non servono: account di servizio
creati dai pacchetti, utenti di test mai rimossi, account di ex collaboratori. Un attaccante che fa
bruteforce o riusa credenziali trapelate cerca proprio queste porte dimenticate. Il primo lavoro di
hardening sugli account è *sapere chi c'è* e *chiudere ciò che non deve entrare*.

## Leggere passwd e shadow

Gli account vivono in due file. `/etc/passwd` (leggibile da tutti) elenca gli account; `/etc/shadow`
(solo root) tiene gli hash delle password e le policy di scadenza.

```bash
# formato passwd: nome:x:UID:GID:commento:home:shell
grep -E ':[0-9]{4,}:' /etc/passwd    # account con UID >= 1000 = tipicamente umani
getent passwd | awk -F: '$3>=1000 && $3<65534 {print $1, $3, $7}'
```

Il campo chiave per la sicurezza è l'ultimo: la **shell**. Un account di servizio non deve avere una
shell interattiva.

```bash
# account di sistema (UID < 1000) che però hanno una shell di login = sospetto
awk -F: '$3<1000 && $7 ~ /sh$/ {print $1, $3, $7}' /etc/passwd
```

## Account di servizio: niente login

I demoni (nginx, postgres, ...) girano sotto account dedicati che **non devono poter fare login**. La
shell corretta per loro è `/usr/sbin/nologin` (o `/bin/false`): se qualcuno prova ad autenticarsi,
viene rifiutato.

```bash
# imposta nologin su un account di servizio
usermod -s /usr/sbin/nologin postgres

# blocca la password di un account (login via password impossibile; la ! in shadow)
passwd -l nomeutente
passwd -S nomeutente          # stato: L = locked, P = password set, NP = nessuna password
```

Attenzione a `NP` (nessuna password): un account senza password che accetta login è un buco grave.

```bash
# trova account con password VUOTA (gravissimo)
awk -F: '($2==""){print $1" NON ha password!"}' /etc/shadow
```

## Scadenza e policy

`chage` gestisce la vita di una password: scadenza, intervallo minimo/massimo, avviso. Non abusarne
(password che scadono troppo spesso spingono a sceglierne di deboli), ma su account sensibili serve.

```bash
chage -l matteo                 # mostra le date di scadenza
chage -M 365 -W 14 matteo       # max 365 giorni, avviso 14 giorni prima
```

## Mantenere pulito l'elenco

```text {hl_lines=[2,4]}
Controlli periodici sugli account:
  - chi ha UID 0 oltre a root? (NON dovrebbe essercene nessun altro)
  - chi appartiene ai gruppi potenti: sudo/wheel, docker, adm?
  - ci sono account di persone che non ci sono più?
  - ci sono account senza password o con shell dove non serve?
```

```bash
# chi altro ha UID 0 (= poteri di root)? deve stampare solo "root"
awk -F: '$3==0 {print $1}' /etc/passwd

# membri del gruppo che garantisce sudo (sudo su Debian, wheel su RHEL)
getent group sudo wheel docker
```

Il gruppo **docker** merita una nota: chi vi appartiene può, di fatto, diventare root (montando il
filesystem host in un container). Trattalo come appartenenza a wheel/sudo.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> gli account di servizio li crea il gestore pacchetti già configurati con nologin. Perché controllarli a mano se la distribuzione fa la cosa giusta di default?</summary>
<p>Perché "di default" copre il caso pulito ma non la realtà di un sistema vissuto, ed è proprio nelle
deviazioni dal default che si annidano i problemi. Primo, non tutti i pacchetti sono scrupolosi: software
di terze parti, script di installazione scaricati, vecchi pacchetti o configurazioni ereditate possono
creare account con shell di login "perché era comodo durante lo sviluppo". Secondo, i sistemi cambiano
mano: un account creato nologin può essere modificato nel tempo — qualcuno gli dà una shell per fare
debug e non la toglie, un ripristino da backup riporta una vecchia configurazione, una migrazione copia
account senza rivederli. Terzo, il controllo non serve solo a trovare l'errore del packager, ma a
mantenere una <em>baseline</em>: sapere esattamente quali account esistono e quali possono autenticarsi è
ciò che ti permette di accorgerti se ne compare uno nuovo e inatteso — che è uno dei segni classici di
una compromissione (un attaccante che si crea un account di persistenza). Non stai sfiduciando la
distribuzione: stai costruendo la conoscenza di "cosa è normale" sul <em>tuo</em> sistema, senza la quale
non puoi riconoscere l'anomalia. Il comando che elenca gli UID 0 o gli account senza password costa
secondi e va messo tra i controlli periodici proprio perché l'unico momento in cui scopri un account di
troppo non dev'essere dopo che è stato usato contro di te.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Sapere quali account esistono, dare `nologin` ai servizi, bloccare le password inutili, sorvegliare chi
ha UID 0 e le appartenenze a gruppi potenti: è l'igiene base degli accessi. Ma decidere *chi può
entrare* è metà del lavoro; l'altra metà è cosa ciascuno può *toccare* una volta dentro — i [permessi
dei file]({{< relref "post/permessi-dei-file" >}}), prossimo capitolo.
