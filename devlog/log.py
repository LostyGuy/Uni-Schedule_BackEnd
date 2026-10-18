#!/usr/bin/env python3
"""
CLI helper to quickly append entries to devlog/entries.js

Usage:
    python devlog/log.py "Fixed collision test" -t tests,schedule -s passed -b "14/14 Passed" --target "test_schedule.py"
"""

import os
import sys
import json
import re
import argparse
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ENTRIES_FILE = os.path.join(os.path.dirname(__file__), "entries.js")

def add_entry(title, status="passed", badge="", tags=None, target="", notes="", terminal=""):
    if not os.path.exists(ENTRIES_FILE):
        print(f"Error: {ENTRIES_FILE} not found!")
        sys.exit(1)

    today = date.today().isoformat()
    tags_list = [t.strip().lstrip("#") for t in (tags or "").split(",") if t.strip()]

    badge_default = "Passed ✅" if status == "passed" else status.upper()

    new_item = {
        "date": today,
        "title": title,
        "status": status,
        "badge": badge or badge_default,
        "tags": tags_list or ["general"],
        "open": True,
        "target": target,
        "bullets": [n.strip() for n in notes.split(";") if n.strip()] if notes else [title],
        "terminal": terminal
    }

    with open(ENTRIES_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Match: const ENTRIES = [ ... ];
    match = re.search(r"const\s+ENTRIES\s*=\s*(\[[\s\S]*?\])\s*;", content)
    if not match:
        print("Could not find `const ENTRIES = [...]` in entries.js")
        sys.exit(1)

    try:
        entries_json_str = match.group(1)
        # Parse loosely or load
        # Since entries.js might have comments or trailing commas, we can prepend safely
        new_entry_formatted = json.dumps(new_item, indent=2)
        # Indent it nicely
        indented = "  " + new_entry_formatted.replace("\n", "\n  ") + ",\n"

        # Insert right after the opening bracket '['
        bracket_pos = content.find("const ENTRIES = [")
        if bracket_pos != -1:
            insert_point = bracket_pos + len("const ENTRIES = [")
            new_content = content[:insert_point] + "\n" + indented + content[insert_point:]

            with open(ENTRIES_FILE, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"✅ Successfully added entry: '{title}' to devlog/entries.js")
            try:
                from sync_readme import sync_readme
                sync_readme(max_count=3)
            except Exception as sync_err:
                print(f"Note: Could not auto-sync README.md: {sync_err}")
        else:
            print("Failed to locate insertion point in entries.js")
    except Exception as e:
        print(f"Error updating entries.js: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quickly append a devlog entry.")
    parser.add_argument("title", help="Headline for the dev diary entry")
    parser.add_argument("-s", "--status", default="passed", choices=["passed", "wip", "refactor", "bugfix", "feature"], help="Entry status")
    parser.add_argument("-b", "--badge", default="", help="Short badge label (e.g. '14/14 Passed')")
    parser.add_argument("-t", "--tags", default="tests,backend", help="Comma-separated tags (e.g. tests,backend,auth)")
    parser.add_argument("--target", default="", help="Specific file or test targeted")
    parser.add_argument("-n", "--notes", default="", help="Semicolon-separated notes/bullet points")
    parser.add_argument("--terminal", default="", help="Terminal command or output snippet")

    args = parser.parse_args()
    add_entry(args.title, args.status, args.badge, args.tags, args.target, args.notes, args.terminal)
