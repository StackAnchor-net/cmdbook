# Compose

Manage multi-container applications with Docker Compose. These commands use the Compose v2 plugin (`docker compose`) and read `compose.yaml` in the current directory.

## Starting and stopping

### Start all services in the background

```bash
docker compose up -d
```

### Rebuild images and start all services

```bash
docker compose up -d --build
```

### Start services from a specific compose file

```bash
docker compose -f <file.yaml> up -d
```

### Stop and remove containers and networks

```bash
docker compose down
```

Named volumes are kept. See the cleanup page for removing them as well.

### Restart a service

```bash
docker compose restart <service>
```

## Inspecting

### List the containers of the project

```bash
docker compose ps
```

### Follow the logs of a service

```bash
docker compose logs -f <service>
```

### Print the resolved compose configuration

```bash
docker compose config
```

This validates the file and shows it with variables interpolated.

## Working with services

### Open a shell in a service container

```bash
docker compose exec <service> sh
```

### Pull the latest images for all services

```bash
docker compose pull
```
