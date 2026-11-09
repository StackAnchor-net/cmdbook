# Networking

Services, ingress and port forwarding.

## Services

### List services

```bash
kubectl get svc
```

### List services in all namespaces

```bash
kubectl get svc -A
```

### Show the endpoints behind a service

```bash
kubectl get endpoints <service>
```

An empty endpoint list usually means the service selector matches no ready pods.

### Describe a service

```bash
kubectl describe svc <service>
```

### Expose a deployment as a service

```bash
kubectl expose deployment <deployment> --port=<port> --target-port=<target-port>
```

### List ingresses

```bash
kubectl get ingress -A
```

## Port forwarding

### Forward a local port to a service

```bash
kubectl port-forward svc/<service> <local-port>:<service-port>
```

## Testing from inside the cluster

These pods are removed automatically when you exit (`--rm`).

### Run a throwaway shell pod

```bash
kubectl run busybox-test --rm -it --restart=Never --image=busybox:1.36 -- sh
```

### Curl a service from inside the cluster

```bash
kubectl run curl-test --rm -it --restart=Never --image=curlimages/curl -- curl -s http://<service>.<namespace>.svc.cluster.local:<port>
```

### Check DNS resolution of a service

```bash
kubectl run dns-test --rm -it --restart=Never --image=busybox:1.36 -- nslookup <service>.<namespace>.svc.cluster.local
```

### List network policies

```bash
kubectl get networkpolicy -A
```
