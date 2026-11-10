# Deployments

Apply manifests, scale, roll out and roll back deployments.

### Apply a manifest

```bash
kubectl apply -f <file.yaml>
```

### ⚠ Delete the resources defined in a manifest

```bash
kubectl delete -f <file.yaml>
```

!!! warning
    Every resource listed in the file is deleted from the cluster, including the data of any PersistentVolumeClaims it defines when the volume's reclaim policy is `Delete`.

### Watch a rollout until it finishes

```bash
kubectl rollout status -w deployment/<deployment>
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
kubectl scale --replicas=<count> deployment/<deployment>
```

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
