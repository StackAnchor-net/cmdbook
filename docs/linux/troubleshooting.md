# Troubleshooting

A symptom-first checklist for common Linux problems. Find what is going wrong, run the first command, and follow the links to the detailed pages when a symptom is covered elsewhere.

## Disk full

Start with `df -h` and `df -i` from [Disk](disk.md) to see whether you ran out of space or out of inodes ("No space left on device" with free blocks usually means inodes).

### Find the largest subdirectories of a directory

```bash
sudo du -xh --max-depth=1 <dir> | sort -rh | head -n 10
```

`-x` stays on one filesystem and `--max-depth=1` limits the report to direct children. `sort -rh` puts the biggest first.

### List deleted files that processes still hold open

```bash
sudo lsof +L1
```

If `df` reports a full disk but `du` cannot find the data, a deleted log file may still be open. The space returns once the owning process is restarted or closes the file.

## Service will not start

Begin with `systemctl status <service>` from [systemd](systemd.md).

### Read the recent log lines of a failing service

```bash
journalctl -u <service> --since "10 minutes ago"
```

For other time windows and boot-level errors see [systemd](systemd.md).

## No network connectivity

Check addresses and routes first (`ip -br addr`, `ip route` in [ip and ss](../networking/ip-ss.md)).

### Test reachability of a host with a fixed number of packets

```bash
ping -c 4 <host>
```

Ping your default gateway's IP first (shown as `via <address>` by `ip route`), then a known external IP, then a name. If the IPs work but the name does not, move on to DNS.

## DNS resolution fails

Compare your resolver with a direct query using the `dig` commands in [DNS](../networking/dns.md), and use `resolvectl status` there on systemd-resolved systems.

### Show which nameservers the system is configured to use

```bash
cat /etc/resolv.conf
```

On systemd-resolved hosts this is often a stub pointing to a local address. `sudo systemctl restart systemd-resolved` restarts the resolver if it is wedged.

## Permission denied

### Show the permissions of every component in a path

```bash
namei -l <path>
```

A missing execute bit on any parent directory also causes "Permission denied", not just the file's own mode.

### Inspect recent SELinux denials

```bash
sudo ausearch -m avc -ts recent
```

On SELinux systems (RHEL, Fedora) a denial can occur even when the Unix permissions are right. Fix the label or policy; switching SELinux to permissive or disabled is a last resort.

## Unresponsive process

Find it with `pgrep -a <name>` and ask it to stop with `kill <pid>` or `pkill <name>` ([Processes](processes.md)); escalate only if that fails.

### ⚠ Force-kill a process that ignores a normal kill

```bash
kill -9 <pid>
```

!!! warning
    `SIGKILL` cannot be caught, so the process gets no chance to flush buffers, remove lock files or close connections. Unsaved data and in-flight work are lost. A process stuck in uninterruptible sleep (state `D`) will not die until its I/O completes.

## High CPU or memory

For a ranked list of processes see [Processes](processes.md).

### Watch CPU, memory, swap and I/O wait every 2 seconds

```bash
vmstat 2
```

Persistent non-zero `si`/`so` columns mean swapping; a high `wa` means the CPU is waiting on disk.

### Show total, used and available memory

```bash
free -h
```

Judge memory by the `available` column rather than `free`, because the kernel uses spare RAM for cache.

## SSH connection refused or timing out

A literal "Connection refused" usually means nothing is listening (the daemon is stopped, or bound to another port or address): confirm it with `sudo ss -tlnp` ([ip and ss](../networking/ip-ss.md)). The SSH unit is `ssh` on Debian/Ubuntu and `sshd` on RHEL/Fedora, so use that name with `systemctl status <service>` ([systemd](systemd.md)). A timeout usually points to a firewall silently dropping packets, so check that next (a REJECT rule can also produce "refused").

### Check whether the firewall allows SSH

```bash
sudo ufw status
```

`ufw` is the default on Ubuntu. On systems that use nftables or firewalld, run `sudo nft list ruleset` instead (plain `iptables -L` may show nothing there).

## Cron job not running

### Read the cron daemon's log for today

```bash
journalctl -u cron --since today
```

The unit is `cron` on Debian/Ubuntu and `crond` on RHEL/Fedora. On Debian/Ubuntu with rsyslog you can also `grep CRON /var/log/syslog`, a file that does not exist on RHEL.

## Filesystem errors

### ⚠ Check and repair an unmounted filesystem

```bash
sudo fsck <device>
```

!!! warning
    Run it only on an unmounted filesystem (`sudo umount <device>`); the root filesystem needs a live or rescue boot. Repairs can discard damaged files or directory entries, so back up or image the device first.

Topics based on Neel Shah's [Linux troubleshooting cheat sheet](https://www.linkedin.com/posts/neelcshah_devops-cloud-linux-share-7303435732763787264-Mm-v/).
