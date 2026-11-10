# Deployments

Apply manifests, create, scale, roll out and roll back deployments.

## Manifests

### Apply a manifest

```bash
kubectl apply -f <file.yaml>
```

### Apply all manifests in a directory

```bash
kubectl apply -f <dir>
```

### Preview what an apply would change

```bash
kubectl diff -f <file.yaml>
```

### ⚠ Delete the resources defined in a manifest

```bash
kubectl delete -f <file.yaml>
```

!!! warning
    Every resource listed in the file is deleted from the cluster, including the data of any PersistentVolumeClaims it defines when the volume's reclaim policy is `Delete`.

## Creating workloads

### Create a deployment

```bash
kubectl create deployment <name> --image=<image>
```

### Create a job that runs one command

```bash
kubectl create job <name> --image=busybox:1.36 -- echo "<message>"
```

## Rollouts

### Update the image of a deployment

```bash
kubectl set image deployment/<deployment> <container>=<image>:<tag>
```

### Watch a rollout until it finishes

```bash
kubectl rollout status -w deployment/<deployment>
```

### Restart all pods of a deployment

```bash
kubectl rollout restart deployment/<deployment>
```

Pods are replaced gradually, following the deployment's rolling update strategy.

### Show the rollout history

```bash
kubectl rollout history deployment/<deployment>
```

### Roll back to the previous revision

```bash
kubectl rollout undo deployment/<deployment>
```

### Roll back to a specific revision

```bash
kubectl rollout undo deployment/<deployment> --to-revision=<revision>
```

Find revision numbers with the rollout history command.

## Scaling

### Scale a deployment

```bash
kubectl scale --replicas=<count> deployment/<deployment>
```

### Autoscale a deployment

```bash
kubectl autoscale deployment <deployment> --min=<min> --max=<max>
```

This creates a HorizontalPodAutoscaler. Add `--cpu-percent=<percent>` to set the CPU target. It needs metrics-server and CPU requests on the pods.

## Logs and commands

### Show the logs of a deployment

```bash
kubectl logs deploy/<deployment>
```

Logs come from one pod of the deployment.

Commands adapted from the [kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) by The Kubernetes Authors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
