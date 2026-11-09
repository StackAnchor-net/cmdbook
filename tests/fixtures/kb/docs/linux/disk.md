# Disk

Intro prose with `<not-a-heading>` and a table.

| a | b |
|---|---|
| 1 | 2 |

### Show disk usage

```bash
df -h
```

### Sample output only

```text
Filesystem  Size
```

### Heading without a block

Just prose here.

### Two blocks

```text
ignored
```

```bash
first-one
```

```bash
second-one
```

### ⚠ Wipe a device

```bash
dd if=/dev/zero of=<device> bs=1M
```

!!! warning
    All data on the device is lost.

### Multi-line command

```bash
kubectl apply -f - <<EOF
a: 1
EOF
echo done 2>&1
```

## Fence trap

```text
### Not a heading
```

```bash
echo trapped
```

### Tilde fence

~~~bash extra words
ls -la <dir>
~~~

### Long fence

````bash
echo ```
````

### Text fence containing fake things

```text
### inside text fence
~~~bash
not-a-block
~~~
```

### Real one after

```bash
echo real
```
