---
title: "SELinux"
description: "SELinux aggiunge a Linux il controllo d'accesso obbligatorio: una politica di sistema che nemmeno root può scavalcare, basata su etichette e regole su cosa ogni processo può toccare. Spaventa per la fama di 'cosa che rompe tutto e si disabilita', ma capirne modi, contesti e il flusso di troubleshooting lo rende un alleato potente. Enforcing, context e audit2allow."
slug: "selinux"
date: 2026-05-05T09:00:00+02:00
lastmod: 2026-05-05T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - SELinux
    - MAC
keywords:
    - SELinux
    - mandatory access control
    - enforcing permissive
    - audit2allow
image: "cover.png"
toc: true
links:
  - title: "SELinux Project Wiki"
    description: "Documentazione di riferimento su concetti e strumenti SELinux."
    website: https://github.com/SELinuxProject/selinux/wiki
  - title: "RHEL — Using SELinux"
    description: "Guida pratica all'uso di SELinux su RHEL/Fedora."
    website: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/
---

## Perché conta

Tutto ciò che abbiamo visto finora è **controllo discrezionale**: il proprietario di una risorsa
decide, e root scavalca ogni controllo. Il limite è evidente — se un servizio che gira come root (o un
processo che ottiene root) viene compromesso, il DAC non lo ferma. Il **controllo d'accesso obbligatorio
(MAC)** aggiunge una politica di sistema che vale *sopra* il DAC e che **nemmeno root può aggirare**:
anche se un processo è root, può fare solo ciò che la politica SELinux consente al suo *tipo*. È un
confinamento potentissimo — e la risposta sbagliata, `setenforce 0`, è anche la più diffusa.

## L'idea: etichette e tipi

In SELinux ogni processo e ogni risorsa hanno un'**etichetta (context)**, e la politica definisce quali
interazioni tra etichette sono permesse. Il campo che conta di più è il **type** (type enforcement).

```bash
ls -Z /var/www/html/index.html     # contesto del file
# unconfined_u:object_r:httpd_sys_content_t:s0
#                       ^^^^^^^^^^^^^^^^^^^^ il TYPE: "contenuto web per httpd"
ps -eZ | grep nginx                # contesto del processo
# system_u:system_r:httpd_t:s0 ...  ← il processo web gira nel type httpd_t
```

La politica dice, in sostanza: "un processo `httpd_t` può leggere file `httpd_sys_content_t`". Se il
web server (confinato in `httpd_t`) viene compromesso, **non** può leggere `/etc/shadow`
(`shadow_t`) o scrivere ovunque: la politica glielo vieta, root o no.

## I tre modi

```bash
getenforce                     # Enforcing | Permissive | Disabled
setenforce 1                   # Enforcing: applica la politica (OBIETTIVO)
setenforce 0                   # Permissive: NON applica, ma LOGGA le violazioni (per diagnosi)
```

```text {hl_lines=[2,3]}
Enforcing   → la politica è applicata (produzione)
Permissive  → non blocca ma registra cosa bloccherebbe → usalo per DIAGNOSTICARE, non come resa
Disabled    → SELinux spento (da evitare: perdi anche le etichette)
```

Il riflesso sbagliato è passare a `Disabled` al primo problema. Quello giusto è passare a `Permissive`
*temporaneamente* per vedere *cosa* verrebbe bloccato, capirlo, correggere la politica, e tornare a
`Enforcing`.

## Il troubleshooting che non spaventa

Quando "qualcosa non funziona e sospetto SELinux", il flusso è preciso:

```bash
# 1. le negazioni finiscono nell'audit log
ausearch -m avc -ts recent            # mostra gli Access Vector Cache denial recenti
# 2. sealert spiega in linguaggio umano e suggerisce la soluzione
sealert -a /var/log/audit/audit.log
# 3. spesso basta un booleano o un contesto giusto, non disabilitare tutto
```

