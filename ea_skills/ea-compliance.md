---
skill_id: ea-compliance
name: EA Principles & Standards Compliance Check
version: "1.0"
trigger_keywords:
  - compliance check
  - EA principles
  - governance review
  - standards review
  - DEWA standards
  - architecture principles
  - TOGAF
  - governance
priority: 4
active: true
---

## Description

The EA Compliance skill performs a structured pass/fail compliance check of a proposed solution, architecture, or project against DEWA's EA principles, TOGAF compliance markers, and relevant DEWA technology governance standards. It maps each solution element to the applicable principle, produces per-principle verdicts with evidence, and lists specific remediation actions for non-compliant elements. This skill is used during architecture governance gates and project portfolio reviews.

## Trigger Conditions

- Explicit: User asks "is this solution compliant with EA principles?", "run a compliance check", "governance review"
- Explicit: User references TOGAF, DEWA standards, or EA principles in their query
- Implicit: User describes a solution and asks whether it aligns with DEWA strategy or governance
- Implicit: User asks about architecture governance, DEWA IT standards, or architecture board requirements

## Inputs

| Input                | Type           | Required | Description                                                             |
|----------------------|----------------|----------|-------------------------------------------------------------------------|
| solution_description | text/document  | required | Description of the solution, architecture, or project being checked     |
| solution_type        | text           | optional | Type of check (new system, architecture change, procurement, vendor eval) |
| dewa_principles_ref  | reference      | optional | DEWA EA principles (auto-loaded from KB)                                |
| togaf_phase          | text           | optional | TOGAF ADM phase for phase-specific compliance (A–H)                     |

## Process Steps

1. **Extract solution elements**: Identify all key solution components — technology choices, integration approaches, data handling, security mechanisms, deployment model, vendor relationships, and governance structures.

2. **Load DEWA EA principles** — apply the following 8 DEWA EA core principles:
   - **P1 — Reuse First**: Prefer existing DEWA-approved systems before procuring or building new
   - **P2 — Data Sovereignty**: DEWA data must remain within UAE; no unauthorised cross-border transfer
   - **P3 — Integration via Standards**: All system-to-system integration must use DEWA API Gateway or approved middleware
   - **P4 — Security by Design**: Security controls (auth, encryption, network segmentation) must be built in from day 1
   - **P5 — Vendor Independence**: Avoid proprietary lock-in; prefer open standards and portable architectures
   - **P6 — Scalability & Resilience**: Solutions must support defined growth projections and DEWA BCM requirements
   - **P7 — Governance Alignment**: Solutions must pass DEWA architecture review and receive EA sign-off before implementation
   - **P8 — Simplicity**: Prefer simple, maintainable solutions over complex ones; avoid unnecessary duplication of capability

3. **Map solution elements to each principle**: For every principle, identify which solution elements are directly relevant. Collect evidence for compliance or non-compliance from the solution description.

4. **Assign per-principle verdict**:
   - **PASS**: Solution element is clearly compliant; evidence is present
   - **CONDITIONAL**: Solution is partially compliant but requires a specific action to achieve full compliance
   - **FAIL**: Solution element clearly violates the principle; remediation required before approval
   - **N/A**: Principle is not applicable to this solution type

5. **Check TOGAF compliance markers** (if applicable):
   - Architecture Vision (Phase A): Business goals and drivers documented
   - Business Architecture (Phase B): Business processes impacted identified
   - Information Systems Architecture (Phase C): Data entities and application components mapped
   - Technology Architecture (Phase D): Technology components and standards referenced
   - Opportunities & Solutions (Phase E): Implementation approach and sequencing defined

6. **Identify governance requirements**: Based on solution scope, determine which DEWA governance bodies must approve (EA Review Board, Technology Board, Information Security Committee, Data Governance Committee, Change Advisory Board).

7. **Produce Compliance Report** with principles table, TOGAF markers, governance checklist, and remediation plan.

## Output Format

```
# EA Compliance Report — [Solution Name]
**Checked by:** Ask EA (AI-assisted compliance)
**Check date:** [date]
**Solution type:** [New System / Enhancement / Integration / Procurement / Study]
**Overall verdict:** [COMPLIANT | CONDITIONALLY COMPLIANT | NON-COMPLIANT]
**Principles passed:** [X/8] | **Conditional:** [X/8] | **Failed:** [X/8]

---

## Executive Summary
[2–3 sentences: solution overview, compliance status, critical failures, required actions before approval]

---

## Principles Compliance Table

| # | Principle                    | Verdict        | Evidence                                             | Gap / Action Required                              |
|---|------------------------------|----------------|------------------------------------------------------|----------------------------------------------------|
| P1 | Reuse First                 | [PASS/COND/FAIL/N/A] | [evidence from solution description]          | [specific action if COND or FAIL]                  |
| P2 | Data Sovereignty            | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |
| P3 | Integration via Standards   | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |
| P4 | Security by Design          | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |
| P5 | Vendor Independence         | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |
| P6 | Scalability & Resilience    | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |
| P7 | Governance Alignment        | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |
| P8 | Simplicity                  | [PASS/COND/FAIL/N/A] | [evidence]                                    | [action]                                           |

---

## TOGAF Compliance Markers

| Phase | Area                          | Status          | Finding                                            |
|-------|-------------------------------|-----------------|---------------------------------------------------|
| A     | Architecture Vision           | [PASS/WARN/N/A] | [finding]                                         |
| B     | Business Architecture         | [PASS/WARN/N/A] | [finding]                                         |
| C     | Information Systems Arch.     | [PASS/WARN/N/A] | [finding]                                         |
| D     | Technology Architecture       | [PASS/WARN/N/A] | [finding]                                         |
| E     | Opportunities & Solutions     | [PASS/WARN/N/A] | [finding]                                         |

---

## Required Governance Approvals

| Governance Body                     | Required | Status    | Reason                                        |
|-------------------------------------|----------|-----------|-----------------------------------------------|
| EA Review Board                     | [Y/N]    | [Pending/Obtained/N/A] | [reason]                              |
| EA Technology Board                 | [Y/N]    | [Pending/Obtained/N/A] | [reason — required for new tech]       |
| Information Security Committee      | [Y/N]    | [Pending/Obtained/N/A] | [reason — required for security changes] |
| Data Governance Committee           | [Y/N]    | [Pending/Obtained/N/A] | [reason — required for new data entities] |
| Change Advisory Board               | [Y/N]    | [Pending/Obtained/N/A] | [reason — required for production changes] |

---

## Remediation Plan

| # | Principle | Gap Description                     | Remediation Action                               | Owner         | Priority |
|---|-----------|-------------------------------------|--------------------------------------------------|---------------|----------|
| 1 | [Px]      | [specific gap]                      | [specific action to achieve compliance]          | [team/role]   | [H/M/L] |

---

## Compliance Certificate

[If COMPLIANT or CONDITIONALLY COMPLIANT]:
This solution has been assessed against DEWA EA principles and is [approved for | conditionally approved pending: {conditions}] progression to the next phase.

[If NON-COMPLIANT]:
This solution cannot progress to the next phase until the FAIL items in the Remediation Plan are addressed and re-assessed.
```

