---
title: "Capabilities: oltre il root tutto-o-niente"
description: "Storicamente root poteva tutto e un utente normale quasi niente: nessuna via di mezzo. Le capabilities spezzano i poteri di root in tanti permessi distinti, così un programma può ottenere solo quello che gli serve — aprire una porta bassa, per esempio — senza essere root. Come leggerle, assegnarle ai file al posto del SUID e azzerarle nei servizi."
slug: "capabilities-linux"
date: 2026-04-28T09:00:00+02:00
lastmod: 2026-04-28T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Capabilities
keywords:
    - linux capabilities
    - setcap getcap
    - CAP_NET_BIND_SERVICE
    - privilegi granulari
image: "cover.png"
toc: true
links:
  - title: "man 7 capabilities"
    description: "L'elenco completo delle capabilities e il loro significato."
    website: https://man7.org/linux/man-pages/man7/capabilities.7.html
  - title: "man 8 setcap"
    description: "Assegnare capabilities a un eseguibile."
    website: https://man7.org/linux/man-pages/man8/setcap.8.html
---

## Perché conta

Nel modello classico c'erano solo due stati: root (può tutto) o non-root (quasi niente). Questo creava
un problema: un programma che aveva bisogno di *un solo* potere di root — per esempio aprire la porta
80, riservata a root — doveva girare *interamente* da root, con tutti i suoi poteri. Le **capabilities**
spezzano l'onnipotenza di root in ~40 permessi distinti, così si può concedere *esattamente* quello che
serve. È il [privilegio minimo]({{< relref "post/principio-minimo-privilegio" >}}) applicato
ai poteri del kernel.

## Alcune capabilities chiave

```text {hl_lines=[2,5]}
CAP_NET_BIND_SERVICE  → aprire porte sotto la 1024 (es. 80, 443) senza essere root
CAP_NET_ADMIN         → configurare la rete (interfacce, firewall)
CAP_SYS_ADMIN         → "il nuovo root": enorme e pericolosa, da evitare come la peste
CAP_DAC_OVERRIDE      → ignorare i permessi dei file (quasi root sui file)
CAP_CHOWN             → cambiare proprietario dei file
CAP_SYS_PTRACE        → ispezionare/alterare altri processi (debug, ma anche attacco)
```

`CAP_SYS_ADMIN` è tristemente nota come "il nuovo root": concede talmente tanto che darla equivale quasi
a dare root. Diffidane.

## Leggere e assegnare capabilities sui file

Si possono attaccare a un eseguibile (**file capabilities**): il programma le ottiene all'esecuzione,
senza essere SUID-root. È l'alternativa moderna e più sicura al [SUID]({{< relref
"post/permessi-speciali-suid-sgid" >}}).

```bash
getcap -r /usr/bin 2>/dev/null         # elenca i binari con capabilities assegnate
# es: /usr/bin/ping = cap_net_raw+ep   ← ping non è più SUID-root, ha solo questa capability

# dare a un'app il permesso di aprire la porta 80, senza renderla root né SUID
setcap 'cap_net_bind_service=+ep' /usr/local/bin/myapp
getcap /usr/local/bin/myapp            # verifica
setcap -r /usr/local/bin/myapp         # rimuovere tutte le capabilities
```

Il `+ep` significa *effective* + *permitted*: la capability è attiva all'avvio. Perché questo è meglio
del SUID? Perché `myapp` ottiene *solo* il potere di aprire porte basse, non l'intero root: se viene
compromesso, l'attaccante non eredita l'onnipotenza.

## Azzerare le capabilities nei servizi

Nel [sandboxing systemd]({{< relref "post/systemd-hardening-servizi" >}}) abbiamo visto
`CapabilityBoundingSet=`. Qui si chiude il cerchio: si parte da zero e si concede solo lo stretto
necessario.

```text {hl_lines=[2,3]}
# nella unit del servizio
CapabilityBoundingSet=CAP_NET_BIND_SERVICE   # il servizio può SOLO aprire porte basse
AmbientCapabilities=CAP_NET_BIND_SERVICE     # e le riceve all'avvio, senza essere root
# tutto il resto dei poteri di root è precluso, anche se gira come root
```

Così un web server può legarsi alla 443 pur avendo azzerato ogni altro potere: compromesso, non può
caricare moduli kernel, non può ignorare i permessi dei file, non può amministrare la rete.

## Verificare le capabilities di un processo

```bash
grep Cap /proc/<pid>/status            # bitmask delle capabilities del processo
getpcaps <pid>                         # versione leggibile
capsh --decode=0000000000003000        # decodifica una bitmask in nomi
```

## Conclusione

Le capabilities trasformano il root tutto-o-niente in un insieme di permessi concedibili uno a uno:
un binario ottiene solo `CAP_NET_BIND_SERVICE` invece di tutto root, un servizio azzera il bounding set
e riceve solo ciò che gli serve. È privilegio minimo a livello di kernel. Ma capabilities e permessi
restano *discrezionali*; per una politica che nemmeno root o il proprietario possano aggirare serve il
controllo d'accesso **obbligatorio**: [SELinux]({{< relref "post/selinux" >}}), prossimo capitolo.
