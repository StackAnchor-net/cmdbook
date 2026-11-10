# Compose

Manage multi-container applications with Docker Compose. These commands use the Compose v2 plugin (`docker compose`) and read `compose.yaml` in the current directory.

### Start all services in the background

```bash
docker compose up -d
```

### Stop and remove containers and networks

```bash
docker compose down
```

Named volumes are kept. See the cleanup page for removing them as well.

### List the containers of the project

```bash
docker compose ps
```

### Follow the logs of a service

```bash
docker compose logs -f <service>
```

See also the official [Docker CLI cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).
