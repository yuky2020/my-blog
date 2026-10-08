# Ambiente di laboratorio per la serie "Network Security"

> Ricerca per il ticket `11-lab-environment.md`. Data: 2026-10-08.
> Obiettivo: un lab riproducibile su **un solo PC Linux, 16 GB di RAM, gratuito**, che copra
> attacchi a livello 2 (ARP spoofing, DHCP rogue/starvation, MAC flooding, VLAN double tagging
> 802.1Q), firewall nftables, Suricata, TLS/DNS, e che si descriva in un **file versionabile**.

## Raccomandazione in breve

- **Scelta principale: containerlab** per i capitoli 02-10. Topologia in un unico file YAML
  versionabile, consumo di RAM minimo (i nodi sono container che condividono il kernel), progetto
  molto attivo (v0.79.0, 21 ago 2026), licenza BSD-3. Nodi `linux` (Alpine/Debian con scapy,
  dnsmasq, nft, Suricata) collegati da coppie veth per gli attacchi host-to-host, e un nodo
  `ovs-bridge` (Open vSwitch) come switch reale per VLAN/trunk/802.1Q.
- **Alternativa mirata: GNS3 o libvirt/virt-install + VM**. Serve dove containerlab non arriva:
  (a) cap. 03, per DTP e per il comportamento "fail-open" del CAM su uno switch vero (immagine
  Cisco IOSvL2/IOU in GNS3); (b) cap. 11, per le appliance a VM intere pfSense/OPNsense.
- **Scartato: Proxmox VE**. È un hypervisor bare-metal: si installa *come* sistema operativo della
  macchina, non accanto al desktop del lettore, e la topologia non è un file versionabile pulito.
  Adatto solo a chi dedica un intero PC, fuori dallo scope.

---

## Criteri di valutazione

| Criterio | Perché conta per la serie |
|---|---|
| Gratuito / open source | Requisito esplicito; i lettori devono riprodurre senza licenze |
| Gira su 1 PC, 16 GB RAM | Vincolo hardware del lettore tipo |
| Attacchi L2 reali | Cap. 02-03: ARP, DHCP, MAC flooding, 802.1Q double tagging |
| Topologia in file versionabile | Allineato al blog (config in repo, `license:` dedicata al cap. 11) |
| Mantenuto al 2026 | Verificato su release/commit ufficiali |
| Screenshot per le gallerie | Il tool scelto determina come catturare Wireshark/dashboard |

### Nota tecnica: cosa richiede davvero ogni attacco L2

Questo determina la scelta più di ogni altra cosa.

- **ARP spoofing, DHCP rogue/starvation**: bastano due o più host sullo stesso dominio di
  broadcast L2. Funzionano fra namespace di rete collegati da veth/bridge: le coppie veth sono
  trasparenti al traffico Ethernet, quindi i frame ARP/DHCP passano senza problemi.
- **MAC flooding (es. `macof`)**: la *tecnica* (generare migliaia di MAC sorgente) e la sua
  *rilevazione* si riproducono ovunque. Il comportamento hardware "CAM pieno -> lo switch va in
  fail-open e inonda tutte le porte" **non** si replica fedelmente su un bridge Linux o su Open
  vSwitch (hanno una FDB software che non degrada come il TCAM di uno switch fisico). Per mostrare
  il vero fail-open serve un'immagine di switch reale (Cisco IOSvL2/IOU in GNS3).
