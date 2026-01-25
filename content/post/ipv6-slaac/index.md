---
title: "A Deep Dive into IPv6 Stateless Address Autoconfiguration (SLAAC)"
description: "A technical exploration of IPv6 Stateless Address Autoconfiguration (SLAAC), a mechanism for IPv6 hosts to automatically configure their own IP addresses."
slug: "ipv6-slaac"
date: 2026-01-25T10:00:00+02:00
categories:
    - Networking
    - IPv6
tags:
    - IPv6
    - SLAAC
    - Autoconfiguration
image: "images/1.png"
---

## Introduction to IPv6 Stateless Address Autoconfiguration (SLAAC)

IPv6 Stateless Address Autoconfiguration (SLAAC) is a mechanism for IPv6 hosts to automatically configure their own IP addresses. It is a simple and efficient mechanism that does not require a DHCP server.

This article will provide a technical deep dive into IPv6 SLAAC, exploring how it works, the different types of addresses that can be configured using SLAAC, and the benefits that it provides.

## How SLAAC Works

SLAAC works by using a combination of two protocols:

*   **Neighbor Discovery Protocol (NDP):** NDP is a protocol that is used by IPv6 hosts to discover their neighbors on the network. It is also used to discover the routers on the network.
*   **Modified EUI-64:** Modified EUI-64 is a format for creating a 64-bit interface identifier from a 48-bit MAC address.

The following is a step-by-step overview of how SLAAC works:

1.  An IPv6 host sends a Router Solicitation (RS) message to the all-routers multicast address.
2.  The routers on the network respond with a Router Advertisement (RA) message. The RA message contains a number of different options, such as the prefix that should be used for address autoconfiguration, the lifetime of the prefix, and the default router.
3.  The IPv6 host uses the prefix in the RA message to create a global unicast address. It does this by combining the prefix with a 64-bit interface identifier. The interface identifier is typically created using the Modified EUI-64 format.
4.  The IPv6 host then performs Duplicate Address Detection (DAD) to make sure that the address is not already in use on the network. It does this by sending a Neighbor Solicitation (NS) message to the solicited-node multicast address. If the host does not receive a Neighbor Advertisement (NA) message in response, it can then use the address.

## Types of Addresses Configured Using SLAAC

SLAAC can be used to configure two types of addresses:

*   **Link-Local Addresses:** Link-local addresses are used for communication on a single link. They are not routable on the internet. Link-local addresses are always configured using SLAAC.
*   **Global Unicast Addresses:** Global unicast addresses are used for communication on the internet. They are routable on the internet. Global unicast addresses can be configured using SLAAC or DHCPv6.

## Benefits of SLAAC

SLAAC provides a number of benefits, including:

*   **Simplicity:** SLAAC is a very simple and efficient mechanism for address autoconfiguration.
*   **No DHCP server required:** SLAAC does not require a DHCP server. This can simplify the management of the network.
*   **Scalability:** SLAAC is a very scalable mechanism for address autoconfiguration. It can be used to configure a very large number of hosts.

## SLAAC vs. DHCPv6

SLAAC and DHCPv6 are two different mechanisms for address autoconfiguration in IPv6. SLAAC is a stateless mechanism, while DHCPv6 is a stateful mechanism.

SLAAC is a good choice for networks where simplicity and scalability are important. DHCPv6 is a good choice for networks where more control over the address allocation process is required.

## Conclusion

IPv6 Stateless Address Autoconfiguration (SLAAC) is a mechanism for IPv6 hosts to automatically configure their own IP addresses. It is a simple, efficient, and scalable mechanism that does not require a DHCP server. A deep understanding of SLAAC is essential for anyone who is responsible for managing an IPv6 network.
