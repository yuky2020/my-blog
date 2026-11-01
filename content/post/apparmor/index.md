---
title: "AppArmor"
description: "AppArmor è l'altro controllo d'accesso obbligatorio di Linux, diffuso su Ubuntu e SUSE: confina i programmi con profili basati sui percorsi dei file, più leggibili delle etichette di SELinux. Profili in enforce o complain, come leggerli, scriverli e metterli a punto. Quando preferirlo e in cosa differisce da SELinux."
slug: "apparmor"
date: 2026-05-12T09:00:00+02:00
lastmod: 2026-05-12T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - AppArmor
    - MAC
keywords:
    - AppArmor
    - mandatory access control
    - profili apparmor
    - aa-enforce
image: "cover.png"
toc: true
links:
  - title: "AppArmor Wiki"
    description: "Documentazione ufficiale di AppArmor, profili e strumenti."
    website: https://gitlab.com/apparmor/apparmor/-/wikis/home
  - title: "Ubuntu — AppArmor"
    description: "Guida all'uso di AppArmor sulle distribuzioni Ubuntu."
    website: https://ubuntu.com/server/docs/security-apparmor
---

## Perché conta

[SELinux]({{< relref "post/selinux" >}}) è potentissimo ma usa etichette e type, che molti trovano
ostici. **AppArmor** persegue lo stesso scopo — controllo d'accesso obbligatorio che confina i
programmi — con un modello diverso: **profili basati sui percorsi**. Un profilo dice, in un file di
testo leggibile, "questo programma può leggere qui, scrivere lì, usare queste capabilities, e
nient'altro". È il MAC di default su Ubuntu e SUSE, ed è spesso più immediato da capire e da scrivere.

## Lo stato dei profili

```bash
aa-status            # quali profili sono caricati e in quale modalità
# apparmor module is loaded.
# 30 profiles are in enforce mode.
#    /usr/sbin/nginx ...
# 5 profiles are in complain mode.
```

Come SELinux, ha due modalità operative per profilo:

```text {hl_lines=[2,3]}
enforce   → applica il profilo: ciò che non è permesso viene bloccato (produzione)
complain  → non blocca, ma LOGGA le violazioni → per mettere a punto un profilo nuovo
```

```bash
aa-enforce /etc/apparmor.d/usr.sbin.nginx    # metti un profilo in enforce
aa-complain /etc/apparmor.d/usr.sbin.nginx   # mettilo in complain (diagnosi)
```

## Leggere un profilo

I profili vivono in `/etc/apparmor.d/`. La sintassi è esplicita e leggibile:

```text {hl_lines=[4,5,7]}
#include <tunables/global>
/usr/local/bin/myapp {
  #include <abstractions/base>
  capability net_bind_service,          # può aprire porte basse
  /etc/myapp/** r,                      # legge la sua config
  /var/lib/myapp/** rw,                 # legge e scrive i suoi dati
  /var/log/myapp/app.log w,             # scrive il suo log
  network inet stream,                  # socket TCP
  # tutto ciò che non è elencato è NEGATO
}
```

La filosofia è la stessa del [privilegio minimo]({{< relref "post/principio-minimo-privilegio" >}}):
elenchi ciò che è permesso, tutto il resto è vietato. Se `myapp` viene compromesso, non può leggere
`/etc/shadow` né scrivere fuori dalle sue directory: non è nel profilo.

## Mettere a punto un profilo nuovo

AppArmor ha strumenti che *generano* il profilo osservando l'applicazione in funzione:

```bash
aa-genprof /usr/local/bin/myapp     # avvia la generazione guidata: usa l'app, poi conferma gli accessi
aa-logprof                          # rivede i log e propone di aggiungere al profilo gli accessi visti
```

Il flusso tipico: metti il profilo in `complain`, usi l'applicazione normalmente, poi `aa-logprof`
legge cosa ha fatto e ti chiede quali accessi autorizzare. Confermi solo quelli legittimi, passi a
`enforce`.

## SELinux o AppArmor?

```text {hl_lines=[1,2]}
AppArmor  → profili per-percorso, leggibili, rapidi da scrivere; default Ubuntu/SUSE
SELinux   → etichette/type, più granulare e rigoroso; default RHEL/Fedora/Android
```

Non si scelgono: di solito **usi quello della tua distribuzione** (sono alternativi, non si installano
insieme). Il principio è identico — una politica obbligatoria che confina i programmi oltre il DAC —
e vale la regola d'oro di entrambi: davanti a un problema, **metti in complain/permissive e diagnostica,
non disabilitare**.

## Conclusione

AppArmor confina i programmi con profili per-percorso leggibili, in enforce o complain, con strumenti
che li generano osservando l'app: lo stesso MAC di SELinux con un'ergonomia diversa. Confinamento e
controlli sono in posto; ma un sistema sicuro è anche un sistema *osservato*. Passiamo al monitoraggio:
l'[auditing con auditd]({{< relref "post/auditd" >}}), prossimo capitolo.
