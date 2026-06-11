#!/usr/bin/env python3
"""PostToolUse hook for Ask EA skill validation."""

from __future__ import annotations

from ask_ea_hook_lib import (
    append_hook_event,
    collect_health,
    core_skill_metadata,
    extract_skill_paths,
    lowest_scored_skill,
    process_specific_issues,
    read_hook_payload,
    repo_relative,
    skill_id_for_path,
    validate_skill_file,
    write_telemetry,
)


def main() -> int:
    payload = read_hook_payload()
    skill_paths = extract_skill_paths(payload)
    if not skill_paths:
        return 0

    lowest = lowest_scored_skill()
    health = collect_health()
    results: list[dict] = []

    for path in skill_paths:
        skill_id = skill_id_for_path(path)
        meta = core_skill_metadata(skill_id)
        issues = validate_skill_file(path) + process_specific_issues(path)
        results.append(
            {
                "path": repo_relative(path),
                "skill_id": skill_id,
                "skill_label": meta.get("label") if meta else None,
                "issues": issues,
                "health": health,
                "lowest_scored_skill": lowest,
            }
        )
        if issues:
            print(
                "[Ask EA hooks] Validation warning for "
                f"`{repo_relative(path)}`: " + " | ".join(issues)
            )
        else:
            print(
                "[Ask EA hooks] Validated "
                f"`{repo_relative(path)}`: frontmatter and core sections are present."
            )
            if meta:
                print(
                    "[Ask EA hooks] Process check passed: "
                    f"{meta.get('label')} still covers {meta.get('governance_gate')}."
                )
        append_hook_event(
            {
                "hook_event": "post_tool_use",
                "kind": "core_skill_validation",
                "skill_id": skill_id,
                "skill_label": meta.get("label") if meta else skill_id,
                "path": repo_relative(path),
                "issues": issues,
                "validation_status": "warning" if issues else "pass",
            }
        )

    if lowest:
        print(
            "[Ask EA hooks] Live score watch: "
            f"{lowest.get('name', lowest.get('skill_id'))} remains lowest at "
            f"{lowest.get('avg')}/5."
        )

    print(
        "[Ask EA hooks] Health: "
        + ", ".join(f"{name}={status}" for name, status in health.items())
    )
    write_telemetry("ask-ea-post-tool-use.json", {"results": results})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
