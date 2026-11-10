# Keys & CSRs

Generate private keys, certificate signing requests and self-signed certificates. Keep key files out of version control.

!!! warning
    Commands with `-nodes` write the private key **unencrypted** to disk. Anyone who can read the file can impersonate the server, so restrict its permissions (for example `chmod 600`) and never commit it.

## Keys and CSRs

### Create a new key and CSR for a domain

```bash
openssl req -new -newkey rsa:2048 -nodes -keyout <key.pem> -out <csr.pem> -subj "/CN=<domain>"
```

Generates a 2048-bit RSA key (unencrypted, because of `-nodes`) and a signing request to send to your CA.

### Create a key and CSR with a subject alternative name

```bash
openssl req -new -newkey rsa:2048 -nodes -keyout <key.pem> -out <csr.pem> -subj "/CN=<domain>" -addext "subjectAltName=DNS:<domain>"
```

Add more names by comma-separating entries, for example `DNS:example.com,DNS:www.example.com`.

### Inspect a CSR and verify its signature

```bash
openssl req -in <csr.pem> -noout -text -verify
```

### Generate an EC private key on the P-256 curve

```bash
openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:P-256 -out <key.pem>
```

The key is written unencrypted. Use `openssl req -new -key <key.pem> ...` afterwards to make a CSR from it.

### Create a self-signed certificate

```bash
openssl req -x509 -newkey rsa:2048 -nodes -keyout <key.pem> -out <cert.pem> -days 365 -subj "/CN=<domain>" -addext "subjectAltName=DNS:<domain>"
```

Suitable for testing only; clients will not trust it unless you add it to their trust store. The key is unencrypted.

## Check that files match

### Hash the public key of a certificate

```bash
openssl x509 -noout -pubkey -in <cert.pem> | sha256sum
```

### Hash the public key of a private key

```bash
openssl pkey -pubout -in <key.pem> | sha256sum
```

Run both hash commands: if the two digests are identical, the private key belongs to the certificate. If `sha256sum` is missing (older macOS), use `shasum -a 256` instead. To compare a CSR instead of a certificate, hash the output of `openssl req -noout -pubkey -in <csr.pem>`.

See also the [OpenSSL command documentation](https://docs.openssl.org/master/man1/).
