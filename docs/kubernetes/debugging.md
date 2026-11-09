# Debugging

Find out why workloads are failing.

### List recent events, oldest first

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Show logs of the previous (crashed) container

```bash
kubectl logs --previous <pod>
```

Useful for pods in `CrashLoopBackOff`: the current container has little to show, the previous one holds the crash output.

### Attach an ephemeral debug container to a pod

```bash
kubectl debug -it <pod> --image=busybox:1.36 --target=<container>
```

### Show CPU and memory usage of pods

```bash
kubectl top pods
```

`kubectl top` requires metrics-server to be installed in the cluster.

### Check whether you may perform an action

```bash
kubectl auth can-i <verb> <resource>
```

For example `kubectl auth can-i create deployments -n <namespace>`.

### ⚠ Drain a node

```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
```

!!! warning
    Every evictable pod on the node is terminated, and data in their `emptyDir` volumes is lost. DaemonSet pods are left running. Run `kubectl uncordon <node>` afterwards to allow scheduling again.
