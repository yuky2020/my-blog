---
title: "Hashing e integrità"
description: "Una funzione di hash trasforma dati di qualsiasi dimensione in un'impronta fissa. Sembra semplice, ma le proprietà che la rendono crittografica — resistenza alle collisioni, effetto valanga — sono sottili, e usare l'hash giusto per lo scopo giusto evita errori che si pagano caro."
slug: "hashing-e-integrita"
date: 2026-08-18T09:00:00+02:00
lastmod: 2026-08-18T09:00:00+02:00
categories:
    - Security
    - Cryptography
tags:
    - Crittografia
    - Hashing
    - Integrità
keywords:
    - funzioni di hash
    - SHA-256
    - SHA-3
    - collisioni
    - effetto valanga
math: true
image: "cover.png"
toc: true
links:
  - title: "SHA-3 — NIST FIPS 202"
    description: "Lo standard della famiglia di hash SHA-3 (Keccak)."
    website: https://csrc.nist.gov/pubs/fips/202/final
  - title: "SHA-256 — NIST FIPS 180-4"
    description: "Lo standard delle funzioni di hash SHA-2."
    website: https://csrc.nist.gov/pubs/fips/180-4/upd1/final
---

## Perché conta

Il tag AEAD del [capitolo precedente]({{< relref "post/cifratura-simmetrica-e-aead" >}}) ci ha dato
un primo assaggio di integrità. Ora il mattone fondamentale: la **funzione di hash crittografica**.
Prende dati di qualsiasi dimensione e produce un'impronta di lunghezza fissa — il *digest*. È ovunque:
verifica dei download, [SBOM e firma del software]({{< relref "post/firma-artefatti-sigstore" >}}),
strutture come i Merkle tree della [Certificate Transparency]({{< relref "post/certificate-transparency" >}}),
deduplicazione, blockchain. Sembra banale; le proprietà che la rendono *crittografica* non lo sono.

## Le tre proprietà

Una funzione di hash è crittografica se soddisfa tre proprietà, in difficoltà crescente:

```text {hl_lines=[2,3,4]}
Dato un hash h = H(m):
  1. Resistenza alla preimmagine   → dato h, infattibile trovare m
  2. Resistenza alla 2a preimmagine → dato m, infattibile trovare m' ≠ m con H(m')=H(m)
  3. Resistenza alle collisioni     → infattibile trovare QUALSIASI coppia m≠m' con H(m)=H(m')
```

La resistenza alle **collisioni** è la più forte e la più difficile da garantire: non devi trovare un
secondo messaggio per *uno dato*, ma *una coppia qualsiasi* che collida — e qui il paradosso del
compleanno gioca contro di te.

## Il paradosso del compleanno

Se l'output ha $n$ bit, ci sono $2^n$ valori possibili. Ingenuamente penseresti che servano $2^n$
tentativi per una collisione. In realtà, per il paradosso del compleanno, ne bastano circa:

$$ 2^{n/2} $$

Un hash da 256 bit offre quindi circa $2^{128}$ di sicurezza contro le collisioni, non $2^{256}$. È il
motivo per cui gli hash moderni usano output ampi (256+ bit): la resistenza alle collisioni è
*metà* della lunghezza in bit. Un hash da 128 bit avrebbe solo $2^{64}$ di margine — oggi aggredibile.

## L'effetto valanga

Una buona funzione di hash ha l'**effetto valanga**: cambiare un solo bit dell'input cambia circa
*metà* dei bit dell'output, in modo imprevedibile.

```text
H("crittografia")  = 1a2b3c... (256 bit)
H("Crittografia")  = f9e8d7... (completamente diverso, pur cambiando 1 bit)
```

Questo rende impossibile "avvicinarsi" a un digest per tentativi incrementali: non c'è correlazione
tra la distanza degli input e quella degli output. È ciò che rende l'hash utile come impronta
infalsificabile.

## Quale hash usare

```text {hl_lines=[2,3,5]}
Scopo generale (integrità, firme, SBOM):
  SHA-256 / SHA-512   → solido, standard, ovunque
  SHA-3 (Keccak)      → costruzione diversa (sponge), utile come alternativa indipendente
EVITARE per uso crittografico:
  MD5, SHA-1          → collisioni PRATICHE dimostrate. Rotti. Solo per checksum non ostili.
```

