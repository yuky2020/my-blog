---
title: "Sandboxing dei servizi con systemd"
description: "systemd può rinchiudere un servizio in una gabbia robusta con poche righe nella unit: filesystem in sola lettura, niente nuovi privilegi, home nascoste, capabilities azzerate, syscall filtrate. È la difesa in profondità più sottovalutata di Linux: se il servizio viene compromesso, l'attaccante trova un recinto, non il sistema. Le direttive che contano, con analyze-security."
slug: "systemd-hardening-servizi"
date: 2026-03-10T09:00:00+01:00
lastmod: 2026-03-10T09:00:00+01:00
categories:
    - Security
    - DevOps
tags:
    - Linux
    - Hardening
    - systemd
keywords:
    - systemd hardening
    - ProtectSystem
    - NoNewPrivileges
    - seccomp
image: "cover.png"
toc: true
links:
  - title: "man 5 systemd.exec"
    description: "Tutte le direttive di sandboxing per i servizi."
    website: https://man7.org/linux/man-pages/man5/systemd.exec.5.html
  - title: "systemd — Security features"
    description: "Panoramica delle funzioni di isolamento dei servizi."
    website: https://0pointer.net/blog/dynamic-users-with-systemd.html
---

## Perché conta

Un servizio non-root compromesso è meno grave di uno root — ma può comunque leggere dati, scrivere
dove non dovrebbe, aprire connessioni, tentare escalation. La difesa in profondità dice: assumi che il
servizio *verrà* bucato, e limita cosa potrà fare allora. systemd offre per questo uno dei sandbox più
semplici da attivare in tutto Linux: **poche righe nella unit** mettono il processo in un recinto di
filesystem, privilegi e syscall. Eppure è tra le funzioni meno usate. Rimediamo.

## Misurare prima: systemd-analyze security

systemd ti dà un voto di esposizione per ogni servizio. Parti da qui per sapere dove intervenire.

```bash
systemd-analyze security                      # classifica TUTTI i servizi per esposizione
systemd-analyze security nginx.service        # dettaglio: quali protezioni mancano
# Overall exposure level: 8.6 UNSAFE  →  l'obiettivo è portarlo verso "OK/GOOD"
```

## Le direttive che contano

Si aggiungono nel blocco `[Service]`, idealmente via drop-in (`systemctl edit myapp.service`) così non
tocchi la unit originale.

```text {hl_lines=[3,4,5,8,11]}
# systemctl edit myapp.service  → crea override.conf
[Service]
NoNewPrivileges=true          # il processo e i figli NON possono acquisire nuovi privilegi (blocca SUID/escalation)
ProtectSystem=strict          # tutto il filesystem in sola lettura...
ReadWritePaths=/var/lib/myapp # ...tranne i percorsi che dichiari esplicitamente
ProtectHome=true              # /home, /root, /run/user invisibili al servizio
PrivateTmp=true               # /tmp privato e separato (niente attacchi via file temporanei condivisi)
PrivateDevices=true           # niente accesso ai device fisici
CapabilityBoundingSet=        # azzera tutte le capabilities (vedi cap. 16)
RestrictAddressFamilies=AF_INET AF_INET6   # solo socket di rete IP, niente AF_NETLINK ecc.
SystemCallFilter=@system-service   # consenti solo le syscall tipiche di un servizio (seccomp)
```

Ciascuna chiude una categoria di abusi: `NoNewPrivileges` spegne il trucco del SUID; `ProtectSystem=strict`
rende impossibile scrivere binari di sistema; `PrivateTmp` isola i file temporanei; `SystemCallFilter`
blocca intere famiglie di syscall (es. quelle per caricare moduli kernel) che un servizio normale non
usa mai.

## Un esempio completo

