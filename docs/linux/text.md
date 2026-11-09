# Text processing

Search and transform text with grep, sed, awk, sort and jq. Examples use GNU tools. BSD/macOS differs mainly in `sed -i` and a few `grep` flags.

### Search recursively for a string with line numbers

```bash
grep -rn "<text>" <dir>
```

### Search case-insensitively and list only matching files

```bash
grep -rli "<text>" <dir>
```

### Show lines of context around each match

```bash
grep -n -C 3 "<text>" <file>
```

`-B <n>` shows lines before and `-A <n>` lines after the match.

### Show lines that do not match a pattern

```bash
grep -v "<text>" <file>
```

### Replace text in place in a file

```bash
sed -i 's/<old>/<new>/g' <file>
```

GNU sed. On macOS/BSD, `-i` requires a backup suffix argument: `sed -i '' 's/<old>/<new>/g' <file>`. To work on both, use `sed -i.bak ...` and delete the `.bak` file afterwards.

### Print a line range of a file

```bash
sed -n '10,20p' <file>
```

### Print one column from whitespace-separated text

```bash
awk '{print $2}' <file>
```

### Sum a numeric column

```bash
awk '{sum += $1} END {print sum}' <file>
```

### Count occurrences of each distinct line, most frequent first

```bash
sort <file> | uniq -c | sort -rn
```

### Follow a log file and survive rotation

```bash
tail -F <file>
```

`-F` keeps retrying if the file is rotated or recreated; `-f` does not.

### Pretty-print JSON

```bash
jq . <file.json>
```

### Extract a field from JSON

```bash
jq -r '.<field>' <file.json>
```

### Extract a field from every element of a JSON array

```bash
jq -r '.[].<field>' <file.json>
```

### Filter JSON array elements by a field value

```bash
jq '.[] | select(.<field> == "<value>")' <file.json>
```
