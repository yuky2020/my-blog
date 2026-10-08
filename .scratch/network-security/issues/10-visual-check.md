# Verifica visiva del rendering

Type: task
Status: open

## Question

I diagrammi Mermaid, le formule KaTeX, la galleria, `quote`, `links:` e `<details>` si vedono
correttamente nel browser, in tema chiaro e scuro, anche da telefono? La build passa, ma Mermaid
segnala gli errori di sintassi solo a runtime. Chrome non era collegato, quindi serve l'utente.

Checklist (HITL):
1. `hugo server` acceso, aprire `http://127.0.0.1:1313/p/network-security-roadmap/`
   e `http://127.0.0.1:1313/p/threat-modeling-networks/`.
2. Ogni blocco Mermaid è un diagramma, non un errore o testo grezzo.
3. Le formule `R = P × I` sono rese da KaTeX.
4. Il box `links:` in fondo mostra i 4 link.
5. Il `<details>` si apre e si chiude.
6. Attivare il tema scuro con il toggle: i diagrammi restano leggibili.
7. Homepage: la roadmap è il primo post; la categoria Security ha il badge rosso.
