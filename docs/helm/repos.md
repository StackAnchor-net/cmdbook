# Repositories & charts

Add chart repositories, find charts and look at a chart before you install it. Repository commands only change your local Helm configuration, not the cluster.

## Repositories

### Add a chart repository

```bash
helm repo add <name> <url>
```

For example, `helm repo add example https://charts.example.com`.

### Refresh the local repository index

```bash
helm repo update
```

Run this before searching or installing so you see the newest chart versions.

### List configured repositories

```bash
helm repo list
```

## Finding charts

### Search added repositories for a chart

```bash
helm search repo <keyword>
```

### List every available version of a chart

```bash
helm search repo <repo>/<chart> --versions
```

### Search Artifact Hub for a chart

```bash
helm search hub <keyword>
```

This queries Artifact Hub over the network and does not need any repository added.

## Fetching a chart

### Download a chart and unpack it

```bash
helm pull <repo>/<chart> --untar
```

Without `--untar` you get the packaged `.tgz` archive instead of a directory.

See also the official [Helm command reference](https://helm.sh/docs/helm/).
