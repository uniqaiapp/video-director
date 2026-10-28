# Neon rain street

> a woman waits under a shop awning on a rainy neon street at night and says one line

| | |
|---|---|
| Mode | text-to-video |
| Duration | 8 s |
| Aspect | 9:16 |
| Lens | 35mm anamorphic, f/2, oval bokeh |
| Light | magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car |
| Style | anamorphic, teal and magenta grade, Kodak 500T grain in the shadows |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | she stands under the awning watching the rain, neon reflections sliding across her coat | slow push-in at eye level, framed waist-up |
| 2-4s | a car passes, its headlights sweep across her face; she turns to the camera | continue the push-in |
| 4-6s | she says the line, half smiling | hold on a medium close-up |
| 6-8s | she steps out into the rain and opens the umbrella | slow tilt up following the umbrella |

**Motion physics.** rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles

**Sound.** Ambience: steady rain, tyres on wet asphalt, a distant siren. Effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."

**Negative.** morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter

**Notes.** Vertical framing for Reels. Veo adds 'subtitles, captions' to the negative field because there is dialogue.

## Prompts

### Kling 3.0

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. 0-2s: She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. 2-4s: A car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. 4-6s: She says the line, half smiling. Camera: hold on a medium close-up. 6-8s: She steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. One continuous take over 8 seconds. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter, subtitles, captions
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo tends to burn in subtitles when there is dialogue: 'subtitles, captions' are added to the negative field
- [Run in UniqAI](https://uniqai.app/models/veo?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 1048 characters, limit is 800
- Check: Wan 2.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- [Run in UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. Shot 1 (0-2s): She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Shot 2 (2-4s): A car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Shot 3 (4-6s): She says the line, half smiling. Camera: hold on a medium close-up. Shot 4 (6-8s): She steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again." Avoid: morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Slow push-in at eye level, framed waist-up: A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Check: Runway Gen-4 / 4.5: 8s is not an available length (5/10 s); nearest is 10s, re-time the beats
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. 0-2s: She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. 2-4s: A car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. 4-6s: She says the line, half smiling. Camera: hold on a medium close-up. 6-8s: She steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
