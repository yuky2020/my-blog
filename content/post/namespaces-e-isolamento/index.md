---
title: "Namespaces e isolamento"
description: "I namespaces danno a un processo una vista privata del sistema — propri PID, rete, mount, utenti — ed è il meccanismo del kernel su cui poggiano i container. Capirli spiega come isolare un servizio e perché i container non sono magia. unshare, i tipi di namespace, i user namespace per far girare root 'finto', e systemd-nspawn come container leggero."
slug: "namespaces-e-isolamento"
date: 2026-06-09T09:00:00+02:00
lastmod: 2026-06-09T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Namespaces
keywords:
    - namespaces linux
    - unshare
    - user namespace
    - isolamento container
image: "cover.png"
toc: true
links:
  - title: "man 7 namespaces"
    description: "I tipi di namespace del kernel e il loro funzionamento."
    website: https://man7.org/linux/man-pages/man7/namespaces.7.html
  - title: "man 1 unshare"
    description: "Eseguire un processo in nuovi namespace."
    website: https://man7.org/linux/man-pages/man1/unshare.1.html
---

## Perché conta

Finora abbiamo confinato i processi con permessi, capabilities e MAC — ma condividendo la stessa vista
del sistema. I **namespaces** fanno un passo oltre: danno a un processo una vista *privata* di una
risorsa, come se avesse un sistema tutto suo. Un processo in un PID namespace vede solo i propri
processi; in un network namespace, una propria pila di rete. È il meccanismo con cui si costruiscono i
**container** — e capirlo demistifica cosa sono davvero (non macchine virtuali, ma processi isolati dal
kernel) e come usarli per isolare un servizio.

## I tipi di namespace

```text {hl_lines=[2,6,8]}
PID     → albero dei processi privato (dentro, il tuo processo è PID 1; non vede gli altri)
NET     → interfacce, routing, firewall propri
MNT     → tabella dei mount privata (propria vista del filesystem)
UTS     → hostname proprio
IPC     → memoria condivisa / code di messaggi separate
USER    → mappatura UID/GID propria (root "dentro" ≠ root "fuori") ← chiave per la sicurezza
CGROUP  → vista dei cgroup propria
TIME    → clock boot/monotonic propri
```

## Vederli e crearli a mano

```bash
lsns                               # elenca i namespace attivi e i processi che li usano
ls -l /proc/$$/ns/                 # i namespace del tuo shell corrente

# crea un processo con PID e mount namespace nuovi (serve privilegio o userns)
unshare --pid --mount --fork --mount-proc bash
ps aux        # dentro: vedi pochissimi processi — sei "solo" nel tuo PID namespace
```

## Il user namespace: root "finto"

Il più interessante per la sicurezza è il **user namespace**: permette a un utente non privilegiato di
avere i poteri di root *dentro* il namespace, mentre *fuori* resta un utente normale. Così un processo
può fare operazioni "da root" nel suo mondo isolato senza essere root sul sistema reale.

```bash
# root dentro, utente normale fuori: nessun privilegio reale acquisito
unshare --user --map-root-user bash
id        # dentro: uid=0(root) — ma è root solo in questo namespace
```

È il fondamento dei **container rootless** (Podman rootless): il container "crede" di avere root, ma sul
sistema ospite è confinato ai privilegi di un utente normale. Un'enorme riduzione del rischio rispetto
ai container che girano come root reale.

## systemd-nspawn: un container leggero

systemd include un gestore di container minimale, utile per isolare un servizio o testare in un
ambiente separato senza installare Docker/Podman.

```bash
# avvia una shell in un container basato su una directory (un "chroot potenziato")
systemd-nspawn -D /var/lib/machines/test
# con isolamento di rete e utenti:
systemd-nspawn -D /var/lib/machines/test --private-network -U
```

## Il legame con l'hardening

I namespaces sono il motivo per cui il [sandboxing di systemd]({{< relref
"post/systemd-hardening-servizi" >}}) funziona: direttive come `PrivateTmp`, `ProtectHome`,
`PrivateNetwork` creano namespace dedicati per il servizio. E spiegano perché un container **non è una
barriera di sicurezza perfetta**: condivide il kernel con l'host, quindi una vulnerabilità del kernel
può permettere la fuga. I container isolano, ma il confinamento forte richiede comunque capabilities
ridotte, seccomp e MAC — gli stessi strumenti dei capitoli precedenti, applicati dentro il container.

## Conclusione

I namespaces danno viste private di PID, rete, mount e utenti: sono il mattone dei container e del
sandboxing systemd, e i user namespace permettono root "finto" senza privilegi reali. Isolamento a
parte, resta un ultimo livello da indurire — quello più profondo, dove vivono i parametri del sistema
stesso: il [kernel hardening con sysctl]({{< relref "post/kernel-hardening-sysctl" >}}), prossimo
capitolo.
