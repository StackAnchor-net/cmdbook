# Deployments

Scale, roll out and roll back deployments.

## Inspecting

### List deployments

```bash
kubectl get deployments
```

### Describe a deployment

```bash
kubectl describe deployment <deployment>
```

## Rollouts

### Watch a rollout until it finishes

```bash
kubectl rollout status deployment/<deployment>
```

### Show the revision history of a deployment

```bash
kubectl rollout history deployment/<deployment>
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

### Roll back to a specific revision

```bash
kubectl rollout undo deployment/<deployment> --to-revision=<revision>
```

## Changing a deployment

### Scale a deployment

```bash
kubectl scale deployment/<deployment> --replicas=<count>
```

### Change the image of a container

```bash
kubectl set image deployment/<deployment> <container>=<image>:<tag>
```

### Edit a deployment in your editor

```bash
kubectl edit deployment/<deployment>
```
