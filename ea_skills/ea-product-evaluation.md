---
skill_id: ea-product-evaluation
name: Product Evaluation
version: "1.0"
trigger_keywords:
  - vendor
  - product
  - cots
  - rfp
  - compare platforms
  - compare tools
  - product evaluation
  - technology selection
  - product comparison
  - vendor comparison
  - evaluate product
  - evaluate vendor
  - vendor evaluation
  - select vendor
  - product shortlist
  - make or buy
  - build or buy
  - reuse before build
priority: 5
active: true
---

## Description

Product Evaluation provides structured, Gartner-style technology assessments for DEWA procurement decisions, applying the DEWA Reuse Before Build principle. It produces scored comparison matrices, TCO estimates, and TOGAF-aligned recommendations to support EA Board and procurement committee decisions.

**Standards:** Gartner-style product assessment, TOGAF, DEWA Reuse Before Build
**Discovered from:** "I want to build an AI assistant for our procurement team that uses RAG over our vendor contracts and"

## Trigger Conditions

- User asks to compare, evaluate, or shortlist technology products or vendors
- User asks about COTS selection, RFP evaluation criteria, or technology selection
- User is choosing between platforms, tools, or vendors for a specific DEWA use case
- User references 'Reuse Before Build', make-vs-buy, or platform rationalisation
- User asks for a product assessment or vendor scoring framework

## Inputs

| Input              | Type         | Required  | Description |
|--------------------|--------------|-----------|-------------|
| user_query        | text        | required | The user's question or uploaded document content |
| dewa_context      | reference   | optional | DEWA EA knowledge base — systems inventory, principles (auto-loaded) |
| use_case          | text        | optional | Specific DEWA use case the product must serve (e.g., 'customer self-service portal') |
| candidate_products| text        | optional | Comma-separated list of products or vendors to compare |
| dewa_standards    | reference   | optional | DEWA technology standards and approved vendor list (auto-loaded) |

## Process Steps

1. **Define evaluation scope**: Identify the use case, stakeholders, decision timeline, and budget envelope.
   - Confirm whether this is a new capability (Build/Buy) or a replacement (Reuse/Migrate)
2. **Apply DEWA Reuse Before Build principle**: Check the DEWA systems inventory and approved product list first.
   - If an existing DEWA system covers ≥70% of requirements, recommend Reuse with a gap analysis
3. **Define evaluation criteria**: Establish weighted criteria aligned to DEWA EA standards.
   - Functional fit (30%), Technical architecture fit (25%), Security & compliance (20%), TCO (15%), Vendor viability (10%)
   - Adjust weights based on the specific use case and DEWA's strategic priorities
4. **Score each product/vendor**: Assess each candidate against the defined criteria on a 1–5 scale.
   - Reference Gartner Magic Quadrant position where available
   - Check DEWA's approved vendor list and any existing contracts that may apply
5. **Perform TCO analysis**: Estimate 3-year total cost of ownership for each candidate.
   - Include licence, implementation, integration, training, and ongoing support costs
6. **Assess integration complexity**: Evaluate how each product integrates with the DEWA systems landscape.
   - Prefer products with standard API (REST/SOAP) connectors to DEWA's integration layer
   - Flag any proprietary integration requirements as risks
7. **Check security and compliance**: Verify each product against DEWA cybersecurity standards.
   - UAE data residency requirements, ISO 27001, IEC 62443 (for OT systems where applicable)
8. **Produce recommendation**: Rank products, state the recommended choice with rationale, and define the next step.
   - Include a risk table for the recommended option
   - Flag if an EA Board or procurement committee submission is required

## Output Format

