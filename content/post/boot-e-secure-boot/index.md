---
title: "Boot sicuro e GRUB"
description: "Chi controlla il processo di avvio controlla la macchina: con accesso fisico (o alla console di una VM) si può entrare in modalità single-user, modificare i parametri del kernel e scavalcare le difese. Password su GRUB, Secure Boot e la catena di fiducia dall'UEFI al kernel. Fin dove arriva questa protezione e fin dove no."
slug: "boot-e-secure-boot"
date: 2026-04-14T09:00:00+02:00
lastmod: 2026-04-14T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Boot
keywords:
    - secure boot
    - grub password
    - single user mode
    - catena di fiducia
image: "cover.png"
toc: true
links:
  - title: "GRUB Manual — Security"
    description: "Protezione delle voci di menu e dell'editing di GRUB con password."
    website: https://www.gnu.org/software/grub/manual/grub/grub.html#Security
  - title: "Debian — SecureBoot"
    description: "Come funziona Secure Boot con Linux e la catena di firme."
    website: https://wiki.debian.org/SecureBoot
---

## Perché conta

Tutte le difese viste finora presuppongono un sistema *già avviato* e integro. Ma il processo di avvio
è esso stesso un bersaglio: chi ha accesso alla console — fisicamente, o alla console di una VM/IPMI —
può interrompere GRUB, aggiungere `init=/bin/bash` ai parametri del kernel e ottenere una shell di root
*senza password*, scavalcando login, SSH e PAM. La sicurezza del boot chiude questa porta e stabilisce
una **catena di fiducia** dal firmware al kernel.

## La minaccia: la shell di root al boot

Dal menu di GRUB, premendo `e` si editano i parametri di avvio. Aggiungere `init=/bin/bash` o
`systemd.unit=rescue.target` può dare una shell privilegiata prima che partano le protezioni. È il
motivo per cui, con accesso alla console, un sistema non protetto al boot è già perso.

```text {hl_lines=[2]}
# ciò che un attaccante aggiunge alla riga 'linux ...' nel menu GRUB:
init=/bin/bash          # il kernel avvia una shell invece di systemd → root senza login
```

## Password su GRUB

Proteggere l'*editing* delle voci e la modalità rescue con una password impedisce questo scavalcamento.

```bash
grub-mkpasswd-pbkdf2        # genera un hash: grub.pbkdf2.sha512.10000.XXXX...
```

```text {hl_lines=[2,3,5]}
# /etc/grub.d/40_custom
set superusers="admin"
password_pbkdf2 admin grub.pbkdf2.sha512.10000.XXXX...
# per lasciare l'avvio normale senza password ma proteggere l'EDITING:
#   aggiungi --unrestricted alle voci di menu generate
```
```bash
update-grub     # Debian/Ubuntu    (grub2-mkconfig -o /boot/grub2/grub.cfg su RHEL)
```

Il bilanciamento tipico: l'avvio normale non chiede password (il server riparte da solo dopo un
riavvio), ma *modificare* i parametri o entrare in rescue sì.

## Secure Boot: la catena di fiducia

**Secure Boot** (UEFI) verifica la firma crittografica di ogni anello della catena d'avvio: il firmware
verifica il bootloader (shim/GRUB), che verifica il kernel, che verifica i moduli. Se un componente non
è firmato da una chiave fidata, non parte. Protegge da **bootkit** e da un kernel/bootloader manomesso.

```bash
mokutil --sb-state            # Secure Boot enabled / disabled
bootctl status                # stato del boot UEFI e del firmware
```

Su Linux funziona tramite `shim` firmato da Microsoft (la cui chiave è nei firmware) che a sua volta
verifica il bootloader della distribuzione. Puoi anche iscrivere le *tue* chiavi (MOK) per firmare moduli
kernel custom.

## Fin dove arriva (e fin dove no)

```text {hl_lines=[1,4]}
Protegge: scavalcamento via console/GRUB, bootkit, kernel/bootloader manomessi
NON protegge da solo: dischi non cifrati estratti e letti su un'altra macchina
  → per quello serve la cifratura del disco (prossimo capitolo)
Richiede: accesso fisico/console protetto; su cloud/VM, dipende dalle protezioni del provider
```

Secure Boot verifica che il software che *parte* sia fidato, ma non protegge i **dati a riposo**: chi
stacca il disco e lo legge altrove scavalca tutto. È il naturale ponte al prossimo tema.

## Conclusione

Password su GRUB contro lo scavalcamento da console e Secure Boot per la catena di fiducia del software
d'avvio chiudono gli attacchi al boot — ma non proteggono i dati su un disco rimosso. Per quello serve
rendere illeggibile il disco stesso: la [cifratura con LUKS]({{< relref "post/cifratura-dischi-luks" >}}),
prossimo capitolo.
