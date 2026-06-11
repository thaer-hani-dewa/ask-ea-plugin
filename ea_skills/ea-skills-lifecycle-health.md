---
skill_id: ea-skills-lifecycle-health
name: EA Skills Lifecycle & Health Check
version: "1.0"
trigger_keywords:
  - skill lifecycle
  - skill health
  - skill score
  - skill intel
  - skills dashboard
  - skill governance
  - skill quality
  - improvement loop
priority: 4
active: true
---

## Description

This skill defines how Ask EA skills are governed end-to-end: health monitoring, scoring, telemetry review, autonomous improvement loop checks, audit evidence, and release readiness. It is used as the operational playbook for maintaining skill quality and demonstrating measurable improvement over time.

## Scope

- Monitor skill quality scores and trends.
- Verify skill telemetry and usage coverage.
- Inspect improvement-loop outcomes and audit artifacts.
- Validate that skill updates are safely promoted and traceable.
- Produce executive-ready lifecycle snapshots for governance reviews.

## Lifecycle Stages

1. **Design**
   - Define objective, trigger keywords, inputs/outputs, rubric, and test cases.
   - Ensure alignment to DEWA EA standards and governance constraints.

2. **Deploy**
   - Publish `ea_skills/<skill-id>.md` to host and n8n runtime container.
   - Confirm skill appears in UI routing/activation traces.

3. **Observe**
   - Collect scored executions and trace entries.
   - Verify skill activity and score coverage in Skills Intel panel.

4. **Improve**
   - For underperforming skills (below threshold), run improvement loop.
   - Apply audited updates and re-check post-change behavior.

5. **Govern**
   - Preserve audit logs, before/after diffs, and report artifacts.
   - Provide lifecycle status to architecture leadership.

## Health Checks

### 1) Runtime Availability

- `GET /api/skill-scores/healthz` (or service equivalent)
- `GET /api/skill-improvement/healthz`
- `GET /api/skill-discovery/healthz`
- `GET /api/trace/healthz` (or trace service status)

Pass criteria:
- All critical services respond successfully within expected latency.

### 2) Score Health

- Confirm each core skill has recent evaluations.
- Check average score by skill and trend direction.
- Flag skills below improvement threshold (default: `< 3.5/5`).

Pass criteria:
- No critical skill is unscored for a long period.
- Low-score skills are queued for improvement with owner and timestamp.

### 3) Telemetry Health

- Validate `Skills activity` stream receives activation events.
- Ensure route-to-skill mapping is correct for representative prompts.

Pass criteria:
- Skill detection and evaluation events are present and consistent.

### 4) Improvement Loop Health

- Run one controlled cycle when a candidate exists.
- Verify cycle status (`done`, `all_good`, `no_scores`).
- Confirm audit JSON and HTML report are generated.

Pass criteria:
- Every applied change has machine-readable audit + human-readable report.

### 5) Artifact Integrity

- Validate latest report path is accessible.
- Confirm changed skill content was synchronized to container runtime.
- Confirm rollback/reset path works.

Pass criteria:
- Skill file and runtime container content are consistent.
- Reset path restores baseline deterministically.

## Standard Operating Procedure (Weekly)

1. Open Skills Intel and capture current score snapshot.
2. Review bottom 3 skills by average score.
3. Run improvement loop only for qualified low-score candidates.
4. Open latest improvement report and verify change rationale + diff.
5. Record outcomes in governance notes (improved/skipped/all good).
6. Re-run representative prompts for impacted skills.

## Executive Reporting Template

Use this structure in leadership updates:

- **Overall status:** Healthy / Needs attention
- **Skills monitored:** [count]
- **Low-score skills:** [skill list + score]
- **Improvements applied this period:** [count + names]
- **Evidence:** [latest audit report paths]
- **Top risks:** [routing gaps, stale scores, service downtime]
- **Next actions (owner/date):** [3 items max]

## Required Evidence

- `ea_skills/audit/*.json` (cycle audits)
- `ea_skills/audit/reports/*.html` (human-readable reports)
- latest skill score snapshot and trace samples
- changed skill markdown diff (before/after)

## Guardrails

- Do not apply un-audited skill edits in production demos.
- Do not run overlapping improvement cycles.
- Always keep backup/restore path available for demo and governance runs.
- Treat deterministic demo mode as demo-only; for true model behavior, run live LLM loop mode.

## Output Format

When this skill is invoked, output:

1. **Health summary** (services, score state, telemetry, improvement status)
2. **Findings** (ordered by severity)
3. **Evidence pointers** (paths/endpoints)
4. **Actions** (owner + timeline)

