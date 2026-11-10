#!/usr/bin/env python3
"""Write machine-readable files into the built site (run after `zensical build`).

    build_agent_files.py [--config mkdocs.yml] [--docs docs] [--site site]

Writes llms.txt, llms-full.txt and commands.json, and copies every page's raw
Markdown next to its HTML (e.g. site/kubernetes/pods.md).
"""
import argparse
import json
import os
import re
import shutil
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kb_parse  # noqa: E402
from markdown.extensions.toc import slugify, unique  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTRUCTIVE = "⚠ "


def nav_pages(items, section=None):
    """Flatten nav into (section, title, md_path) tuples in nav order."""
    for item in items:
        for title, value in item.items():
            if isinstance(value, list):
                yield from nav_pages(value, title)
            else:
                yield section, title, value


def page_url(base, md_path):
    if md_path == "index.md":
        return base
    if md_path.endswith("/index.md"):
        return base + md_path[: -len("index.md")]
    return base + md_path[:-3] + "/"


def heading_ids(text):
    """Map (line, ) of each heading to the id Python-Markdown's toc gives it."""
    ids, taken = {}, set()
    fence = None
    for no, line in enumerate(text.splitlines(), 1):
        m = kb_parse.FENCE_RE.match(line)
        if fence is not None:
            if m and m.group(2)[0] == fence[0] and len(m.group(2)) >= fence[1] and not m.group(3).strip():
                fence = None
            continue
        if m and not (m.group(2)[0] == "`" and "`" in m.group(3)):
            fence = (m.group(2)[0], len(m.group(2)))
            continue
        h = kb_parse.HEADING_RE.match(line)
        if h and h.group(2):
            title = re.sub(r"[`*_]", "", h.group(2)).rstrip("# ").strip()
            ids[no] = unique(slugify(title, "-"), taken)
    return ids


def build(config_path, docs_dir, site_dir):
    with open(config_path, encoding="utf-8") as fh:
        config = yaml.safe_load(fh)
    base = config["site_url"].rstrip("/") + "/"
    pages = list(nav_pages(config["nav"]))
    titles = {path: title for _, title, path in pages}

    commands = []
    for c in kb_parse.load(docs_dir):
        md_path = c.source.split("/", 1)[1]
        with open(os.path.join(docs_dir, md_path), encoding="utf-8") as fh:
            anchor = heading_ids(fh.read()).get(c.line)
        url = page_url(base, md_path) + ("#" + anchor if anchor else "")
        destructive = c.description.startswith(DESTRUCTIVE)
        commands.append({
            "category": c.category,
            "page": titles.get(md_path, md_path),
            "path": md_path,
            "url": url,
            "description": c.description[len(DESTRUCTIVE):] if destructive else c.description,
            "destructive": destructive,
            "command": c.command,
            "placeholders": kb_parse.placeholders(c.command),
        })

    lines = ["# %s" % config["site_name"], "", "> %s" % config["site_description"], "",
             "Every page is also available as raw Markdown. "
             "All commands as JSON: %scommands.json. Full text: %sllms-full.txt." % (base, base)]
    sections = []
    for section, title, path in pages:
        if not sections or sections[-1][0] != (section or "Overview"):
            sections.append((section or "Overview", []))
        sections[-1][1].append((title, path))
    for name, entries in sections:
        lines += ["", "## %s" % name, ""]
        lines += ["- [%s](%s%s)" % (t, base, p) for t, p in entries]
    lines += ["", "## Optional", "",
              "- [All commands (JSON)](%scommands.json)" % base,
              "- [Full documentation in one file](%sllms-full.txt)" % base, ""]

    full = []
    for _, title, path in pages:
        with open(os.path.join(docs_dir, path), encoding="utf-8") as fh:
            full.append("<!-- source: %s%s -->\n\n%s" % (base, path, fh.read().strip()))
        dest = os.path.join(site_dir, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(docs_dir, path), dest)

    def write(name, text):
        with open(os.path.join(site_dir, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)

    write("llms.txt", "\n".join(lines))
    write("llms-full.txt", "# %s\n\n> %s\n\n" % (config["site_name"], config["site_description"])
          + "\n\n---\n\n".join(full) + "\n")
    write("commands.json", json.dumps(commands, indent=2, ensure_ascii=False) + "\n")
    return commands


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--config", default=os.path.join(ROOT, "mkdocs.yml"))
    p.add_argument("--docs", default=os.path.join(ROOT, "docs"))
    p.add_argument("--site", default=os.path.join(ROOT, "site"))
    a = p.parse_args(argv[1:])
    if not os.path.isdir(a.site):
        sys.stderr.write("build_agent_files: %s not found; run `zensical build` first\n" % a.site)
        return 1
    commands = build(a.config, a.docs, a.site)
    print("wrote llms.txt, llms-full.txt, commands.json (%d commands) to %s" % (len(commands), a.site))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
