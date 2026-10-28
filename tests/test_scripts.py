"""Script tests: CLI help, every example checks clean and reproduces its committed rendering byte-for-byte,
model table matches references/model-notes.md, scaffolds behave."""
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from scripts import storyboard  # noqa: E402

SCRIPT = os.path.join(ROOT, "scripts", "storyboard.py")
EXAMPLES = sorted(glob.glob(os.path.join(ROOT, "examples", "*.json")))


def run(*argv, cwd=None):
    p = subprocess.run([sys.executable, SCRIPT] + list(argv), capture_output=True, text=True, cwd=cwd or ROOT)
    return p.returncode, p.stdout, p.stderr


class TestCli(unittest.TestCase):
    def test_help(self):
        code, out, _ = run("--help")
        self.assertEqual(code, 0)
        self.assertIn("storyboard", out)
        for sub in ("new", "check", "render", "models", "vocab"):
            code, out, _ = run(sub, "--help")
            self.assertEqual(code, 0, sub)

    def test_runs_from_any_cwd(self):
        code, out, _ = run("models", cwd=tempfile.gettempdir())
        self.assertEqual(code, 0)
        self.assertIn("kling", out)

    def test_vocab(self):
        code, out, _ = run("vocab", "camera", "orbit")
        self.assertEqual(code, 0)
        self.assertIn("orbit", out.lower())
        for topic in storyboard.VOCAB_FILES:
            code, out, _ = run("vocab", topic)
            self.assertEqual(code, 0, topic)
            self.assertRegex(out, r"\d+ of \d+ entries")


class TestExamples(unittest.TestCase):
    def test_at_least_ten_examples(self):
        self.assertGreaterEqual(len(EXAMPLES), 10)

    def test_every_example_checks_clean(self):
        for path in EXAMPLES:
            code, out, err = run("check", path)
            self.assertEqual(code, 0, path + "\n" + out + err)
            self.assertIn("OK", out)

    def test_every_example_reproduces_markdown(self):
        for path in EXAMPLES:
            md = path[:-5] + ".md"
            self.assertTrue(os.path.exists(md), md)
            code, out, _ = run("render", path, "--model", "all", "--format", "md")
            self.assertEqual(code, 0, path)
            with open(md, "r", encoding="utf-8") as f:
                self.assertEqual(out, f.read(), "examples/%s is stale; re-run the render command in examples/README.md" % os.path.basename(md))

    def test_every_model_renders_every_example(self):
        for path in EXAMPLES:
            board = storyboard.load(path)
            for m in storyboard.MODEL_ORDER:
                r = storyboard.render(board, m)
                self.assertTrue(r["prompt"])
                self.assertNotIn("[[fill", r["prompt"])
                if storyboard.MODELS[m]["negative"] == "none":
                    self.assertEqual(r["negative"], "")

    def test_hard_limits_hold_on_targeted_examples(self):
        for path in EXAMPLES:
            board = storyboard.load(path)
            m = board.get("model")
            cap = storyboard.MODELS[m]["prompt_max"]
            if cap:
                self.assertLessEqual(len(storyboard.render(board, m)["prompt"]), cap, path)

    def test_examples_readme_lists_every_example(self):
        with open(os.path.join(ROOT, "examples", "README.md"), "r", encoding="utf-8") as f:
            readme = f.read()
        for path in EXAMPLES:
            self.assertIn(os.path.basename(path)[:-5] + ".md", readme)


class TestScaffold(unittest.TestCase):
    def test_new_then_check_fails_until_filled(self):
        with tempfile.TemporaryDirectory() as d:
            out = os.path.join(d, "b.json")
            code, text, _ = run("new", "--idea", "a drone flies over a rainy neon city at night", "--duration", "8", "-o", out)
            self.assertEqual(code, 0)
            self.assertIn("4 beats", text)
            board = storyboard.load(out)
            self.assertEqual([b["t"] for b in board["beats"]], [[0, 2], [2, 4], [4, 6], [6, 8]])
            self.assertIn("aerial", board["beats"][0]["camera"])
            self.assertIn("neon", board["light"])
            code, text, _ = run("check", out)
            self.assertEqual(code, 1)
            self.assertIn("unfilled", text)
            raw = json.dumps(board)
            filled = json.loads(re.sub(r"\[\[fill:[^\]]*\]\]", "filled", raw))
            with open(out, "w", encoding="utf-8") as f:
                json.dump(filled, f)
            code, text, _ = run("check", out, "--model", "kling")
            self.assertEqual(code, 0, text)

    def test_beat_grid(self):
        self.assertEqual(storyboard.beat_grid(5), [[0, 2], [2, 4], [4, 5]])
        self.assertEqual(storyboard.beat_grid(10, 3), [[0, 3], [3, 6], [6, 9], [9, 10]])

    def test_check_catches_gaps_and_negatives(self):
        board = storyboard.load(EXAMPLES[0])
        board["beats"][1]["t"] = [3, 4]
        board["negative"].append("no text")
        errors, warns = storyboard.check_board(board)
        self.assertTrue(any("contiguous" in e for e in errors))
        self.assertTrue(any("no text" in w for w in warns))

    def test_model_fit_warnings(self):
        board = storyboard.load(os.path.join(ROOT, "examples", "rooftop-timelapse-dusk.json"))
        _, warns = storyboard.check_board(board, "veo")
        self.assertTrue(any("not an available length" in w for w in warns))
        _, warns = storyboard.check_board(board, "runway")
        self.assertTrue(any("ignores negative" in w for w in warns))
        self.assertTrue(any("no native audio" in w for w in warns))

    def test_veo_adds_subtitles_negative_with_dialogue(self):
        board = storyboard.load(os.path.join(ROOT, "examples", "candle-confession.json"))
        self.assertIn("subtitles", storyboard.render(board, "veo")["negative"])
        self.assertNotIn("subtitles", storyboard.render(board, "kling")["negative"])

    def test_wan_limit_is_enforced(self):
        board = storyboard.load(os.path.join(ROOT, "examples", "desert-car-chase.json"))
        board["physics"] = board["physics"] * 6
        errors, _ = storyboard.check_board(board, "wan")
        self.assertTrue(any("limit is 800" in e for e in errors))


class TestModelNotesInSync(unittest.TestCase):
    def test_table_matches_script(self):
        rows = list(storyboard.read_tables(os.path.join(ROOT, "references", "model-notes.md")))
        table = {r[0].strip("`"): r for r in rows[1:] if r[0].startswith("`")}
        for key in storyboard.MODEL_ORDER:
            self.assertIn(key, table, key)
            m = storyboard.MODELS[key]
            row = table[key]
            self.assertEqual(row[2], storyboard.durations_text(m), key)
            self.assertEqual(row[4].startswith("yes"), m["audio"] == "native", key)
            if m["prompt_max"]:
                self.assertIn(str(m["prompt_max"]), row[5], key)
        self.assertIn(storyboard.CHECKED_ON, open(os.path.join(ROOT, "references", "model-notes.md"), encoding="utf-8").read())


if __name__ == "__main__":
    unittest.main()
