# Coastline drone at dawn

> drone flight along a rocky coastline at dawn

| | |
|---|---|
| Mode | text-to-video |
| Duration | 10 s |
| Aspect | 16:9 |
| Lens | 24mm wide, deep focus |
| Light | low golden sun from the left, long shadows on the rocks |
| Style | clean digital cinema, natural colour, slight warm grade |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | aerial view over the surf, the coast ahead | aerial, slow forward drift |
| 2-4s | the lighthouse appears on the headland | continue forward, slight tilt down |
| 4-6s | waves break white against the rocks below | continue forward |
| 6-8s | the drone passes the lighthouse on its left | slow pan right to keep it in frame |
| 8-10s | open sea beyond, the sun clears the mist | hold, drifting forward |

**Motion physics.** waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon

**Sound.** Ambience: wind, surf below.

**Negative.** morphing, flicker, text, watermark, jump cuts, frame jitter

**Notes.** Written for Wan's 800-character prompt field: short beats, no style paragraph.

## Prompts

### Kling 3.0

```text
A rocky coastline with white surf and a single lighthouse in the Atlantic coast at dawn, low mist over the water. Clean digital cinema, natural colour, slight warm grade. 24mm wide, deep focus. Low golden sun from the left, long shadows on the rocks. 0-2s: Aerial view over the surf, the coast ahead. Camera: aerial, slow forward drift. 2-4s: The lighthouse appears on the headland. Camera: continue forward, slight tilt down. 4-6s: Waves break white against the rocks below. Camera: continue forward. 6-8s: The drone passes the lighthouse on its left. Camera: slow pan right to keep it in frame. 8-10s: Open sea beyond, the sun clears the mist. Camera: hold, drifting forward. Motion: waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon. Audio. Ambience: wind, surf below.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, frame jitter
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A rocky coastline with white surf and a single lighthouse in the Atlantic coast at dawn, low mist over the water. Clean digital cinema, natural colour, slight warm grade. 24mm wide, deep focus. Low golden sun from the left, long shadows on the rocks. One continuous take over 10 seconds. Aerial view over the surf, the coast ahead. Camera: aerial, slow forward drift. Then the lighthouse appears on the headland. Camera: continue forward, slight tilt down. Then waves break white against the rocks below. Camera: continue forward. Then the drone passes the lighthouse on its left. Camera: slow pan right to keep it in frame. Then open sea beyond, the sun clears the mist. Camera: hold, drifting forward. Motion: waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon. Audio. Ambience: wind, surf below.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, frame jitter
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A rocky coastline with white surf and a single lighthouse in the Atlantic coast at dawn, low mist over the water. 24mm wide, deep focus. Low golden sun from the left, long shadows on the rocks. Aerial view over the surf, the coast ahead. Camera: aerial, slow forward drift. Then the lighthouse appears on the headland. Camera: continue forward, slight tilt down. Then waves break white against the rocks below. Camera: continue forward. Then the drone passes the lighthouse on its left. Camera: slow pan right to keep it in frame. Then open sea beyond, the sun clears the mist. Camera: hold, drifting forward. Motion: waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon. Audio. Ambience: wind, surf below.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, frame jitter
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A rocky coastline with white surf and a single lighthouse in the Atlantic coast at dawn, low mist over the water. Clean digital cinema, natural colour, slight warm grade. 24mm wide, deep focus. Low golden sun from the left, long shadows on the rocks. Shot 1 (0-2s): Aerial view over the surf, the coast ahead. Camera: aerial, slow forward drift. Shot 2 (2-4s): The lighthouse appears on the headland. Camera: continue forward, slight tilt down. Shot 3 (4-6s): Waves break white against the rocks below. Camera: continue forward. Shot 4 (6-8s): The drone passes the lighthouse on its left. Camera: slow pan right to keep it in frame. Shot 5 (8-10s): Open sea beyond, the sun clears the mist. Camera: hold, drifting forward. Motion: waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon. Audio. Ambience: wind, surf below. Avoid: morphing, flicker, text, watermark, jump cuts, frame jitter.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Aerial, slow forward drift: A rocky coastline with white surf and a single lighthouse in the Atlantic coast at dawn, low mist over the water. Aerial view over the surf, the coast ahead. Camera: aerial, slow forward drift. Then the lighthouse appears on the headland. Camera: continue forward, slight tilt down. Then waves break white against the rocks below. Camera: continue forward. Then the drone passes the lighthouse on its left. Camera: slow pan right to keep it in frame. Then open sea beyond, the sun clears the mist. Camera: hold, drifting forward. Motion: waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon. Clean digital cinema, natural colour, slight warm grade.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A rocky coastline with white surf and a single lighthouse in the Atlantic coast at dawn, low mist over the water. Clean digital cinema, natural colour, slight warm grade. 24mm wide, deep focus. Low golden sun from the left, long shadows on the rocks. 0-2s: Aerial view over the surf, the coast ahead. Camera: aerial, slow forward drift. 2-4s: The lighthouse appears on the headland. Camera: continue forward, slight tilt down. 4-6s: Waves break white against the rocks below. Camera: continue forward. 6-8s: The drone passes the lighthouse on its left. Camera: slow pan right to keep it in frame. 8-10s: Open sea beyond, the sun clears the mist. Camera: hold, drifting forward. Motion: waves roll and break at real speed; mist drifts slowly; parallax between rocks and horizon. Audio. Ambience: wind, surf below.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, frame jitter
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
