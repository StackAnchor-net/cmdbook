# Debugging

Find out why workloads are failing.

## Events and logs

### List events, oldest first

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

### List only warning events

```bash
kubectl events --types=Warning
```

### Show logs of the previous (crashed) container

```bash
kubectl logs <pod> --previous
```

Useful for pods in `CrashLoopBackOff`: the current container has little to show, the previous one holds the crash output.

## Debug containers

### Attach an ephemeral debug container to a pod

```bash
kubectl debug <pod> -it --image=busybox:1.36
```

### Attach a debug container that targets one container

```bash
kubectl debug -it <pod> --image=busybox:1.36 --target=<container>
```

`--target` shares the process namespace of that container so you can see its processes.

### Start a debug pod on a node

```bash
kubectl debug node/<node> -it --image=busybox:1.36
```

The node's root filesystem is mounted at `/host` inside the debug pod.

## Permissions

### Check whether you may perform an action

```bash
kubectl auth can-i <verb> <resource>
```

For example `kubectl auth can-i create deployments -n <namespace>`.

## Nodes

### Show CPU and memory usage of nodes

```bash
kubectl top node
```

This needs metrics-server.

### Describe a node

```bash
kubectl describe nodes <node>
```

### List nodes with their Ready status

```bash
kubectl get node -o custom-columns='NODE_NAME:.metadata.name,STATUS:.status.conditions[?(@.type=="Ready")].status'
```

### List the taints of all nodes

```bash
kubectl get nodes -o='custom-columns=NodeName:.metadata.name,TaintKey:.spec.taints[*].key,TaintValue:.spec.taints[*].value,TaintEffect:.spec.taints[*].effect'
```

### Mark a node unschedulable

```bash
kubectl cordon <node>
```

Existing pods keep running; only new pods are kept away.

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

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
