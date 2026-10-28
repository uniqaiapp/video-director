# Negative prompts

A negative list names things that must not appear. It works where the model has a separate negative field (Kling, Veo, Wan) and is appended as an "Avoid:" sentence where it does not (Seedance). Runway ignores negatives entirely; write the positive version instead. The `check` command warns about both cases.

Two rules that hold on every model:

1. **Nouns, not sentences.** "no text" inside a prompt is read as "text". Write `text` in the negative list, nothing in the prompt.
2. **Short list.** Six to ten terms. Long negative lists degrade the positive prompt on Kling and Wan.

Query from the CLI: `python3 scripts/storyboard.py vocab negative hands`.

| Problem you see | Negative term(s) | Positive phrasing that works better |
|---|---|---|
| Faces or objects melting between frames | morphing, warping | "the subject keeps the same face and clothing throughout" |
| Extra fingers, fused hands | extra limbs, warped hands, extra fingers | "hands rest on the table, fingers relaxed and visible" |
| Brightness pulsing | flicker, strobing | "constant exposure" |
| Random captions, signs, watermarks | text, captions, subtitles, watermark, logo | keep signs out of frame, or say "signs out of focus" |
| Unwanted cuts | jump cuts, scene change | "one continuous take" |
| Shaky, jittery frames | frame jitter, camera shake | "smooth gimbal movement" |
| Plastic, over-smooth skin | plastic skin, airbrushed, over-smoothed | "natural skin texture, visible pores, fine grain" |
| Over-saturated, HDR look | oversaturated, HDR glow, neon haze (if unwanted) | "muted, filmic colour" |
| Blurry, low detail | blurry, low resolution, out of focus (only if not intended) | name the aperture and focus plane |
| Duplicate subjects | duplicate, clone, twins | "one person in frame" |
| Distorted background architecture | warped architecture, bent lines | "straight architectural lines" |
| Objects floating | floating, levitating | describe contact: "feet planted", "cup rests on the saucer" |
| Slow-motion when you wanted real time | slow motion | "real-time speed" |
| Wrong era or style bleed | cartoon, anime, 3D render, illustration | "photographic, live-action" |
| Mirror text, gibberish on labels | gibberish text, unreadable labels | turn labels away from camera |
| Extra people in an empty scene | crowd, bystanders | "empty street" |
| Lens dirt and artefacts | lens dirt, chromatic aberration, vignette (if unwanted) | |

## Default list

The `new` command starts every storyboard with: `morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter`. Remove the ones that conflict with the shot (a CCTV look wants its timestamp text; a music video may want jump cuts) and add one or two that match the specific risk of the scene.

## Per-model notes

| Model | Where negatives go | Limit |
|---|---|---|
| Kling 3.0 | separate negative prompt field | 2500 characters |
| Veo 3 | `negativePrompt` parameter; plain nouns, Google's own guidance says not to write "no" or "don't" | not documented |
| Wan 2.5 | separate field | 500 characters |
| Seedance 2.0 | no field; appended inline as "Avoid: ..." | counts toward the prompt |
| Runway Gen-4 | not supported; Runway's prompting guide asks for positive phrasing only | dropped by render |
