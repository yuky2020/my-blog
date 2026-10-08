# Build con Hugo latest

Type: task
Status: resolved

## Question

Il deploy usa `hugo-version: latest` (oggi v0.167.0). La build passa?

## Answer

No, falliva per due problemi preesistenti. Corretti il 2026-10-08:
- `config/_default/security.toml` con `allowContent = [".*"]` (le pagine `.html` in `content/page/`);
- date `2021-9-29` / `2021-11-7` dei `week_*` con lo zero davanti.
Build locale con v0.167.0: 422 pagine, 0 errori.
Nota: `content/page/code` e `game` non hanno front matter e non generano una pagina propria
(comportamento preesistente).
