#!/usr/bin/env python3
"""storyboard.py: scaffold, check and render second-by-second storyboards for AI video models.

Zero dependencies (Python 3.9+ stdlib). Runs from any directory.

  python3 scripts/storyboard.py models
  python3 scripts/storyboard.py new --idea "a barista pours latte art at dawn" --duration 8 -o board.json
  python3 scripts/storyboard.py check board.json [--model kling]
  python3 scripts/storyboard.py render board.json --model veo [--format txt|md]
  python3 scripts/storyboard.py render board.json --model all --format md
  python3 scripts/storyboard.py vocab camera [push]

A storyboard is a small JSON file (see `new` for the shape and examples/ for finished ones).
The agent fills the creative content; this script keeps the structure honest and formats the
same storyboard for each model's limits and syntax. Model limits live in MODELS below and in
references/model-notes.md; both carry the date they were last checked.
"""
import argparse
import json
import math
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(ROOT, "references")
VERSION = "0.1.0"
CHECKED_ON = "2026-10-28"
UTM = "utm_source=github&utm_medium=examples&utm_campaign=video-director"

# ---------------------------------------------------------------------------
# Model table. Numbers are from each vendor's public documentation as read on
# CHECKED_ON; references/model-notes.md has the source URLs. "soft" limits are
# recommendations, not API rejections. Keep this table and model-notes.md in sync
# (tests/test_scripts.py compares them).
# ---------------------------------------------------------------------------
MODELS = {
    "kling": {
        "label": "Kling 3.0",
        "durations": list(range(3, 16)),
        "aspects": ["16:9", "9:16", "1:1"],
        "audio": "native",
        "prompt_max": 2500,
        "prompt_soft": None,
        "negative": "field",
        "negative_max": 2500,
        "modes": ["t2v", "i2v"],
        "multishot": True,
        "uniqai": "https://uniqai.app/models/kling?" + UTM,
        "uniqai_note": "UniqAI runs Kling 3.0 at 5 s or 8 s in 16:9, 9:16 or 1:1, from text or a photo.",
    },
    "veo": {
        "label": "Veo 3 / 3.1",
        "durations": [4, 6, 8],
        "aspects": ["16:9", "9:16"],
        "audio": "native",
        "prompt_max": None,
        "prompt_soft": 2000,
        "negative": "field",
        "negative_max": None,
        "modes": ["t2v", "i2v"],
        "multishot": False,
        "uniqai": "https://uniqai.app/models/veo?" + UTM,
        "uniqai_note": "UniqAI runs Veo 3 at 6 s or 8 s with audio, in 16:9 or 9:16, from text or a photo.",
    },
    "wan": {
        "label": "Wan 2.5",
        "durations": [5, 10],
        "aspects": ["16:9", "9:16", "1:1", "4:3", "3:4"],
        "audio": "native",
        "prompt_max": 800,
        "prompt_soft": None,
        "negative": "field",
        "negative_max": 500,
        "modes": ["t2v", "i2v"],
        "multishot": False,
        "uniqai": "https://uniqai.app/video/text-to-video?" + UTM,
        "uniqai_note": "UniqAI runs Wan 2.5 next to Kling 3.0 and Veo 3, so one storyboard can be compared across models.",
    },
    "seedance": {
        "label": "Seedance 2.0",
        "durations": list(range(4, 16)),
        "aspects": ["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"],
        "audio": "native",
        "prompt_max": None,
        "prompt_soft": 1500,
        "negative": "inline",
        "negative_max": None,
        "modes": ["t2v", "i2v"],
        "multishot": True,
        "uniqai": None,
        "uniqai_note": None,
    },
    "runway": {
        "label": "Runway Gen-4 / 4.5",
        "durations": [5, 10],
        "aspects": ["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"],
        "audio": "none",
        "prompt_max": 1000,
        "prompt_soft": None,
        "negative": "none",
        "negative_max": None,
        "modes": ["t2v", "i2v"],
        "multishot": False,
        "uniqai": None,
        "uniqai_note": None,
    },
    "generic": {
        "label": "Generic (any model)",
        "durations": list(range(2, 31)),
        "aspects": ["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"],
        "audio": "unknown",
        "prompt_max": None,
        "prompt_soft": 2000,
        "negative": "field",
        "negative_max": None,
        "modes": ["t2v", "i2v"],
        "multishot": True,
        "uniqai": None,
        "uniqai_note": None,
    },
}
ALIASES = {"kling3": "kling", "kling-3": "kling", "veo3": "veo", "veo-3": "veo", "wan2.5": "wan",
           "wan25": "wan", "gen4": "runway", "gen-4": "runway", "seedance2": "seedance", "any": "generic",
           "sora": "generic"}
