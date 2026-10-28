# Camera moves

Vocabulary that every current video model responds to. Name the move, the speed and the subject it relates to, in that order: "slow push-in on her hands" beats "cinematic camera". One move per beat; two moves in one beat is where most prompts fall apart.

Query from the CLI: `python3 scripts/storyboard.py vocab camera orbit`.

| Move | Phrase to use | What it says to the viewer | Watch out |
|---|---|---|---|
| Static | locked-off shot, tripod, no camera movement | calm, observational, lets the subject's motion carry the beat | models drift anyway; add "camera stays fixed" if it matters |
| Push-in | slow push-in on [subject] | growing attention, intimacy, dread | over 4 s it reads as a zoom; keep it to one beat |
| Pull-back | slow pull-back revealing [space] | context reveal, isolation, ending | reveal must be described: say what appears at the edges |
| Dolly in / out | dolly in along the table | same as push but with parallax; feels physical | say "dolly" only when foreground objects exist to show parallax |
| Tracking | tracking shot alongside [subject], matching their pace | energy, following a journey | the model needs a direction: left-to-right, from behind |
| Follow (behind) | following shot from behind at shoulder height | immersion, anticipation | risk of the subject's back for the whole clip; cut to a side angle in the next beat |
| Lead (in front) | leading shot, camera moves backwards ahead of [subject] | the face while moving | say the camera is "ahead of" the subject, not "in front of" (that reads as static) |
| Pan | slow pan left to right across [scene] | survey, landscape | pans over 90 degrees get mushy; split into two beats |
| Whip pan | fast whip pan to [new subject] | sudden shift, comedy, energy | works as a transition between beats; motion blur is expected |
| Tilt | slow tilt up from [low thing] to [high thing] | scale, reveal of height | name both ends |
| Pedestal / crane | crane up from street level to rooftop height | grandeur, overview | models confuse crane with tilt; say "the camera itself rises" |
| Orbit / arc | slow 90-degree orbit around [subject], clockwise | product, hero moment, 3D presence | full 360 in one clip usually breaks the subject; 90 to 180 degrees is safe |
| Handheld | handheld, slight natural sway | documentary, nerves, presence | "shaky cam" gives you broken frames; "slight sway" is the usable version |
| Steadicam / gimbal | smooth gimbal glide through [space] | polished movement, walkthrough | describe the path: "through the doorway and into the kitchen" |
| Dolly zoom | dolly zoom, background compresses while subject stays the same size | vertigo, realisation | hit or miss on every model; try once, keep expectations low |
| Aerial / drone | aerial view, slow forward drift, slight tilt down | scale, establishing | altitude matters: "low aerial, 20 metres up" vs "high aerial" |
| FPV drone | fast FPV drone dive through [gap] | adrenaline | fast FPV eats detail; keep the environment simple |
| Rack focus | rack focus from [foreground] to [background] | attention shift without moving | state both planes and the direction |
| Snap zoom | quick snap zoom on [detail] | emphasis, meme energy | only one per clip |
| Top-down | top-down overhead shot, camera looking straight down | process, food, maps | say "straight down" or you get a high angle |
| Low angle | low angle looking up at [subject] | power, scale | combine with a slow push for a hero beat |
| Dutch angle | dutch angle, camera tilted 15 degrees | unease | state the degrees, otherwise the model picks 45 |
| POV | first-person point of view, hands visible | immersion, product use | describe the hands and what they hold |
| Over-the-shoulder | over-the-shoulder shot from behind [A] looking at [B] | conversation, confrontation | name who is in focus |
| Hold | hold on [subject] for the last two seconds | ending, letting the shot breathe | use as the final beat; prevents the model from inventing a new event |

## Speed words

| Word | Approximate feel | Use |
|---|---|---|
| glacial, barely perceptible | motion visible only across the whole clip | mood pieces, product, portrait |
| slow | one move over 3 to 4 seconds | default for almost everything |
| steady | constant, medium speed | tracking, walkthrough |
| brisk | one move over about 1 second | energy, comedy |
| fast, whip, snap | under half a second | transitions, emphasis |

## Combining moves across beats

A storyboard reads well when the camera changes once per two beats, not every beat. The usual shape for an 8-second clip: beat 1 establishes with a slow move, beats 2 and 3 continue or hold that move while the subject acts, beat 4 holds or pulls back. For a 5-second clip: one move, one hold.
