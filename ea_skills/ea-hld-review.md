---
skill_id: ea-hld-review
name: HLD Architecture Review
version: "1.0"
trigger_keywords:
  - HLD
  - high level design
  - architecture review
  - solution design
  - architecture document
  - technical design
  - high-level design
priority: 2
active: true
---

## Description

The HLD Architecture Review skill performs a structured compliance assessment of High-Level Design documents against DEWA's 5-layer architecture standard, approved technology list, and reuse-first policy. It evaluates each architecture layer, flags non-compliant technology choices, identifies missed reuse opportunities for existing DEWA systems, and produces a layer-by-layer compliance report with a sign-off readiness checklist. This skill is the primary quality gate before any solution proceeds to detailed design and procurement.

## Trigger Conditions

- Explicit: User uploads or pastes an HLD document
- Explicit: User asks for "architecture review", "HLD review", "technical design review"
- Implicit: User describes a solution design with technology choices and asks if it is compliant
- Implicit: Document content contains DEWA 5-layer architecture terminology (Presentation, Application, Integration, Data, Infrastructure)

## Inputs

| Input              | Type           | Required | Description                                                                    |
|--------------------|----------------|----------|--------------------------------------------------------------------------------|
| hld_content        | text/document  | required | The HLD text or extracted document content                                     |
| project_context    | text           | optional | Project name, scope, requestor, target environment (on-prem/cloud/hybrid)     |
| dewa_tech_list     | reference      | optional | DEWA approved technology list (auto-loaded from KB)                            |
| dewa_systems_inv   | reference      | optional | DEWA systems inventory for reuse identification (auto-loaded from KB)          |

## Process Steps

1. **Identify solution scope**: Extract project name, type, target users, and deployment model (on-premises, cloud, hybrid, SaaS).

2. **Map the 5-layer architecture presence** — for each layer, assess whether it is addressed in the HLD:
   - **Presentation Layer**: User interfaces, web portals, mobile apps, dashboards
   - **Application Layer**: Business logic, microservices, APIs, workflows, AI/ML components
   - **Integration Layer**: ESB, API gateway, middleware, event streaming, data exchange formats
   - **Data Layer**: Databases, data warehouses, data lakes, caches, file storage
   - **Infrastructure Layer**: Compute, network, security zones, DR/HA strategy, container orchestration

3. **Technology compliance check**: For each technology named in the HLD, check against DEWA's approved technology list. Flag any technology that is:
   - Not on the approved list (needs architecture board approval)
   - Approved but not preferred (recommend preferred alternative)
   - Deprecated or under retirement at DEWA

4. **Reuse opportunity identification**: Cross-reference all new components proposed against the DEWA systems inventory. For each component, check if an existing DEWA-operated system could provide the same capability (e.g., proposing a new identity store when ADFS/Azure AD is available).

5. **Integration pattern review**: For every integration point, verify it uses approved patterns (REST API via DEWA API Gateway, SFTP for batch file transfer, Azure Service Bus for event-driven, SAP iDOC for SAP integrations). Flag direct DB-to-DB integrations or custom binary protocols.

6. **Security and resilience assessment**: Check for security zones, encryption at rest/in transit, authentication method (ADFS SSO / Azure AD MFA), network segmentation, backup strategy, and RTO/RPO targets.

7. **Score each layer 1–5** and compute overall compliance score.

8. **Produce layer-by-layer compliance report** with risk register and sign-off checklist.

## Output Format

