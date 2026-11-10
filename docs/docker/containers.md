# Containers

Run, inspect and stop containers.

### Run a container in the background

```bash
docker run -d <image>
```

### Run a container with a published port

```bash
docker run -p <host-port>:<container-port> <image>
```

### List running containers

```bash
docker ps
```

### List all containers, including stopped ones

```bash
docker ps --all
```

### Follow the logs of a container

```bash
docker logs -f <container>
```

### Open a shell in a running container

```bash
docker exec -it <container> sh
```

### Show the full metadata of a container

```bash
docker inspect <container>
```

### Stop a container

```bash
docker stop <container>
```

### ⚠ Remove a container

```bash
docker rm <container>
```

!!! warning
    The container and its writable filesystem layer are deleted, so files and logs written inside it are lost. Data in named volumes is kept.

See also the official [Docker CLI cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).
