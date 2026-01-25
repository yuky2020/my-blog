---
title: "A Deep Dive into RSVP-TE"
description: "A technical exploration of Resource Reservation Protocol - Traffic Engineering (RSVP-TE), a signaling protocol for MPLS traffic engineering."
slug: "rsvp-te"
date: 2026-01-25T10:00:00+02:00
categories:
    - Networking
    - MPLS
tags:
    - RSVP-TE
    - MPLS
    - Traffic Engineering
image: "images/1.png"
---

## Introduction to RSVP-TE

Resource Reservation Protocol - Traffic Engineering (RSVP-TE) is a signaling protocol for MPLS traffic engineering. It is an extension to the original RSVP protocol, and it is used to establish and maintain Label Switched Paths (LSPs) in an MPLS network.

This article will provide a technical deep dive into RSVP-TE, exploring its architecture, key components, and how it works.

## RSVP-TE Architecture

The RSVP-TE architecture is made up of a number of different components:

*   **Ingress Label Edge Router (LER):** The ingress LER is the router that is at the beginning of an LSP. It is responsible for initiating the LSP setup process.
*   **Egress Label Edge Router (LER):** The egress LER is the router that is at the end of an LSP. It is responsible for terminating the LSP.
*   **Label Switching Router (LSR):** The LSR is a router that is in the middle of an LSP. It is responsible for forwarding traffic based on the MPLS labels.

## Key Components of RSVP-TE

The key components of RSVP-TE are:

*   **Path Message:** The Path message is sent from the ingress LER to the egress LER. It is used to request the setup of an LSP. The Path message contains a number of different objects, such as the LSP's destination address, the LSP's bandwidth requirements, and the LSP's path.
*   **Resv Message:** The Resv message is sent from the egress LER to the ingress LER. It is used to reserve the resources for the LSP. The Resv message contains a number of different objects, such as the LSP's label and the LSP's bandwidth allocation.
*   **Label Switched Path (LSP):** An LSP is a path that is established through an MPLS network. It is a unidirectional path, and it is identified by a label.

## How RSVP-TE Works

The following is a step-by-step overview of how RSVP-TE works:

1.  The ingress LER sends a Path message to the egress LER.
2.  The Path message is forwarded by the LSRs along the path to the egress LER.
3.  Each LSR along the path examines the Path message and makes a decision about whether or not to admit the LSP.
4.  If an LSR admits the LSP, it forwards the Path message to the next hop LSR.
5.  If an LSR does not admit the LSP, it sends a PathErr message back to the ingress LER.
6.  When the egress LER receives the Path message, it sends a Resv message back to the ingress LER.
7.  The Resv message is forwarded by the LSRs along the path to the ingress LER.
8.  Each LSR along the path examines the Resv message and reserves the resources for the LSP.
9.  When the ingress LER receives the Resv message, the LSP is established.

## Benefits of RSVP-TE

RSVP-TE provides a number of benefits, including:

*   **Traffic Engineering:** RSVP-TE can be used to engineer the traffic in an MPLS network. It can be used to steer traffic around congested links, and it can be used to provide QoS for different types of traffic.
*   **Fast Reroute (FRR):** RSVP-TE can be used to provide fast reroute for LSPs. FRR is a mechanism that allows an LSP to be quickly rerouted around a failed link or node.
*   **Constraint-Based Routing:** RSVP-TE can be used to perform constraint-based routing. Constraint-based routing is a mechanism that allows an LSP to be routed based on a set of constraints, such as bandwidth, latency, and jitter.

## Conclusion

RSVP-TE is a signaling protocol for MPLS traffic engineering. It is an extension to the original RSVP protocol, and it is used to establish and maintain Label Switched Paths (LSPs) in an MPLS network. RSVP-TE provides a number of benefits, including traffic engineering, fast reroute, and constraint-based routing. A deep understanding of RSVP-TE is essential for anyone who is responsible for managing an MPLS network.
