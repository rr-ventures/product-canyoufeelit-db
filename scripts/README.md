# Scripts — Automation Tools

These scripts save time on repetitive tasks. They're optional but helpful once you're past Mix 1.

---

## Available Scripts

### 1. `tracklist_formatter.py`
**Purpose**: Converts raw tracklist into YouTube-formatted tracklist with timestamps.

**Input**: Text file with one track per line (`Artist — Track Title`)

**Output**: Formatted tracklist with timestamps (`00:00 Artist — Track Title`)

**Usage**:
```bash
python scripts/tracklist_formatter.py input.txt output.txt
```

You'll be prompted to enter each track's duration (MM:SS format).

**When to use**: After finalizing your mix tracklist, before writing the YouTube description.

---

### 2. `metadata_template.py`
**Purpose**: Generates complete upload metadata (title, description, filename, pinned comment).

**Input**: Interactive prompts (mix number, emotion, genre, etc.)

**Output**: Text file with all metadata ready to copy/paste into YouTube.

**Usage**:
```bash
python scripts/metadata_template.py
```

Follow the prompts. Script saves output to `/content/mix[XX]_metadata.txt`.

**When to use**: After recording your mix, before uploading to YouTube.

---

## Setup (First Time Only)

These scripts use Python 3 (no external dependencies needed).

**Check if you have Python installed**:
```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/).

---

## Tips

- Run scripts from the project root directory (`C:\code\product-canyoufeelit-db\`)
- Keep input files (raw tracklists) in `/content/` folder
- Scripts are designed to be simple—modify them if you need different formats
- If a script saves time on 3+ mixes, it's worth using. If not, skip it.

---

## Future Script Ideas (Backlog)

- **Thumbnail generator**: Auto-generate text-based thumbnails with consistent styling
- **Distribution poster**: Auto-post to Reddit/Discord with formatted text
- **Analytics scraper**: Pull YouTube stats weekly and save to spreadsheet
- **Copyright checker**: Flag tracks that have been claimed in previous mixes

Add these only if the manual process becomes a genuine bottleneck.
