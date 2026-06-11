#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# Ask EA Plugin — Installer
# Usage:  bash install.sh [TARGET_PROJECT_DIR]
# Default target: current working directory
# ─────────────────────────────────────────────────────────────────────────────
set -e

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-$(pwd)}"

echo ""
echo "=================================================="
echo "  Ask EA Plugin — Installing to:"
echo "  $TARGET"
echo "=================================================="

# ── 1. Claude Code skill ──────────────────────────────────────────────────────
echo ""
echo "[1/4] Installing Claude Code skill (ask-ea-skill-ops)..."
mkdir -p "$TARGET/.claude/skills/ask-ea-skill-ops"
cp -r "$PLUGIN_DIR/skills/ask-ea-skill-ops/." "$TARGET/.claude/skills/ask-ea-skill-ops/"
echo "      ✓ .claude/skills/ask-ea-skill-ops/SKILL.md"

# ── 2. Hooks ──────────────────────────────────────────────────────────────────
echo ""
echo "[2/4] Installing Claude Code hooks..."
mkdir -p "$TARGET/.claude/hooks"
cp "$PLUGIN_DIR/hooks/"*.py "$TARGET/.claude/hooks/"
echo "      ✓ ask_ea_hook_lib.py"
echo "      ✓ ask_ea_session_start.py"
echo "      ✓ ask_ea_pre_tool_use.py"
echo "      ✓ ask_ea_post_tool_use.py"
echo "      ✓ ask_ea_stop.py"

# ── 3. EA skill definitions ───────────────────────────────────────────────────
echo ""
echo "[3/4] Installing EA skill definitions..."
mkdir -p "$TARGET/ea_skills"
cp "$PLUGIN_DIR/ea_skills/"*.md "$TARGET/ea_skills/"
COUNT=$(ls "$PLUGIN_DIR/ea_skills/"*.md | wc -l | tr -d ' ')
echo "      ✓ $COUNT skill files → ea_skills/"

# ── 4. Merge hook settings ────────────────────────────────────────────────────
echo ""
echo "[4/4] Registering hooks in .claude/settings.json..."
mkdir -p "$TARGET/.claude"
python3 - "$TARGET/.claude/settings.json" "$PLUGIN_DIR/settings-patch.json" << 'PYEOF'
import json, sys, os

settings_path = sys.argv[1]
patch_path    = sys.argv[2]

# Load existing settings or start empty
if os.path.exists(settings_path):
    with open(settings_path) as f:
        settings = json.load(f)
else:
    settings = {}

with open(patch_path) as f:
    patch = json.load(f)

# Merge hooks — append Ask EA entries without removing existing ones
settings.setdefault("hooks", {})
for event, entries in patch["hooks"].items():
    settings["hooks"].setdefault(event, [])
    for entry in entries:
        cmd = entry["hooks"][0]["command"]
        # Skip if already registered
        already = any(
            h.get("command") == cmd
            for e in settings["hooks"][event]
            for h in e.get("hooks", [])
        )
        if not already:
            settings["hooks"][event].append(entry)

with open(settings_path, "w") as f:
    json.dump(settings, f, indent=2)
PYEOF
echo "      ✓ hooks registered in .claude/settings.json"

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
echo "=================================================="
echo "  Ask EA Plugin installed successfully!"
echo ""
echo "  What was installed:"
echo "  • .claude/skills/ask-ea-skill-ops/   ← Claude Code skill"
echo "  • .claude/hooks/ask_ea_*.py          ← 5 lifecycle hooks"
echo "  • ea_skills/*.md                     ← 13 EA skill definitions"
echo "  • .claude/settings.json              ← hooks registered"
echo ""
echo "  Next step: open Claude Code in $TARGET"
echo "  The /ask-ea-skill-ops skill and EA hooks are now active."
echo "=================================================="
echo ""
