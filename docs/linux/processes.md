# Processes

Inspect and control running processes. `ps --sort` is GNU procps (Linux); on macOS/BSD use `ps aux -r` (CPU) or `ps aux -m` (memory) instead.

### List all processes with full command lines

```bash
ps aux
```

### Show the top 10 processes by CPU usage

```bash
ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu | head -n 11
```

Linux only (`--sort` is a procps option). The leading `-` means descending; the extra line is the header.

### Show the top 10 processes by memory usage

```bash
ps -eo pid,user,%cpu,%mem,rss,comm --sort=-%mem | head -n 11
```

`rss` is the resident memory in KiB.

### Find processes by name with their command lines

```bash
pgrep -a <name>
```

### Show the process tree

```bash
ps -ef --forest
```

### ⚠ Terminate a process gracefully by PID

```bash
kill <pid>
```

!!! warning
    Sends SIGTERM. The process may flush and exit cleanly, but any unsaved in-memory state is lost when it exits.

### ⚠ Force-kill a process by PID

```bash
kill -9 <pid>
```

!!! warning
    SIGKILL cannot be caught: no cleanup runs, so unsaved data, temp files and locks held by the process are left behind.

### ⚠ Kill all processes matching a name

```bash
pkill <name>
```

!!! warning
    Matches every process whose name contains the pattern and sends SIGTERM to all of them. Preview the matches with `pgrep -a <name>` first.

### List open files of a process

```bash
lsof -p <pid>
```

### Find which process listens on a port

```bash
lsof -i :<port>
```

Run as root to see processes owned by other users.

### Show uptime and load average

```bash
uptime
```

The three load numbers are 1, 5 and 15 minute averages; compare them with the CPU count from `nproc`.
