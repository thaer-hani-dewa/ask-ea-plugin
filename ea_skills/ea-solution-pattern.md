---
skill_id: ea-solution-pattern
name: Solution Pattern Recommendation
version: "1.0"
trigger_keywords:
  - solution pattern
  - architecture pattern
  - reference architecture
  - pattern library
  - best practice architecture
  - recommended pattern
  - what pattern
  - integration pattern
priority: 6
active: true
---

## Description

The Solution Pattern skill recommends the most appropriate DEWA-approved reference architecture patterns for a given solution domain and use case. It matches the solution scenario to DEWA's pattern library, presents the top 3 candidate patterns with a structured comparison, recommends the primary pattern with justification, and maps the required approved DEWA technologies and existing systems for each pattern. This skill prevents teams from designing solutions from scratch when a proven, approved reference architecture already exists.

## Trigger Conditions

- Explicit: User asks for a "solution pattern", "architecture pattern", "reference architecture"
- Explicit: User asks "what pattern should I use for X?"
- Implicit: User describes a solution type (web portal, IoT pipeline, data warehouse, AI system) and asks for architecture guidance
- Implicit: User asks about DEWA best practices for a specific technology domain

## Inputs

| Input                | Type   | Required | Description                                                               |
|----------------------|--------|----------|---------------------------------------------------------------------------|
| solution_description | text   | required | Description of what the solution needs to do                              |
| solution_domain      | text   | optional | Domain hint: web/mobile, integration, data, IoT, AI/ML, security, SaaS   |
| constraints          | text   | optional | Known constraints: on-prem only, existing system reuse, budget, timeline  |
| current_systems      | text   | optional | Existing DEWA systems already in scope                                    |

## Process Steps

1. **Identify solution domain**: Classify the solution into one of DEWA's primary architecture domains based on the description:
   - **Customer-Facing Web/Mobile**: Self-service portals, mobile apps, customer dashboards
   - **Enterprise Integration**: System-to-system data exchange, API-first connectivity, event-driven messaging
   - **Data & Analytics**: Data warehouse, data lake, reporting, business intelligence
   - **IoT & Smart Infrastructure**: Smart meters, sensors, edge computing, real-time telemetry
   - **AI/ML & Intelligent Systems**: AI decision support, machine learning pipelines, predictive analytics
   - **Identity & Access Management**: Authentication, authorisation, SSO, directory services
   - **Infrastructure Modernisation**: Cloud migration, containerisation, infrastructure-as-code

2. **Match to DEWA reference architecture patterns** — for the identified domain, identify the top 3 applicable patterns from DEWA's pattern library:

   **Customer-Facing Web/Mobile patterns:**
   - PAT-01: Progressive Web App on DEWA Private Cloud (React/Vue + .NET Core API + Oracle + DEWA API Gateway + ADFS SSO)
   - PAT-02: Native Mobile App with Backend-for-Frontend (Flutter/React Native + BFF microservice + API Gateway + Azure AD B2C)
   - PAT-03: Headless Portal Pattern (decoupled front end + CMS + API composition layer + DEWA legacy system facade)

   **Enterprise Integration patterns:**
   - PAT-04: API-First Integration (REST APIs via DEWA API Gateway + OpenAPI spec + API versioning strategy)
   - PAT-05: Event-Driven Messaging (Azure Service Bus + event-driven microservices + SAP iDOC for SAP integrations)
   - PAT-06: Batch File Integration (SFTP/FTPS + Azure Blob staging + ADF pipeline + validation layer)

   **Data & Analytics patterns:**
   - PAT-07: Modern Data Warehouse (Azure Synapse Analytics + ADF ingest + Power BI reporting layer + row-level security)
   - PAT-08: Lambda Architecture (hot path: Azure Event Hub + Stream Analytics; cold path: ADLS Gen2 + Spark + Synapse)
   - PAT-09: Operational Data Store (ODS pattern — near-real-time integrated view for operational reporting)

   **IoT & Smart Infrastructure patterns:**
   - PAT-10: IoT Edge-to-Cloud Pipeline (IoT Edge devices + MQTT broker + Azure IoT Hub + Time Series DB + dashboards)
   - PAT-11: Smart Meter Analytics (MDMS integration + DLMS/COSEM protocol adapter + real-time analytics + AMI head-end)
   - PAT-12: OT/IT Integration Bridge (Purdue model security zones + OSIsoft PI bridge + Azure IoT Hub for cloud analytics)

   **AI/ML & Intelligent Systems patterns:**
   - PAT-13: AI-Assisted Decision Support (LM Studio on-prem LLMs + RAG over knowledge base + human-in-the-loop workflow + audit log)
   - PAT-14: ML Pipeline (Azure ML or Databricks + feature store + model registry + A/B testing + drift monitoring)
   - PAT-15: Intelligent Document Processing (document extraction + classification + human review queue + structured output to ERP)

