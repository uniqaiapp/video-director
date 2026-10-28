# Candle confession

> an old man at a candlelit table says one sentence to someone off-screen

| | |
|---|---|
| Mode | text-to-video |
| Duration | 8 s |
| Aspect | 16:9 |
| Lens | 85mm, f/2, shallow depth of field |
| Light | candlelight as the only source, warm flicker, Rembrandt triangle on the far cheek, rapid falloff into darkness |
| Style | period drama, Rembrandt lighting, warm low-key, fine grain |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | he stares at the candle, the flame reflected in his eyes, breathing slowly | locked-off medium close-up |
| 2-4s | he looks up at someone off-screen to the right | slow push-in |
| 4-7s | he says the line, slowly, and his hands tighten | continue the push-in to a close-up |
| 7-8s | he looks back down at the flame; it flickers | hold |

**Motion physics.** the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons

**Sound.** Ambience: quiet room, wind outside, a clock ticking. Effects: the candle flame guttering. Dialogue: The old man says, slowly, lip-synced: "I never told her it was me."

**Negative.** morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin

**Notes.** 'flicker' in the negative list refers to exposure flicker; the candle flicker is described in the light and physics fields, which models separate well.

## Prompts

### Kling 3.0

```text
An old man with a white beard and a lined face, wearing a dark wool coat, hands folded on the table in a farmhouse kitchen at night, a single candle on a wooden table, the rest of the room in shadow. Period drama, Rembrandt lighting, warm low-key, fine grain. 85mm, f/2, shallow depth of field. Candlelight as the only source, warm flicker, Rembrandt triangle on the far cheek, rapid falloff into darkness. 0-2s: He stares at the candle, the flame reflected in his eyes, breathing slowly. Camera: locked-off medium close-up. 2-4s: He looks up at someone off-screen to the right. Camera: slow push-in. 4-7s: He says the line, slowly, and his hands tighten. Camera: continue the push-in to a close-up. 7-8s: He looks back down at the flame; it flickers. Camera: hold. Motion: the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons. Audio. Ambience: quiet room, wind outside, a clock ticking. Sound effects: the candle flame guttering. Dialogue: The old man says, slowly, lip-synced: "I never told her it was me."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
An old man with a white beard and a lined face, wearing a dark wool coat, hands folded on the table in a farmhouse kitchen at night, a single candle on a wooden table, the rest of the room in shadow. Period drama, Rembrandt lighting, warm low-key, fine grain. 85mm, f/2, shallow depth of field. Candlelight as the only source, warm flicker, Rembrandt triangle on the far cheek, rapid falloff into darkness. One continuous take over 8 seconds. He stares at the candle, the flame reflected in his eyes, breathing slowly. Camera: locked-off medium close-up. Then he looks up at someone off-screen to the right. Camera: slow push-in. Then he says the line, slowly, and his hands tighten. Camera: continue the push-in to a close-up. Then he looks back down at the flame; it flickers. Camera: hold. Motion: the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons. Audio. Ambience: quiet room, wind outside, a clock ticking. Sound effects: the candle flame guttering. Dialogue: The old man says, slowly, lip-synced: "I never told her it was me."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin, subtitles, captions
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo tends to burn in subtitles when there is dialogue: 'subtitles, captions' are added to the negative field
- [Run in UniqAI](https://uniqai.app/models/veo?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
An old man with a white beard and a lined face, wearing a dark wool coat, hands folded on the table in a farmhouse kitchen at night, a single candle on a wooden table, the rest of the room in shadow. 85mm, f/2, shallow depth of field. Candlelight as the only source, warm flicker, Rembrandt triangle on the far cheek, rapid falloff into darkness. He stares at the candle, the flame reflected in his eyes, breathing slowly. Camera: locked-off medium close-up. Then he looks up at someone off-screen to the right. Camera: slow push-in. Then he says the line, slowly, and his hands tighten. Camera: continue the push-in to a close-up. Then he looks back down at the flame; it flickers. Camera: hold. Motion: the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons. Audio. Ambience: quiet room, wind outside, a clock ticking. Sound effects: the candle flame guttering. Dialogue: The old man says, slowly, lip-synced: "I never told her it was me."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 1034 characters, limit is 800
- Check: Wan 2.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- [Run in UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
An old man with a white beard and a lined face, wearing a dark wool coat, hands folded on the table in a farmhouse kitchen at night, a single candle on a wooden table, the rest of the room in shadow. Period drama, Rembrandt lighting, warm low-key, fine grain. 85mm, f/2, shallow depth of field. Candlelight as the only source, warm flicker, Rembrandt triangle on the far cheek, rapid falloff into darkness. Shot 1 (0-2s): He stares at the candle, the flame reflected in his eyes, breathing slowly. Camera: locked-off medium close-up. Shot 2 (2-4s): He looks up at someone off-screen to the right. Camera: slow push-in. Shot 3 (4-7s): He says the line, slowly, and his hands tighten. Camera: continue the push-in to a close-up. Shot 4 (7-8s): He looks back down at the flame; it flickers. Camera: hold. Motion: the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons. Audio. Ambience: quiet room, wind outside, a clock ticking. Sound effects: the candle flame guttering. Dialogue: The old man says, slowly, lip-synced: "I never told her it was me." Avoid: morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Locked-off medium close-up: An old man with a white beard and a lined face, wearing a dark wool coat, hands folded on the table in a farmhouse kitchen at night, a single candle on a wooden table, the rest of the room in shadow. He stares at the candle, the flame reflected in his eyes, breathing slowly. Camera: locked-off medium close-up. Then he looks up at someone off-screen to the right. Camera: slow push-in. Then he says the line, slowly, and his hands tighten. Camera: continue the push-in to a close-up. Then he looks back down at the flame; it flickers. Camera: hold. Motion: the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons. Period drama, Rembrandt lighting, warm low-key, fine grain.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
An old man with a white beard and a lined face, wearing a dark wool coat, hands folded on the table in a farmhouse kitchen at night, a single candle on a wooden table, the rest of the room in shadow. Period drama, Rembrandt lighting, warm low-key, fine grain. 85mm, f/2, shallow depth of field. Candlelight as the only source, warm flicker, Rembrandt triangle on the far cheek, rapid falloff into darkness. 0-2s: He stares at the candle, the flame reflected in his eyes, breathing slowly. Camera: locked-off medium close-up. 2-4s: He looks up at someone off-screen to the right. Camera: slow push-in. 4-7s: He says the line, slowly, and his hands tighten. Camera: continue the push-in to a close-up. 7-8s: He looks back down at the flame; it flickers. Camera: hold. Motion: the flame flickers and the light on his face flickers with it; natural micro-movements, breathing, a slow blink; hands tighten with visible tendons. Audio. Ambience: quiet room, wind outside, a clock ticking. Sound effects: the candle flame guttering. Dialogue: The old man says, slowly, lip-synced: "I never told her it was me."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
