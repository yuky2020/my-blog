# Serie "Zero Trust in pratica" — mappa

Status: resolved
Obiettivo: nuova serie di ~20 articoli su Zero Trust (richiesta utente 2026-10-08), italiano,
tutte le funzionalità del tema, retrodatati, con cross-link ai post esistenti.

## Decisioni
- 20 capitoli: 00 roadmap (weight:2, in evidenza) + 19 capitoli tematici.
- Lingua italiano; cover generate con scripts/make-cover.py (kicker "Zero Trust · NN").
- Date settimanali di martedì, 2026-05-12 → 2026-09-22 (tutte nel passato → pubblicate).
- Relref ai post esistenti: zero-trust-architecture, network-microsegmentation,
  mtls-service-to-service, sase, siem-log-correlation, network-observability, nac-8021x,
  stateful-firewalls-nftables, ids-ips-suricata, ebpf-network-security, tls-deep-dive,
  vlan-hopping-and-switch-hardening, dns-tunneling-detection, layer2-attacks-arp-spoofing.

## Capitoli (slug)
00 zero-trust-la-serie · 01 zero-trust-i-cinque-principi · 02 oltre-il-perimetro ·
03 identita-il-nuovo-perimetro · 04 mfa-resistente-al-phishing · 05 pdp-pep-il-motore-delle-policy ·
06 microsegmentazione-nello-zero-trust · 07 ztna-oltre-la-vpn · 08 sase-e-zero-trust ·
09 device-trust-e-posture · 10 least-privilege-e-jit · 11 identita-dei-workload-mtls ·
12 spiffe-e-spire · 13 service-mesh-e-zero-trust · 14 policy-as-code-con-opa ·
15 verifica-continua-e-accesso-adattivo · 16 telemetria-e-analytics-zero-trust ·
17 zero-trust-nel-cloud · 18 zero-trust-per-i-dati · 19 migrare-a-zero-trust

## Esito
20 articoli scritti, cover generate, build verde (0 errori). Fix YAML: tre `links[].description`
contenevano ": " non quotato → quotate. Serie autonoma, non nel pool del cron network-security.
