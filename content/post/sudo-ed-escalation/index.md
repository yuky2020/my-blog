---
title: "sudo e l'escalation controllata"
description: "Dare a una persona i poteri di root senza consegnarle la password di root: è il compito di sudo, che concede privilegi in modo granulare e tracciato. Ma un sudoers scritto male regala root invece di prestarlo. Come configurarlo col privilegio minimo, evitare le trappole (NOPASSWD, wildcard, ALL) e leggere cosa può fare un utente."
slug: "sudo-ed-escalation"
date: 2026-02-10T09:00:00+01:00
lastmod: 2026-02-10T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - sudo
keywords:
    - sudo
    - sudoers
    - privilege escalation
    - NOPASSWD
image: "cover.png"
toc: true
links:
  - title: "man 5 sudoers"
    description: "La sintassi completa del file sudoers."
    website: https://man7.org/linux/man-pages/man5/sudoers.5.html
  - title: "Sudo — Security Policies"
    description: "Documentazione ufficiale sulle policy e le best practice."
    website: https://www.sudo.ws/docs/man/sudoers.man/
---

## Perché conta

Dare la password di root a un amministratore è un errore su più fronti: non è tracciabile (tutti sono
"root", nessuno è responsabile), non è revocabile singolarmente, e dà poteri totali per un compito che
magari ne richiede uno solo. **sudo** risolve tutto questo: ogni utente usa la *propria* password,
esegue solo i comandi che gli concedi, e ogni uso è **loggato**. Ma sudo è potente quanto il suo file
di configurazione — e un `sudoers` sciatto è una scalata a root servita.

## La regola base

Si modifica *sempre* con `visudo`, che valida la sintassi prima di salvare (un errore di sintassi può
chiuderti fuori da sudo).

```bash
visudo                      # modifica /etc/sudoers con validazione
visudo -f /etc/sudoers.d/ops   # meglio: file separati in sudoers.d/
```

Una regola ha la forma: `CHI  SU-QUALI-HOST = (COME-QUALE-UTENTE)  QUALI-COMANDI`.

```text {hl_lines=[2,5]}
# dare TUTTO (comodo, pericoloso): l'utente diventa root a piacere
matteo  ALL=(ALL:ALL) ALL

# privilegio minimo: solo i comandi che servono davvero
deploy  ALL=(root) /usr/bin/systemctl restart myapp, /usr/bin/journalctl -u myapp *
backup  ALL=(root) /usr/bin/rsync
```

La seconda forma è l'obiettivo: `deploy` può riavviare *il suo* servizio e leggerne i log, nient'altro.
Non può aprire una shell di root.

## Le trappole che regalano root

```text {hl_lines=[1,3,5]}
NOPASSWD: ALL        → chi ottiene la sessione dell'utente ha root senza nemmeno una password
comandi con wildcard → /usr/bin/vi *  permette :!sh  → shell di root (vedi GTFOBins)
editor/pager/interpreti → less, vi, man, python: quasi tutti possono lanciare una shell
ALL con (ALL:ALL)    → può diventare QUALUNQUE utente, non solo root
```

Il tranello più sottile: concedere un comando "innocuo" che però può **evadere in una shell**. `sudo
vi`, `sudo less`, `sudo find`, `sudo python` → da ciascuno si apre una shell di root. Se devi concedere
un editor, usa `sudoedit` (apre il file coi tuoi privilegi, non una shell di root):

```text
# invece di: alice ALL=(root) /usr/bin/vi /etc/nginx/nginx.conf   (evadibile!)
alice  ALL=(root) sudoedit /etc/nginx/nginx.conf
```

## Leggere e verificare i privilegi

```bash
sudo -l                 # cosa posso eseguire io con sudo? (da lanciare come l'utente)
sudo -l -U deploy       # cosa può fare l'utente 'deploy' (da root)
```

`sudo -l` è il primo comando che esegue un attaccante dopo aver preso un account — fallo prima tu, su
ogni account con sudo, e chiediti: "questa riga permette di diventare root in modo imprevisto?".

## Irrobustire sudo

```text {hl_lines=[2,4]}
# in /etc/sudoers.d/hardening
Defaults  timestamp_timeout=5      # la "memoria" della password dura 5 min, non 15
Defaults  passwd_tries=3           # tentativi prima di abortire
Defaults  logfile="/var/log/sudo.log"   # log dedicato, oltre al journal
Defaults  requiretty               # niente sudo da sessioni non-tty (riduce abusi da script)
Defaults  use_pty                  # esegui in uno pseudo-tty (ostacola alcuni attacchi)
```

E la cosa più importante: **chi è nel gruppo sudo/wheel?** Quel gruppo è la porta principale a root.
Tienilo corto e rivisto — è lo stesso ragionamento degli [account e gruppi
potenti]({{< relref "post/utenti-gruppi-account" >}}).

## Conclusione

sudo presta i poteri di root in modo tracciato e granulare — se il sudoers rispetta il privilegio
minimo, evita NOPASSWD e wildcard, e non concede comandi che aprono shell. È la via corretta per
l'accesso privilegiato *locale*. Ma la maggior parte degli accessi a un server arriva da remoto, ed è
lì che si gioca la prima linea: l'[hardening di SSH]({{< relref "post/hardening-ssh" >}}), prossimo
capitolo.
