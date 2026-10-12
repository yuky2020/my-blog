---
title: "Crittografia applicata: la serie"
description: "Dieci capitoli per capire la crittografia che usi ogni giorno senza accorgertene: cifratura simmetrica e AEAD, hashing, HMAC, password, chiavi asimmetriche, scambio di chiavi, firme, PKI e il futuro post-quantum. Pratica, non matematica fine a sé stessa."
slug: "crittografia-applicata-la-serie"
date: 2026-08-04T09:00:00+02:00
lastmod: 2026-08-04T09:00:00+02:00
categories:
    - Security
    - Cryptography
tags:
    - Crittografia
    - TLS
    - PKI
keywords:
    - crittografia applicata
    - AES
    - RSA
    - TLS
    - serie
image: "cover.png"
weight: 2
toc: true
links:
  - title: "Cryptographic Right Answers"
    description: "Le scelte crittografiche sensate di default, aggiornate nel tempo."
    website: https://www.latacora.com/blog/2018/04/03/cryptographic-right-answers/
  - title: "NIST Cryptographic Standards"
    description: "Gli standard crittografici di riferimento del NIST."
    website: https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines
---

## Perché questa serie

Usi la crittografia centinaia di volte al giorno senza pensarci: ogni sito in HTTPS, ogni messaggio
cifrato, ogni password salvata, ogni aggiornamento firmato. Quando funziona è invisibile. Quando la si
implementa male — ed è facile — i dati trapelano in silenzio, e nessun test funzionale se ne accorge.
Questa serie in **10 capitoli** spiega la crittografia *applicata*: non le dimostrazioni matematiche,
ma *quale* primitiva usare, *perché*, e quali errori evitare.

## La regola d'oro

Prima di tutto il resto, una regola che vale più di ogni capitolo:

> **Non inventare la tua crittografia, e non implementare primitive a mano.** Usa librerie
> affermate, revisionate, e le loro impostazioni predefinite sicure.

La crittografia fallisce in modi silenziosi: un nonce riusato, un confronto non a tempo costante, un
padding mal gestito. Capire *come* funziona serve a usarla bene e a riconoscere gli errori — non a
riscriverla. Tutta la serie è pensata con questo spirito.

## La mappa

```mermaid
flowchart TD
    SYM[Simmetrica<br/>AES, AEAD] --> HASH[Hashing<br/>integrità]
    HASH --> MAC[HMAC<br/>autenticità]
    MAC --> PW[Password<br/>hashing]
    PW --> ASYM[Asimmetrica<br/>RSA, ECC]
    ASYM --> KEX[Scambio chiavi<br/>forward secrecy]
    KEX --> SIG[Firme<br/>digitali]
    SIG --> PKI[PKI<br/>catena di fiducia]
    PKI --> PQC[Post-quantum]
    style SYM fill:#fde2e4,stroke:#e63946
    style PKI fill:#e8f0fe,stroke:#4361ee
```

Si parte dai mattoni più semplici (cifrare e verificare l'integrità) e si sale fino a come TLS, le
firme del software e la PKI li combinano. L'ultimo capitolo guarda avanti: cosa cambia quando
arriveranno i computer quantistici.

## I tre obiettivi della crittografia

Tutto ruota attorno a tre proprietà, e confonderle è l'errore concettuale più comune:

- **Riservatezza**: nessuno legge il messaggio tranne il destinatario. → cifratura.
- **Integrità**: il messaggio non è stato alterato. → hash, MAC.
- **Autenticità**: il messaggio viene davvero da chi dice. → MAC, firme.

Cifrare *non* garantisce integrità; un hash *non* garantisce autenticità. Gran parte della serie è
imparare quale strumento dà quale garanzia, e come combinarli senza lasciare buchi.

## A chi si rivolge

A chi scrive software e deve scegliere come cifrare dati, salvare password, verificare firme — senza
essere un crittografo. Diamo per note le basi (byte, encoding, un po' di aritmetica); tutto il resto
lo costruiamo. Questa serie è il complemento naturale di temi già trattati come il
[TLS]({{< relref "post/tls-deep-dive" >}}) e la [Certificate Transparency]({{< relref "post/certificate-transparency" >}}).

Partiamo dal mattone più usato di tutti: la cifratura simmetrica, prossimo capitolo.