- **VLAN 802.1Q, trunk, native VLAN, double tagging**: serve un dataplane che gestisca davvero i
  tag. Il bridge Linux, con `vlan_filtering` disattivo (default), è trasparente ai tag; con
  `vlan_filtering` attivo fa filtraggio per (MAC, tag) ma non emula un trunk Cisco in modo comodo
  ([docs.kernel.org/networking/bridge](https://kernel.org/doc/Documentation/networking/bridge.rst)).
  **Open vSwitch** gestisce nativamente access/trunk 802.1Q e la modalità `dot1q-tunnel`
  (802.1ad / double-tag), quindi è lo strumento giusto per il double tagging senza hardware
  ([patch libvirt OVS dot1q-tunnel](https://lists.libvirt.org/archives/list/devel@lists.libvirt.org/thread/GY4Z4NBHFTFH6HY6JHMPCZFPVFIFL2FT)).
- **DTP (Dynamic Trunking Protocol)**: è proprietario Cisco. Nessun bridge Linux né OVS lo parla.
  La variante "switch spoofing via DTP" si dimostra **solo** con un'immagine Cisco (IOSvL2/IOU in
  GNS3). Il double tagging, invece, si mostra benissimo con OVS configurando la native VLAN.

Conseguenza: per coprire *tutto* senza immagini Cisco, si usa containerlab con nodi Linux + OVS, e
si spiega a parole (o con un breve riquadro) che DTP e il fail-open del CAM sono fenomeni di switch
fisici. Chi vuole la fedeltà totale su quei due dettagli passa a GNS3 con IOSvL2/IOU (immagini non
redistribuibili legalmente -> non "gratuite" in senso stretto, va dichiarato).

---

## Candidato 1 — containerlab (scelta principale)

**Mantenimento:** molto attivo. Ultima release **v0.79.0 del 21 agosto 2026**; cadenza di rilascio
mensile (v0.78.x ad agosto, v0.77.0 a giugno 2026)
([releases su GitHub](https://github.com/srl-labs/containerlab/releases)). Licenza **BSD-3-Clause**
([LICENSE](https://raw.githubusercontent.com/srl-labs/containerlab/main/LICENSE)).

**Attacchi L2 — possibilità e limiti:**
- I nodi `linux` sono container (namespace di rete separati) collegati da veth: ARP spoofing, DHCP
  rogue/starvation e il traffico MAC flooding passano senza ostacoli.
- Kind `bridge` = bridge Linux preesistente (containerlab non crea il bridge, aggiunge solo regole
  iptables di FORWARD) ([kind bridge](https://containerlab.dev/manual/kinds/bridge/)).
- Kind **`ovs-bridge`** = Open vSwitch preesistente, con "più opzioni di connettività del classico
  bridge Linux" e L2 estesa via VXLAN ([kind ovs-bridge](https://containerlab.dev/manual/kinds/ovs-bridge/)).
  È qui che si fa VLAN/trunk/802.1Q/double tagging.
- **Limite 1:** i container condividono il kernel dell'host. Per i topic della serie non è un
  problema (nftables e Suricata girano per-namespace), ma non si possono caricare moduli kernel
  diversi per nodo. **Limite 2:** niente DTP e niente fail-open hardware del CAM (vedi nota sopra).
  **Limite 3:** bridge e OVS vanno pre-creati a mano con uno script di setup accanto alla topologia.

**Risorse:** minime. Un container Alpine occupa decine di MB di RAM; su 16 GB si tengono
comodamente decine di nodi. È l'unico candidato che permette lab densi senza problemi.

**Topologia versionabile:** file unico `*.clab.yml` (dichiarativo: `name`, `topology.nodes`,
`topology.kinds`, `topology.links`) ([topo-def-file](https://containerlab.dev/manual/topo-def-file/)).
Ideale per il repo del blog e per il requisito "config con `license:` dedicata" del cap. 11.

**Screenshot:** si cattura il traffico con `ip netns exec clab-<lab>-<nodo> tcpdump`/Wireshark
sulle veth dell'host, oppure Wireshark dentro un nodo con GUI. Dashboard Suricata/EveBox via
container con porta esposta.

## Candidato 2 — libvirt / virt-install (alternativa per VM intere)

**Mantenimento:** attivo. `virt-install` 5.1.0 pacchettizzato nel 2026 (build 5.1.0-4 del
19/07/2026 su Arch) ([Arch extra/virt-install](https://archlinux.org/packages/extra/x86_64/virt-install/));
libvirt 11.x nel 2026 ([openSUSE libvirt 11.4.0](https://pkgdex.org/opensuse/leap%2016.0/x86_64/oss/libvirt-11.4.0-160000.2.2.rpm.html)).
Gratuito (LGPL/GPL).

**Attacchi L2 — possibilità e limiti:** VM intere con kernel proprio -> massima fedeltà per
nftables/Suricata (interfacce e conntrack reali). Per le VLAN si collegano le VM a Open vSwitch
(libvirt ha il supporto nativo alle reti OVS, incluso `dot1q-tunnel`). Stessi limiti di OVS su DTP
(assente) e CAM fail-open. ARP/DHCP/MAC flooding ok.

**Risorse:** pesanti. Ogni VM Linux "vera" chiede 1-2 GB di RAM: su 16 GB si arriva a circa 4-6 VM.
Vincolante per topologie con molti nodi.

**Topologia versionabile:** sì ma frammentata — un XML per dominio (`virsh dumpxml`) più un XML per
rete, oppure uno script `virt-install`. Meno elegante del singolo YAML di containerlab; va
corredato da uno script di orchestrazione.

**Screenshot:** Wireshark dentro la VM, o cattura sul bridge/OVS dell'host.

## Candidato 3 — GNS3 (alternativa per switch Cisco reali e appliance)

**Mantenimento:** attivo su due rami. **v3.0.6 del 28/01/2026** (API FastAPI, RBAC, image manager)
e ramo 2.2.x ancora supportato (2.2.59 del 09/05/2026)
([release note GNS3 v3](https://packettracernetwork.com/download/download-gns3.html)).

**Attacchi L2 — possibilità e limiti:** è il più completo sul L2. Con **Cisco IOSvL2 / IOU L2**
supporta DTP, port security, PVST+/RPVST+, MST e il comportamento autentico del CAM; è il contesto
classico dei lab VLAN hopping (Kali attaccante + host vittima + IOSvL2)
([switching in GNS3](https://docs.gns3.com/docs/using-gns3/beginners/switching-and-gns3)). Dispone
anche di Open vSwitch integrato e dello switch built-in. **Limite grosso:** le immagini Cisco
IOSvL2/IOU non sono redistribuibili legalmente e vanno procurate dal lettore -> contro il requisito
"gratuito/riproducibile". Con OVS/built-in il problema sparisce ma si perde DTP.

**Risorse:** la GUI più la GNS3 VM (o il backend locale) aggiungono overhead; ogni nodo IOU/IOSvL2
è una VM leggera ma non quanto un container. Su 16 GB si gestiscono lab medi.

**Topologia versionabile:** sì, file progetto `.gns3` (JSON) più la cartella del progetto. Meno
leggibile in diff rispetto a uno YAML, ma versionabile. Supporta appliance pfSense/OPNsense,
utile per il cap. 11.

**Screenshot:** ottimo — GUI con topologia grafica (perfetta per le gallerie) e Wireshark
integrato con un clic sul link.

## Candidato 4 — Proxmox VE (scartato)

**Mantenimento:** attivo e gratuito, ma **è un hypervisor bare-metal**: si installa come sistema
operativo della macchina ([guide installazione bare-metal](https://www.cherryservers.com/blog/how-to-install-proxmox-on-bare-metal)).
Non è pensato per convivere col desktop del lettore su un PC d'uso quotidiano. La topologia si
costruisce da web UI / API (VM + SDN), non in un file versionabile pulito e leggibile in diff.
Overhead di gestione alto per lo scopo. **Escluso**: contraddice "un solo PC" inteso come la
macchina che il lettore già usa, e il requisito del file versionabile.

---

## Mappa capitolo -> strumento

| Cap. | Tema | Strumento consigliato |
|---|---|---|
| 02 | L2: ARP spoofing, MAC flooding, DHCP starvation | **containerlab** (nodi linux + ovs-bridge); nota su CAM fail-open |
| 03 | VLAN hopping, DTP, port security | **containerlab + OVS** per double tagging; **GNS3 + IOSvL2** per DTP/CAM autentici (caveat licenza) |
| 04 | nftables, conntrack | **containerlab** (nodo linux con nft); eventuale VM libvirt per conntrack "vero" |
| 05 | Suricata | **containerlab** (container Suricata + EveBox) |
| 06-07 | TLS, DNS/DNSSEC/DoH | **containerlab** (openssl, unbound/bind, dnsmasq in container) |
| 08 | DDoS | **containerlab** (generatori di traffico in container) |
| 09 | IPsec vs WireGuard | **containerlab** (kernel host supporta WireGuard/xfrm) |
| 10 | Analisi pcap Wireshark | i pcap prodotti nei lab containerlab; Wireshark sull'host |
| 11 | Homelab completo (pfSense/OPNsense, Suricata, VLAN) | **GNS3** o **libvirt/virt-install** (appliance a VM intere) |

Così lo strumento base è uno solo (containerlab) per 9 capitoli su 10, e si introduce un secondo
strumento solo dove serve davvero una VM intera o uno switch Cisco.

---

## Esempio minimo di topologia (attaccante / vittima / gateway / switch)

Formato containerlab, file `lab-l2.clab.yml`. Lo "switch" è un nodo `ovs-bridge` (Open vSwitch
reale, da pre-creare), così da avere un dataplane 802.1Q vero per i capitoli VLAN.

Script di setup (prima del `deploy`):

```bash
# crea il bridge Open vSwitch usato come "switch" del lab
sudo ovs-vsctl add-br sw0
sudo ip link set sw0 up
```

Topologia:

```yaml
name: lab-l2

topology:
  kinds:
    linux:
      image: wettyoss/wetty:latest   # sostituibile con un'immagine propria (scapy, nft, suricata)

  nodes:
    # switch Ethernet reale (Open vSwitch pre-creato con nome sw0)
    sw0:
      kind: ovs-bridge

    # gateway / router della rete vittima
    gateway:
      kind: linux
      image: alpine:3.20
      exec:
        - ip addr add 10.0.0.1/24 dev eth1
        - ip link set eth1 up

    # host vittima
    victim:
      kind: linux
      image: alpine:3.20
      exec:
        - ip addr add 10.0.0.10/24 dev eth1
        - ip link set eth1 up
        - ip route add default via 10.0.0.1

    # macchina attaccante (scapy, dsniff/arpspoof, yersinia, macof, ecc.)
    attacker:
      kind: linux
      image: alpine:3.20   # o un'immagine con i tool preinstallati
      exec:
        - ip addr add 10.0.0.66/24 dev eth1
        - ip link set eth1 up

  links:
    - endpoints: ["gateway:eth1", "sw0:p-gw"]
    - endpoints: ["victim:eth1",  "sw0:p-victim"]
    - endpoints: ["attacker:eth1","sw0:p-attacker"]
```

Deploy / distruzione:

```bash
sudo containerlab deploy -t lab-l2.clab.yml
# ... esercizi (es. arpspoof, dhcp rogue, macof) da dentro il nodo attacker ...
sudo containerlab destroy -t lab-l2.clab.yml
```

Per il **double tagging 802.1Q** (cap. 03) si configurano le porte OVS con native VLAN e trunk, ad
esempio:

```bash
# porta attaccante = access sulla native VLAN 1; porta vittima = trunk
sudo ovs-vsctl set port p-attacker tag=1
sudo ovs-vsctl set port p-victim   trunks=1,20
# l'attaccante invia un frame con doppio tag (outer=1 nativo, inner=20):
# lo switch toglie il tag nativo e inoltra verso la VLAN 20
```

In alternativa, la variante con **DTP** (switch spoofing) richiede un'immagine Cisco IOSvL2/IOU in
GNS3, con la porta in `dynamic desirable`/`dynamic auto` e `yersinia`/`scapy` lato attaccante.

---

## Fonti

- containerlab, releases ufficiali: <https://github.com/srl-labs/containerlab/releases>
- containerlab, licenza BSD-3: <https://raw.githubusercontent.com/srl-labs/containerlab/main/LICENSE>
- containerlab, kind `bridge`: <https://containerlab.dev/manual/kinds/bridge/>
- containerlab, kind `ovs-bridge`: <https://containerlab.dev/manual/kinds/ovs-bridge/>
- containerlab, topology definition file: <https://containerlab.dev/manual/topo-def-file/>
- Linux bridge e VLAN 802.1Q (kernel docs): <https://kernel.org/doc/Documentation/networking/bridge.rst>
- Open vSwitch `dot1q-tunnel` (802.1ad double-tag), patch libvirt: <https://lists.libvirt.org/archives/list/devel@lists.libvirt.org/thread/GY4Z4NBHFTFH6HY6JHMPCZFPVFIFL2FT>
- VLAN hopping / double tagging (spiegazione tecnica): <https://networklessons.com/switching/vlan-hopping>
- GNS3 v3.0 release / note: <https://packettracernetwork.com/download/download-gns3.html>
- GNS3, switching e opzioni (IOSvL2, IOU, OVS, built-in): <https://docs.gns3.com/docs/using-gns3/beginners/switching-and-gns3>
- virt-install 5.1.0 (2026, Arch): <https://archlinux.org/packages/extra/x86_64/virt-install/>
- libvirt 11.x (2026, openSUSE): <https://pkgdex.org/opensuse/leap%2016.0/x86_64/oss/libvirt-11.4.0-160000.2.2.rpm.html>
- Proxmox VE installazione bare-metal: <https://www.cherryservers.com/blog/how-to-install-proxmox-on-bare-metal>
