# DNS

Query and debug name resolution. `dig` ships with the `bind-utils` / `dnsutils` packages. `resolvectl` only exists on systems running systemd-resolved (Linux). Examples use `example.com`.

### Look up the IPv4 address of a name

```bash
dig +short example.com
```

### Look up a specific record type

```bash
dig +short example.com MX
```

Other common types: `A`, `AAAA`, `NS`, `TXT`, `CNAME`, `SOA`.

### Query a specific DNS server

```bash
dig @<server> example.com
```

### Trace delegation from the root servers

```bash
dig +trace example.com
```

### Reverse lookup of an IP address

```bash
dig -x 203.0.113.10 +short
```

### Show the DNS servers systemd-resolved uses

```bash
resolvectl status
```
