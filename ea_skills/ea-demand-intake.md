---
skill_id: ea-demand-intake
name: EA Demand Intake & Classification
version: "1.0"
trigger_keywords:
  - new demand
  - project request
  - demand classification
  - intake
  - triage
  - demand form
  - classify demand
  - categorise
  - categorize
priority: 5
active: true
---

## Description

The Demand Intake skill classifies and triages incoming project demands to determine the appropriate level of EA engagement, required deliverables, and recommended timeline. It extracts demand metadata, assesses strategic alignment with DEWA's digital agenda, assigns an EA effort tier (Tier 1–3), and produces a structured classification report that the EA team uses to prioritise and assign incoming work. This skill ensures every project gets the right level of architecture governance from day one.

## Trigger Conditions

- Explicit: User submits a "new demand", "project request", or "intake form"
- Explicit: User asks "classify this demand", "triage this project", "what EA deliverables do we need?"
- Implicit: User describes a new project and asks what the EA process involves
- Implicit: User provides a demand description with requestor and purpose details

## Inputs

| Input                | Type   | Required | Description                                                              |
|----------------------|--------|----------|--------------------------------------------------------------------------|
| demand_description   | text   | required | The project or demand description from the requestor                     |
| requestor_department | text   | optional | Department submitting the demand                                         |
| project_sponsor      | text   | optional | Executive sponsor name or role                                           |
| requested_date       | text   | optional | Target delivery date (for timeline assessment)                           |
| estimated_budget     | text   | optional | Estimated project budget (for effort tier calibration)                  |

## Process Steps

1. **Extract demand metadata**: Project name (or generate a working title), requestor department, project sponsor, estimated budget, and target delivery date.

2. **Classify demand type** — assign one of these 5 types:
   - **New System**: Building or procuring a net-new system or capability
   - **Enhancement**: Adding features or upgrading an existing DEWA system
   - **Integration**: Connecting two or more existing systems (new data flow or API)
   - **Decommission**: Retiring or replacing an existing system
   - **Study**: Architecture study, feasibility analysis, or proof of concept

3. **Assess strategic alignment** — score 1–5 on how strongly the demand aligns with each DEWA strategic pillar:
   - Customer Experience (digital self-service, customer empowerment)
   - Operational Excellence (automation, efficiency, cost reduction)
   - Innovation & Intelligence (AI/ML, data analytics, smart infrastructure)
   - Infrastructure Modernisation (cloud migration, legacy retirement, resilience)
   - Sustainability (smart grid, energy efficiency, environmental initiatives)

   Report top 2 pillars and an overall Strategic Alignment Score (1–5).

4. **Assign EA Effort Tier** based on demand complexity and strategic impact:
   - **Tier 1 — Light Touch**: Simple enhancement, minor integration, or study. EA review only (no HLD required). Effort: 1–3 days EA time.
   - **Tier 2 — Standard**: New integration, significant enhancement, or mid-scale new system. HLD required. EA involvement in solution design. Effort: 1–3 weeks EA time.
   - **Tier 3 — Full Engagement**: Major new system, platform replacement, cross-domain integration, or AI/data platform. Full architecture engagement: BRD review, HLD, impact analysis, compliance check, technology selection, and architecture board presentation. Effort: 4–12 weeks EA time.

5. **Identify required EA deliverables** per tier:
   - Tier 1: Demand classification, EA recommendation memo
   - Tier 2: BRD review (if not already complete), HLD review, compliance check
   - Tier 3: All Tier 2 deliverables plus: impact analysis, technology assessment, architecture board pack, EA sign-off certificate

6. **Recommend EA assigned owner**: Based on demand domain (integration, data, infrastructure, AI, customer-facing), recommend the appropriate EA specialist or team.

7. **Estimate timeline**: Based on tier, deliverables required, and backlog context, estimate realistic EA engagement timeline.

8. **Produce Demand Classification Report**.

## Demo Upgrade: Structured Intake Gate

Before finalising the demand classification, force a structured intake gate:

