# Aggiornare la sezione lab della roadmap a containerlab

Type: task
Status: resolved
Blocked by: 11

## Question

Il post 0 (`content/post/network-security-roadmap/index.md`, sezione "Cosa serve per i lab") e
l'esercizio zero descrivono un lab con libvirt e `virt-install`. Il ticket "Ambiente di
laboratorio per i capitoli" ha scelto containerlab con uno switch Open vSwitch. Riscrivere la
sezione con un `.clab.yml` minimo (attaccante, vittima, gateway, switch) e adattare l'esercizio
zero. Va fatto prima del capitolo 02, che usa lo stesso lab.

## Answer

Resolved 2026-10-08. Riscritta la sezione "Cosa serve per i lab" e l'esercizio zero del post 0
con containerlab + Open vSwitch (`lab-l2.clab.yml`), coerente col ticket Ambiente di laboratorio.
