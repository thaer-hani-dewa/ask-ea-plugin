---
skill_id: ea-brd-review
name: BRD Completeness Review
version: "1.0"
trigger_keywords:
  - BRD
  - business requirement
  - business case
  - requirement document
  - project brief
  - review the brd
  - analyse the brd
  - analyze the brd
  - upload and identify
priority: 1
active: true
---

## Description

The BRD Completeness Review skill performs a systematic, structured assessment of Business Requirements Documents against DEWA's Enterprise Architecture standards. It scores each BRD section on a 1–5 scale, identifies missing or weak elements, and produces an executive summary with actionable recommendations. This skill is the primary intake quality gate for all projects requiring EA involvement.

## Trigger Conditions

- Explicit: User uploads or pastes a BRD document (PDF, Word, PowerPoint)
- Explicit: User types "review BRD", "analyse BRD", "check BRD completeness"
- Implicit: User references "business requirements", "project brief", or "business case" and asks for analysis
- Implicit: Attached document content contains section headers typical of BRDs (Objectives, Scope, Stakeholders, Requirements)

## Inputs

| Input            | Type           | Required | Description                                                       |
|------------------|----------------|----------|-------------------------------------------------------------------|
| brd_content      | text/document  | required | The BRD text or extracted document content (from PDF/DOCX/PPTX)  |
| project_context  | text           | optional | Additional background — project name, sponsor, target date        |
| dewa_standards   | reference      | optional | Relevant DEWA EA principle references (auto-loaded from KB)       |

## Process Steps

1. **Extract and inventory document structure**: Identify all section headers and sub-sections present in the BRD. List them explicitly.

2. **Identify key project metadata**: Extract project name, project sponsor, target go-live date, requestor department, and project type (New System / Enhancement / Integration / Decommission).

3. **Map against DEWA EA BRD completeness checklist** — evaluate each of these 7 mandatory sections:
   - Business Drivers & Strategic Alignment (link to DEWA strategy)
   - Current State Description (as-is systems, pain points)
   - Target State Vision (to-be capability)
   - Gap Analysis (what changes are needed)
   - Integration Points (which DEWA systems are affected or consumed)
   - Non-Functional Requirements (performance, security, availability, scalability)
   - EA Governance Sign-off Path (who must approve, which boards)

4. **Score each section 1–5**:
   - 1 = Missing entirely
   - 2 = Mentioned only (no detail)
   - 3 = Present but incomplete (key sub-elements missing)
   - 4 = Mostly complete (minor gaps)
   - 5 = Fully complete and aligned with DEWA standards

5. **Identify missing or weak elements**: For every section scoring 1–3, list the specific sub-elements missing and provide a concrete example of what good content looks like.

6. **Cross-check integration points**: Verify any DEWA systems named actually exist in the DEWA systems inventory. Flag unknown or ambiguous system names.

7. **Flag risks**: Identify any requirements that introduce security, data sovereignty, or vendor lock-in risks per DEWA EA principles.

8. **Produce executive summary**: Overall completeness score (weighted average), top 3 gaps, top 3 recommendations, and recommended next step (Ready for HLD / Needs revision / Refer back to business).

## Output Format

```
# BRD Completeness Review — [Project Name]
**Reviewed by:** Ask EA (AI-assisted review)
**Review date:** [date]
**Overall Completeness Score:** [X.X / 5.0] ([percentage]%)
**Review verdict:** [READY FOR HLD | NEEDS REVISION | REFER BACK TO BUSINESS]

---

## Executive Summary
[2–3 sentences covering: what was reviewed, overall quality, critical gaps, recommended next step]

---

## Section Completeness Scores

| Section                              | Score | Status         | Key Gap                          |
|--------------------------------------|-------|----------------|----------------------------------|
| Business Drivers & Strategic Alignment | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |
| Current State Description            | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |
| Target State Vision                  | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |
| Gap Analysis                         | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |
| Integration Points                   | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |
| Non-Functional Requirements          | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |
| EA Governance Sign-off Path          | [1-5] | [PASS/WARN/FAIL] | [gap or "Complete"]             |

---

## Missing Elements — Detail

### [Section name — if score <= 3]
**Score:** [X/5]
**Missing:** [specific sub-elements not present]
**What good looks like:** [concrete example of complete content]

---

## Integration Point Verification

| System Named in BRD | Status in DEWA Inventory | Flag |
|---------------------|--------------------------|------|
| [system name]       | [Confirmed / Not found / Ambiguous] | [note] |

---

## Risk Flags

| Risk                     | Category                 | DEWA Principle Reference      | Severity |
|--------------------------|--------------------------|-------------------------------|----------|
| [risk description]       | [Security/Data/Vendor/Governance] | [principle]          | [H/M/L] |

---

## Top 3 Recommendations

1. [Most critical gap and how to fix it]
2. [Second most critical gap]
3. [Third most critical gap]

---

## Next Step

**Recommended action:** [READY FOR HLD REVIEW | REVISE AND RESUBMIT | ESCALATE TO BUSINESS OWNER]
**Suggested owner:** [EA team member role or department]
**Target completion:** [timeframe]
```

