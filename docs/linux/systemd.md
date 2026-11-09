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

### Enable a service at boot and start it now

```bash
sudo systemctl enable --now <service>
```

### Reload systemd after editing unit files

```bash
sudo systemctl daemon-reload
```

### List failed units

```bash
systemctl --failed
```

### Show the unit file and drop-ins of a service

```bash
systemctl cat <service>
```

### List timers and when they fire next

```bash
systemctl list-timers
```

### Follow the logs of a service

```bash
journalctl -u <service> -f
```

### Show the last 100 log lines of a service

```bash
journalctl -u <service> -n 100 --no-pager
```

### Show logs since a point in time

```bash
journalctl -u <service> --since "1 hour ago"
```

`--since` also accepts timestamps such as `"2026-01-15 08:00:00"`.

### Show only errors from the current boot

```bash
journalctl -b -p err
```

### Show how much space the journal uses

```bash
journalctl --disk-usage
```

### ⚠ Shrink the journal to a maximum size

```bash
sudo journalctl --vacuum-size=<size>
```

!!! warning
    Deletes the oldest archived journal files until the total is under the limit (for example `500M`). Those log entries are lost permanently.
