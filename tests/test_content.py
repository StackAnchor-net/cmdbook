"""Content-convention tests for docs/. Independent of bin/kb_parse.py."""
import ipaddress
import re
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*(.*)$")
HEADING = re.compile(r"^(#{1,6})(?:\s+(.*?))?\s*#*\s*$")
IPV4 = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])")
PRIVATE_NETS = [ipaddress.ip_network(n) for n in ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")]


def rel(path):
    return path.relative_to(ROOT).as_posix()


def md_files():
    return sorted(DOCS.rglob("*.md"))


def parse(path):
    """Return (sections, orphans, unclosed).

    sections: list of dicts {line, desc, raw, blocks: [(line, lang, text)]}
    orphans: bash blocks outside any ### section, as (line, lang, text)
    unclosed: fences still open at end of file, as (line, lang)
    """
    sections, orphans = [], []
    current = None
    fence = None  # (char, length, lang, start_line, lines)
    for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if fence is None:
            m = FENCE.match(line)
            if m:
                marker, info = m.groups()
                lang = info.split()[0] if info.split() else ""
                fence = (marker[0], len(marker), lang, no, [])
                continue
            h = HEADING.match(line)
            if h and len(h.group(1)) <= 3:
                if len(h.group(1)) == 3:
                    current = {"line": no, "desc": h.group(2) or "", "raw": line, "blocks": []}
                    sections.append(current)
                else:
                    current = None
        else:
            ch, length, lang, start, body = fence
            m = FENCE.match(line)
            if m and m.group(1)[0] == ch and len(m.group(1)) >= length and not m.group(2).strip():
                block = (start, lang, "\n".join(body))
                if lang == "bash":
                    (current["blocks"] if current else orphans).append(block)
                fence = None
            else:
                body.append(line)
    unclosed = [(fence[3], fence[2])] if fence else []
    return sections, orphans, unclosed


def bash_blocks(path):
    sections, orphans, _ = parse(path)
    out = list(orphans)
    for s in sections:
        out.extend(s["blocks"])
    return out


def nav_files(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, list):
        for item in node:
            yield from nav_files(item)
    elif isinstance(node, dict):
        for value in node.values():
            yield from nav_files(value)


class ContentTests(unittest.TestCase):
    def test_pages_exist(self):
        self.assertTrue(md_files(), "no markdown files under docs/")

    def test_exactly_one_bash_block_per_heading(self):
        errors = []
        for p in md_files():
            sections, orphans, unclosed = parse(p)
            for line, lang in unclosed:
                errors.append(f"{rel(p)}:{line}: unclosed code fence (```{lang}) never closed before end of file")
            for s in sections:
                n = len(s["blocks"])
                if n != 1:
                    errors.append(f"{rel(p)}:{s['line']}: '### {s['desc']}' has {n} bash blocks, expected 1")
            for line, _, _ in orphans:
                errors.append(f"{rel(p)}:{line}: bash block outside any ### section")
        self.assertFalse(errors, "\n" + "\n".join(errors))

    def test_blocks_and_descriptions_not_empty(self):
        errors = []
        for p in md_files():
            sections, _, _ = parse(p)
            for s in sections:
                if not s["desc"].strip():
                    errors.append(f"{rel(p)}:{s['line']}: empty heading description")
                for line, _, text in s["blocks"]:
                    if not text.strip():
                        errors.append(f"{rel(p)}:{line}: empty bash block under '### {s['desc']}'")
        self.assertFalse(errors, "\n" + "\n".join(errors))

    def test_no_duplicate_commands(self):
        seen, errors = {}, []
        for p in md_files():
            for line, _, text in bash_blocks(p):
                key = " ".join(text.split())
                if not key:
                    continue
                here = f"{rel(p)}:{line}"
                if key in seen:
                    errors.append(f"duplicate command {key!r}: {seen[key]} and {here}")
                else:
                    seen[key] = here
        self.assertFalse(errors, "\n" + "\n".join(errors))

    def test_nav_matches_files(self):
        cfg = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
        listed = [f for f in nav_files(cfg.get("nav", [])) if f.endswith(".md")]
        errors = []
        for f in sorted(set(listed)):
            if not (DOCS / f).is_file():
                errors.append(f"mkdocs.yml: nav references missing file docs/{f}")
        for f in set(listed):
            if listed.count(f) > 1:
                errors.append(f"mkdocs.yml: docs/{f} listed in nav more than once")
        listed_set = set(listed)
        for p in md_files():
            if p.relative_to(DOCS).as_posix() not in listed_set:
                errors.append(f"{rel(p)}:1: page missing from mkdocs.yml nav")
        self.assertFalse(errors, "\n" + "\n".join(errors))

    def test_site_builds_without_warnings(self):
        exe = Path(sys.executable).parent / "zensical"
        if not exe.exists():
            self.fail(f"zensical not found next to {sys.executable}; install requirements.txt in the venv")
        r = subprocess.run([str(exe), "build", "--strict", "--clean"], cwd=ROOT,
                           capture_output=True, text=True)
        out = ANSI.sub("", r.stdout + r.stderr)
        self.assertEqual(r.returncode, 0, f"zensical build failed:\n{out}")
        for bad in ("Warning", "warning:", "issue found"):
            self.assertNotIn(bad, out, f"zensical build output contains {bad!r}:\n{out}")

    def test_no_private_ipv4(self):
        errors = []
        for p in md_files():
            for no, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                for m in IPV4.finditer(line):
                    try:
                        ip = ipaddress.ip_address(m.group(0))
                    except ValueError:
                        continue
                    if any(ip in n for n in PRIVATE_NETS):
                        errors.append(f"{rel(p)}:{no}: private IPv4 address {m.group(0)}")
        self.assertFalse(errors, "\n" + "\n".join(errors))

    def test_warning_marker_followed_by_space(self):
        errors = []
        for p in md_files():
            sections, _, _ = parse(p)
            for s in sections:
                if s["desc"].startswith("⚠") and not s["desc"].startswith("⚠ "):
                    errors.append(f"{rel(p)}:{s['line']}: '⚠' must be followed by a space: {s['raw']!r}")
        self.assertFalse(errors, "\n" + "\n".join(errors))


if __name__ == "__main__":
    unittest.main()
