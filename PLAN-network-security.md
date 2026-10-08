# Piano contenuti: Network Security

## 1. Com'è fatto il blog oggi

**Tema:** Hugo Stack v3.34.0 (Hugo module). Permalink `post = /p/:slug/`.

**Struttura degli articoli recenti (40+ post datati 2026-01-25):**
- page bundle: `content/post/<slug>/index.md` + `images/1.png` come cover
- front matter YAML: `title`, `description`, `slug`, `date`, `categories`, `tags`, `image`
- corpo: `## Introduction` → 3–5 sezioni `##` → `## Conclusion`, liste puntate, 40–80 righe
- in inglese

**Cosa manca:** niente codice, niente diagrammi, niente formule, niente link esterni o fonti, niente
collegamenti tra post. Tutti hanno la stessa data. È questo che rende il contenuto piatto, ed è
quello che i nuovi post devono correggere.

**Post di security già presenti (da non duplicare, ma da linkare):**
`bgp-security-rpki`, `zero-trust-architecture`, `network-security-mesh-architecture`, `sase`,
`wireguard-vpn`.

## 2. Funzionalità di Stack da usare (tutte)

| Funzionalità | Come si usa | Stato oggi |
|---|---|---|
| Cover image | `image: cover.png` nel front matter | usata |
| Indice (TOC) | widget già attivo; `toc: true/false` per post | attivo, mai regolato |
| Tempo di lettura | `readingTime` | attivo |
| Diagrammi Mermaid | blocco ` ```mermaid ` (render hook del tema, Mermaid 11) | **mai usato** |
| Formule KaTeX | `math: true` (già globale) + `$...$` / `$$...$$` | **mai usato** |
| Codice evidenziato | blocchi ` ```bash `, numeri di riga già attivi; `{hl_lines=[3,5]}` | quasi mai |
| Galleria immagini | più immagini **sulla stessa riga/paragrafo** → galleria PhotoSwipe | mai |
| Shortcode `quote` | `{{< quote author="" source="" url="" >}}` | mai |
| Shortcode `youtube` / `video` | `{{< youtube ID >}}`, `{{< video src="..." >}}` | solo post vecchi |
| Shortcode `gitlab` | snippet incorporato | mai |
| `rawhtml` (locale) | `<details>` per soluzioni/spoiler, visto che `unsafe = false` | mai |
| Link esterni | `links:` nel front matter (titolo, sito, descrizione, immagine) → box in fondo | **mai usato** |
| Contenuti correlati | `related.toml` su tag/categorie → serve un tagging coerente | tag sparsi |
| Pagina categoria | `content/categories/security/_index.md` con `style.background/color`, `image`, `description` | assente |
| Licenza per post | `license:` sovrascrive CC BY-NC-SA | mai |
| Commenti per post | `comments: false` dove serve | mai |
| Ultimo aggiornamento | `lastmod:` (oppure `enableGitInfo`) → mostra "Last updated" | mai |
| Post fissati | `weight: 1` porta in cima il pillar | mai |
| Keywords / SEO | `keywords:` + `description` | parziale |
| Ricerca / archivi / tag cloud | widget già attivi, si popolano da soli | ok |

## 3. Tassonomia

- **Categorie** (max 2 per post): `Security` + una tra `Networking`, `Hands-on`.
- **Tag controllati** (riusarli sempre identici, sono loro a guidare i "Related"):
  `Network Security`, `Firewall`, `IDS/IPS`, `TLS`, `DNS Security`, `VPN`, `Zero Trust`,
  `Threat Modeling`, `Packet Analysis`, `Hardening`, `Linux`, `Attacks`.
- Creare `content/categories/security/_index.md` con colore dedicato e descrizione.

## 4. Serie: "Network Security dal cavo in su" (12 post, in italiano)

Il post 0 è il pillar (fissato in cima), gli altri lo linkano e ne sono linkati.

