# Pods

Inspect, create and manage pods with kubectl. Add `-n <namespace>` to any command to target a namespace other than the current one.

## Listing and filtering

### List pods with node and IP details

```bash
kubectl get pods -o wide
```

### List pods in all namespaces

```bash
kubectl get pods --all-namespaces
```

### List pods matching a label

```bash
kubectl get pods -l <label-key>=<label-value>
```

### List pods together with their labels

```bash
kubectl get pods --show-labels
```

### List only running pods

```bash
kubectl get pods --field-selector=status.phase=Running
```

### List pods sorted by restart count

```bash
kubectl get pods --sort-by='.status.containerStatuses[0].restartCount'
```

The sort uses the first container of each pod.

### List the container images used in all namespaces

```bash
kubectl get pods -A -o=custom-columns='DATA:spec.containers[*].image'
```

### Show a pod as YAML

```bash
kubectl get pod <pod> -o yaml
```

### Describe a pod and its recent events

```bash
kubectl describe pods <pod>
```

## Logs

### Follow the logs of a pod

```bash
kubectl logs -f <pod>
```

### Show the logs of one container in a pod

```bash
kubectl logs <pod> -c <container>
```

### Show the logs of all pods matching a label

```bash
kubectl logs -l <label-key>=<label-value>
```

### Follow the logs of all containers of pods matching a label

```bash
kubectl logs -f -l <label-key>=<label-value> --all-containers
```

## Running commands and copying files

### Open a shell in a pod

```bash
kubectl exec --stdin --tty <pod> -- /bin/sh
```

Add `-c <container>` after the pod name to pick a container in a multi-container pod.

### Run a single command in a pod

```bash
kubectl exec <pod> -- ls /
```

Use `-c <container>` to pick a container, or `deploy/<deployment>` instead of the pod name to target a pod of a deployment.

### Copy a local file into a pod

```bash
kubectl cp <local-path> <namespace>/<pod>:<remote-path>
```

`kubectl cp` needs the `tar` binary inside the container image.

### Copy a file out of a pod

```bash
kubectl cp <namespace>/<pod>:<remote-path> <local-path>
```

Like the upload direction, this requires `tar` in the container image.

## Resource usage

### Show CPU and memory usage of all pods

```bash
kubectl top pods
```

`kubectl top` requires metrics-server to be installed in the cluster.

### Show CPU and memory usage of a pod's containers

```bash
kubectl top pod <pod> --containers
```

### List pods sorted by CPU usage

```bash
kubectl top pod --sort-by=cpu
```

`--sort-by` orders a list of pods, so the command takes no pod name here; use `--sort-by=memory` to rank by memory.

## Create, label and delete

### Generate a pod manifest without creating the pod

```bash
kubectl run <name> --image=<image> --dry-run=client -o yaml > <file.yaml>
```

### Add a label to a pod

```bash
kubectl label pods <pod> <label-key>=<label-value>
```

### ⚠ Delete a pod

```bash
kubectl delete pod <pod>
```

!!! warning
    The pod is terminated gracefully and anything in its container filesystem or `emptyDir` volumes is lost. A pod managed by a Deployment or ReplicaSet is recreated; a bare pod is gone for good.

### ⚠ Delete a pod immediately

```bash
kubectl delete pod <pod> --now
```

!!! warning
    The pod is terminated with a minimal grace period, and anything in its container filesystem or `emptyDir` volumes is lost. A pod managed by a Deployment or ReplicaSet is recreated; a bare pod is gone for good.

### ⚠ Delete pods and services matching a label

```bash
kubectl delete pods,services -l <label-key>=<label-value>
```

!!! warning
    Every pod and service in the current namespace carrying the label is deleted, and data in the pods' container filesystems and `emptyDir` volumes is lost. Pods owned by a Deployment are recreated.

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