MODEL_ORDER = ["kling", "veo", "wan", "seedance", "runway", "generic"]

FILL = "[[fill:"  # marker left by `new`; `check` refuses to pass while any remain

# ---------------------------------------------------------------------------
# Keyword hints used by `new`. Deterministic, small, and only a starting point.
# ---------------------------------------------------------------------------
HINTS = [
    (r"\b(drone|aerial|coastline|coast|skyline|mountain|valley|canyon|from above)\b", {
        "lens": "24mm wide, deep focus, f/8",
        "camera": "aerial, slow forward drift with a gentle tilt down",
        "physics": "parallax between foreground and horizon; wind moves grass and water",
        "sound": {"ambience": "wind, distant surf", "fx": "", "dialogue": ""}}),
    (r"\b(macro|pour|drip|drop|steam|coffee|latte|ramen|honey|syrup|sauce)\b", {
        "lens": "100mm macro, f/4, shallow depth of field",
        "camera": "locked-off, then a slow push-in on the detail",
        "physics": "liquid has weight and surface tension; steam rises and curls; droplets fall at real speed",
        "sound": {"ambience": "quiet room tone", "fx": "liquid pour, soft ceramic contact", "dialogue": ""}}),
    (r"\b(night|neon|rain|rainy|wet|storm)\b", {
        "light": "practical neon and shop signs, wet-asphalt reflections, cool key with warm fill",
        "physics": "rain streaks catch the light; puddles ripple on impact; reflections distort with movement",
        "sound": {"ambience": "steady rain, distant traffic", "fx": "", "dialogue": ""}}),
    (r"\b(portrait|face|woman|man|person|girl|boy|talks?|says|speaking|dialogue|interview)\b", {
        "lens": "85mm, f/2, shallow depth of field",
        "camera": "slow push-in at eye level",
        "light": "soft key from a window, gentle fill, subtle rim",
        "physics": "natural micro-movements: breathing, blinks, weight shifts; hair reacts to air"}),
    (r"\b(product|sneaker|shoe|bottle|watch|phone|perfume|turntable|packshot)\b", {
        "lens": "50mm, f/5.6, product in sharp focus",
        "camera": "slow 90-degree orbit on a turntable",
        "light": "studio softbox key, gradient backdrop, controlled specular highlights",
        "physics": "rigid object, consistent reflections as it rotates, no deformation",
        "sound": {"ambience": "", "fx": "soft whoosh on the reveal", "dialogue": ""}}),
    (r"\b(car|chase|race|run|running|sprint|motorbike|fast|speed)\b", {
        "lens": "35mm, f/4",
        "camera": "tracking shot alongside, then a whip pan to the front",
        "physics": "motion blur on the background, weight transfer in turns, dust and debris kicked up",
        "sound": {"ambience": "", "fx": "engine, tyres on gravel", "dialogue": ""}}),
    (r"\b(underwater|ocean|sea|jellyfish|fish|diver|reef)\b", {
        "lens": "16mm wide, f/4",
        "camera": "slow drift upward, slight roll",
        "light": "caustic light patterns from the surface, blue falloff with depth",
        "physics": "everything moves slowly with drag; bubbles rise; particles drift in the water column",
        "sound": {"ambience": "muffled underwater hum, bubbles", "fx": "", "dialogue": ""}}),
    (r"\b(timelapse|time-lapse|sunrise|sunset|dawn|dusk|golden hour)\b", {
        "light": "golden hour, low sun, long shadows, warm highlights with cool shadows",
        "physics": "shadows lengthen and shift; clouds move with the wind"}),
    (r"\b(city|street|crowd|market|subway|train)\b", {
        "lens": "35mm, f/2.8",
        "camera": "handheld follow, slight sway",
        "sound": {"ambience": "street noise, footsteps, distant voices", "fx": "", "dialogue": ""}}),
    (r"\b(sci-fi|spaceship|corridor|robot|cyberpunk|hologram)\b", {
        "light": "hard practical lights, volumetric haze, cold blue key with a single warm accent",
        "physics": "haze reacts to movement; metallic surfaces keep sharp reflections"}),
]

