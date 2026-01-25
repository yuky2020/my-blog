---
title: "A Deep Dive into BGP Attributes and Path Selection"
description: "A technical exploration of BGP attributes and the BGP path selection process."
slug: "bgp-attributes-and-path-selection"
date: 2026-01-25T10:00:00+02:00
categories:
    - Networking
    - BGP
tags:
    - BGP
    - BGP Attributes
    - BGP Path Selection
image: "images/1.png"
---

## Introduction to BGP Attributes and Path Selection

The Border Gateway Protocol (BGP) is the routing protocol that is used to exchange routing information between autonomous systems (ASes) on the internet. BGP is a path vector protocol, which means that it uses a number of attributes to describe the path to a destination. These attributes are used by BGP to select the best path to a destination.

This article will provide a technical deep dive into BGP attributes and the BGP path selection process.

## BGP Attributes

BGP uses a number of attributes to describe the path to a destination. These attributes can be divided into two categories:

*   **Well-known attributes:** Well-known attributes are attributes that must be recognized by all BGP implementations.
*   **Optional attributes:** Optional attributes are attributes that do not need to be recognized by all BGP implementations.

Some of the most important BGP attributes include:

*   **AS_PATH:** The AS_PATH attribute is a list of the ASes that a route has traversed. It is used to prevent routing loops.
*   **NEXT_HOP:** The NEXT_HOP attribute is the IP address of the next hop router to a destination.
*   **LOCAL_PREF:** The LOCAL_PREF attribute is a value that is used to prefer one route over another. It is only used within an AS.
*   **MED (Multi-Exit Discriminator):** The MED attribute is a value that is used to prefer one route over another. It is used between ASes.
*   **COMMUNITY:** The COMMUNITY attribute is a value that is used to group routes together.

## The BGP Path Selection Process

The BGP path selection process is the process that BGP uses to select the best path to a destination. The BGP path selection process is a complex process that involves a number of different steps.

The BGP path selection process is as follows:

1.  **Select the path with the highest WEIGHT:** The WEIGHT attribute is a Cisco proprietary attribute that is used to prefer one route over another. It is only used on a single router.
2.  **Select the path with the highest LOCAL_PREF:** The LOCAL_PREF attribute is a value that is used to prefer one route over another. It is only used within an AS.
3.  **Select the path that was locally originated:** A locally originated route is a route that was originated by the local router.
4.  **Select the path with the shortest AS_PATH:** The AS_PATH attribute is a list of the ASes that a route has traversed.
5.  **Select the path with the lowest ORIGIN type:** The ORIGIN attribute is an attribute that indicates how a route was learned. The possible values are IGP, EGP, and INCOMPLETE.
6.  **Select the path with the lowest MED:** The MED attribute is a value that is used to prefer one route over another. It is used between ASes.
7.  **Prefer eBGP over iBGP paths:** eBGP is the BGP that is used between ASes. iBGP is the BGP that is used within an AS.
8.  **Select the path with the lowest IGP metric to the BGP next hop:** The IGP metric is the metric that is used by the Interior Gateway Protocol (IGP) to calculate the cost to a destination.
9.  **Select the path with the oldest eBGP route:** This step is used to prevent route flapping.
10. **Select the path with the lowest router ID:** The router ID is a unique identifier for a router.
11. **Select the path with the lowest cluster list length:** The cluster list is a list of the route reflectors that a route has traversed.
12. **Select the path with the lowest neighbor address:** The neighbor address is the IP address of the BGP neighbor that advertised the route.

## Conclusion

BGP attributes and the BGP path selection process are two of the most important concepts in BGP. BGP attributes are used to describe the path to a destination, and the BGP path selection process is the process that BGP uses to select the best path to a destination. A deep understanding of BGP attributes and the BGP path selection process is essential for anyone who is responsible for managing a BGP network.
