# Releases & rollback

See which releases exist, how they changed and how to undo a bad upgrade. Each upgrade creates a new numbered revision. For rollouts at the Kubernetes level, see [Deployments](../kubernetes/deployments.md).

### List releases in all namespaces

```bash
helm list -A
```

### Show the status of a release

```bash
helm status <release> -n <namespace>
```

### Show the revision history of a release

```bash
helm history <release> -n <namespace>
```

Use the revision numbers from this list with `helm rollback`.

### Roll back a release to a revision

```bash
helm rollback <release> <revision> -n <namespace> --wait
```

A rollback creates a new revision with the old content; it does not rewind the history.

### ⚠ Uninstall a release

```bash
helm uninstall <release> -n <namespace>
```

!!! warning
    All Kubernetes resources created by the release are deleted, and the release history is removed so you can no longer roll back. Data stored in chart-managed resources is lost.

See also the official [Helm command reference](https://helm.sh/docs/helm/).
