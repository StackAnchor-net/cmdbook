# Disk

Check disk usage, mounts and block devices. `lsblk` and `findmnt` are Linux-only; `df`, `du` and `find` also work on macOS/BSD.

### Show free space per filesystem

```bash
df -h
```

### Show filesystem types alongside usage

```bash
df -hT
```

`-T` is GNU/Linux; omit it on macOS.

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

### Show the total size of a directory

```bash
du -sh <dir>
```

### Find files larger than 100 MB

```bash
find <dir> -type f -size +100M
```

### List the 10 largest files under a directory

```bash
find <dir> -type f -exec du -h {} + | sort -rh | head -n 10
```

### List block devices

```bash
lsblk
```

### List block devices with filesystem type, label and UUID

```bash
lsblk -f
```

### Show mounted filesystems as a tree

```bash
findmnt
```

### Show which filesystem holds a path

```bash
findmnt -T <path>
```
