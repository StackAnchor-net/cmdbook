# Cleanup

Reclaim disk space used by Docker. Check what is using space first, then prune.

### Show disk usage by images, containers and volumes

```bash
docker system df
```

### ⚠ Remove all stopped containers

```bash
docker container prune
```

!!! warning
    Every stopped container is removed along with its writable filesystem layer. Logs and files inside those containers are lost.

### ⚠ Remove dangling images

```bash
docker image prune
```

!!! warning
    Untagged images that no container references are deleted. They can only be recovered by rebuilding or pulling.

### ⚠ Remove all unused images

```bash
docker image prune -a
```

!!! warning
    Every image not used by at least one container is deleted, including tagged ones. Locally built images that were never pushed to a registry are lost.

### ⚠ Remove unused volumes

```bash
docker volume prune
```

!!! warning
    Volumes not attached to any container are deleted permanently, along with all data stored in them.

### ⚠ Remove unused networks

```bash
docker network prune
```

!!! warning
    All user-defined networks with no connected containers are removed.

### ⚠ Remove all unused Docker data

```bash
docker system prune
```

!!! warning
    Removes stopped containers, unused networks, dangling images and build cache. Volumes are not touched unless you add `--volumes`.

### ⚠ Stop a Compose project and delete its volumes

```bash
docker compose down -v
```

!!! warning
    Containers, networks and the named volumes declared in the compose file are removed. Data stored in those volumes, such as databases, is lost.
