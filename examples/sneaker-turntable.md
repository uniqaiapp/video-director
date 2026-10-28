# Sneaker turntable

> product shot of a white sneaker rotating on a turntable

| | |
|---|---|
| Mode | image-to-video |
| Duration | 5 s |
| Aspect | 1:1 |
| Lens | 50mm, f/5.6, product in sharp focus |
| Light | three-point studio lighting, large softbox key from the upper left, soft rim from behind, controlled specular highlights on the leather |
| Style | clean high-key commercial look, neutral colour |

**Start frame.** the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | the sneaker sits on a matte turntable, three-quarter view, and begins to rotate | slow 90-degree orbit, clockwise, at shoe height |
| 2-4s | the rotation reveals the side profile and the stitching | continue the orbit |
| 4-5s | the shoe comes to rest facing the camera | hold |

**Motion physics.** rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant

**Sound.** Effects: soft whoosh on the reveal.

**Negative.** morphing, warped shape, flicker, text, watermark, logo, extra shoes

**Notes.** Runway drops the negative list and the sound block; both are kept here for the edit.

## Prompts

### Kling 3.0

```text
A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. Clean high-key commercial look, neutral colour. 50mm, f/5.6, product in sharp focus. Three-point studio lighting, large softbox key from the upper left, soft rim from behind, controlled specular highlights on the leather. Start frame: the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image. 0-2s: The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. 2-4s: The rotation reveals the side profile and the stitching. Camera: continue the orbit. 4-5s: The shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Audio. Sound effects: soft whoosh on the reveal.
```

Negative prompt field:

```text
morphing, warped shape, flicker, text, watermark, logo, extra shoes
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. Clean high-key commercial look, neutral colour. 50mm, f/5.6, product in sharp focus. Three-point studio lighting, large softbox key from the upper left, soft rim from behind, controlled specular highlights on the leather. Start frame: the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image. One continuous take over 5 seconds. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Audio. Sound effects: soft whoosh on the reveal.
```

Negative prompt field:

```text
morphing, warped shape, flicker, text, watermark, logo, extra shoes
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 5s is not an available length (4/6/8 s); nearest is 4s, re-time the beats
- Check: Veo 3 / 3.1: aspect 1:1 not offered (16:9, 9:16)
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. 50mm, f/5.6, product in sharp focus. Three-point studio lighting, large softbox key from the upper left, soft rim from behind, controlled specular highlights on the leather. Start frame: the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Audio. Sound effects: soft whoosh on the reveal.
```

Negative prompt field:

```text
morphing, warped shape, flicker, text, watermark, logo, extra shoes
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 908 characters, limit is 800
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. Clean high-key commercial look, neutral colour. 50mm, f/5.6, product in sharp focus. Three-point studio lighting, large softbox key from the upper left, soft rim from behind, controlled specular highlights on the leather. Start frame: the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image. Shot 1 (0-2s): The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Shot 2 (2-4s): The rotation reveals the side profile and the stitching. Camera: continue the orbit. Shot 3 (4-5s): The shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Audio. Sound effects: soft whoosh on the reveal. Avoid: morphing, warped shape, flicker, text, watermark, logo, extra shoes.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- Start frame: the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead

### Generic (any model)

```text
A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. Clean high-key commercial look, neutral colour. 50mm, f/5.6, product in sharp focus. Three-point studio lighting, large softbox key from the upper left, soft rim from behind, controlled specular highlights on the leather. Start frame: the same white sneaker, three-quarter view on a light-grey backdrop; the shape, colour and laces stay exactly as in the image. 0-2s: The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. 2-4s: The rotation reveals the side profile and the stitching. Camera: continue the orbit. 4-5s: The shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Audio. Sound effects: soft whoosh on the reveal.
```

Negative prompt field:

```text
morphing, warped shape, flicker, text, watermark, logo, extra shoes
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
