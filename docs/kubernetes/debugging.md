# Debugging

Find out why workloads are failing.

## Events and logs

### List recent events, oldest first

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

### List only warning events in all namespaces

```bash
kubectl get events -A --field-selector type=Warning
```

### Show logs of the previous (crashed) container

```bash
kubectl logs --previous <pod>
```

Useful for pods in `CrashLoopBackOff`: the current container has little to show, the previous one holds the crash output.

### Dump the full YAML of a pod

```bash
kubectl get pod <pod> -o yaml
```

### List pods that are not running

```bash
kubectl get pods -A --field-selector status.phase!=Running
```

## Interactive debugging

### Attach an ephemeral debug container to a pod

```bash
kubectl debug -it <pod> --image=busybox:1.36 --target=<container>
```

### Start a debug pod on a node

```bash
kubectl debug node/<node> -it --image=busybox:1.36
```

The node's filesystem is mounted at `/host` inside the debug pod.

## Resource usage and permissions

### Show CPU and memory usage of pods

```bash
kubectl top pods
```

`kubectl top` requires metrics-server to be installed in the cluster.

### Show CPU and memory usage of nodes

```bash
kubectl top nodes
```

### Check whether you may perform an action

```bash
kubectl auth can-i <verb> <resource>
```

For example `kubectl auth can-i create deployments -n <namespace>`.

### Describe a node

```bash
kubectl describe node <node>
```

## Node maintenance

### Mark a node unschedulable

```bash
kubectl cordon <node>
```

### Mark a node schedulable again

```bash
kubectl uncordon <node>
```

### ⚠ Drain a node

```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
```

!!! warning
    Every evictable pod on the node is terminated, and data in their `emptyDir` volumes is lost. DaemonSet pods are left running. Run `kubectl uncordon <node>` afterwards to allow scheduling again.
