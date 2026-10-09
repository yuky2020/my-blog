---
title: "DevSecOps in pratica: la serie"
description: "Trenta capitoli per portare la sicurezza dentro il ciclo di sviluppo, non dopo. Dalla cultura dello shift-left alla supply chain, dalla pipeline CI/CD al runtime di Kubernetes: una mappa per costruire software sicuro senza fermare la consegna."
slug: "devsecops-la-serie"
date: 2026-03-10T09:00:00+02:00
lastmod: 2026-03-10T09:00:00+02:00
categories:
    - Security
    - DevOps
tags:
    - DevSecOps
    - CI/CD
    - Supply Chain
keywords:
    - DevSecOps
    - shift left
    - secure SDLC
    - pipeline sicura
    - serie
image: "cover.png"
weight: 2
toc: true
links:
  - title: "OWASP DevSecOps Guideline"
    description: "La guida OWASP per integrare la sicurezza nel ciclo DevOps."
    website: https://owasp.org/www-project-devsecops-guideline/
  - title: "NIST SSDF (SP 800-218)"
    description: "Il Secure Software Development Framework del NIST."
    website: https://csrc.nist.gov/pubs/sp/800/218/final
---

## Perché questa serie

Per anni la sicurezza è arrivata alla fine: un audit a ridosso del rilascio, una lista di
vulnerabilità da sistemare *dopo* che il codice era già scritto, un cancello che rallentava la
consegna senza renderla più sicura. **DevSecOps** ribalta questo ordine: la sicurezza entra in ogni
fase del ciclo di vita, automatizzata, misurata e trattata come responsabilità di tutti — non come
il compito di un team separato alla fine della catena.

Questa serie è un percorso pratico in **30 capitoli**. Non un elenco di strumenti, ma un modo di
pensare: ogni controllo il più presto possibile (*shift left*), ogni artefatto verificabile, ogni
decisione di rischio esplicita. Gli strumenti cambiano ogni due anni; i principi no.

## Come è organizzata

```mermaid
flowchart LR
    C[Cultura<br/>shift-left] --> D[Design<br/>threat model]
    D --> B[Build<br/>SAST/SCA/segreti]
    B --> A[Artefatti<br/>SBOM/firma/SLSA]
    A --> P[Deploy<br/>pipeline/IaC/policy]
    P --> R[Runtime<br/>K8s/admission/Falco]
    R --> O[Operate<br/>vuln mgmt/IR/metriche]
    O --> C
    style C fill:#fde2e4,stroke:#e63946
    style R fill:#e8f0fe,stroke:#4361ee
```

Il filo conduttore segue il viaggio del codice: nasce da una **cultura** e da un **design** sicuri,
viene **costruito** con controlli automatici, impacchettato in **artefatti** verificabili, portato in
produzione da una **pipeline** governata, difeso a **runtime** e **operato** con misure e risposta
agli incidenti. Poi si ricomincia: DevSecOps è un ciclo, non una linea.

## I capitoli

1. **Fondamenta** — Cos'è DevSecOps, il Secure SDLC, il threat modeling nel ciclo, la gestione dei
   segreti.
2. **Build** — SAST, SCA e dipendenze, DAST, IAST/RASP, fuzzing: trovare i difetti mentre si scrive.
3. **Supply chain** — SBOM, SLSA, firma degli artefatti: fidarsi solo di ciò che si può verificare.
4. **Pipeline e deploy** — Sicurezza della CI/CD, IaC security, policy as code nella pipeline.
5. **Runtime** — Sicurezza delle immagini, hardening di Kubernetes, admission control, runtime
   security, segreti e identità dei workload.
6. **Operate** — Patch management, security gates, vulnerability management, logging e detection,
   incident response, compliance as code, metriche e cultura.

## A chi si rivolge

A chi scrive codice e vuole capire dove la sicurezza tocca il suo lavoro; a chi gestisce pipeline e
cluster e deve renderli difendibili; a chi guida team e vuole misurare il rischio invece di
subirlo. Diamo per note le basi di Git, container e CI/CD; tutto il resto lo costruiamo insieme.

DevSecOps non rallenta la consegna: la rende *ripetibile*. Un rilascio sicuro e automatizzato è più
veloce di un audit manuale fatto nel panico la sera prima. Partiamo dal perché, nel primo capitolo.
