#!/usr/bin/env python3
"""Stop hook for Ask EA hook telemetry snapshots."""

from __future__ import annotations

import json

from ask_ea_hook_lib import HOOK_EVENTS_FILE, append_hook_event, write_telemetry


def read_recent_events(limit: int = 30) -> list[dict]:
    if not HOOK_EVENTS_FILE.exists():
        return []
    events: list[dict] = []
    for line in HOOK_EVENTS_FILE.read_text(encoding="utf-8").splitlines()[-limit:]:
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def main() -> int:
    recent = read_recent_events()
    touched = []
    seen = set()
    warnings = 0
    for event in recent:
        skill_id = event.get("skill_id")
        if skill_id and skill_id not in seen:
            seen.add(skill_id)
            touched.append(skill_id)
        if event.get("validation_status") == "warning":
            warnings += 1

    snapshot = {
        "recent_event_count": len(recent),
        "touched_skills": touched,
        "warning_count": warnings,
    }
    write_telemetry("ask-ea-stop.json", snapshot)
    append_hook_event(
        {
            "hook_event": "stop",
            "kind": "session_snapshot",
            "touched_skills": touched,
            "warning_count": warnings,
        }
    )
    if touched:
        print("[Ask EA hooks] Session touched core skills: " + ", ".join(touched))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