DEFAULT_NEGATIVE = ["morphing", "extra limbs", "warped hands", "flicker", "text", "watermark", "logo",
                    "jump cuts", "frame jitter"]


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def resolve_model(name):
    n = (name or "generic").lower().strip()
    n = ALIASES.get(n, n)
    if n not in MODELS:
        raise SystemExit("unknown model %r; known: %s" % (name, ", ".join(MODEL_ORDER)))
    return n


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def beat_grid(duration, step=2):
    """Beats of `step` seconds covering [0, duration]; the last beat absorbs the remainder."""
    n = max(1, int(math.ceil(duration / float(step))))
    beats = []
    for i in range(n):
        start = i * step
        end = duration if i == n - 1 else min(duration, (i + 1) * step)
        beats.append([start, end])
    return beats


def fmt_t(a, b):
    def f(x):
        return str(int(x)) if float(x).is_integer() else ("%.1f" % x)
    return "%s-%ss" % (f(a), f(b))


def wc(s):
    return len(s.split()) if s else 0


def end(s):
    """Trim and make sure the fragment ends a sentence (keeps a closing quote intact)."""
    s = (s or "").strip()
    if not s:
        return ""
    return s if s[-1] in ".!?\"'" else s + "."


def cap(s):
    return s[0].upper() + s[1:] if s else s


def beat_bodies(board):
    """[(action, camera)] with sentence punctuation applied."""
    return [(end(b.get("action", "")), end(b.get("camera", ""))) for b in board["beats"]]


def beats_sentences(board):
    out = []
    for b, (action, cam) in zip(board["beats"], beat_bodies(board)):
        t = fmt_t(b["t"][0], b["t"][1])
        out.append("%s: %s" % (t, " ".join(p for p in [cap(action), "Camera: " + cam if cam else ""] if p)))
    return out


def merged_beats(board, joiner="Then"):
    """Beats as one continuous description for single-shot models."""
    parts = []
    for i, (action, cam) in enumerate(beat_bodies(board)):
        s = cap(action) if i == 0 else "%s %s" % (joiner, action)
        if cam:
            s += " Camera: " + cam
        parts.append(s)
    return " ".join(parts)


