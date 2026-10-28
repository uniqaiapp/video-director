# Cat at the rainy window

> a tabby cat watches rain on a window, then turns to the camera

| | |
|---|---|
| Mode | text-to-video |
| Duration | 5 s |
| Aspect | 16:9 |
| Lens | 85mm, f/2, shallow depth of field |
| Light | soft overcast daylight through the window as key, warm lamp fill from inside the room |
| Style | soft, warm, slightly desaturated, 35mm film grain |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | the cat sits on the sill watching raindrops run down the glass, tail curled | locked-off, medium shot from inside the room |
| 2-4s | its ear twitches; it turns its head slowly towards the camera | slow push-in |
| 4-5s | it blinks once and holds the look | hold on a close-up |

**Motion physics.** fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed

**Sound.** Ambience: rain tapping on glass, quiet room tone.

**Negative.** morphing, extra limbs, flicker, text, watermark, jump cuts, duplicate cat

## Prompts

### Kling 3.0

```text
A grey tabby cat with green eyes, fur slightly backlit in a window sill in a quiet apartment on a rainy afternoon, raindrops running down the glass. Soft, warm, slightly desaturated, 35mm film grain. 85mm, f/2, shallow depth of field. Soft overcast daylight through the window as key, warm lamp fill from inside the room. 0-2s: The cat sits on the sill watching raindrops run down the glass, tail curled. Camera: locked-off, medium shot from inside the room. 2-4s: Its ear twitches; it turns its head slowly towards the camera. Camera: slow push-in. 4-5s: It blinks once and holds the look. Camera: hold on a close-up. Motion: fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed. Audio. Ambience: rain tapping on glass, quiet room tone.
```

Negative prompt field:

```text
morphing, extra limbs, flicker, text, watermark, jump cuts, duplicate cat
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A grey tabby cat with green eyes, fur slightly backlit in a window sill in a quiet apartment on a rainy afternoon, raindrops running down the glass. Soft, warm, slightly desaturated, 35mm film grain. 85mm, f/2, shallow depth of field. Soft overcast daylight through the window as key, warm lamp fill from inside the room. One continuous take over 5 seconds. The cat sits on the sill watching raindrops run down the glass, tail curled. Camera: locked-off, medium shot from inside the room. Then its ear twitches; it turns its head slowly towards the camera. Camera: slow push-in. Then it blinks once and holds the look. Camera: hold on a close-up. Motion: fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed. Audio. Ambience: rain tapping on glass, quiet room tone.
```

Negative prompt field:

```text
morphing, extra limbs, flicker, text, watermark, jump cuts, duplicate cat
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 5s is not an available length (4/6/8 s); nearest is 4s, re-time the beats
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A grey tabby cat with green eyes, fur slightly backlit in a window sill in a quiet apartment on a rainy afternoon, raindrops running down the glass. 85mm, f/2, shallow depth of field. Soft overcast daylight through the window as key, warm lamp fill from inside the room. The cat sits on the sill watching raindrops run down the glass, tail curled. Camera: locked-off, medium shot from inside the room. Then its ear twitches; it turns its head slowly towards the camera. Camera: slow push-in. Then it blinks once and holds the look. Camera: hold on a close-up. Motion: fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed. Audio. Ambience: rain tapping on glass, quiet room tone.
```

Negative prompt field:

```text
morphing, extra limbs, flicker, text, watermark, jump cuts, duplicate cat
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A grey tabby cat with green eyes, fur slightly backlit in a window sill in a quiet apartment on a rainy afternoon, raindrops running down the glass. Soft, warm, slightly desaturated, 35mm film grain. 85mm, f/2, shallow depth of field. Soft overcast daylight through the window as key, warm lamp fill from inside the room. Shot 1 (0-2s): The cat sits on the sill watching raindrops run down the glass, tail curled. Camera: locked-off, medium shot from inside the room. Shot 2 (2-4s): Its ear twitches; it turns its head slowly towards the camera. Camera: slow push-in. Shot 3 (4-5s): It blinks once and holds the look. Camera: hold on a close-up. Motion: fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed. Audio. Ambience: rain tapping on glass, quiet room tone. Avoid: morphing, extra limbs, flicker, text, watermark, jump cuts, duplicate cat.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Locked-off, medium shot from inside the room: A grey tabby cat with green eyes, fur slightly backlit in a window sill in a quiet apartment on a rainy afternoon, raindrops running down the glass. The cat sits on the sill watching raindrops run down the glass, tail curled. Camera: locked-off, medium shot from inside the room. Then its ear twitches; it turns its head slowly towards the camera. Camera: slow push-in. Then it blinks once and holds the look. Camera: hold on a close-up. Motion: fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed. Soft, warm, slightly desaturated, 35mm film grain.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A grey tabby cat with green eyes, fur slightly backlit in a window sill in a quiet apartment on a rainy afternoon, raindrops running down the glass. Soft, warm, slightly desaturated, 35mm film grain. 85mm, f/2, shallow depth of field. Soft overcast daylight through the window as key, warm lamp fill from inside the room. 0-2s: The cat sits on the sill watching raindrops run down the glass, tail curled. Camera: locked-off, medium shot from inside the room. 2-4s: Its ear twitches; it turns its head slowly towards the camera. Camera: slow push-in. 4-5s: It blinks once and holds the look. Camera: hold on a close-up. Motion: fur ripples slightly as the head turns; the tail settles after a small flick; raindrops merge and run at real speed. Audio. Ambience: rain tapping on glass, quiet room tone.
```

Negative prompt field:

```text
morphing, extra limbs, flicker, text, watermark, jump cuts, duplicate cat
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
