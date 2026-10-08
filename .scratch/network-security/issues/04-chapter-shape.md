# Schema e funzionalità dei capitoli

Type: task
Status: resolved

## Question

Quale struttura e quali funzionalità di Stack usa ogni capitolo?

## Answer

Definito in `PLAN-network-security.md`, sezioni 2–5:
- schema: perché conta, come funziona (Mermaid), attacco (codice), difesa (config con `hl_lines`),
  lab (`<details>` con `rawhtml`), conclusione con "Prossimo nella serie";
- front matter: `links:`, `keywords`, `toc`, `math` dove serve, `lastmod`;
- tag solo dalla lista controllata; categorie `Security` + `Networking`;
- `archetypes/post.md` e `content/categories/security/_index.md` creati.
