# Setup

This repo is meant to be run inside a Dev Container.

## Quick start
1. Install Docker
2. Install VS Code + Dev Containers extension
3. Open repo → "Reopen in Container"

## What's included
- A consistent dev environment
- Docker runtime support
- Python 3 with pip
- Node.js and npm
- Space for docs and screenshots

## Python Dependencies

After opening in container, dependencies are automatically installed. To manually install:

```bash
pip install -r requirements.txt
```

## DJ Library Management Setup

### Rekordbox Integration
1. Export your Rekordbox library to XML (File → Export Collection in Rekordbox)
2. Use scripts in `/scripts/` folder to process the XML
3. Converted data will be stored in `/data/` folder

### Quick Start for Mixing Library Features
1. Export Rekordbox library to XML
2. `pip install -r requirements.txt`
3. `python scripts/rekordbox_parser.py path/to/rekordbox.xml` (when implemented)
4. Explore converted JSON data in `/data/rekordbox_library.json`