MD5 e SHA-1 non sono "deboli": sono **rotti**. Esistono collisioni costruite in pratica (due file
diversi con lo stesso hash), quindi non offrono più alcuna garanzia contro un avversario. Vanno
eliminati da ogni contesto di sicurezza.

## L'errore da evitare: l'hash non autentica

Un hash dimostra che i dati *non sono cambiati per caso* o che corrispondono a un valore noto. **Non**
dimostra *chi* li ha prodotti, né li protegge da un attaccante che può cambiare *sia* i dati *sia*
l'hash. Se pubblichi `file + H(file)` e un attaccante controlla il canale, sostituisce entrambi. Per
legare l'integrità a un segreto (autenticità) serve altro: l'HMAC, prossimo capitolo. E attenzione a
un uso sbagliatissimo che tratteremo dopo — **l'hash semplice non va usato per le password**.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se SHA-256 è così solido, perché non usarlo anche per le password invece di algoritmi dedicati come Argon2?</summary>
<p>Perché per le password la proprietà che vuoi è l'<em>opposto</em> di quella per cui SHA-256 è
progettato, ed è esattamente questa inversione di obiettivo a rendere l'hash generico pericoloso lì.
SHA-256 è costruito per essere <strong>veloce</strong>: deve calcolare l'impronta di gigabyte di dati in
un istante, verificare firme e integrità senza rallentare nulla. La velocità è una virtù quando l'hash
serve a fare integrità. Ma quando l'hash protegge una password, la velocità diventa il regalo più grande
che puoi fare all'attaccante. Pensa a cosa succede quando un database di password trapela: l'attaccante ha
gli hash e vuole risalire alle password provando candidati (dizionari, password comuni, brute force su
quelle corte). Il suo collo di bottiglia è quanti tentativi al secondo riesce a fare. Con SHA-256, su
hardware moderno — e peggio su GPU o ASIC costruiti apposta — parliamo di <em>miliardi</em> di hash al
secondo: un dizionario di tutte le password umane plausibili si esaurisce in minuti o ore. Hai usato un
hash eccellente e hai protetto quasi nulla, perché la sua velocità lavora per chi attacca. Gli algoritmi
di password hashing come Argon2, bcrypt e scrypt fanno la scelta deliberatamente opposta: sono
<em>lenti</em> e, nel caso di Argon2 e scrypt, deliberatamente <em>costosi in memoria</em>. Puoi tararli
perché un singolo hash impieghi, diciamo, un decimo di secondo e richieda decine di megabyte di RAM: per
te che verifichi un login è impercettibile, ma per l'attaccante che deve provare miliardi di candidati
diventa proibitivo in tempo e in costo hardware, e il requisito di memoria neutralizza proprio il
vantaggio delle GPU, che hanno molti core ma poca memoria per core. In più questi algoritmi integrano il
<em>salt</em> per impedire gli attacchi precalcolati (le rainbow table) e il <em>costo regolabile</em> per
restare al passo con l'hardware che migliora. In breve: SHA-256 risponde alla domanda "questi dati sono
integri?" nel modo più efficiente possibile; le password pongono la domanda opposta, "quanto posso
rendere costoso indovinare?", e lì la risposta giusta è un algoritmo progettato per essere lento e avido
di memoria. Usare SHA-256 per le password non è un'ottimizzazione, è usare lo strumento costruito per
l'obiettivo sbagliato. Lo vedremo in dettaglio nel capitolo sul password hashing.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Una funzione di hash crittografica dà un'impronta fissa con resistenza a preimmagine e collisioni
(ridotta a $2^{n/2}$ dal paradosso del compleanno) ed effetto valanga: usa SHA-256/SHA-3, mai MD5 o
SHA-1. Ma l'hash garantisce integrità, non *autenticità*: non dice chi ha prodotto i dati. Per legarli
a un segreto condiviso serve aggiungere una chiave all'hash — è l'HMAC, prossimo capitolo.
