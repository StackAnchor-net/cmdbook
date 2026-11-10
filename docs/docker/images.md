# Images

Build, tag, list, pull, push and remove images.

## Registry access

### Log in to a registry

```bash
docker login -u <username>
```

Docker prompts for the password. Pass a registry host as a last argument to log in somewhere other than Docker Hub.

### Search Docker Hub for an image

```bash
docker search <image>
```

### Pull an image from a registry

```bash
docker pull <image>:<tag>
```

### Tag an image for a registry

```bash
docker tag <image>:<tag> <registry>/<image>:<tag>
```

### Push a tagged image to a registry

```bash
docker push <registry>/<image>:<tag>
```

### Push an image to a user repository

```bash
docker push <username>/<image>:<tag>
```

Sign in first with the login command above if you are not already.

## Building and inspecting

### Build an image from the Dockerfile in the current directory

```bash
docker build -t <image>:<tag> .
```

### Build an image without using the cache

```bash
docker build --no-cache -t <image>:<tag> .
```

### List local images

```bash
docker images
```

### Show the full metadata of an image

```bash
docker image inspect <image>:<tag>
```

## Removing

### ⚠ Remove a local image

```bash
docker rmi <image>:<tag>
```

!!! warning
    The image tag is removed from this machine. An image that was never pushed to a registry cannot be recovered, and Docker refuses to remove an image that a container still uses.

### ⚠ Remove all unused images

```bash
docker image prune -a
```

!!! warning
    Every image not used by at least one container is deleted, including tagged ones. Images that were never pushed to a registry cannot be recovered; others must be pulled again.

See also the official [Docker CLI cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).
