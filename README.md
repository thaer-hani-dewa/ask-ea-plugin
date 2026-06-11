# Ask EA Plugin

**Enterprise Architecture skill pack for Claude Code** — built by the DEWA EA team.

Installs 13 governed EA skills, 5 Claude Code lifecycle hooks, and the `ask-ea-skill-ops` Claude Code skill into any project.

---

## What's included

### Claude Code skill
| Skill | Trigger | Purpose |
|-------|---------|---------|
| `ask-ea-skill-ops` | Editing EA skill files, reviewing skill health | Grounds Claude in the EA skill catalog and lifecycle playbook |

### EA skill definitions (13 skills)
These are instruction files used by the Ask EA n8n workflow. Each skill has defined trigger keywords, process steps, output format, and evaluation rubric.

| Skill | Description |
|-------|-------------|
| `ea-demand-intake` | Classify and triage new project demands |
| `ea-brd-review` | Score BRDs against DEWA EA standards |
| `ea-hld-review` | Compliance check for High-Level Designs |
| `ea-architecture-diagram` | Generate DEWA 5-layer architecture diagrams |
| `ea-sa-diagram-design` | SA diagrams in Mermaid for OpenFlowKit |
| `ea-solution-pattern` | Recommend DEWA-approved reference patterns |
| `ea-impact-analysis` | Upstream/downstream change impact assessment |
| `ea-compliance` | EA principles & TOGAF compliance check |
| `ea-capability-mapping` | Business capability heat maps |
| `ea-product-evaluation` | Gartner-style technology assessments |
| `ea-ai-governance-check` | AI risk tier classification (Tier 0–3) |
| `ea-orchestrator` | Multi-skill coordination |
| `ea-skills-lifecycle-health` | Skill quality and improvement playbook |

### Claude Code hooks (5 hooks)
| Hook | Event | What it does |
|------|-------|-------------|
| `ask_ea_session_start.py` | SessionStart | Shows EA skill catalog, live scores, and service health |
| `ask_ea_pre_tool_use.py` | PreToolUse (Write/Edit) | Warns before editing skill files — protects required frontmatter |
| `ask_ea_post_tool_use.py` | PostToolUse (Write/Edit) | Validates skill file structure after edits |
| `ask_ea_stop.py` | Stop | Saves session snapshot of which skills were touched |
| `ask_ea_hook_lib.py` | — | Shared library used by all hooks |

---

## Installation

### Option 1 — Install script (recommended)

```bash
git clone <repo-url> ask-ea-plugin
cd ask-ea-plugin
bash install.sh /path/to/your/project
```

Or install into the current directory:
```bash
bash install.sh
```

### Option 2 — Manual

1. Copy `skills/ask-ea-skill-ops/` → `.claude/skills/ask-ea-skill-ops/`
2. Copy `hooks/*.py` → `.claude/hooks/`
3. Copy `ea_skills/*.md` → `ea_skills/`
4. Merge `settings-patch.json` hooks into your `.claude/settings.json`

---

## After installation

Open Claude Code in your project. You will see:

- **SessionStart**: EA skill catalog and health summary printed at startup
- **Skill available**: `/ask-ea-skill-ops` — manage and review EA skills
- **Hooks active**: Pre/post edit validation on any `ea_skills/*.md` file

### Verify installation
```bash
# Confirm skill is visible
ls .claude/skills/ask-ea-skill-ops/

# Confirm hooks are registered
cat .claude/settings.json | python3 -c "import sys,json; h=json.load(sys.stdin).get('hooks',{}); [print(e, len(v), 'entries') for e,v in h.items()]"

# Confirm EA skills are present
ls ea_skills/*.md | wc -l   # should be 13
```

---

## Plugin structure

```
ask-ea-plugin/
├── skills/
│   └── ask-ea-skill-ops/
│       └── SKILL.md          ← Claude Code skill
├── hooks/
│   ├── ask_ea_hook_lib.py    ← Shared library
│   ├── ask_ea_session_start.py
│   ├── ask_ea_pre_tool_use.py
│   ├── ask_ea_post_tool_use.py
│   └── ask_ea_stop.py
├── ea_skills/
│   └── ea-*.md               ← 13 EA skill definitions
├── settings-patch.json       ← Hook registration config
├── install.sh                ← Automated installer
└── README.md
```

---

## Contributing

Skills follow the frontmatter contract:
```yaml
---
skill_id: ea-example
name: Example Skill
version: "1.0"
trigger_keywords:
  - keyword one
  - keyword two
priority: 2
active: true
---
```

Required sections in every skill file:
- `## Description`
- `## Trigger Conditions`
- `## Inputs`
- `## Process Steps`
- `## Output Format`
- `## Evaluation Rubric`
- `## Test Cases`

---

## Maintainer

DEWA · Innovation & The Future · Enterprise Architecture Office  
Built with Claude Code · Version 1.0 · June 2026
