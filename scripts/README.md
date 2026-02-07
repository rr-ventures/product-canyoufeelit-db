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

### 3. `rekordbox_parser.py` (Coming Soon)
**Purpose**: Parse Rekordbox XML exports and convert to JSON format.

**Input**: Rekordbox XML export file

**Output**: JSON file with track metadata (title, artist, genre, BPM, key, rating, etc.)

**Usage**:
```bash
python scripts/rekordbox_parser.py path/to/rekordbox.xml
```

**When to use**: After exporting your Rekordbox library, to convert it to a usable format.

---

### 4. `copyright_checker.py` (Coming Soon)
**Purpose**: Flag tracks with high copyright risk before uploading mixes.

**Input**: Track list or Rekordbox library data

**Output**: List of risky tracks with risk levels

**When to use**: Before finalizing a mix tracklist, to avoid copyright issues on YouTube.

---

### 5. `tracklist_generator.py` (Coming Soon)
**Purpose**: Auto-generate tracklists from Rekordbox playlists or mix files.

**Input**: Rekordbox playlist or mix file

**Output**: Formatted tracklist ready for YouTube description

**When to use**: After recording a mix, to quickly generate the tracklist.

---

### 6. `inbox_processor.py` (Coming Soon)
**Purpose**: Organize new music downloads and suggest playlists.

**Input**: Folder of new music files

**Output**: Organized files with metadata suggestions

**When to use**: After downloading new tracks, to organize and tag them.

---

## Future Script Ideas (Backlog)

- **Thumbnail generator**: Auto-generate text-based thumbnails with consistent styling
- **Distribution poster**: Auto-post to Reddit/Discord with formatted text
- **Analytics scraper**: Pull YouTube stats weekly and save to spreadsheet

Add these only if the manual process becomes a genuine bottleneck.