# ---------------------------------------------------------------------------
# new
# ---------------------------------------------------------------------------
def cmd_new(a):
    idea = a.idea.strip()
    low = idea.lower()
    hints = {"lens": "", "camera": "", "light": "", "physics": "", "sound": None}
    for pattern, h in HINTS:
        if re.search(pattern, low):
            for k, v in h.items():
                if not hints.get(k):
                    hints[k] = v
    model = resolve_model(a.model)
    duration = a.duration
    grid = beat_grid(duration, a.beat)
    n = len(grid)
    beats = []
    for i, (s, e) in enumerate(grid):
        if i == 0:
            action = FILL + " establish the subject and the space; what is the first thing we see]]"
        elif i == n - 1:
            action = FILL + " resolve: the last gesture, the hold, or the reveal]]"
        else:
            action = FILL + " one clear change: a movement, a reaction, a reveal]]"
        beats.append({"t": [s, e], "action": action,
                      "camera": hints["camera"] if i == 0 else FILL + " continue, change or hold the move]]"})
    sound = hints["sound"] or {"ambience": FILL + " room tone or environment]]", "fx": "", "dialogue": ""}
    board = {
        "title": idea[:60],
        "idea": idea,
        "mode": a.mode,
        "duration_s": duration,
        "aspect": a.aspect,
        "model": model,
        "style": FILL + " film stock or grade, era, overall mood, e.g. 'Kodak 250D, muted teal shadows']]",
        "subject": FILL + " who or what, with 2-3 concrete visual details]]",
        "setting": FILL + " where and when, with one texture and one weather or light cue]]",
        "lens": hints["lens"] or FILL + " focal length, aperture, depth of field]]",
        "light": hints["light"] or FILL + " key, fill, rim, practicals; time of day]]",
        "beats": beats,
        "physics": hints["physics"] or FILL + " how things move: weight, drag, cloth, hair, liquid, particles]]",
        "sound": sound,
        "negative": list(DEFAULT_NEGATIVE),
        "image_ref": FILL + " describe the start frame and what must stay fixed]]" if a.mode == "i2v" else "",
        "notes": "",
    }
    text = json.dumps(board, indent=2, ensure_ascii=False) + "\n"
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote %s (%d beats, %ss, %s, %s)" % (a.out, n, duration, a.aspect, MODELS[model]["label"]))
        fills = text.count(FILL)
        print("%d [[fill: ...]] slots to complete, then: python3 scripts/storyboard.py check %s" % (fills, a.out))
    else:
        sys.stdout.write(text)


# ---------------------------------------------------------------------------
# check
# ---------------------------------------------------------------------------
REQUIRED = ["title", "idea", "mode", "duration_s", "aspect", "subject", "setting", "lens", "light", "beats",
            "physics", "sound", "negative"]


