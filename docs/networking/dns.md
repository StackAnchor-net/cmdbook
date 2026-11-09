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

### Look up TXT records

```bash
dig +short example.com TXT
```

### Look up name servers of a domain

```bash
dig +short example.com NS
```

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

### Show only the answer section

```bash
dig example.com +noall +answer
```

Includes the TTL, which shows how long resolvers may cache the record.

### Resolve a name the way applications do

```bash
getent hosts example.com
```

Uses the system resolver order from `nsswitch.conf` (including `/etc/hosts`), unlike `dig`, which always queries DNS directly.

### Show the DNS servers systemd-resolved uses

```bash
resolvectl status
```

### Resolve a name through systemd-resolved

```bash
resolvectl query example.com
```

### Flush the systemd-resolved cache

```bash
sudo resolvectl flush-caches
```
