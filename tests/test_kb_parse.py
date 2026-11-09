"""Tests for bin/kb_parse.py and a syntax check of bin/kb."""
import importlib.util
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARSER = os.path.join(ROOT, "bin", "kb_parse.py")
KB = os.path.join(ROOT, "bin", "kb")
FIXTURES = os.path.join(ROOT, "tests", "fixtures", "kb", "docs")

_spec = importlib.util.spec_from_file_location("kb_parse", PARSER)
kb_parse = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kb_parse)


def by_desc(commands):
    return dict((c.description, c) for c in commands)


class FixtureParseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.commands = kb_parse.load(FIXTURES)
        cls.by_desc = by_desc(cls.commands)

    def test_basic_heading_and_block(self):
        c = self.by_desc["Show disk usage"]
        self.assertEqual(c.command, "df -h")
        self.assertEqual(c.category, "linux")
        self.assertEqual(c.source, "docs/linux/disk.md")

    def test_non_bash_blocks_and_prose_ignored(self):
        self.assertNotIn("Sample output only", self.by_desc)
        self.assertNotIn("not-a-heading", " ".join(self.by_desc))

    def test_heading_without_block_yields_nothing(self):
        self.assertNotIn("Heading without a block", self.by_desc)

    def test_only_first_bash_block(self):
        self.assertEqual(self.by_desc["Two blocks"].command, "first-one")

    def test_multiline_command_preserved(self):
        cmd = self.by_desc["Multi-line command"].command
        self.assertEqual(cmd, "kubectl apply -f - <<EOF\na: 1\nEOF\necho done 2>&1")

    def test_tilde_fence_with_extra_words(self):
        self.assertEqual(self.by_desc["Tilde fence"].command, "ls -la <dir>")

    def test_long_fence_with_backticks_inside(self):
        self.assertEqual(self.by_desc["Long fence"].command, "echo ```")

    def test_heading_inside_fence_not_a_heading(self):
        self.assertNotIn("Not a heading", self.by_desc)
        self.assertNotIn("inside text fence", self.by_desc)
        # the bash-looking fence nested in a text fence is not a block either
        self.assertNotIn("Text fence containing fake things", self.by_desc)
        self.assertNotIn("not-a-block", [c.command for c in self.commands])

    def test_level2_heading_ends_section_and_bash_without_h3_ignored(self):
        self.assertNotIn("echo trapped", [c.command for c in self.commands])

    def test_warning_prefix_preserved(self):
        c = self.by_desc["⚠ Wipe a device"]
        self.assertTrue(c.description.startswith("⚠ "))
        self.assertEqual(c.command, "dd if=/dev/zero of=<device> bs=1M")

    def test_category_display_names(self):
        self.assertEqual(self.by_desc["Show disk usage"].category_name, "Linux")
        self.assertEqual(self.by_desc["Logs of a pod"].category_name, "Kubernetes")
        self.assertEqual(self.by_desc["Custom thing"].category_name, "Custom")
        self.assertEqual(kb_parse.category_display("docker"), "Docker")
        self.assertEqual(kb_parse.category_display("networking"), "Networking")

    def test_docs_root_pages_skipped(self):
        self.assertNotIn("Root page command", self.by_desc)

    def test_line_numbers(self):
        self.assertEqual(self.by_desc["Show disk usage"].line, 9)
        self.assertEqual(self.by_desc["Logs of a pod"].line, 3)
        with open(os.path.join(FIXTURES, "linux", "disk.md"), encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for c in self.commands:
            if c.source.endswith("linux/disk.md"):
                self.assertEqual(lines[c.line - 1], "### " + c.description)

    def test_order_is_sorted_by_file(self):
        sources = [c.source for c in self.commands]
        self.assertEqual(sources, sorted(sources))


class ParseTextTests(unittest.TestCase):
    def test_indented_fence_in_admonition(self):
        text = "### Thing\n\n!!! note\n    ```bash\n    echo hi\n      indented\n    ```\n"
        cmds = kb_parse.parse_text(text, "linux", "docs/linux/x.md")
        self.assertEqual(cmds[0].command, "echo hi\n  indented")

    def test_crlf(self):
        cmds = kb_parse.parse_text("### T\r\n\r\n```bash\r\nls\r\n```\r\n", "linux", "s")
        self.assertEqual(cmds[0].command, "ls")

    def test_unclosed_fence_yields_nothing(self):
        self.assertEqual(kb_parse.parse_text("### T\n\n```bash\nls\n", "linux", "s"), [])

    def test_level4_heading_does_not_end_section(self):
        text = "### T\n\n#### Sub\n\n```bash\nls\n```\n"
        self.assertEqual(kb_parse.parse_text(text, "linux", "s")[0].command, "ls")


class PlaceholderTests(unittest.TestCase):
    def test_extraction_in_order(self):
        cmd = "kubectl logs <pod> -n <namespace> -c <container.name>"
        self.assertEqual(kb_parse.placeholders(cmd), ["pod", "namespace", "container.name"])

    def test_duplicates_listed_once(self):
        self.assertEqual(kb_parse.placeholders("a <x> b <y> c <x>"), ["x", "y"])

    def test_shell_syntax_not_matched(self):
        for cmd in ("ls 2>&1", "cat <<EOF", "sort < in.txt", "diff <(a) <(b)",
                    "echo a >> f", "cmd <<-EOF", "cat <<< word", "x <1abc>"):
            self.assertEqual(kb_parse.placeholders(cmd), [], cmd)

    def test_filename_style_names(self):
        self.assertEqual(kb_parse.placeholders("cp <file.txt> <my-dir_1>"), ["file.txt", "my-dir_1"])

    def test_substitute_all_occurrences(self):
        self.assertEqual(kb_parse.substitute("a <x> <y> <x>", {"x": "1", "y": "2"}), "a 1 2 1")

    def test_substitute_missing_keeps_literal(self):
        self.assertEqual(kb_parse.substitute("a <x> <y>", {"x": "1"}), "a 1 <y>")

    def test_substitute_is_single_pass(self):
        self.assertEqual(kb_parse.substitute("<a> <b>", {"a": "<b>", "b": "z"}), "<b> z")

    def test_substitute_value_with_backslash(self):
        self.assertEqual(kb_parse.substitute("<a>", {"a": "x\\1y"}), "x\\1y")


def run_parser(*args):
    return subprocess.run([sys.executable, PARSER] + list(args), stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, universal_newlines=True, encoding="utf-8")


class CliTests(unittest.TestCase):
    def test_list_format(self):
        r = run_parser("list", FIXTURES)
        self.assertEqual(r.returncode, 0, r.stderr)
        lines = r.stdout.splitlines()
        self.assertEqual(len(lines), len(kb_parse.load(FIXTURES)))
        for i, line in enumerate(lines):
            fields = line.split("\t")
            self.assertEqual(len(fields), 3, line)
            self.assertEqual(fields[0], str(i))
        self.assertIn("Linux › Show disk usage", lines[2])
        self.assertTrue(lines[2].endswith("\tdocs/linux/disk.md:9"))

    def index_of(self, desc):
        for line in run_parser("list", FIXTURES).stdout.splitlines():
            idx, title, _ = line.split("\t")
            if title.endswith(desc):
                return idx
        self.fail(desc)

    def test_get(self):
        r = run_parser("get", FIXTURES, self.index_of("Multi-line command"))
        self.assertEqual(r.stdout, "kubectl apply -f - <<EOF\na: 1\nEOF\necho done 2>&1\n")

    def test_preview(self):
        r = run_parser("preview", FIXTURES, self.index_of("Show disk usage"))
        self.assertEqual(r.stdout, "df -h\n\nsource: docs/linux/disk.md:9\n")

    def test_placeholders(self):
        r = run_parser("placeholders", FIXTURES, self.index_of("Logs of a pod"))
        self.assertEqual(r.stdout.split(), ["pod", "namespace"])

    def test_fill(self):
        idx = self.index_of("Logs of a pod")
        r = run_parser("fill", FIXTURES, idx, "web-1", "")
        self.assertEqual(r.stdout, "kubectl logs -f web-1 -n <namespace> | grep web-1\n")

    def test_bad_index(self):
        self.assertEqual(run_parser("get", FIXTURES, "999").returncode, 1)
        self.assertEqual(run_parser("get", FIXTURES, "abc").returncode, 1)

    def test_real_docs_parse(self):
        r = run_parser("list", os.path.join(ROOT, "docs"))
        self.assertEqual(r.returncode, 0, r.stderr)


class KbScriptTests(unittest.TestCase):
    def test_bash_syntax(self):
        r = subprocess.run(["bash", "-n", KB], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_help_and_unknown_option(self):
        r = subprocess.run(["bash", KB, "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
        self.assertEqual(r.returncode, 0)
        self.assertIn("Usage: kb", r.stdout)
        r = subprocess.run(["bash", KB, "--bogus"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           universal_newlines=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("Usage: kb", r.stderr)


if __name__ == "__main__":
    unittest.main()