| # | Slug | Taglio | Funzionalità protagoniste |
|---|---|---|---|
| 0 | `network-security-roadmap` | Pillar: mappa della serie, modello a strati | `weight: 1`, Mermaid mindmap, `links:` a tutti i post, `quote` |
| 1 | `threat-modeling-networks` | STRIDE applicato a una rete reale | Mermaid flowchart (trust boundary), tabella, `<details>` esercizio |
| 2 | `layer2-attacks-arp-spoofing` | ARP spoofing, MAC flooding, DHCP starvation + difese | Mermaid sequenceDiagram, codice `scapy`, galleria screenshot Wireshark |
| 3 | `vlan-hopping-and-switch-hardening` | Double tagging, DTP, port security | codice config switch con `hl_lines`, Mermaid |
| 4 | `stateful-firewalls-nftables` | Da iptables a nftables, conntrack | codice `nft` lungo con righe evidenziate, Mermaid stateDiagram (stati conntrack) |
| 5 | `ids-ips-suricata` | Suricata in lab, scrittura regole | codice regole, galleria dashboard, `youtube` demo, `links:` |
| 6 | `tls-deep-dive` | Handshake TLS 1.3, PKI, cert pinning | Mermaid sequenceDiagram, **KaTeX** (ECDHE), `openssl` CLI |
| 7 | `dns-security-dnssec-doh` | Poisoning, DNSSEC, DoH/DoT | Mermaid chain of trust, `dig` output, `quote` da RFC |
| 8 | `ddos-anatomy-and-mitigation` | Volumetrici vs L7, amplificazione | **KaTeX** fattore di amplificazione, grafici come galleria, tabella |
| 9 | `ipsec-vs-wireguard` | Confronto, lega a `wireguard-vpn` | tabella confronto, Mermaid, codice config, `links:` |
| 10 | `packet-analysis-wireshark` | Hands-on: trovare un attacco in un pcap | galleria, `<details>` soluzioni, `video` o `youtube` |
| 11 | `building-a-security-homelab` | Lab completo (pfSense/OPNsense, Suricata, VLAN) | Mermaid topologia, galleria foto, `gitlab`/repo, `license:` diversa per i file di config |

Ordine di pubblicazione: 0 → 1 → 2 … uno a settimana, `date` reali e distinte; `lastmod`
quando un post viene aggiornato.

## 5. Template per ogni nuovo post

```yaml
---
title: "..."
description: "..."            # 1 frase, usata anche per SEO/OpenGraph
slug: "..."
date: 2026-10-XXT10:00:00+02:00
lastmod: 2026-10-XXT10:00:00+02:00
categories: [Security, Networking]
tags: [Network Security, ...]   # solo dalla lista controllata
keywords: [...]
image: "cover.png"
toc: true
math: false                     # true solo dove serve
links:
  - title: "RFC ..."
    description: "..."
    website: "https://..."
---
```

Corpo:
1. Hook + perché conta (2–3 paragrafi)
2. Come funziona → **diagramma Mermaid**
3. L'attacco → codice/comandi reali
4. La difesa → configurazione reale con righe evidenziate
5. Lab / esercizio → soluzione in `<details>` via `rawhtml`
6. Conclusione + "Next in the series" (link al post successivo e al pillar)

## 6. Lavoro preliminare (prima del primo post)

1. `categories/security/_index.md` con colore e cover.
2. Configurare `enableGitInfo = true` (lastmod automatico) — opzionale.
3. Verificare che Mermaid e KaTeX rendano: un post di prova in `draft: true`.
4. Installare Hugo extended in locale per `hugo server` (ora non è installato).
5. Archetype `archetypes/post.md` con il template sopra, così `hugo new post/<slug>/index.md` lo usa.

## 7. Decisioni (2026-10-08)

- **Lingua:** italiano. Titoli, descrizioni e corpo in italiano; i termini tecnici restano in
  inglese (es. "handshake", "conntrack"). Slug in inglese per URL stabili. I tag della lista
  controllata restano quelli in inglese, così si collegano ai post esistenti.
- **Cover:** generate, tutte con lo stesso stile (stessa palette, stesso layout, icona del tema
  del post), salvate come `cover.png` 1600×900 nel bundle.
- **Commenti:** si resta su Disqus (`matteobianchi-eu`), nessuna modifica.
