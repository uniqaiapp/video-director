# Per-model formatting notes

What each model accepts and how it reads a prompt. The values below are what `scripts/storyboard.py` uses (the `MODELS` table; `tests/test_scripts.py` checks that this file and the table agree). They were read from each vendor's public documentation on **2026-10-28**. Vendors change limits without notice: when a value here disagrees with the vendor page, trust the vendor page and open an issue.

`python3 scripts/storyboard.py models` prints the same table from the script.

| Key | Model | Lengths | Aspects | Native audio | Prompt limit | Negatives | Shots |
|---|---|---|---|---|---|---|---|
| `kling` | Kling 3.0 | 3-15 s | 16:9, 9:16, 1:1 | yes | 2500 characters | separate field, 2500 characters | multi-shot |
| `veo` | Veo 3 / 3.1 | 4/6/8 s | 16:9, 9:16 | yes | no hard cap; keep under ~2000 characters | `negativePrompt` field | single continuous shot |
| `wan` | Wan 2.5 | 5/10 s | 16:9, 9:16, 1:1, 4:3, 3:4 | yes | 800 characters | separate field, 500 characters | single shot |
| `seedance` | Seedance 2.0 | 4-15 s | 16:9, 9:16, 1:1, 4:3, 3:4, 21:9 | yes | no hard cap; keep under ~1500 characters | inline ("Avoid: ...") | multi-shot |
| `runway` | Runway Gen-4 / 4.5 | 5/10 s | 16:9, 9:16, 1:1, 4:3, 3:4, 21:9 | no | 1000 characters | not supported | single shot |
| `generic` | any model | 2-30 s | any | unknown | keep under ~2000 characters | separate field | multi-shot |

Aliases accepted by the CLI: `kling3`, `veo3`, `wan2.5`, `gen4`, `seedance2`, `any`. `sora` maps to `generic`: OpenAI announced Sora's discontinuation in spring 2026, so there is no live target to format for.

## Kling 3.0 (Kuaishou)

- Source: Kling AI documentation and API reference at klingai.com (model `kling-v3`), and the in-app composer.
- Reads prompts in the order subject, movement, scene, camera, light, atmosphere. The render command emits exactly that order.
- Follows timed beats as shots ("0-2s: ... 2-4s: ...") and keeps the subject consistent across them. For a single continuous take, remove the timestamps and merge the beats into one sentence.
- Native audio: speech and effects generated from the prompt; quote dialogue with a speaker.
- Negative prompt is a separate field. Terms, not sentences.
- Text-to-video and image-to-video; with a start image, describe only what changes, not what is already in the frame.
- UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1 from text or a photo ([model page](https://uniqai.app/models/kling?utm_source=github&utm_medium=skill&utm_campaign=video-director)). Kuaishou announced Kling 4.0 in October 2026 with longer single-pass clips; this file targets 3.0 until the 4.0 API limits are published.

## Veo 3 / Veo 3.1 (Google DeepMind)

- Source: Google AI for Developers, "Generate videos with Veo" and the Veo prompt guide; Vertex AI Veo reference.
- Clips of 4, 6 or 8 seconds at 720p or 1080p, 16:9 or 9:16. A 10-second storyboard must be re-timed to 8 s (the check command says so).
- One continuous shot per generation. The render command merges beats with "Then" into a single description instead of numbering shots.
- Native audio is the strongest of the group: describe ambience, effects and dialogue explicitly; dialogue in quotes with a speaker produces lip-synced speech.
- Known habit: burned-in subtitles whenever there is dialogue. The render command adds `subtitles, captions` to the negative field.
- Negatives go in the `negativePrompt` parameter as plain nouns. Google's guide says explicitly not to use "no" or "don't".
- Veo 3.1 adds reference images, first/last frame and extension; the storyboard `image_ref` maps to the first frame.
- UniqAI runs Veo 3 at 6 s or 8 s with audio in 16:9 or 9:16 from text or a photo ([model page](https://uniqai.app/models/veo?utm_source=github&utm_medium=skill&utm_campaign=video-director)).

## Wan 2.5 (Alibaba)

- Source: Alibaba Cloud Model Studio documentation for `wan2.5-t2v` and `wan2.5-i2v`.
- 5 or 10 seconds, 480p/720p/1080p, five aspect ratios.
- Prompt field is limited to 800 characters and the negative field to 500. The render command uses a terse layout (subject, lens, light, beats, motion, audio) and the check command fails hard on the limits.
- Native audio generated from the description; also accepts an uploaded audio track for sync (not covered by the storyboard format).
- Single shot: write beats as a continuous action.

## Seedance 2.0 (ByteDance)

- Source: Volcengine Ark (BytePlus ModelArk) Seedance documentation.
- Multi-shot by design: numbered shots with an explicit camera per shot are followed well, which is why the render command emits "Shot 1 (0-2s): ...".
- Native audio in 2.0. Seedance 1.0 Pro had none; if you target 1.0, treat the sound block as a note for the edit.
- No separate negative field; the render command appends "Avoid: ..." to the prompt. Keep the list short because it counts toward the prompt.

## Runway Gen-4 / Gen-4.5

- Source: Runway Help Center, "Gen-4 Video prompting guide" and the Runway API reference (`promptText` up to 1000 characters).
- Gen-4 is image-to-video first: give it the start frame. Gen-4.5 takes text-only prompts.
- Runway's guide asks for simple, positive phrasing and a camera instruction first; negatives and "do not" are ignored, so the render command drops the negative list and leads with the first beat's camera move.
- No native audio. The sound block is dropped from the prompt; keep it in the storyboard for the edit.
- 5 or 10 seconds; six aspect ratios.

## Generic

For models not listed (Hailuo/MiniMax, Luma, Pika, LTX, open-weights models): the generic target emits the full structured prompt with timed beats and a separate negative list. Trim to the model's limit by hand, then open an issue with the vendor's documented limits so the model can be added.
