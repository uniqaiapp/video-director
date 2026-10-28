# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-10-28

### Added
- `SKILL.md`: the storyboarding workflow (idea to timed beats to per-model prompt) for Claude Code, with Cursor, Codex and generic `AGENTS.md` adapters.
- `scripts/storyboard.py`: `new`, `check`, `render`, `models`, `vocab` commands; stdlib only.
- Model targets: Kling 3.0, Veo 3 / 3.1, Wan 2.5, Seedance 2.0, Runway Gen-4 / 4.5, generic; limits dated 2026-10-28 in `references/model-notes.md`.
- `references/`: camera moves, lenses, lighting, motion physics, sound design, negative prompts, storyboard format (CC BY 4.0).
- Twelve example storyboards in `examples/`, each with its rendered prompts for every model.
- Tests (`python3 tests/run.py`), CI workflow, issue and PR templates, banner, terminal demo and social preview assets.
