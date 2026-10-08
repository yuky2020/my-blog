# Cosa entra nel repo

Type: grilling
Status: resolved

## Question

Nel working tree ci sono file nuovi che non sono contenuti del blog: `.agents/` e `.claude/skills/`
(38 skill installate nel progetto), `.scratch/` (questa mappa), `PLAN-network-security.md`,
`scripts/make-cover.py`. Quali vanno in commit, quali in `.gitignore`, quali spostati fuori dal repo?
Nota: tutto ciò che sta in `content/`, `static/` e `assets/` finisce online; questi file no.

## Answer

Resolved 2026-10-08 (scelta utente: commit e push ora).
- In commit: contenuti (`content/`), `config/`, `archetypes/`, `scripts/`, `PLAN-network-security.md`,
  e la mappa wayfinder `.scratch/` (serve all'agente cloud che la fa avanzare).
- In `.gitignore` (locali, non contenuti): `.agents/`, `.claude/`, `skills-lock.json`, `.hugo_build.lock`.