## Evaluation Rubric

| Criterion                    | Weight | 1 (Poor)                                             | 3 (Adequate)                                          | 5 (Excellent)                                                   |
|------------------------------|--------|------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| Principle coverage           | 25%    | Fewer than 5 of 8 principles assessed                | All 8 principles assessed but some marked N/A without justification | All 8 principles assessed with clear N/A justification where applicable |
| Evidence quality             | 20%    | Verdicts assigned without evidence                   | Evidence provided but taken from surface-level reading | Evidence is specific quotes or elements from the solution description |
| Gap specificity              | 20%    | Gaps described vaguely ("not aligned")               | Gaps are specific to the principle                    | Gaps are specific, actionable, and mapped to exact solution elements |
| Remediation clarity          | 20%    | No remediation actions provided                      | Generic actions ("review the design")                 | Specific actions with owner, priority, and measurable acceptance criteria |
| TOGAF mapping accuracy       | 15%    | No TOGAF assessment                                  | TOGAF phases mentioned without mapping to solution    | TOGAF phases mapped to specific solution elements with evidence |

## Test Cases

### TC-01: Fully Compliant Solution
- **Input:** Solution proposal for a MyDEWA portal enhancement using existing DEWA API Gateway, Oracle DB on DEWA private cloud, ADFS SSO, with EA review board approval pending
- **Expected output:** P1 PASS (reusing API Gateway, existing DB); P2 PASS (private cloud, UAE); P3 PASS (API Gateway); P4 COND (SSO confirmed, MFA status unknown); P7 PASS (EA board approval noted); Overall CONDITIONALLY COMPLIANT pending MFA confirmation
- **Pass criteria:** At least 6 principles assessed; P3 PASS noted; verdict is COMPLIANT or CONDITIONAL

### TC-02: Solution Violating Data Sovereignty
- **Input:** Proposal to store DEWA customer meter readings on AWS US-East-1 for cost reasons
- **Expected output:** P2 FAIL (data outside UAE); P5 WARN (AWS lock-in); Remediation: migrate to Azure UAE North or DEWA private cloud; governance requires Data Governance Committee approval
- **Pass criteria:** P2 verdict = FAIL; Data Governance Committee = Required; specific UAE-hosting alternative recommended

### TC-03: Monolithic Solution vs Microservices Standard
- **Input:** Proposal for a new DEWA operational system as a single monolithic Java EE application with no API layer
- **Expected output:** P3 FAIL or COND (no API layer means future integrations bypass gateway); P5 WARN (monolith is vendor/framework lock-in risk); P6 WARN (scaling a monolith vs DEWA BCM requirements); P8 COND (simplicity depends on team capability)
- **Pass criteria:** P3 flagged; P5 flagged; recommendation includes modular API layer

### TC-04: Solution With No Governance Approval Path
- **Input:** A vendor-proposed solution that is being fast-tracked to implementation without any EA review
- **Expected output:** P7 FAIL (no EA review noted); Overall NON-COMPLIANT; EA Review Board listed as Required/Pending; compliance certificate denies progression
- **Pass criteria:** P7 = FAIL; EA Review Board = Required; Compliance Certificate is non-compliant text

### TC-05: TOGAF Phase Compliance — Phase C
- **Input:** A Phase C (Information Systems Architecture) artefact for a new DEWA data warehouse
- **Expected output:** TOGAF phases A, B checked for prerequisites; Phase C assessed for data entities, application components, and data flow; Phase D and E marked N/A (not yet reached)
- **Pass criteria:** Phase C assessment is the most detailed; phases A and B include prerequisite checks; phases D/E are N/A with justification

## Human Approval Points

- The AI-generated compliance report is advisory only; the EA Lead Architect must review and countersign before it is communicated to the project team or used in an architecture board submission
- FAIL verdicts on P2 (Data Sovereignty) or P4 (Security by Design) must be escalated to the DEWA CISO — the AI must not suggest workarounds without human oversight
- The Compliance Certificate section must be explicitly approved by a human EA reviewer — the AI generates the draft but does not self-certify
