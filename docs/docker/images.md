# Images

Build, list, pull, push and remove images.

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

### Pull an image from a registry

```bash
docker pull <image>:<tag>
```

### Push an image to a registry

```bash
docker push <username>/<image>:<tag>
```

Run `docker login -u <username>` first if you are not signed in.

### ⚠ Remove a local image

```bash
docker rmi <image>:<tag>
```

!!! warning
    The image tag is removed from this machine. An image that was never pushed to a registry cannot be recovered, and Docker refuses to remove an image that a container still uses.

See also the official [Docker CLI cheat sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf).