```text {hl_lines=[8,9,10,11,12,13]}
# /etc/systemd/system/myapp.service
[Service]
ExecStart=/usr/local/bin/myapp
User=myapp
Group=myapp
# --- sandbox ---
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
PrivateDevices=true
ReadWritePaths=/var/lib/myapp
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX
CapabilityBoundingSet=
SystemCallFilter=@system-service
SystemCallArchitectures=native
LockPersonality=true
MemoryDenyWriteExecute=true   # niente memoria contemporaneamente scrivibile ed eseguibile (ostacola exploit)
```

`DynamicUser=true` è un bonus: fa girare il servizio sotto un utente *effimero* creato al volo e distrutto
allo stop — zero account da gestire, isolamento massimo (usalo solo con servizi che non hanno bisogno di
un UID stabile).

## Applicare e verificare

```bash
systemctl daemon-reload
systemctl restart myapp.service
systemd-analyze security myapp.service     # il voto deve essere migliorato
journalctl -u myapp -e                      # controlla che non si sia rotto nulla
```

Il rischio pratico: una direttiva troppo stretta impedisce al servizio di funzionare (es. non può
scrivere dove gli serve). Si procede per gradi, guardando i log: se il servizio si lamenta di un
percorso, lo aggiungi a `ReadWritePaths`; se di una syscall negata, allenti il filtro.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se il servizio gira già sotto un utente non privilegiato dedicato, non è già abbastanza isolato? Che cosa aggiunge davvero tutto questo sandboxing, a parte il rischio di romperlo?</summary>
<p>Girare sotto un utente dedicato è il primo strato e il più importante, ma protegge solo lungo un asse —
i permessi DAC — e lascia aperti molti altri che il sandboxing chiude. Pensa a cosa può fare un servizio
compromesso che gira come utente <code>myapp</code> non privilegiato, senza sandbox: può leggere ogni
file leggibile da "altri" sul sistema (e sono tanti: /etc/passwd, configurazioni, log, codice di altre
app), può scrivere in /tmp file che altri processi leggono (attacchi via file temporanei), può tentare di
sfruttare un binario SUID per salire a root, può aprire connessioni di rete verso l'esterno per
esfiltrare o scaricare un secondo stadio, può leggere le home degli utenti se i permessi lo consentono,
può provare syscall esotiche per sfruttare vulnerabilità del kernel. L'utente dedicato non ferma nulla di
tutto questo, perché sono tutte azioni che un utente normale <em>può</em> fare. Il sandboxing di systemd
chiude ciascuna di queste strade: <code>ProtectSystem=strict</code> + <code>ReadWritePaths</code> riduce
il filesystem a sola lettura tranne la sua cartella, quindi non scrive da nessun'altra parte;
<code>ProtectHome</code> gli nasconde le home; <code>PrivateTmp</code> gli dà un /tmp separato, neutralizzando
gli attacchi via temporanei; <code>NoNewPrivileges</code> rende inutile qualsiasi SUID, chiudendo la via
di escalation; <code>SystemCallFilter</code> gli toglie le syscall che non userebbe mai, riducendo la
superficie del kernel sfruttabile; <code>RestrictAddressFamilies</code> limita i tipi di socket. Ogni
direttiva trasforma "cosa potrebbe fare un attaccante da dentro quel servizio" in un recinto molto più
piccolo. Sul rischio di romperlo: è reale ma gestibile — si procede per gradi guardando i log, e il voto
di <code>systemd-analyze security</code> ti guida. Il costo è qualche minuto di tuning una volta; il
beneficio è che una compromissione del servizio resta confinata invece di diventare un piede dentro il
sistema. Questo è esattamente il senso della difesa in profondità: non un muro solo, ma tanti recinti.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Con una manciata di direttive — `NoNewPrivileges`, `ProtectSystem`, `PrivateTmp`, capabilities azzerate,
filtro seccomp — systemd mette ogni servizio in una gabbia, e `systemd-analyze security` misura i
progressi. È difesa in profondità quasi gratuita. I servizi, però, sono anche processi che consumano
risorse: la prossima linea di difesa riguarda [processi, risorse e
cgroups]({{< relref "post/processi-e-risorse-cgroups" >}}).
