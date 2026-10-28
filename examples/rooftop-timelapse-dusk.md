# Rooftop timelapse at dusk

> timelapse from a rooftop as the city goes from dusk to night

| | |
|---|---|
| Mode | text-to-video |
| Duration | 12 s |
| Aspect | 16:9 |
| Lens | 24mm wide, deep focus |
| Light | blue hour sky as key fading to night; building windows and street lights switching on |
| Style | clean digital cinema, blue hour palette shifting to warm sodium and LED |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-3s | timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades | locked-off wide, parapet in the lower third |
| 3-6s | windows light up across the skyline one block at a time | very slow push-in |
| 6-9s | traffic on the bridge becomes streaks of red and white | continue the push-in |
| 9-12s | full night; the river reflects the lights; a plane crosses the sky | hold |

**Motion physics.** timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still

**Sound.** Ambience: distant city hum, wind on the rooftop.

**Negative.** morphing, flicker, text, watermark, jump cuts, warped architecture, bent lines

**Notes.** 12 s needs a multi-shot or long-clip model; the check command flags the length on Veo, Wan and Runway.

## Prompts

### Kling 3.0

```text
A dense city skyline with a river, a bridge and traffic on the embankment in a rooftop terrace with a low parapet in the foreground, late evening. Clean digital cinema, blue hour palette shifting to warm sodium and LED. 24mm wide, deep focus. Blue hour sky as key fading to night; building windows and street lights switching on. 0-3s: Timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades. Camera: locked-off wide, parapet in the lower third. 3-6s: Windows light up across the skyline one block at a time. Camera: very slow push-in. 6-9s: Traffic on the bridge becomes streaks of red and white. Camera: continue the push-in. 9-12s: Full night; the river reflects the lights; a plane crosses the sky. Camera: hold. Motion: timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still. Audio. Ambience: distant city hum, wind on the rooftop.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, warped architecture, bent lines
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A dense city skyline with a river, a bridge and traffic on the embankment in a rooftop terrace with a low parapet in the foreground, late evening. Clean digital cinema, blue hour palette shifting to warm sodium and LED. 24mm wide, deep focus. Blue hour sky as key fading to night; building windows and street lights switching on. One continuous take over 12 seconds. Timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades. Camera: locked-off wide, parapet in the lower third. Then windows light up across the skyline one block at a time. Camera: very slow push-in. Then traffic on the bridge becomes streaks of red and white. Camera: continue the push-in. Then full night; the river reflects the lights; a plane crosses the sky. Camera: hold. Motion: timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still. Audio. Ambience: distant city hum, wind on the rooftop.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, warped architecture, bent lines
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 12s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A dense city skyline with a river, a bridge and traffic on the embankment in a rooftop terrace with a low parapet in the foreground, late evening. 24mm wide, deep focus. Blue hour sky as key fading to night; building windows and street lights switching on. Timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades. Camera: locked-off wide, parapet in the lower third. Then windows light up across the skyline one block at a time. Camera: very slow push-in. Then traffic on the bridge becomes streaks of red and white. Camera: continue the push-in. Then full night; the river reflects the lights; a plane crosses the sky. Camera: hold. Motion: timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still. Audio. Ambience: distant city hum, wind on the rooftop.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, warped architecture, bent lines
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 839 characters, limit is 800
- Check: Wan 2.5: 12s is not an available length (5/10 s); nearest is 10s, re-time the beats
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A dense city skyline with a river, a bridge and traffic on the embankment in a rooftop terrace with a low parapet in the foreground, late evening. Clean digital cinema, blue hour palette shifting to warm sodium and LED. 24mm wide, deep focus. Blue hour sky as key fading to night; building windows and street lights switching on. Shot 1 (0-3s): Timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades. Camera: locked-off wide, parapet in the lower third. Shot 2 (3-6s): Windows light up across the skyline one block at a time. Camera: very slow push-in. Shot 3 (6-9s): Traffic on the bridge becomes streaks of red and white. Camera: continue the push-in. Shot 4 (9-12s): Full night; the river reflects the lights; a plane crosses the sky. Camera: hold. Motion: timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still. Audio. Ambience: distant city hum, wind on the rooftop. Avoid: morphing, flicker, text, watermark, jump cuts, warped architecture, bent lines.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Locked-off wide, parapet in the lower third: A dense city skyline with a river, a bridge and traffic on the embankment in a rooftop terrace with a low parapet in the foreground, late evening. Timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades. Camera: locked-off wide, parapet in the lower third. Then windows light up across the skyline one block at a time. Camera: very slow push-in. Then traffic on the bridge becomes streaks of red and white. Camera: continue the push-in. Then full night; the river reflects the lights; a plane crosses the sky. Camera: hold. Motion: timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still. Clean digital cinema, blue hour palette shifting to warm sodium and LED.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5: 12s is not an available length (5/10 s); nearest is 10s, re-time the beats
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A dense city skyline with a river, a bridge and traffic on the embankment in a rooftop terrace with a low parapet in the foreground, late evening. Clean digital cinema, blue hour palette shifting to warm sodium and LED. 24mm wide, deep focus. Blue hour sky as key fading to night; building windows and street lights switching on. 0-3s: Timelapse: clouds streak across a deep blue sky, the last orange on the horizon fades. Camera: locked-off wide, parapet in the lower third. 3-6s: Windows light up across the skyline one block at a time. Camera: very slow push-in. 6-9s: Traffic on the bridge becomes streaks of red and white. Camera: continue the push-in. 9-12s: Full night; the river reflects the lights; a plane crosses the sky. Camera: hold. Motion: timelapse motion: clouds streak, shadows sweep, traffic blurs into streaks; the buildings stay perfectly still. Audio. Ambience: distant city hum, wind on the rooftop.
```

Negative prompt field:

```text
morphing, flicker, text, watermark, jump cuts, warped architecture, bent lines
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
