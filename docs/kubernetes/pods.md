# Pods

Inspect, create and manage pods with kubectl. Add `-n <namespace>` to any command to target a namespace other than the current one.

### List pods with node and IP details

```bash
kubectl get pods -o wide
```

### List pods matching a label selector

```bash
kubectl get pods -l <label-key>=<label-value>
```

### Describe a pod and its recent events

```bash
kubectl describe pod <pod>
```

### Follow the logs of a pod

```bash
kubectl logs -f <pod>
```

### Open a shell in a pod

```bash
kubectl exec -it <pod> -- sh
```

Use `-c <container>` after the pod name to pick a container in a multi-container pod.

### ⚠ Delete a pod

```bash
kubectl delete pod <pod>
```

!!! warning
    The pod and anything in its container filesystem or `emptyDir` volumes is lost. A pod managed by a Deployment or ReplicaSet is recreated; a bare pod is gone for good.
