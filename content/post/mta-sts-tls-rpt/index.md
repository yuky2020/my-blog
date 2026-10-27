---
title: "MTA-STS e TLS-RPT: rendere obbligatorio il TLS tra server di posta"
description: "SMTP cifra solo in modo opportunistico, e chi sta on-path può togliere STARTTLS senza che nessuno se ne accorga. MTA-STS pubblica una policy che rende TLS obbligatorio, TLS-RPT ti dice quando qualcosa non va: come funzionano, come si configurano e come si testano."
slug: "mta-sts-tls-rpt"
date: 2026-10-27T09:00:00+02:00
lastmod: 2026-10-27T09:00:00+02:00
categories:
    - Security
    - Networking
tags:
    - Network Security
    - TLS
    - DNS Security
    - Attacks
    - Hardening
keywords:
    - MTA-STS
    - TLS-RPT
    - STARTTLS
    - SMTP
    - downgrade attack
image: "cover.png"
toc: true
math: true
links:
  - title: "RFC 8461 — SMTP MTA Strict Transport Security (MTA-STS)"
    description: La specifica della policy MTA-STS, del record DNS e delle modalità testing/enforce.
    website: https://www.rfc-editor.org/rfc/rfc8461
  - title: "RFC 8460 — SMTP TLS Reporting"
    description: Il formato dei report JSON e il record _smtp._tls per riceverli.
    website: https://www.rfc-editor.org/rfc/rfc8460
  - title: "RFC 3207 — SMTP Service Extension for Secure SMTP over TLS"
    description: Il comando STARTTLS originale, alla base del problema del downgrade.
    website: https://www.rfc-editor.org/rfc/rfc3207
---

## Perché conta

Quando un server di posta consegna un messaggio a un altro, la sessione SMTP parte in chiaro sulla porta 25 e
solo dopo il comando `STARTTLS` (RFC 3207) passa a TLS. Il client non sa *a priori* se il destinatario lo
supporta, quindi se la negoziazione fallisce fa la cosa più "gentile": consegna in chiaro. È cifratura
**opportunistica**, e per un attaccante on-path è sufficiente cancellare la riga `250-STARTTLS` dalla risposta
del server per ottenere una sessione leggibile e modificabile. Nessun errore, nessun log sul mittente.

[DANE]({{< relref "post/dane-tlsa-dnssec" >}}) risolve il problema ma richiede DNSSEC. **MTA-STS** (RFC 8461)
offre lo stesso risultato appoggiandosi al modello WebPKI già noto: il destinatario pubblica via HTTPS una
policy che dice "i miei MX supportano TLS con certificato valido, se non riesci a usarlo non consegnare".
**TLS-RPT** (RFC 8460) completa il quadro con report giornalieri sui fallimenti.

## Come funziona

Il dominio `example.com` pubblica due cose: un record TXT che segnala l'esistenza della policy e un file
servito via HTTPS da un host dedicato, `mta-sts.example.com`.

```mermaid
sequenceDiagram
    participant S as MTA mittente
    participant D as DNS
    participant W as mta-sts.example.com (HTTPS)
    participant M as mx1.example.com
    S->>D: TXT _mta-sts.example.com
    D-->>S: "v=STSv1; id=20261027T0900"
    S->>W: GET /.well-known/mta-sts.txt
    W-->>S: mode: enforce, mx, max_age
    Note over S: policy in cache per max_age secondi
    S->>M: EHLO + STARTTLS
    M-->>S: certificato per mx1.example.com
    Note over S: nome MX in policy e certificato valido?<br/>se no: non consegna, riprova più tardi
    S->>M: DATA (cifrato)
```

Il campo `id` nel TXT serve solo a segnalare che la policy è cambiata: il mittente la riscarica quando
l'`id` differisce da quello in cache. Il file di policy è testo semplice:

```text
version: STSv1
mode: enforce
mx: mx1.example.com
mx: mx2.example.com
max_age: 604800
```

`max_age` è in secondi: $604800 = 7 \times 86400$, cioè sette giorni. Questo numero è il vero parametro di
sicurezza. Un attaccante che blocca o falsifica il TXT *dopo* che il mittente ha già la policy in cache non
ottiene nulla per $T_{cache} = max\_age$ secondi; ma il **primo** contatto resta non protetto (modello TOFU,
Trust On First Use), come ammette l'RFC. Più `max_age` è alto, più a lungo dura la protezione dopo ogni
fetch riuscito, ma più lento è il rollback se sbagli la configurazione.

## L'attacco

Il downgrade si dimostra in laboratorio con un MITM che filtra l'annuncio STARTTLS. Con `nftables` e un
proxy trasparente, oppure più semplicemente con uno script `scapy`/`mitmproxy` che riscrive la risposta
`EHLO`, il client vede questo:

