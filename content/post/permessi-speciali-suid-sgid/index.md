---
title: "Permessi speciali: SUID, SGID, sticky"
description: "Tre bit che cambiano le regole: SUID fa eseguire un programma con i privilegi del proprietario (spesso root), SGID con quelli del gruppo, lo sticky bit protegge le directory condivise. Il SUID è potente e pericoloso: un binario SUID-root vulnerabile è una scalata a root pronta. Come trovarli, capirli e ridurli."
slug: "permessi-speciali-suid-sgid"
date: 2026-02-03T09:00:00+01:00
lastmod: 2026-02-03T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - SUID
keywords:
    - SUID
    - SGID
    - sticky bit
    - privilege escalation
image: "cover.png"
toc: true
links:
  - title: "GTFOBins"
    description: "Catalogo di binari Unix abusabili per escalation, utile per capire il rischio SUID."
    website: https://gtfobins.github.io/
  - title: "man 2 setuid"
    description: "Come un processo cambia il proprio UID effettivo."
    website: https://man7.org/linux/man-pages/man2/setuid.2.html
---

## Perché conta

I [permessi normali]({{< relref "post/permessi-dei-file" >}}) decidono *chi accede* a un file. I
permessi speciali cambiano *con quali privilegi gira* un programma — ed è qui che nascono le scalate a
root. Un binario **SUID-root** viene eseguito con i poteri di root *da chiunque* lo lanci: se quel
binario ha una falla, chiunque può sfruttarla per diventare root. È per questo che l'inventario dei
SUID è uno dei primi controlli di un pentester — e deve essere uno dei tuoi.

## I tre bit

```text {hl_lines=[2,3]}
SUID (4000): il processo gira con l'UID del PROPRIETARIO del file, non di chi lo lancia
SGID (2000): gira con il GID del gruppo del file (sui file); eredita il gruppo (sulle dir)
Sticky (1000): in una dir condivisa, solo l'owner di un file può cancellarlo (es. /tmp)
```

Nell'output di `ls` appaiono al posto della `x`:

```bash
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ...   la 's' al posto della x dell'owner = SUID
#    ^
ls -ld /tmp
# drwxrwxrwt ... la 't' finale = sticky bit
```

`passwd` **deve** essere SUID-root: un utente normale lo lancia, ma deve scrivere in `/etc/shadow`
(di root). Il SUID è il meccanismo che glielo consente in modo controllato — il problema è quando è
applicato a binari che non ne hanno bisogno.

## Trovarli tutti

```bash
# inventario completo dei SUID e SGID sul sistema
find / -xdev \( -perm -4000 -o -perm -2000 \) -type f -exec ls -l {} \; 2>/dev/null
```

Confronta la lista con ciò che ti aspetti. I SUID-root legittimi sono pochi e noti: `passwd`, `su`,
`sudo`, `mount`, `ping` (sulle distro più vecchie), `pkexec`. **Tutto il resto va messo in
discussione.**

## Perché un SUID di troppo è una scalata a root

Il rischio concreto: molti programmi comuni, se SUID-root, permettono di eseguire comandi arbitrari con
i privilegi di root. Il catalogo **GTFOBins** documenta esattamente questo. Esempio classico: se `find`
fosse SUID-root (non lo è di default, ma capita per errore)…

```bash
# SE find è SUID-root, questa riga dà una shell di root a chiunque:
find . -exec /bin/sh -p \; -quit
```

Non è una falla di `find`: è il SUID messo dove non serve. La lezione: **ogni bit SUID è una delega di
privilegi**, e va trattato con lo stesso sospetto di un account con poteri di root.

## Ridurre e togliere

```bash
# togliere il SUID da un binario che non ne ha bisogno
chmod u-s /percorso/al/binario

# montare le partizioni dati con nosuid: i bit SUID lì vengono IGNORATI dal kernel
#  /etc/fstab:
#  /dev/sdb1  /data  ext4  defaults,nosuid,nodev,noexec  0 2
```

L'opzione di mount **`nosuid`** è una difesa forte: su partizioni che contengono solo dati (`/home`,
`/tmp`, `/data`), dice al kernel di ignorare qualsiasi bit SUID. Così, anche se un attaccante riesce a
depositare lì un binario SUID-root, non gli serve a nulla. Insieme a `nodev` e `noexec` è una tripletta
classica dell'hardening del filesystem.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> i binari SUID del sistema li ha messi la distribuzione e sono testati da anni. Perché preoccuparsi: non è paranoia inventariarli e montare mezzo sistema con nosuid?</summary>
<p>I SUID della distribuzione sono il <em>caso buono</em>, ed è vero che sono pochi, noti e rivisti; il
rischio non viene da loro ma da tutto ciò che si aggiunge intorno, e l'inventario serve proprio a
separare i due. Primo, il software di terze parti: pacchetti esterni, installer manuali, build custom e
vecchi programmi aggiungono i propri SUID, a volte senza che tu te ne accorga, e quelli non hanno gli
anni di revisione dei binari core. Un solo SUID-root scritto male è una scalata a root pronta per
chiunque abbia già un accesso non privilegiato — ed è esattamente così che un attaccante trasforma un
accesso limitato (un web server compromesso, un account rubato) in controllo totale. Secondo, anche i
SUID legittimi hanno avuto vulnerabilità gravi reali: pensa a pkexec, sudo, o ad altri binari di sistema
che negli anni hanno avuto CVE di escalation a root — "testato da anni" non significa "immune", significa
"finora". Non puoi fare molto contro una CVE in sudo se non aggiornare, ma puoi ridurre il resto della
superficie. Terzo, l'inventario non è paranoia, è <em>baseline</em>: la lista dei SUID del tuo sistema
dovrebbe essere corta e stabile, così quando ne compare uno nuovo lo noti — e un SUID-root apparso dal
nulla è un segnale classico di compromissione (un attaccante che si lascia una backdoor di persistenza).
Sul nosuid: non monti "mezzo sistema" così, monti le partizioni di <em>soli dati</em> dove un SUID non ha
alcuna ragione legittima di esistere; i binari di sistema stanno in <code>/usr</code>, che resta normale.
È una difesa quasi gratuita che annulla un'intera tecnica di attacco (depositare un SUID in /tmp o /home).
Il costo è un comando di inventario ogni tanto e tre parole in fstab; il beneficio è chiudere la via di
escalation più diretta che esista.</p>
</details>
{{< /rawhtml >}}

## Conclusione

SUID e SGID cambiano i privilegi d'esecuzione: potentissimi dove servono (pochi binari), pericolosi
ovunque altro. Inventariali, togli quelli inutili, e monta le partizioni dati con `nosuid,nodev,noexec`.
Il SUID è un modo *implicito* di dare privilegi; esiste anche un modo *esplicito* e controllato di farlo
— concedere a una persona il potere di eseguire comandi da root in modo tracciato: è
[sudo]({{< relref "post/sudo-ed-escalation" >}}), prossimo capitolo.
