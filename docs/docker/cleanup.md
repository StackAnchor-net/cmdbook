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
    Every dangling image (untagged and unreferenced) is deleted. Add `-a` to remove all images not used by a container, including tagged ones.

### ⚠ Remove unused volumes

```bash
docker volume prune
```

!!! warning
    Since Docker Engine 23.0 this removes only unused anonymous volumes, permanently, along with their data. Unused named volumes are removed only if you add `-a`/`--all`.

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

See also the official [Docker CLI cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).
