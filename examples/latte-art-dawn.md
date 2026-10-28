# Latte art at dawn

> a barista pours latte art at dawn in an empty cafe

| | |
|---|---|
| Mode | text-to-video |
| Duration | 8 s |
| Aspect | 16:9 |
| Lens | 100mm macro, f/4, shallow depth of field |
| Light | low golden sun as key from camera-right, soft bounce fill, steam backlit |
| Style | Kodak 250D look, warm highlights, muted shadows, fine grain |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | the milk jug tilts and a thin white stream hits the brown crema | locked-off, top-down on the cup |
| 2-4s | the stream wobbles side to side and a white heart forms on the surface | slow push-in on the cup |
| 4-6s | the jug lifts and draws a thin line through the heart | continue the push-in |
| 6-8s | the barista sets the jug down; steam rises off the cup | hold |

**Motion physics.** milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap

**Sound.** Ambience: quiet cafe, espresso machine idling. Effects: milk pouring, a ceramic tap as the jug lands.

**Negative.** morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts

**Notes.** Good first test for any model: one subject, one light, one liquid.

## Prompts

### Kling 3.0

```text
A barista in a grey apron, sleeves rolled, steady hands holding a steel milk jug in an empty cafe at dawn, a wooden counter lit by low sun through the front window. Kodak 250D look, warm highlights, muted shadows, fine grain. 100mm macro, f/4, shallow depth of field. Low golden sun as key from camera-right, soft bounce fill, steam backlit. 0-2s: The milk jug tilts and a thin white stream hits the brown crema. Camera: locked-off, top-down on the cup. 2-4s: The stream wobbles side to side and a white heart forms on the surface. Camera: slow push-in on the cup. 4-6s: The jug lifts and draws a thin line through the heart. Camera: continue the push-in. 6-8s: The barista sets the jug down; steam rises off the cup. Camera: hold. Motion: milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap. Audio. Ambience: quiet cafe, espresso machine idling. Sound effects: milk pouring, a ceramic tap as the jug lands.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A barista in a grey apron, sleeves rolled, steady hands holding a steel milk jug in an empty cafe at dawn, a wooden counter lit by low sun through the front window. Kodak 250D look, warm highlights, muted shadows, fine grain. 100mm macro, f/4, shallow depth of field. Low golden sun as key from camera-right, soft bounce fill, steam backlit. One continuous take over 8 seconds. The milk jug tilts and a thin white stream hits the brown crema. Camera: locked-off, top-down on the cup. Then the stream wobbles side to side and a white heart forms on the surface. Camera: slow push-in on the cup. Then the jug lifts and draws a thin line through the heart. Camera: continue the push-in. Then the barista sets the jug down; steam rises off the cup. Camera: hold. Motion: milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap. Audio. Ambience: quiet cafe, espresso machine idling. Sound effects: milk pouring, a ceramic tap as the jug lands.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- [Run in UniqAI](https://uniqai.app/models/veo?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A barista in a grey apron, sleeves rolled, steady hands holding a steel milk jug in an empty cafe at dawn, a wooden counter lit by low sun through the front window. 100mm macro, f/4, shallow depth of field. Low golden sun as key from camera-right, soft bounce fill, steam backlit. The milk jug tilts and a thin white stream hits the brown crema. Camera: locked-off, top-down on the cup. Then the stream wobbles side to side and a white heart forms on the surface. Camera: slow push-in on the cup. Then the jug lifts and draws a thin line through the heart. Camera: continue the push-in. Then the barista sets the jug down; steam rises off the cup. Camera: hold. Motion: milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap. Audio. Ambience: quiet cafe, espresso machine idling. Sound effects: milk pouring, a ceramic tap as the jug lands.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 908 characters, limit is 800
- Check: Wan 2.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- [Run in UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A barista in a grey apron, sleeves rolled, steady hands holding a steel milk jug in an empty cafe at dawn, a wooden counter lit by low sun through the front window. Kodak 250D look, warm highlights, muted shadows, fine grain. 100mm macro, f/4, shallow depth of field. Low golden sun as key from camera-right, soft bounce fill, steam backlit. Shot 1 (0-2s): The milk jug tilts and a thin white stream hits the brown crema. Camera: locked-off, top-down on the cup. Shot 2 (2-4s): The stream wobbles side to side and a white heart forms on the surface. Camera: slow push-in on the cup. Shot 3 (4-6s): The jug lifts and draws a thin line through the heart. Camera: continue the push-in. Shot 4 (6-8s): The barista sets the jug down; steam rises off the cup. Camera: hold. Motion: milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap. Audio. Ambience: quiet cafe, espresso machine idling. Sound effects: milk pouring, a ceramic tap as the jug lands. Avoid: morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Locked-off, top-down on the cup: A barista in a grey apron, sleeves rolled, steady hands holding a steel milk jug in an empty cafe at dawn, a wooden counter lit by low sun through the front window. The milk jug tilts and a thin white stream hits the brown crema. Camera: locked-off, top-down on the cup. Then the stream wobbles side to side and a white heart forms on the surface. Camera: slow push-in on the cup. Then the jug lifts and draws a thin line through the heart. Camera: continue the push-in. Then the barista sets the jug down; steam rises off the cup. Camera: hold. Motion: milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap. Kodak 250D look, warm highlights, muted shadows, fine grain.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A barista in a grey apron, sleeves rolled, steady hands holding a steel milk jug in an empty cafe at dawn, a wooden counter lit by low sun through the front window. Kodak 250D look, warm highlights, muted shadows, fine grain. 100mm macro, f/4, shallow depth of field. Low golden sun as key from camera-right, soft bounce fill, steam backlit. 0-2s: The milk jug tilts and a thin white stream hits the brown crema. Camera: locked-off, top-down on the cup. 2-4s: The stream wobbles side to side and a white heart forms on the surface. Camera: slow push-in on the cup. 4-6s: The jug lifts and draws a thin line through the heart. Camera: continue the push-in. 6-8s: The barista sets the jug down; steam rises off the cup. Camera: hold. Motion: milk pours in a steady column and ripples on contact; steam rises and curls; the jug has weight and lands with a small tap. Audio. Ambience: quiet cafe, espresso machine idling. Sound effects: milk pouring, a ceramic tap as the jug lands.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
