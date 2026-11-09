# Config

Contexts, namespaces, ConfigMaps and Secrets.

### Switch to another context

```bash
kubectl config use-context <context>
```

### Set the default namespace for the current context

```bash
kubectl config set-context --current --namespace=<namespace>
```

### Decode one key of a Secret

```bash
kubectl get secret <secret> -o jsonpath='{.data.<key>}' | base64 -d
```

Secret values are base64-encoded, not encrypted. Keys that contain dots must be escaped in the JSONPath, for example `{.data.tls\.crt}`.

### Apply a manifest

```bash
kubectl apply -f <file.yaml>
```

### ⚠ Delete the resources defined in a manifest

```bash
kubectl delete -f <file.yaml>
```

!!! warning
    Every resource listed in the file is deleted from the cluster, including the data of any PersistentVolumeClaims it defines when the volume's reclaim policy is `Delete`.
