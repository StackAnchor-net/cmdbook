# Text processing

Search and transform text with grep, sed, sort and jq. Examples use GNU tools. BSD/macOS differs mainly in `sed -i` and a few `grep` flags.

### Search recursively for a string with line numbers

```bash
grep -rn "<text>" <dir>
```

### Replace text in place in a file

```bash
sed -i 's/<old>/<new>/g' <file>
```

GNU sed. On macOS/BSD, `-i` requires a backup suffix argument: `sed -i '' 's/<old>/<new>/g' <file>`. To work on both, use `sed -i.bak ...` and delete the `.bak` file afterwards.

### Count occurrences of each distinct line, most frequent first

```bash
sort <file> | uniq -c | sort -rn
```

### Pretty-print JSON

```bash
jq . <file.json>
```
