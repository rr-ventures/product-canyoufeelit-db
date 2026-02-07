#!/usr/bin/env python3
"""
Rekordbox XML Parser

Parse Rekordbox library XML export and convert to JSON format.

Usage:
    python scripts/rekordbox_parser.py path/to/rekordbox.xml

Output:
    Saves converted data to data/rekordbox_library.json
"""

import sys
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_rekordbox_xml(xml_path):
    """
    Parse Rekordbox XML export and extract track metadata.
    
    Returns a list of track dictionaries with metadata.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    tracks = []
    
    # Rekordbox XML structure: COLLECTION > TRACK elements
    for track_elem in root.findall('.//TRACK'):
        track = {
            'title': track_elem.get('Name', ''),
            'artist': track_elem.get('Artist', ''),
            'album': track_elem.get('Album', ''),
            'genre': track_elem.get('Genre', ''),
            'bpm': track_elem.get('AverageBpm', ''),
            'key': track_elem.get('Tonality', ''),
            'rating': track_elem.get('Rating', ''),
            'date_added': track_elem.get('DateAdded', ''),
            'play_count': track_elem.get('PlayCount', '0'),
            'file_path': track_elem.get('Location', ''),
        }
        tracks.append(track)
    
    return tracks


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/rekordbox_parser.py path/to/rekordbox.xml")
        sys.exit(1)
    
    xml_path = sys.argv[1]
    
    if not Path(xml_path).exists():
        print(f"Error: File '{xml_path}' not found.")
        sys.exit(1)
    
    print(f"Parsing Rekordbox XML: {xml_path}")
    
    try:
        tracks = parse_rekordbox_xml(xml_path)
        print(f"Found {len(tracks)} tracks.")
        
        # Create data directory if it doesn't exist
        data_dir = Path('data')
        data_dir.mkdir(exist_ok=True)
        
        # Save to JSON
        output_path = data_dir / 'rekordbox_library.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(tracks, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Converted data saved to '{output_path}'")
        
    except ET.ParseError as e:
        print(f"Error: Invalid XML file. {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
