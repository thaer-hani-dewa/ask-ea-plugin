---
skill_id: ea-orchestrator
name: EA Skill Orchestrator
version: "1.0"
trigger_keywords:
  - help
  - what can you do
  - show skills
  - available skills
priority: 0
active: true
---

## Description

The EA Skill Orchestrator routes incoming user requests to the correct specialist EA skill based on keyword detection in the user's input. It acts as the routing layer that decides which skill to activate, loads the corresponding skill instructions, and ensures every AI response is labelled with the active skill context. When no specialist skill matches, the orchestrator handles the request as a general EA Q&A.

## Trigger Conditions

- Explicit: User types "help", "skills", or "what can you do"
- Implicit: Any message arrives — the orchestrator always runs first to detect skill triggers
- Fallback: No specialist skill keyword matched — route to general EA Q&A mode

## Routing Table

| Skill ID              | Trigger Keywords                                                                           | Priority |
|-----------------------|-------------------------------------------------------------------------------------------|----------|
| ea-brd-review         | brd, business requirement, business case, requirement document, project brief             | 1        |
| ea-hld-review         | hld, high level design, architecture review, solution design, architecture document, technical design | 2  |
| ea-impact-analysis    | impact analysis, impact assessment, downstream systems, affected systems, change impact   | 3        |
| ea-compliance         | compliance check, ea principles, governance review, dewa standards, architecture principles | 4      |
| ea-demand-intake      | new demand, project request, demand classification, intake, triage, demand form           | 5        |
| ea-solution-pattern   | solution pattern, architecture pattern, reference architecture, pattern library           | 6        |

## Inputs

| Input         | Type   | Required | Description                                          |
|---------------|--------|----------|------------------------------------------------------|
| user_input    | text   | required | The raw user message or chat input                   |
| session_id    | string | optional | Session identifier for context continuity            |
| attached_doc  | text   | optional | Extracted document content if a file was uploaded    |

## Process Steps

1. Receive the user input (strip any document attachment prefix for keyword matching)
2. Normalize input to lowercase for case-insensitive matching
3. Iterate through the routing table in priority order; stop at first match
4. If a match is found: load the matched skill's `.md` file from `/home/node/ea_skills/`
5. Prepend skill context to the AI Agent input: `[EA SKILL ACTIVE: {skill_name}]\n\nSKILL INSTRUCTIONS:\n{skill_content}\n\n---\nUSER INPUT:\n{original_input}`
6. Set `_activeSkill` metadata on the output item for the Skill Evaluator
7. If no match: pass the input unchanged, set `_activeSkill = 'none'`
8. Return the (possibly modified) item to the AI Agent node

## Output Format

**When skill matched:**
```
[EA SKILL ACTIVE: {Skill Name}]

SKILL INSTRUCTIONS:
{full skill markdown content}

---
USER INPUT:
{original user message}
```

**When no skill matched (general Q&A):**
```
{original user message unchanged}
```

**Response label** (the AI Agent must prefix its reply):
```
[Skill: {skill_name}] — {response content}
```

## Evaluation Rubric

| Criterion              | Weight | 1 (Poor)                              | 3 (Adequate)                            | 5 (Excellent)                                  |
|------------------------|--------|---------------------------------------|------------------------------------------|------------------------------------------------|
| Routing accuracy       | 25%    | Wrong skill triggered or none when one should fire | Correct skill triggered for obvious inputs | Correct skill for subtle and multi-intent inputs |
| Context injection      | 20%    | Skill file not loaded or empty         | Skill content partially injected         | Full skill content prepended with correct format |
| Skill detection confidence | 20% | Mis-triggers on unrelated text       | Correct for explicit triggers only       | Correct for both explicit and implicit triggers |
| Fallback handling      | 20%    | Crashes or returns empty on no match  | Returns unchanged input on no match      | Returns unchanged input and sets _activeSkill='none' cleanly |
| Response labelling     | 15%    | AI response has no skill label        | Label present but inconsistently formatted | Label always present, correctly formatted, skill name accurate |

## Test Cases

### TC-01: BRD Upload Trigger
- **Input:** "Can you review this BRD for me? [attached PDF content]"
- **Expected output:** Routes to `ea-brd-review`, prepends full BRD review skill instructions
- **Pass criteria:** `_activeSkill === 'ea-brd-review'`; chatInput contains "SKILL INSTRUCTIONS:"

### TC-02: HLD Architecture Question
- **Input:** "I need an architecture review of this HLD design for the smart meter portal"
- **Expected output:** Routes to `ea-hld-review`
- **Pass criteria:** `_activeSkill === 'ea-hld-review'`

### TC-03: Compliance Query
- **Input:** "Does this solution comply with DEWA EA principles?"
- **Expected output:** Routes to `ea-compliance`
- **Pass criteria:** `_activeSkill === 'ea-compliance'`

### TC-04: Ambiguous Input — Fallback
- **Input:** "What is the weather in Dubai?"
- **Expected output:** No skill triggered; input passed through unchanged
- **Pass criteria:** `_activeSkill === 'none'`; chatInput unchanged

### TC-05: Demand Classification
- **Input:** "We have a new demand for a mobile app — how do we classify it?"
- **Expected output:** Routes to `ea-demand-intake`
- **Pass criteria:** `_activeSkill === 'ea-demand-intake'`

## Human Approval Points

- No human approval required at the routing stage — routing is fully automated
- If the routing result is unexpected (wrong skill fired), the user can override by typing the skill name explicitly (e.g., "use BRD review skill")
