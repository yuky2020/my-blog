---
title: "Auditing con auditd"
description: "auditd registra a livello di kernel chi ha fatto cosa: accessi a file sensibili, esecuzione di comandi, modifiche alla configurazione, uso di syscall. È la scatola nera del sistema, indispensabile per le indagini e per molti standard di compliance. Regole di audit utili, come interrogare i log con ausearch e aureport, e cosa vale la pena sorvegliare."
slug: "auditd"
date: 2026-05-19T09:00:00+02:00
lastmod: 2026-05-19T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Auditing
keywords:
    - auditd
    - audit rules
    - ausearch
    - audit linux
image: "cover.png"
toc: true
links:
  - title: "man 8 auditd"
    description: "Il demone di audit del kernel Linux."
    website: https://man7.org/linux/man-pages/man8/auditd.8.html
  - title: "man 7 audit.rules"
    description: "Sintassi delle regole di audit."
    website: https://man7.org/linux/man-pages/man8/auditctl.8.html
---

## Perché conta

Un sistema che non osservi è un sistema di cui non sai nulla: non puoi accorgerti di una compromissione,
né ricostruire cosa è successo dopo. **auditd** è la scatola nera di Linux: registra, a livello di
kernel, eventi di sicurezza — chi ha letto un file sensibile, chi ha eseguito un comando, chi ha
modificato la configurazione, quali syscall sono state invocate. È indispensabile per le indagini
forensi e richiesto da molti standard (PCI DSS, CIS). A differenza del semplice logging applicativo,
opera *sotto* le applicazioni, quindi è difficile da eludere.

## Come funziona

Il kernel genera eventi secondo le **regole** che carichi; `auditd` li scrive in
`/var/log/audit/audit.log`. Le regole possono sorvegliare *file* (watch) o *syscall* (con filtri).

```bash
auditctl -s                 # stato del sottosistema di audit
auditctl -l                 # regole attualmente caricate
```

## Regole utili

Si mettono in `/etc/audit/rules.d/*.rules` (caricate al boot). Due famiglie:

```text {hl_lines=[3,4,7,10]}
# --- WATCH sui file sensibili (-w percorso -p permessi -k etichetta) ---
# -p: r=read w=write x=exec a=attribute change ; -k: chiave per ritrovarli
-w /etc/passwd    -p wa -k identita        # modifiche agli account
-w /etc/shadow    -p wa -k identita
-w /etc/sudoers   -p wa -k escalation      # chi tocca le regole sudo
-w /etc/ssh/sshd_config -p wa -k sshd

# --- SYSCALL (-a azione,filtro -S syscall) ---
-a always,exit -F arch=b64 -S execve -k exec        # ogni comando eseguito
-a always,exit -F arch=b64 -S mount -S umount2 -k mount
-a always,exit -F arch=b64 -F euid=0 -S execve -k root_cmds   # comandi eseguiti da root
```

I **watch** su `/etc/passwd`, `/etc/shadow`, `/etc/sudoers` catturano esattamente le modifiche che un
attaccante fa per persistere (creare un account, darsi sudo). La regola su `execve` registra ogni
comando eseguito — preziosissima in un'indagine.

```bash
augenrules --load       # carica le regole da rules.d
auditctl -e 2           # rende la configurazione IMMUTABILE fino al reboot (1=on, 2=locked)
```

`-e 2` è importante: blocca le regole finché non si riavvia, così un attaccante non può disattivare
l'audit al volo per nascondersi.

## Interrogare i log

```bash
# tutti gli eventi con una certa chiave
ausearch -k identita -ts today
ausearch -k escalation -i          # -i = interpreta UID/syscall in forma leggibile
# chi ha eseguito cosa da root, oggi
ausearch -k root_cmds -ts today -i
# report riassuntivi
aureport --summary
aureport -au                       # tentativi di autenticazione
aureport -x --summary              # eseguibili più usati
```

Le **chiavi** (`-k`) sono il trucco di usabilità: etichetti le regole per argomento e poi filtri gli
eventi per argomento, senza grep a mano in un log enorme.

## Attenzione al volume

auditd può generare moltissimi eventi: la regola su `execve` su un sistema attivo produce molto. Si
bilancia — sorvegliare i file *davvero* sensibili e i comandi di root, non tutto — e si gestiscono
rotazione e spazio (`max_log_file`, `space_left_action` in `/etc/audit/auditd.conf`), inviando
idealmente i log a un collettore esterno (prossimo capitolo).

## Conclusione

auditd registra a livello di kernel chi tocca i file sensibili e chi esegue comandi, in modo difficile
da eludere (regole immutabili con `-e 2`), interrogabile per chiavi con `ausearch`/`aureport`: la
scatola nera per indagini e compliance. auditd è specializzato sugli eventi di sicurezza; il resto dei
log di sistema — servizi, kernel, boot — passa per journald, il [prossimo capitolo]({{< relref
"post/logging-journald" >}}).
