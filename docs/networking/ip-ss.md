# ip and ss

Inspect interfaces, routes and sockets with `iproute2`. These tools are Linux-only; on macOS use `ifconfig`, `netstat -rn` and `lsof -i`.

### Show interface addresses in brief form

```bash
ip -br addr
```

### Show link state of all interfaces

```bash
ip -br link
```

### Show the routing table

```bash
ip route
```

### Show which route and source address a destination uses

```bash
ip route get 198.51.100.7
```

### Show the neighbor (ARP/NDP) table

```bash
ip neigh
```

### Add an IP address to an interface

```bash
sudo ip addr add 192.0.2.10/24 dev <interface>
```

The change is not persistent; it is lost on reboot or when the network manager reconfigures the interface.

### List listening TCP sockets with owning processes

```bash
sudo ss -tlnp
```

Without root, `-p` only shows your own processes.

### List listening UDP sockets

```bash
sudo ss -ulnp
```

### List established TCP connections with processes

```bash
sudo ss -tanp state established
```

### Count TCP connections by state

```bash
ss -tan | awk 'NR>1 {print $1}' | sort | uniq -c | sort -rn
```

### Show sockets using a given port

```bash
ss -tan '( sport = :<port> or dport = :<port> )'
```

### Show a socket usage summary

```bash
ss -s
```
