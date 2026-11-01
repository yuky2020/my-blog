---
title: "Linux Hardening in pratica: la serie"
description: "Una serie in 25 capitoli per mettere in sicurezza un sistema Linux davvero, comando dopo comando: dal modello di permessi a SSH, sudo, PAM, systemd sandboxing, nftables, SELinux/AppArmor, auditd, LUKS, kernel hardening e CIS. Non teoria astratta ma configurazioni reali, con esempi che puoi copiare e verificare."
slug: "linux-hardening-la-serie"
date: 2026-01-06T09:00:00+01:00
lastmod: 2026-01-06T09:00:00+01:00
weight: 2
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Sysadmin
    - Roadmap
keywords:
    - linux hardening
    - sicurezza linux
    - sysadmin
    - roadmap linux
image: "cover.png"
toc: true
---

## Perché questa serie

Un server Linux appena installato è comodo e insicuro: servizi in ascolto che non ti servono, un
account root raggiungibile via SSH con password, permessi larghi, nessun audit. **Hardening** significa
ridurre metodicamente tutto questo — la superficie d'attacco, i privilegi, le strade per muoversi dentro
il sistema — fino a lasciare attivo solo ciò che serve, con il minimo dei permessi, sotto osservazione.

Questa serie è deliberatamente **pratica**. Niente elenchi di "best practice" senza contesto: ogni
capitolo spiega *perché* un controllo conta e poi mostra i **comandi e le configurazioni reali** per
applicarlo e verificarlo. Gli esempi sono pensati per distribuzioni mainstream (Debian/Ubuntu e
RHEL/Fedora); dove divergono, lo segnalo.

## Come leggerla

L'ordine costruisce dal basso: prima il modello (utenti, permessi), poi gli accessi (sudo, SSH, PAM),
poi i servizi e la rete, la manutenzione, i controlli avanzati (capabilities, SELinux/AppArmor), il
monitoraggio (auditd, journald, AIDE) e infine isolamento, kernel e automazione.

## I capitoli

**Fondamenta**
1. [Il modello di sicurezza di Linux]({{< relref "post/modello-sicurezza-linux" >}})
2. [Utenti, gruppi e account]({{< relref "post/utenti-gruppi-account" >}})
3. [I permessi dei file]({{< relref "post/permessi-dei-file" >}})
4. [Permessi speciali: SUID, SGID, sticky]({{< relref "post/permessi-speciali-suid-sgid" >}})

**Accessi**
5. [sudo e l'escalation controllata]({{< relref "post/sudo-ed-escalation" >}})
6. [Hardening di SSH]({{< relref "post/hardening-ssh" >}})
7. [Autenticazione e PAM]({{< relref "post/autenticazione-pam" >}})

**Servizi e processi**
8. [systemd: servizi e unit]({{< relref "post/systemd-servizi-e-unit" >}})
9. [Sandboxing dei servizi con systemd]({{< relref "post/systemd-hardening-servizi" >}})
10. [Processi, risorse e cgroups]({{< relref "post/processi-e-risorse-cgroups" >}})

**Rete**
11. [Firewall con nftables]({{< relref "post/firewall-nftables" >}})
12. [Ridurre la superficie di rete]({{< relref "post/superficie-di-rete-servizi" >}})

**Manutenzione e boot**
13. [Aggiornamenti e gestione pacchetti]({{< relref "post/aggiornamenti-e-pacchetti" >}})
14. [Boot sicuro e GRUB]({{< relref "post/boot-e-secure-boot" >}})
15. [Cifratura dei dischi con LUKS]({{< relref "post/cifratura-dischi-luks" >}})

**Controlli avanzati**
16. [Capabilities: oltre il root tutto-o-niente]({{< relref "post/capabilities-linux" >}})
17. [SELinux]({{< relref "post/selinux" >}})
18. [AppArmor]({{< relref "post/apparmor" >}})

**Monitoraggio**
19. [Auditing con auditd]({{< relref "post/auditd" >}})
20. [Logging e journald]({{< relref "post/logging-journald" >}})
21. [Integrità dei file con AIDE]({{< relref "post/integrita-file-aide" >}})

**Isolamento, kernel, automazione**
22. [Namespaces e isolamento]({{< relref "post/namespaces-e-isolamento" >}})
23. [Kernel hardening con sysctl]({{< relref "post/kernel-hardening-sysctl" >}})
24. [CIS Benchmark e automazione]({{< relref "post/cis-benchmark-e-automazione" >}})

## Il filo conduttore

Tre principi attraversano ogni capitolo: **privilegio minimo** (dare il meno possibile, a persone e
processi), **superficie minima** (ciò che non esiste non si attacca), e **visibilità** (un sistema che
non osservi è un sistema di cui non sai nulla). Si parte dal modello che rende tutto il resto
comprensibile: [come Linux decide chi può fare cosa]({{< relref "post/modello-sicurezza-linux" >}}).
