# Connecting & config

Log in, run one-off commands, debug failed connections and manage host keys. Never turn off host key checking to get past a warning; verify the key instead.

## Logging in

### Install your public key on a server

```bash
ssh-copy-id -i <key-file.pub> <user>@<host>
```

Appends the key to `~/.ssh/authorized_keys` on the server. This needs a working password (or other) login once.

### Connect with a specific key and port

```bash
ssh -i <key-file> -p <port> <user>@<host>
```

`-i` selects the identity file and `-p` the server port. Add `-o IdentitiesOnly=yes` if the agent offers so many keys that the server rejects you before yours is tried.

### Run a single command on a remote host

```bash
ssh <user>@<host> '<command>'
```

Quote the command so your local shell does not expand it. Add `-T` for non-interactive use in scripts.

## Debugging

### Debug a failing connection

```bash
ssh -v <user>@<host>
```

Shows which keys are offered and where authentication fails. Repeat the flag (`-vv`, `-vvv`) for more detail.

### Show the effective client config for a host

```bash
ssh -G <host>
```

Prints every option after `~/.ssh/config` and defaults are applied, without connecting. Handy to confirm that a `Host` block matched.

## Host keys

### Fetch and check a server's host key fingerprint

```bash
ssh-keyscan -t ed25519 <host> | ssh-keygen -lf -
```

Compare the printed fingerprint with one the server admin gave you over a trusted channel before you accept it. Do not append the raw scan to `known_hosts` blindly.

### ⚠ Remove a host from your known hosts file

```bash
ssh-keygen -R <host>
```

!!! warning
    Deletes every `known_hosts` entry for that host, so the next connection asks you to trust its key again. Only do this after confirming that the host key really changed, for example after a rebuild; an unexpected change can also mean someone is intercepting the connection. A backup is left in `known_hosts.old`.

See also the [OpenSSH manual pages](https://www.openssh.com/manual.html).
