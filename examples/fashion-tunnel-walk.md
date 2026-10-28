# Fashion walk through the tunnel

> a model in a flowing red dress walks towards the camera through a concrete tunnel

| | |
|---|---|
| Mode | image-to-video |
| Duration | 10 s |
| Aspect | 9:16 |
| Lens | 35mm, f/2.8 |
| Light | cold fluorescent strip lights as key from above, warm light at the far end of the tunnel as backlight |
| Style | editorial fashion film, high contrast, muted concrete tones against saturated red |

**Start frame.** the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | she stands at the far end of the tunnel in silhouette against the warm light, then starts walking | locked-off, full body, low angle |
| 2-4s | she walks towards the camera with a steady stride, the dress trailing | slow pull-back ahead of her, matching her pace |
| 4-6s | the strip lights pass overhead and catch the silk; she looks straight into the lens | continue the pull-back |
| 6-8s | she stops, turns her shoulder and the dress swings around her | hold at full body |
| 8-10s | the dress settles; she holds the pose | slow push-in to waist-up |

**Motion physics.** silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later

**Sound.** Ambience: tunnel echo, distant traffic. Effects: boot heels on wet concrete, fabric rustle.

**Negative.** morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin

**Notes.** Vertical; 10 s uses five beats with one camera change at 2 s and one at 8 s.

## Prompts

### Kling 3.0

