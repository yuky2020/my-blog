---
title: "CSPM: la postura di sicurezza"
description: "La maggior parte dei breach cloud nasce da misconfigurazioni, non da exploit. Il CSPM (Cloud Security Posture Management) scansiona di continuo l'ambiente confrontandolo con benchmark e best practice, e segnala ciò che è configurato male prima che qualcuno lo sfrutti. Come funziona, cosa trova, e perché la vera sfida è passare dal trovare al correggere."
slug: "cspm-postura-sicurezza"
date: 2026-09-15T09:00:00+02:00
lastmod: 2026-09-15T09:00:00+02:00
categories:
    - Cloud
    - Cloud Security
tags:
    - Cloud
    - CSPM
    - Postura
keywords:
    - CSPM
    - posture management
    - misconfiguration
    - CIS benchmark cloud
image: "cover.png"
toc: true
links:
  - title: "CIS Benchmarks"
    description: "I benchmark di configurazione sicura per i principali cloud."
    website: https://www.cisecurity.org/cis-benchmarks
  - title: "AWS Security Hub"
    description: "Postura di sicurezza centralizzata e controlli automatici."
    website: https://docs.aws.amazon.com/securityhub/latest/userguide/
---

## Perché conta

La [threat detection]({{< relref "post/threat-detection-cloud" >}}) ti dice quando qualcuno ti sta
attaccando. Il CSPM risponde a una domanda che viene *prima*: la mia configurazione offre il fianco?
Dato che la stragrande maggioranza degli incidenti cloud nasce da **misconfigurazioni** — un bucket
pubblico, un gruppo di sicurezza aperto, il logging spento, la cifratura non attiva — il modo più
efficace di ridurre il rischio è trovare e chiudere questi buchi *prima* che qualcuno li sfrutti. Il
**Cloud Security Posture Management** fa esattamente questo, in continuazione.

## Il ciclo del CSPM

```mermaid
flowchart LR
    SCAN[Scansiona tutte<br/>le risorse] --> CMP[Confronta con<br/>benchmark e policy]
    CMP --> FIND[Elenca le<br/>misconfigurazioni]
    FIND --> FIX[Correggi<br/>manuale o auto]
    FIX --> SCAN
    style CMP fill:#fde2e4,stroke:#e63946
```

Il CSPM legge in continuo lo stato di tutte le risorse dell'ambiente e lo confronta con un insieme di
regole: i **benchmark CIS**, le best practice del provider, e le tue policy custom. Produce un elenco
di scostamenti con una priorità, e idealmente chiude il cerchio con la **remediation** — manuale o
automatica.

## Cosa trova tipicamente

```text {hl_lines=[2,3,4]}
Finding CSPM ricorrenti:
  - storage pubblico o senza cifratura
  - security group con 0.0.0.0/0 su porte sensibili (22, 3389, 3306...)
  - audit trail disattivato o non centralizzato
  - utenti senza MFA, chiavi d'accesso vecchie mai ruotate
  - ruoli con permessi amministrativi non necessari
```

Sono gli stessi temi dei capitoli precedenti — identità, storage, rete, logging — visti ora
dall'angolo del *controllo continuo*: non basta configurare bene una volta, perché gli ambienti cloud
cambiano ogni giorno e la postura **deriva** nel tempo. Qualcuno apre una porta "per un test", crea un
bucket al volo, assegna un permesso di troppo: il CSPM intercetta questa deriva.

## Il collo di bottiglia: dal trovare al correggere

Un CSPM attivato per la prima volta su un ambiente maturo restituisce spesso **migliaia** di finding.
Il rischio è la paralisi. La chiave è **prioritizzare per rischio reale**, non per numero: un bucket
pubblico con dati di clienti conta più di cento avvisi cosmetici. E dove possibile, **prevenire invece
di correggere**: molte misconfigurazioni non dovrebbero mai nascere, se l'infrastruttura è definita come
codice e controllata *prima* del deploy — il ponte verso il prossimo capitolo.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se il CSPM trova migliaia di problemi e nessuno riesce a chiuderli tutti, non è uno strumento che produce solo ansia e una lista infinita che fa sembrare tutto rotto?</summary>
<p>È un rischio reale — un CSPM mal usato genera una lista schiacciante che demoralizza invece di aiutare
— ma la lista infinita non è un difetto dello strumento: è la fotografia onesta di un debito di sicurezza
che <em>esisteva già</em>, solo invisibile. Prima del CSPM i mille problemi c'erano comunque; semplicemente
non li vedevi, il che è peggio, non meglio. Il valore sta nel non trattare la lista come un compito "tutto
o niente". Primo, <em>prioritizza per rischio</em>: non tutti i finding sono uguali, e un buon CSPM li
pesa — esposizione a Internet, sensibilità dei dati, privilegi coinvolti. Dieci finding critici chiusi
valgono più di mille cosmetici, e quei dieci li affronti subito. Secondo, <em>ferma l'emorragia</em>:
configura guardrail preventivi perché i <em>nuovi</em> problemi non nascano più (il blocco accesso
pubblico a livello di account, le policy d'organizzazione), così la lista smette di crescere mentre
smaltisci l'arretrato. Terzo, <em>misura la tendenza, non il totale</em>: l'obiettivo non è "zero finding"
oggi — irrealistico — ma una curva che scende e un tempo di correzione dei critici che si accorcia.
Quarto, <em>automatizza le correzioni ovvie</em>: molti finding (cifratura da attivare, tag mancanti,
logging da accendere) si rimediano in automatico senza intervento umano. La lista infinita fa paura solo
se la guardi come un muro; vista come una coda prioritizzata da cui togli prima le cose che bruciano, è
esattamente ciò che ti mancava per sapere dove intervenire. L'alternativa — non sapere — non è meno ansia:
è solo ignoranza che sembra calma finché non arriva il breach.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Il CSPM scansiona di continuo l'ambiente contro benchmark e policy, segnalando le misconfigurazioni —
la causa principale dei breach — prima che vengano sfruttate; la sfida vera è prioritizzare per rischio
e, meglio ancora, prevenire. E prevenire significa controllare la configurazione *prima* del deploy,
quando è ancora codice. È il tema dell'[Infrastructure as Code sicuro e policy as
code]({{< relref "post/iac-sicuro-policy-as-code" >}}), prossimo capitolo.
