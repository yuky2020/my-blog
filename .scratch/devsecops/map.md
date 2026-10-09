# Serie "DevSecOps in pratica" — mappa

Status: resolved
Obiettivo: serie di 30 capitoli su DevSecOps (richiesta utente 2026-10-09), italiano,
tutte le funzionalità del tema, retrodatati (martedì 2026-03-10 → 2026-09-29), cross-link
ai post esistenti. Richiesta: "fai 30 articoli e pubblicali" → tema scelto: DevSecOps.

## Decisioni
- 30 capitoli: 00 roadmap (weight:2, in evidenza) + 29 capitoli tematici, ordine narrativo
  shift-left: cultura → design → build → artefatti → deploy → runtime → operate → cultura.
- Lingua italiano; cover generate con scripts/make-cover.py (kicker "DevSecOps · NN").
- Date settimanali di martedì, 2026-03-10 → 2026-09-29 (tutte nel passato → pubblicate).
- Cap. 24 usa math:true (KaTeX) per CVSS/EPSS.

## Relref ai post esistenti
threat-modeling-networks, policy-as-code-con-opa, ebpf-network-security,
kubernetes-networking-model, container-networking, identita-dei-workload-mtls,
spiffe-e-spire, siem-log-correlation, ssh-hardening, least-privilege-e-jit,
zero-trust-la-serie, telemetria-e-analytics-zero-trust, mtls-service-to-service.

## Capitoli (slug)
00 devsecops-la-serie · 01 cos-e-devsecops · 02 secure-sdlc ·
03 threat-modeling-nel-ciclo · 04 gestione-dei-segreti · 05 sast-analisi-statica ·
06 sca-e-dipendenze · 07 dast-analisi-dinamica · 08 iast-e-rasp · 09 fuzzing ·
10 sbom-trasparenza · 11 supply-chain-slsa · 12 firma-artefatti-sigstore ·
13 sicurezza-pipeline-ci-cd · 14 iac-security · 15 policy-as-code-pipeline ·
16 container-image-security · 17 kubernetes-hardening · 18 admission-control ·
19 runtime-security-falco · 20 secrets-in-kubernetes · 21 identita-workload-pipeline ·
22 dependency-patch-management · 23 security-gates · 24 vulnerability-management-triage ·
25 logging-detection-pipeline · 26 incident-response-devsecops · 27 compliance-as-code ·
28 metriche-devsecops · 29 cultura-security-champions

## Esito
30 articoli scritti (00 roadmap weight:2 + 29 capitoli), cover generate, build verde (exit 0),
30/30 resi, KaTeX ok nei cap. 24 e 28, Mermaid e <details> in tutti. Serie autonoma.
