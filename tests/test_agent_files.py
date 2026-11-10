"""Build the site into a temp dir, run bin/build_agent_files.py and check its output."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "bin"))
import build_agent_files  # noqa: E402
import kb_parse  # noqa: E402

ZENSICAL = ROOT / ".venv" / "bin" / "zensical"


def nav_paths(items):
    for item in items:
        for value in item.values():
            if isinstance(value, list):
                yield from nav_paths(value)
            else:
                yield value


@unittest.skipUnless(ZENSICAL.exists(), "needs .venv with zensical installed")
class AgentFilesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.site = Path(cls.tmp.name) / "site"
        config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
        # Zensical wants relative paths, so build from a copy of docs/ inside the temp dir.
        shutil.copytree(ROOT / "docs", Path(cls.tmp.name) / "docs")
        cfg = Path(cls.tmp.name) / "mkdocs.yml"
        cfg.write_text(yaml.safe_dump(config, allow_unicode=True), encoding="utf-8")
        cls.build = subprocess.run(
            [str(ZENSICAL), "build", "--strict", "--clean", "-f", str(cfg)],
            capture_output=True, text=True, cwd=cls.tmp.name)
        if cls.build.returncode == 0:
            build_agent_files.build(str(ROOT / "mkdocs.yml"), str(ROOT / "docs"), str(cls.site))
        cls.config = config

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_strict_build_has_no_warnings(self):
        out = self.build.stdout + self.build.stderr
        self.assertEqual(self.build.returncode, 0, out)
        self.assertNotRegex(out.lower(), r"warn")
        self.assertIn("No issues found", out)

    def test_viewport_and_extra_css(self):
        html = (self.site / "index.html").read_text(encoding="utf-8")
        self.assertIn('name="viewport"', html)
        self.assertIn("stylesheets/extra.css", html)
        self.assertTrue((self.site / "stylesheets" / "extra.css").exists())

    def test_commands_json(self):
        data = json.loads((self.site / "commands.json").read_text(encoding="utf-8"))
        expected = len(kb_parse.load(ROOT / "docs"))
        self.assertEqual(len(data), expected)
        fields = {"category", "page", "path", "url", "description", "destructive", "command", "placeholders"}
        for entry in data:
            self.assertEqual(set(entry), fields)
            self.assertIsInstance(entry["destructive"], bool)
            self.assertIsInstance(entry["placeholders"], list)
            self.assertFalse(entry["description"].startswith("⚠"))
            self.assertTrue(entry["url"].startswith(self.config["site_url"]))

    def test_anchors_exist_in_built_html(self):
        data = json.loads((self.site / "commands.json").read_text(encoding="utf-8"))
        base = self.config["site_url"]
        for entry in data:
            self.assertIn("#", entry["url"], entry["description"])
            page, anchor = entry["url"][len(base):].split("#")
            html = (self.site / page / "index.html").read_text(encoding="utf-8")
            self.assertIn('id="%s"' % anchor, html, entry["url"])

    def test_llms_txt_lists_every_nav_page(self):
        llms = (self.site / "llms.txt").read_text(encoding="utf-8")
        self.assertTrue(llms.startswith("# "))
        self.assertRegex(llms, r"(?m)^> ")
        base = self.config["site_url"]
        for path in nav_paths(self.config["nav"]):
            self.assertIn("](%s%s)" % (base, path), llms)
            self.assertTrue((self.site / path).exists(), path)
            self.assertEqual((self.site / path).read_text(encoding="utf-8"),
                             (ROOT / "docs" / path).read_text(encoding="utf-8"))

    def test_llms_full_contains_every_page(self):
        full = (self.site / "llms-full.txt").read_text(encoding="utf-8")
        for path in nav_paths(self.config["nav"]):
            self.assertIn("<!-- source: %s%s -->" % (self.config["site_url"], path), full)

    def test_robots_txt(self):
        robots = (self.site / "robots.txt").read_text(encoding="utf-8")
        self.assertRegex(robots, r"(?m)^Allow: /$")
        for url in re.findall(r"(?m)^Sitemap: (\S+)", robots):
            self.assertTrue((self.site / url[len(self.config["site_url"]):]).exists(), url)


if __name__ == "__main__":
    unittest.main()
