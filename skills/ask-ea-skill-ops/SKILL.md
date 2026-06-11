---
name: ask-ea-skill-ops
description: Use when editing Ask EA skill markdown, reviewing skill health and lifecycle readiness, or preparing the Skills Intel / improvement-loop demo. Grounds Claude work in the Ask EA skill catalog, lifecycle health playbook, and local skill services.
---

# Ask EA Skill Operations

Use this skill when the task is about the Ask EA skill system rather than generic app code.

## Use When

- Editing any file in `ea_skills/`
- Reviewing skill quality, readiness, or lifecycle health
- Preparing workshop or GitHub artifacts for Ask EA skills
- Checking why a skill is underperforming in Skills Intel
- Explaining the improvement loop, discovery flow, or trace flow

## Primary Sources

- `ea_skills/README.md`
- `ea_skills/ea-skills-lifecycle-health.md`
- `services/skill_scores/server.py`
- `services/skill_trace/server.py`
- `services/skill_improvement/server.py`
- `services/skill_discovery/server.py`
- `.claude/hooks/README.md`

## Operating Rules

1. Treat each `ea_skills/*.md` file as a governed skill contract.
2. Preserve frontmatter fields:
   - `skill_id`
   - `name`
   - `version`
   - `trigger_keywords`
   - `priority`
   - `active`
3. Preserve the core skill sections unless the user explicitly wants a different format:
   - `Description`
   - `Trigger Conditions`
   - `Inputs`
   - `Process Steps`
   - `Output Format`
   - `Evaluation Rubric`
   - `Test Cases`
4. When discussing health, ground the answer in:
   - live score state
   - trace availability
   - improvement-loop status
   - discovery service status
5. Prefer repo-local hooks and docs over personal machine-specific `~/.claude/*` behavior when preparing shareable results.

## Health Checklist

- Score service: `http://127.0.0.1:8753/healthz`
- Improvement service: `http://127.0.0.1:8754/healthz`
- Trace service: `http://127.0.0.1:8755/healthz`
- Discovery service: `http://127.0.0.1:8756/healthz`

## Expected Outputs

- A valid Ask EA skill file change
- A clear health/readiness summary
- A GitHub-friendly explanation of how Claude hooks reinforce the Ask EA skills lifecycle
