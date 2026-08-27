---
title: Open review comments
---

# Open review comments

Fifty unresolved threads from the source document, with their real Google comment IDs.
Sixteen of these were dropped by the original migration and every one of those is from February.

When a comment is applied, add `status: applied` and the commit hash beside it, and mark the row in
`ASEPD_Open_Comments_Tracker.xlsx`.

!!! note "Anchoring"
    The Google export does not expose which text each comment was attached to, so these could not be
    placed back inline automatically. They are listed here by rank. Place each one as you work through it.

---

## Rank LML version

### `AAAB60w8-zg`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Relationship freeze (T15), all filters (T17,T18)

> modify for version LML 1.4 because I later found that Innoslate employs LML 1.4

- [ ] applied

## Rank Relationship corrections

### `AAAB4xFXrvE`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Freeze (T15)

> incorrect. "sourced by"

> **Sadaf Shaikh replied:** System Req (sourced by) Trade Study

- [ ] applied

### `AAAB5d3-5l8`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Freeze (T15), V&V design

> what about tracing to system requirements?

> **Sadaf Shaikh replied:** System Req (verified by) Verification Req

- [ ] applied

### `AAAB4xlgcPg`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Freeze (T15)

> Risk (references) trade study

- [ ] applied

### `AAAB4xlgcPk`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Freeze (T15)

> Risk (caused by) Requirement

- [ ] applied

### `AAAB4xlgcPw`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Freeze (T15)

> RIsk caused by Asset
> Risk caused by Requirement

- [ ] applied

### `AAAB6feBJ4M`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Freeze (T15)

> replace allocated to with "performs". 
> 
> Asset (performs) Action

- [ ] applied

### `AAAB6wHzTy4`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15)

> component asset "references" trade study

- [ ] applied

### `AAAB6wHzTzA`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15)

> Action uses Resource

- [ ] applied

### `AAAB6wHzTzI`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15), interface guidance

> Asset connects to Conduit

- [ ] applied

### `AAAB6wHzTzY`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15), guidelines (T45)

> there should be downstream relationships emanating from the decision (could be an asset or requirement or action)
> 
> need to make fixes in guidelines to incorporate this

- [ ] applied

### `AAAB6wHzTzc`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15), risk guidance

> component cannot resolve a risk. Risk is resolved by decision and component should be linked to that decision.

- [ ] applied

### `AAAB60w8-zU`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15), action diagram guidance

> This should be "traced from"
> 
> in stage 3 under "Low-level action diagrams":
> 
> if they are serving as requirements, the same relationship should appear
> 
> if they serve as design choice, use Action "satisfies" Requirement relationship

- [ ] applied

### `AAAB4xFXrqw`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15), trade study guidance

> resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Issue, and Decision enabled by Trade Study.

> **Sadaf Shaikh replied:** so Replace relationship between trade study and risk(modelled as issue) with decision and risk.  trade study (enables) decision (resolves) issue (modelled as issue)

- [ ] applied

### `AAAB4xFXrrE`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15)

> Use case/scenario (traced from) Stakeholder requirement.

- [ ] applied

### `AAAB5d3-5l0`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15), V&V design

> Add instructions for creating relationship: Stakeholder req (verified by) Verification Req

- [ ] applied

### `AAAB4xFXrrk`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15)

> incorrect. "traced from"

> **Sadaf Shaikh replied:** System Req (traced from) Stakeholder Req

- [ ] applied

### `AAAB3YKxxYg`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15)

> derived reqs (sourced by) the trade study (avoid trade study is traced from derived reqs)
> 
> in the triangle:
> - upstream requirement
> - trade study
> - downstream requirement
> 
> t satisfies u
> d sourced by t
> d traced from u

- [ ] applied

### `AAAB4xlgcPo`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Freeze (T15)

> modify instructions according to the following principle:
> 
> in the triangle:
> - upstream requirement
> - trade study
> - downstream requirement
> 
> 
> t satisfies u
> d sourced by t
> d traced from u

- [ ] applied

## Rank Document inconsistency

### `AAAB60w8-zM`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Guidelines revision (T45), compliance queries

> MAJOR PROBLEM:
> 
> this is correct. Look for consistency in the deliverables document as well as in these guidelines.

- [ ] applied

### `AAAB60w8-zo`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Guidelines revision (T45)

> Invert this so students are not confused when comparing with the deliverable guidelines

- [ ] applied

### `AAAB60w8-3Q`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Guidelines revision (T45)

> this needs to be consistent with the rest of the guidelines in all the documents.

- [ ] applied

## Rank Labels for filters

### `AAAB5eBvJ7o`

- **Sadaf Shaikh**, 2026-05-07
- Blocks: Template project (T19) — EARLIER than the freeze

> also, add the label "Selected component" for easy filtering when we create traceability matrix between functional requirements and selected components

- [ ] applied

### `AAAB6wHzTzk`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Template project (T19)

> also, add label "Analysis" to this artifact to be able to filter out just the analyses artifacts

- [ ] applied

## Rank SRD auto-link gap

### `AAAB5eL9tMg`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Traceability standups (T24), quality scan (T25)

> write instructions on establishing links between actions/assets and requirements generated by SRD because "Generate SRD" doesnt automatically create these links

- [ ] applied

## Rank Missing instructions

### `AAABzzIlFO0`

- **Sadaf Shaikh**, 2026-02-06
- Blocks: Guidelines (T45)

> mention standard naming convention

- [ ] applied

