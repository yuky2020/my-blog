---
title: "Admission control: il buttafuori del cluster"
description: "L'admission control è l'ultimo punto in cui dire 'no' prima che un pod parta. Validare e mutare le richieste all'API server significa rifiutare immagini non firmate, container privilegiati e configurazioni fuori policy. Kyverno e OPA Gatekeeper come PEP del cluster."
slug: "admission-control"
date: 2026-07-14T09:00:00+02:00
lastmod: 2026-07-14T09:00:00+02:00
categories:
    - Security
    - DevOps
tags:
    - DevSecOps
    - Kubernetes
    - Admission Control
keywords:
    - admission control
    - Kyverno
    - OPA Gatekeeper
    - validating webhook
    - policy enforcement
image: "cover.png"
toc: true
links:
  - title: "Kubernetes — Admission Controllers"
    description: "Come funzionano gli admission controller e i webhook."
    website: https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/
  - title: "Kyverno"
    description: "Policy engine per Kubernetes nativo, senza linguaggio dedicato."
    website: https://kyverno.io/
---

## Perché conta

L'[hardening]({{< relref "post/kubernetes-hardening" >}}) definisce *come* dovrebbe girare un pod. Ma
chi impedisce che qualcuno applichi comunque un manifest che viola quelle regole? L'**admission
control** è la risposta: il punto, lungo il percorso di ogni richiesta all'API server, in cui si può
*rifiutare* o *modificare* un oggetto **prima** che venga persistito e schedulato. È l'ultima porta —
e la più efficace, perché agisce su *tutto* ciò che entra nel cluster, da qualunque fonte.

## Dove si inserisce

```mermaid
flowchart LR
    U[kubectl / CI / operator] -->|crea pod| API[API server]
    API --> AUTH[AuthN/AuthZ<br/>RBAC]
    AUTH --> MUT[Mutating<br/>webhook]
    MUT --> VAL[Validating<br/>webhook<br/>= PEP]
    VAL -->|conforme| ETCD[(etcd → schedulato)]
    VAL -.non conforme.-> REJ[RIFIUTATO<br/>con motivazione]
    style VAL fill:#fde2e4,stroke:#e63946
```

Dopo l'autenticazione e RBAC, la richiesta passa da due tipi di webhook:

- **Mutating**: *modifica* l'oggetto. Es. inietta automaticamente un security context sicuro, aggiunge
  label, imposta limiti di risorse di default.
- **Validating**: *accetta o rifiuta*. È il [PEP]({{< relref "post/pdp-pep-il-motore-delle-policy" >}})
  del cluster: valuta l'oggetto contro le policy e, se viola, lo blocca con un messaggio.

## Cosa si applica qui

L'admission control è dove le promesse dei capitoli precedenti diventano enforcement reale:

```text {hl_lines=[1,2,3]}
Rifiuta se:
  - immagine NON firmata da identità attesa   (verifica Sigstore/cosign)
  - immagine con CVE critici o senza SBOM
  - container privilegiato / runAsRoot / hostPath pericolosi
  - manca il limite di risorse, usa tag :latest, namespace sbagliato
Muta per imposizione:
  - aggiungi securityContext sicuro di default, label owner, networkpolicy
```

La verifica della firma è l'esempio più nitido: la [firma]({{< relref "post/firma-artefatti-sigstore" >}})
diventa un *controllo d'accesso* solo quando un validating webhook la verifica e rifiuta ciò che non
proviene dall'identità attesa. Senza admission control, firmare è teatro.

## Kyverno e OPA Gatekeeper

Due approcci allo stesso ruolo di PEP:

- **Kyverno**: le policy sono risorse Kubernetes in YAML, native per chi già conosce i manifest.
  Nessun linguaggio nuovo da imparare; fa anche mutazione e generazione di risorse.
- **OPA Gatekeeper**: porta [OPA e Rego]({{< relref "post/policy-as-code-pipeline" >}}) nel cluster.
  Più potente ed espressivo, a costo di imparare Rego, e con il vantaggio di condividere lo *stesso*
  linguaggio di policy tra pipeline e cluster.

## Pipeline e cluster: due reti, non una

L'admission control e il controllo in pipeline si rafforzano a vicenda. La pipeline cattura presto e
dà feedback allo sviluppatore (shift-left); l'admission control cattura *tutto* ciò che arriva
all'API, incluso ciò che bypassa la pipeline — un `kubectl apply` manuale, un operator, un attaccante
con credenziali. Fare entrambi significa feedback precoce **e** enforcement inaggirabile.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se già controllo tutto in pipeline — scansione immagini, firma, policy Rego — perché aggiungere l'admission control nel cluster? Non è controllare due volte la stessa cosa?</summary>
<p>È controllare la stessa <em>regola</em> in due punti con garanzie diverse, e la differenza è tutta in
ciò che ciascun punto può garantire. La pipeline ha un presupposto fatale come unico controllo: che ogni
cosa che arriva nel cluster sia passata <em>dalla</em> pipeline. Nella realtà non è così. Un operatore
sotto incidente fa un <code>kubectl apply</code> a mano per "sistemare al volo"; un operator o un
controller crea pod dinamicamente senza passare da nessuna CI; un Helm chart di terze parti installa
risorse che la tua pipeline non ha mai visto; un attaccante che ha ottenuto credenziali valide parla
direttamente con l'API server — e nessuno di questi percorsi tocca la pipeline. Tutto ciò che la pipeline
verifica diventa irrilevante per qualunque oggetto che entra da una porta diversa. L'admission control
chiude proprio questo: sta sull'API server, quindi vede <em>ogni</em> richiesta di creazione o modifica,
da qualunque fonte, e applica la policy lì, nell'unico collo di bottiglia che nessuno può aggirare senza
compromettere l'API stessa. Questo non rende inutile la pipeline, anzi: i due hanno scopi complementari.
La pipeline è veloce, dà feedback allo sviluppatore riga per riga sulla pull request, fa fallire la build
quando il contesto è fresco — è prevenzione e insegnamento (shift-left). L'admission control è tardivo e
muto per lo sviluppatore ma <em>inaggirabile</em> — è enforcement. Il modello corretto è lo stesso
principio ("solo immagini firmate") espresso una volta e applicato in due punti: in pipeline per fermare
presto e bene, all'ammissione per fermare comunque. Togliere la pipeline ti lascia l'enforcement senza
feedback precoce; togliere l'admission control ti lascia il feedback con un enforcement pieno di buchi.
Li vuoi entrambi perché difendono da fallimenti diversi.</p>
</details>
{{< /rawhtml >}}

## Conclusione

L'admission control è il buttafuori del cluster: mutating webhook che impongono default sicuri,
validating webhook che rifiutano ciò che viola le policy — immagini non firmate, container
privilegiati, configurazioni fuori norma. È dove firma e policy diventano enforcement inaggirabile, a
complemento della pipeline. Ma tutti i controlli visti finora sono *preventivi*: agiscono prima che il
codice giri. Qualcosa passerà comunque, e allora serve vedere e reagire a ciò che accade *mentre*
succede. È la runtime security, prossimo capitolo.
