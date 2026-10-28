# Examples

Twelve finished storyboards. Each `.json` is the storyboard; the `.md` next to it is produced by

```bash
python3 scripts/storyboard.py render examples/<name>.json --model all --format md -o examples/<name>.md
```

and contains the timeline plus the rendered prompt, negative field and fit warnings for every model. `tests/test_scripts.py` re-renders each one and fails if the committed `.md` differs, so what you read here is what the script prints.

| Storyboard | Target | Length | Mode | What it shows |
|---|---|---|---|---|
| [latte-art-dawn](latte-art-dawn.md) | Kling 3.0 | 8 s | T2V | the baseline: one subject, one light, one liquid; a good first test on any model |
| [neon-rain-street](neon-rain-street.md) | Veo 3 | 8 s, 9:16 | T2V | dialogue with lip sync, vertical framing, neon practicals; Veo gets `subtitles, captions` in its negative field |
| [candle-confession](candle-confession.md) | Veo 3 | 8 s | T2V | single light source, Rembrandt setup, a 3-second dialogue beat |
| [sci-fi-corridor-reveal](sci-fi-corridor-reveal.md) | Veo 3 | 8 s | T2V | a light change as the event, following shot, volumetric haze |
| [coastline-drone-dawn](coastline-drone-dawn.md) | Wan 2.5 | 10 s | T2V | aerial with five beats kept under Wan's 800-character prompt field |
| [ramen-steam-macro](ramen-steam-macro.md) | Wan 2.5 | 5 s, 9:16 | T2V | macro food shot, steam and liquid physics, terse layout |
| [sneaker-turntable](sneaker-turntable.md) | Runway Gen-4 | 5 s, 1:1 | I2V | product orbit from a start image; Runway drops negatives and audio, the notes say so |
| [fashion-tunnel-walk](fashion-tunnel-walk.md) | Kling 3.0 | 10 s, 9:16 | I2V | walking physics, silk, a pull-back ahead of the subject, start-frame description |
| [desert-car-chase](desert-car-chase.md) | Kling 3.0 | 10 s | T2V | a deliberate cut at 6 s; single-shot models get a warning about beat 4 |
| [cat-window-rain](cat-window-rain.md) | Seedance 2.0 | 5 s | T2V | small animal micro-motion, three beats, numbered-shot output |
| [jellyfish-drift](jellyfish-drift.md) | Seedance 2.0 | 10 s | T2V | underwater drag, caustics, a rack focus beat |
| [rooftop-timelapse-dusk](rooftop-timelapse-dusk.md) | generic | 12 s | T2V | 3-second beats, timelapse physics; shows the length warnings on Veo, Wan and Runway |

## Reading a rendered page

Each `.md` has the same sections: a header table (mode, duration, aspect, lens, light, style), the timeline, physics, sound, negatives, then one `### Model` block per target with the prompt in a code block, the negative field where the model has one, the render notes, and `Check:` lines for anything that does not fit that model. A `**Does not fit:**` line means the prompt breaks a hard limit on that model and needs trimming.

## Adding one

1. `python3 scripts/storyboard.py new --idea "..." --duration 8 --model kling -o examples/<name>.json`
2. Fill every `[[fill: ...]]` slot; follow `SKILL.md` step 3.
3. `python3 scripts/storyboard.py check examples/<name>.json` until it says `OK`.
4. Render the `.md` with the command at the top, add a row to the table above, and say in the row what the clip actually looked like on the target model.