```
# HLD Architecture Review — [Project Name]
**Reviewed by:** Ask EA (AI-assisted review)
**Review date:** [date]
**Overall Compliance Score:** [X.X / 5.0]
**Review verdict:** [APPROVED FOR DETAILED DESIGN | CONDITIONAL APPROVAL | REWORK REQUIRED]

---

## Executive Summary
[2–3 sentences: architecture overview, compliance status, critical issues, recommendation]

---

## 5-Layer Compliance Assessment

| Layer            | Present | Score | Status          | Key Finding                                    |
|------------------|---------|-------|-----------------|------------------------------------------------|
| Presentation     | [Y/N]   | [1-5] | [PASS/WARN/FAIL] | [finding or "Compliant"]                      |
| Application      | [Y/N]   | [1-5] | [PASS/WARN/FAIL] | [finding or "Compliant"]                      |
| Integration      | [Y/N]   | [1-5] | [PASS/WARN/FAIL] | [finding or "Compliant"]                      |
| Data             | [Y/N]   | [1-5] | [PASS/WARN/FAIL] | [finding or "Compliant"]                      |
| Infrastructure   | [Y/N]   | [1-5] | [PASS/WARN/FAIL] | [finding or "Compliant"]                      |

---

## Technology Compliance

| Technology Named     | DEWA Approval Status      | Recommendation                                    |
|----------------------|---------------------------|---------------------------------------------------|
| [tech name]          | [Approved/Not approved/Deprecated] | [Use as-is / Use preferred alternative: X / Requires board approval] |

---

## Reuse Opportunities

| Proposed Component        | Existing DEWA System         | Reuse Feasibility | Action Required                     |
|---------------------------|------------------------------|-------------------|-------------------------------------|
| [proposed component]      | [existing system]            | [High/Medium/Low] | [Replace with existing / Integrate with existing / New justified] |

---

## Integration Pattern Review

| Integration Point         | Pattern Used              | Status          | Recommended Pattern                  |
|---------------------------|---------------------------|-----------------|--------------------------------------|
| [integration description] | [pattern]                 | [PASS/WARN/FAIL] | [recommended pattern if non-compliant] |

---

## Security & Resilience Assessment

| Concern                      | Status          | Detail                                             |
|------------------------------|-----------------|----------------------------------------------------|
| Authentication method        | [PASS/WARN/FAIL] | [method used vs. ADFS/Azure AD SSO requirement]   |
| Encryption at rest           | [PASS/WARN/FAIL] | [what is encrypted, algorithm]                    |
| Encryption in transit        | [PASS/WARN/FAIL] | [TLS version, certificate management]             |
| Network segmentation         | [PASS/WARN/FAIL] | [zones defined, DMZ, internal separation]         |
| Backup & DR strategy         | [PASS/WARN/FAIL] | [RPO/RTO targets vs. DEWA standard]               |
| Data residency               | [PASS/WARN/FAIL] | [on-UAE vs. off-UAE data storage]                 |

---

## Risk Register

| Risk                         | Category       | Severity | DEWA Principle        | Mitigation                                     |
|------------------------------|----------------|----------|-----------------------|------------------------------------------------|
| [risk]                       | [Security/Compliance/Reuse/Performance] | [H/M/L] | [principle] | [mitigation action] |

---

## EA Sign-Off Checklist

- [ ] 5-layer architecture fully addressed
- [ ] All technologies on DEWA approved list (or board approval pending)
- [ ] Reuse opportunities documented (no unnecessary duplication)
- [ ] Integration via approved patterns only
- [ ] Security requirements met (auth, encryption, network zones)
- [ ] Data residency confirmed (UAE-hosted)
- [ ] RTO/RPO defined and aligned with DEWA BCM standards
- [ ] Architecture review approved by EA Lead Architect
- [ ] Technology selections approved by EA Technology Board (if new tech)

---

## Conditions / Actions Required

[If CONDITIONAL APPROVAL or REWORK, list specific conditions that must be met before approval]
```

## Evaluation Rubric