- Explicitly justify the selected demand type using at least 2 signals from the request.
- Explicitly justify the EA effort tier using complexity, cross-domain impact, and business criticality.
- Name the required governance checkpoints up front:
  - EA Lead review for all demands
  - Data Governance Committee when external data sharing, analytics vendors, or master data movement is involved
  - OT Security review whenever the demand touches smart grid, SCADA, or operational technology
- End with the first 3 actions, each with an owner and expected timing.

## Mandatory Quality Checks

Before sending the final answer, verify that the output contains:

1. Demand type with evidence
2. Tier with evidence
3. Required EA deliverables
4. Named governance approvals
5. First 3 actions with owners

## Output Format

```
# EA Demand Classification Report
**Reference:** EA-[YYYY]-[XXX]
**Classified by:** Ask EA (AI-assisted intake)
**Classification date:** [date]
**Requestor:** [department / sponsor]

---

## Demand Summary

| Field                  | Value                                                   |
|------------------------|---------------------------------------------------------|
| Working title          | [generated or provided title]                           |
| Demand type            | [New System / Enhancement / Integration / Decommission / Study] |
| Requestor department   | [department]                                            |
| Project sponsor        | [sponsor or role]                                       |
| Estimated budget       | [budget or "Not provided"]                              |
| Target delivery date   | [date or "Not provided"]                                |

---

## Strategic Alignment

| DEWA Strategic Pillar          | Alignment Score | Rationale                                   |
|-------------------------------|-----------------|---------------------------------------------|
| Customer Experience           | [1-5]           | [why]                                       |
| Operational Excellence        | [1-5]           | [why]                                       |
| Innovation & Intelligence     | [1-5]           | [why]                                       |
| Infrastructure Modernisation  | [1-5]           | [why]                                       |
| Sustainability                | [1-5]           | [why]                                       |

**Overall Strategic Alignment Score:** [X.X / 5.0]
**Primary alignment:** [top pillar]
**Secondary alignment:** [second pillar]

---

## EA Classification

**Effort Tier:** Tier [1/2/3] — [Light Touch / Standard / Full Engagement]
**Classification rationale:** [2–3 sentences explaining why this tier was selected]

---

## Required EA Deliverables

| Deliverable                  | Required | Estimated EA Effort | Notes                                |
|------------------------------|----------|---------------------|--------------------------------------|
| Demand classification        | Y        | 0.5 days            | This document                        |
| BRD review                   | [Y/N]    | [effort]            | [condition if conditional]           |
| HLD review                   | [Y/N]    | [effort]            | [condition]                          |
| Impact analysis              | [Y/N]    | [effort]            | [condition]                          |
| Compliance check             | [Y/N]    | [effort]            | [condition]                          |
| Technology assessment        | [Y/N]    | [effort]            | [condition]                          |
| Architecture board pack      | [Y/N]    | [effort]            | [condition — Tier 3 only]            |
| EA sign-off certificate      | [Y/N]    | [effort]            | [condition]                          |

**Total estimated EA effort:** [X–Y days / weeks]

---

## EA Engagement Timeline

| Phase                         | Start              | Duration          | Dependency                         |
|-------------------------------|--------------------|-------------------|------------------------------------|
| BRD review (if required)      | [On demand receipt] | [duration]       | BRD submitted by requestor         |
| HLD review (if required)      | [After BRD approval] | [duration]      | Approved BRD                       |
| Impact analysis (if required) | [With HLD]         | [duration]        | HLD draft available                |
| Compliance check              | [With HLD]         | [duration]        | HLD draft available                |
| Architecture board submission | [After reviews]    | [duration]        | All review artefacts complete      |
| EA sign-off                   | [After board]      | [duration]        | Board approval                     |

---

## Recommended EA Owner

**Primary EA contact:** [role — e.g., Integration Architect / Data Architect / EA Lead]
**Rationale:** [why this specialist is the right owner for this demand type]
**Backup contact:** [secondary EA team member role]

---

## Initial Risk Flags

[Any early-stage risks or concerns identified at intake — e.g., tight timeline, budget mismatch with scope, cross-domain complexity, vendor involvement]
```

