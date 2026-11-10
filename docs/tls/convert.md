# Convert formats

Switch between PEM (Base64 text), DER (binary) and PKCS#12 bundles, protect keys with a passphrase, and generate random secrets.

### Convert a certificate from PEM to DER

```bash
openssl x509 -in <cert.pem> -outform DER -out <cert.der>
```

### Convert a certificate from DER to PEM

```bash
openssl x509 -in <cert.der> -inform DER -out <cert.pem>
```

### Bundle a key and certificate into a PKCS#12 file

```bash
openssl pkcs12 -export -inkey <key.pem> -in <cert.pem> -out <bundle.p12>
```

Prompts for an export password. Add `-certfile <chain.pem>` to include intermediate certificates in the bundle.

### Extract the key and certificates from a PKCS#12 file

```bash
openssl pkcs12 -in <bundle.p12> -nodes -out <all.pem>
```

!!! warning
    `-nodes` writes the private key to `<all.pem>` **unencrypted**. Protect the file with strict permissions and delete it when you are done.

### Add a passphrase to a private key

```bash
openssl pkey -in <key.pem> -aes256 -out <encrypted-key.pem>
```

Prompts for the new passphrase. To go the other way, run `openssl pkey -in <encrypted-key.pem> -out <key.pem>`, which asks for the passphrase and writes an unencrypted copy.

### Generate a random Base64 secret

```bash
openssl rand -base64 32
```

Prints 32 random bytes encoded as Base64, useful for passwords, tokens and shared secrets.

See also the [OpenSSL command documentation](https://docs.openssl.org/master/man1/).
