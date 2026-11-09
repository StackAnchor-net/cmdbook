# systemd

Manage services and read logs on systemd-based Linux distributions. Everything on this page is Linux-only. Most `systemctl` changes need root, so prefix with `sudo`.

### Show the status of a service

```bash
systemctl status <service>
```

### Restart a service

```bash
sudo systemctl restart <service>
```

### List failed units

```bash
systemctl --failed
```

### Follow the logs of a service

```bash
journalctl -u <service> -f
```

### ⚠ Shrink the journal to a maximum size

```bash
sudo journalctl --vacuum-size=<size>
```

!!! warning
    Deletes the oldest archived journal files until the total is under the limit (for example `500M`). Those log entries are lost permanently.
