# Inspect & debug

Check what a release was deployed with, and render or validate charts locally before they touch the cluster. If a release misbehaves, continue with [Kubernetes debugging](../kubernetes/debugging.md).

## Deployed releases

### Show the values you set on a release

```bash
helm get values <release> -n <namespace>
```

### Show all values of a release, defaults included

```bash
helm get values <release> -n <namespace> --all
```

### Show the manifests a release applied

```bash
helm get manifest <release> -n <namespace>
```

## Charts

### Show the default values of a chart

```bash
helm show values <repo>/<chart>
```

Save the output to a file and edit it to build your own values file.

### Show the metadata of a chart

```bash
helm show chart <repo>/<chart>
```

### Render a chart to YAML locally

```bash
helm template <release> <chart-dir> -f <values.yaml>
```

Pipe the output to `kubectl diff -f -` or a file to review it.

### Check a chart for problems

```bash
helm lint <chart-dir>
```

See also the official [Helm command reference](https://helm.sh/docs/helm/).