```bash
# server reale
$ nc mx1.example.com 25
220 mx1.example.com ESMTP
EHLO test.local
250-mx1.example.com
250-PIPELINING
250-STARTTLS
250 8BITMIME

# dopo il MITM: STARTTLS è sparito, il mittente prosegue in chiaro
250-mx1.example.com
250-PIPELINING
250 8BITMIME
```

Una seconda variante è il MX falso: l'attaccante avvelena la risposta DNS per `MX example.com` e punta a un
server che presenta un certificato qualsiasi, perché i client SMTP opportunistici di norma **non validano**
il certificato (spesso è autofirmato anche per i server legittimi). Entrambi gli scenari sono invisibili senza
una policy esplicita.

## La difesa

Lato DNS si pubblicano i due record (il secondo abilita TLS-RPT):

```text
_mta-sts.example.com.   IN TXT "v=STSv1; id=20261027T0900"
_smtp._tls.example.com. IN TXT "v=TLSRPTv1; rua=mailto:tlsrpt@example.com"
```

L'host `mta-sts.example.com` deve avere un certificato WebPKI valido e servire il file esattamente su
`/.well-known/mta-sts.txt`. Con nginx:

```nginx {hl_lines=[3,6,9]}
server {
    listen 443 ssl;
    server_name mta-sts.example.com;
    ssl_certificate     /etc/letsencrypt/live/mta-sts.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/mta-sts.example.com/privkey.pem;
    root /var/www/mta-sts;

    location = /.well-known/mta-sts.txt {
        default_type text/plain;
    }
}
```

Il percorso consigliato è graduale: parti con `mode: testing` (i mittenti consegnano comunque ma inviano
report TLS-RPT sui problemi), osserva i report per qualche settimana, poi passa a `mode: enforce` alzando
`max_age` fino a settimane. Ogni volta che cambi la policy devi **cambiare l'`id`** nel TXT, altrimenti i
mittenti continuano a usare la copia in cache.

Per la parte in ricezione basta che i tuoi MX abbiano un certificato valido il cui nome coincida con una
voce `mx:` (sono ammessi wildcard come `*.example.com`). Per la parte in invio, Postfix non implementa
MTA-STS in modo nativo: si usa il demone [postfix-mta-sts-resolver](https://github.com/Snawoot/postfix-mta-sts-resolver)
come `smtp_tls_policy_maps`, che traduce la policy in una regola `secure`/`encrypt` per ogni dominio.

Il report TLS-RPT arriva come JSON compresso: conta sessioni riuscite e fallite, con motivo
(`certificate-expired`, `starttls-not-supported`, `sts-policy-invalid`…). Un picco di
`starttls-not-supported` per un solo mittente è esattamente la firma di un downgrade in corso.

## Lab

Obiettivo: verificare che un dominio di test applichi la policy. Con containerlab crea un mittente Postfix,
un MX e un nodo MITM in mezzo.

1. Pubblica policy `mode: testing` e TXT `_mta-sts` su un dominio di prova.
2. Dal MITM filtra `250-STARTTLS` e invia una mail: consegna avvenuta, ma cosa trovi nei report TLS-RPT?
3. Passa a `mode: enforce`, cambia l'`id` e ripeti. Cosa cambia e perché?

{{< rawhtml >}}
<details><summary>Soluzione</summary>
<p>In <code>testing</code> il mittente consegna comunque in chiaro (la policy è solo osservata) ma al report
successivo trovi un record <code>starttls-not-supported</code> contro il tuo MX: è il segnale che qualcuno,
o qualcosa, ha rimosso l'annuncio. Passando a <code>enforce</code> e cambiando l'<code>id</code>, il mittente
riscarica la policy; ora, non vedendo STARTTLS, rifiuta di consegnare e mette il messaggio in coda con errore
temporaneo, riprovando fino al timeout della coda. Se la causa era un MITM, il messaggio non viene mai
consegnato in chiaro; se era un tuo MX mal configurato, hai appena causato un ritardo di posta: per questo
si osserva sempre prima in <code>testing</code>.</p>
</details>
{{< /rawhtml >}}

## Conclusione

MTA-STS non è perfetto: il primo contatto resta vulnerabile e dipende dalla WebPKI. Ma costa un record DNS,
un file statico e un certificato, e trasforma un downgrade silenzioso in un errore visibile. Abbinalo sempre
a TLS-RPT, parti in `testing`, cambia l'`id` a ogni modifica e valuta DANE se hai già DNSSEC.

**Articoli correlati:** [DANE e TLSA]({{< relref "post/dane-tlsa-dnssec" >}}) ·
[SPF, DKIM e DMARC]({{< relref "post/email-authentication-spf-dkim-dmarc" >}}) ·
[TLS in profondità]({{< relref "post/tls-deep-dive" >}})
