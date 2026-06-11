---
skill_id: ea-ai-governance-check
name: AI Governance Check
version: "1.0"
trigger_keywords:
  - ai governance
  - ai compliance
  - ai use case
  - genai
  - copilot
  - agent
  - rag
  - model card
  - hitl
  - ai risk tier
priority: 1
active: true
---

## Description

The AI Governance Check skill evaluates whether a BRD, requirement set, use case, HLD, or proposal falls within DEWA's AI governance framework and, if so, whether it conforms to the required risk tier, agent classification, data handling rules, architecture standard, lifecycle gates, and enterprise guardrails.

This skill is not a general EA principles review. It is a specialized governance overlay for AI-related initiatives and should be used together with BRD review, HLD review, demand intake, or EA compliance whenever the request involves GenAI, copilots, agents, ML-assisted decisioning, AI skills, prompt-based workflows, or automation with AI.

Canonical policy reference:
- `governance/ea_ai_governance_v1.yaml`

## Trigger Conditions

- Explicit: User asks for "AI governance check", "AI compliance", "AI use case review", "agent governance", or "Copilot compliance"
- Implicit: The BRD or use case mentions AI, GenAI, LLM, agent, Copilot, RAG, model, prompt, summarisation, recommendation, prediction, classification, or AI-assisted automation
- Implicit: The request includes AI architecture, model selection, prompt workflows, governed connectors, HITL, kill-switch, or model card requirements
- Implicit: The proposed solution writes to enterprise systems or handles confidential or restricted data with AI

## Inputs

| Input | Type | Required | Description |
|------|------|----------|-------------|
| ai_use_case_content | text/document | required | BRD, HLD, requirement set, use case, or proposal content |
| project_context | text | optional | Business context, owner, target users, environment, rollout stage |
| governance_policy | reference | optional | Structured AI governance policy asset from `governance/ea_ai_governance_v1.yaml` |
| primary_review_type | text | optional | BRD review, HLD review, intake, or standalone governance review |

## Process Steps

1. **Decide whether the framework applies**
   - Determine whether the use case is AI-related.
   - If the use case is not AI-related, say so clearly and stop the AI governance review.
   - Do not force AI governance on pure non-AI initiatives.

2. **Extract AI-relevant facts**
   - Identify whether the use case uses GenAI, copilots, agents, ML models, prompt workflows, automation with decisioning, plugins, or reusable skills.
   - Extract enterprise actions, data sources, target users, outputs, and whether any system write-back is proposed.

3. **Classify the AI use case**
   - Assign the dominant operating mode: advisory, knowledge, workflow, transactional, or autonomous.
   - If the use case blends multiple modes, state the primary type and list the secondary ones.

4. **Assign the risk tier**
   - Use DEWA's Tier 0 to Tier 3 model.
   - Prefer deterministic classification:
     - Tier 0 if prohibited use cases are present.
     - Tier 1 if confidential data, governed write-back, PII classification, or autonomous enterprise action is present.
     - Tier 2 if this is a bounded enterprise copilot, RAG assistant, or governed knowledge or advisory workflow.
     - Tier 3 if low-risk productivity support with no write-back and no sensitive data.
   - State why the chosen tier applies.

5. **Check data governance and classification**
   - Identify likely source data classification: Public, Internal, Confidential, or Restricted.
   - Check for restricted data exposure, PII handling, masking requirements, and cross-border processing risks.
   - Apply the rule that AI outputs inherit the highest source classification.

6. **Check architecture conformance**
   - Assess the use case against the 7-layer AI reference architecture:
     - UI Layer
     - AI Layer
     - Orchestration
     - Integration
     - Security
     - Data Access
     - Monitoring
   - Flag direct database access, unapproved public LLMs, undocumented webhooks, unlogged calls, or missing monitoring.

7. **Check lifecycle and gate readiness**
   - Review the 11-point AI gate checklist.
   - Note which gates are complete, partial, or missing.
   - Explicitly check for:
     - risk tier assignment
     - data inventory
     - security review
     - HITL design
     - model card
     - success metrics
     - kill-switch
     - retirement criteria
     - AI Team sign-off

