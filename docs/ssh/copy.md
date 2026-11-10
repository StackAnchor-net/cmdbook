# Copying files

Transfer files over SSH with `scp`, `sftp` and `rsync`. For local copies with `rsync` see [Files](../linux/files.md). Note that `scp` uses `-P` for the port while `ssh` uses `-p`.

## scp and sftp

### Upload a file with scp

```bash
scp -P <port> <file> <user>@<host>:<path>
```

Omit `-P` for the default port 22.

### Download a file with scp

```bash
scp <user>@<host>:<remote-file> <local-dir>/
```

### Copy a directory recursively with scp

```bash
scp -r <dir> <user>@<host>:<path>
```

### Open an interactive sftp session

```bash
sftp -P <port> <user>@<host>
```

Inside the session use `ls`, `cd`, `get <file>` and `put <file>`; `lcd` and `lls` act on the local side.

## rsync over SSH

Trailing slashes matter: `<src>/` copies the contents of the directory, while `<src>` without a slash creates the directory itself inside the destination.

### Sync a directory to a remote host

```bash
rsync -avz -e 'ssh -p <port>' <src>/ <user>@<host>:<dest>/
```

`-a` keeps permissions and times, `-z` compresses in transit. Re-running it only sends what changed.

### Preview what rsync would change

```bash
rsync -avzn -e 'ssh -p <port>' <src>/ <user>@<host>:<dest>/
```

`-n` (`--dry-run`) lists the transfers without making any.

### ⚠ Sync and delete extra files on the destination

```bash
rsync -avz --delete -e 'ssh -p <port>' <src>/ <user>@<host>:<dest>/
```

!!! warning
    `--delete` removes every file in `<dest>` that does not exist in `<src>`, with no trash. Run it first with `-n` (previous command plus `--delete`) and check the list, and double-check the trailing slashes.

See also the [OpenSSH manual pages](https://www.openssh.com/manual.html).
