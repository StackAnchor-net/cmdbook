# Networking

Reach services and pods from your machine, and test connectivity from inside the cluster.

### Forward a local port to a service

```bash
kubectl port-forward svc/<service> <local-port>:<service-port>
```

### Forward a local port to a pod

```bash
kubectl port-forward <pod> <local-port>:<container-port>
```

### Start a throwaway shell pod inside the cluster

```bash
kubectl run -i --tty <name> --image=busybox:1.28 -- sh
```

From this shell you can test DNS and connectivity, for example `nslookup <service>`. The pod keeps existing after you exit; remove it with `kubectl delete pod <name>`.

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
