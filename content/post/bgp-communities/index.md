---
title: "A Deep Dive into BGP Communities"
description: "A technical exploration of BGP communities, a powerful tool for tagging and filtering BGP routes."
slug: "bgp-communities"
date: 2026-01-25T10:00:00+02:00
categories:
    - Networking
    - BGP
tags:
    - BGP
    - BGP Communities
image: "images/1.png"
---

## Introduction to BGP Communities

The BGP community attribute is a powerful tool for tagging and filtering BGP routes. It is a transitive optional attribute, which means that it can be passed from one AS to another. BGP communities are used to group routes together so that they can be treated in the same way.

This article will provide a technical deep dive into BGP communities, exploring the different types of BGP communities, how they are used, and how they can be configured.

## Types of BGP Communities

There are two main types of BGP communities:

*   **Standard Communities:** Standard communities are 32-bit values that are divided into two 16-bit parts. The first part is the AS number of the AS that originated the community, and the second part is a value that is defined by the AS.
*   **Extended Communities:** Extended communities are 64-bit values that provide a more flexible way to tag and filter BGP routes. They can be used to encode a wide range of information, such as the origin of a route, the type of a route, and the VPN that a route belongs to.

## Well-Known BGP Communities

There are a number of well-known BGP communities that have a special meaning. Some of the most important well-known BGP communities include:

*   **NO_EXPORT:** The NO_EXPORT community tells a BGP router not to advertise a route to any eBGP peers.
*   **NO_ADVERTISE:** The NO_ADVERTISE community tells a BGP router not to advertise a route to any BGP peers.
*   **LOCAL_AS:** The LOCAL_AS community tells a BGP router not to advertise a route outside of the local AS.

## How BGP Communities Are Used

BGP communities are used for a wide range of purposes, including:

*   **Route Filtering:** BGP communities can be used to filter routes. For example, a BGP router can be configured to only accept routes that have a particular community value.
*   **Route Policy:** BGP communities can be used to apply a policy to a set of routes. For example, a BGP router can be configured to set the LOCAL_PREF attribute of all routes that have a particular community value.
*   **VPNs:** BGP communities are used to identify the VPN that a route belongs to. This is essential for MPLS L3VPNs.

## Configuring BGP Communities

BGP communities can be configured on a BGP router using a route map. A route map is a set of rules that are used to match and modify BGP routes.

The following is an example of a route map that is used to set the community value of a BGP route:

```
route-map SET_COMMUNITY permit 10
 set community 100:10
```

This route map will set the community value of all BGP routes that match the route map to 100:10.

## Conclusion

BGP communities are a powerful tool for tagging and filtering BGP routes. They are used for a wide range of purposes, including route filtering, route policy, and VPNs. A deep understanding of BGP communities is essential for anyone who is responsible for managing a BGP network.
