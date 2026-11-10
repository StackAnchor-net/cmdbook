# Networking

Reach services and pods from your machine, and test connectivity from inside the cluster.

## Services

### List services

```bash
kubectl get services
```

### Show the EndpointSlices behind a service

```bash
kubectl get endpointslices -l kubernetes.io/service-name=<service>
```

An empty result usually means the service selector matches no ready pods. EndpointSlices replace the Endpoints API, which is deprecated since Kubernetes 1.33.

### Edit a service in your editor

```bash
kubectl edit svc/<service>
```

## Port forwarding

### Forward a local port to a service

```bash
kubectl port-forward svc/<service> <local-port>:<service-port>
```

### Forward a local port to a pod

```bash
kubectl port-forward <pod> <local-port>:<container-port>
```

### Forward a local port to a pod of a deployment

```bash
kubectl port-forward deploy/<deployment> <local-port>:<container-port>
```

## Testing from inside the cluster

The `--rm` flag deletes these pods when you exit.

### Start a throwaway shell pod inside the cluster

```bash
kubectl run -i --tty --rm <name> --image=busybox:1.36 --restart=Never -- sh
```

From this shell you can test DNS and connectivity, for example `nslookup <service>`.

### Curl a service from inside the cluster

```bash
kubectl run curl-test --rm -it --restart=Never --image=curlimages/curl -- curl -s http://<service>.<namespace>.svc.cluster.local:<port>
```

### Check DNS resolution of a service

```bash
kubectl run dns-test --rm -it --restart=Never --image=busybox:1.36 -- nslookup <service>.<namespace>.svc.cluster.local
```

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
