# Keys & agent

Create SSH key pairs, inspect them and keep them loaded in an agent so you type a passphrase once per session. Prefer Ed25519 keys and protect every private key with a passphrase.

## Key pairs

### Generate an Ed25519 key pair

```bash
ssh-keygen -t ed25519 -C "<comment>" -f <key-file>
```

Writes the private key to `<key-file>` and the public key to `<key-file>.pub`. You are prompted for a passphrase; do not leave it empty on a laptop or shared host. The comment is only a label, such as `alice@example.com`.

### Show the fingerprint of a key

```bash
ssh-keygen -lf <key-file.pub>
```

Prints the size, SHA256 fingerprint, comment and type. Compare it with the fingerprint shown by your Git host or the server admin.

### Derive the public key from a private key

```bash
ssh-keygen -y -f <key-file>
```

Useful when the `.pub` file is lost. You are asked for the passphrase if the key has one.

### Change the passphrase of a private key

```bash
ssh-keygen -p -f <key-file>
```

Prompts for the old passphrase and then the new one. An empty new passphrase removes protection, so avoid that.

## ssh-agent

### Start an agent in the current shell

```bash
eval "$(ssh-agent -s)"
```

Starts `ssh-agent` and exports `SSH_AUTH_SOCK` into this shell. Many desktops and `systemd --user` already run an agent, so check `echo "$SSH_AUTH_SOCK"` first.

### Add a private key to the agent

```bash
ssh-add <key-file>
```

Asks for the passphrase once. Add `-t <seconds>` to have the agent forget the key after that lifetime.

### List the keys loaded in the agent

```bash
ssh-add -l
```

Shows one fingerprint per loaded key. It exits non-zero with "The agent has no identities" when the agent is empty.

See also the [OpenSSH manual pages](https://www.openssh.com/manual.html).
