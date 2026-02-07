#!/usr/bin/env python3
"""
Tracklist Generator

Auto-generate tracklists from Rekordbox playlists or mix files.

Usage:
    python scripts/tracklist_generator.py [playlist_name] [output_file.txt]

If no playlist name provided, will list available playlists.
"""

import sys
import json
from pathlib import Path


def load_rekordbox_library():
    """Load Rekordbox library from JSON file."""
    library_path = Path('data/rekordbox_library.json')
    
    if not library_path.exists():
        print("Error: Rekordbox library not found. Run rekordbox_parser.py first.")
        sys.exit(1)
    
    with open(library_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def list_playlists():
    """List available playlists from Rekordbox library."""
    # Placeholder - would need to parse playlist data from XML
    print("Playlist listing not yet implemented.")
    print("This feature requires parsing playlist data from Rekordbox XML.")


def generate_tracklist(playlist_name, output_file):
    """
    Generate a formatted tracklist from a Rekordbox playlist.
    
    Output format: Artist — Track Title
    """
    library = load_rekordbox_library()
    
    # Placeholder - would filter by playlist name
    # For now, just format all tracks
    print(f"Generating tracklist for playlist: {playlist_name}")
    print("Note: Playlist filtering not yet implemented. Using all tracks.")
    
    tracklist = []
    for track in library:
        artist = track.get('artist', 'Unknown')
        title = track.get('title', 'Unknown')
        tracklist.append(f"{artist} — {title}")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(tracklist))
    
    print(f"✅ Tracklist saved to '{output_file}'")
    print(f"   {len(tracklist)} tracks")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/tracklist_generator.py [playlist_name] [output_file.txt]")
        print("\nAvailable playlists:")
        list_playlists()
        sys.exit(1)
    
    playlist_name = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else f"{playlist_name}_tracklist.txt"
    
    generate_tracklist(playlist_name, output_file)


if __name__ == "__main__":
    main()
