# Storyboard file format

A storyboard is one JSON object. `python3 scripts/storyboard.py new --idea "..." -o board.json` writes a scaffold with `[[fill: ...]]` slots; `check` refuses to pass while any remain.

```json
{
  "title": "Latte art at dawn",
  "idea": "a barista pours latte art at dawn in an empty cafe",
  "mode": "t2v",
  "duration_s": 8,
  "aspect": "16:9",
  "model": "kling",
  "style": "Kodak 250D look, warm highlights, muted shadows, fine grain",
  "subject": "a barista in a grey apron, sleeves rolled, steady hands",
  "setting": "an empty cafe at dawn, counter lit by low sun through the front window",
  "lens": "100mm macro, f/4, shallow depth of field",
  "light": "low golden sun as key from camera-right, soft bounce fill, steam backlit",
  "beats": [
    {"t": [0, 2], "action": "the milk jug tilts and a thin stream hits the crema", "camera": "locked-off, top-down on the cup"},
    {"t": [2, 4], "action": "the stream wobbles side to side; a white heart forms", "camera": "slow push-in on the cup"},
    {"t": [4, 6], "action": "the jug lifts and draws a line through the heart", "camera": "continue the push-in"},
    {"t": [6, 8], "action": "the barista sets the jug down; steam rises off the cup", "camera": "hold"}
  ],
  "physics": "milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight",
  "sound": {"ambience": "quiet cafe, espresso machine idling", "fx": "milk pouring, ceramic tap as the jug lands", "dialogue": ""},
  "negative": ["morphing", "extra limbs", "warped hands", "flicker", "text", "watermark", "logo", "jump cuts"],
  "image_ref": "",
  "notes": ""
}
```

## Fields

| Field | Type | Rule |
|---|---|---|
| `title` | string | short, used as a heading |
| `idea` | string | the original one-liner, kept verbatim |
| `mode` | `t2v` or `i2v` | image-to-video requires `image_ref` |
| `duration_s` | number | must equal the end of the last beat |
| `aspect` | string | `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `21:9`; checked against the model |
| `model` | string | default target for `check` and `render`; any key from `models` |
| `style` | string | film stock, grade, era, mood; one line |
| `subject` | string | who or what, with two or three concrete visual details |
| `setting` | string | where and when, with one texture and one light or weather cue |
| `lens` | string | focal length, aperture, depth of field (see lenses.md) |
| `light` | string | key, fill, rim, practicals, time of day (see lighting.md) |
| `beats` | list | contiguous `t` ranges from 0 to `duration_s`; each has `action` and optional `camera`, `notes` |
| `physics` | string | how things move (see motion-physics.md) |
| `sound` | object or null | `ambience`, `fx`, `dialogue`; dialogue in quotes with a speaker |
| `negative` | list of strings | nouns, 6-10 items (see negative-prompts.md) |
| `image_ref` | string | i2v only: what the start frame shows and what must stay fixed |
| `notes` | string | anything for the human editor; never rendered into prompts |

## Beat rules the check command enforces

- Beats are contiguous and end exactly at `duration_s`.
- A beat longer than 4 seconds gets a warning: it almost always contains two events.
- An action over 45 words gets a warning: models follow short, concrete beats.
- Negative terms that start with "no", "not", "without" or "avoid" get a warning.

## Timing guide

| Clip length | Beats | Shape |
|---|---|---|
| 4-5 s | 2-3 | establish, one change, hold |
| 6-8 s | 3-4 | establish, develop, turn, resolve |
| 10 s | 4-5 | add a second development beat; keep the last beat as a hold |
| 12-15 s | 5-7 | two mini-scenes or one scene with a light change; only on multi-shot models |

The first beat sets the frame; the last beat is a hold or a reveal, never a new event, because models run out of frames and either freeze or invent something.
