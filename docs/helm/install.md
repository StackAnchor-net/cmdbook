# Install & upgrade

Install a chart as a release and change it later. Releases live in a namespace, so pass `-n` (or `--namespace`) consistently. To check what the chart created, see the [Kubernetes pods](../kubernetes/pods.md) and [deployments](../kubernetes/deployments.md) pages.

### Install a chart into a new namespace

```bash
helm install <release> <repo>/<chart> --namespace <namespace> --create-namespace --version <version>
```

Pinning `--version` keeps installs repeatable; without it Helm picks the latest version.

### Install with a values file and an override

```bash
helm install <release> <repo>/<chart> -n <namespace> -f <values.yaml> --set <key>=<value>
```

`--set` wins over values from `-f`, and later `-f` files win over earlier ones.

### Preview an install without creating anything

```bash
helm install <release> <repo>/<chart> -n <namespace> -f <values.yaml> --dry-run --debug
```

Renders the manifests and prints them. Nothing is applied to the cluster.

### Install or upgrade, rolling back on failure

```bash
helm upgrade --install <release> <repo>/<chart> -n <namespace> -f <values.yaml> --atomic --wait --timeout 5m
```

`--wait` blocks until resources are ready. `--atomic` rolls the release back if that fails (Helm 4 renames it `--rollback-on-failure`, and still accepts `--atomic`). A good fit for CI pipelines.

### Upgrade a release keeping its earlier values

```bash
helm upgrade <release> <repo>/<chart> -n <namespace> --reuse-values --set <key>=<value>
```

Without `--reuse-values` (or `--reset-then-reuse-values`), values you set on a previous install are reset to chart defaults.

### Fetch the subcharts a chart depends on

```bash
helm dependency update <chart-dir>
```

Downloads the charts listed under `dependencies` in `Chart.yaml` into `charts/` and refreshes `Chart.lock`.

See also the official [Helm command reference](https://helm.sh/docs/helm/).
