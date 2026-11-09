# Pods

Inspect, create and manage pods with kubectl. Add `-n <namespace>` to any command to target a namespace other than the current one.

## Listing

### List pods in a namespace

```bash
kubectl get pods -n <namespace>
```

### List pods in all namespaces

```bash
kubectl get pods -A
```

### List pods with node and IP details

```bash
kubectl get pods -o wide
```

### List pods matching a label selector

```bash
kubectl get pods -l <label-key>=<label-value>
```

### Watch pods change state

```bash
kubectl get pods -w
```

### List only pods in a given phase

```bash
kubectl get pods --field-selector status.phase=Running
```

## Inspecting

### Describe a pod and its recent events

```bash
kubectl describe pod <pod>
```

### Follow the logs of a pod

```bash
kubectl logs -f <pod>
```

### Show the last lines of a pod's logs

```bash
kubectl logs --tail=100 <pod>
```

### Follow the logs of one container in a pod

```bash
kubectl logs -f <pod> -c <container>
```

## Running things

### Open a shell in a pod

```bash
kubectl exec -it <pod> -- sh
```

Use `-c <container>` after the pod name to pick a container in a multi-container pod.

### Run a single command in a pod

```bash
kubectl exec <pod> -- ls /etc
```

### Forward a local port to a pod

```bash
kubectl port-forward <pod> <local-port>:<container-port>
```

### Copy a file out of a pod

```bash
kubectl cp <namespace>/<pod>:<remote-path> <local-path>
```

### Start a pod from an image

```bash
kubectl run <pod> --image=<image>
```

## Deleting

### ⚠ Delete a pod

```bash
kubectl delete pod <pod>
```

!!! warning
    The pod and anything in its container filesystem or `emptyDir` volumes is lost. A pod managed by a Deployment or ReplicaSet is recreated; a bare pod is gone for good.

### ⚠ Force-delete a stuck pod

```bash
kubectl delete pod <pod> --grace-period=0 --force
```

!!! warning
    Skips graceful shutdown: the API object is removed immediately without waiting for the kubelet to confirm the containers stopped, so processes may keep running and unflushed data is lost.
