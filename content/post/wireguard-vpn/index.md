---
title: "How to create a Site-to-Site VPN with WireGuard"
description: "A comprehensive guide to setting up a secure and efficient site-to-site VPN using WireGuard."
slug: "wireguard-site-to-site-vpn"
date: 2024-07-27T10:00:00+02:00
categories:
    - Networking
tags:
    - WireGuard
    - VPN
    - Security
---

## Introduction

WireGuard is a modern, fast, and secure VPN that is easy to configure. In this guide, we will walk through the process of setting up a site-to-site VPN using WireGuard. This will allow you to securely connect two networks, for example, your office network and your home network.

### Prerequisites

*   Two Linux servers, each on a different network. We will call them `site-a` and `site-b`.
*   Root access to both servers.
*   A public IP address for each server.

## Step 1: Install WireGuard

First, we need to install WireGuard on both servers.

**On Debian/Ubuntu:**

```bash
sudo apt update
sudo apt install wireguard
```

**On CentOS/RHEL:**

```bash
sudo dnf install elrepo-release
sudo dnf install kmod-wireguard wireguard-tools
```

## Step 2: Generate Keys

WireGuard works by encrypting traffic with public-key cryptography. Each server needs a private key and a public key.

**On both `site-a` and `site-b`:**

1.  Go to the WireGuard configuration directory:

    ```bash
    cd /etc/wireguard
    ```

2.  Generate the private and public keys:

    ```bash
    wg genkey | tee privatekey | wg pubkey > publickey
    ```

    This will create two files: `privatekey` and `publickey`.

3.  Secure the private key:

    ```bash
    chmod 600 privatekey
    ```

## Step 3: Configure WireGuard

Now we need to create a configuration file for each server.

### On `site-a`

1.  Create a new configuration file:

    ```bash
    sudo nano /etc/wireguard/wg0.conf
    ```

2.  Add the following content to the file. Replace the placeholders with your actual values.

    ```ini
    [Interface]
    Address = 10.0.1.1/24
    PrivateKey = <site-a-private-key>
    ListenPort = 51820

    [Peer]
    PublicKey = <site-b-public-key>
    Endpoint = <site-b-public-ip>:51820
    AllowedIPs = 10.0.2.0/24
    ```

    *   `Address`: The private IP address for `site-a`'s WireGuard interface.
    *   `PrivateKey`: The content of `site-a`'s `privatekey` file.
    *   `ListenPort`: The port WireGuard will listen on.
    *   `PublicKey`: The content of `site-b`'s `publickey` file.
    *   `Endpoint`: The public IP address and port of `site-b`.
    *   `AllowedIPs`: The IP address range of the network at `site-b`.

### On `site-b`

1.  Create a new configuration file:

    ```bash
    sudo nano /etc/wireguard/wg0.conf
    ```

2.  Add the following content to the file. Replace the placeholders with your actual values.

    ```ini
    [Interface]
    Address = 10.0.2.1/24
    PrivateKey = <site-b-private-key>
    ListenPort = 51820

    [Peer]
    PublicKey = <site-a-public-key>
    Endpoint = <site-a-public-ip>:51820
    AllowedIPs = 10.0.1.0/24
    ```

    *   `Address`: The private IP address for `site-b`'s WireGuard interface.
    *   `PrivateKey`: The content of `site-b`'s `privatekey` file.
    *   `ListenPort`: The port WireGuard will listen on.
    *   `PublicKey`: The content of `site-a`'s `publickey` file.
    *   `Endpoint`: The public IP address and port of `site-a`.
    *   `AllowedIPs`: The IP address range of the network at `site-a`.

## Step 4: Enable IP Forwarding

For the two sites to be able to communicate, we need to enable IP forwarding on both servers.

1.  Edit the `sysctl.conf` file:

    ```bash
    sudo nano /etc/sysctl.conf
    ```

2.  Uncomment the following line:

    ```
    net.ipv4.ip_forward=1
    ```

3.  Apply the changes:

    ```bash
    sudo sysctl -p
    ```

## Step 5: Start WireGuard

Now we can start the WireGuard service on both servers.

1.  Start the WireGuard interface:

    ```bash
    sudo wg-quick up wg0
    ```

2.  Enable the WireGuard service to start on boot:

    ```bash
    sudo systemctl enable wg-quick@wg0
    ```

## Step 6: Configure Firewall

You may need to configure your firewall to allow WireGuard traffic.

**On both servers (using ufw):**

```bash
sudo ufw allow 51820/udp
sudo ufw allow from 10.0.0.0/16 to any
```

## Conclusion

You should now have a working site-to-site VPN with WireGuard. You can test the connection by pinging one server from the other using their WireGuard IP addresses.

```bash
# From site-a
ping 10.0.2.1

# From site-b
ping 10.0.1.1
```