Due aggiustamenti coprono la maggioranza dei casi:

```bash
# A) BOOLEANI: interruttori predefiniti per comportamenti comuni
getsebool -a | grep httpd                     # es: httpd_can_network_connect
setsebool -P httpd_can_network_connect on     # -P = persistente

# B) CONTESTI: dare l'etichetta giusta a file in percorsi non standard
semanage fcontext -a -t httpd_sys_content_t "/srv/web(/.*)?"
restorecon -Rv /srv/web                        # riapplica i contesti
```

## Quando serve una regola nuova: audit2allow

Se un'applicazione legittima ha bisogno di un accesso che nessun booleano copre, si genera un **modulo
di policy** dai denial — senza disabilitare nulla.

```bash
ausearch -m avc -ts recent | audit2allow -M myapp_local
semodule -i myapp_local.pp        # installa il modulo: concede SOLO ciò che serviva
```

Attenzione: `audit2allow` va usato con criterio — concedi solo ciò che è davvero legittimo, non tutto
ciò che l'app prova a fare (potrebbe provare anche cose che è giusto bloccare).

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> SELinux ha la fama di rompere le applicazioni e di essere complicatissimo. Visto che ho già DAC stretto, capabilities e sandboxing systemd, non è più pragmatico disabilitarlo e vivere sereni?</summary>
<p>È il ragionamento più comune e anche quello che butta via la protezione più forte proprio quando
servirebbe di più. Partiamo dalla fama: SELinux "rompe le app" quasi sempre perché i file sono nel posto
sbagliato (contesto errato) o manca un booleano — due cose che si diagnosticano in minuti con
<code>ausearch</code> e <code>sealert</code> e si risolvono con un comando, senza disabilitare niente. La
complessità vera (scrivere policy da zero) non ti riguarda nel 95% dei casi: usi la policy mirata della
distribuzione e la ritocchi con booleani e contesti. Ora il punto sostanziale: DAC stretto, capabilities
e sandboxing systemd sono ottimi, ma hanno un limite comune — operano dentro il modello discrezionale e,
soprattutto, dipendono dal fatto che <em>tu</em> li abbia configurati correttamente per ogni servizio.
SELinux aggiunge qualcosa che gli altri non danno: un confinamento <em>obbligatorio</em>, definito a
livello di sistema, che vale anche contro un processo che è diventato root e che resta in piedi anche
dove ti sei dimenticato di sandboxare. Il caso che conta è questo: un servizio ha una vulnerabilità che
permette l'esecuzione di codice e magari un'escalation a root. Il DAC a quel punto non ferma più nulla
(root scavalca tutto), e se quel servizio non l'avevi sandboxato con systemd, l'attaccante è libero. Con
SELinux in enforcing, invece, il processo resta confinato nel suo type: il web server compromesso, anche
da root, non può leggere /etc/shadow né scrivere fuori dalle sue directory, perché la policy non lo
prevede per <code>httpd_t</code>. È esattamente la difesa che interviene quando tutte le altre hanno
ceduto. Disabilitarlo per "vivere sereni" significa rinunciare all'unico strato che un attaccante con
root non può semplicemente aggirare — in cambio di non dover imparare due comandi. Il pragmatismo vero è
tenerlo in enforcing e imparare il flusso di troubleshooting: è molto meno lavoro di quanto la sua fama
suggerisca, e copre proprio lo scenario peggiore.</p>
</details>
{{< /rawhtml >}}

## Conclusione

SELinux impone una politica di sistema che confina ogni processo al suo type e che nemmeno root
scavalca; il segreto è non disabilitarlo ma usare `Permissive` per diagnosticare, booleani e contesti
per correggere, `audit2allow` per i casi residui. Esiste un secondo approccio al MAC, più semplice da
leggere e basato sui percorsi invece che sulle etichette: [AppArmor]({{< relref "post/apparmor" >}}),
prossimo capitolo.
