---
title: "Ridurre la superficie di rete"
description: "Un servizio legato a 0.0.0.0 è esposto a tutta la rete; lo stesso servizio su 127.0.0.1 è raggiungibile solo in locale. Scoprire cosa ascolta e dove, legare i servizi interni al solo loopback e capire la differenza è uno degli interventi più efficaci e trascurati. ss, binding degli indirizzi e il senso di 'meno porte aperte'."
slug: "superficie-di-rete-servizi"
date: 2026-03-31T09:00:00+02:00
lastmod: 2026-03-31T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Rete
keywords:
    - ss comando
    - listening ports
    - bind 127.0.0.1
    - superficie di rete
image: "cover.png"
toc: true
links:
  - title: "man 8 ss"
    description: "Lo strumento moderno per ispezionare socket e porte in ascolto."
    website: https://man7.org/linux/man-pages/man8/ss.8.html
  - title: "man 7 socket"
    description: "Concetti di socket, indirizzi e binding in Linux."
    website: https://man7.org/linux/man-pages/man7/socket.7.html
---

## Perché conta

Il [firewall]({{< relref "post/firewall-nftables" >}}) blocca ciò che non vuoi raggiungibile, ma la
difesa migliore è che il servizio non ascolti affatto dove non deve. Un database, una cache, un pannello
di amministrazione interni spesso non hanno alcun bisogno di essere raggiungibili dalla rete: devono
parlare solo con processi sullo stesso host. La differenza tra legarli a `0.0.0.0` (tutte le interfacce)
o a `127.0.0.1` (solo loopback) è enorme — e si risolve con una riga di configurazione.

## Vedere cosa ascolta

`ss` (il moderno sostituto di `netstat`) mostra i socket in ascolto, su quale indirizzo e di quale
processo.

```bash
ss -tulpn
# Netid  State   Local Address:Port    Process
# tcp    LISTEN  0.0.0.0:5432          postgres   ← ESPOSTO a tutta la rete!
# tcp    LISTEN  127.0.0.1:6379        redis      ← solo locale, bene
# tcp    LISTEN  *:443                 nginx      ← pubblico: ok se è un web server
```

La colonna da leggere è **Local Address**:

```text {hl_lines=[2,3]}
0.0.0.0  o  *    → ascolta su TUTTE le interfacce = raggiungibile da fuori
127.0.0.1 / ::1  → ascolta solo su loopback = SOLO processi locali
10.0.0.5         → ascolta su una specifica interfaccia (es. rete interna)
```

Un `0.0.0.0` su un servizio che dovrebbe essere interno è il bersaglio da correggere.

## Legare al loopback

La correzione sta nella configurazione del servizio. Esempi tipici:

```text {hl_lines=[2,5,8]}
# PostgreSQL — postgresql.conf
listen_addresses = 'localhost'      # invece di '*'

# Redis — redis.conf
bind 127.0.0.1 ::1                   # invece di 0.0.0.0

# un'app che espone una porta di gestione
# avviala con --host 127.0.0.1 invece di --host 0.0.0.0
```

Dopo il riavvio del servizio, `ss -tulpn` deve mostrare `127.0.0.1` al posto di `0.0.0.0`. Se un
processo esterno deve comunque raggiungerlo, la via corretta non è aprirlo al mondo ma esporlo tramite
un reverse proxy o un tunnel, controllando l'accesso a monte.

## Il ragionamento completo

```text {hl_lines=[1,2,3]}
Per ogni porta in ascolto, in ordine:
  1. serve il servizio?           NO → spegnilo (cap. 8)
  2. deve essere in rete?         NO → bind su 127.0.0.1
  3. deve essere pubblico?        NO → bind su interfaccia interna + firewall per sorgente
  4. è pubblico davvero?          SÌ → firewall lo consente + servizio indurito
```

Questo intreccia i tre strumenti: spegnere (systemd), legare bene (binding), filtrare (nftables). Nessuno
dei tre, da solo, copre tutto; insieme riducono la superficie di rete al minimo reale.

## Verifica dall'esterno

Il modo più onesto di sapere cosa è esposto è guardare *da fuori*, come farebbe un attaccante:

```bash
# da un ALTRO host (con autorizzazione!): quali porte vede dall'esterno?
nmap -Pn -p- nome-o-ip-del-server
```

Ciò che `nmap` vede aperto dall'esterno è la tua vera superficie di rete pubblica. Idealmente coincide
con la manciata di porte che *intendi* pubblicare, e nient'altro.

## Conclusione

Scoprire cosa ascolta con `ss`, legare al loopback tutto ciò che è interno, e verificare dall'esterno:
la superficie di rete si riduce al minimo con poche modifiche di binding. Un sistema sicuro va però
anche *mantenuto* sicuro nel tempo: il software invecchia e le vulnerabilità emergono. La manutenzione è
il prossimo tema — [aggiornamenti e gestione pacchetti]({{< relref "post/aggiornamenti-e-pacchetti" >}}).