3. **Compare top 3 patterns**: For each candidate pattern, assess:
   - Fit to requirements (High/Medium/Low)
   - Implementation complexity (High/Medium/Low)
   - DEWA technology alignment (percentage of approved components)
   - Reuse of existing DEWA systems (High/Medium/Low)
   - Time to first value
   - Operational risk

4. **Recommend primary pattern**: Select the pattern with the best balance of fit, low complexity, high DEWA alignment, and high reuse. Provide explicit justification.

5. **Map required DEWA systems and technologies**: For the recommended pattern, list each component with the DEWA-approved technology, whether an existing DEWA system covers it, and any procurement needed.

6. **List known risks and mitigations**: For the recommended pattern, list the top 3 implementation risks with mitigations.

## Output Format

```
# Solution Pattern Recommendation — [Solution Name]
**Recommended by:** Ask EA (AI-assisted pattern matching)
**Date:** [date]
**Solution domain:** [domain]
**Primary recommendation:** [PAT-XX: Pattern Name]

---

## Solution Context
[2–3 sentences summarising what the solution needs to do and the key constraints that shaped the pattern selection]

---

## Pattern Comparison

| Attribute                    | [PAT-XX: Pattern A]    | [PAT-XX: Pattern B]    | [PAT-XX: Pattern C]    |
|------------------------------|------------------------|------------------------|------------------------|
| Fit to requirements          | [H/M/L]                | [H/M/L]                | [H/M/L]                |
| Implementation complexity    | [H/M/L]                | [H/M/L]                | [H/M/L]                |
| DEWA technology alignment    | [%]                    | [%]                    | [%]                    |
| Existing DEWA systems reuse  | [H/M/L]                | [H/M/L]                | [H/M/L]                |
| Time to first value          | [estimate]             | [estimate]             | [estimate]             |
| Operational risk             | [H/M/L]                | [H/M/L]                | [H/M/L]                |

---

## Primary Recommendation: [PAT-XX — Pattern Name]

**Why this pattern:**
[3–5 bullet points explaining why this pattern was selected over the alternatives]

**Pattern overview:**
[Architecture description — which components are in each layer, how data flows, where security controls are applied]

---

## Technology Stack for Recommended Pattern

| Architecture Component    | DEWA Approved Technology        | Existing DEWA System?   | Action Required                        |
|---------------------------|----------------------------------|-------------------------|----------------------------------------|
| [component name]          | [technology]                     | [Yes: system name / No] | [Reuse / Configure / Procure / Build]  |

---

## DEWA Systems to Reuse or Integrate

| System                    | Role in this Pattern             | Integration Type                        |
|---------------------------|----------------------------------|-----------------------------------------|
| [DEWA system name]        | [what it does in this pattern]   | [API / Event / Batch / Auth / Data]     |

---

## Implementation Risks & Mitigations

| Risk                              | Likelihood | Impact | Mitigation                                   |
|-----------------------------------|------------|--------|----------------------------------------------|
| [risk]                            | [H/M/L]    | [H/M/L] | [specific mitigation]                       |

---

## Next Steps

1. [First concrete action — e.g., raise demand, submit BRD, schedule HLD workshop]
2. [Second action]
3. [Third action]
```

## Evaluation Rubric

