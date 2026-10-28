## What changed

## How to test

```bash
python3 tests/run.py
```

If an example changed, re-render it so the committed `.md` matches:
`python3 scripts/storyboard.py render examples/<name>.json --model all --format md -o examples/<name>.md`

## Honesty check

- [ ] Any new numbers (model limits, lengths) have a source URL and a check date in `references/model-notes.md`
- [ ] No personal names or secrets added
- [ ] `SKILL.md` is still under 500 lines
