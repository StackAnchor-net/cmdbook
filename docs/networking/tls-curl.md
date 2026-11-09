# TLS and curl

Debug HTTP and TLS endpoints with `curl`, `openssl` and `nc`. Examples use `example.com`.

### Show a verbose request with TLS handshake details

```bash
curl -v https://example.com
```

### Fetch only the response headers

```bash
curl -I https://example.com
```

### Follow redirects and show the final status code

```bash
curl -sSL -o /dev/null -w '%{http_code} %{url_effective}\n' https://example.com
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

### Set a connection and total timeout

```bash
curl --connect-timeout 5 --max-time 20 https://example.com
```

### Send a request with a custom header

```bash
curl -H 'Authorization: Bearer <token>' https://example.com/api
```

### Skip certificate verification

```bash
curl -k https://example.com
```

!!! warning
    `-k` disables certificate validation, so the connection is open to interception. Use it only to confirm that a certificate problem is the cause, never in scripts.

### Show the certificate chain a server presents

```bash
openssl s_client -connect example.com:443 -servername example.com -showcerts </dev/null
```

`-servername` sets SNI, required when one IP serves several hostnames. `</dev/null` makes it exit instead of waiting for input.

### Show certificate subject, issuer and validity dates

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Show only the certificate expiry date

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -enddate
```

### Check whether a certificate expires within 30 days

```bash
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -checkend 2592000
```

Prints "Certificate will expire" and exits 1 if it does; exits 0 otherwise.

### Show the dates of a local certificate file

```bash
openssl x509 -in <cert.pem> -noout -subject -issuer -dates
```

### Check whether a TCP port is open

```bash
nc -zv example.com <port>
```

`-z` scans without sending data, `-v` reports the result. Flags shown work with OpenBSD and macOS `nc`.
