# Deployments

Scale, roll out and roll back deployments.

### Watch a rollout until it finishes

```bash
kubectl rollout status deployment/<deployment>
```

### Restart all pods of a deployment

```bash
kubectl rollout restart deployment/<deployment>
```

Pods are replaced gradually, following the deployment's rolling update strategy.

### Roll back to the previous revision

```bash
kubectl rollout undo deployment/<deployment>
```

### Scale a deployment

```bash
kubectl scale deployment/<deployment> --replicas=<count>
```
