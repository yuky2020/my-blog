---
title: "Crittografia dei dati nel cloud"
description: "Cifrare i dati a riposo e in transito è la rete di sicurezza quando tutto il resto fallisce: se un attaccante copia un disco o intercetta il traffico, trova solo rumore. Nel cloud la cifratura è quasi sempre disponibile e spesso attiva di default, ma chi controlla le chiavi cambia tutto. Encryption at rest, in transit e il nodo del key management."
slug: "crittografia-dati-cloud"
date: 2026-07-28T09:00:00+02:00
lastmod: 2026-07-28T09:00:00+02:00
categories:
    - Cloud
tags:
    - Cloud
    - Crittografia
    - KMS
keywords:
    - encryption at rest
    - encryption in transit
    - BYOK
    - crittografia cloud
image: "cover.png"
toc: true
links:
  - title: "AWS — Encryption at rest and in transit"
    description: "Panoramica dei servizi e delle opzioni di cifratura su AWS."
    website: https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html
  - title: "Google Cloud — Encryption at rest"
    description: "Come GCP cifra i dati a riposo di default e la gerarchia delle chiavi."
    website: https://cloud.google.com/docs/security/encryption/default-encryption
---

## Perché conta

La cifratura è l'ultima rete di sicurezza: quando l'identità, la rete e la configurazione hanno
fallito e un attaccante mette le mani sui dati, la cifratura decide se trova informazioni o solo
rumore. Nel cloud è quasi sempre disponibile, spesso attiva di default, e costa poco o nulla in
prestazioni grazie all'accelerazione hardware. La domanda non è più "cifrare sì o no", ma **dove, come,
e soprattutto chi tiene le chiavi**.

## I due fronti: a riposo e in transito

```mermaid
flowchart LR
    subgraph REST["A riposo (at rest)"]
        DB[(Disco / DB / storage)]
        DB -.cifrato con.-> K1[Chiave dal KMS]
    end
    subgraph TRANSIT["In transito (in transit)"]
        C[Client] -->|TLS| S[Servizio]
    end
    style K1 fill:#fde2e4,stroke:#e63946
```

- **A riposo**: dischi, database, storage a oggetti, backup, snapshot. Si appoggia alla
  [crittografia a busta del KMS]({{< relref "post/gestione-segreti-e-kms" >}}) vista prima: i dati sono
  cifrati con chiavi dati, le chiavi dati con la master.
- **In transito**: ogni byte che viaggia in rete, protetto da **TLS**. Vale non solo verso Internet ma
  anche *dentro* la tua rete cloud: tra servizi, verso il database, tra microservizi. "Rete privata"
  non significa "rete fidata".

## Chi tiene le chiavi: il vero controllo

Chi controlla la chiave controlla i dati. Le opzioni, dalla più comoda alla più controllata:

```text {hl_lines=[3]}
Chiavi gestite dal provider   → comode, zero gestione, il provider può tecnicamente accedervi
Chiavi gestite da te nel KMS  → tu decidi rotazione, revoca e policy d'uso (raccomandato)
BYOK (bring your own key)     → importi la tua chiave nel KMS del provider
HYOK / external key           → la chiave resta fuori dal cloud, sotto il tuo controllo totale
```

Per la maggior parte dei casi, **chiavi tue gestite nel KMS del provider** è il giusto equilibrio:
controlli policy, rotazione e revoca (revocare la chiave rende i dati illeggibili all'istante, un
"interruttore d'emergenza" potente), senza l'onere operativo di custodire hardware. BYOK e chiavi
esterne servono a requisiti di compliance o sovranità del dato più stringenti.

## La cifratura non sostituisce il controllo d'accesso

Un equivoco frequente: "i dati sono cifrati, quindi sono al sicuro". La cifratura a riposo protegge
contro chi ruba il *supporto fisico* o un backup — non contro chi ha i permessi IAM per leggere i dati
*attraverso il servizio*, perché per lui la decifratura è trasparente. Un bucket cifrato ma pubblico
resta un data breach. La cifratura è *complementare* al controllo d'accesso, non un suo sostituto.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se il provider offre la cifratura a riposo attiva di default e gestisce lui le chiavi, perché dovrei complicarmi la vita con chiavi mie nel KMS? I dati sono già cifrati.</summary>
<p>Perché "cifrati con chiavi del provider" e "cifrati con chiavi tue" proteggono da minacce diverse, e
la differenza conta proprio nei casi che ti tengono sveglio la notte. Con le chiavi gestite dal provider
ottieni la protezione base — se qualcuno ruba un disco fisico dal data center, trova rumore — ed è già
meglio di niente. Ma non ottieni tre cose. Primo, il <em>controllo della revoca</em>: con una chiave tua
puoi, in caso di incidente o sospetto, revocarla e rendere i dati immediatamente illeggibili a chiunque,
incluse applicazioni compromesse che avevano i permessi — è un interruttore d'emergenza che le chiavi del
provider non ti danno. Secondo, la <em>separazione dei poteri</em>: con chiavi tue, l'accesso ai dati
richiede sia il permesso sul servizio sia il permesso sulla chiave KMS, due controlli IAM distinti che
puoi affidare a ruoli diversi — così nessuna singola identità, da sola, decifra tutto. Terzo, la
<em>garanzia verso terzi e la compliance</em>: molti requisiti normativi e contrattuali chiedono che il
cliente, non il provider, controlli le chiavi; con chiavi tue hai log d'uso delle chiavi, policy
esplicite e la possibilità di dimostrare chi può decifrare cosa. Sul "complicarmi la vita": gestire una
chiave nel KMS del provider è questione di pochi clic o poche righe di IaC — non stai custodendo hardware,
stai solo spostando la proprietà logica della chiave dal provider a te. Il costo è minimo, il controllo
che guadagni è sostanziale. Le chiavi del provider vanno bene per dati a basso rischio; per tutto ciò che
conta, le chiavi tue sono lo standard ragionevole.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Cifrare a riposo e in transito è la rete di sicurezza finale, ma il controllo vero sta nelle chiavi:
gestirle tu nel KMS dà revoca, separazione dei poteri e compliance, mentre la cifratura resta
complementare — mai sostitutiva — del controllo d'accesso. Il servizio dove questi principi si
scontrano più spesso con la realtà degli incidenti è lo storage a oggetti, i famigerati bucket. È il
prossimo capitolo, [sicurezza dello storage a oggetti]({{< relref "post/sicurezza-storage-oggetti" >}}).
