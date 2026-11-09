# Containers

Run, inspect and stop containers.

## Running

### Run a container in the background with a port, env var and name

```bash
docker run -d --name <name> -p <host-port>:<container-port> -e <VAR>=<value> <image>
```

### Run a throwaway interactive container

```bash
docker run --rm -it <image> sh
```

`--rm` removes the container when it exits.

## Listing and logs

### List running containers

```bash
docker ps
```

### List all containers, including stopped ones

```bash
docker ps -a
```

### Follow the last lines of a container's logs

```bash
docker logs -f --tail 100 <container>
```

### Show the published ports of a container

```bash
docker port <container>
```

## Inside a container

### Open a shell in a running container

```bash
docker exec -it <container> sh
```

### Copy a file out of a container

```bash
docker cp <container>:<remote-path> <local-path>
```

### Copy a file into a container

```bash
docker cp <local-file> <container>:<remote-path>
```

## Inspecting

### Show the status of a container

```bash
docker inspect --format '{{.State.Status}}' <container>
```

### Show the IP address of a container

```bash
docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>
```

### Show a one-off snapshot of resource usage

```bash
docker stats --no-stream
```

## Lifecycle

### Stop a container

```bash
docker stop <container>
```

### Start a stopped container

```bash
docker start <container>
```

### Restart a container

```bash
docker restart <container>
```

### ⚠ Force-remove a container

```bash
docker rm -f <container>
```

!!! warning
    The container is killed if running and removed, and anything written to its filesystem outside of volumes is lost.
