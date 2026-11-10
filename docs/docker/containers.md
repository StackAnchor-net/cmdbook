# Containers

Run, list, inspect, stop and remove containers.

## Running

### Run a container in the background

```bash
docker run -d <image>
```

### Run a named container

```bash
docker run --name <name> <image>
```

### Run a container with a published port

```bash
docker run -p <host-port>:<container-port> <image>
```

### Run a container in the background with a port, env var and name

```bash
docker run -d --name <name> -p <host-port>:<container-port> -e <VAR>=<value> <image>
```

### Start a stopped container

```bash
docker start <container>
```

### Stop a container

```bash
docker stop <container>
```

## Inspecting

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

### Follow the last lines of a container's logs

```bash
docker logs -f --tail 100 <container>
```

### Show the full metadata of a container

```bash
docker inspect <container>
```

### Show the IP address of a container

```bash
docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>
```

### Show live resource usage of containers

```bash
docker container stats
```

### Show a one-off snapshot of resource usage

```bash
docker stats --no-stream
```

### Show system-wide Docker information

```bash
docker info
```

## Working inside a container

### Open a shell in a running container

```bash
docker exec -it <container> sh
```

### Copy a file out of a container

```bash
docker cp <container>:<remote-path> <local-path>
```

## Removing

### ⚠ Remove a container

```bash
docker rm <container>
```

!!! warning
    The container and its writable filesystem layer are deleted, so files and logs written inside it are lost. Data in named volumes is kept.

See also the official [Docker CLI cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).
