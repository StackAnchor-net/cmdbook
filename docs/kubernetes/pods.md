# Pods

Inspect, create and manage pods with kubectl. Add `-n <namespace>` to any command to target a namespace other than the current one.

### List pods with node and IP details

```bash
kubectl get pods -o wide
```

### Describe a pod and its recent events

```bash
kubectl describe pods <pod>
```

### Follow the logs of a pod

```bash
kubectl logs -f <pod>
```

### Open a shell in a pod

```bash
kubectl exec --stdin --tty <pod> -- /bin/sh
```

Add `-c <container>` after the pod name to pick a container in a multi-container pod.

### Show CPU and memory usage of a pod's containers

```bash
kubectl top pod <pod> --containers
```

`kubectl top` requires metrics-server to be installed in the cluster.

### ⚠ Delete a pod immediately

```bash
kubectl delete pod <pod> --now
```

!!! warning
    The pod is terminated with a minimal grace period, and anything in its container filesystem or `emptyDir` volumes is lost. A pod managed by a Deployment or ReplicaSet is recreated; a bare pod is gone for good.

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
