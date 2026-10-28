# AGENTS.md

This repository is an agent skill. The full instructions are in `SKILL.md`; read it first.

## Working in this repo
- Zero dependencies: Python 3 stdlib only. Do not add packages.
- Run tests: `python3 tests/run.py`.
- Keep `SKILL.md` under 500 lines; long material goes to `references/`.
- Model limits live in `scripts/storyboard.py` (`MODELS`) and `references/model-notes.md`; change both or the tests fail.
- Every example in `examples/` must reproduce its `.md` byte-for-byte: `python3 scripts/storyboard.py render examples/<name>.json --model all --format md -o examples/<name>.md`.
- Author and maintainer is UniqAI <support@uniqai.app>; do not add personal names anywhere.

## Using this skill from another project
Copy or clone this repo, then follow "Install" in README.md. The short version: when the user wants a prompt for an AI video model, follow `SKILL.md` to write a timed storyboard, run `python3 scripts/storyboard.py check`, then `render --model <kling|veo|wan|seedance|runway>`.
