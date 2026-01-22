#!/usr/bin/env python3
"""
Tracklist Formatter Script

Converts raw tracklist (artist - title) into YouTube-formatted tracklist with timestamps.

Usage:
    python tracklist_formatter.py input.txt output.txt

Input format (one track per line):
    Artist — Track Title
    Artist — Track Title

Output format:
    00:00 Artist — Track Title
    04:23 Artist — Track Title

You'll be prompted to enter the duration of each track.
"""

import sys
import re


def parse_time(time_str):
    """Convert MM:SS or M:SS to total seconds."""
    parts = time_str.split(':')
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    return 0


def format_time(seconds):
    """Convert seconds to MM:SS format."""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


def main():
    if len(sys.argv) != 3:
        print("Usage: python tracklist_formatter.py input.txt output.txt")
        print("\nInput file should have one track per line: Artist — Track Title")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            tracks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    print(f"Found {len(tracks)} tracks.\n")

    # Get track durations
    durations = []
    for i, track in enumerate(tracks, 1):
        while True:
            duration_input = input(f"Track {i} duration (MM:SS): ").strip()
            if re.match(r'^\d{1,2}:\d{2}$', duration_input):
                durations.append(parse_time(duration_input))
                break
            else:
                print("Invalid format. Use MM:SS (e.g., 4:23)")

    # Calculate timestamps
    timestamps = [0]
    for duration in durations[:-1]:
        timestamps.append(timestamps[-1] + duration)

    # Format output
    formatted_tracks = []
    for timestamp, track in zip(timestamps, tracks):
        formatted_tracks.append(f"{format_time(timestamp)} {track}")

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(formatted_tracks))

    print(f"\n✅ Formatted tracklist saved to '{output_file}'")
    print(f"\nTotal mix duration: {format_time(sum(durations))}")


if __name__ == "__main__":
    main()
