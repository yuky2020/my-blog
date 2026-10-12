---
title: "Troubleshooting dei difetti di stampa"
description: "Ogni difetto di stampa è un sintomo con una causa fisica: stringing, under-extrusion, warping, layer shift, elephant foot. Una guida diagnostica per leggere un pezzo venuto male e risalire alla causa, cambiando un parametro alla volta invece di arrendersi. La chiusura della serie."
slug: "troubleshooting-difetti-stampa"
date: 2026-09-29T09:00:00+02:00
lastmod: 2026-09-29T09:00:00+02:00
categories:
    - Making
    - 3D Printing
tags:
    - Stampa 3D
    - Troubleshooting
    - Difetti
keywords:
    - troubleshooting stampa 3d
    - stringing
    - under extrusion
    - layer shift
    - elephant foot
image: "cover.png"
toc: true
links:
  - title: "Simplify3D — Troubleshooting Guide"
    description: "Catalogo illustrato dei difetti con cause e soluzioni."
    website: https://www.simplify3d.com/resources/print-quality-troubleshooting/
  - title: "Prusa — Print quality"
    description: "Diagnosi dei problemi di qualità più comuni."
    website: https://help.prusa3d.com/
---

## Perché conta

Hai attraversato la serie: capisci la [FDM]({{< relref "post/come-funziona-fdm" >}}), la
[macchina]({{< relref "post/anatomia-della-stampante" >}}), i
[materiali]({{< relref "post/filamenti-e-materiali" >}}), lo
[slicing]({{< relref "post/slicing-e-gcode" >}}), il
[primo layer]({{< relref "post/primo-layer-e-adesione" >}}) e la
[calibrazione]({{< relref "post/calibrazione-temperature-flow" >}}). Il **troubleshooting** è
l'abilità che unisce tutto: guardare un pezzo venuto male e risalire alla causa. Perché ogni difetto è
un *sintomo* con una causa fisica precisa — e chi la riconosce cambia un parametro, non dieci.

## Il metodo diagnostico

```mermaid
flowchart LR
    S[Osserva il sintomo:<br/>dove, quando, che aspetto] --> C[Ipotizza la causa<br/>fisica più probabile]
    C --> F[Cambia UN parametro]
    F --> T[Ristampa un test<br/>piccolo e veloce]
    T --> V{Risolto?}
    V -->|no| C
    V -->|sì| OK[Annota: impari il tuo setup]
    style C fill:#fde2e4,stroke:#e63946
```

La disciplina è la stessa della calibrazione: **un parametro alla volta**, test piccoli e veloci (non
ristampare il pezzo grande da due ore), e annotare cosa ha funzionato. Chi cambia tutto insieme non
imparerà mai cosa contava davvero.

## Il catalogo dei difetti comuni

```text {hl_lines=[2,5,8]}
SINTOMO                        CAUSA PROBABILE                 COSA PROVARE
Fili sottili (stringing)       temp alta / filo umido / retr.  abbassa temp, asciuga, calibra retraction
Buchi, pareti deboli (under)   flusso basso / nozzle intasato  alza flusso, pulisci nozzle, controlla filo
Angoli sollevati (warping)     ritiro / piano freddo / correnti piano più caldo, brim, no correnti
Strati disallineati (shift)    cinghie/pulegge / testa urta    tendi cinghie, serra pulegge, rallenta
Base svasata (elephant foot)   nozzle troppo basso / piano caldo alza Z-offset un filo, -5°C sul piano
Superficie mossa (ghosting)    vibrazioni / troppo veloce      rallenta, irrigidisci il telaio
Pezzo staccato a metà          adesione / warping / urto testa  vedi primo layer + warping
Delaminazione tra strati       temp troppo bassa / raffr. alto  alza temp, riduci ventola
```

Le righe evidenziate sono i tre casi più frequenti: **stringing**, **under-extrusion** e **warping**.
Nota come molti sintomi rimandino a capitoli precedenti — il troubleshooting è applicare quella
conoscenza al contrario, dal sintomo alla causa.

## Dove si manifesta dà l'indizio

*Quando* e *dove* compare il difetto restringe la causa più del difetto stesso:

- **Fin dal primo layer** → [livellamento, Z-offset, adesione]({{< relref "post/primo-layer-e-adesione" >}}),
  quasi mai la calibrazione fine.
