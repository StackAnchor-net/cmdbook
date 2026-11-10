# EKS & ECR

Connect kubectl to a cluster and authenticate Docker against the container registry. Once the kubeconfig entry exists, see [Config](../kubernetes/config.md) for switching contexts and namespaces. For building, tagging and pushing images, see [Images](../docker/images.md).

## EKS

### List clusters in a region

```bash
aws eks list-clusters --region <region>
```

### Add a cluster to your kubeconfig

```bash
aws eks update-kubeconfig --name <cluster> --region <region>
```

Creates or updates a context for the cluster in `~/.kube/config`. Add `--profile <profile>` if the cluster lives in another account.

### Check the status of a cluster

```bash
aws eks describe-cluster --name <cluster> --query cluster.status --region <region>
```

Returns `ACTIVE` for a healthy cluster.

## ECR

### Log Docker in to a private registry

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```

The token lasts 12 hours. For example, `<account-id>` could be `123456789012`.

### List images in a repository

```bash
aws ecr describe-images --repository-name <repository> --region <region>
```

See also the official [AWS CLI v2 command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).
