# Config

Contexts, namespaces, ConfigMaps and Secrets.

## Contexts and namespaces

### List available contexts

```bash
kubectl config get-contexts
```

### Show the current context

```bash
kubectl config current-context
```

### Switch to another context

```bash
kubectl config use-context <context>
```

### Set the default namespace for the current context

```bash
kubectl config set-context --current --namespace=<namespace>
```

### Show the active kubeconfig without credentials

```bash
kubectl config view --minify
```

## ConfigMaps and Secrets

### List ConfigMaps

```bash
kubectl get configmaps -n <namespace>
```

### Show a ConfigMap as YAML

```bash
kubectl get configmap <configmap> -o yaml
```

### List Secrets

```bash
kubectl get secrets -n <namespace>
```

### Decode one key of a Secret

```bash
kubectl get secret <secret> -o jsonpath='{.data.<key>}' | base64 -d
```

Secret values are base64-encoded, not encrypted. Keys that contain dots must be escaped in the JSONPath, for example `{.data.tls\.crt}`.

## Applying manifests

### Preview what a manifest would change

```bash
kubectl diff -f <file.yaml>
```

### Apply a manifest

```bash
kubectl apply -f <file.yaml>
```

### Validate a manifest against the server without applying it

```bash
kubectl apply -f <file.yaml> --dry-run=server
```

### ⚠ Delete the resources defined in a manifest

```bash
kubectl delete -f <file.yaml>
```

!!! warning
    Every resource listed in the file is deleted from the cluster, including the data of any PersistentVolumeClaims it defines when the volume's reclaim policy is `Delete`.

## Discovering the API

### Show documentation for a resource field

```bash
kubectl explain pod.spec.containers
```

### List resource types the cluster supports

```bash
kubectl api-resources
```
