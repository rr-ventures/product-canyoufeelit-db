#!/usr/bin/env python3
"""
YouTube Metadata Template Generator

Generates title, description, and filename for a mix based on user input.

Usage:
    python metadata_template.py

Interactive prompts will guide you through the process.
Outputs a text file with complete upload metadata.
"""

import os
from datetime import datetime


def main():
    print("=" * 50)
    print("YouTube Mix Metadata Generator")
    print("=" * 50)
    print()

    # Get inputs
    mix_number = input("Mix number (e.g., 01, 02): ").strip()
    emotion = input("Emotion/state (e.g., 'when you finally let go'): ").strip().lower()
    genre = input("Genre/vibe (e.g., 'trip hop mix', 'lofi beats'): ").strip().lower()
    duration = input("Mix duration (e.g., 25min, 30min): ").strip()

    print("\nEmotional hook (1-2 sentences describing the vibe):")
    hook = input("> ").strip()

    tracklist_file = input("\nTracklist file path (or press Enter to add manually later): ").strip()

    landing_page = input("Landing page URL: ").strip()
    discord_link = input("Discord invite URL: ").strip()

    # Generate title
    title = f"{emotion} | {genre}"

    # Generate filename
    safe_emotion = emotion.replace(' ', '_').replace('|', '').replace('/', '')
    filename = f"CYFI_Mix{mix_number}_{safe_emotion}_Final"

    # Load tracklist if provided
    tracklist = "[Paste formatted tracklist here]"
    if tracklist_file and os.path.exists(tracklist_file):
        with open(tracklist_file, 'r', encoding='utf-8') as f:
            tracklist = f.read().strip()

    # Generate description
    description = f"""{hook}

This is a {duration} trip hop mix for {emotion.replace('when ', '').replace('the ', '')}. Real DJ craft. Real tracks. No filler.

🎧 TRACKLIST
{tracklist}

---

💌 Join the list for weekly track finds + meaning (no spam):
{landing_page}

💬 Discord for people who feel it:
{discord_link}

---

ABOUT CAN YOU FEEL IT

We're building a catalog of mixes that don't just sound good—they land. For late nights, deep feelings, and the moments when you need music that gets it.

This isn't background noise. It's resonance.

---

#triphop #lofi #chillmusic #latenightvibes #emotionalbeats
"""

    # Generate pinned comment
    pinned_comment = f"""If this mix resonates with you, there's more where it came from.

💌 Weekly track finds + meaning (no spam): {landing_page}
💬 Discord for people who get it: {discord_link}

New mixes every fortnight. This is just the beginning.

What track hit different for you? 👇"""

    # Create output
    output = f"""=============================================
MIX METADATA - Mix {mix_number}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
=============================================

FILENAME:
{filename}.mp3

TITLE (Character count: {len(title)}):
{title}

DESCRIPTION:
{description}

PINNED COMMENT:
{pinned_comment}

TAGS (copy/paste into YouTube):
trip hop mix, lofi mix, chill music, late night music, emotional mix, can you feel it, downtempo, ambient hip hop, nostalgic mix, melancholic beats

THUMBNAIL FILENAME:
{filename}_thumb.png

=============================================
"""

    # Save to file
    output_filename = f"mix{mix_number}_metadata.txt"
    output_path = os.path.join('content', output_filename)

    os.makedirs('content', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n✅ Metadata saved to '{output_path}'")
    print("\nNext steps:")
    print("1. Copy metadata from the file when uploading to YouTube")
    print("2. Double-check tracklist formatting")
    print("3. Review title character count (aim for <70)")


if __name__ == "__main__":
    main()