```
# Product Evaluation — [Use Case]
**Decision required by:** [date]   **Budget envelope:** AED [X]M

## Evaluation Matrix

| Criterion               | Weight | [Product A] | [Product B] | [Product C] |
|-------------------------|--------|-------------|-------------|-------------|
| Functional fit          | 30%    | 4           | 3           | 5           |
| Technical architecture  | 25%    | 3           | 4           | 3           |
| Security & compliance   | 20%    | 5           | 4           | 4           |
| TCO (3-year)           | 15%    | 3           | 5           | 2           |
| Vendor viability        | 10%    | 4           | 3           | 4           |
| **Weighted score**      |        | **3.75**    | **3.70**    | **3.80**    |

## TCO Comparison (3-Year, AED)

| Cost Category  | [Product A] | [Product B] | [Product C] |
|----------------|-------------|-------------|-------------|
| Licence        | [amount]    | [amount]    | [amount]    |
| Implementation | [amount]    | [amount]    | [amount]    |
| **Total**      | [total]     | [total]     | [total]     |

## Recommendation
**Recommended:** [Product X] — [rationale in 2–3 sentences]
**Next step:** [Proceed to RFP / EA Board submission / Proof of Concept]

## Risk Summary
| Risk                  | Severity | Mitigation                    |
|-----------------------|----------|-------------------------------|
| [integration risk]    | H/M/L    | [mitigation]                  |
```

## Evaluation Rubric

| Criterion                      | Weight | 1 (Poor)                                      | 3 (Adequate)                                  | 5 (Excellent) |
|--------------------------------|--------|-----------------------------------------------|-----------------------------------------------|---------------|
| Criteria relevance            | 20%    | Generic criteria not specific to DEWA        | Standard criteria with partial DEWA context  | Criteria explicitly tied to DEWA EA standards and strategic priorities |
| Scoring evidence              | 25%    | Scores with no justification                 | Scores with brief rationale                  | Scores with specific product capability evidence and DEWA context |
| TCO accuracy                  | 20%    | No cost analysis                             | High-level cost comparison only              | Itemised 3-year TCO per product including integration and support costs |
| DEWA ecosystem fit            | 20%    | No reference to existing DEWA systems        | Some integration notes                       | Integration complexity assessed against full DEWA systems landscape |
| Recommendation clarity        | 15%    | No clear recommendation                      | Recommendation without rationale             | Ranked recommendation with rationale, risks, and next step |

## Test Cases

### TC-01: Customer Portal Platform Selection
- **Input:** "Compare Salesforce, ServiceNow, and Microsoft Dynamics for DEWA's customer service portal."
- **Expected output:** Scored matrix with all three products; UAE data residency check; integration with SAP CRM/ISU noted; TCO comparison.
- **Pass criteria:** All 5 criteria scored for each product; DEWA data residency requirement checked; recommendation with next step

### TC-02: Reuse Before Build Check
- **Input:** "We need a document management system — should we buy SharePoint or build one?"
- **Expected output:** Check existing DEWA systems first; if SharePoint or similar exists in inventory, Reuse recommendation with gap analysis.
- **Pass criteria:** DEWA inventory check performed; if existing system found, Reuse recommendation with gap %; Build only if <70% coverage

### TC-03: OT Security Product
- **Input:** "Evaluate vendors for industrial control system security monitoring in our grid infrastructure."
- **Expected output:** IEC 62443 compliance check added to criteria; OT-specific vendors (Claroty, Dragos, Nozomi) in evaluation; on-prem preference for OT data.
- **Pass criteria:** IEC 62443 in security criteria; OT data residency requirement flagged; ≥2 OT-specialist vendors evaluated

## Human Approval Points

- Product evaluations for systems with a 3-year TCO >AED 1M must be reviewed by the DEWA EA Manager before the recommendation is submitted to procurement
- Any product touching OT/industrial control systems must be reviewed by the DEWA OT Security team before selection
- Recommendations that deviate from DEWA's approved vendor list require explicit EA Board endorsement

## Notes

This skill file was auto-generated by Ask EA Skill Discovery on initial adoption.
Run the Skill Improvement Loop (`/improve-skill ea-product-evaluation`) to further enrich
it with DEWA-specific depth based on real evaluation data.