## Evaluation Rubric

| Criterion                    | Weight | 1 (Poor)                                             | 3 (Adequate)                                          | 5 (Excellent)                                                   |
|------------------------------|--------|------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| Classification accuracy      | 25%    | Wrong demand type assigned                           | Correct demand type for clear-cut cases               | Correct demand type with explicit rationale for borderline cases |
| Strategic alignment scoring  | 20%    | Alignment scores not justified                       | Scores given with brief rationale                     | Scores given with specific evidence from demand description and DEWA strategy |
| Effort tier justification    | 20%    | Tier assigned without rationale                      | Tier assigned with general rationale                  | Tier assigned with specific criteria: complexity, strategic impact, cross-domain scope |
| Deliverables completeness    | 20%    | Deliverables list is incomplete or generic           | Correct deliverables identified for the tier          | Correct deliverables with effort estimates and dependencies     |
| Timeline realism             | 15%    | Timeline not provided or unrealistic                 | Timeline provided but without dependency mapping      | Realistic timeline with explicit dependencies and EA backlog consideration |

## Test Cases

### TC-01: New Mobile App Demand
- **Input:** "Customer Experience department requests a new DEWA Smart Home mobile app that integrates with smart meters, MDMS, and MyDEWA account data. Budget: AED 2M. Target: Q4."
- **Expected output:** Type = New System; Tier 3; Customer Experience and Innovation & Intelligence as top pillars; all Tier 3 deliverables required; recommended owner = Mobile/Integration Architect
- **Pass criteria:** Tier = 3; at least 6 deliverables listed; timeline spans 8–12 weeks minimum

### TC-02: Legacy System Decommission
- **Input:** "We want to retire the legacy DEWA SMS gateway and migrate all SMS sending to the new notification service."
- **Expected output:** Type = Decommission; Tier 2; Operational Excellence primary pillar; deliverables = BRD review, impact analysis, compliance check, HLD review; risk flag for existing integrations to legacy gateway
- **Pass criteria:** Type = Decommission; impact analysis = Required; at least one risk flag about integration migration

### TC-03: Minor Enhancement
- **Input:** "Add a PDF download button to the existing bill history page in MyDEWA portal."
- **Expected output:** Type = Enhancement; Tier 1; Customer Experience primary; deliverables = classification only + EA recommendation memo; EA effort 0.5–1 day
- **Pass criteria:** Tier = 1; no HLD or architecture board required; total EA effort <= 1 day

### TC-04: Strategic Transformation Demand
- **Input:** "COO office requests a study for migrating all DEWA enterprise systems to a cloud-native microservices architecture over 5 years. Budget TBD."
- **Expected output:** Type = Study; Tier 3; all 5 pillars have high alignment; full Tier 3 deliverables; timeline 12+ weeks for the study phase alone; architecture board pack required
- **Pass criteria:** Tier = 3; Strategic Alignment >= 4.0; architecture board pack = Required

### TC-05: Vendor-Led Integration
- **Input:** "A new energy analytics vendor needs access to DEWA smart meter data via an API. They have their own cloud platform in Europe."
- **Expected output:** Type = Integration; Tier 2 (with P2 data sovereignty flag escalating to near-Tier 3); risk flags for data sovereignty (European cloud) and vendor API security; compliance check required; Data Governance Committee approval flagged
- **Pass criteria:** P2/data sovereignty risk explicitly flagged; Data Governance Committee mentioned; compliance check = Required

## Human Approval Points

- The EA Demand Classification Report must be reviewed and approved by the EA Lead Architect before it is sent to the requestor department — AI generates the draft, EA Lead confirms
- For Tier 3 demands, the Project Sponsor must acknowledge the EA timeline and effort before engagement begins — the AI-generated classification is used as the basis for this discussion
- Demands touching DEWA OT systems (SCADA, smart grid infrastructure) must be flagged to the OT Security team at intake, regardless of tier
