"""Structure tests shared by every uniqaiapp repo: one SKILL.md, thin adapters, no forbidden strings."""
import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "video-director"
FORBIDDEN = ["aeoria", "richpeach", "/Users/", "/Volumes/", "node_modules", "sk-ant-", "sk_live", "api_key=",
             "API_KEY=<real", "TODO: fill", "lorem ipsum"]
TEXT_EXT = {".md", ".py", ".mjs", ".js", ".json", ".yml", ".yaml", ".svg", ".txt", ".mdc", ".cff", ".toml", ""}
SKIP_DIRS = {".git", "__pycache__"}


def read(rel):
    with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "SKILL.md has no YAML frontmatter"
    data = {}
    for line in m.group(1).splitlines():
        if line.startswith("  ") or not line.strip():
            continue
        k, _, v = line.partition(":")
        data[k.strip()] = v.strip()
    return data


def tracked_text_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            if ext in TEXT_EXT and fn != ".DS_Store":
                yield os.path.relpath(os.path.join(dirpath, fn), ROOT)


class TestSkill(unittest.TestCase):
    def setUp(self):
        self.skill = read("SKILL.md")
        self.fm = frontmatter(self.skill)

    def test_name_matches_repo(self):
        self.assertEqual(self.fm["name"], REPO)
        self.assertEqual(os.path.basename(ROOT), REPO)
        self.assertRegex(self.fm["name"], r"^[a-z0-9-]{1,64}$")

    def test_description(self):
        d = self.fm["description"]
        self.assertTrue(1 <= len(d) <= 1024, len(d))
        self.assertNotIn("\n", d)
        for word in ("Kling", "Veo", "storyboard"):
            self.assertIn(word, d)

    def test_body_length(self):
        self.assertLess(len(self.skill.splitlines()), 500)

    def test_no_host_specific_keys(self):
        self.assertNotIn("allowed-tools", self.skill.split("---")[1])


class TestAdapters(unittest.TestCase):
    def test_plugin_json(self):
        p = json.loads(read(".claude-plugin/plugin.json"))
        fm = frontmatter(read("SKILL.md"))
        self.assertEqual(p["name"], fm["name"])
        version = re.search(r"^\s+version:\s*(\S+)", read("SKILL.md"), re.M).group(1)
        self.assertEqual(p["version"], version)
        self.assertEqual(p["author"]["name"], "UniqAI")
        self.assertEqual(p["skills"], ["./"])

    def test_versions_match(self):
        version = re.search(r"^\s+version:\s*(\S+)", read("SKILL.md"), re.M).group(1)
        top = re.search(r"^## \[(\d+\.\d+\.\d+)\]", read("CHANGELOG.md"), re.M).group(1)
        self.assertEqual(top, version)
        from scripts import storyboard
        self.assertEqual(storyboard.VERSION, version)

    def test_cursor_rule(self):
        text = read(".cursor/rules/%s.mdc" % REPO)
        self.assertIn("@SKILL.md", text)
        self.assertTrue(text.startswith("---\n"))

    def test_agents_and_codex_point_to_skill(self):
        self.assertIn("SKILL.md", read("AGENTS.md"))
        self.assertIn("SKILL.md", read("codex/INSTRUCTIONS.md"))

    def test_required_files(self):
        for rel in ["README.md", "LICENSE", "CONTRIBUTING.md", "CHANGELOG.md", ".gitignore", ".gitattributes",
                    ".editorconfig", ".github/workflows/ci.yml", ".github/ISSUE_TEMPLATE/bug_report.md",
                    ".github/ISSUE_TEMPLATE/feature_request.md", ".github/ISSUE_TEMPLATE/config.yml",
                    ".github/PULL_REQUEST_TEMPLATE.md", ".github/repo.json", "assets/banner.svg",
                    "assets/banner-light.svg", "assets/demo.svg", "assets/icon.svg", "assets/social-preview.png",
                    "examples/README.md", "tests/run.py"]:
            self.assertTrue(os.path.exists(os.path.join(ROOT, rel)), rel)

    def test_repo_json(self):
        r = json.loads(read(".github/repo.json"))
        self.assertEqual(r["name"], REPO)
        self.assertTrue(r["description"])
        self.assertLessEqual(len(r["topics"]), 20)
        self.assertIn("utm_campaign=" + REPO, r["homepage"])


class TestHygiene(unittest.TestCase):
    def test_forbidden_strings(self):
        hits = []
        for rel in tracked_text_files():
            for n, line in enumerate(read(rel).splitlines(), 1):
                low = line.lower()
                for bad in FORBIDDEN:
                    if bad.lower() in low:
                        if bad == "/Volumes/" and "conventions-allow: abs-path" in line:
                            continue
                        if bad == "node_modules" and rel in (".gitignore", "tests/test_adapters.py"):
                            continue
                        if rel == "tests/test_adapters.py":
                            continue
                        hits.append("%s:%d: %s" % (rel, n, bad))
        self.assertEqual(hits, [])

    def test_copyright_is_brand(self):
        for rel in tracked_text_files():
            if rel == "tests/test_adapters.py":
                continue
            for line in read(rel).splitlines():
                if "Copyright (c)" in line:
                    self.assertIn("UniqAI", line, rel)

    def test_utm_on_every_uniqai_link(self):
        bad = []
        for rel in tracked_text_files():
            for m in re.finditer(r"https://uniqai\.app[^\s)\"'<>]*", read(rel)):
                url = m.group(0)
                if url.endswith("?"):  # string concatenation in scripts: "...?" + UTM
                    continue
                if "utm_campaign=video-director" not in url:
                    bad.append("%s: %s" % (rel, url))
        self.assertEqual(bad, [])

    def test_readme_uniqai_link_budget(self):
        readme = read("README.md")
        links = re.findall(r"https://uniqai\.app[^\s)\"'<>]*", readme)
        self.assertLessEqual(len(links), 3, links)
        self.assertEqual(readme.count("Made by"), 1)

    def test_asset_sizes(self):
        limits = {"assets/banner.svg": 30, "assets/banner-light.svg": 30, "assets/demo.svg": 60,
                  "assets/social-preview.png": 200, "assets/icon.svg": 8}
        for rel, kb in limits.items():
            self.assertLessEqual(os.path.getsize(os.path.join(ROOT, rel)), kb * 1024, rel)

    def test_no_external_resources_in_svgs(self):
        for rel in ("assets/banner.svg", "assets/banner-light.svg", "assets/demo.svg", "assets/icon.svg"):
            text = read(rel)
            self.assertNotIn("<script", text, rel)
            self.assertNotIn("http://", text.replace("http://www.w3.org", ""), rel)
            self.assertNotIn("<image", text, rel)


if __name__ == "__main__":
    unittest.main()
