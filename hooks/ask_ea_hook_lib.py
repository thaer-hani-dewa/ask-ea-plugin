#!/usr/bin/env python3
"""Shared helpers for Ask EA repo-local Claude hooks."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
EA_SKILLS_DIR = REPO_ROOT / "ea_skills"
TELEMETRY_DIR = REPO_ROOT / ".claude" / "telemetry"
HOOK_EVENTS_FILE = TELEMETRY_DIR / "hooks-events.jsonl"
REQUIRED_FRONTMATTER_KEYS = [
    "skill_id",
    "name",
    "version",
    "trigger_keywords",
    "priority",
    "active",
]
REQUIRED_SECTIONS = [
    "Description",
    "Trigger Conditions",
    "Inputs",
    "Process Steps",
    "Output Format",
    "Evaluation Rubric",
    "Test Cases",
]
HEALTH_ENDPOINTS = {
    "scores": "http://127.0.0.1:8753/healthz",
    "improvement": "http://127.0.0.1:8754/healthz",
    "discovery": "http://127.0.0.1:8756/healthz",
    "trace": "http://127.0.0.1:8755/healthz",
}
SCORES_ENDPOINT = "http://127.0.0.1:8753/skill-scores"
CORE_SKILL_HOOKS = {
    "ea-brd-review": {
        "label": "BRD Review",
        "process": "Demand quality gate",
        "hook_focus": "Preserve the BRD completeness scoring gate and EA governance sign-off logic.",
        "required_terms": [
            "Overall Completeness Score",
            "Review verdict",
            "Integration Points",
            "EA Governance Sign-off Path",
        ],
        "governance_gate": "Ready for HLD / Needs revision",
        "visual": {"accent": "#0a8f79", "icon": "clipboard"},
    },
    "ea-hld-review": {
        "label": "HLD Review",
        "process": "Architecture compliance gate",
        "hook_focus": "Protect the 5-layer compliance review, approved technology checks, and reuse-first review.",
        "required_terms": [
            "5-Layer Compliance Assessment",
            "Technology compliance check",
            "Reuse opportunity identification",
            "APPROVED FOR DETAILED DESIGN",
        ],
        "governance_gate": "Detailed design approval",
        "visual": {"accent": "#2f67d8", "icon": "layers"},
    },
    "ea-architecture-diagram": {
        "label": "Architecture Diagram",
        "process": "Solution visualization",
        "hook_focus": "Keep DEWA 5-layer mapping, diagram family choice, and OpenFlowKit handoff instructions intact.",
        "required_terms": [
            "OpenFlowKit",
            "5-layer",
            "diagram-ready architecture description",
            "security boundaries",
        ],
        "governance_gate": "Architecture visualization quality",
        "visual": {"accent": "#7b5cff", "icon": "diagram"},
    },
    "ea-impact-analysis": {
        "label": "Impact Analysis",
        "process": "Change impact assessment",
        "hook_focus": "Keep upstream/downstream impact dimensions and rollout sequencing explicit.",
        "required_terms": [
            "Data impact",
            "Process impact",
            "Integration impact",
            "change sequencing recommendation",
        ],
        "governance_gate": "Change risk sign-off",
        "visual": {"accent": "#d4870a", "icon": "pulse"},
    },
    "ea-compliance": {
        "label": "EA Compliance",
        "process": "Governance compliance review",
        "hook_focus": "Preserve compliance scoring, policy exceptions, and board escalation signals.",
        "required_terms": [
            "governance",
            "compliance",
            "EA principles",
            "architecture board",
        ],
        "governance_gate": "Policy compliance",
        "visual": {"accent": "#1a7a4a", "icon": "shield"},
    },
    "ea-demand-intake": {
        "label": "Demand Intake",
        "process": "Demand triage",
        "hook_focus": "Protect demand classification, effort tiering, and governance checkpoint logic.",
        "required_terms": [
            "Demand Classification Report",
            "Strategic Alignment Score",
            "EA Effort Tier",
            "governance checkpoints",
        ],
        "governance_gate": "Intake triage",
        "visual": {"accent": "#c94f3a", "icon": "intake"},
    },
    "ea-solution-pattern": {
        "label": "Solution Pattern",
        "process": "Reference architecture selection",
        "hook_focus": "Keep the top-3 pattern comparison and DEWA-approved technology mapping intact.",
        "required_terms": [
            "top 3 candidate patterns",
            "DEWA reference architecture patterns",
            "Compare top 3 patterns",
            "recommended primary pattern",
        ],
        "governance_gate": "Pattern selection",
        "visual": {"accent": "#6f56d9", "icon": "pattern"},
    },
    "ea-capability-mapping": {
        "label": "Capability Mapping",
        "process": "Business capability planning",
        "hook_focus": "Preserve heatmap output, maturity scoring, and investment prioritization logic.",
        "required_terms": [
            "Capability Heat Map",
            "Strategic alignment",
            "Current",
            "Target",
            "Build/Buy/Reuse",
        ],
        "governance_gate": "Investment planning",
        "visual": {"accent": "#0b8ca8", "icon": "heatmap"},
    },
    "ea-sa-diagram-design": {
        "label": "SA Diagram Design",
        "process": "Detailed diagram design",
        "hook_focus": "Preserve Mermaid export, DEWA layer mapping, and governance notes for diagram design work.",
        "required_terms": [
            "Architecture Diagram (Mermaid)",
            "Layer mapping table",
            "Governance notes",
            "Assumptions and constraints",
        ],
        "governance_gate": "Diagram design control",
        "visual": {"accent": "#2858b8", "icon": "flow"},
    },
    "ea-ai-governance-check": {
        "label": "AI Governance Check",
        "process": "AI risk governance gate",
        "hook_focus": "Preserve risk tier assignment (Tier 0–3), governance verdict logic, HITL requirements, data classification rules, and the 11-gate checklist. Do not remove or weaken the PROHIBITED verdict path or the approval matrix.",
        "required_terms": [
            "Governance verdict",
            "Risk tier",
            "AI Governance Gates",
            "Required Approvals",
            "Remediation Actions",
            "Data Governance Assessment",
            "Reference Architecture Conformance",
        ],
        "governance_gate": "AI risk gate — COMPLIANT / CONDITIONALLY COMPLIANT / NON-COMPLIANT / PROHIBITED",
        "visual": {"accent": "#dc3535", "icon": "shield"},
    },
}


def read_hook_payload() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def http_json(url: str, timeout: float = 0.75) -> object | None:
    try:
        with urlopen(url, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except (OSError, URLError, json.JSONDecodeError, TimeoutError):
        return None


def http_ok(url: str, timeout: float = 0.5) -> bool:
    try:
        with urlopen(url, timeout=timeout) as response:
            return 200 <= getattr(response, "status", 200) < 300
    except OSError:
        return False


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break
    if end_index is None:
        return {}

    result: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in lines[1:end_index]:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_key:
            bucket = result.setdefault(current_key, [])
            if isinstance(bucket, list):
                bucket.append(stripped[2:].strip().strip('"').strip("'"))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        cleaned = value.strip()
        if cleaned.lower() in {"true", "false"}:
            result[current_key] = cleaned.lower() == "true"
        elif cleaned.startswith("[") and cleaned.endswith("]"):
            items = [
                item.strip().strip('"').strip("'")
                for item in cleaned[1:-1].split(",")
                if item.strip()
            ]
            result[current_key] = items
        elif cleaned == "":
            result[current_key] = []
        else:
            result[current_key] = cleaned.strip('"').strip("'")
    return result


def discover_skill_files() -> list[Path]:
    if not EA_SKILLS_DIR.exists():
        return []
    return sorted(
        path
        for path in EA_SKILLS_DIR.glob("*.md")
        if path.name.lower() != "readme.md"
    )


def discover_skills() -> list[dict]:
    skills: list[dict] = []
    for path in discover_skill_files():
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        skills.append(
            {
                "path": path,
                "frontmatter": frontmatter,
                "text": text,
                "active": bool(frontmatter.get("active")),
                "skill_id": str(frontmatter.get("skill_id") or path.stem),
                "name": str(frontmatter.get("name") or path.stem),
            }
        )
    return skills


def section_names(text: str) -> set[str]:
    return set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))


def validate_skill_file(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return [f"file not found: {path.name}"]
    text = path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(text)
    missing_keys = [key for key in REQUIRED_FRONTMATTER_KEYS if key not in frontmatter]
    if missing_keys:
        issues.append(f"missing frontmatter keys: {', '.join(missing_keys)}")

    sections = section_names(text)
    missing_sections = [name for name in REQUIRED_SECTIONS if name not in sections]
    if missing_sections:
        issues.append(f"missing sections: {', '.join(missing_sections)}")
    return issues


def process_specific_issues(path: Path) -> list[str]:
    skill_id = path.stem
    spec = CORE_SKILL_HOOKS.get(skill_id)
    if not spec:
        return []
    text = path.read_text(encoding="utf-8")
    missing_terms = [term for term in spec["required_terms"] if term.lower() not in text.lower()]
    if not missing_terms:
        return []
    return [f"missing core process signals: {', '.join(missing_terms)}"]


def collect_health() -> dict[str, str]:
    return {name: ("up" if http_ok(url) else "down") for name, url in HEALTH_ENDPOINTS.items()}


def load_scoreboard() -> list[dict]:
    data = http_json(SCORES_ENDPOINT)
    return data if isinstance(data, list) else []


def lowest_scored_skill() -> dict | None:
    scored = [
        row for row in load_scoreboard()
        if isinstance(row, dict) and float(row.get("avg") or 0) > 0
    ]
    if not scored:
        return None
    return min(scored, key=lambda row: float(row.get("avg") or 0))


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def is_skill_path(path: Path) -> bool:
    try:
        resolved = path.resolve()
    except OSError:
        return False
    return resolved.parent == EA_SKILLS_DIR.resolve() and resolved.suffix == ".md"


def _looks_like_path(value: str) -> bool:
    return "/" in value or value.endswith(".md") or value.endswith(".json")


def _extract_candidate_paths(value: object) -> list[Path]:
    candidates: list[Path] = []
    if isinstance(value, str) and _looks_like_path(value):
        path = Path(value)
        if not path.is_absolute():
            path = REPO_ROOT / path
        candidates.append(path)
    elif isinstance(value, dict):
        for nested in value.values():
            candidates.extend(_extract_candidate_paths(nested))
    elif isinstance(value, list):
        for item in value:
            candidates.extend(_extract_candidate_paths(item))
    return candidates


def extract_skill_paths(payload: dict) -> list[Path]:
    unique: list[Path] = []
    seen: set[str] = set()
    for candidate in _extract_candidate_paths(payload):
        if not is_skill_path(candidate):
            continue
        key = str(candidate.resolve())
        if key in seen:
            continue
        seen.add(key)
        unique.append(candidate.resolve())
    return unique


def skill_id_for_path(path: Path) -> str:
    return path.stem


def core_skill_metadata(skill_id: str) -> dict:
    return CORE_SKILL_HOOKS.get(skill_id, {})


def active_core_skills() -> list[dict]:
    rows: list[dict] = []
    for skill in discover_skills():
        skill_id = skill["skill_id"]
        meta = CORE_SKILL_HOOKS.get(skill_id)
        if not meta:
            continue
        rows.append(
            {
                "skill_id": skill_id,
                "label": meta["label"],
                "process": meta["process"],
                "hook_focus": meta["hook_focus"],
                "governance_gate": meta["governance_gate"],
                "visual": meta["visual"],
                "active": skill["active"],
            }
        )
    return rows


def ensure_telemetry_dir() -> None:
    TELEMETRY_DIR.mkdir(parents=True, exist_ok=True)


def write_telemetry(name: str, payload: dict) -> None:
    ensure_telemetry_dir()
    target = TELEMETRY_DIR / name
    target.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def append_hook_event(event: dict) -> None:
    ensure_telemetry_dir()
    enriched = {"ts": datetime.utcnow().isoformat() + "Z", **event}
    with HOOK_EVENTS_FILE.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(enriched) + "\n")
