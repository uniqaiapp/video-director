# Desert car chase

> a vintage muscle car races across a desert road chased by a dust cloud

| | |
|---|---|
| Mode | text-to-video |
| Duration | 10 s |
| Aspect | 16:9 |
| Lens | 200mm telephoto for the opening, compressed background |
| Light | hard midday sun from directly above, deep black shadows under the car, heat shimmer on the road |
| Style | 70s road movie, bleached highlights, heavy 35mm grain, slight halation |

## Timeline

| Time | Action | Camera |
|---|---|---|
| 0-2s | the car approaches head-on through heat shimmer, a dust cloud rising behind it | locked-off low angle on the road, telephoto |
| 2-4s | the car roars past the camera, dust and gravel spraying | whip pan to follow it |
| 4-6s | the car from the side at speed, the mesas sliding by | tracking shot alongside at wheel height |
| 6-8s | the driver's hand shifts gear; the car lurches forward | cut to an interior over-the-shoulder shot |
| 8-10s | the car shrinks into the distance, the dust settles on the empty road | locked-off wide from behind, hold |

**Motion physics.** the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road

**Sound.** Ambience: desert wind, insects. Effects: V8 engine roar building and passing, gravel spray, a gear change.

**Negative.** morphing, warped wheels, flicker, text, watermark, logo, frame jitter, extra cars

**Notes.** Multi-shot on purpose: Kling 3.0 follows the cut at 6 s. On single-shot models (Veo, Wan, Runway) the check command warns about beat 4; drop the interior beat for those. 21:9 would suit the genre, but Kling offers 16:9, 9:16 and 1:1.

## Prompts

### Kling 3.0

```text
A dusty black 1970 muscle car with chrome bumpers, driver barely visible through the glare in a straight two-lane desert highway at midday, heat shimmer, mesas on the horizon. 70s road movie, bleached highlights, heavy 35mm grain, slight halation. 200mm telephoto for the opening, compressed background. Hard midday sun from directly above, deep black shadows under the car, heat shimmer on the road. 0-2s: The car approaches head-on through heat shimmer, a dust cloud rising behind it. Camera: locked-off low angle on the road, telephoto. 2-4s: The car roars past the camera, dust and gravel spraying. Camera: whip pan to follow it. 4-6s: The car from the side at speed, the mesas sliding by. Camera: tracking shot alongside at wheel height. 6-8s: The driver's hand shifts gear; the car lurches forward. Camera: cut to an interior over-the-shoulder shot. 8-10s: The car shrinks into the distance, the dust settles on the empty road. Camera: locked-off wide from behind, hold. Motion: the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road. Audio. Ambience: desert wind, insects. Sound effects: V8 engine roar building and passing, gravel spray, a gear change.
```

Negative prompt field:

```text
morphing, warped wheels, flicker, text, watermark, logo, frame jitter, extra cars
```

