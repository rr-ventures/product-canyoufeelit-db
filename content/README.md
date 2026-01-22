# Content — Mix Planning & Tracklists

Store all mix-related content here: themes, tracklists, metadata, retrospectives.

---

## Folder Purpose

This is your content library. Every mix you create should have its own set of files here.

---

## File Naming Convention

### Per Mix:
- `mix-[XX]-theme.txt` — One-line theme description
- `mix-[XX]-tracklist.md` — Full tracklist with timestamps
- `mix-[XX]-metadata.txt` — Title, description, tags (ready to copy/paste into YouTube)
- `mix-[XX]-pinned-comment.txt` — Pinned comment text
- `mix-[XX]-notes.md` — Personal notes (what worked, what didn't, copyright claims)
- `mix-[XX]-retrospective.md` — Post-upload reflection (learnings, analytics)

### Example for Mix 1:
```
mix-01-theme.txt
mix-01-tracklist.md
mix-01-metadata.txt
mix-01-pinned-comment.txt
mix-01-notes.md
mix-01-retrospective.md
```

---

## Mix Planning Workflow

1. **Brainstorm theme** → Save in `mix-[XX]-theme.txt`
2. **Curate tracks** → Build list in `mix-[XX]-tracklist.md`
3. **Record mix** → Note any issues in `mix-[XX]-notes.md`
4. **Generate metadata** → Run `scripts/metadata_template.py` or manually create `mix-[XX]-metadata.txt`
5. **Upload to YouTube** → Copy/paste from metadata file
6. **Post pinned comment** → Copy from `mix-[XX]-pinned-comment.txt`
7. **Track performance** → After 1 week, fill out `mix-[XX]-retrospective.md`

---

## Tracklist Template

```markdown
# Mix [XX]: [Theme Name]

**Theme**: [One sentence describing the emotional vibe]

**Duration**: [XX min]

**Recorded**: [Date]

---

## Tracklist

00:00 Artist — Track Title
04:23 Artist — Track Title
08:45 Artist — Track Title
...

---

## Notes

[Any notes about track selection, transitions, or production]
```

---

## Other Files to Store Here

- `mix-ideas.md` — Backlog of future mix themes
- `track-inbox.md` — Songs you want to use but haven't placed yet
- `email-calendar.md` — Plan for upcoming newsletters
- `newsletters/` — Archive of sent emails (create subfolder if needed)

---

## Tips

- **One file per mix** — Don't cram everything into one giant doc
- **Date your retrospectives** — So you can see progress over time
- **Track copyright claims** — Note which tracks/labels caused claims in `mix-[XX]-notes.md`
- **Save raw tracklists** — Before formatting with timestamps (easier to edit)

---

## Next Steps

1. Create `mix-01-theme.txt` with your first mix theme
2. Start curating tracks into `mix-01-tracklist.md`
3. Follow the workflow above for each mix
