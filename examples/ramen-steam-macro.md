# Ramen steam macro

> macro shot of a bowl of ramen as chopsticks lift the noodles

| | |
|---|---|
| Mode | text-to-video |
| Duration | 5 s |
| Aspect | 9:16 |
| Lens | 100mm macro, f/4, shallow depth of field |
| Light | warm pendant lamp as key from above, steam backlit |
| Style | warm food-film look, rich colour |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | steam rises off the broth, chopsticks dip in | locked-off, 45 degrees above the bowl |
| 2-4s | the chopsticks lift a tangle of noodles, broth dripping | slow tilt up following the noodles |
| 4-5s | the noodles hang and drip; steam curls through the light | hold |

**Motion physics.** steam rises and curls; broth drips at real speed; noodles sag with weight

**Sound.** Ambience: small shop, broth simmering. Effects: chopsticks on ceramic, a drip.

**Negative.** morphing, warped hands, flicker, text, watermark, jump cuts

**Notes.** Vertical; kept under Wan's 800-character limit.

## Prompts

### Kling 3.0

```text
A bowl of tonkotsu ramen with a soft egg, chopsticks lifting noodles in a dark wooden counter in a small ramen shop. Warm food-film look, rich colour. 100mm macro, f/4, shallow depth of field. Warm pendant lamp as key from above, steam backlit. 0-2s: Steam rises off the broth, chopsticks dip in. Camera: locked-off, 45 degrees above the bowl. 2-4s: The chopsticks lift a tangle of noodles, broth dripping. Camera: slow tilt up following the noodles. 4-5s: The noodles hang and drip; steam curls through the light. Camera: hold. Motion: steam rises and curls; broth drips at real speed; noodles sag with weight. Audio. Ambience: small shop, broth simmering. Sound effects: chopsticks on ceramic, a drip.
```

Negative prompt field:

```text
morphing, warped hands, flicker, text, watermark, jump cuts
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A bowl of tonkotsu ramen with a soft egg, chopsticks lifting noodles in a dark wooden counter in a small ramen shop. Warm food-film look, rich colour. 100mm macro, f/4, shallow depth of field. Warm pendant lamp as key from above, steam backlit. One continuous take over 5 seconds. Steam rises off the broth, chopsticks dip in. Camera: locked-off, 45 degrees above the bowl. Then the chopsticks lift a tangle of noodles, broth dripping. Camera: slow tilt up following the noodles. Then the noodles hang and drip; steam curls through the light. Camera: hold. Motion: steam rises and curls; broth drips at real speed; noodles sag with weight. Audio. Ambience: small shop, broth simmering. Sound effects: chopsticks on ceramic, a drip.
```

Negative prompt field:

```text
morphing, warped hands, flicker, text, watermark, jump cuts
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 5s is not an available length (4/6/8 s); nearest is 4s, re-time the beats
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A bowl of tonkotsu ramen with a soft egg, chopsticks lifting noodles in a dark wooden counter in a small ramen shop. 100mm macro, f/4, shallow depth of field. Warm pendant lamp as key from above, steam backlit. Steam rises off the broth, chopsticks dip in. Camera: locked-off, 45 degrees above the bowl. Then the chopsticks lift a tangle of noodles, broth dripping. Camera: slow tilt up following the noodles. Then the noodles hang and drip; steam curls through the light. Camera: hold. Motion: steam rises and curls; broth drips at real speed; noodles sag with weight. Audio. Ambience: small shop, broth simmering. Sound effects: chopsticks on ceramic, a drip.
```

Negative prompt field:

```text
morphing, warped hands, flicker, text, watermark, jump cuts
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A bowl of tonkotsu ramen with a soft egg, chopsticks lifting noodles in a dark wooden counter in a small ramen shop. Warm food-film look, rich colour. 100mm macro, f/4, shallow depth of field. Warm pendant lamp as key from above, steam backlit. Shot 1 (0-2s): Steam rises off the broth, chopsticks dip in. Camera: locked-off, 45 degrees above the bowl. Shot 2 (2-4s): The chopsticks lift a tangle of noodles, broth dripping. Camera: slow tilt up following the noodles. Shot 3 (4-5s): The noodles hang and drip; steam curls through the light. Camera: hold. Motion: steam rises and curls; broth drips at real speed; noodles sag with weight. Audio. Ambience: small shop, broth simmering. Sound effects: chopsticks on ceramic, a drip. Avoid: morphing, warped hands, flicker, text, watermark, jump cuts.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Locked-off, 45 degrees above the bowl: A bowl of tonkotsu ramen with a soft egg, chopsticks lifting noodles in a dark wooden counter in a small ramen shop. Steam rises off the broth, chopsticks dip in. Camera: locked-off, 45 degrees above the bowl. Then the chopsticks lift a tangle of noodles, broth dripping. Camera: slow tilt up following the noodles. Then the noodles hang and drip; steam curls through the light. Camera: hold. Motion: steam rises and curls; broth drips at real speed; noodles sag with weight. Warm food-film look, rich colour.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A bowl of tonkotsu ramen with a soft egg, chopsticks lifting noodles in a dark wooden counter in a small ramen shop. Warm food-film look, rich colour. 100mm macro, f/4, shallow depth of field. Warm pendant lamp as key from above, steam backlit. 0-2s: Steam rises off the broth, chopsticks dip in. Camera: locked-off, 45 degrees above the bowl. 2-4s: The chopsticks lift a tangle of noodles, broth dripping. Camera: slow tilt up following the noodles. 4-5s: The noodles hang and drip; steam curls through the light. Camera: hold. Motion: steam rises and curls; broth drips at real speed; noodles sag with weight. Audio. Ambience: small shop, broth simmering. Sound effects: chopsticks on ceramic, a drip.
```

Negative prompt field:

```text
morphing, warped hands, flicker, text, watermark, jump cuts
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
