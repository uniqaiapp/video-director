# video-director for Codex

Paste the block below into your project's AGENTS.md (or Codex custom instructions),
and copy `SKILL.md`, `scripts/` and `references/` from https://github.com/uniqaiapp/video-director into `.agents/skills/video-director/`.

---
When the user asks for an AI video prompt, a storyboard, a shot list, or a prompt for Kling, Veo, Wan, Seedance or Runway, follow `.agents/skills/video-director/SKILL.md`: write the timed storyboard JSON, run `python3 .agents/skills/video-director/scripts/storyboard.py check <file> --model <model>`, fix every ERROR, then `render --model <model>` and return the prompt with its negative field and notes.
---
