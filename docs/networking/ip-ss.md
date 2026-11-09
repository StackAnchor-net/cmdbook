# ip and ss

Inspect interfaces, routes and sockets with `iproute2`. These tools are Linux-only; on macOS use `ifconfig`, `netstat -rn` and `lsof -i`.

### Show interface addresses in brief form

```bash
ip -br addr
```

### Show the routing table

```bash
ip route
```

### Show which route and source address a destination uses

```bash
ip route get 198.51.100.7
```

### List listening TCP sockets with owning processes

```bash
sudo ss -tlnp
```

Without root, `-p` only shows your own processes.

### List established TCP connections with processes

```bash
sudo ss -tanp state established
```

### Show a socket usage summary

```bash
ss -s
```
