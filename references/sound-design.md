# Sound design

Models with native audio (Kling 3.0, Veo 3, Wan 2.5, Seedance 2.0 at the time of writing; see model-notes.md) generate sound from the prompt. If you say nothing, you get a generic bed or silence. Describe three layers and keep each to a phrase: ambience (the room), effects (things that happen), dialogue (what is said and by whom). Models without native audio ignore the block; the render command drops it for them.

Query from the CLI: `python3 scripts/storyboard.py vocab sound rain`.

## Ambience

| Scene | Phrase to use |
|---|---|
| Quiet interior | quiet room tone, faint refrigerator hum |
| Cafe | cafe ambience, espresso machine hiss, low chatter, cups |
| Street, day | city traffic, footsteps, a distant siren |
| Street, night rain | steady rain, tyres on wet asphalt, distant thunder |
| Forest | wind in the trees, birdsong, a stream |
| Beach | surf rolling in, gulls, wind |
| Underwater | muffled underwater hum, bubbles |
| Office | keyboard clicks, air conditioning hum, muffled voices |
| Car interior | engine hum, road noise, indicator ticking |
| Train | rail rhythm, carriage creak, announcement muffled |
| Stadium | crowd roar, whistle, PA echo |
| Desert | wind, insects, silence between gusts |
| Space / sci-fi | low ship hum, ventilation, distant alarms |
| Nightclub | muffled bass through the wall, crowd |

## Effects

| Event | Phrase to use |
|---|---|
| Pour | liquid pouring into a ceramic cup, soft splash |
| Steam | hiss of steam |
| Footsteps | footsteps on gravel / wooden floor / wet concrete |
| Door | door creaks open, latch clicks |
| Glass | glass clink, ice settling |
| Fabric | fabric rustle |
| Impact | a dull thud, then silence |
| Whoosh | soft whoosh on the reveal |
| Keys, phone | keys jingle, phone buzz |
| Engine | engine revs, tyres on gravel, gear change |
| Fire | crackling fire, a log shifts |
| Rain on window | rain tapping on glass |
| Camera | shutter click (only if a camera is in the shot) |

## Dialogue

Write the line in quotes with the speaker and the delivery: `The barista says, warmly: "First one's on the house."` Rules that hold across models:

- One or two short lines per clip; a 10-second clip fits about 25 words of speech.
- Name the language if it is not English, and say "lip-synced" when the speaker is on screen.
- Say "off-screen voice" or "voiceover" for narration so the model does not invent a speaker.
- Veo tends to burn in subtitles when dialogue is present; the render command adds "subtitles, captions" to its negative field automatically.
- For silence, say so: "no dialogue, no music". An empty dialogue field is not an instruction.

## Music

| Phrase | Use |
|---|---|
| no music | default for anything you will score later |
| soft piano underscore, sparse | emotional, slow |
| low synth drone | tension, sci-fi |
| upbeat acoustic guitar | lifestyle, product |
| muffled club music from another room | realism in interiors |

Generated music is rarely usable in a final edit; treat it as a placeholder and plan to replace it. The storyboard still benefits from naming it, because music words change the pacing of the generated motion.
