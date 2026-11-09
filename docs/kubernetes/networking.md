# Networking

Services, endpoints and in-cluster connectivity tests.

### Show the endpoints behind a service

```bash
kubectl get endpoints <service>
```

An empty endpoint list usually means the service selector matches no ready pods.

## Testing from inside the cluster

These pods are removed automatically when you exit (`--rm`).

### Curl a service from inside the cluster

```bash
kubectl run curl-test --rm -it --restart=Never --image=curlimages/curl -- curl -s http://<service>.<namespace>.svc.cluster.local:<port>
```

### Check DNS resolution of a service

```bash
kubectl run dns-test --rm -it --restart=Never --image=busybox:1.36 -- nslookup <service>.<namespace>.svc.cluster.local
```

### Forward a local port to a service

```bash
kubectl port-forward svc/<service> <local-port>:<service-port>
```
