#!/usr/bin/env python3
"""PreToolUse hook for Ask EA skill edits."""

from __future__ import annotations

from ask_ea_hook_lib import (
    REQUIRED_FRONTMATTER_KEYS,
    REQUIRED_SECTIONS,
    append_hook_event,
    core_skill_metadata,
    extract_skill_paths,
    read_hook_payload,
    repo_relative,
    skill_id_for_path,
)


def main() -> int:
    payload = read_hook_payload()
    skill_paths = extract_skill_paths(payload)
    if not skill_paths:
        return 0

    for path in skill_paths:
        skill_id = skill_id_for_path(path)
        meta = core_skill_metadata(skill_id)
        print(
            "[Ask EA hooks] Editing skill "
            f"`{repo_relative(path)}`. Preserve frontmatter keys: "
            + ", ".join(REQUIRED_FRONTMATTER_KEYS)
            + "."
        )
        print(
            "[Ask EA hooks] Required sections: "
            + ", ".join(REQUIRED_SECTIONS)
            + "."
        )
        if meta:
            print(
                "[Ask EA hooks] Core process guardrail: "
                f"{meta.get('label')} supports {meta.get('process')}. "
                f"{meta.get('hook_focus')}"
            )
            append_hook_event(
                {
                    "hook_event": "pre_tool_use",
                    "kind": "core_skill_edit",
                    "skill_id": skill_id,
                    "skill_label": meta.get("label"),
                    "path": repo_relative(path),
                    "process": meta.get("process"),
                }
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
