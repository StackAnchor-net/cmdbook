# Files

Find, copy, archive and change files. Examples use GNU tools; the notes call out BSD/macOS differences.

### Find files by name

```bash
find <dir> -name "<pattern>"
```

Quote the pattern so the shell does not expand it, for example `"*.log"`.

### Find files modified in the last day

```bash
find <dir> -type f -mtime -1
```

`-mtime -1` means less than 24 hours ago; `-mtime +7` means more than 7 days ago.

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

### List the contents of a tar archive

```bash
tar -tzf <archive.tar.gz>
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

### Preview what rsync would transfer

```bash
rsync -avhn <src>/ <dest>/
```

`-n` (`--dry-run`) makes no changes.

### Copy to a remote host over SSH

```bash
rsync -avzh --progress <src>/ <user>@example.com:<dest>/
```

### Make a file executable

```bash
chmod +x <file>
```

### Change permissions recursively

```bash
chmod -R u=rwX,g=rX,o= <dir>
```

Capital `X` sets execute only on directories and files that are already executable.

### Change owner and group recursively

```bash
sudo chown -R <user>:<group> <dir>
```

### Show detailed file metadata

```bash
stat <file>
```

### Print the permissions and owner of a file

```bash
stat -c '%a %U:%G %n' <file>
```

GNU `stat` syntax; on macOS/BSD use `stat -f '%Lp %Su:%Sg %N' <file>`.