8. **Check enterprise guardrails**
   - Approved models only
   - Mandatory prompt and response logging
   - Data masking and classification enforcement
   - Human approval for high-stakes or write-back actions
   - Full auditability
   - Prohibited use case rejection

9. **Determine approvals**
   - Always identify whether EA, AI Team, and Security approval are needed.
   - Add Data Governance Office if classification, PII, or cross-border issues are relevant.
   - Add CAB if production changes or operational deployment are involved.

10. **Issue the governance verdict**
   - `NOT APPLICABLE`: not an AI use case
   - `COMPLIANT`: framework applies and no material governance gaps are found
   - `CONDITIONALLY COMPLIANT`: feasible but controls, approvals, or design changes are missing
   - `NON-COMPLIANT`: governance gaps must be closed before proceeding
   - `PROHIBITED`: Tier 0 or blocked scenario

11. **Produce actionable remediation**
   - For every gap, provide a control-level remediation with owner and priority.
   - Avoid vague advice such as "review governance" or "check security".

## Output Format

```md
# AI Governance Review — [Use Case or Project Name]
**Reviewed by:** Ask EA (AI governance overlay)
**Review date:** [date]
**Primary review type:** [BRD review / HLD review / intake / standalone]
**AI relevance:** [YES / NO]
**Governance verdict:** [NOT APPLICABLE / COMPLIANT / CONDITIONALLY COMPLIANT / NON-COMPLIANT / PROHIBITED]

---

## Executive Summary
[2-4 sentences summarising AI relevance, risk tier, key governance finding, and immediate decision]

---

## AI Use Case Classification

| Item | Assessment | Evidence |
|------|------------|----------|
| AI-related | [Yes/No] | [evidence from the document] |
| AI pattern | [GenAI / RAG / Copilot / Agent / ML / Workflow automation] | [evidence] |
| Agent type | [Advisory / Knowledge / Workflow / Transactional / Autonomous] | [evidence] |
| Risk tier | [Tier 0 / Tier 1 / Tier 2 / Tier 3] | [why] |

---

## Data Governance Assessment

| Item | Status | Finding |
|------|--------|---------|
| Source data classification | [Public / Internal / Confidential / Restricted / Unknown] | [finding] |
| PII or restricted data exposure | [PASS / WARN / FAIL] | [finding] |
| Masking or tokenisation | [PASS / WARN / FAIL] | [finding] |
| Output classification inheritance | [PASS / WARN / FAIL] | [finding] |
| UAE residency / cross-border processing | [PASS / WARN / FAIL] | [finding] |

---

## Reference Architecture Conformance

| Layer | Status | Finding | Required Action |
|------|--------|---------|-----------------|
| UI Layer | [PASS/WARN/FAIL] | [finding] | [action] |
| AI Layer | [PASS/WARN/FAIL] | [finding] | [action] |
| Orchestration | [PASS/WARN/FAIL] | [finding] | [action] |
| Integration | [PASS/WARN/FAIL] | [finding] | [action] |
| Security | [PASS/WARN/FAIL] | [finding] | [action] |
| Data Access | [PASS/WARN/FAIL] | [finding] | [action] |
| Monitoring | [PASS/WARN/FAIL] | [finding] | [action] |

---

## AI Governance Gates

| Gate | Status | Finding |
|------|--------|---------|
| Use case documented | [Done / Partial / Missing] | [finding] |
| Risk tier assigned | [Done / Partial / Missing] | [finding] |
| Data inventory completed | [Done / Partial / Missing] | [finding] |
| Data protection assessed | [Done / Partial / Missing] | [finding] |
| Security review initiated | [Done / Partial / Missing] | [finding] |
| Human-in-the-loop defined | [Done / Partial / Missing] | [finding] |
| Model Card started | [Done / Partial / Missing] | [finding] |
| Success metrics defined | [Done / Partial / Missing] | [finding] |
| Retirement criteria set | [Done / Partial / Missing] | [finding] |
| Kill-switch designed | [Done / Partial / Missing] | [finding] |
| AI Team sign-off obtained | [Done / Partial / Missing] | [finding] |

---

## Required Approvals

| Approval Body | Required | Reason | Status |
|--------------|----------|--------|--------|
| Enterprise Architecture | [Y/N] | [reason] | [Pending / Obtained / N/A] |
| AI Team | [Y/N] | [reason] | [Pending / Obtained / N/A] |
| Security Team | [Y/N] | [reason] | [Pending / Obtained / N/A] |
| Data Governance Office | [Y/N] | [reason] | [Pending / Obtained / N/A] |
| Change Advisory Board | [Y/N] | [reason] | [Pending / Obtained / N/A] |

---

## Prohibited or High-Risk Findings

- [finding 1]
- [finding 2]

---

## Remediation Actions

| # | Gap | Action | Owner | Priority |
|---|-----|--------|-------|----------|
| 1 | [gap] | [specific control or design action] | [owner] | [H/M/L] |

---

## Final Decision

**Decision:** [NOT APPLICABLE / COMPLIANT / CONDITIONALLY COMPLIANT / NON-COMPLIANT / PROHIBITED]
**Reason:** [clear rationale]
**Next step:** [what should happen before build, review, or approval proceeds]
```

