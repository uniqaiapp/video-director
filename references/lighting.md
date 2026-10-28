# Lighting

Light is the cheapest way to make generated video look intentional. Name the key light (where the main light comes from), the quality (hard or soft), the colour temperature contrast, and any practicals (lights visible in the frame). Keep it constant across beats unless a change in light *is* the beat.

Query from the CLI: `python3 scripts/storyboard.py vocab light rim`.

| Setup | Phrase to use | Mood | Pairs well with |
|---|---|---|---|
| Window key | soft daylight from a large window camera-left, gentle fill | natural, honest, interview | portraits, kitchens, offices |
| Golden hour | low golden-hour sun, long shadows, warm highlights, cool shadows | nostalgia, romance, ending | landscapes, walking shots, drone |
| Blue hour | blue hour, deep blue sky, warm practical lights starting to show | melancholy, city, transition | cityscapes, cars, rooftops |
| Overcast | overcast sky, soft even light, no hard shadows | documentary, calm, fashion | street, product outdoors, faces |
| Hard sun | hard midday sun, deep black shadows, high contrast | heat, desert, tension | action, western, sport |
| Backlight / rim | strong backlight, rim light outlining the subject, lens flare | hero, silhouette, separation | dust, hair, water spray |
| Silhouette | subject in silhouette against a bright background | mystery, graphic | doorways, sunsets, windows |
| Rembrandt | Rembrandt lighting, triangle of light on the far cheek | classic portrait, drama | 85mm, dark backgrounds |
| Butterfly / beauty | beauty lighting from above the lens, soft shadow under the nose | glamour, cosmetics | beauty products, close-ups |
| Low key | low-key lighting, single hard source, most of the frame in shadow | noir, thriller | smoke, rain, interrogation |
| High key | high-key lighting, bright and even, white background | clean commercial, tech | product, explainer |
| Neon practicals | neon signs as practicals, magenta and cyan, wet reflections | cyberpunk, night city | rain, 35mm anamorphic |
| Candle / fire | candlelight, warm flicker, falloff into darkness | intimacy, period, ritual | close-ups, dialogue |
| Screen glow | face lit by a phone or monitor glow, cool blue | isolation, late night | tight portraits |
| Volumetric | volumetric light shafts through haze or dust | cathedral, forest, warehouse | wide lenses, slow push-in |
| Caustics | caustic light patterns rippling across surfaces | underwater, poolside | underwater, slow drifts |
| Headlights | passing car headlights sweeping across the room | motel, suspense | interiors at night, slow pan |
| Stage / concert | concert lighting, moving beams, haze, colour washes | music, energy | handheld, crowd |
| Studio product | three-point studio lighting, softbox key, gradient backdrop | catalogue, packshot | orbit, turntable |
| Mixed temperature | tungsten interior with blue daylight through the window | realism, depth | kitchens, cafes, hotel rooms |

## Light quality words

| Word | Meaning |
|---|---|
| hard | small source, crisp shadow edges (sun, bare bulb) |
| soft | large source, gradual shadow edges (window, softbox, overcast) |
| diffused | light passed through a material; softer still |
| specular | sharp bright reflections on glossy surfaces |
| falloff | how quickly light fades with distance; "rapid falloff" means the background goes dark |
| motivated | light that has a visible or plausible source in the scene; the single most useful word for realism |

## Colour and grade

| Phrase | Effect |
|---|---|
| teal and orange grade | the default blockbuster contrast; safe |
| muted, desaturated, lifted blacks | indie, melancholy |
| warm highlights, cool shadows | pleasant separation without stylisation |
| monochrome with one accent colour | graphic, music video |
| Kodak Vision3 250D, soft halation | filmic daylight stock |
| Kodak 500T, grain in the shadows, tungsten | filmic night stock |
| bleach bypass, high contrast, silver tones | war film, grit |

## Light as the beat

Changes in light are events the models handle well, because they are global: "the sun breaks through the clouds", "the neon sign flickers on", "someone opens the fridge and cold light spills out", "headlights sweep across the ceiling". One light change per clip is plenty.
