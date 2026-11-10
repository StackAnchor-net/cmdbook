# Config

Contexts, namespaces, ConfigMaps and Secrets.

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

### Read one key of a ConfigMap

```bash
kubectl get configmap <configmap> -o jsonpath='{.data.<key>}'
```

Keys that contain dots must be escaped in the JSONPath, for example `{.data.ca\.crt}`.

### Print all keys of a Secret, decoded

```bash
kubectl get secret <secret> -o go-template='{{range $k,$v := .data}}{{"### "}}{{$k}}{{"\n"}}{{$v|base64decode}}{{"\n\n"}}{{end}}'
```

Secret values are base64-encoded, not encrypted. The template decodes them for you, so no external tools are needed. This prints sensitive data to your terminal.

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