### `AAABzzIlFRc`

- **Sadaf Shaikh**, 2026-02-06
- Blocks: Guidelines (T45)

> No relationship that makes sense to me

- [ ] applied

### `AAAB57gYWUk`

- **Sadaf Shaikh**, 2026-05-08
- Blocks: Guidelines (T45)

> future iteration: no instructions given to create relationship between system and subsystem requirements

- [ ] applied

### `AAAB6feBJ5M`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Guidelines (T45)

> provide instructions on deriving system technical requirements.
> 
> take inspiration from stage 3 technical requirements instructions.

- [ ] applied

### `AAAB57gYWLs`

- **Sadaf Shaikh**, 2026-05-15
- Blocks: Guidelines (T45)

> if the generated subsystem functional requirement is related to the technical requirement, add the technical requirement to the same functional requirement
> 
> create traceability with upstream requirement (system) from stage 2 
> 
> technical requirement in SRD (specified by) Measure

> **Sadaf Shaikh replied:** -technical requirements should be created manually in the SRD along with their associated measure entities

- [ ] applied

### `AAAB6wHzTzQ`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Guidelines (T45)

> add some explanation/context

- [ ] applied

### `AAAB6wHzTzg`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Guidelines (T45)

> add after this:
> issue "references" Analysis Artifact called "Design Analysis Report"

- [ ] applied

## Rank Canvas reporting

### `AAABzy-qwug`

- **Munzir Zafar**, 2026-02-06
- Blocks: Deliverable templates (T92)

> Need a template for allowing students to easily populate the deliverables for canvas submission

> **Munzir Zafar replied:** see this chatgpt conversation for details https://chatgpt.com/share/69858d38-40a0-8001-81a5-bb744606d549

- [ ] applied

### `AAABzy-qwus`

- **Munzir Zafar**, 2026-02-06
- Blocks: Deliverable templates (T92)

> traceability of user needs to extracts needs to be generated in a form that can be made part of the report to be submitted

- [ ] applied

### `AAABzy-qwuM`

- **Munzir Zafar**, 2026-02-06
- Blocks: Deliverable templates (T92)

> Each Notes Document (or each statement inside it) should include:
> 
> Stakeholder name and ID (given in stakeholders list)
> 
> Stakeholder role / perspective
> 
> Context (meeting, site visit, email, etc.)

> **Munzir Zafar replied:** should create a template for this as well

> **Sadaf Shaikh replied:** can we just relate the stakeholder entity with this document and add context in the description?

> **Sadaf Shaikh replied:** why a template?

- [ ] applied

### `AAAB6wHzT2I`

- **Sadaf Shaikh**, 2026-05-21
- Blocks: Deliverable templates (T92)

> Look at all the deliverables in this stage for missing reporting instructions for Canvas.

- [ ] applied

## Rank Deferred by author

### `AAAB57gYWJ0`

- **Sadaf Shaikh**, 2026-05-08

> future iteration: stakeholder req -> scenarios ->action diagrams (some decomposition)
> add stakeholder functional requirements from the action diagram

- [ ] applied

### `AAAB57gYWJ8`

- **Sadaf Shaikh**, 2026-05-08

> future iteration: after concept is finalized, we think of more solution-dep scenarios -> more action diagrams -> system functional requirements from added actions (these should be documented separately)

- [ ] applied

### `AAAB5eL9tNY`

- **Sadaf Shaikh**, 2026-05-08

> modify this instruction to add a separate Measure entity for the selected component

> **Sadaf Shaikh replied:** future iteration: technical requirement in SRD (specified by) Measure (satisfied by) selected component (specified by) Measure

- [ ] applied

## Rank Content and pedagogy

### `AAABzUWr0R4`

- **Sadaf Shaikh**, 2026-02-03
- Blocks: Freeze (T15), helpful not blocking

> Ailiya to make a separate table on a subset of relationships between entities from LML specification

- [ ] applied

### `AAABzUWr0Tw`

- **Sadaf Shaikh**, 2026-02-03

> Mention of an earlier exercise done on risk and issue.

- [ ] applied

### `AAABzurITFc`

- **Sadaf Shaikh**, 2026-02-04

> should we keep it in this section?

- [ ] applied

### `AAABvWHEtbE`

- **Ailiya Fatima**, 2026-02-09

> why not use import analyzer here

- [ ] applied

### `AAABvWHEtbI`

- **Ailiya Fatima**, 2026-02-09

> how to add this to innoslate

- [ ] applied

### `AAABzXMVlDs`

- **Sadaf Shaikh**, 2026-02-10

> pg 87 of real-mbse book

- [ ] applied

### `AAAB0D17Il8`

- **Sadaf Shaikh**, 2026-02-10

> elaborate on the attributes for each of these entities

- [ ] applied

### `AAAB0D17ImI`

- **Sadaf Shaikh**, 2026-02-10

> should be added in the appendix

- [ ] applied

### `AAAB0D17ImM`

- **Sadaf Shaikh**, 2026-02-10

> needs to be reviewed

- [ ] applied

### `AAAB0D17ImY`

- **Sadaf Shaikh**, 2026-02-10

> think about this

- [ ] applied

### `AAAB0EbNaqM`

- **Sadaf Shaikh**, 2026-02-11

> as is architecture captured as context diagram?

> **Sadaf Shaikh replied:** list of scenarios for both?

> **Sadaf Shaikh replied:** list of scenarios for to-be only

- [ ] applied
