---
title: "Hardening di SSH"
description: "SSH è la porta principale di ogni server e il bersaglio costante dei bruteforce automatici. Passare all'autenticazione a chiave, disabilitare login root e password, restringere chi può entrare e irrobustire gli algoritmi trasforma la porta più attaccata nella più solida. La configurazione sshd_config completa, spiegata riga per riga."
slug: "hardening-ssh"
date: 2026-02-17T09:00:00+01:00
lastmod: 2026-02-17T09:00:00+01:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - SSH
keywords:
    - ssh hardening
    - sshd_config
    - autenticazione a chiave
    - disable root login
image: "cover.png"
toc: true
links:
  - title: "man 5 sshd_config"
    description: "Tutte le direttive di configurazione del server SSH."
    website: https://man7.org/linux/man-pages/man5/sshd_config.5.html
  - title: "Mozilla — OpenSSH Guidelines"
    description: "Configurazioni consigliate per algoritmi e cifrari SSH."
    website: https://infosec.mozilla.org/guidelines/openssh
---

## Perché conta

Apri un server su Internet e in pochi minuti vedrai nei log tentativi di login SSH da indirizzi di
tutto il mondo: bot che provano `root`/`admin` con password comuni, senza sosta. SSH è la porta
principale e il bersaglio costante. La buona notizia: irrobustirlo è tra gli interventi col miglior
rapporto sforzo/beneficio. L'idea guida è eliminare ciò che i bot attaccano — le password — e ridurre
chi e come può entrare.

## Il passo decisivo: solo chiavi

Una chiave Ed25519 non si indovina con il bruteforce come una password. Genera la coppia sul tuo
client, installa la pubblica sul server, verifica di poter entrare, *poi* disabilita le password.

```bash
# sul CLIENT
ssh-keygen -t ed25519 -C "matteo@laptop"
ssh-copy-id -i ~/.ssh/id_ed25519.pub matteo@server
ssh matteo@server    # verifica che la chiave funzioni PRIMA di togliere le password
```

## sshd_config, riga per riga

Metti le direttive in un drop-in dedicato (`/etc/ssh/sshd_config.d/hardening.conf`) così
aggiornamenti e pacchetti non le sovrascrivono:

```text {hl_lines=[2,3,4,7]}
# /etc/ssh/sshd_config.d/10-hardening.conf
PermitRootLogin no               # root non entra mai direttamente: si usa sudo
PasswordAuthentication no        # niente password: solo chiavi
KbdInteractiveAuthentication no  # chiude anche la via "interattiva" alle password
PubkeyAuthentication yes
AuthenticationMethods publickey
AllowUsers matteo deploy         # SOLO questi utenti possono fare SSH (whitelist)
MaxAuthTries 3                   # pochi tentativi per connessione
LoginGraceTime 20                # 20s per autenticarsi, poi chiude
X11Forwarding no                 # disattiva ciò che non usi
AllowAgentForwarding no
```

`PermitRootLogin no` e `PasswordAuthentication no` da soli azzerano la quasi totalità dei bruteforce.
`AllowUsers` è potente: anche se un account di servizio avesse una password debole, non è nella lista,
quindi SSH lo rifiuta a priori.

## Algoritmi moderni

Limita cifrari e scambio di chiavi a quelli robusti (evita algoritmi legacy):

```text
# stesso file drop-in
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com
```

## Applicare in sicurezza

**Non chiuderti fuori.** Valida la configurazione e tieni una sessione aperta mentre ne apri una nuova
per provare.

```bash
sshd -t                      # valida la sintassi: se stampa errori, NON riavviare
systemctl reload sshd        # applica senza buttare giù le connessioni attive
# poi, da un ALTRO terminale: ssh matteo@server  → se funziona, sei a posto
```

## Difese di contorno

```text {hl_lines=[1,3]}
- fail2ban / sshguard: bannano gli IP dopo N tentativi falliti (meno rumore nei log)
- cambiare la porta 22: NON è sicurezza, riduce solo il rumore degli scanner
- limitare SSH al firewall: accettare la 22 solo da reti fidate (vedi cap. nftables)
- 2FA con PAM: aggiungere un secondo fattore (TOTP) oltre alla chiave (vedi cap. PAM)
```

Nota onesta: cambiare porta e fail2ban **riducono il rumore**, non sostituiscono le chiavi. La vera
sicurezza è "niente password + whitelist utenti + chiavi forti".

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> se uso già fail2ban che banna i bruteforce e cambio la porta SSH, i bot non mi trovano e non insistono. Serve davvero disabilitare le password e passare alle chiavi?</summary>
<p>Sì, perché fail2ban e la porta non standard risolvono il <em>sintomo</em> (il rumore dei bot di massa)
ma non la <em>vulnerabilità</em> (una password indovinabile resta indovinabile). Sono difese utili come
contorno, non come sostituti, e la differenza emerge appena l'attaccante non è un bot stupido. La porta
diversa dalla 22 ferma solo gli scanner pigri: chi ti prende di mira fa un port scan e trova il servizio
SSH in pochi secondi, qualunque porta tu usi — è security by obscurity, abbassa il rumore di fondo ma non
l'attaccante mirato. fail2ban banna dopo N tentativi, ma non protegge da un attacco lento e distribuito
(pochi tentativi da molti IP, sotto la soglia), né da una password che compare in un leak e viene provata
una volta sola, con successo, senza mai scattare il ban. Soprattutto, entrambi presuppongono che esista
ancora qualcosa da indovinare: finché le password sono abilitate, la sicurezza del tuo server dipende
dalla password più debole tra tutti gli account abilitati — incluso magari un account di servizio o di
test che hai dimenticato. Passare alle chiavi elimina il problema alla radice: una chiave Ed25519 non si
indovina con la forza bruta in tempi umani, quindi i tentativi di login con password semplicemente non
possono riuscire, bannati o no. A quel punto fail2ban e la porta diventano quello che devono essere —
riduzione del rumore sopra una base già solida — invece dell'unica cosa che ti separa da una
compromissione. L'ordine giusto è: prima togli ciò che si può indovinare (password), poi aggiungi il
contorno. Non il contrario.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Chiavi al posto delle password, niente root diretto, whitelist di utenti, algoritmi moderni e un reload
validato: SSH passa da porta più attaccata a porta più solida. SSH è un consumatore del sistema di
autenticazione sottostante; per il secondo fattore, le policy password e il blocco dopo troppi
tentativi, bisogna scendere al livello che governa *come* Linux autentica: [PAM]({{< relref
"post/autenticazione-pam" >}}), prossimo capitolo.
