# Containers

Run, inspect and stop containers.

### Run a container in the background with a port, env var and name

```bash
docker run -d --name <name> -p <host-port>:<container-port> -e <VAR>=<value> <image>
```

### List all containers, including stopped ones

```bash
docker ps -a
```

### Follow the last lines of a container's logs

```bash
docker logs -f --tail 100 <container>
```

### Open a shell in a running container

```bash
docker exec -it <container> sh
```

### Copy a file out of a container

```bash
docker cp <container>:<remote-path> <local-path>
```

### Show the IP address of a container

```bash
docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>
```

### Show a one-off snapshot of resource usage

```bash
docker stats --no-stream
```
