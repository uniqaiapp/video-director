# Sci-fi corridor reveal

> a lone engineer walks down a dark spaceship corridor and a door opens onto a planet

| | |
|---|---|
| Mode | text-to-video |
| Duration | 8 s |
| Aspect | 16:9 |
| Lens | 24mm anamorphic, deep focus, horizontal flares |
| Light | cold blue strip lights along the floor as key, a warm orange glow leaking from the door at the end |
| Style | hard sci-fi, cold palette with a single warm accent, volumetric haze, anamorphic flares |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | she walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls | following shot from behind at shoulder height |
| 2-4s | the door at the end slides open with a hiss and warm light floods the corridor | continue following, the warm light growing |
| 4-6s | she stops in the doorway; beyond it a vast orange planet fills the sky | slow push past her shoulder towards the view |
| 6-8s | she lowers the scanner and stares; dust drifts in the light | hold, framing her silhouette against the planet |

**Motion physics.** haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight

**Sound.** Ambience: low ship hum, ventilation. Effects: boots on metal, the door hiss, a soft rising tone as the light floods in.

**Negative.** morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, cartoon

**Notes.** Light change is the beat: the warm door light is the only event the model needs to get right.

## Prompts

### Kling 3.0

```text
A female engineer in a worn grey jumpsuit with a tool belt, short hair, carrying a handheld scanner in a long, dim spaceship corridor with ribbed metal walls, thin haze in the air. Hard sci-fi, cold palette with a single warm accent, volumetric haze, anamorphic flares. 24mm anamorphic, deep focus, horizontal flares. Cold blue strip lights along the floor as key, a warm orange glow leaking from the door at the end. 0-2s: She walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls. Camera: following shot from behind at shoulder height. 2-4s: The door at the end slides open with a hiss and warm light floods the corridor. Camera: continue following, the warm light growing. 4-6s: She stops in the doorway; beyond it a vast orange planet fills the sky. Camera: slow push past her shoulder towards the view. 6-8s: She lowers the scanner and stares; dust drifts in the light. Camera: hold, framing her silhouette against the planet. Motion: haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight. Audio. Ambience: low ship hum, ventilation. Sound effects: boots on metal, the door hiss, a soft rising tone as the light floods in.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, cartoon
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A female engineer in a worn grey jumpsuit with a tool belt, short hair, carrying a handheld scanner in a long, dim spaceship corridor with ribbed metal walls, thin haze in the air. Hard sci-fi, cold palette with a single warm accent, volumetric haze, anamorphic flares. 24mm anamorphic, deep focus, horizontal flares. Cold blue strip lights along the floor as key, a warm orange glow leaking from the door at the end. One continuous take over 8 seconds. She walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls. Camera: following shot from behind at shoulder height. Then the door at the end slides open with a hiss and warm light floods the corridor. Camera: continue following, the warm light growing. Then she stops in the doorway; beyond it a vast orange planet fills the sky. Camera: slow push past her shoulder towards the view. Then she lowers the scanner and stares; dust drifts in the light. Camera: hold, framing her silhouette against the planet. Motion: haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight. Audio. Ambience: low ship hum, ventilation. Sound effects: boots on metal, the door hiss, a soft rising tone as the light floods in.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, cartoon
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- [Run in UniqAI](https://uniqai.app/models/veo?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A female engineer in a worn grey jumpsuit with a tool belt, short hair, carrying a handheld scanner in a long, dim spaceship corridor with ribbed metal walls, thin haze in the air. 24mm anamorphic, deep focus, horizontal flares. Cold blue strip lights along the floor as key, a warm orange glow leaking from the door at the end. She walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls. Camera: following shot from behind at shoulder height. Then the door at the end slides open with a hiss and warm light floods the corridor. Camera: continue following, the warm light growing. Then she stops in the doorway; beyond it a vast orange planet fills the sky. Camera: slow push past her shoulder towards the view. Then she lowers the scanner and stares; dust drifts in the light. Camera: hold, framing her silhouette against the planet. Motion: haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight. Audio. Ambience: low ship hum, ventilation. Sound effects: boots on metal, the door hiss, a soft rising tone as the light floods in.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, cartoon
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 1167 characters, limit is 800
- Check: Wan 2.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- [Run in UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A female engineer in a worn grey jumpsuit with a tool belt, short hair, carrying a handheld scanner in a long, dim spaceship corridor with ribbed metal walls, thin haze in the air. Hard sci-fi, cold palette with a single warm accent, volumetric haze, anamorphic flares. 24mm anamorphic, deep focus, horizontal flares. Cold blue strip lights along the floor as key, a warm orange glow leaking from the door at the end. Shot 1 (0-2s): She walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls. Camera: following shot from behind at shoulder height. Shot 2 (2-4s): The door at the end slides open with a hiss and warm light floods the corridor. Camera: continue following, the warm light growing. Shot 3 (4-6s): She stops in the doorway; beyond it a vast orange planet fills the sky. Camera: slow push past her shoulder towards the view. Shot 4 (6-8s): She lowers the scanner and stares; dust drifts in the light. Camera: hold, framing her silhouette against the planet. Motion: haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight. Audio. Ambience: low ship hum, ventilation. Sound effects: boots on metal, the door hiss, a soft rising tone as the light floods in. Avoid: morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, cartoon.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Following shot from behind at shoulder height: A female engineer in a worn grey jumpsuit with a tool belt, short hair, carrying a handheld scanner in a long, dim spaceship corridor with ribbed metal walls, thin haze in the air. She walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls. Camera: following shot from behind at shoulder height. Then the door at the end slides open with a hiss and warm light floods the corridor. Camera: continue following, the warm light growing. Then she stops in the doorway; beyond it a vast orange planet fills the sky. Camera: slow push past her shoulder towards the view. Then she lowers the scanner and stares; dust drifts in the light. Camera: hold, framing her silhouette against the planet. Motion: haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight. Hard sci-fi, cold palette with a single warm accent, volumetric haze, anamorphic flares.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- **Does not fit:** Runway Gen-4 / 4.5: prompt is 1022 characters, limit is 1000
- Check: Runway Gen-4 / 4.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A female engineer in a worn grey jumpsuit with a tool belt, short hair, carrying a handheld scanner in a long, dim spaceship corridor with ribbed metal walls, thin haze in the air. Hard sci-fi, cold palette with a single warm accent, volumetric haze, anamorphic flares. 24mm anamorphic, deep focus, horizontal flares. Cold blue strip lights along the floor as key, a warm orange glow leaking from the door at the end. 0-2s: She walks away from the camera down the corridor, boots echoing, scanner light sweeping the walls. Camera: following shot from behind at shoulder height. 2-4s: The door at the end slides open with a hiss and warm light floods the corridor. Camera: continue following, the warm light growing. 4-6s: She stops in the doorway; beyond it a vast orange planet fills the sky. Camera: slow push past her shoulder towards the view. 6-8s: She lowers the scanner and stares; dust drifts in the light. Camera: hold, framing her silhouette against the planet. Motion: haze swirls as she passes; the door moves on a mechanical track at constant speed; dust catches the light and drifts slowly; her boots land with weight. Audio. Ambience: low ship hum, ventilation. Sound effects: boots on metal, the door hiss, a soft rising tone as the light floods in.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, cartoon
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
