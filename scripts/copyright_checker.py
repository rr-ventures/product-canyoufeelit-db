#!/usr/bin/env python3
"""
Copyright Checker

Flag tracks with high copyright risk before uploading mixes to YouTube.

Usage:
    python scripts/copyright_checker.py [tracklist_file.txt]

If no file provided, will check against Rekordbox library in data/rekordbox_library.json
"""

import sys
import json
from pathlib import Path


def load_rekordbox_library():
    """Load Rekordbox library from JSON file."""
    library_path = Path('data/rekordbox_library.json')
    
    if not library_path.exists():
        print("Warning: Rekordbox library not found. Run rekordbox_parser.py first.")
        return []
    
    with open(library_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_copyright_risk(track):
    """
    Check if a track has copyright risk indicators.
    
    Returns a risk level: 'low', 'medium', 'high'
    """
    # Placeholder logic - to be implemented with actual copyright API
    # (AudD or ACRCloud integration)
    
    title = track.get('title', '').lower()
    artist = track.get('artist', '').lower()
    
    # High-risk indicators (major labels, popular artists)
    high_risk_keywords = ['sony', 'warner', 'universal', 'emi', 'atlantic']
    
    # Medium-risk indicators
    medium_risk_keywords = ['remix', 'bootleg', 'mashup']
    
    for keyword in high_risk_keywords:
        if keyword in title or keyword in artist:
            return 'high'
    
    for keyword in medium_risk_keywords:
        if keyword in title:
            return 'medium'
    
    return 'low'


def main():
    tracks_to_check = []
    
    if len(sys.argv) > 1:
        # Check specific tracklist file
        tracklist_path = sys.argv[1]
        if not Path(tracklist_path).exists():
            print(f"Error: File '{tracklist_path}' not found.")
            sys.exit(1)
        
        with open(tracklist_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and '—' in line:
                    parts = line.split('—', 1)
                    tracks_to_check.append({
                        'artist': parts[0].strip(),
                        'title': parts[1].strip() if len(parts) > 1 else ''
                    })
    else:
        # Check entire Rekordbox library
        tracks_to_check = load_rekordbox_library()
    
    if not tracks_to_check:
        print("No tracks to check.")
        sys.exit(0)
    
    print(f"Checking {len(tracks_to_check)} tracks for copyright risk...\n")
    
    risky_tracks = {
        'high': [],
        'medium': [],
        'low': []
    }
    
    for track in tracks_to_check:
        risk = check_copyright_risk(track)
        risky_tracks[risk].append({
            'artist': track.get('artist', 'Unknown'),
            'title': track.get('title', 'Unknown'),
            'risk': risk
        })
    
    # Print results
    if risky_tracks['high']:
        print("⚠️  HIGH RISK TRACKS:")
        for track in risky_tracks['high']:
            print(f"  - {track['artist']} — {track['title']}")
        print()
    
    if risky_tracks['medium']:
        print("⚠️  MEDIUM RISK TRACKS:")
        for track in risky_tracks['medium']:
            print(f"  - {track['artist']} — {track['title']}")
        print()
    
    print(f"✅ Low risk: {len(risky_tracks['low'])} tracks")
    print(f"⚠️  Medium risk: {len(risky_tracks['medium'])} tracks")
    print(f"🚨 High risk: {len(risky_tracks['high'])} tracks")
    
    if risky_tracks['high']:
        print("\n⚠️  WARNING: High-risk tracks detected. Consider removing before upload.")


if __name__ == "__main__":
    main()
