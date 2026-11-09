# Files

Find, archive and copy files. Examples use GNU tools.

### Find files modified in the last day

```bash
find <dir> -type f -mtime -1
```

`-mtime -1` means modified less than 24 hours ago. `find` ignores fractions of a day, so `-mtime +7` matches only files modified at least 8 days ago.

### ⚠ Delete files matching a name

```bash
find <dir> -type f -name "<pattern>" -delete
```

!!! warning
    Permanently deletes every matching file with no trash and no confirmation. Run the same command with `-print` instead of `-delete` first, and keep `-delete` as the last expression.

### Create a compressed tar archive

```bash
tar -czf <archive.tar.gz> <dir>
```

### Extract a tar archive into a directory

```bash
tar -xzf <archive.tar.gz> -C <dest>
```

The destination directory must already exist. Existing files with the same names are overwritten.

### Copy a directory with rsync and show progress

```bash
rsync -avh --progress <src>/ <dest>/
```

The trailing slash on the source copies its contents rather than the directory itself.
