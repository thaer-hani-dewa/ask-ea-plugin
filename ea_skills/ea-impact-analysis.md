---
skill_id: ea-impact-analysis
name: Application & Integration Impact Analysis
version: "1.0"
trigger_keywords:
  - impact analysis
  - impact assessment
  - downstream systems
  - affected systems
  - change impact
  - integration impact
  - what systems
priority: 3
active: true
---

## Description

The Impact Analysis skill performs a structured assessment of how a proposed change (system upgrade, new integration, decommission, or configuration change) will affect upstream consumers and downstream dependencies across the DEWA application landscape. It categorises impact by type (data, process, integration, UI, security), rates severity per system, and produces a change sequencing recommendation to minimise risk during rollout.

## Trigger Conditions

- Explicit: User asks "what is the impact of changing X?", "run an impact analysis", "which systems will be affected?"
- Explicit: User describes a system change and asks about downstream effects
- Implicit: User discusses an upgrade, migration, or integration change for a named DEWA system
- Implicit: User mentions "affected systems", "integration dependencies", "downstream consumers"

## Inputs

| Input                | Type   | Required | Description                                                       |
|----------------------|--------|----------|-------------------------------------------------------------------|
| changed_component    | text   | required | The system, API, service, or data entity being changed            |
| change_description   | text   | required | What is changing (upgrade, API change, decommission, schema change) |
| change_scope         | text   | optional | Scope of change (data model, API contract, authentication, performance) |
| target_date          | text   | optional | Planned change date for sequencing recommendations                |

## Process Steps

1. **Identify the changed component**: Extract system name, component type (COTS system, custom service, API, database, identity provider), and change type (upgrade, decommission, schema change, API version change, config change).

2. **Classify impact dimensions** — for each potentially affected system, assess impact across 5 dimensions:
   - **Data impact**: Does the change alter data structures, formats, or availability that downstream systems depend on?
   - **Process impact**: Does the change alter business process flows, workflows, or business rules?
   - **Integration impact**: Does the change break or alter APIs, message formats, authentication flows, or middleware connections?
   - **UI impact**: Does the change affect user-facing screens, self-service portals, or mobile apps?
   - **Security impact**: Does the change alter authentication, authorisation, encryption, or access control?

3. **Identify affected systems from DEWA systems inventory**: Cross-reference the changed component against known DEWA system dependencies. For each affected system, determine:
   - Integration type (API consumer, data consumer, authentication dependency, UI federation)
   - Integration direction (upstream / downstream / bidirectional)
   - Business criticality (Mission Critical / Business Critical / Supporting)

4. **Rate impact severity per system** — for each affected system:
   - **High**: System will break or produce incorrect results without remediation before the change
   - **Medium**: System will degrade or require configuration update; can function in limited mode temporarily
   - **Low**: Minor change required; no user-visible impact; can be updated post-change

5. **Identify hidden dependencies**: Flag any systems that may be indirectly affected through shared databases, shared APIs, or shared authentication services. Note confidence level (Confirmed / Probable / Unknown).

6. **Estimate remediation effort** per system (T-shirt sizing: S = < 1 day, M = 1–5 days, L = 1–2 weeks, XL = > 2 weeks).

7. **Recommend change sequencing**: Propose a staged rollout order that minimises simultaneous high-severity impacts. Identify if a freeze period or change window is needed.

8. **Produce Impact Analysis Report**.

## Output Format

```
# Impact Analysis Report — [Change Description]
**Analysed by:** Ask EA (AI-assisted analysis)
**Analysis date:** [date]
**Changed component:** [system / component]
**Change type:** [Upgrade / Decommission / Schema change / API change / Config change]
**Total systems affected:** [count]
**High-severity impacts:** [count]

---

## Executive Summary
[2–3 sentences: what is changing, how many systems affected, severity distribution, key risks, rollout recommendation]

---

## Affected Systems Summary

| System               | Criticality | Impact Type(s)                | Severity | Remediation Effort | Dependency Confidence |
|----------------------|-------------|-------------------------------|----------|--------------------|-----------------------|
| [system name]        | [Mission/Business/Supporting] | [Data/Process/Integration/UI/Security] | [H/M/L] | [S/M/L/XL] | [Confirmed/Probable/Unknown] |

---

## Impact Detail by System

### [System Name] — [Severity: HIGH/MEDIUM/LOW]
**Criticality:** [Mission Critical / Business Critical / Supporting]
**Integration type:** [API consumer / Data consumer / Auth dependency / UI federation]
**Impact dimensions:**
- Data: [description or N/A]
- Process: [description or N/A]
- Integration: [specific API / message format / auth flow affected]
- UI: [description or N/A]
- Security: [description or N/A]

**Remediation required:** [specific action — e.g., "Update API client to v2.1", "Migrate to new OAuth2 endpoint", "Re-test batch file processing"]
**Estimated effort:** [S/M/L/XL]
**Owner:** [team or role]

---

## Hidden Dependencies

| System               | Indirect Dependency Path                      | Confidence  | Action                              |
|----------------------|-----------------------------------------------|-------------|-------------------------------------|
| [system]             | [path: system A -> shared DB -> system B]     | [C/P/U]     | [Verify and assess]                 |

---

## Change Sequencing Recommendation

**Recommended rollout order:**

1. **[Pre-change — Week -2]**: [Preparation actions — e.g., deploy API adapter, notify teams]
2. **[Change window — Day 0]**: [The core change]
3. **[Post-change — Day +1]**: [High-severity system updates]
4. **[Post-change — Week +1]**: [Medium-severity system updates]
5. **[Post-change — Week +4]**: [Low-severity cleanup and monitoring confirmation]

**Change window recommendation:** [Off-peak weekend / Business hours with rollback / Maintenance window required]
**Rollback trigger:** [Define condition that triggers rollback]

---

## Risk Assessment

| Risk                              | Probability | Impact | Mitigation                                          |
|-----------------------------------|-------------|--------|-----------------------------------------------------|
| [risk]                            | [H/M/L]     | [H/M/L] | [mitigation action]                               |
```

