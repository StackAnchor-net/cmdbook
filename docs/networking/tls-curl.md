# TLS and curl

Debug HTTP and TLS endpoints with `curl`, `openssl` and `nc`. Examples use `example.com`.

### Show a verbose request with TLS handshake details

```bash
curl -v https://example.com
```

### Break down request timing

```bash
curl -sS -o /dev/null -w 'dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\n' https://example.com
```

All values are cumulative seconds from the start of the request.

### Send a request to a specific IP while keeping the hostname

```bash
curl --resolve example.com:443:203.0.113.10 https://example.com
```

Bypasses DNS, which is useful to test a new server before changing records. SNI and the `Host` header still use `example.com`.

### Skip certificate verification

```bash
curl -k https://example.com
```

!!! warning
    `-k` disables certificate validation, so the connection is open to interception. Use it only to confirm that a certificate problem is the cause, never in scripts.

### Show certificate subject, issuer and validity dates

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Check whether a certificate expires within 30 days

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -checkend 2592000
```

Prints "Certificate will expire" and exits 1 if it does; exits 0 otherwise.

### Check whether a TCP port is open

```bash
nc -zv example.com <port>
```

`-z` scans without sending data, `-v` reports the result. Flags shown work with OpenBSD and macOS `nc`.
