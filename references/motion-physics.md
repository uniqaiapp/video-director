# Motion physics

Most "AI video" tells come from motion that ignores mass, drag or contact. A one-sentence physics note in the storyboard fixes a surprising share of them, because the models were trained on real footage and respond to physical vocabulary. Describe *how* things move, not only *that* they move.

Query from the CLI: `python3 scripts/storyboard.py vocab physics cloth`.

| Material or event | Phrase to use | Why it helps |
|---|---|---|
| Walking | natural gait, weight shifts from foot to foot, arms swing opposite to legs | prevents gliding and moonwalking |
| Running | leaning forward, hair and clothing trailing, feet leaving the ground, dust kicked up | gives stride and effort |
| Hands and objects | fingers wrap around the cup, grip visible, the cup tilts with the wrist | hands are the weakest area; contact words help |
| Hair | hair moves with the head and settles a moment later, strands catch the wind | adds lag, the key to believable hair |
| Cloth | fabric folds and swings with the body, settles after the movement stops | prevents painted-on clothing |
| Silk, chiffon | light fabric floats and ripples, slow to settle | flowing fashion shots |
| Denim, leather | heavy fabric moves little, creases at the joints | stops heavy clothes from fluttering |
| Liquid pour | liquid falls in a steady column, splashes on contact, surface ripples spread and fade | pours are a classic failure |
| Steam, smoke | steam rises, curls and thins out, drifts with the air | stops it from looking like fog |
| Fire | flames flicker upward, embers rise and fade, light flickers on nearby surfaces | ties light to the source |
| Rain | rain falls in straight lines, droplets bounce off hard surfaces, puddles ripple on impact | adds contact |
| Snow | snow drifts down slowly, swirls in the wind, settles on shoulders | slow vertical motion |
| Water surface | small waves, reflections distort as the surface moves | keeps reflections alive |
| Underwater | everything moves slowly with drag, bubbles rise, particles drift | removes "air" movement |
| Wind | wind pushes grass and leaves in one direction, gusts come and go | makes stillness feel alive |
| Vehicles | the car leans into the turn, suspension absorbs bumps, wheels spin with motion blur | stops cars from sliding |
| Motorbike | rider leans with the bike, tyres compress under braking | weight transfer |
| Falling object | falls with gravity, accelerates, bounces once and settles | stops floating |
| Thrown object | arcs through the air, spins, lands with a small bounce | parabola |
| Animals | the cat's weight shifts before it jumps, tail balances, fur ripples | anticipation before action |
| Birds | wings beat in a steady rhythm, gliding between beats, body tilts in turns | stops flapping without flying |
| Crowd | people move at slightly different speeds, some stop, some turn | prevents synchronised crowds |
| Camera contact | the camera passes close enough that the door frame fills the edge for a moment | makes camera moves feel physical |
| Glass, reflections | reflections slide across the glass as the camera moves | anchors camera motion |
| Dust, particles | dust catches the light and drifts slowly | cheap depth cue |
| Mechanical | gears turn at constant speed, pistons move in rhythm | predictable motion the models like |
| Slow motion | slow motion, 120 fps feel, droplets hang in the air | say "slow motion" once; combine with a short beat |
| Timelapse | timelapse, clouds streak, shadows sweep, people blur | global, well understood |

## Speed and timing words

| Word | Use |
|---|---|
| real-time | default; say it when the model tends to slow things down (pours, walking) |
| slow motion | one beat at most; everything in frame slows, including hair and water |
| gradual, over the whole clip | for changes that should take the full duration (sunset, melting) |
| sudden, within half a second | for impacts, reveals, reactions |
| settles | the single most useful verb: "the hair settles", "the dust settles", "the cloth settles" |

## What to keep out

Hold the physics note to one or two sentences and only about the things in the shot. A physics line about rain in a scene with no rain confuses the model more than it helps. Negative prompts for physics ("no sliding feet") work poorly; "feet plant firmly on each step" works better.
