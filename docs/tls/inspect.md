# Inspect certificates

Read the contents of a certificate file, check how long it stays valid and confirm it chains to a CA. Every command here works on local PEM files. To fetch a certificate from a server first, see [Check remote endpoints](remote.md).

These pages use OpenSSL 3 syntax. On macOS the built-in `openssl` is LibreSSL, which lacks some options (such as `-ext`); check with `openssl version` and install OpenSSL 3 (for example with Homebrew) if a flag is rejected.

### Show the full text of a certificate

```bash
openssl x509 -in <cert.pem> -noout -text
```

`-noout` suppresses the PEM re-encoding so only the decoded fields are printed.

### Show subject, issuer and validity of a certificate file

```bash
openssl x509 -in <cert.pem> -noout -subject -issuer -dates
```

### Show the SHA-256 fingerprint of a certificate

```bash
openssl x509 -in <cert.pem> -noout -fingerprint -sha256
```

Compare this value with the one your CA or a colleague gives you to confirm you hold the same certificate.

### List the hostnames a certificate covers

```bash
openssl x509 -in <cert.pem> -noout -ext subjectAltName
```

Modern clients match the hostname against the Subject Alternative Names, not the common name.

### Check whether a certificate file expires within a period

```bash
openssl x509 -in <cert.pem> -noout -checkend <seconds>
```

Exits 0 if the certificate is still valid after `<seconds>` seconds (86400 is one day), and 1 if it will have expired. Handy in cron jobs and monitoring scripts.

### Verify a certificate against a CA and intermediate

```bash
openssl verify -CAfile <ca.pem> -untrusted <intermediate.pem> <cert.pem>
```

Prints `<cert.pem>: OK` when the chain builds up to the trusted root in `<ca.pem>`. The intermediate is passed with `-untrusted` because it is only used to link the chain, not trusted on its own.

See also the [OpenSSL command documentation](https://docs.openssl.org/master/man1/).
