---
title: "Kernel hardening con sysctl"
description: "Il kernel espone centinaia di parametri che cambiano il comportamento di rete e memoria, e alcuni contano per la sicurezza: protezioni anti-spoofing, difese contro link malevoli, restrizioni su ptrace e dmesg, ASLR. Un file sysctl commentato con le impostazioni di hardening che vale la pena applicare, e cosa fa ciascuna. Più il blocco dei moduli kernel inutili."
slug: "kernel-hardening-sysctl"
date: 2026-06-16T09:00:00+02:00
lastmod: 2026-06-16T09:00:00+02:00
categories:
    - Security
tags:
    - Linux
    - Hardening
    - Kernel
keywords:
    - sysctl hardening
    - kernel hardening
    - ASLR
    - module blacklist
image: "cover.png"
toc: true
links:
  - title: "man 8 sysctl"
    description: "Lettura e scrittura dei parametri del kernel a runtime."
    website: https://man7.org/linux/man-pages/man8/sysctl.8.html
  - title: "Kernel Self Protection Project"
    description: "Linee guida sulle protezioni del kernel Linux."
    website: https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project
---

## Perché conta

Il kernel è il cuore del sistema, e molti suoi comportamenti si regolano con i parametri **sysctl**.
Alcuni sono rilevanti per la sicurezza: come tratta pacchetti sospetti, quanto protegge la memoria dei
processi, quanto espone ai processi non privilegiati. I default sono scelti per compatibilità, non per
massima sicurezza — e irrobustirli costa un file di configurazione. Non è il primo intervento da fare
(gli accessi e i servizi vengono prima), ma è un completamento solido.

## Come si applicano

```bash
sysctl net.ipv4.ip_forward            # leggi un parametro
sysctl -w kernel.kptr_restrict=2      # imposta a runtime (temporaneo)
# persistente: metti le righe in /etc/sysctl.d/*.conf
sysctl --system                       # ricarica tutti i file sysctl.d
```

## Un file di hardening commentato

```text {hl_lines=[3,8,12,15,18]}
# /etc/sysctl.d/99-hardening.conf

# --- Rete: anti-spoofing e pacchetti sospetti ---
net.ipv4.conf.all.rp_filter = 1            # reverse path filter: scarta pacchetti con sorgente impossibile
net.ipv4.conf.all.accept_redirects = 0     # ignora ICMP redirect (possibile MITM)
net.ipv6.conf.all.accept_redirects = 0
net.ipv4.conf.all.accept_source_route = 0  # scarta pacchetti con source routing
net.ipv4.conf.all.log_martians = 1         # logga pacchetti con indirizzi impossibili
net.ipv4.tcp_syncookies = 1                # difesa contro i SYN flood

# --- Memoria e processi ---
kernel.randomize_va_space = 2              # ASLR pieno: randomizza gli indirizzi (ostacola exploit)
kernel.kptr_restrict = 2                   # nascondi gli indirizzi del kernel (/proc, dmesg)
kernel.dmesg_restrict = 1                  # solo root legge il ring buffer del kernel
kernel.yama.ptrace_scope = 1               # un processo non può ispezionarne un altro a piacere
kernel.unprivileged_bpf_disabled = 1       # niente eBPF per utenti non privilegiati
kernel.kexec_load_disabled = 1             # impedisci di caricare un altro kernel a runtime

# --- Filesystem ---
fs.protected_symlinks = 1                  # difesa da attacchi via link simbolici in dir condivise
fs.protected_hardlinks = 1
fs.suid_dumpable = 0                        # i processi SUID non generano core dump (fuga di segreti)
```

Ciascuna chiude una porta: `rp_filter` e `accept_redirects=0` ostacolano spoofing e MITM;
`randomize_va_space=2` (ASLR) rende gli exploit di memoria molto più difficili; `ptrace_scope=1`
impedisce che un processo compromesso ispezioni la memoria di un altro (es. per rubare segreti);
`protected_symlinks` neutralizza una classe classica di attacchi nelle directory world-writable come
`/tmp`.

## Bloccare i moduli kernel inutili

Ogni modulo kernel caricabile è codice che gira nel contesto più privilegiato. Moduli per protocolli o
filesystem esotici che non usi sono superficie d'attacco inutile: si possono mettere in blacklist.

```text {hl_lines=[2,3]}
# /etc/modprobe.d/blacklist-hardening.conf
install dccp /bin/true          # protocolli di rete rari e storicamente bacati
install sctp /bin/true
install firewire-core /bin/true # interfacce DMA = rischio con accesso fisico
install usb-storage /bin/true   # SOLO se non ti servono chiavette USB (es. server)
```

`install <modulo> /bin/true` fa sì che il tentativo di caricare il modulo non faccia nulla. Utile per
protocolli obsoleti (dccp, sctp, rds) che hanno avuto CVE e che quasi nessuno usa.

## Verificare

```bash
sysctl -a 2>/dev/null | grep -E 'randomize_va_space|rp_filter|ptrace_scope'
lsmod                              # moduli attualmente caricati
```

## Conclusione

Un file sysctl di hardening — anti-spoofing, ASLR pieno, restrizioni su ptrace/dmesg, protezione dei
symlink — più la blacklist dei moduli inutili, irrobustiscono il livello più profondo del sistema a
costo quasi nullo. Abbiamo coperto l'intero stack, dagli account al kernel; resta da rendere tutto
questo **ripetibile e verificabile** invece che manuale. È il [CIS Benchmark e
l'automazione]({{< relref "post/cis-benchmark-e-automazione" >}}), capitolo che chiude la serie.
