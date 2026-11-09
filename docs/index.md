# cmdbook

cmdbook is a DevOps command knowledge base for Kubernetes, Docker, Linux and networking.
The same Markdown feeds this website and a local terminal picker, `kb`.

## Start here

- [Kubernetes](kubernetes/pods.md)
- [Docker](docker/containers.md)
- [Linux](linux/processes.md)
- [Networking](networking/dns.md)

## Content convention

Each command is a level-3 heading with a description, followed by exactly one `bash` block
holding the command. Everything else on a page is for reading only.

- `<placeholder>` marks a value you fill in, for example `<pod>` or `<namespace>`.
- Commands whose description starts with `⚠ ` are destructive; the page says what is lost.
- Examples use documentation-safe names and addresses such as `example.com` and `192.0.2.10`.

## Using kb

```text
bin/kb            # pick a command; Enter copies it to the clipboard
bin/kb --print    # print the chosen command to stdout instead
```

`kb` asks for a value for each placeholder before copying the command.