def check_board(board, model=None):
    """Return (errors, warnings). Errors are structural; warnings are model-fit problems."""
    errors, warns = [], []
    for k in REQUIRED:
        if k not in board:
            errors.append("missing field: %s" % k)
    if errors:
        return errors, warns
    raw = json.dumps(board, ensure_ascii=False)
    if FILL in raw:
        errors.append("%d unfilled [[fill: ...]] slot(s) remain" % raw.count(FILL))
    if board["mode"] not in ("t2v", "i2v"):
        errors.append("mode must be t2v or i2v, got %r" % board["mode"])
    d = board["duration_s"]
    if not isinstance(d, (int, float)) or d <= 0:
        errors.append("duration_s must be a positive number")
        return errors, warns
    beats = board["beats"]
    if not isinstance(beats, list) or not beats:
        errors.append("beats must be a non-empty list")
        return errors, warns
    expect = 0
    for i, b in enumerate(beats):
        t = b.get("t")
        if not (isinstance(t, list) and len(t) == 2):
            errors.append("beat %d: t must be [start, end]" % (i + 1))
            continue
        s, e = t
        if abs(s - expect) > 1e-6:
            errors.append("beat %d starts at %ss, expected %ss (beats must be contiguous)" % (i + 1, s, expect))
        if e <= s:
            errors.append("beat %d: end must be after start" % (i + 1))
        if e - s > 4:
            warns.append("beat %d is %ss long; beats over 4 s usually read as two events, split it" % (i + 1, e - s))
        if not b.get("action", "").strip():
            errors.append("beat %d: action is empty" % (i + 1))
        elif wc(b["action"]) > 45:
            warns.append("beat %d: action is %d words; models follow short, concrete beats better" % (i + 1, wc(b["action"])))
        expect = e
    if abs(expect - d) > 1e-6:
        errors.append("beats end at %ss but duration_s is %ss" % (expect, d))
    if board["mode"] == "i2v" and not board.get("image_ref", "").strip():
        errors.append("mode is i2v but image_ref is empty: describe the start frame")
    if not isinstance(board["negative"], list):
        errors.append("negative must be a list of short terms")
    else:
        for n in board["negative"]:
            if re.match(r"^\s*(no|not|don'?t|without|avoid)\b", n, re.I):
                warns.append("negative term %r: list the thing itself, not 'no thing' (models read the noun)" % n)
    s = board.get("sound")
    if s is not None and not isinstance(s, dict):
        errors.append("sound must be an object {ambience, fx, dialogue} or null")

    if model:
        m = MODELS[model]
        if d not in m["durations"]:
            near = min(m["durations"], key=lambda x: abs(x - d))
            warns.append("%s: %ss is not an available length (%s); nearest is %ss, re-time the beats" % (
                m["label"], d, durations_text(m), near))
        if board["aspect"] not in m["aspects"]:
            warns.append("%s: aspect %s not offered (%s)" % (m["label"], board["aspect"], ", ".join(m["aspects"])))
        if board["mode"] not in m["modes"]:
            warns.append("%s: mode %s not offered" % (m["label"], board["mode"]))
        has_sound = bool(s and any((s.get(k) or "").strip() for k in ("ambience", "fx", "dialogue")))
        if has_sound and m["audio"] == "none":
            warns.append("%s has no native audio: the sound block is dropped from the prompt, add audio in the edit" % m["label"])
        if (s or {}).get("dialogue", "").strip() and m["audio"] == "native" and model == "veo":
            warns.append("Veo tends to burn in subtitles when there is dialogue: 'subtitles, captions' are added to the negative field")
        if board["negative"] and m["negative"] == "none":
            warns.append("%s ignores negative prompts: the negative list is dropped, phrase what you want instead" % m["label"])
        cuts = [i + 1 for i, b in enumerate(beats)
                if re.search(r"\b(cut to|cut:|new angle|cuts? to|hard cut)\b", (b.get("camera", "") + " " + b.get("action", "")), re.I)]
        if cuts and not m["multishot"]:
            warns.append("%s is single-shot: beat %s asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually" % (
                m["label"], ", ".join(str(c) for c in cuts)))
        prompt = render(board, model)["prompt"]
        if m["prompt_max"] and len(prompt) > m["prompt_max"]:
            errors.append("%s: prompt is %d characters, limit is %d" % (m["label"], len(prompt), m["prompt_max"]))
        elif m["prompt_soft"] and len(prompt) > m["prompt_soft"]:
            warns.append("%s: prompt is %d characters; over ~%d the model starts ignoring detail" % (m["label"], len(prompt), m["prompt_soft"]))
        neg = render(board, model)["negative"]
        if neg and m["negative_max"] and len(neg) > m["negative_max"]:
            errors.append("%s: negative prompt is %d characters, limit is %d" % (m["label"], len(neg), m["negative_max"]))
    return errors, warns


def durations_text(m):
    ds = m["durations"]
    if len(ds) > 4 and ds == list(range(ds[0], ds[-1] + 1)):
        return "%d-%d s" % (ds[0], ds[-1])
    return "/".join(str(x) for x in ds) + " s"


def cmd_check(a):
    board = load(a.file)
    models = [resolve_model(a.model)] if a.model else ([resolve_model(board.get("model"))] if board.get("model") else [])
    errors, warns = check_board(board)
    for m in models:
        e2, w2 = check_board(board, m)
        errors += [x for x in e2 if x not in errors]
        warns += [x for x in w2 if x not in warns]
    name = os.path.basename(a.file)
    for e in errors:
        print("ERROR  %s: %s" % (name, e))
    for w in warns:
        print("WARN   %s: %s" % (name, w))
    if errors:
        print("%s: %d error(s), %d warning(s)" % (name, len(errors), len(warns)))
        return 1
    print("OK     %s: %d beats, %ss, %d warning(s)%s" % (
        name, len(board["beats"]), board["duration_s"], len(warns),
        " for " + ", ".join(MODELS[m]["label"] for m in models) if models else ""))
    return 0


