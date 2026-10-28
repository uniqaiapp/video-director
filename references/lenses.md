# Lenses, focus and format

Models do not simulate optics exactly, but focal length and aperture words change framing, background compression and depth of field reliably. Name one lens for the whole clip; changing lenses between beats implies a cut.

Query from the CLI: `python3 scripts/storyboard.py vocab lens macro`.

| Lens | Phrase to use | Look | Best for | Avoid for |
|---|---|---|---|---|
| 14-16mm ultra-wide | 16mm ultra-wide, slight barrel distortion | huge space, stretched edges, everything in focus | interiors, architecture, underwater, FPV | faces (distorts noses) |
| 24mm wide | 24mm wide, deep focus | open, contextual, slight exaggeration of distance | landscapes, aerial, walkthroughs, action | tight portraits |
| 35mm | 35mm, natural perspective | the "documentary" look, little distortion | street, handheld, two-shots | isolating one subject in clutter |
| 50mm | 50mm, natural perspective, f/2.8 | close to the human eye | products, dialogue, general use | drama that wants compression |
| 85mm portrait | 85mm, f/2, shallow depth of field | flattering compression, creamy background | portraits, beauty, emotion | spaces that need to read as spaces |
| 100mm macro | 100mm macro, f/4, extremely shallow depth of field | tiny subjects fill the frame, texture, liquid | food, product detail, insects, materials | anything that moves across frame fast |
| 135-200mm telephoto | 200mm telephoto, compressed background | layers stacked, subject isolated, heat shimmer | wildlife, sports, distant subjects, cityscapes | small rooms |
| Anamorphic | anamorphic 2x, oval bokeh, horizontal lens flares | wide cinematic frame, streaked highlights | sci-fi, music video, night neon | clean product work |
| Vintage | vintage lens, soft edges, low contrast, mild halation | nostalgic, filmic, gentle | memories, period pieces | crisp commercial work |
| Tilt-shift | tilt-shift, narrow band of focus | miniature effect | aerial city, timelapse | portraits |
| Fisheye | fisheye, extreme barrel distortion | skate video, 90s | action sports, comedy | everything else |

## Aperture and depth of field

| Phrase | Effect |
|---|---|
| f/1.4, razor-thin depth of field | one eye sharp, the rest soft; risky for moving subjects |
| f/2, shallow depth of field | face sharp, background a soft wash; the default portrait look |
| f/4, moderate depth of field | subject and nearby objects sharp |
| f/8, deep focus | foreground to horizon sharp; landscapes, aerial |
| f/16, everything sharp, slight diffraction softness | rarely needed; implies bright daylight |

## Focus behaviour

| Phrase | Effect |
|---|---|
| focus locked on [subject] | prevents focus hunting when the subject moves |
| rack focus from A to B | attention shift; name both planes |
| focus breathing as the lens pulls | subtle size change on focus pulls; adds realism |
| soft focus throughout | dreamy; also hides model artefacts |

## Format and texture

| Phrase | Effect |
|---|---|
| shot on 35mm film, fine grain | organic grain, slightly lifted blacks |
| shot on 16mm film, visible grain | gritty, documentary, music video |
| digital cinema, clean, high dynamic range | modern commercial look |
| 1990s camcorder, interlaced, 4:3 | nostalgia, found footage; say 4:3 in the aspect field too |
| CCTV, fixed wide, timestamp overlay | surveillance; the timestamp counts as text, remove "text" from the negative list |
| black and white, high contrast | removes colour problems entirely; good for first tests |

## Aspect ratio

| Aspect | Use |
|---|---|
| 16:9 | default, landscape, YouTube, web |
| 9:16 | vertical: Reels, TikTok, Shorts; frame subjects taller than wide |
| 1:1 | feed posts, product tiles |
| 21:9 | cinematic widescreen; not every model offers it (see model-notes.md) |
| 4:3 / 3:4 | retro, photo-like; offered by Wan, Seedance and Runway |

Decide the aspect before writing beats. A 9:16 storyboard should describe vertical compositions ("full body, head near the top of the frame"); a 16:9 one describes horizontal ones.
