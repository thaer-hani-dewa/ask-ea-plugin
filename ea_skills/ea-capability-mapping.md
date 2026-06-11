---
skill_id: ea-capability-mapping
name: Capability Mapping
version: "1.0"
trigger_keywords:
  - capability map
  - business capability
  - heatmap
  - operating model
  - capability assessment
priority: 5
active: true
---

## Description

Capability Mapping analyses DEWA's business capabilities against strategic objectives, producing heat-mapped assessments that surface gaps, duplication, and investment priorities aligned with DEWA's digital transformation agenda and EA Framework 4.0. Outputs feed directly into the DEWA EA investment planning cycle and EA Board presentations.

**Standards:** TOGAF Business Architecture, EA Framework 4.0
**Discovered from:** "Can you create a capability map for DEWA customer operations including billing and field service capabilities?"

## Trigger Conditions

- User asks to create a capability map, business capability model, or operating model
- User asks which capabilities are weak, missing, or duplicated across DEWA divisions
- User asks how capabilities align to DEWA 2030 strategy, Smart Dubai, or Net Zero 2050
- User uploads an organisational design or strategy document requiring capability assessment
- User references operating model, capability maturity, or heatmap in any context

## Inputs

| Input              | Type         | Required  | Description |
|--------------------|--------------|-----------|-------------|
| user_query        | text        | required | The user's question or uploaded document content |
| dewa_context      | reference   | optional | DEWA EA knowledge base — systems inventory, principles (auto-loaded) |
| business_unit     | text        | optional | DEWA division or function scope (e.g., Customer Operations, Grid Management) |
| strategic_goals   | reference   | optional | DEWA strategic objectives to map capabilities against (auto-loaded) |

## Process Steps

1. **Identify scope and purpose**: Determine which DEWA business domain the capability map covers and what decision it supports.
   - Clarify if scope is enterprise-wide or limited to a specific function
   - Identify the strategic objectives the map must align to (DEWA 2030, Smart Dubai, Net Zero 2050)
2. **Define capability taxonomy**: Establish the capability hierarchy for the domain.
   - Level 1: Core domain capabilities (e.g., Customer Engagement, Asset Management, Grid Operations)
   - Level 2: Sub-capabilities (e.g., Meter Reading, Billing, Fault Management)
   - Align taxonomy to TOGAF Business Architecture categories and DEWA EA Framework 4.0
3. **Assess current capability maturity**: Score each capability 1–5.
   - 1 = Non-existent or ad hoc  |  3 = Defined and repeatable  |  5 = Optimised and data-driven
   - Reference DEWA systems inventory to identify which systems support each capability
4. **Identify capability gaps**: Compare current maturity against target state required by strategic objectives.
   - Flag capabilities below target maturity as gaps; flag those with no supporting system as critical gaps
5. **Detect duplication and redundancy**: Identify where multiple systems or teams serve the same capability.
   - Cross-reference the DEWA systems inventory for overlapping functional coverage
6. **Prioritise investment areas**: Rank gaps by strategic impact and maturity deficit.
   - Apply DEWA's Reuse Before Build principle: classify each gap as Build, Buy (COTS), or Reuse
   - Use a 2×2 grid: Strategic Importance vs. Capability Gap Size
7. **Render the capability heat map**: Produce a structured table with colour-coded maturity ratings.
   - 🔴 Critical Gap (deficit > 2)  |  🟠 Needs Improvement (1–2)  |  🟢 Adequate  |  🔵 Exceeds Target
8. **Governance alignment**: Identify which capability investment recommendations require EA Board review or an investment committee submission.

## Output Format

```
# Capability Map — [Domain Name]
**Scope:** [Enterprise / Division / Function]   **Date:** [date]
**Strategic alignment:** [DEWA strategy references]

## Capability Heat Map

| Capability (L1)     | Sub-capability (L2)  | Current | Target | Gap  | Priority | Supporting System(s)   |
|---------------------|----------------------|---------|--------|------|----------|------------------------|
| Customer Engagement | Meter Reading        | 3       | 4      | 🟠 1 | Medium   | MDMS, SAP ISU          |
| ...                 | ...                  | ...     | ...    | ...  | ...      | ...                    |

## Gap Summary

| Priority | Capability       | Gap | Action        | DEWA Principle          |
|----------|------------------|-----|---------------|-------------------------|
| High     | [capability]     | [n] | Build/Buy/Reuse | Reuse Before Build     |

## Strategic Alignment

| DEWA Goal              | Required Capabilities | Current Coverage | Gap Risk |
|------------------------|-----------------------|-----------------|----------|
| [e.g., Net Zero 2050]  | [capabilities]        | [%]             | H/M/L    |

## Recommendations
1. [Highest-priority investment with Build/Buy/Reuse rationale]
2. [Second priority]
3. [Third priority]
```

## Evaluation Rubric

| Criterion                      | Weight | 1 (Poor)                                      | 3 (Adequate)                                  | 5 (Excellent) |
|--------------------------------|--------|-----------------------------------------------|-----------------------------------------------|---------------|
| Capability taxonomy quality   | 20%    | Flat list, no hierarchy                      | Two-level hierarchy defined                  | L1/L2 aligned to TOGAF Business Architecture |
| Maturity scoring rigour       | 20%    | Scores with no evidence                      | Scores with general rationale                | Scores with specific system/process evidence from DEWA inventory |
| DEWA systems linkage          | 20%    | No reference to DEWA systems                 | Some systems named                           | Every capability mapped to a specific DEWA system or gap flagged |
| Strategic alignment           | 15%    | No link to DEWA goals                        | Generic strategy reference                   | Each gap mapped to a specific DEWA 2030 / Smart Dubai objective |
| Recommendation actionability  | 15%    | Vague priorities                             | Priorities stated without rationale          | Build/Buy/Reuse per capability with effort estimate and owner |
| Governance alignment          | 10%    | No governance noted                          | Governance mentioned generically             | Specific DEWA EA governance gates identified for each investment |

## Test Cases

### TC-01: Customer Operations Domain
- **Input:** "Create a capability map for DEWA customer operations including billing, complaints, and digital self-service."
- **Expected output:** Heat map with ≥3 L1 capabilities; SAP ISU, MyDEWA, CRM identified; alignment to smart customer experience.
- **Pass criteria:** Map has L1/L2 hierarchy; ≥2 capabilities linked to DEWA systems; ≥1 capability gap identified

### TC-02: Detecting Duplication
- **Input:** "We think field operations and customer service overlap — map overlapping capabilities."
- **Expected output:** Map showing overlapping sub-capabilities; duplicate system support identified; Reuse recommendation.
- **Pass criteria:** Duplication section present; ≥1 Reuse recommendation in gap summary

### TC-03: Strategic Gap for Net Zero
- **Input:** "What capabilities do we need to support DEWA Net Zero 2050?"
- **Expected output:** ≥3 Net Zero-related capabilities; maturity scores; Build/Buy options; governance notes for major investments.
- **Pass criteria:** ≥3 capabilities with maturity scores; Build vs Buy options stated; governance flag if >AED 1M implied

## Human Approval Points

- Any 'High' priority capability investment must be reviewed by the EA Manager before entering the DEWA investment plan
- Capability maps identifying a critical gap requiring a new major system (>AED 1M estimated) require EA Board presentation
- Capabilities flagged as critical gaps in customer-facing services must be validated by the relevant DEWA business owner

## Notes

This skill file was auto-generated by Ask EA Skill Discovery on initial adoption.
Run the Skill Improvement Loop (`/improve-skill ea-capability-mapping`) to further enrich
it with DEWA-specific depth based on real evaluation data.