- **Sempre a una certa altezza** → qualcosa di meccanico a quella Z, o surriscaldamento progressivo.
- **Solo sugli sbalzi** → raffreddamento insufficiente o mancanza di
  [supporti]({{< relref "post/supporti-e-orientamento" >}}).
- **A metà di stampe lunghe, poi blocco** → [heat creep / intasamento]({{< relref "post/anatomia-della-stampante" >}})
  o filamento che si aggroviglia sulla bobina.

## La mentalità: isolare, non arrendersi

Il principio che chiude la serie: una stampa fallita non è sfortuna, è *informazione*. Dice esattamente
cosa non va, se sai leggerla. L'errore del principiante è reagire al fallimento cambiando tutto o
arrendendosi; l'approccio che funziona è trattare ogni difetto come un piccolo esperimento — un'ipotesi,
una variabile, un test — finché il setup è affidabile. È la stessa mentalità delle altre serie del
blog: capire il sistema abbastanza da riconoscere, dal sintomo, cosa è andato storto.

{{< rawhtml >}}
<details>
<summary><strong>Domanda:</strong> alla fine ci sono decine di difetti e decine di cause che si sovrappongono. Non è più semplice comprare una stampante "chiusa" e di qualità che fa tutto da sola, invece di imparare tutto questo?</summary>
<p>È una scelta legittima e per molti la risposta giusta — ma vale la pena capire cosa compri e cosa non
compri con una macchina "che fa tutto da sola", perché il marketing suggerisce che elimini il bisogno di
capire, e non è così. Cosa compri davvero con le stampanti moderne chiuse e ben ingegnerizzate: un telaio
rigido (meno ghosting e layer shift), calibrazioni automatiche serie (livellamento, compensazione,
spesso flow e pressure advance tarati), una camera che gestisce temperatura e correnti (meno warping),
profili di materiale già ottimizzati, e sensori che fermano la stampa se il filo finisce o si inceppa.
Tutto questo <em>riduce drasticamente la frequenza</em> dei difetti e abbassa la barriera d'ingresso: è
reale e per chi vuole "premere stampa e avere il pezzo" è denaro ben speso. Cosa <em>non</em> compri:
l'immunità dalla fisica. Quella macchina usa gli stessi principi FDM — deposita plastica fusa strato su
strato, non stampa nel vuoto, i pezzi restano anisotropi, il filamento assorbe ancora umidità, gli
sbalzi oltre i 45° vogliono comunque supporti, gli incastri vogliono comunque tolleranze. Quando (non se)
qualcosa andrà storto — un filamento nuovo che si comporta diversamente, un modello con sbalzi impossibili,
un pezzo funzionale che si rompe nella direzione sbagliata, un incastro che non chiude, una bobina umida
che fa crepitare il nozzle — la macchina automatica non ti dirà <em>perché</em>, ti darà solo un pezzo
brutto o un errore generico. E le decisioni che contano di più per un buon risultato — orientamento,
scelta del materiale, quando servono supporti, come progettare o adattare un modello — restano tue a
prescindere dall'automazione, perché dipendono dallo scopo del pezzo, che solo tu conosci. Quindi il
quadro onesto: una buona macchina chiusa ti fa partire prima e sbagliare meno, ed è un ottimo
investimento se il tuo obiettivo è usare la stampa come strumento senza farne un hobby. Ma la comprensione
di questa serie non diventa inutile: diventa ciò che ti permette di <em>sfruttare appieno</em> anche la
macchina migliore, di risolvere i casi che l'automazione non copre, e di passare da "stampo quello che
trovo già pronto" a "stampo quello che mi serve, come mi serve". L'automazione sposta il punto di
partenza; non sposta il soffitto, che resta fatto di quanto capisci il processo.</p>
</details>
{{< /rawhtml >}}

## Conclusione

Il troubleshooting è leggere un pezzo fallito come informazione: ogni difetto — stringing,
under-extrusion, warping, layer shift, elephant foot — ha una causa fisica, e *dove* e *quando* compare
la rivela. Il metodo è sempre lo stesso: un'ipotesi, un parametro, un test. Qui si chiude la serie
**Stampa 3D in pratica**: dalla fisica della FDM al pezzo finito, con un filo conduttore unico —
capire il processo trasforma la stampa 3D da magia imprevedibile a mestiere ripetibile.