## Evaluation Rubric

| Criterion                    | Weight | 1 (Poor)                                          | 3 (Adequate)                                         | 5 (Excellent)                                             |
|------------------------------|--------|---------------------------------------------------|------------------------------------------------------|-----------------------------------------------------------|
| Section completeness scoring | 20%    | Scores assigned without justification             | Scores assigned with general rationale               | Scores assigned with specific evidence from BRD text      |
| DEWA standards alignment     | 20%    | No reference to DEWA EA standards                 | References DEWA standards generically                | Maps each gap to a specific DEWA EA principle or standard |
| Gap identification quality   | 20%    | Vague or generic gaps listed                      | Specific gaps identified but without improvement guidance | Specific gaps with concrete "what good looks like" examples |
| Recommendation specificity   | 15%    | Recommendations are generic ("add more detail")   | Recommendations are specific to the BRD             | Recommendations include owner, action, and timeframe      |
| Risk flagging                | 15%    | No risks identified even when present             | Risks identified but not categorised                 | Risks categorised, rated H/M/L, mapped to DEWA principles |
| Actionability                | 10%    | Review verdict not provided                       | Verdict provided without rationale                   | Verdict with clear rationale and recommended next step    |

## Test Cases

### TC-01: Complete BRD — Smart Meter Portal
- **Input:** A BRD for DEWA Smart Meter Customer Portal with all 7 sections fully populated, mentioning SAP ISU, MDMS, MyDEWA app, and AES-256 encryption requirement
- **Expected output:** Overall score 4.2–5.0; verdict READY FOR HLD; integration points confirmed for SAP ISU and MDMS; no critical gaps
- **Pass criteria:** All 7 sections scored 4 or 5; integration table shows SAP ISU and MDMS as "Confirmed"

### TC-02: Partial BRD — Missing NFRs
- **Input:** A BRD with good business context but no non-functional requirements section and no security requirements
- **Expected output:** NFR section scored 1; security risk flag raised; recommendation to add performance targets, availability SLA, and security classification
- **Pass criteria:** NFR section score <= 2; Risk Flags table contains at least one security entry; recommendation 1 addresses NFRs

### TC-03: BRD Without Integration Points
- **Input:** A BRD describing a new customer-facing web portal but with no mention of any DEWA backend systems
- **Expected output:** Integration Points section scored 1; recommendation to identify SAP CRM, identity provider (ADFS/Azure AD), and payment gateway connections
- **Pass criteria:** Integration Points score = 1; output explicitly names systems that should be identified

### TC-04: BRD With Wrong DEWA System Names
- **Input:** A BRD referencing "DEWA ERP", "customer database", and "legacy billing system" without using standard DEWA system names
- **Expected output:** Integration Point Verification table flags all three as "Ambiguous" or "Not found"; recommendation to align with DEWA systems inventory naming
- **Pass criteria:** Verification table shows flags; output does not silently accept the ambiguous names

### TC-05: One-Paragraph Stub BRD
- **Input:** "We need a mobile app for DEWA customers to pay bills and report faults."
- **Expected output:** All 7 sections scored 1; Overall score 1.0; verdict REFER BACK TO BUSINESS; detailed guidance on minimum BRD requirements
- **Pass criteria:** Overall score <= 1.5; verdict is REFER BACK; output provides the full completeness checklist as a starting template

## Human Approval Points

- Before escalating a REFER BACK verdict to the business owner, an EA reviewer must confirm the assessment is fair and not based on document parsing errors
- If the BRD references a strategic initiative (DEWA Digital Transformation Programme, Smart Dubai), a human EA reviewer must validate the strategic alignment score before it is communicated to the project team
- If a security risk is flagged at severity HIGH, it must be reviewed by the DEWA CISO team before the project proceeds to HLD