# ---------------------------------------------------------------------------
# render
# ---------------------------------------------------------------------------
def sound_lines(board, model):
    s = board.get("sound") or {}
    amb, fx, dlg = (s.get("ambience") or "").strip(), (s.get("fx") or "").strip(), (s.get("dialogue") or "").strip()
    if not (amb or fx or dlg):
        return []
    if MODELS[model]["audio"] == "none":
        return []
    parts = []
    if amb:
        parts.append("Ambience: " + end(amb))
    if fx:
        parts.append("Sound effects: " + end(fx))
    if dlg:
        parts.append("Dialogue: " + end(dlg))
    return ["Audio. " + " ".join(parts)]


def render(board, model):
    """Return {prompt, negative, notes, label} for one model."""
    m = MODELS[model]
    style, lens, light = (cap(end(board.get(k, ""))) for k in ("style", "lens", "light"))
    look = " ".join(x for x in [style, lens, light] if x)
    subject = board["subject"].strip().rstrip(".")
    opener = cap(end("%s in %s" % (subject, board["setting"].strip()) if board.get("setting", "").strip() else subject))
    beats = beats_sentences(board)
    physics = ("Motion: " + end(board["physics"])) if board.get("physics", "").strip() else ""
    sound = sound_lines(board, model)
    neg_terms = list(board.get("negative") or [])
    notes = []
    image_line = ""
    if board["mode"] == "i2v" and board.get("image_ref", "").strip():
        image_line = "Start frame: " + end(board["image_ref"])

    if model == "kling":
        # Kling reads subject -> movement -> scene -> camera -> light; multi-shot via numbered beats.
        lines = [opener, look]
        if image_line:
            lines.append(image_line)
        lines += beats + [physics] + sound
        prompt = " ".join(x for x in lines if x)
        negative = ", ".join(neg_terms)
        notes.append("Paste the negative list into Kling's separate negative prompt field, not the prompt.")
        notes.append("Multi-shot: Kling 3.0 follows the timed beats as shots; for one continuous take, drop the timestamps.")
    elif model == "veo":
        # Veo: one continuous shot, audio described explicitly, dialogue quoted, negatives as nouns.
        lines = [opener, look]
        if image_line:
            lines.append(image_line)
        lines += ["One continuous take over %s seconds. %s" % (board["duration_s"], merged_beats(board)), physics] + sound
        prompt = " ".join(x for x in lines if x)
        dlg = (board.get("sound") or {}).get("dialogue", "")
        if dlg and dlg.strip():
            for t in ("subtitles", "captions"):
                if t not in neg_terms:
                    neg_terms.append(t)
        negative = ", ".join(neg_terms)
        notes.append("Put the negative list in the negativePrompt field as plain nouns; Veo ignores 'no X' inside the prompt.")
        notes.append("Dialogue goes in quotes with a speaker: Veo generates the voice and lip sync from it.")
    elif model == "wan":
        # Wan 2.5: 800-character prompt field, so be terse; audio is generated from the description.
        lines = [opener, lens, light]
        if image_line:
            lines.append(image_line)
        lines += [merged_beats(board), physics] + sound
        prompt = " ".join(x for x in lines if x)
        negative = ", ".join(neg_terms)
        notes.append("Prompt field is limited to 800 characters and the negative field to 500; the check command enforces both.")
    elif model == "seedance":
        # Seedance: numbered shots with explicit camera per shot; negatives inline as 'avoid'.
        shots = []
        for i, (b, (action, cam)) in enumerate(zip(board["beats"], beat_bodies(board))):
            t = fmt_t(b["t"][0], b["t"][1])
            shots.append("Shot %d (%s): %s%s" % (i + 1, t, cap(action), " Camera: " + cam if cam else ""))
        lines = [opener, look]
        if image_line:
            lines.append(image_line)
        lines += shots + [physics] + sound
        if neg_terms:
            lines.append("Avoid: %s." % ", ".join(neg_terms))
        prompt = " ".join(x for x in lines if x)
        negative = ""
        notes.append("Seedance has no separate negative field; the list is appended as an 'Avoid:' sentence.")
    elif model == "runway":
        # Runway: camera first, positive phrasing only, no negatives, no audio, under 1000 characters.
        first_cam = (board["beats"][0].get("camera") or "").strip().rstrip(".")
        lines = []
        if first_cam:
            lines.append(cap(first_cam) + ":")
        lines += [opener, merged_beats(board, joiner="Then"), physics, style]
        prompt = " ".join(x for x in lines if x)
        negative = ""
        notes.append("Runway reads positive phrasing only: the negative list is dropped, say what should be there instead.")
        notes.append("Gen-4 is image-to-video first: give it the start frame; Gen-4.5 also takes text only.")
        if board["mode"] == "i2v" and board.get("image_ref"):
            notes.append("Start frame: " + board["image_ref"])
    else:
        lines = [opener, look]
        if image_line:
            lines.append(image_line)
        lines += beats + [physics] + sound
        prompt = " ".join(x for x in lines if x)
        negative = ", ".join(neg_terms)
    prompt = re.sub(r"\s+", " ", prompt).strip()
    return {"prompt": prompt, "negative": negative, "notes": notes, "label": m["label"], "model": model}


