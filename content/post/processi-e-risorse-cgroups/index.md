---
title: "Processi, risorse e cgroups"
description: "Un processo impazzito o malevolo che divora CPU, memoria o process table può mettere in ginocchio un sistema: è un denial of service dall'interno. Leggere i processi via ps e /proc, imporre limiti con cgroups e le direttive systemd, difendersi dalle fork bomb. Come tenere sotto controllo chi consuma cosa."
slug: "processi-e-risorse-cgroups"
date: 2026-03-17T09:00:00+01:00
lastmod: 2026-03-17T09:00:00+01:00
categories:
    - Security
    - DevOps
tags:
    - Linux
    - Hardening
    - cgroups
keywords:
    - cgroups
    - limiti risorse
    - fork bomb
    - process management
image: "cover.png"
toc: true
links:
  - title: "man 7 cgroups"
    description: "Il meccanismo del kernel per limitare e isolare le risorse dei processi."
    website: https://man7.org/linux/man-pages/man7/cgroups.7.html
  - title: "man 5 systemd.resource-control"
    description: "Direttive systemd per i limiti di CPU, memoria e processi."
    website: https://man7.org/linux/man-pages/man5/systemd.resource-control.5.html
---

## Perché conta

Non tutte le minacce arrivano da fuori. Un processo che apre file senza sosta, un servizio con una
memory leak, una fork bomb (accidentale o dolosa) possono esaurire CPU, RAM o la process table e
rendere il sistema inutilizzabile — un **denial of service dall'interno**. L'hardening non è solo
chiudere porte: è anche garantire che nessun singolo processo o utente possa affamare gli altri. Lo
strumento del kernel per questo sono i **cgroups**.

## Leggere i processi

```bash
ps -eo pid,user,%cpu,%mem,rss,comm --sort=-%mem | head   # chi consuma più RAM
ps -eo pid,user,nlwp,comm --sort=-nlwp | head            # chi ha più thread
top -o %MEM                                              # vista live, ordinata per memoria
# /proc è la verità: ogni processo è una cartella
cat /proc/<pid>/status | grep -E 'VmRSS|Threads|Uid'
ls -l /proc/<pid>/fd | wc -l                             # quanti file aperti
```

`/proc` è la finestra del kernel sui processi: lì leggi memoria reale, thread, file descriptor, limiti
e persino la riga di comando (`/proc/<pid>/cmdline`).

## cgroups: i limiti del kernel

I **control group** (v2 sui sistemi moderni) permettono al kernel di imporre tetti a CPU, memoria,
I/O e numero di processi per un gruppo. systemd li usa dietro le quinte e li espone come direttive: è
il modo più semplice di applicarli a un servizio.

```text {hl_lines=[3,4,5,6]}
# systemctl edit myapp.service
[Service]
MemoryMax=512M            # oltre, il processo viene killato (OOM) prima di affamare il sistema
MemoryHigh=400M           # soglia "morbida": il kernel rallenta il processo
CPUQuota=50%              # al massimo mezza CPU
TasksMax=100              # al massimo 100 processi/thread → tappo alle fork bomb
```

`TasksMax` è la difesa diretta contro le fork bomb: un servizio che tenta di creare migliaia di processi
sbatte contro il tetto invece di saturare la process table di tutto il sistema.

## Verificare i limiti in azione

```bash
systemctl show myapp.service -p MemoryMax -p TasksMax -p CPUQuota
systemd-cgtop                      # vista live del consumo PER cgroup/servizio
cat /sys/fs/cgroup/system.slice/myapp.service/memory.current   # memoria usata ora
```

## Limiti per utente, non solo per servizio

Per gli utenti interattivi, i limiti si impostano via [pam_limits]({{< relref
"post/autenticazione-pam" >}}) (`/etc/security/limits.conf`) — tetti a processi e file aperti per
account — oppure via le slice di systemd (`user-<UID>.slice`).

```text {hl_lines=[2]}
# /etc/security/limits.conf — tappo classico anti fork bomb per utente
*    hard    nproc    2048
```

## La difesa stratificata

```text {hl_lines=[1,2,3]}
- limiti per-servizio  → MemoryMax/TasksMax/CPUQuota nelle unit (il più preciso)
- limiti per-utente    → limits.conf / user slice (copre le sessioni interattive)
- monitoraggio         → systemd-cgtop + alert quando un cgroup satura (vedi cap. logging)
```

## Conclusione

Leggere i processi via `ps` e `/proc`, e imporre tetti con cgroups (`MemoryMax`, `TasksMax`, `CPUQuota`)
impedisce che un singolo processo — buggato o malevolo — affami il sistema. Finora abbiamo lavorato
"dentro" la macchina; ora usciamo verso la rete, dove si decide cosa il mondo può raggiungere: il
[firewall con nftables]({{< relref "post/firewall-nftables" >}}), prossimo capitolo.