- Paste the negative list into Kling's separate negative prompt field, not the prompt.
- Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.
- [Run in UniqAI](https://uniqai.app/models/kling/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.

### Veo 3 / 3.1

```text
A dusty black 1970 muscle car with chrome bumpers, driver barely visible through the glare in a straight two-lane desert highway at midday, heat shimmer, mesas on the horizon. 70s road movie, bleached highlights, heavy 35mm grain, slight halation. 200mm telephoto for the opening, compressed background. Hard midday sun from directly above, deep black shadows under the car, heat shimmer on the road. One continuous take over 10 seconds. The car approaches head-on through heat shimmer, a dust cloud rising behind it. Camera: locked-off low angle on the road, telephoto. Then the car roars past the camera, dust and gravel spraying. Camera: whip pan to follow it. Then the car from the side at speed, the mesas sliding by. Camera: tracking shot alongside at wheel height. Then the driver's hand shifts gear; the car lurches forward. Camera: cut to an interior over-the-shoulder shot. Then the car shrinks into the distance, the dust settles on the empty road. Camera: locked-off wide from behind, hold. Motion: the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road. Audio. Ambience: desert wind, insects. Sound effects: V8 engine roar building and passing, gravel spray, a gear change.
```

Negative prompt field:

```text
morphing, warped wheels, flicker, text, watermark, logo, frame jitter, extra cars
```

- Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.
- Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.
- Check: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
- Check: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
- [Run in UniqAI](https://uniqai.app/models/veo/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.

### Wan 2.5

```text
A dusty black 1970 muscle car with chrome bumpers, driver barely visible through the glare in a straight two-lane desert highway at midday, heat shimmer, mesas on the horizon. 200mm telephoto for the opening, compressed background. Hard midday sun from directly above, deep black shadows under the car, heat shimmer on the road. The car approaches head-on through heat shimmer, a dust cloud rising behind it. Camera: locked-off low angle on the road, telephoto. Then the car roars past the camera, dust and gravel spraying. Camera: whip pan to follow it. Then the car from the side at speed, the mesas sliding by. Camera: tracking shot alongside at wheel height. Then the driver's hand shifts gear; the car lurches forward. Camera: cut to an interior over-the-shoulder shot. Then the car shrinks into the distance, the dust settles on the empty road. Camera: locked-off wide from behind, hold. Motion: the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road. Audio. Ambience: desert wind, insects. Sound effects: V8 engine roar building and passing, gravel spray, a gear change.
```

Negative prompt field:

```text
morphing, warped wheels, flicker, text, watermark, logo, frame jitter, extra cars
```

- Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.
- **Does not fit:** Wan 2.5: prompt is 1200 characters, limit is 800
- Check: Wan 2.5 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
- [Run in UniqAI](https://uniqai.app/video/text-to-video/?utm_source=github&utm_medium=examples&utm_campaign=video-director): UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.

### Seedance 2.0

```text
A dusty black 1970 muscle car with chrome bumpers, driver barely visible through the glare in a straight two-lane desert highway at midday, heat shimmer, mesas on the horizon. 70s road movie, bleached highlights, heavy 35mm grain, slight halation. 200mm telephoto for the opening, compressed background. Hard midday sun from directly above, deep black shadows under the car, heat shimmer on the road. Shot 1 (0-2s): The car approaches head-on through heat shimmer, a dust cloud rising behind it. Camera: locked-off low angle on the road, telephoto. Shot 2 (2-4s): The car roars past the camera, dust and gravel spraying. Camera: whip pan to follow it. Shot 3 (4-6s): The car from the side at speed, the mesas sliding by. Camera: tracking shot alongside at wheel height. Shot 4 (6-8s): The driver's hand shifts gear; the car lurches forward. Camera: cut to an interior over-the-shoulder shot. Shot 5 (8-10s): The car shrinks into the distance, the dust settles on the empty road. Camera: locked-off wide from behind, hold. Motion: the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road. Audio. Ambience: desert wind, insects. Sound effects: V8 engine roar building and passing, gravel spray, a gear change. Avoid: morphing, warped wheels, flicker, text, watermark, logo, frame jitter, extra cars.
```

- Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.

### Runway Gen-4 / 4.5

```text
Locked-off low angle on the road, telephoto: A dusty black 1970 muscle car with chrome bumpers, driver barely visible through the glare in a straight two-lane desert highway at midday, heat shimmer, mesas on the horizon. The car approaches head-on through heat shimmer, a dust cloud rising behind it. Camera: locked-off low angle on the road, telephoto. Then the car roars past the camera, dust and gravel spraying. Camera: whip pan to follow it. Then the car from the side at speed, the mesas sliding by. Camera: tracking shot alongside at wheel height. Then the driver's hand shifts gear; the car lurches forward. Camera: cut to an interior over-the-shoulder shot. Then the car shrinks into the distance, the dust settles on the empty road. Camera: locked-off wide from behind, hold. Motion: the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road. 70s road movie, bleached highlights, heavy 35mm grain, slight halation.
```

- Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.
- Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.
- **Does not fit:** Runway Gen-4 / 4.5: prompt is 1044 characters, limit is 1000
- Check: Runway Gen-4 / 4.5 has no native audio: the sound block is dropped from the prompt, add audio in the edit
- Check: Runway Gen-4 / 4.5 ignores negative prompts: the negative list is dropped, phrase what you want instead
- Check: Runway Gen-4 / 4.5 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually

### Generic (any model)

```text
A dusty black 1970 muscle car with chrome bumpers, driver barely visible through the glare in a straight two-lane desert highway at midday, heat shimmer, mesas on the horizon. 70s road movie, bleached highlights, heavy 35mm grain, slight halation. 200mm telephoto for the opening, compressed background. Hard midday sun from directly above, deep black shadows under the car, heat shimmer on the road. 0-2s: The car approaches head-on through heat shimmer, a dust cloud rising behind it. Camera: locked-off low angle on the road, telephoto. 2-4s: The car roars past the camera, dust and gravel spraying. Camera: whip pan to follow it. 4-6s: The car from the side at speed, the mesas sliding by. Camera: tracking shot alongside at wheel height. 6-8s: The driver's hand shifts gear; the car lurches forward. Camera: cut to an interior over-the-shoulder shot. 8-10s: The car shrinks into the distance, the dust settles on the empty road. Camera: locked-off wide from behind, hold. Motion: the car squats under acceleration and leans in the pass; wheels spin with motion blur; dust and gravel are thrown backwards and settle slowly; heat shimmer distorts the far road. Audio. Ambience: desert wind, insects. Sound effects: V8 engine roar building and passing, gravel spray, a gear change.
```

Negative prompt field:

```text
morphing, warped wheels, flicker, text, watermark, logo, frame jitter, extra cars
```


---

Rendered by `python3 scripts/storyboard.py render <board.json> --model all --format md` (video-director 0.1.0).
