# 17 — Articoli extra, secondo lotto

Status: resolved
Type: task

## Obiettivo

Dopo il primo lotto di extra (ticket 16), scrivere altri articoli di network security fuori dalla
serie numerata, su argomenti non ancora coperti, in italiano e con tutte le funzionalità del tema.

## Esito

5 articoli scritti, build verde (0 errori), tutti con cover generata, Mermaid, code `hl_lines`,
`<details>`, `links:` e cross-link `relref` verso i capitoli esistenti. Retrodatati (ago–set 2026)
per essere già pubblicati.

- **DHCP snooping e Dynamic ARP Inspection** (2026-08-22) — complementa il cap. 02 (L2) e NAC.
- **SPF, DKIM e DMARC** (2026-08-29) — email auth, si lega a DNS security.
- **Microsegmentazione della rete** (2026-09-05) — movimento laterale, Zero Trust, NetworkPolicy k8s.
- **SIEM e correlazione dei log** (2026-09-12) — detection, Sigma, ATT&CK; si lega a IDS/IPS.
- **DNS tunneling e rilevamento** (2026-09-19) — canale nascosto C2/esfiltrazione; KaTeX per l'entropia.

Totale articoli network security sul blog: 22.

Nota: fuori dal pool del cron, che controlla i post esistenti ed evita duplicati.
