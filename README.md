# cmdbook

A DevOps command knowledge base for Kubernetes, Docker, Linux, networking and Git.

The same Markdown files feed two front ends:

- **Website** at <https://stackanchor-net.github.io/cmdbook/>, built with
  [Zensical](https://zensical.org/) and deployed to GitHub Pages.
- **`kb`**, a local terminal picker built on [fzf](https://github.com/junegunn/fzf).
  It lets you search every command, preview it and copy it to the clipboard.

## Content convention

Every page under `docs/` follows one strict rule, and both front ends depend on it.

Each command is a level-3 heading with a short description, followed by exactly one
fenced `bash` block that holds the command:

````markdown
### Follow the logs of a pod

```bash
kubectl logs -f <pod>
```
````

- `<placeholder>` marks a value you fill in. `kb` prompts for each one before copying.
- Destructive commands start their description with `⚠ `, and the page says what is lost.
- Anything else on a page (prose, tables, notes) is shown on the website and ignored by `kb`.
- Examples use documentation-safe names and addresses only: `example.com`,
  `192.0.2.0/24` and `203.0.113.0/24`.

## Build the site

Requires Python 3.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/zensical serve           # live preview at http://localhost:8000
.venv/bin/zensical build --strict  # static output in site/
```

## Run kb

Requires `bash`, `python3` and `fzf`. Works on macOS and Linux.

```bash
bin/kb            # pick a command; Enter copies it to the clipboard
bin/kb --print    # print the chosen command to stdout instead
```

On macOS `kb` copies with `pbcopy`. Elsewhere it uses the OSC 52 terminal escape
sequence, which also works over SSH in terminals that support it, such as iTerm2.

To call `kb` from anywhere, symlink it onto your `PATH`:

```bash
ln -s "$PWD/bin/kb" ~/.local/bin/kb
```

## Tests

```bash
.venv/bin/python -m unittest discover -s tests -v
```

The tests fail if a command heading does not have exactly one `bash` block, if a command
is duplicated, if a page is missing from the navigation, or if the site build reports
warnings. They also cover the `kb` parser.
