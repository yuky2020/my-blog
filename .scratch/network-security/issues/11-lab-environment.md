# Ambiente di laboratorio per i capitoli

Type: research
Status: resolved

## Question

Quale ambiente di lab usano i capitoli 02–11, in modo che i lettori possano riprodurre gli
esercizi con un solo PC? Candidati: libvirt/virt-install (già citato nella roadmap), containerlab,
GNS3, Proxmox. Criteri: gratuito, gira su un PC con 16 GB di RAM, permette attacchi L2
(ARP, DHCP, VLAN con 802.1Q), si descrive in un file versionabile, è aggiornato al 2026.
Il risultato decide anche come produrre gli screenshot per le gallerie.

## Answer

Resolved 2026-10-08 da un agente di ricerca. Dettagli e fonti: [research/11-lab-environment.md](../research/11-lab-environment.md).

- **Scelta principale: containerlab** per i capitoli 02–10. Topologia in un file `.clab.yml`
  versionabile, consumo di RAM minimo, progetto attivo (v0.79.0, agosto 2026). Lo switch è un
  nodo Open vSwitch, che gestisce 802.1Q e il double tagging.
- **Limiti:** DTP è proprietario Cisco e il fail-open della CAM table non si replica su bridge
  Linux/OVS. Per mostrarli serve GNS3 con immagini Cisco IOSvL2/IOU, che non sono redistribuibili.
- **Capitolo 11 (homelab con OPNsense/pfSense):** VM intere con libvirt o GNS3.
- **Proxmox scartato:** si installa come sistema operativo della macchina e la topologia non si
  versiona in modo pulito.
