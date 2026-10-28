<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="video-director: Turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary." src="assets/banner.svg" width="1280" height="320">
</picture>

# video-director: AI video prompts for Kling, Veo 3, Wan and Runway

[![License: MIT](https://img.shields.io/badge/license-MIT-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#install)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#install)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#install)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-d1fe17?style=flat-square&labelColor=0d0f12)](#install)

**Idea in, second-by-second storyboard out, rendered as a prompt in each model's own shape.**

[Quickstart](#quickstart) · [How it works](#how-it-works) · [Examples](#examples) · [Install](#install) · [FAQ](#faq)

</div>

AI video prompts for Kling 3.0, Veo 3, Wan 2.5, Seedance and Runway, written the way the models read them: a timed storyboard (0-2 s, 2-4 s, ...) with one camera move per beat, a lens, a light setup, a sentence of motion physics, three layers of sound and a short negative list, then rendered per model with its length limit, negative-prompt handling and audio support applied. Works for text-to-video and image-to-video. It ships as a Claude Code skill, a Cursor rule and a Codex / `AGENTS.md` snippet, plus a stdlib Python script you can run without any agent.

| **Storyboard first** | **Per-model rendering** | **Vocabulary that works** |
|:---|:---|:---|
| The script scaffolds a beat grid and refuses to render until every slot is filled and the timeline adds up. | One storyboard becomes a Kling multi-shot prompt, a Veo single take with quoted dialogue, an 800-character Wan prompt, numbered Seedance shots or a positive-only Runway prompt. | Eight reference tables (camera, lens, light, physics, sound, negatives, model limits, format) that the agent and the `vocab` command pull from. |

## Quickstart

```bash
git clone https://github.com/uniqaiapp/video-director
cd video-director
python3 scripts/storyboard.py new --idea "latte art at dawn" -o board.json   # scaffold with [[fill: ...]] slots
python3 scripts/storyboard.py check examples/latte-art-dawn.json --model kling
python3 scripts/storyboard.py render examples/latte-art-dawn.json --model kling
```

The first command writes a storyboard skeleton with a 2-second beat grid and pre-filled lens, camera and sound hints (the idea mentions a pour and dawn). The agent, or you, fills the slots; `check` validates; `render` prints the prompt, its negative field and the notes for that model.

## Demo

<img alt="video-director demo: scaffold a storyboard, check an example, render it for Kling 3.0" src="assets/demo.svg" width="820">

## How it works

1. **Scaffold.** `new` turns the idea into JSON: beats every 2 seconds (the last one absorbs the remainder), `[[fill: ...]]` markers for subject, setting, style and each beat, and keyword hints for lens, camera, light, physics and sound when the idea is obviously macro, aerial, night, portrait, product, underwater, chase or sci-fi.
2. **Fill.** The skill (`SKILL.md`) tells the agent how: one event per beat, the first beat establishes and the last one holds, one camera move per two beats, concrete nouns, physics as one sentence, sound as three phrases, negatives as nouns. Vocabulary comes from `references/`.
3. **Check.** Structural errors (unfilled slots, gaps in the timeline, prompt over a hard cap) fail; model-fit problems warn: Veo only does 4/6/8 s, Wan and Runway 5/10 s, Runway ignores negatives and has no audio, a cut on a single-shot model.
4. **Render.** The same storyboard in each model's shape. Kling reads subject, look, timed shots, motion, audio; Veo gets "one continuous take" with beats joined by "Then", quoted dialogue, and `subtitles, captions` added to its negative field because it burns subtitles in otherwise; Wan gets the terse layout; Seedance gets `Shot 1 (0-2s): ...`; Runway gets the camera first and positive phrasing only.

```
idea ──new──▶ board.json ──fill (agent)──▶ check ──▶ render --model kling | veo | wan | seedance | runway
                                             ▲                   │
                                             └── fix one field ◀─┘  (floating → physics, flat → light, artefacts → negative)
```

Model limits live in one table (`python3 scripts/storyboard.py models`) with the date they were read from the vendor docs; `references/model-notes.md` has the sources. There are no quality scores or benchmarks in this repo: the script enforces structure and limits, the clip quality depends on the beats.

## Examples

Twelve storyboards in [`examples/`](examples/README.md), each with a Markdown page showing the timeline and the rendered prompt for every model. The pages are regenerated by the tests, so they match the script.

<details>
<summary><b>Neon rain street (Veo 3, 8 s, vertical, dialogue): storyboard → prompt</b></summary>

**Storyboard** (`examples/neon-rain-street.json`, abridged)

```text
0-2s  she stands under the awning watching the rain, neon reflections sliding across her coat   | slow push-in at eye level, framed waist-up
2-4s  a car passes, its headlights sweep across her face; she turns to the camera                | continue the push-in
4-6s  she says the line, half smiling                                                            | hold on a medium close-up
6-8s  she steps out into the rain and opens the umbrella                                         | slow tilt up following the umbrella
physics: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles
sound:   steady rain, tyres on wet asphalt, a distant siren | umbrella snapping open | She says, quietly, lip-synced: "You're late. Again."
```

**Veo 3 prompt** (`render --model veo`)

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. One continuous take over 8 seconds. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Negative field: `morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter, subtitles, captions`

Full page with every model: [examples/neon-rain-street.md](examples/neon-rain-street.md).

</details>

<details>
<summary><b>Sneaker turntable (Runway Gen-4, 5 s, image-to-video): what gets dropped and why</b></summary>

Runway reads positive phrasing only and has no native audio, so `render --model runway` leads with the camera move, keeps the beats and physics, and drops the negative list and the sound block. The notes say so, and `check --model runway` prints the same two warnings. The storyboard keeps both for the edit.

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

Full page: [examples/sneaker-turntable.md](examples/sneaker-turntable.md).

</details>

<details>
<summary><b>Desert car chase (Kling 3.0, 10 s): a deliberate cut, and what single-shot models say about it</b></summary>

Beat 4 is "cut to an interior over-the-shoulder shot". Kling 3.0 follows timed beats as shots, so the prompt keeps it. `check --model veo` answers:

```text
WARN   desert-car-chase.json: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
WARN   desert-car-chase.json: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
OK     desert-car-chase.json: 5 beats, 10s, 2 warning(s) for Veo 3 / 3.1
```

Full page: [examples/desert-car-chase.md](examples/desert-car-chase.md).

</details>

| Storyboard | Target | Shows |
|---|---|---|
| [latte-art-dawn](examples/latte-art-dawn.md) | Kling 3.0, 8 s | the baseline: one subject, one light, one liquid |
| [candle-confession](examples/candle-confession.md) | Veo 3, 8 s | single light source, a 3-second dialogue beat |
| [sci-fi-corridor-reveal](examples/sci-fi-corridor-reveal.md) | Veo 3, 8 s | a light change as the event |
| [coastline-drone-dawn](examples/coastline-drone-dawn.md) | Wan 2.5, 10 s | five aerial beats under the 800-character cap |
| [ramen-steam-macro](examples/ramen-steam-macro.md) | Wan 2.5, 5 s, 9:16 | macro, steam and liquid physics |
| [fashion-tunnel-walk](examples/fashion-tunnel-walk.md) | Kling 3.0, 10 s, 9:16 | image-to-video, walking and silk physics |
| [cat-window-rain](examples/cat-window-rain.md) | Seedance 2.0, 5 s | micro-motion, numbered shots |
| [jellyfish-drift](examples/jellyfish-drift.md) | Seedance 2.0, 10 s | underwater drag, caustics, rack focus |
| [rooftop-timelapse-dusk](examples/rooftop-timelapse-dusk.md) | generic, 12 s | 3-second beats; length warnings on Veo, Wan, Runway |

## Install

Works with every agent that reads instruction files. Python 3.9+ (or any Python 3 you already have). No packages to install.

<details open>
<summary><b>Claude Code</b></summary>

```bash
# user-level
git clone https://github.com/uniqaiapp/video-director ~/.claude/skills/video-director
# or project-level
git clone https://github.com/uniqaiapp/video-director .claude/skills/video-director
```

Then `/video-director` in any session, or just describe the clip; the skill's `description` triggers it. `npx skills add uniqaiapp/video-director` works too once the repo is public. As a plugin, once the uniqaiapp marketplace is published: `/plugin marketplace add uniqaiapp/skills` then `/plugin install video-director@uniqaiapp`.

</details>

<details>
<summary><b>Cursor</b></summary>

Copy `SKILL.md`, `scripts/`, `references/` and [`.cursor/rules/video-director.mdc`](.cursor/rules/video-director.mdc) into your project. The rule file embeds the skill with `@SKILL.md`.

</details>

<details>
<summary><b>Codex / any AGENTS.md agent</b></summary>

Copy `SKILL.md`, `scripts/` and `references/` into `.agents/skills/video-director/` and add the snippet from [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) to your `AGENTS.md`. The repo's own [`AGENTS.md`](AGENTS.md) is the generic version.

</details>

<details>
<summary><b>Without an agent</b></summary>

Every command runs standalone: `python3 scripts/storyboard.py --help`. Paste [`SKILL.md`](SKILL.md) into any model's system prompt; it has no agent-specific syntax outside the frontmatter.

</details>

## Usage

```bash
python3 scripts/storyboard.py models                                   # limits table with its check date
python3 scripts/storyboard.py new --idea "..." --duration 8 --model veo --aspect 9:16 -o board.json
python3 scripts/storyboard.py vocab camera orbit                      # also: lens, light, physics, sound, negative
python3 scripts/storyboard.py check board.json --model veo
python3 scripts/storyboard.py render board.json --model veo           # or kling,wan  or  all --format md -o board.md
```

Where to run the prompt: Kling 3.0, Veo 3 and Wan 2.5 are available side by side in [UniqAI's text-to-video composer](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=readme&utm_campaign=video-director), so one storyboard can be tried on three models from the same page; any other front end or API works the same way, the prompt is plain text.

## FAQ

<details>
<summary><b>Which model should I pick?</b></summary>

Dialogue or sound that matters: Veo 3 (strongest native audio, but 8 s max). A cut inside the clip or 10-15 s: Kling 3.0 or Seedance 2.0 (multi-shot). A start image and a product: Runway Gen-4 or Kling. A cheap first pass: Wan 2.5, keep the prompt short. The `check` command tells you what will not fit before you spend credits.

</details>

<details>
<summary><b>The clip floats, slides or morphs. What do I change?</b></summary>

One field at a time: floating or sliding is `physics` ("feet plant firmly on each step", "the cup rests on the saucer"); morphing is usually too many events, so remove a beat or turn the last one into a hold; artefacts go in `negative` as nouns. Re-check, re-render. `references/motion-physics.md` has the phrases.

</details>

<details>
<summary><b>Are the model limits current?</b></summary>

They were read from each vendor's documentation on the date printed by `python3 scripts/storyboard.py models` and listed with sources in `references/model-notes.md`. Vendors change limits without notice. When the check disagrees with the vendor page, trust the page and open an issue or a PR with the URL and date.

</details>

<details>
<summary><b>Does this work for Sora, Hailuo, Luma, Pika?</b></summary>

Use `--model generic`: the full structured prompt with a separate negative list, which you trim to the model's limit by hand. `sora` is accepted as an alias for `generic` because OpenAI discontinued Sora in 2026 and there is no live target to format for. PRs adding a model need its documented limits with a source.

</details>

## Related

- [awesome-ai-video-prompts](https://github.com/uniqaiapp/awesome-ai-video-prompts): curated, categorised prompts for AI video models with the settings that produced them, as JSON and Markdown.
- [ai-video-pricing](https://github.com/uniqaiapp/ai-video-pricing): hand-checked price table for AI video generation, per second and per clip, with source URL and check date on every row.
- [ugc-ad-director](https://github.com/uniqaiapp/ugc-ad-director): script and shot-list short UGC-style ads for AI video: hook, proof, offer, with per-model prompt output.
- [no-plastic](https://github.com/uniqaiapp/no-plastic): prompt rules and a checker for natural-looking AI portraits: skin texture, lighting and lens choices that avoid the plastic look.

## Contributing

Issues and pull requests are welcome. Keep changes small and include a storyboard plus its rendered prompt in the PR description. See [CONTRIBUTING.md](CONTRIBUTING.md) for the local checks (`python3 tests/run.py`, no dependencies).

## License

Code and examples: [MIT](LICENSE). The vocabulary in `references/`: CC BY 4.0, attribution "UniqAI, github.com/uniqaiapp/video-director". © UniqAI

---

<div align="center">

<sub>Made by <a href="https://uniqai.app/?utm_source=github&utm_medium=readme&utm_campaign=video-director">UniqAI</a>, an AI photo, video and chat app: Kling 3.0, Veo 3, Flux, Nano Banana and GPT-5/Claude/Gemini/Grok in one place. We wrote this skill to stop re-explaining camera moves to ourselves.</sub>

</div>