## Evaluation Rubric

| Criterion                    | Weight | 1 (Poor)                                               | 3 (Adequate)                                            | 5 (Excellent)                                                   |
|------------------------------|--------|--------------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------|
| System coverage              | 25%    | Only directly connected systems identified             | Direct dependencies identified; some indirect missed    | Direct and indirect dependencies mapped; confidence levels rated |
| Dependency tracing depth     | 20%    | Only surface-level connections traced                  | Integration types identified for most systems           | Full impact dimension analysis per system (data/process/integration/UI/security) |
| Severity calibration         | 20%    | All systems rated same severity                        | Severity differentiated by system type                  | Severity rated with specific technical rationale per system     |
| Sequencing logic             | 20%    | No sequencing recommended or random order              | Basic before/after change grouping                      | Detailed week-by-week rollout with rollback triggers and change window recommendation |
| Documentation of unknowns    | 15%    | No acknowledgement of unknown dependencies             | Some unknowns flagged                                   | All unknowns explicitly listed with confidence levels and investigation actions |

## Test Cases

### TC-01: SAP ISU Upgrade
- **Input:** "SAP ISU is being upgraded from 6.0 to 7.0. What systems are affected?"
- **Expected output:** Affected systems include MDMS (meter data), MyDEWA portal (billing display), CCC (customer care), payment gateway integrations; High severity for real-time billing integrations; Medium for reporting consumers; sequencing starts with adapter testing 2 weeks prior
- **Pass criteria:** At least 4 systems identified; at least 2 high-severity items; sequencing includes pre-change preparation phase

### TC-02: MDM System Schema Change
- **Input:** "We are changing the DEWA master customer data model — adding a new mandatory field for smart home enrollment. What is the impact?"
- **Expected output:** All systems consuming customer master data flagged (CRM, billing, MyDEWA, field force); data impact dimension for all; integration impact for API consumers; sequencing notes mandatory field requires all consumers updated before field is enforced
- **Pass criteria:** Data impact dimension flagged for all; sequencing warns about mandatory field rollout order

### TC-03: API Gateway Replacement
- **Input:** "We are replacing the DEWA API Gateway with a new vendor. All current REST APIs will need to be re-registered."
- **Expected output:** All systems using REST APIs through the gateway are affected; High severity for all external-facing APIs; process to re-register and update endpoint URLs; suggests API version freeze window
- **Pass criteria:** High severity for all systems using the gateway; specific action "update endpoint URLs" mentioned; change window recommended

### TC-04: Identity Provider Migration
- **Input:** "DEWA is migrating from on-prem ADFS to Azure AD for authentication. What are the integration impacts?"
- **Expected output:** All systems using ADFS SSO flagged; impact on SAML vs OAuth2/OIDC token format; MyDEWA portal, intranet, and all Azure-integrated apps need reconfiguration; security impact dimension for all; sequencing suggests test environment first
- **Pass criteria:** Security impact dimension for all; SAML-to-OIDC migration mentioned; at least 3 specific systems named

### TC-05: New Microservice Introduction
- **Input:** "We are introducing a new notification microservice that will replace all direct email/SMS calls from 5 applications."
- **Expected output:** The 5 applications identified as requiring integration updates (Medium severity each); new integration dependency created; no downstream breakage but change sequencing needed to avoid double notifications
- **Pass criteria:** All 5 applications listed; "double notification" risk flagged; sequencing addresses migration cutover

## Human Approval Points

- Impact analysis output must be reviewed by the EA Lead Architect before being shared with project teams to ensure no DEWA systems have been overlooked
- For changes rated High severity affecting Mission Critical systems (MDMS, SAP ISU, ADFS, API Gateway), the Change Advisory Board must approve the rollout plan
- Where dependency confidence is "Unknown" for any Mission Critical system, a technical investigation must be completed before change approval
