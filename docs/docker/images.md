# Images

Build, tag, inspect and push images.

### Build an image from the Dockerfile in the current directory

```bash
docker build -t <image>:<tag> .
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

### List local images

```bash
docker images
```

### Show the full metadata of an image

```bash
docker image inspect <image>:<tag>
```
