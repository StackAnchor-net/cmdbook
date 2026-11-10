# Tunnels & jump hosts

Forward ports and reach hosts behind a bastion. `-N` means no remote command, so the session only carries the forwarding.

### Forward a local port to a remote service

```bash
ssh -N -L <local-port>:<target-host>:<target-port> <user>@<host>
```

Connections to `localhost:<local-port>` travel through `<host>` and come out to `<target-host>:<target-port>`, as seen from `<host>`. Use `localhost` as the target to reach a service listening only on the server itself.

### Expose a local service on a remote host

```bash
ssh -N -R <remote-port>:localhost:<local-port> <user>@<host>
```

A reverse tunnel: `<remote-port>` on the server forwards back to a port on your machine. By default it binds only to the server's loopback; exposing it further needs `GatewayPorts` in the server config.

### Start a SOCKS proxy through a host

```bash
ssh -N -D <port> <user>@<host>
```

Point a browser or tool at `socks5h://localhost:<port>` to send its traffic (and DNS lookups) through `<host>`.

### Connect through a jump host

```bash
ssh -J <user>@<jump-host> <user>@<host>
```

Opens the session to `<host>` through the bastion without giving the bastion your private key. Chain several hops with commas.

### Connect with agent forwarding

```bash
ssh -A <user>@<host>
```

!!! warning
    Anyone with root on `<host>` can use your forwarded agent while you are connected. Prefer `-J` (or `ProxyJump`) for reaching other hosts, and only use `-A` towards machines you fully trust.

## Make a jump host permanent

Put it in `~/.ssh/config` so a plain `ssh app` works, including for `scp` and `rsync`:

```text
Host bastion
    HostName bastion.example.com
    User alice

Host app
    HostName 198.51.100.20
    User alice
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
    ProxyJump bastion
```

Check the result with `ssh -G app` ([Connecting & config](connect.md)).

See also the [OpenSSH manual pages](https://www.openssh.com/manual.html).
