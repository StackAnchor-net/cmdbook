#!/usr/bin/env python3
"""Parse the cmdbook Markdown under docs/ into a list of commands.

Used as a module by the tests and as a script by bin/kb:

    kb_parse.py list <docs_dir>
    kb_parse.py get <docs_dir> <index>
    kb_parse.py preview <docs_dir> <index>
    kb_parse.py placeholders <docs_dir> <index>
    kb_parse.py fill <docs_dir> <index> [value ...]
"""
import os
import re
import sys

PLACEHOLDER_RE = re.compile(r"<([A-Za-z][A-Za-z0-9_.-]*)>")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*$")
FENCE_RE = re.compile(r"^([ \t]*)(`{3,}|~{3,})(.*)$")

CATEGORY_NAMES = {
    "kubernetes": "Kubernetes",
    "docker": "Docker",
    "linux": "Linux",
    "networking": "Networking",
    "git": "Git",
    "helm": "Helm",
    "terraform": "Terraform",
    "aws": "AWS",
    "ssh": "SSH",
    "tls": "TLS",
}


class Command(object):
    def __init__(self, category, category_name, description, command, source, line):
        self.category = category
        self.category_name = category_name
        self.description = description
        self.command = command
        self.source = source
        self.line = line

    def __repr__(self):
        return "Command(%r, %r, %s:%d)" % (self.category, self.description, self.source, self.line)


def category_display(category):
    return CATEGORY_NAMES.get(category, category.capitalize())


def placeholders(command):
    """Unique placeholder names in order of first appearance."""
    seen = []
    for name in PLACEHOLDER_RE.findall(command):
        if name not in seen:
            seen.append(name)
    return seen


def substitute(command, values):
    """Replace every <name> found in `values` (dict); others stay literal.

    Single pass, so a value that itself looks like <x> is never expanded again.
    """
    def repl(match):
        value = values.get(match.group(1))
        return match.group(0) if value is None else value
    return PLACEHOLDER_RE.sub(repl, command)


def parse_text(text, category, source):
    """Return the commands found in one Markdown page."""
    commands = []
    cat_name = category_display(category)
    current = None  # [description, line, command-or-None]
    fence = None    # (char, length, indent, is_bash, lines)

    def finish():
        if current is not None and current[2] is not None:
            commands.append(Command(category, cat_name, current[0], current[2], source, current[1]))

    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip("\r")
        if fence is not None:
            char, length, indent, is_bash, body = fence
            m = FENCE_RE.match(line)
            if m and m.group(2)[0] == char and len(m.group(2)) >= length and not m.group(3).strip():
                if is_bash and current is not None and current[2] is None:
                    current[2] = "\n".join(body).rstrip("\n")
                fence = None
            else:
                body.append(line[indent:] if line[:indent].strip() == "" else line.lstrip())
            continue
        m = FENCE_RE.match(line)
        if m and not (m.group(2)[0] == "`" and "`" in m.group(3)):
            info = m.group(3).strip().split()
            is_bash = bool(info) and info[0] == "bash"
            fence = (m.group(2)[0], len(m.group(2)), len(m.group(1)), is_bash, [])
            continue
        h = HEADING_RE.match(line)
        if h and len(h.group(1)) <= 3:
            finish()
            current = None
            if len(h.group(1)) == 3:
                desc = (h.group(2) or "").strip()
                if desc:
                    current = [desc, lineno, None]
    finish()
    return commands


def load(docs_dir):
    """All commands under docs_dir, in sorted file order."""
    docs_dir = os.path.abspath(docs_dir)
    root = os.path.dirname(docs_dir)
    result = []
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        dirnames.sort()
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            rel_docs = os.path.relpath(path, docs_dir)
            parts = rel_docs.split(os.sep)
            if len(parts) < 2:
                continue  # pages directly in docs/ have no category
            source = os.path.relpath(path, root).replace(os.sep, "/")
            with open(path, encoding="utf-8") as fh:
                result.extend(parse_text(fh.read(), parts[0], source))
    # os.walk visits a directory's files before its subdirectories; sort for a stable order
    result.sort(key=lambda c: (c.source.split("/"), c.line))
    return result


def _get(docs_dir, index):
    commands = load(docs_dir)
    try:
        i = int(index)
        if i < 0:
            raise IndexError
        return commands[i]
    except (ValueError, IndexError):
        sys.stderr.write("kb_parse: no command with index %s\n" % index)
        sys.exit(1)


def main(argv):
    if len(argv) < 3 or argv[1] not in ("list", "get", "preview", "placeholders", "fill"):
        sys.stderr.write(__doc__)
        return 2
    action, docs_dir = argv[1], argv[2]
    out = sys.stdout
    if action == "list":
        for i, c in enumerate(load(docs_dir)):
            title = "%s › %s" % (c.category_name, c.description)
            title = " ".join(title.split())
            # Show the command too, so fzf can match on it (first line only).
            lines = c.command.splitlines() or [""]
            cmd = " ".join(lines[0].split()) + (" ..." if len(lines) > 1 else "")
            out.write("%d\t%s  \u2502 %s\t%s:%d\n" % (i, title, cmd, c.source, c.line))
        return 0
    if len(argv) < 4:
        sys.stderr.write(__doc__)
        return 2
    c = _get(docs_dir, argv[3])
    if action == "get":
        out.write(c.command + "\n")
    elif action == "preview":
        out.write("%s\n\nsource: %s:%d\n" % (c.command, c.source, c.line))
    elif action == "placeholders":
        for name in placeholders(c.command):
            out.write(name + "\n")
    else:  # fill: positional values map onto placeholders in order; "" keeps the literal
        names = placeholders(c.command)
        values = {}
        for name, value in zip(names, argv[4:]):
            if value != "":
                values[name] = value
        out.write(substitute(c.command, values) + "\n")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
