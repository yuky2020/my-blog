# Wayfinder map: Network Security dal cavo in su

Label: wayfinder:map

## Destination

Serie di 12 post in italiano sulla network security pubblicata su matteobianchi.eu: ogni capitolo
segue lo schema del piano e usa le funzionalità di Stack previste, la build Hugo locale è verde
e il lavoro è in push sul repo.

## Notes

- Dominio: contenuti per un blog Hugo (tema Stack v3.34, Hugo module). Spec di partenza:
  [PLAN-network-security.md](../../PLAN-network-security.md).
- **Esecuzione dentro la mappa**: per scelta dell'utente questa mappa non si ferma alle decisioni.
  I ticket `task` comprendono anche la scrittura dei capitoli, un capitolo per ticket e per sessione.
- Skill da consultare: `grilling` + `domain-modeling` per i ticket HITL, `research` per i ticket research,
  `caveman` per lo stile delle risposte in chat (non per i post).
- Strumenti: `archetypes/post.md` per i nuovi capitoli, `scripts/make-cover.py` per le cover,
  Hugo extended per la build (non installato in sistema: usare un binario ufficiale).
- I post sono in italiano; slug e tag restano in inglese.
- Ogni capitolo, appena scritto, va linkato nella tabella della roadmap
  (`content/post/network-security-roadmap/index.md`) e nel "Prossimo nella serie" del capitolo precedente.

## Decisions so far

- [Lingua dei post](issues/01-post-language.md): italiano, termini tecnici in inglese, slug e tag in inglese.
- [Cover dei post](issues/02-cover-images.md): generate con `scripts/make-cover.py`, stile unico, 1600×900.
- [Sistema di commenti](issues/03-comments.md): resta Disqus.
- [Schema e funzionalità dei capitoli](issues/04-chapter-shape.md): schema in 6 sezioni, archetype, tassonomia controllata.
- [Build con Hugo latest](issues/05-hugo-latest-build.md): permesso HTML in `content/` e date dei `week_*` corrette; build verde.
- [Capitoli 00 e 01](issues/06-chapters-00-01.md): roadmap e threat modeling scritti, build verde.
- [Ambiente di laboratorio per i capitoli](issues/11-lab-environment.md): containerlab + Open vSwitch per 02–10; GNS3 solo per DTP/CAM Cisco; VM libvirt per il cap. 11.
- [Calendario di pubblicazione](issues/07-publishing-schedule.md): settimanale di martedì, tutti retrodatati; serie 2026-07-21 → 2026-10-06; build esterna.
- [Sezione lab della roadmap](issues/15-roadmap-lab-section.md): post 0 aggiornato a containerlab + OVS.
- [Fatti tecnici e stesura dei capitoli](issues/13-write-chapter-02.md): scritti tutti i capitoli 02–11; build verde 447 pagine.
- [Articoli extra oltre la serie](issues/16-extra-articles.md): SSH hardening, WPA3, 802.1X/NAC, mTLS, eBPF.
- [Articoli extra, secondo lotto](issues/17-extra-articles-batch-2.md): DHCP snooping/DAI, SPF/DKIM/DMARC, microsegmentazione, SIEM, DNS tunneling.

## Not yet specified

- **Immagini dentro i post.** Le gallerie richiedono screenshot dei lab (Wireshark, Suricata):
  dipendono dall'ambiente di lab e da chi li produce.
- **Serie come oggetto del sito.** Forse serve un tag o una tassonomia `series` con una pagina
  dedicata, oltre alla roadmap. Da valutare dopo 3–4 capitoli.
- **Video.** Lo shortcode `youtube`/`video` è previsto in alcuni capitoli, ma non è chiaro chi
  registra le demo.

## Out of scope

- Rivedere o tradurre i ~40 post esistenti del 2026 (generici, tutti con la stessa data): è un'altra
  iniziativa, non serve alla serie.
- Cambiare tema o sistema di commenti.
- Build e deploy del sito: li fa uno script esterno che prende il repo e lo ricostruisce
  (indicazione dell'utente, 2026-10-08). La mappa si occupa solo degli articoli.
