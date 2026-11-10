# Config

Contexts, namespaces, ConfigMaps and Secrets, plus a few commands to explore the cluster and its API.

## Contexts and namespaces

### Show the merged kubeconfig

```bash
kubectl config view
```

### Show the current context

```bash
kubectl config current-context
```

### List the available contexts

```bash
kubectl config get-contexts
```

### Switch to another context

```bash
kubectl config use-context <context>
```

### Set the default namespace for the current context

```bash
kubectl config set-context --current --namespace=<namespace>
```

## ConfigMaps and Secrets

### Read one key of a ConfigMap

```bash
kubectl get configmap <configmap> -o jsonpath='{.data.<key>}'
```

Keys that contain dots must be escaped in the JSONPath, for example `{.data.ca\.crt}`.

### Decode one key of a Secret

```bash
kubectl get secret <secret> -o jsonpath='{.data.<key>}' | base64 -d
```

Secret values are base64-encoded, not encrypted. This prints sensitive data to your terminal.

### Print all keys of a Secret, decoded

```bash
kubectl get secret <secret> -o go-template='{{range $k,$v := .data}}{{"### "}}{{$k}}{{"\n"}}{{$v|base64decode}}{{"\n\n"}}{{end}}'
```

The template decodes every key for you, so no external tools are needed. This prints sensitive data to your terminal.

## Exploring the cluster

### Show the addresses of the control plane and core services

```bash
kubectl cluster-info
```

### List the resource types the API server offers

```bash
kubectl api-resources
```

### List only namespaced resource types

```bash
kubectl api-resources --namespaced=true
```

### Read the documentation of a resource type

```bash
kubectl explain <resource>
```

Drill into fields with a dotted path, for example `kubectl explain pod.spec.containers`.

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
