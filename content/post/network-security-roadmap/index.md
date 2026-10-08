---
title: "Network Security dal cavo in su: la roadmap"
description: "Mappa della serie sulla sicurezza delle reti: un modello a strati per capire dove nascono gli attacchi, dove si fermano e in che ordine studiarli."
slug: "network-security-roadmap"
date: 2026-07-21T09:00:00+02:00
lastmod: 2026-07-21T09:00:00+02:00
weight: 1
categories:
    - Security
    - Networking
tags:
    - Network Security
    - Threat Modeling
    - Zero Trust
keywords:
    - sicurezza delle reti
    - network security roadmap
    - defense in depth
    - modello OSI sicurezza
image: "cover.png"
toc: true
links:
  - title: MITRE ATT&CK
    description: Il catalogo delle tecniche usate dagli attaccanti reali, organizzato per tattica.
    website: https://attack.mitre.org/
  - title: NIST SP 800-207 — Zero Trust Architecture
    description: Il documento di riferimento sul modello Zero Trust.
    website: https://csrc.nist.gov/pubs/sp/800/207/final
  - title: CIS Critical Security Controls
    description: Un elenco di controlli difensivi in ordine di priorità.
    website: https://www.cisecurity.org/controls
  - title: Wireshark
    description: L'analizzatore di pacchetti che useremo in quasi tutti i lab.
    website: https://www.wireshark.org/
---

## Perché una serie, e perché "dal cavo in su"

Sulla sicurezza delle reti si trovano due tipi di materiale: guide molto teoriche, che elencano
acronimi senza mai mostrare un pacchetto, e tutorial che spiegano come lanciare uno strumento
senza dire perché funziona. Questa serie prova a stare in mezzo.

L'idea è semplice: partire dal livello più basso, il cavo e lo switch, e salire uno strato alla volta
fino a TLS e DNS. Per ogni livello vediamo **come funziona il protocollo**, **come viene
attaccato** e **come lo si difende**, con comandi reali e un piccolo laboratorio da rifare a casa.

{{< quote author="Bruce Schneier" source="Crypto-Gram, maggio 2000" url="https://www.schneier.com/crypto-gram/archives/2000/0515.html" >}}
Security is a process, not a product.
{{< /quote >}}

Questo post è la mappa: resta fissato in cima al blog e verrà aggiornato man mano che escono i
capitoli.

## Il modello a strati

Ogni livello della rete si fida di quello sotto. Se un attaccante controlla lo strato 2, può
leggere e modificare tutto quello che ci passa sopra, a meno che uno strato superiore (ad esempio
TLS) non aggiunga protezioni proprie. Per questo la difesa si costruisce **in profondità**: ogni
strato deve reggere anche quando quello sotto è compromesso.

```mermaid
flowchart BT
    L1["L1 · Fisico<br/>accesso alle porte, tap"]
    L2["L2 · Data link<br/>ARP, VLAN, STP, DHCP"]
    L3["L3 · Rete<br/>IP spoofing, routing, BGP"]
    L4["L4 · Trasporto<br/>firewall stateful, SYN flood"]
    L7["L5-7 · Applicazione<br/>TLS, DNS, HTTP"]
    L1 --> L2 --> L3 --> L4 --> L7
    IDS(["IDS / IPS<br/>osserva tutti gli strati"]) -.-> L2 & L3 & L4 & L7
    ZT(["Zero Trust<br/>nessuno strato è fidato a priori"]) -.-> L7
    classDef attack fill:#fde2e4,stroke:#e63946,color:#111;
    class L1,L2,L3,L4,L7 attack;
```

La freccia va dal basso verso l'alto: è la direzione in cui si propaga la fiducia, e quindi
anche il danno.

## La mappa della serie

```mermaid
mindmap
  root((Network<br/>Security))
    Metodo
      Threat modeling
      Homelab
    Strato 2
      ARP spoofing
      VLAN hopping
    Strato 3-4
      Firewall nftables
      DDoS
    Strato 7
      TLS 1.3
      DNSSEC e DoH
    Rilevamento
      Suricata
      Wireshark
    Tunnel
      IPsec vs WireGuard
```