| Criterion                    | Weight | 1 (Poor)                                               | 3 (Adequate)                                           | 5 (Excellent)                                                   |
|------------------------------|--------|--------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------------------------|
| Layer coverage               | 20%    | Less than 3 of 5 layers assessed                       | All 5 layers mentioned but shallowly assessed          | All 5 layers thoroughly assessed with specific findings         |
| Technology compliance        | 20%    | Technologies not checked against DEWA approved list    | Some technologies checked                              | All named technologies checked, non-compliant ones flagged with alternatives |
| Reuse identification         | 20%    | No reuse opportunities identified                      | 1–2 reuse opportunities noted                          | All applicable reuse opportunities identified with feasibility scores |
| Integration pattern correctness | 15%  | Integration patterns not reviewed                      | Patterns reviewed but without DEWA standard reference  | All integration points evaluated against DEWA approved patterns |
| Security adequacy            | 15%    | Security section missing or only auth checked          | Auth, encryption checked; network and DR missing       | All 6 security concerns assessed with DEWA standard references  |
| Diagram completeness         | 10%    | No assessment of whether diagram is present/adequate   | Diagram presence noted                                 | Diagram assessed for layer coverage and integration visibility  |

## Test Cases

### TC-01: Fully Compliant HLD
- **Input:** HLD for a DEWA self-service portal using React frontend, .NET Core API, DEWA API Gateway, Oracle DB (approved), ADFS SSO, hosted on DEWA private cloud, with DR to secondary site
- **Expected output:** Overall score 4.5+; verdict APPROVED FOR DETAILED DESIGN; all layers present; all technologies confirmed approved; ADFS auth confirmed
- **Pass criteria:** Verdict is APPROVED; Technology Compliance table shows all items as "Approved"; sign-off checklist all checked

### TC-02: HLD Using Non-Approved Technology Stack
- **Input:** HLD proposing MongoDB (not on DEWA approved DB list), Kubernetes on AWS (cloud not approved without board approval), and Auth0 (not ADFS/Azure AD)
- **Expected output:** Verdict REWORK REQUIRED; 3 technology flags; recommendations to use Oracle/SQL Server, DEWA private cloud Kubernetes, ADFS/Azure AD
- **Pass criteria:** Technology Compliance table shows at least 3 non-approved flags; Auth0 flagged against ADFS standard; verdict is REWORK

### TC-03: HLD Missing Integration Layer
- **Input:** HLD describing frontend and backend components but with no mention of API gateway, middleware, or how DEWA legacy systems (SAP, MDMS) are connected
- **Expected output:** Integration Layer scored 1; flag for missing API gateway; recommendation to route all integrations through DEWA API Gateway
- **Pass criteria:** Integration Layer score = 1; specific recommendation for DEWA API Gateway

### TC-04: Cloud-First HLD vs On-Prem DEWA Standard
- **Input:** HLD proposing full deployment on Azure Public Cloud with data stored in Azure Southeast Asia region
- **Expected output:** Infrastructure Layer flagged; data residency FAIL (data outside UAE); recommendation for DEWA private cloud or Azure UAE region with data residency compliance
- **Pass criteria:** Data residency row in Security table shows FAIL; specific UAE data residency requirement cited

### TC-05: IoT Solution HLD
- **Input:** HLD for a smart grid IoT solution with edge devices, MQTT broker, time-series database, and analytics dashboard
- **Expected output:** All 5 layers assessed with IoT-specific findings; MQTT noted as acceptable for edge/OT but Azure Service Bus recommended for cloud integration; time-series DB checked against approved list; security zones assessed for OT/IT separation
- **Pass criteria:** OT/IT segmentation mentioned in Security; Integration layer addresses MQTT-to-cloud bridging; Data layer addresses time-series storage

## Human Approval Points

- Before issuing a CONDITIONAL APPROVAL or APPROVED verdict, the EA Lead Architect must review the AI-generated compliance report and sign off
- Any technology not on the DEWA approved list must go to the EA Technology Board for approval — the AI review flags it but the board makes the decision
- Data residency concerns (data outside UAE) must be escalated to DEWA CISO and DPO before any approval is issued
- If the solution touches OT/SCADA systems, the review must include the DEWA OT security team