| Criterion                    | Weight | 1 (Poor)                                             | 3 (Adequate)                                          | 5 (Excellent)                                                   |
|------------------------------|--------|------------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------|
| Domain identification        | 20%    | Wrong domain identified or no classification         | Correct domain identified                             | Correct domain with sub-domain specificity (e.g., IoT edge vs. smart meter) |
| Pattern relevance            | 25%    | Patterns recommended are generic (not DEWA-specific) | Relevant patterns but without DEWA context            | DEWA-specific patterns recommended with PAT-XX references       |
| Comparison quality           | 20%    | Comparison table missing or incomplete               | Comparison covers key attributes                      | All 6 attributes compared; clear winner identified from comparison logic |
| Technology currency          | 20%    | Technologies mentioned are not on DEWA approved list | DEWA-approved technologies used but not all current   | All technologies from current DEWA approved list; versions specified |
| DEWA systems mapping         | 15%    | No mapping to existing DEWA systems                  | Some DEWA systems mentioned                           | All applicable DEWA systems mapped with integration type and reuse assessment |

## Test Cases

### TC-01: Web Self-Service Portal
- **Input:** "We need a new customer self-service portal where DEWA customers can view their bills, report faults, track meter readings, and apply for new connections."
- **Expected output:** Domain = Customer-Facing Web; Primary = PAT-01 or PAT-02; Technology stack includes DEWA API Gateway, ADFS SSO, Oracle DB, .NET Core API; MyDEWA, MDMS, SAP ISU listed as systems to integrate; PAT-03 headless as alternative
- **Pass criteria:** 3 patterns compared; API Gateway and ADFS mentioned; SAP ISU integration point identified

### TC-02: Real-Time IoT Pipeline
- **Input:** "We need to collect readings from 50,000 smart meters every 15 minutes, detect anomalies in real-time, and store historical data for analytics."
- **Expected output:** Domain = IoT & Smart Infrastructure; Primary = PAT-10 or PAT-11; MDMS for meter integration; time-series DB for storage; real-time stream analytics; OT/IT segmentation noted
- **Pass criteria:** PAT-10 or PAT-11 recommended; MDMS listed in systems; OT/IT security zone mentioned; time-series storage in technology stack

### TC-03: Enterprise Data Warehouse
- **Input:** "We need a single source of truth for DEWA operational data — billing, customer, metering, field force — to support executive dashboards and regulatory reporting."
- **Expected output:** Domain = Data & Analytics; Primary = PAT-07 or PAT-08; Azure Synapse or similar; ADF for ingestion from SAP ISU, MDMS, CRM; Power BI for dashboards; row-level security for multi-department access
- **Pass criteria:** Data warehouse pattern; SAP ISU and MDMS as source systems; Power BI or approved BI tool; row-level security mentioned

### TC-04: Microservices API Platform
- **Input:** "We want to modernise DEWA's integration landscape from point-to-point interfaces to an API-first microservices platform."
- **Expected output:** Domain = Enterprise Integration; Primary = PAT-04 or PAT-05; DEWA API Gateway as central; event-driven via Azure Service Bus; OpenAPI specs; API versioning strategy; migration path from legacy point-to-point
- **Pass criteria:** PAT-04 or PAT-05; DEWA API Gateway central to the pattern; migration strategy from legacy integrations mentioned

### TC-05: AI-Assisted Decision System
- **Input:** "We want an AI assistant that helps EA team members review BRD documents, check compliance, and recommend architecture patterns — it should run on-premise using DEWA's own LLMs."
- **Expected output:** Domain = AI/ML & Intelligent Systems; Primary = PAT-13 (AI Decision Support with on-prem LLMs); LM Studio + RAG over DEWA KB; human-in-the-loop workflow; audit log requirement; Ask EA cited as reference implementation
- **Pass criteria:** PAT-13 recommended; on-prem LLM (LM Studio) in technology stack; RAG pattern mentioned; audit log requirement noted

## Human Approval Points

- Pattern recommendations are advisory; the EA Lead Architect must confirm the primary pattern recommendation before it is used as the basis for an HLD or procurement
- If the recommended pattern requires a technology that is not yet on the DEWA approved list, the EA Technology Board must approve the technology before the pattern is adopted
- If the solution involves OT/smart infrastructure (IoT patterns PAT-10, PAT-11, PAT-12), the DEWA OT security team must validate the security zone design before HLD proceeds
