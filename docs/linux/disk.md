# Disk

Check disk usage and block devices. `lsblk` is Linux-only; `df`, `du` and `find` also work on macOS/BSD.

### Show free space per filesystem

```bash
df -h
```

### Show inode usage per filesystem

```bash
df -i
```

A filesystem can report "No space left on device" with free blocks when it runs out of inodes.

### Show the size of each subdirectory, largest last

```bash
du -h -d 1 <dir> | sort -h
```

`-d 1` works on GNU and BSD; GNU also accepts the long form `--max-depth=1`. `sort -h` sorts human-readable sizes (GNU sort, recent BSD sort).

### Find files larger than 100 MB

```bash
find <dir> -type f -size +100M
```

### List block devices

```bash
lsblk
```