def render_txt(board, model):
    r = render(board, model)
    out = ["# %s - %s (%ss, %s, %s)" % (board["title"], r["label"], board["duration_s"], board["aspect"], board["mode"]), "",
           r["prompt"]]
    if r["negative"]:
        out += ["", "NEGATIVE PROMPT:", r["negative"]]
    if r["notes"]:
        out += [""] + ["NOTE: " + n for n in r["notes"]]
    return "\n".join(out) + "\n"


def render_md(board, models):
    L = ["# %s" % board["title"], "",
         "> %s" % board["idea"], "",
         "| | |", "|---|---|",
         "| Mode | %s |" % ("text-to-video" if board["mode"] == "t2v" else "image-to-video"),
         "| Duration | %s s |" % board["duration_s"],
         "| Aspect | %s |" % board["aspect"],
         "| Lens | %s |" % board.get("lens", ""),
         "| Light | %s |" % board.get("light", ""),
         "| Style | %s |" % board.get("style", ""), ""]
    if board["mode"] == "i2v" and board.get("image_ref"):
        L += ["**Start frame.** %s" % board["image_ref"], ""]
    L += ["## Timeline", "", "| Time | Action | Camera |", "|---|---|---|"]
    for b in board["beats"]:
        L.append("| %s | %s | %s |" % (fmt_t(b["t"][0], b["t"][1]), b["action"], b.get("camera", "")))
    L += ["", "**Motion physics.** %s" % board.get("physics", ""), ""]
    s = board.get("sound") or {}
    labels = {"ambience": "Ambience", "fx": "Effects", "dialogue": "Dialogue"}
    if any((s.get(k) or "").strip() for k in labels):
        L += ["**Sound.** " + " ".join("%s: %s" % (labels[k], end(s[k])) for k in labels if (s.get(k) or "").strip()), ""]
    if board.get("negative"):
        L += ["**Negative.** " + ", ".join(board["negative"]), ""]
    if board.get("notes"):
        L += ["**Notes.** " + board["notes"], ""]
    L += ["## Prompts", ""]
    for model in models:
        r = render(board, model)
        m = MODELS[model]
        errors, warns = check_board(board, model)
        L += ["### %s" % r["label"], "", "```text", r["prompt"], "```", ""]
        if r["negative"]:
            L += ["Negative prompt field:", "", "```text", r["negative"], "```", ""]
        for n in r["notes"]:
            L.append("- %s" % n)
        for e in errors:
            L.append("- **Does not fit:** %s" % e)
        for w in warns:
            L.append("- Check: %s" % w)
        if m["uniqai"]:
            L.append("- [Run in UniqAI](%s): %s" % (m["uniqai"], m["uniqai_note"]))
        L.append("")
    L += ["---", "", "Rendered by `python3 scripts/storyboard.py render <board.json> --model %s --format md` (video-director %s)." % (
        "all" if models == MODEL_ORDER else ",".join(models), VERSION), ""]
    return "\n".join(L)


