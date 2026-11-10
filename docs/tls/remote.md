# Check remote endpoints

Use `openssl s_client` to see what a server presents during the TLS handshake: its certificate chain, supported protocol versions and STARTTLS behaviour. Commands pipe `/dev/null` into `s_client` so it exits after the handshake instead of waiting for input. For quick subject, issuer and expiry checks against a server, see [TLS and curl](../networking/tls-curl.md).

### Show the full certificate chain a server sends

```bash
openssl s_client -connect <host>:443 -servername <host> -showcerts </dev/null
```

`-servername` sets SNI, which servers hosting several sites need in order to pick the right certificate.

### Test whether a server accepts TLS 1.2

```bash
openssl s_client -connect <host>:443 -servername <host> -tls1_2 </dev/null
```

A successful handshake prints the negotiated protocol and cipher; a failure prints a handshake error.

### Test whether a server accepts TLS 1.3

```bash
openssl s_client -connect <host>:443 -servername <host> -tls1_3 </dev/null
```

### Verify a server certificate against a hostname

```bash
openssl s_client -connect <host>:443 -servername <host> -verify_hostname <host> -verify_return_error </dev/null
```

Fails the handshake if the chain does not verify against the system trust store or the name does not match. Look for `Verification: OK` in the output.

### Check whether a server staples an OCSP response

```bash
openssl s_client -connect <host>:443 -servername <host> -status </dev/null
```

Look for an `OCSP Response Status` section in the output, or "no response sent" if stapling is off.

### Test STARTTLS on a mail submission port

```bash
openssl s_client -starttls smtp -connect <host>:587 -servername <host> </dev/null
```

Other values for `-starttls` include `imap`, `pop3` and `ftp`; use the matching port.

See also the [OpenSSL command documentation](https://docs.openssl.org/master/man1/).
