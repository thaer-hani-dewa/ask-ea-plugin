---
skill_id: ea-architecture-diagram
name: Architecture Diagram Generation
version: 1.0
trigger_keywords:
  - architecture diagram
  - high level architecture diagram
  - integration view
  - draw architecture
  - visual representation
  - openflowkit
priority: high
active: true
---

# Architecture Diagram Generation

## Description

Use this skill when the user asks Ask EA to produce a DEWA-compliant solution architecture diagram while staying in the Ask EA conversation. The skill should preserve the BRD analysis context, reuse earlier findings from the same chat, and generate a diagram-oriented response aligned with DEWA's 5-layer architecture and approved template style.

## Trigger Conditions

Activate when the user asks to:

- create or generate an architecture diagram
- produce a high-level architecture diagram from a BRD
- show an integration view or system context diagram
- draw the proposed solution architecture
- generate a visual 5-layer architecture representation

## Inputs

- the current user prompt
- any uploaded BRD or requirements document
- earlier Ask EA analysis already produced in the same conversation
- DEWA standards, system inventory, and integration guidance
- the approved EA Architecture Diagram template as the visual baseline

## Process Steps

1. Reuse the current Ask EA context first.
   - Summarize the relevant business objective, systems, integrations, risks, and assumptions already established in the conversation.
   - Do not ask the user to repeat information already available in the same chat unless there is a real gap.

2. Map the solution to DEWA's mandatory 5-layer architecture.
   - Channels / Users
   - Front-end
   - Application
   - Middleware
   - Back-end / Data

   Also choose the best primary diagram family for the use case:
   - solution integration view for business applications, APIs, and system reuse
   - network and security view for trust zones, SSO, DMZ, or gateway concerns
   - cloud platform view for cloud-native, container, or landing-zone patterns
   - infrastructure deployment view for servers, clusters, HA, DR, and hosting topology

3. Identify DEWA-specific architecture content for the diagram.
   - existing systems to reuse
   - APIs and integration paths
   - middleware or gateway layer
   - data stores and master systems
   - identity, security, and network boundaries

4. Produce a diagram-ready architecture description.
   - list components by layer
   - show key interactions and data flows
   - identify external/internal systems
   - show security boundaries, integration boundaries, and operational notes

5. If a rendered diagram is requested or supported, generate output that can be passed to OpenFlowKit or another rendering layer.
   - keep naming consistent with DEWA standards
   - favor a clean executive-friendly view first
   - provide a more detailed integration view only when useful

6. Close with diagram assumptions and any missing information.
   - note unresolved components
   - note where business or solution owner confirmation is required

## Output Format

Structure the answer in this order:

1. Diagram Intent
2. Architecture Layers
3. Key Components and Integrations
4. Security and Governance Notes
5. Diagram Assumptions

If possible, also include a diagram-ready block or rendered visual reference.

## Quality Checklist

Before finalizing, verify the response includes:

- a complete 5-layer mapping
- DEWA system reuse opportunities
- middleware/API integration path
- security or trust boundary notes
- enough structure for downstream diagram rendering

## Evaluation Rubric

Score highly only if the output:

- stays consistent with the earlier Ask EA conversation and BRD analysis
- is visually structured and diagram-oriented rather than generic prose
- reflects DEWA architecture standards and ecosystem knowledge
- clearly separates layers, components, and integrations
- is strong enough to support an executive-facing architecture visual