## Evaluation Rubric

| Criterion | Weight | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|----------|--------|----------|--------------|---------------|
| AI relevance detection | 15% | Misclassifies non-AI or AI use case | Detects AI relevance but with weak rationale | Correctly distinguishes applicable vs non-applicable cases with evidence |
| Risk tier accuracy | 20% | Tier assignment is arbitrary or unsafe | Tier assigned with partial reasoning | Tier assigned correctly with evidence and policy alignment |
| Control coverage | 20% | Misses key controls like HITL, masking, logging, or kill-switch | Covers some controls | Covers all major controls relevant to the case |
| Approval path accuracy | 15% | Missing or wrong approvers | Basic approval path listed | Approval path is complete and correctly justified |
| Remediation specificity | 20% | Generic actions | Some concrete actions | Control-level actions with owner and priority |
| Prohibited case detection | 10% | Fails to detect blocked scenarios | Flags some serious issues | Reliably detects Tier 0 and other hard-stop conditions |

## Test Cases

### TC-01: Tier 2 RAG Copilot
- **Input:** Internal policy Q&A assistant using governed connectors, no write-back, internal documents only
- **Expected output:** AI relevance = Yes, agent type = Knowledge, tier = Tier 2, verdict = Conditionally Compliant or Compliant depending on missing gates

### TC-02: Tier 1 Transactional Agent
- **Input:** Agent that writes approval results into SAP using confidential records
- **Expected output:** Agent type = Transactional, tier = Tier 1, HITL mandatory, Security and AI Team approval required

### TC-03: Tier 0 Prohibited Scenario
- **Input:** Autonomous deployment agent using public LLM and no human review
- **Expected output:** Verdict = Prohibited, tier = Tier 0, no further progression allowed

### TC-04: Restricted Data Misuse
- **Input:** AI proposal using personal records as direct prompt input
- **Expected output:** Restricted data failure, masking requirement fail, governance verdict = Non-Compliant or Prohibited

### TC-05: Low-Risk Productivity Use Case
- **Input:** Meeting summariser with no write-back and internal notes only
- **Expected output:** Tier = Tier 3, approval path minimal, no high-risk controls beyond approved tooling and logging

## Human Approval Points

- Ask EA's governance result is advisory and must not be treated as the formal approval record.
- Any Tier 0 or Tier 1 conclusion must be reviewed by a human EA or AI governance owner before it is communicated as a final decision.
- If restricted data, cross-border transfer, or production write-back is involved, Security and Data Governance review cannot be waived.
