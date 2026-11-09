# Images

Build, tag, inspect and push images.

## Building

### Build an image from the Dockerfile in the current directory

```bash
docker build -t <image>:<tag> .
```

### Build an image from a specific Dockerfile

```bash
docker build -f <dockerfile> -t <image>:<tag> .
```

### Build an image without using the layer cache

```bash
docker build --no-cache -t <image>:<tag> .
```

## Registries

### Log in to a registry

```bash
docker login <registry>
```

### Tag an image for a registry

```bash
docker tag <image>:<tag> <registry>/<image>:<tag>
```

### Push an image to a registry

```bash
docker push <registry>/<image>:<tag>
```

### Pull an image from a registry

```bash
docker pull <image>:<tag>
```

## Inspecting

### List local images

```bash
docker images
```

### Show the layers of an image

```bash
docker history <image>:<tag>
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
    The local copy of the image is deleted. It can be pulled again only if it exists in a registry; locally built images that were never pushed are lost. Docker refuses if a container still uses the image.
