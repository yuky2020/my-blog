---
title: "Zero Trust in pratica: la serie"
description: "Una serie in 20 capitoli per capire e costruire lo Zero Trust davvero: dai cinque principi NIST all'identità come perimetro, ZTNA, microsegmentazione, mTLS, policy as code e migrazione. Mappa e ordine di lettura."
slug: "zero-trust-la-serie"
date: 2026-05-12T09:00:00+02:00
lastmod: 2026-05-12T09:00:00+02:00
weight: 2
categories:
    - Security
    - Networking
tags:
    - Zero Trust
    - Network Security
keywords:
    - Zero Trust
    - ZTA
    - serie Zero Trust
    - NIST 800-207
image: "cover.png"
toc: true
links:
  - title: "NIST SP 800-207 — Zero Trust Architecture"
    description: Il documento di riferimento che definisce i principi dello Zero Trust.
    website: https://csrc.nist.gov/pubs/sp/800/207/final
---

## Perché questa serie

"Zero Trust" è diventato un termine di marketing: ogni prodotto lo promette, pochi lo spiegano. Ma
sotto il rumore c'è un cambiamento di paradigma concreto e verificabile — smettere di fidarsi della
rete e iniziare a verificare ogni accesso, sempre, in base all'identità e al contesto. Questa serie
in 20 capitoli smonta il concetto nei suoi pezzi reali e mostra come si costruisce, con esempi di
configurazione e laboratori riproducibili. È il seguito naturale del post introduttivo
[Zero Trust Architecture]({{< relref "post/zero-trust-architecture" >}}).

## Il filo del discorso

Lo Zero Trust non è un prodotto che si compra, ma un'architettura che si costruisce per strati. La
serie segue questo ordine:

```mermaid
flowchart TD
    P["Principi<br/>(cap. 01-02)"] --> I["Identità<br/>(cap. 03-04)"]
    I --> M["Motore delle policy<br/>(cap. 05)"]
    M --> R["Rete e accesso<br/>(cap. 06-08)"]
    R --> D["Dispositivi e privilegi<br/>(cap. 09-10)"]
    D --> W["Identità dei workload<br/>(cap. 11-14)"]
    W --> C["Verifica continua<br/>(cap. 15-16)"]
    C --> E["Estensioni: cloud, dati<br/>(cap. 17-18)"]
    E --> MIG["Migrazione<br/>(cap. 19)"]
    style P fill:#fde2e4,stroke:#e63946
```

## I capitoli

**Fondamenti**
- 01 — I cinque principi dello Zero Trust (NIST 800-207)
- 02 — Oltre il perimetro: perché il modello castello-e-fossato non basta più

**Identità**
- 03 — L'identità è il nuovo perimetro
- 04 — MFA resistente al phishing (FIDO2/WebAuthn)
- 05 — PDP e PEP: il motore che decide e applica le policy

**Rete e accesso**
- 06 — Microsegmentazione nello Zero Trust
- 07 — ZTNA: l'accesso oltre la VPN
- 08 — SASE e Zero Trust

**Dispositivi e privilegi**
- 09 — Device trust e postura degli endpoint
- 10 — Least privilege e accesso Just-in-Time

**Identità dei workload**
- 11 — L'identità dei workload con mTLS
- 12 — SPIFFE e SPIRE
- 13 — Service mesh e Zero Trust
- 14 — Policy as code con OPA

**Verifica e osservabilità**
- 15 — Verifica continua e accesso adattivo al rischio
- 16 — Telemetria e analytics nello Zero Trust

**Estensioni e percorso**
- 17 — Zero Trust nel cloud
- 18 — Zero Trust per i dati
- 19 — Migrare a Zero Trust: maturità, roadmap, errori comuni

## Per chi è

Per chi progetta o amministra reti e sistemi e vuole capire lo Zero Trust oltre lo slogan: cosa
significa in termini di identità, policy, segmentazione e verifica, e quali strumenti concreti lo
realizzano. Ogni capitolo è autonomo ma costruisce sui precedenti; la lettura in ordine dà il quadro
completo.

## Convenzioni

Ogni capitolo ha una sezione **Perché conta**, lo sviluppo con diagrammi ed esempi, un **Lab**
riproducibile e una domanda scomoda in fondo. Gli esempi privilegiano strumenti open source
(FreeRADIUS, OPA, SPIRE, Istio/Linkerd, Open vSwitch) e ambienti di laboratorio containerlab.

## Conclusione

Lo Zero Trust si capisce costruendolo. Questa serie parte dai principi e arriva alla migrazione,
pezzo per pezzo, senza slogan. Si comincia dal prossimo capitolo: i cinque principi che definiscono
cosa è davvero Zero Trust — e cosa non lo è.
