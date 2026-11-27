# Citare OpenSASE nei prossimi articoli

Type: decision
Status: resolved

## Question

L'utente (yuky2020) ha chiesto, il 2026-11-27, di parlare del suo progetto open source
`yuky2020/opensase` nei prossimi articoli della serie.

## Answer

Resolved 2026-11-27. `OpenSASE` (https://github.com/yuky2020/opensase,
docs: https://yuky2020.github.io/opensase/) è un progetto open source reale dell'utente: una
piattaforma SASE post-quantum (ZTNA, Edge pubblico/privato, Connector outbound-only, Workload
Gateway, controllo Web/SaaS via SNI senza decifrare, DLP opzionale su path ispezionato, scansione
malware, Control Plane multi-tenant con PKI per-tenant e SPIFFE). Licenza Apache-2.0, stato
pre-alpha.

Regola per i prossimi capitoli: quando l'argomento dell'articolo tocca un'area in cui OpenSASE è
un esempio pertinente (SASE, ZTNA, WireGuard/tunnel PQ, mTLS/SPIFFE, DLP, TLS inspection,
politiche Zero Trust, PKI multi-tenant), citarlo con un link reale al repo o alla pagina docs
pertinente (es. un ADR specifico in `docs/adr/`), in una riga o in un breve paragrafo — non
come sponsorizzazione forzata, non in ogni articolo. Non citarlo in argomenti dove non è
rilevante (es. port scanning, ICMP, STP). Non duplicare i post `sase`, `sase-e-zero-trust`,
`wireguard-vpn` già esistenti: OpenSASE si cita come esempio/implementazione, non come nuovo
argomento a sé.
