# CanYouFeelIt DB

**Complete system for trip-hop/lofi YouTube mix channel production, distribution, and DJ library management.**

This repository combines:
- **YouTube channel workflow** - Mix production, uploads, audience building
- **DJ library management** - Rekordbox integration, tracklist generation, copyright flagging
- **Content systems** - Templates, scripts, workflows for consistent production

---

## What This Does

### YouTube Channel Management
- Mix production workflows and checklists
- Title/description templates
- Newsletter and audience funnel systems
- Distribution strategy and competitor analysis

### DJ Library Management
- **Copyright flagging** - Detect risky tracks before uploading mixes to YouTube
- **Tracklist generation** - Auto-generate tracklists from mixes
- **Rekordbox integration** - Read and sync with Rekordbox library
- **Inbox processing** - Organize new music downloads
- **Mix database** - Store mixes, tracks, YouTube metadata
- **Prompt storage** - Save prompts/scripts related to YouTube channel

---

## Quick Start

### For YouTube Channel Workflow
See **[QUICKSTART.md](./QUICKSTART.md)** for the 7-day plan to upload Mix 1.

### For DJ Library Management
1. Export Rekordbox library to XML
2. `pip install -r requirements.txt`
3. Use scripts in `/scripts/` folder:
   - `tracklist_formatter.py` - Format tracklists with timestamps
   - `metadata_template.py` - Generate YouTube upload metadata
   - (Coming soon: `rekordbox_parser.py`, `copyright_checker.py`)

---

## Project Structure

```
/assets/          → Logos, thumbnails, banners
/backlog/         → Prioritized task lists + mixing library backlog
/content/         → Mix planning, tracklists, metadata per mix
/data/            → Rekordbox library JSON, mix metadata, tracklists
/docs/            → Setup instructions, documentation
/research/        → Competitor analysis, distribution experiments
/scripts/         → Python automation tools
/templates/       → Copy/paste templates for titles, descriptions, emails
/workflows/       → SOPs, checklists, rollout plans
```

---

## Features

### YouTube Channel
1. 14-day launch plan
2. Upload checklists
3. Title/description templates
4. Newsletter templates
5. Audience funnel workflows
6. Distribution strategy guides

### DJ Library Management
1. Parse Rekordbox XML exports
2. Flag tracks with copyright risk
3. Generate formatted tracklists
4. Store mix metadata
5. Track YouTube performance
6. Organize music files

---

## Tech Stack

- **Python** - Core processing and automation scripts
- **Rekordbox XML** - Library source of truth
- **JSON files** - Converted data storage
- **Docker/Dev Containers** - Consistent development environment

---

## Setup

This repo is meant to be run inside a Dev Container.

### Quick start
1. Install Docker
2. Install VS Code + Dev Containers extension
3. Open repo → "Reopen in Container"

See `docs/setup.md` for detailed setup instructions.

---

## Key Documents

- **[QUICKSTART.md](./QUICKSTART.md)** - Start here. 7-day plan to upload Mix 1.
- **[PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)** - Complete project overview
- **[BRAND_MANIFESTO.md](./BRAND_MANIFESTO.md)** - Why this exists. Your North Star.
- **[backlog/prioritized-tasks.md](./backlog/prioritized-tasks.md)** - P0/P1/P2 task lists
- **[backlog/mixing-library-backlog.md](./backlog/mixing-library-backlog.md)** - DJ library management features

---

## Philosophy

**Momentum over perfection** — Ship first, polish later.

The goal is not to build the perfect system. The goal is to ship Mix 1. Everything else is noise until you've uploaded your first video.
