---
title: "CIS Benchmark e automazione"
description: "Fare hardening una volta a mano non scala e non dura: i sistemi cambiano, se ne aggiungono di nuovi, la configurazione deriva. I CIS Benchmark danno una lista di controlli condivisa e verificabile, e strumenti come Lynis e Ansible la trasformano in qualcosa di misurabile e ripetibile. Come passare dall'hardening artigianale a quello sistematico. La chiusura della serie."
slug: "cis-benchmark-e-automazione"
date: 2026-06-23T09:00:00+02:00
lastmod: 2026-06-23T09:00:00+02:00
categories:
    - Security
    - DevOps
tags:
    - Linux
    - Hardening
    - CIS
    - Automazione
keywords:
    - CIS benchmark
    - lynis
    - ansible hardening
    - hardening automatico
image: "cover.png"
toc: true
links:
  - title: "CIS Benchmarks"
    description: "I benchmark di configurazione sicura per Linux e altri sistemi."
    website: https://www.cisecurity.org/cis-benchmarks
  - title: "Lynis"
    description: "Tool open source di auditing e hardening per sistemi Unix/Linux."
    website: https://cisofy.com/lynis/
---

## Perché conta

Tutti i capitoli precedenti descrivono controlli; applicarli *a mano, una volta sola, su una macchina*
non basta nel mondo reale. I sistemi si moltiplicano, le configurazioni **derivano** nel tempo (qualcuno
cambia qualcosa "al volo"), e senza un metodo non sai se la macchina numero 20 è indurita come la prima.
Servono tre cose: una **lista condivisa** di cosa fare, un modo di **misurare** quanto ci si è vicini, e
un modo di **applicarla in modo ripetibile**. Sono rispettivamente i CIS Benchmark, gli scanner di
auditing e l'automazione.

## I CIS Benchmark: la lista condivisa

I **CIS Benchmark** sono documenti dettagliati, mantenuti dal Center for Internet Security, che elencano
centinaia di controlli di hardening per ogni sistema (Ubuntu, RHEL, Debian...), ciascuno con
motivazione, come verificarlo e come applicarlo. Il valore: non devi *inventare* la lista né rischiare
di dimenticare qualcosa — parti da un riferimento riconosciuto e lo adatti al tuo contesto. Molti dei
temi di questa serie (permessi di `/etc/shadow`, SSH, sysctl, auditd...) sono esattamente controlli CIS.

```text {hl_lines=[2,3]}
Struttura tipica di un controllo CIS:
  - Livello 1: hardening di base, basso impatto sull'operatività
  - Livello 2: più restrittivo, per ambienti ad alta sicurezza (può rompere qualcosa)
  → scegli il livello in base al contesto; non tutto va applicato ovunque
```

## Misurare: Lynis

**Lynis** fa l'audit del sistema e produce un report con un punteggio di hardening e suggerimenti
concreti — un modo rapido di sapere "quanto sono messo" senza controllare tutto a mano.

```bash
apt install lynis       # o dnf install lynis
lynis audit system
# ... Hardening index : 72 [############        ]
# Suggestions: ... (elenco di cosa migliorare, con riferimenti)
```

L'**hardening index** dà un numero da seguire nel tempo: l'obiettivo non è "100" (irrealistico e a volte
controproducente), ma una curva che sale e un report che non contiene sorprese.

## Applicare in modo ripetibile: Ansible

L'automazione trasforma l'hardening da "cosa fatta a mano" a **codice** applicabile a N macchine in modo
identico e ri-applicabile (correggendo la deriva). Esistono ruoli Ansible pronti che implementano i CIS
Benchmark.

```yaml
# esempio: usare un ruolo di hardening CIS in un playbook
- hosts: servers
  become: true
  roles:
    - devsec.hardening.os_hardening     # permessi, sysctl, account...
    - devsec.hardening.ssh_hardening    # sshd_config indurito
```

```bash
ansible-playbook -i inventory hardening.yml --check   # --check: mostra cosa cambierebbe (dry-run)
ansible-playbook -i inventory hardening.yml           # applica
```

Il vantaggio è doppio: applichi la *stessa* configurazione a tutta la flotta, e rieseguendo il playbook
riporti allo stato voluto qualunque macchina sia derivata — è il principio della [configurazione come
codice]({{< relref "post/iac-sicuro-policy-as-code" >}}) applicato all'hardening del sistema operativo.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se applico un ruolo CIS pronto con Ansible, non è un modo per indurire senza capire nulla — e quindi il contrario di tutta questa serie, che insisteva sul perché?</summary>
<p>È il rischio reale di ogni automazione — applicare regole a scatola chiusa — ma il modo giusto di
usarla è esattamente l'opposto: l'automazione <em>presuppone</em> la comprensione, non la sostituisce, ed
è qui che tutta la serie ripaga. Un ruolo CIS applicato senza capire cosa fa produce due disastri
prevedibili. Primo, <em>rompe cose e non sai perché</em>: molti controlli CIS di livello 2 disabilitano
funzioni, stringono permessi, cambiano SSH — se non capisci cosa stai applicando, un servizio smette di
funzionare e sei bloccato, con la tentazione di disattivare tutto. Secondo, <em>applichi controlli
inadatti al tuo contesto</em>: non ogni regola ha senso ovunque (un benchmark per workstation differisce
da uno per server esposto), e scegliere il livello e le eccezioni richiede di sapere cosa ti serve
davvero. La comprensione costruita nei capitoli precedenti è ciò che ti permette di usare l'automazione
<em>bene</em>: leggi il ruolo e riconosci i controlli (ah, questo è il sysctl rp_filter, questo è
PermitRootLogin no, questo monta /tmp nosuid), capisci perché ci sono, decidi quali attivare e quali
derogare con cognizione, e quando qualcosa si rompe sai diagnosticarlo invece di arrenderti. L'automazione
risolve il problema dello <em>scalare e del non derivare</em> — applicare la stessa cosa a 50 macchine,
ripristinare lo stato voluto — che è un problema diverso e complementare rispetto al <em>sapere cosa
applicare</em>. Chi capisce ma fa tutto a mano non scala; chi automatizza senza capire costruisce un
castello che crolla al primo imprevisto e non sa rialzarlo. L'obiettivo della serie era darti il primo
pezzo proprio perché il secondo, da solo, è fragile. Automatizza — ma automatizza ciò che capisci.</p>
</details>
{{< /rawhtml >}}

## Conclusione

I CIS Benchmark danno la lista condivisa, Lynis la misura, Ansible la applica in modo ripetibile su
tutta la flotta correggendo la deriva: così l'hardening diventa sistematico invece che artigianale. Qui
si chiude **Linux Hardening in pratica**: dal [modello di permessi del
kernel]({{< relref "post/modello-sicurezza-linux" >}}) fino all'automazione, con un filo conduttore
costante — privilegio minimo, superficie minima, visibilità — e un principio di metodo: ogni controllo
ha un *perché*, e capirlo è ciò che distingue un sistema indurito da una checklist spuntata. Per
ripartire dall'inizio, torna alla [roadmap della serie]({{< relref "post/linux-hardening-la-serie" >}}).