```text
A tall model in a long red silk dress and black boots, hair loose in a concrete pedestrian tunnel with strip lights along the ceiling, puddles on the floor. Editorial fashion film, high contrast, muted concrete tones against saturated red. 35mm, f/2.8. Cold fluorescent strip lights as key from above, warm light at the far end of the tunnel as backlight. Start frame: the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image. 0-2s: She stands at the far end of the tunnel in silhouette against the warm light, then starts walking. Camera: locked-off, full body, low angle. 2-4s: She walks towards the camera with a steady stride, the dress trailing. Camera: slow pull-back ahead of her, matching her pace. 4-6s: The strip lights pass overhead and catch the silk; she looks straight into the lens. Camera: continue the pull-back. 6-8s: She stops, turns her shoulder and the dress swings around her. Camera: hold at full body. 8-10s: The dress settles; she holds the pose. Camera: slow push-in to waist-up. Motion: silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later. Audio. Ambience: tunnel echo, distant traffic. Sound effects: boot heels on wet concrete, fabric rustle.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A tall model in a long red silk dress and black boots, hair loose in a concrete pedestrian tunnel with strip lights along the ceiling, puddles on the floor. Editorial fashion film, high contrast, muted concrete tones against saturated red. 35mm, f/2.8. Cold fluorescent strip lights as key from above, warm light at the far end of the tunnel as backlight. Start frame: the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image. One continuous take over 10 seconds. She stands at the far end of the tunnel in silhouette against the warm light, then starts walking. Camera: locked-off, full body, low angle. Then she walks towards the camera with a steady stride, the dress trailing. Camera: slow pull-back ahead of her, matching her pace. Then the strip lights pass overhead and catch the silk; she looks straight into the lens. Camera: continue the pull-back. Then she stops, turns her shoulder and the dress swings around her. Camera: hold at full body. Then the dress settles; she holds the pose. Camera: slow push-in to waist-up. Motion: silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later. Audio. Ambience: tunnel echo, distant traffic. Sound effects: boot heels on wet concrete, fabric rustle.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A tall model in a long red silk dress and black boots, hair loose in a concrete pedestrian tunnel with strip lights along the ceiling, puddles on the floor. 35mm, f/2.8. Cold fluorescent strip lights as key from above, warm light at the far end of the tunnel as backlight. Start frame: the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image. She stands at the far end of the tunnel in silhouette against the warm light, then starts walking. Camera: locked-off, full body, low angle. Then she walks towards the camera with a steady stride, the dress trailing. Camera: slow pull-back ahead of her, matching her pace. Then the strip lights pass overhead and catch the silk; she looks straight into the lens. Camera: continue the pull-back. Then she stops, turns her shoulder and the dress swings around her. Camera: hold at full body. Then the dress settles; she holds the pose. Camera: slow push-in to waist-up. Motion: silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later. Audio. Ambience: tunnel echo, distant traffic. Sound effects: boot heels on wet concrete, fabric rustle.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 1304 characters, limit is 800
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A tall model in a long red silk dress and black boots, hair loose in a concrete pedestrian tunnel with strip lights along the ceiling, puddles on the floor. Editorial fashion film, high contrast, muted concrete tones against saturated red. 35mm, f/2.8. Cold fluorescent strip lights as key from above, warm light at the far end of the tunnel as backlight. Start frame: the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image. Shot 1 (0-2s): She stands at the far end of the tunnel in silhouette against the warm light, then starts walking. Camera: locked-off, full body, low angle. Shot 2 (2-4s): She walks towards the camera with a steady stride, the dress trailing. Camera: slow pull-back ahead of her, matching her pace. Shot 3 (4-6s): The strip lights pass overhead and catch the silk; she looks straight into the lens. Camera: continue the pull-back. Shot 4 (6-8s): She stops, turns her shoulder and the dress swings around her. Camera: hold at full body. Shot 5 (8-10s): The dress settles; she holds the pose. Camera: slow push-in to waist-up. Motion: silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later. Audio. Ambience: tunnel echo, distant traffic. Sound effects: boot heels on wet concrete, fabric rustle. Avoid: morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.
- Check: Seedance 2.0: prompt is 1544 characters; over ~1500 the model starts ignoring detail

### Runway Gen-4 / 4.5

```text
Locked-off, full body, low angle: A tall model in a long red silk dress and black boots, hair loose in a concrete pedestrian tunnel with strip lights along the ceiling, puddles on the floor. She stands at the far end of the tunnel in silhouette against the warm light, then starts walking. Camera: locked-off, full body, low angle. Then she walks towards the camera with a steady stride, the dress trailing. Camera: slow pull-back ahead of her, matching her pace. Then the strip lights pass overhead and catch the silk; she looks straight into the lens. Camera: continue the pull-back. Then she stops, turns her shoulder and the dress swings around her. Camera: hold at full body. Then the dress settles; she holds the pose. Camera: slow push-in to waist-up. Motion: silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later. Editorial fashion film, high contrast, muted concrete tones against saturated red.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Start frame: the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image
- **Does not fit:** Runway Gen-4 / 4.5: prompt is 1022 characters, limit is 1000
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A tall model in a long red silk dress and black boots, hair loose in a concrete pedestrian tunnel with strip lights along the ceiling, puddles on the floor. Editorial fashion film, high contrast, muted concrete tones against saturated red. 35mm, f/2.8. Cold fluorescent strip lights as key from above, warm light at the far end of the tunnel as backlight. Start frame: the model standing at the far end of the tunnel, full body, silhouette with the red dress catching light; the dress, boots and tunnel geometry stay as in the image. 0-2s: She stands at the far end of the tunnel in silhouette against the warm light, then starts walking. Camera: locked-off, full body, low angle. 2-4s: She walks towards the camera with a steady stride, the dress trailing. Camera: slow pull-back ahead of her, matching her pace. 4-6s: The strip lights pass overhead and catch the silk; she looks straight into the lens. Camera: continue the pull-back. 6-8s: She stops, turns her shoulder and the dress swings around her. Camera: hold at full body. 8-10s: The dress settles; she holds the pose. Camera: slow push-in to waist-up. Motion: silk floats and ripples behind her, slow to settle; boots plant firmly on each step with small splashes in the puddles; hair moves with the head and settles a moment later. Audio. Ambience: tunnel echo, distant traffic. Sound effects: boot heels on wet concrete, fabric rustle.
```

Negative prompt field:

```text
morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, plastic skin
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
