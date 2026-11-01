---
title: "Sicurezza Cloud in pratica: la serie"
description: "Una serie in 20 capitoli sulla sicurezza del cloud, provider-agnostica ma con esempi concreti su AWS, Azure e GCP. Dal modello di responsabilità condivisa all'IAM, crittografia, rete, detection, postura, IaC, container, serverless, multi-account e incident response. Il percorso ordinato per mettere in sicurezza un ambiente cloud."
slug: "sicurezza-cloud-la-serie"
date: 2026-06-16T09:00:00+02:00
lastmod: 2026-06-16T09:00:00+02:00
weight: 2
categories:
    - Cloud
    - Cloud Security
tags:
    - Cloud
    - Sicurezza Cloud
    - Roadmap
keywords:
    - sicurezza cloud
    - cloud security
    - AWS Azure GCP
    - roadmap cloud security
image: "cover.png"
toc: true
---

## Perché questa serie

Il cloud non è "il computer di qualcun altro": è un modello operativo diverso, con primitive di
sicurezza diverse. Firewall, identità, chiavi, log e perimetro esistono ancora, ma cambiano forma —
e la maggior parte degli incidenti cloud non nasce da exploit sofisticati, bensì da **configurazioni
sbagliate**: un bucket pubblico, un ruolo troppo permissivo, una chiave lasciata in chiaro, un log mai
attivato. Questa serie costruisce, capitolo dopo capitolo, il modello mentale per non commettere quegli
errori — e per riconoscerli quando li erediti.

L'approccio è **provider-agnostico**: i principi valgono su AWS, Azure e GCP, e dove serve cito il
servizio concreto di ciascuno. Non è un tutorial "clicca qui": è il *perché* dietro ogni controllo,
così che tu sappia adattarlo al tuo ambiente.

## Come leggerla

I capitoli sono ordinati come un percorso: ciascuno poggia sui precedenti. Si parte dal modello di
responsabilità condivisa (chi protegge cosa), poi l'identità — il vero perimetro del cloud — poi dati,
rete, visibilità, postura e automazione, fino alla risposta agli incidenti.

## I capitoli

1. [Il modello di responsabilità condivisa]({{< relref "post/modello-responsabilita-condivisa" >}})
2. [IAM: identità e accessi]({{< relref "post/iam-identita-e-accessi" >}})
3. [Il principio del privilegio minimo]({{< relref "post/principio-minimo-privilegio" >}})
4. [L'identità dei workload]({{< relref "post/identita-dei-workload" >}})
5. [Gestione dei segreti e KMS]({{< relref "post/gestione-segreti-e-kms" >}})
6. [Crittografia dei dati nel cloud]({{< relref "post/crittografia-dati-cloud" >}})
7. [Sicurezza dello storage a oggetti]({{< relref "post/sicurezza-storage-oggetti" >}})
8. [La rete virtuale: VPC e subnet]({{< relref "post/rete-virtuale-vpc" >}})
9. [Esposizione e perimetro]({{< relref "post/esposizione-perimetro-cloud" >}})
10. [Segmentazione e Zero Trust nel cloud]({{< relref "post/segmentazione-zero-trust-cloud" >}})
11. [Logging e audit trail]({{< relref "post/logging-e-audit-trail" >}})
12. [Threat detection nel cloud]({{< relref "post/threat-detection-cloud" >}})
13. [CSPM: la postura di sicurezza]({{< relref "post/cspm-postura-sicurezza" >}})
14. [Infrastructure as Code sicuro e policy as code]({{< relref "post/iac-sicuro-policy-as-code" >}})
15. [Sicurezza di Kubernetes gestito]({{< relref "post/kubernetes-gestito-sicurezza" >}})
16. [Serverless security]({{< relref "post/serverless-security" >}})
17. [Multi-account e landing zone]({{< relref "post/multi-account-landing-zone" >}})
18. [Compliance e governance nel cloud]({{< relref "post/compliance-e-governance-cloud" >}})
19. [Incident response nel cloud]({{< relref "post/incident-response-cloud" >}})

## Il filo conduttore

```mermaid
flowchart LR
    R[Responsabilità<br/>condivisa] --> I[Identità<br/>il nuovo perimetro]
    I --> D[Dati<br/>cifratura e segreti]
    D --> N[Rete<br/>VPC e perimetro]
    N --> V[Visibilità<br/>log e detection]
    V --> P[Postura<br/>CSPM e IaC]
    P --> IR[Incident<br/>response]
    style I fill:#fde2e4,stroke:#e63946
```

Un filo solo attraversa tutta la serie: nel cloud **l'identità è il perimetro**, e la
**configurazione è il campo di battaglia**. Chi capisce questi due fatti ha già evitato la maggior
parte degli incidenti reali. Si parte dal primo capitolo: chi è responsabile di cosa.
