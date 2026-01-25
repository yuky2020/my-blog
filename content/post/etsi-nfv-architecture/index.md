---
title: "A Deep Dive into the ETSI NFV Architecture"
description: "A technical exploration of the ETSI NFV architecture, a standardized framework for network function virtualization."
slug: "etsi-nfv-architecture"
date: 2026-01-25T10:00:00+02:00
categories:
    - Networking
    - NFV
tags:
    - ETSI NFV
    - NFV
    - Network Virtualization
image: "images/1.png"
---

## Introduction to ETSI NFV

The European Telecommunications Standards Institute (ETSI) has developed a standardized framework for Network Function Virtualization (NFV). The ETSI NFV architecture is a high-level functional architecture that defines the key components of an NFV solution and the interfaces between them.

This article will provide a technical deep dive into the ETSI NFV architecture, exploring its key components, reference points, and how it is being used to build the next generation of telecommunications networks.

## ETSI NFV Architectural Framework

The ETSI NFV architectural framework is made up of three main domains:

*   **Network Functions Virtualization Infrastructure (NFVI):** The NFVI is the foundation of the NFV architecture. It is made up of the physical hardware and software resources that are used to run the virtualized network functions.
*   **Virtualized Network Functions (VNFs):** VNFs are the software implementations of network functions, such as firewalls, load balancers, and routers.
*   **Management and Orchestration (MANO):** The MANO domain is responsible for managing and orchestrating the NFVI and the VNFs.

## Network Functions Virtualization Infrastructure (NFVI)

The NFVI is made up of three main components:

*   **Hardware Resources:** The hardware resources include the compute, storage, and networking resources that are used to run the VNFs.
*   **Virtualization Layer:** The virtualization layer is responsible for abstracting the hardware resources and for creating a virtual environment for the VNFs. This is typically a hypervisor, such as KVM or VMware ESXi.
*   **Virtualization Infrastructure Manager (VIM):** The VIM is responsible for managing the hardware and software resources of the NFVI.

## Virtualized Network Functions (VNFs)

VNFs are the software implementations of network functions. They are designed to run on top of the NFVI, and they can be instantiated and scaled on demand.

VNFs are typically packaged as virtual machines (VMs) or containers. They are managed by a VNF Manager (VNFM), which is responsible for the lifecycle management of the VNF.

## Management and Orchestration (MANO)

The MANO domain is responsible for managing and orchestrating the NFVI and the VNFs. It is made up of three main components:

*   **NFV Orchestrator (NFVO):** The NFVO is responsible for the overall orchestration of the NFV solution. It is responsible for instantiating and scaling the VNFs, and for managing the network services.
*   **VNF Manager (VNFM):** The VNFM is responsible for the lifecycle management of the VNFs. This includes things like instantiating, scaling, and terminating the VNFs.
*   **Virtualization Infrastructure Manager (VIM):** The VIM is responsible for managing the hardware and software resources of the NFVI.

## ETSI NFV Reference Points

The ETSI NFV architecture defines a number of reference points, which are the interfaces between the different components of the architecture. Some of the most important reference points include:

*   **Vi-Vnfm:** This reference point is between the VIM and the VNFM. It is used by the VNFM to manage the lifecycle of the VNFs.
*   **Vn-Nfvo:** This reference point is between the VNFM and the NFVO. It is used by the NFVO to orchestrate the VNFs.
*   **Or-Vi:** This reference point is between the NFVO and the VIM. It is used by the NFVO to manage the resources of the NFVI.

## Conclusion

The ETSI NFV architecture is a standardized framework for network function virtualization. It is a high-level functional architecture that defines the key components of an NFV solution and the interfaces between them. The ETSI NFV architecture is being used by a number of service providers and enterprises to build the next generation of telecommunications networks.