| # | Capitolo | Di cosa parla | Stato |
|---|---|---|---|
| 00 | **Questa roadmap** | Mappa e metodo | ✅ |
| 01 | [Threat modeling per le reti]({{< relref "post/threat-modeling-networks" >}}) | STRIDE applicato a una rete reale | ✅ |
| 02 | [Attacchi a livello 2]({{< relref "post/layer2-attacks-arp-spoofing" >}}) | ARP spoofing, MAC flooding, DHCP starvation | ✅ |
| 03 | [VLAN hopping e hardening degli switch]({{< relref "post/vlan-hopping-and-switch-hardening" >}}) | Double tagging, DTP, port security | ✅ |
| 04 | [Firewall stateful con nftables]({{< relref "post/stateful-firewalls-nftables" >}}) | Da iptables a nftables, conntrack | ✅ |
| 05 | [IDS/IPS con Suricata]({{< relref "post/ids-ips-suricata" >}}) | Installazione e scrittura di regole | ✅ |
| 06 | [TLS 1.3 in profondità]({{< relref "post/tls-deep-dive" >}}) | Handshake, PKI, certificate pinning | ✅ |
| 07 | [Sicurezza del DNS]({{< relref "post/dns-security-dnssec-doh" >}}) | Cache poisoning, DNSSEC, DoH/DoT | ✅ |
| 08 | [Anatomia di un DDoS]({{< relref "post/ddos-anatomy-and-mitigation" >}}) | Attacchi volumetrici, amplificazione, mitigazione | ✅ |
| 09 | [IPsec vs WireGuard]({{< relref "post/ipsec-vs-wireguard" >}}) | Confronto pratico | ✅ |
| 10 | [Analisi dei pacchetti]({{< relref "post/packet-analysis-wireshark" >}}) | Trovare un attacco in un pcap | ✅ |
| 11 | [Un homelab per la sicurezza]({{< relref "post/building-a-security-homelab" >}}) | OPNsense, VLAN, Suricata | ✅ |

## Cosa c'è già sul blog

Alcuni argomenti li ho già trattati in post separati, che la serie riprende e collega:

- [Sicurezza di BGP con RPKI]({{< relref "post/bgp-security-rpki" >}}): come si valida l'origine di una rotta.
- [Zero Trust Architecture]({{< relref "post/zero-trust-architecture" >}}): il modello "mai fidarsi, verificare sempre".
- [Network Security Mesh]({{< relref "post/network-security-mesh-architecture" >}}): la sicurezza oltre il perimetro.
- [SASE]({{< relref "post/sase" >}}): rete e sicurezza come servizio cloud.
- [WireGuard]({{< relref "post/wireguard-vpn" >}}): la base per il capitolo 09.

## Come leggere i capitoli

Ogni capitolo segue lo stesso schema, così è facile orientarsi:

1. **Perché conta**: il problema in due paragrafi.
2. **Come funziona**: il protocollo, con un diagramma.
3. **L'attacco**: cosa fa l'attaccante, con comandi veri.
4. **La difesa**: la configurazione che lo blocca, con le righe importanti evidenziate.
5. **Lab**: un esercizio da fare nel proprio laboratorio, con la soluzione nascosta.

Gli attacchi vanno provati **solo in un laboratorio vostro** o su reti per cui avete
un'autorizzazione scritta. Il capitolo 11 spiega come costruirne uno con poca spesa.

### Cosa serve per i lab

Basta un PC Linux con 16 GB di RAM. Per quasi tutti i capitoli usiamo
[containerlab](https://containerlab.dev/): descrive una topologia in un solo file YAML, avvia i
nodi come container (quindi consuma poca RAM) e usa un vero switch [Open vSwitch](https://www.openvswitch.org/)
quando serve lavorare sulle VLAN. Solo il capitolo 11 passa a macchine virtuali intere.

La topologia minima dei primi capitoli — attaccante, vittima, gateway e uno switch — sta in un
file `lab-l2.clab.yml`:

```yaml
name: lab-l2
topology:
  nodes:
    sw0:       { kind: ovs-bridge }          # switch reale (Open vSwitch, pre-creato)
    gateway:   { kind: linux, image: alpine:3.20 }
    victim:    { kind: linux, image: alpine:3.20 }
    attacker:  { kind: linux, image: alpine:3.20 }
  links:
    - endpoints: ["gateway:eth1",  "sw0:p-gw"]
    - endpoints: ["victim:eth1",   "sw0:p-victim"]
    - endpoints: ["attacker:eth1", "sw0:p-attacker"]
```

```bash
sudo ovs-vsctl add-br sw0 && sudo ip link set sw0 up   # crea lo switch una volta
sudo containerlab deploy -t lab-l2.clab.yml            # avvia il lab
sudo containerlab destroy -t lab-l2.clab.yml           # lo smonta
```

{{< rawhtml >}}
<details>
<summary><strong>Esercizio zero:</strong> perché lo switch è un nodo Open vSwitch e non un normale bridge Linux?</summary>
<p>Un bridge Linux fa passare i frame tra i nodi, ma gestisce le VLAN 802.1Q in modo limitato: il
double tagging del capitolo 03 ha bisogno di un dataplane che tratti i tag come uno switch vero.
Open vSwitch lo fa, e permette di configurare porte access e trunk con <code>ovs-vsctl</code>,
proprio come su uno switch gestito. Per ARP spoofing, DHCP e MAC flooding (capitolo 02) basterebbe
anche il bridge, ma usare OVS da subito evita di cambiare lab a metà serie.</p>
</details>
{{< /rawhtml >}}

## Conclusione

La sicurezza di una rete è forte quanto il suo strato più debole. Questa serie li attraversa tutti
in ordine, dal livello più basso al più alto, mostrando per ciascuno un attacco concreto e la sua
difesa.

**Prossimo nella serie:** [01 · Threat modeling per le reti]({{< relref "post/threat-modeling-networks" >}}). Prima di difendere qualcosa bisogna
sapere cosa si sta difendendo e da chi.
