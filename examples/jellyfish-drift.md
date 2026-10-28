# Jellyfish drift

> a jellyfish drifts upward through dark water towards the light

| | |
|---|---|
| Mode | text-to-video |
| Duration | 10 s |
| Aspect | 16:9 |
| Lens | 16mm wide, f/4 |
| Light | caustic light patterns from the surface, blue falloff into darkness below, the jellyfish lit from above |
| Style | documentary underwater, deep blue, soft highlights |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | the jellyfish pulses once in the dark, tentacles trailing | slow drift upward from below, slight roll |
| 2-4s | it pulses again and rises; tiny particles drift past | continue the drift, orbiting slightly to the left |
| 4-6s | caustic light from the surface starts to ripple across its bell | continue |
| 6-8s | a small school of silver fish passes in the background | rack focus briefly to the fish, then back |
| 8-10s | the jellyfish reaches the bright water and glows; hold | hold, slow drift |

**Motion physics.** everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column

**Sound.** Ambience: muffled underwater hum, bubbles.

**Negative.** morphing, flicker, text, watermark, jump cuts, duplicate jellyfish, cartoon

## Prompts

### Kling 3.0

```text
A translucent moon jellyfish with faint pink organs, tentacles trailing in open ocean at twenty metres depth, dark below, bright surface above. Documentary underwater, deep blue, soft highlights. 16mm wide, f/4. Caustic light patterns from the surface, blue falloff into darkness below, the jellyfish lit from above. 0-2s: The jellyfish pulses once in the dark, tentacles trailing. Camera: slow drift upward from below, slight roll. 2-4s: It pulses again and rises; tiny particles drift past. Camera: continue the drift, orbiting slightly to the left. 4-6s: Caustic light from the surface starts to ripple across its bell. Camera: continue. 6-8s: A small school of silver fish passes in the background. Camera: rack focus briefly to the fish, then back. 8-10s: The jellyfish reaches the bright water and glows; hold. Camera: hold, slow drift. Motion: everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column. Audio. Ambience: muffled underwater hum, bubbles.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, duplicate jellyfish, cartoon
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A translucent moon jellyfish with faint pink organs, tentacles trailing in open ocean at twenty metres depth, dark below, bright surface above. Documentary underwater, deep blue, soft highlights. 16mm wide, f/4. Caustic light patterns from the surface, blue falloff into darkness below, the jellyfish lit from above. One continuous take over 10 seconds. The jellyfish pulses once in the dark, tentacles trailing. Camera: slow drift upward from below, slight roll. Then it pulses again and rises; tiny particles drift past. Camera: continue the drift, orbiting slightly to the left. Then caustic light from the surface starts to ripple across its bell. Camera: continue. Then a small school of silver fish passes in the background. Camera: rack focus briefly to the fish, then back. Then the jellyfish reaches the bright water and glows; hold. Camera: hold, slow drift. Motion: everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column. Audio. Ambience: muffled underwater hum, bubbles.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, duplicate jellyfish, cartoon
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A translucent moon jellyfish with faint pink organs, tentacles trailing in open ocean at twenty metres depth, dark below, bright surface above. 16mm wide, f/4. Caustic light patterns from the surface, blue falloff into darkness below, the jellyfish lit from above. The jellyfish pulses once in the dark, tentacles trailing. Camera: slow drift upward from below, slight roll. Then it pulses again and rises; tiny particles drift past. Camera: continue the drift, orbiting slightly to the left. Then caustic light from the surface starts to ripple across its bell. Camera: continue. Then a small school of silver fish passes in the background. Camera: rack focus briefly to the fish, then back. Then the jellyfish reaches the bright water and glows; hold. Camera: hold, slow drift. Motion: everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column. Audio. Ambience: muffled underwater hum, bubbles.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, duplicate jellyfish, cartoon
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 984 characters, limit is 800
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A translucent moon jellyfish with faint pink organs, tentacles trailing in open ocean at twenty metres depth, dark below, bright surface above. Documentary underwater, deep blue, soft highlights. 16mm wide, f/4. Caustic light patterns from the surface, blue falloff into darkness below, the jellyfish lit from above. Shot 1 (0-2s): The jellyfish pulses once in the dark, tentacles trailing. Camera: slow drift upward from below, slight roll. Shot 2 (2-4s): It pulses again and rises; tiny particles drift past. Camera: continue the drift, orbiting slightly to the left. Shot 3 (4-6s): Caustic light from the surface starts to ripple across its bell. Camera: continue. Shot 4 (6-8s): A small school of silver fish passes in the background. Camera: rack focus briefly to the fish, then back. Shot 5 (8-10s): The jellyfish reaches the bright water and glows; hold. Camera: hold, slow drift. Motion: everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column. Audio. Ambience: muffled underwater hum, bubbles. Avoid: morphing, flicker, text, watermark, jump cuts, duplicate jellyfish, cartoon.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Slow drift upward from below, slight roll: A translucent moon jellyfish with faint pink organs, tentacles trailing in open ocean at twenty metres depth, dark below, bright surface above. The jellyfish pulses once in the dark, tentacles trailing. Camera: slow drift upward from below, slight roll. Then it pulses again and rises; tiny particles drift past. Camera: continue the drift, orbiting slightly to the left. Then caustic light from the surface starts to ripple across its bell. Camera: continue. Then a small school of silver fish passes in the background. Camera: rack focus briefly to the fish, then back. Then the jellyfish reaches the bright water and glows; hold. Camera: hold, slow drift. Motion: everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column. Documentary underwater, deep blue, soft highlights.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A translucent moon jellyfish with faint pink organs, tentacles trailing in open ocean at twenty metres depth, dark below, bright surface above. Documentary underwater, deep blue, soft highlights. 16mm wide, f/4. Caustic light patterns from the surface, blue falloff into darkness below, the jellyfish lit from above. 0-2s: The jellyfish pulses once in the dark, tentacles trailing. Camera: slow drift upward from below, slight roll. 2-4s: It pulses again and rises; tiny particles drift past. Camera: continue the drift, orbiting slightly to the left. 4-6s: Caustic light from the surface starts to ripple across its bell. Camera: continue. 6-8s: A small school of silver fish passes in the background. Camera: rack focus briefly to the fish, then back. 8-10s: The jellyfish reaches the bright water and glows; hold. Camera: hold, slow drift. Motion: everything moves slowly with drag; the bell contracts then relaxes with a lag in the tentacles; bubbles rise; particles drift in the water column. Audio. Ambience: muffled underwater hum, bubbles.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, duplicate jellyfish, cartoon
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
