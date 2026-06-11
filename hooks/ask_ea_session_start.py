#!/usr/bin/env python3
"""SessionStart hook for Ask EA skill operations."""

from __future__ import annotations

from ask_ea_hook_lib import (
    active_core_skills,
    append_hook_event,
    collect_health,
    discover_skills,
    lowest_scored_skill,
    write_telemetry,
)


def main() -> int:
    skills = discover_skills()
    active_count = sum(1 for skill in skills if skill["active"])
    health = collect_health()
    lowest = lowest_scored_skill()
    core_skills = active_core_skills()

    summary = {
        "skill_count": len(skills),
        "active_count": active_count,
        "core_skill_count": len(core_skills),
        "core_skills": core_skills,
        "health": health,
        "lowest_scored_skill": lowest,
    }
    write_telemetry("ask-ea-session-start.json", summary)
    append_hook_event(
        {
            "hook_event": "session_start",
            "kind": "catalog",
            "core_skills": [skill["skill_id"] for skill in core_skills],
            "health": health,
        }
    )

    message = (
        f"[Ask EA hooks] {len(skills)} EA skill files detected "
        f"({active_count} active, {len(core_skills)} core process hooks monitored). "
        "Use `.claude/skills/ask-ea-skill-ops/SKILL.md` when working on skill "
        "routing, quality, lifecycle, or demo readiness."
    )
    print(message)

    if core_skills:
        print(
            "[Ask EA hooks] Core processes: "
            + ", ".join(skill["label"] for skill in core_skills[:6])
            + ("..." if len(core_skills) > 6 else "")
        )

    if lowest:
        print(
            "[Ask EA hooks] Lowest live score: "
            f"{lowest.get('name', lowest.get('skill_id'))} "
            f"{lowest.get('avg')}/5 across {lowest.get('count', 0)} evals."
        )

    print(
        "[Ask EA hooks] Health: "
        + ", ".join(f"{name}={status}" for name, status in health.items())
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
