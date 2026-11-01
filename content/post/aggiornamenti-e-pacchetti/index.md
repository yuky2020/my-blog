---
title: "Aggiornamenti e gestione pacchetti"
description: "Le vulnerabilità note non corrette sono la causa più banale e più frequente di compromissione. Tenere il sistema aggiornato — idealmente in automatico per le patch di sicurezza — e fidarsi solo di repository firmati è manutenzione di sicurezza di base. unattended-upgrades, dnf-automatic, la verifica GPG dei pacchetti e perché le patch tempestive valgono più di molti controlli sofisticati."
slug: "aggiornamenti-e-pacchetti"
date: 2026-04-07T09:00:00+02:00
lastmod: 2026-04-07T09:00:00+02:00
categories:
    - Security
    - DevOps
tags:
    - Linux
    - Hardening
    - Patch Management
keywords:
    - unattended-upgrades
    - dnf-automatic
    - patch management
    - repository firmati
image: "cover.png"
toc: true
links:
  - title: "Debian — UnattendedUpgrades"
    description: "Installazione automatica degli aggiornamenti di sicurezza su Debian/Ubuntu."
    website: https://wiki.debian.org/UnattendedUpgrades
  - title: "Fedora — dnf-automatic"
    description: "Aggiornamenti automatici sulle distribuzioni basate su dnf."
    website: https://dnf.readthedocs.io/en/latest/automatic.html
---

## Perché conta

Molte compromissioni non sfruttano exploit zero-day geniali: sfruttano vulnerabilità **note, con patch
già disponibile**, su sistemi che non sono stati aggiornati. È l'attacco più banale e più efficace,
perché gli exploit per le CVE pubbliche circolano e gli scanner automatici cercano proprio versioni
vecchie. Tenere il sistema aggiornato è, da solo, più efficace di molti controlli sofisticati — ed è
spesso trascurato perché "noioso". L'obiettivo: rendere l'aggiornamento di sicurezza *automatico e
affidabile*.

## Patch di sicurezza automatiche

**Debian/Ubuntu** — `unattended-upgrades` installa da solo gli aggiornamenti di sicurezza:

```bash
apt install unattended-upgrades
dpkg-reconfigure -plow unattended-upgrades   # abilita
```

```text {hl_lines=[2,5]}
# /etc/apt/apt.conf.d/50unattended-upgrades
Unattended-Upgrade::Origins-Pattern {
    "origin=Debian,codename=${distro_codename},label=Debian-Security";
};
Unattended-Upgrade::Automatic-Reboot "false";   # true solo se sei pronto al riavvio notturno
Unattended-Upgrade::Automatic-Reboot-Time "03:30";
```

**Fedora/RHEL** — `dnf-automatic`:

```text {hl_lines=[2,3]}
# /etc/dnf/automatic.conf
[commands]
upgrade_type = security      # solo aggiornamenti di sicurezza
apply_updates = yes          # applicali davvero (non solo scarica)
```
```bash
systemctl enable --now dnf-automatic.timer
```

## La fiducia nei repository: GPG

Un aggiornamento è sicuro solo se viene da una fonte fidata. I gestori di pacchetti verificano la
**firma GPG** di repository e pacchetti: se la firma non torna, il pacchetto viene rifiutato. Questo
protegge da un mirror compromesso o da un man-in-the-middle che prova a servirti pacchetti manomessi.

```bash
apt-key list 2>/dev/null; ls /etc/apt/trusted.gpg.d/   # chiavi fidate (Debian/Ubuntu)
rpm -q gpg-pubkey --qf '%{SUMMARY}\n'                  # chiavi fidate (RHEL/Fedora)
```

La regola: **non aggiungere repository di terze parti senza la loro chiave GPG**, e diffida di
istruzioni che disattivano la verifica delle firme (`[trusted=yes]`, `gpgcheck=0`) — stai dicendo al
sistema di fidarsi ciecamente.

## Sapere cosa è vulnerabile

```bash
# Debian/Ubuntu: aggiornamenti di sicurezza pendenti
apt list --upgradable 2>/dev/null | grep -i security
# RHEL/Fedora: elenco delle CVE con patch disponibile
dnf updateinfo list security
# quali pacchetti sono installati e da quando
dpkg -l | wc -l ; rpm -qa | wc -l
```

## Ridurre anche ciò che è installato

Meno software installato = meno vulnerabilità possibili = meno da aggiornare. Rimuovere pacchetti che
non servono (compilatori su un server di produzione, client vari, tool di debug) è hardening tanto
quanto aggiornare.

```bash
apt autoremove --purge       # rimuove dipendenze orfane
# rivedi i pacchetti installati manualmente e togli ciò che non usi
```

## Conclusione

Patch di sicurezza automatiche, repository firmati e verifica GPG, e meno software installato: è la
manutenzione che chiude la via di compromissione più comune in assoluto. Gli aggiornamenti proteggono
il sistema in esecuzione; ma la sicurezza inizia ancora prima, all'avvio — chi controlla il boot
controlla la macchina. È il [boot sicuro e GRUB]({{< relref "post/boot-e-secure-boot" >}}), prossimo
capitolo.