def cmd_render(a):
    board = load(a.file)
    if a.model == "all":
        models = list(MODEL_ORDER)
    elif a.model:
        models = [resolve_model(x) for x in a.model.split(",")]
    else:
        models = [resolve_model(board.get("model"))]
    if a.format == "md":
        text = render_md(board, models)
    else:
        text = "\n".join(render_txt(board, m) for m in models)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("wrote %s" % a.out)
    else:
        sys.stdout.write(text)
    return 0


# ---------------------------------------------------------------------------
# models / vocab
# ---------------------------------------------------------------------------
def cmd_models(a):
    rows = [("model", "label", "lengths", "aspects", "audio", "prompt cap", "negatives", "shots")]
    for k in MODEL_ORDER:
        m = MODELS[k]
        cap = "%d chars" % m["prompt_max"] if m["prompt_max"] else ("~%d soft" % m["prompt_soft"] if m["prompt_soft"] else "-")
        rows.append((k, m["label"], durations_text(m), " ".join(m["aspects"]), m["audio"], cap, m["negative"],
                     "multi" if m["multishot"] else "single"))
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    for i, r in enumerate(rows):
        print("  ".join(c.ljust(widths[j]) for j, c in enumerate(r)).rstrip())
        if i == 0:
            print("  ".join("-" * w for w in widths))
    print("\nchecked on %s against vendor docs; sources in references/model-notes.md" % CHECKED_ON)
    return 0


VOCAB_FILES = {"camera": "camera-moves.md", "lens": "lenses.md", "light": "lighting.md",
               "physics": "motion-physics.md", "sound": "sound-design.md", "negative": "negative-prompts.md"}


def read_tables(path):
    """Yield (cells) for every data row of every Markdown table in the file."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            yield cells


def cmd_vocab(a):
    fn = VOCAB_FILES.get(a.topic)
    if not fn:
        raise SystemExit("topic must be one of: " + ", ".join(VOCAB_FILES))
    rows = list(read_tables(os.path.join(REFS, fn)))
    header, data = rows[0], rows[1:]
    q = (a.query or "").lower()
    hits = [r for r in data if not q or q in " ".join(r).lower()]
    for r in hits:
        print(" | ".join(r))
    print("\n%d of %d entries from references/%s" % (len(hits), len(data), fn))
    return 0


# ---------------------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(prog="storyboard.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version="video-director " + VERSION)
    sp = p.add_subparsers(dest="cmd")
    n = sp.add_parser("new", help="scaffold a storyboard JSON from a one-line idea")
    n.add_argument("--idea", required=True)
    n.add_argument("--duration", type=int, default=8, help="seconds (default 8)")
    n.add_argument("--beat", type=int, default=2, help="seconds per beat (default 2)")
    n.add_argument("--mode", choices=["t2v", "i2v"], default="t2v")
    n.add_argument("--aspect", default="16:9")
    n.add_argument("--model", default="generic", help="target model: " + ", ".join(MODEL_ORDER))
    n.add_argument("-o", "--out")
    c = sp.add_parser("check", help="validate structure and fit for the target model")
    c.add_argument("file")
    c.add_argument("--model")
    r = sp.add_parser("render", help="format the storyboard as a prompt for one or more models")
    r.add_argument("file")
    r.add_argument("--model", help="kling, veo, wan, seedance, runway, generic, a comma list, or all")
    r.add_argument("--format", choices=["txt", "md"], default="txt")
    r.add_argument("-o", "--out")
    sp.add_parser("models", help="print the model limits table")
    v = sp.add_parser("vocab", help="look up cinematography vocabulary from references/")
    v.add_argument("topic", help=", ".join(VOCAB_FILES))
    v.add_argument("query", nargs="?")
    a = p.parse_args(argv)
    if not a.cmd:
        p.print_help()
        return 0
    return {"new": cmd_new, "check": cmd_check, "render": cmd_render, "models": cmd_models, "vocab": cmd_vocab}[a.cmd](a) or 0


if __name__ == "__main__":
    sys.exit(main())
