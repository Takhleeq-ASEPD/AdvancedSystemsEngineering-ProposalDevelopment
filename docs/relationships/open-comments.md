---
title: Open review comments
---

# Open review comments

Fifty unresolved threads from the source document. Each one carries **the exact text it was
attached to** and the file that text is in, so a change can be made in place rather than searched for.

Recovered by pairing the inline comment anchors in the source with the comment threads in document
order. 115 anchors, 115 threads, one to one.

!!! warning "Confidence"
    Anchors from April and May land precisely. February anchors may have drifted, because Google
    moves a comment's anchor when the text around it is edited and this document was restructured
    several times. Where the anchored text below does not obviously relate to the comment, trust
    the comment and re-read the section rather than trusting the anchor.

**Working rule:** fix each comment in place. Only propagate when the comment itself says to.
A consistency pass at the end catches the rest.

---

## 1 · LML version

### `AAAB60w8-zg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Relationship freeze (T15), all filters (T17,T18)

**Anchored on:**

> "satisfies"** | **

**Comment:**

> modify for version LML 1.4 because I later found that Innoslate employs LML 1.4

- [ ] applied

## 2 · Relationship corrections

### `AAAB6feBJ4M`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/2-system-concept/d3-system-requirements.md`
- **Section:** 2.
- **Blocks:** Freeze (T15)

**Anchored on:**

> Derive Requirements from Architecture & Trade Studies

**Comment:**

> replace allocated to with "performs".   Asset (performs) Action

- [x] applied

### `AAAB4xFXrvE`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/2-system-concept/d3-system-requirements.md`
- **Section:** 3. Create Required Relationships in Innoslate
- **Blocks:** Freeze (T15)

**Anchored on:**

> Create relationship **“derived from”** → Trade Study (Artifact)

**Comment:**

> incorrect. "sourced by"

> **Sadaf Shaikh replied:** System Req (sourced by) Trade Study

- [ ] applied

### `AAAB5d3-5l8`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/2-system-concept/d4-verification-requirements-document-for-system-requirements.md`
- **Section:** (none)
- **Blocks:** Freeze (T15), V&V design

**Anchored on:**

> Trace Verification Requirements to Test Cases (Optional)

**Comment:**

> what about tracing to system requirements?

> **Sadaf Shaikh replied:** System Req (verified by) Verification Req

- [ ] applied

### `AAAB4xlgcPk`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`
- **Section:** 2c. Create Pugh Matrix
- **Blocks:** Freeze (T15)

**Anchored on:**

> It's a good practice to be explicit about all assumptions underlying the scenario.

**Comment:**

> Risk (caused by) Requirement

- [ ] applied

### `AAAB4xlgcPg`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`
- **Section:** 3d. Add an Engineering Margin
- **Blocks:** Freeze (T15)

**Anchored on:**

> Final Specified Value** - Record the final specified value, computed by applying the margin factor to the derived value from Column 6. This is the value that enters the formal requirements document.

**Comment:**

> Risk (references) trade study

- [ ] applied

### `AAAB4xlgcPw`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Freeze (T15)

**Anchored on:**

> add a **“satisfies”** relationship to the subsystem requirements.

**Comment:**

> RIsk caused by Asset Risk caused by Requirement

- [ ] applied

### `AAAB4xFXrqw`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/1-requirements/d3-stakeholder-requirements-document.md`
- **Section:** Why this deliverable is important
- **Blocks:** Freeze (T15), trade study guidance

**Anchored on:**

> Create relationship of trade study with Issue using “resolves”.

**Comment:**

> resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Issue, and Decision enabled by Trade Study.

> **Sadaf Shaikh replied:** so Replace relationship between trade study and risk(modelled as issue) with decision and risk.  trade study (enables) decision (resolves) issue (modelled as issue)

- [ ] applied

### `AAAB4xFXrrE`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/1-requirements/d4-high-level-action-diagrams.md`
- **Section:** Why this deliverable is important
- **Blocks:** Freeze (T15)

**Anchored on:**

> Create relationship “satisfies” for every use case/scenario with the relevant functional requirements in the Stakeholder Requirements document.

**Comment:**

> Use case/scenario (traced from) Stakeholder requirement.

- [ ] applied

### `AAAB5d3-5l0`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/1-requirements/d5-verification-requirements-document-for-stakeholder-requirements.md`
- **Section:** Why this deliverable is important
- **Blocks:** Freeze (T15), V&V design

**Anchored on:**

> Trace to test cases (optional)

**Comment:**

> Add instructions for creating relationship: Stakeholder req (verified by) Verification Req

- [ ] applied

### `AAAB4xFXrrk`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/2-system-concept/d3-system-requirements.md`
- **Section:** 3. Create Required Relationships in Innoslate
- **Blocks:** Freeze (T15)

**Anchored on:**

> Create relationship **“allocated to”** → Action, Asset, or Subsystem (if defined)

**Comment:**

> incorrect. "traced from"

> **Sadaf Shaikh replied:** System Req (traced from) Stakeholder Req

- [ ] applied

### `AAAB3YKxxYg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`
- **Section:** 4a. Create the Trade Study Artifact
- **Blocks:** Freeze (T15)

**Anchored on:**

> dd a **“satisfies”** relationship to each relevant subsystem requirement.

**Comment:**

> derived reqs (sourced by) the trade study (avoid trade study is traced from derived reqs)  in the triangle: - upstream requirement - trade study - downstream requirement  t satisfies u d sourced by t d traced from u

- [ ] applied

### `AAAB6wHzTzc`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Freeze (T15), risk guidance

**Anchored on:**

> In Innoslate, create an Asset entity for each selected component. Record the following attributes: component name, manufacturer, model number, and a link to the datasheet as a reference artifact.

**Comment:**

> component cannot resolve a risk. Risk is resolved by decision and component should be linked to that decision.

- [ ] applied

### `AAAB4xlgcPo`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Freeze (T15)

**Anchored on:**

> component Asset entity using "related to" and to the affected requirement using "traced from."

**Comment:**

> modify instructions according to the following principle:  in the triangle: - upstream requirement - trade study - downstream requirement   t satisfies u d sourced by t d traced from u

- [ ] applied

### `AAAB60w8-zU`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15), action diagram guidance

**Anchored on:**

> Measure → Requirement

**Comment:**

> This should be "traced from"  in stage 3 under "Low-level action diagrams":  if they are serving as requirements, the same relationship should appear  if they serve as design choice, use Action "satisfies" Requirement relationship

- [ ] applied

### `AAAB6wHzTzY`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15), guidelines (T45)

**Anchored on:**

> Low -level Action Diagrams (Del. 1) |

**Comment:**

> there should be downstream relationships emanating from the decision (could be an asset or requirement or action)  need to make fixes in guidelines to incorporate this

- [ ] applied

### `AAAB6wHzTzI`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15), interface guidance

**Anchored on:**

> Component TradeStudies (Del. 7) |

**Comment:**

> Asset connects to Conduit

- [ ] applied

### `AAAB6wHzTzA`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15)

**Anchored on:**

> Component TradeStudies (Del. 7) |

**Comment:**

> Action uses Resource

- [ ] applied

### `AAAB6wHzTy4`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15)

**Anchored on:**

> See note above for Trade Studies (Del. 4 & 7). Valid generic link. Acceptable. | |

**Comment:**

> component asset "references" trade study

- [ ] applied

## 3 · Document inconsistency

### `AAAB60w8-3Q`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines revision (T45)

**Anchored on:**

> Relationship is valid in base LML 2.0

**Comment:**

> this needs to be consistent with the rest of the guidelines in all the documents.

- [ ] applied

### `AAAB60w8-zo`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md and with-verdicts.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines revision (T45)
- *section*

**Anchored on:**

> "traced from"**

**Comment:**

> Invert this so students are not confused when comparing with the deliverable guidelines

- [ ] applied

### `AAAB60w8-zM`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 4.
- **Blocks:** Guidelines revision (T45), compliance queries

**Anchored on:**

> End-to-End Traceability Chain Reference

**Comment:**

> MAJOR PROBLEM:  this is correct. Look for consistency in the deliverables document as well as in these guidelines.

- [ ] applied

## 4 · Labels for filters

### `AAAB5eBvJ7o`

- **Sadaf Shaikh**, 2026-05-07
- **File:** `stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Template project (T19) — EARLIER than the freeze

**Anchored on:**

> llocate the component Asset to the Actions it performs using the "performs" relationship, consistent with the functional allocation from Deliverable 3.**

**Comment:**

> also, add the label "Selected component" for easy filtering when we create traceability matrix between functional requirements and selected components

- [ ] applied

### `AAAB6wHzTzk`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `not located — find by heading below`
- **Section:** 3. Step-by-step Instructions
- **Blocks:** Template project (T19)
- *short anchor — locate by heading*

**Anchored on:**

> Budget Analys

**Comment:**

> also, add label "Analysis" to this artifact to be able to filter out just the analyses artifacts

- [ ] applied

## 5 · SRD auto-link gap

### `AAAB5eL9tMg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/3-stage-synthesis/d3-functional-requirements-document-frd.md`
- **Section:** (none)
- **Blocks:** Traceability standups (T24), quality scan (T25)

**Anchored on:**

> Step 9 — Establish links**

**Comment:**

> write instructions on establishing links between actions/assets and requirements generated by SRD because "Generate SRD" doesnt automatically create these links

- [ ] applied

## 6 · Missing instructions

### `AAABzzIlFRc`

- **Sadaf Shaikh**, 2026-02-06
- **File:** `not located — find by heading below`
- **Section:** (none)
- **Blocks:** Guidelines (T45)
- *short anchor — locate by heading*

**Anchored on:**

> ** # **

**Comment:**

> No relationship that makes sense to me

- [ ] applied

### `AAABzzIlFO0`

- **Sadaf Shaikh**, 2026-02-06
- **File:** `not located — find by heading below`
- **Section:** 4.
- **Blocks:** Guidelines (T45)
- *short anchor — locate by heading*

**Anchored on:**

> Context Diagram

**Comment:**

> mention standard naming convention

- [ ] applied

### `AAAB57gYWUk`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`
- **Section:** 4.
- **Blocks:** Guidelines (T45)

**Anchored on:**

> Step-by-Step Instructions

**Comment:**

> future iteration: no instructions given to create relationship between system and subsystem requirements

- [ ] applied

### `AAAB6feBJ5M`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `stages/2-system-concept/d3-system-requirements.md`
- **Section:** 3
- **Blocks:** Guidelines (T45)

**Anchored on:**

> . System Requirements

**Comment:**

> provide instructions on deriving system technical requirements.  take inspiration from stage 3 technical requirements instructions.

- [ ] applied

### `AAAB57gYWLs`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `not located — find by heading below`
- **Section:** 1.
- **Blocks:** Guidelines (T45)
- *short anchor — locate by heading*

**Anchored on:**

> What This Deliverable Is

**Comment:**

> if the generated subsystem functional requirement is related to the technical requirement, add the technical requirement to the same functional requirement  create traceability with upstream requirement (system) from stage 2   technical requirement in SRD (specified by) Measure

> **Sadaf Shaikh replied:** -technical requirements should be created manually in the SRD along with their associated measure entities

- [ ] applied

### `AAAB6wHzTzg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md and with-verdicts.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines (T45)
- *section*

**Anchored on:**

> Decision → Risk

**Comment:**

> add after this: issue "references" Analysis Artifact called "Design Analysis Report"

- [ ] applied

### `AAAB6wHzTzQ`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines (T45)

**Anchored on:**

> Physical I/O(Del. 2)

**Comment:**

> add some explanation/context

- [ ] applied

## 7 · Canvas reporting

### `AAABzy-qwus`

- **Munzir Zafar**, 2026-02-06
- **File:** `stages/1-requirements/d2-context-diagram.md`
- **Section:** Guidelines
- **Blocks:** Deliverable templates (T92)

**Anchored on:**

> For “As-is Architecture”, fill in the following attributes: 1. Number: “OCD.1” 2. Name: “Context Diagram for As-is Architecture” 3. Description: {*provide a description}

**Comment:**

> traceability of user needs to extracts needs to be generated in a form that can be made part of the report to be submitted

- [ ] applied

### `AAABzy-qwug`

- **Munzir Zafar**, 2026-02-06
- **File:** `stages/1-requirements/d2-context-diagram.md`
- **Section:** Guidelines
- **Blocks:** Deliverable templates (T92)

**Anchored on:**

> Create an asset for the system, name it, number it as “SYS.1” and add a description. 6. Create external assets, name them, and number them as “EXT.n”. Mark external assets by selecting \[image\]on the top-bar. 7. **Connect external systems to the original system** 1. Drag the green circle on the selected Asset to another Asset and the dialog in Figure 4.2 will appear. 2. Define Input/Output, Conduit, Actions, Directionality, and Origin using the pop-up displayed in Figure 4.2. Directions and shapes for the conduits can be changed by selecting the line and using the “Line Options” button at the top. Fill as many fields as possible for each of the entities.

**Comment:**

> Need a template for allowing students to easily populate the deliverables for canvas submission

> **Munzir Zafar replied:** see this chatgpt conversation for details https://chatgpt.com/share/69858d38-40a0-8001-81a5-bb744606d549

- [ ] applied

### `AAABzy-qwuM`

- **Munzir Zafar**, 2026-02-06
- **File:** `stages/1-requirements/d2-context-diagram.md`
- **Section:** Guidelines
- **Blocks:** Deliverable templates (T92)

**Anchored on:**

> Define Input/Output, Conduit, Actions, Directionality, and Origin using the pop-up displayed in Figure 4.2.

**Comment:**

> Each Notes Document (or each statement inside it) should include:  Stakeholder name and ID (given in stakeholders list)  Stakeholder role / perspective  Context (meeting, site visit, email, etc.)

> **Munzir Zafar replied:** should create a template for this as well

> **Munzir Zafar replied:** can we just relate the stakeholder entity with this document and add context in the description?

> **Munzir Zafar replied:** why a template?

- [ ] applied

### `AAAB6wHzT2I`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`
- **Section:** 3.
- **Blocks:** Deliverable templates (T92)

**Anchored on:**

> Step-by-Step Instructions

**Comment:**

> Look at all the deliverables in this stage for missing reporting instructions for Canvas.

- [ ] applied

## 8 · Deferred by author

### `AAAB57gYWJ0`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `stages/1-requirements/d3-stakeholder-requirements-document.md`
- **Section:** Why this deliverable is important

**Anchored on:**

> Decompose Statements

**Comment:**

> future iteration: stakeholder req -> scenarios ->action diagrams (some decomposition) add stakeholder functional requirements from the action diagram

- [ ] applied

### `AAAB57gYWJ8`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `stages/3-stage-synthesis/d1-low-level-action-diagram.md`
- **Section:** 3b.

**Anchored on:**

> Build the Decomposition Diagram

**Comment:**

> future iteration: after concept is finalized, we think of more solution-dep scenarios -> more action diagrams -> system functional requirements from added actions (these should be documented separately)

- [ ] applied

### `AAAB5eL9tNY`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`
- **Section:** 3. Step-by-Step Instructions

**Anchored on:**

> Update the existing Measure entities from Deliverable 4 with the actual datasheet performance values of the selected component. Do not create new Measure entities — update the threshold and objective values in the existing ones to reflect what the selected component actually delivers.

**Comment:**

> modify this instruction to add a separate Measure entity for the selected component

> **Sadaf Shaikh replied:** future iteration: technical requirement in SRD (specified by) Measure (satisfied by) selected component (specified by) Measure

- [ ] applied

## 9 · Content and pedagogy

### `AAABzUWr0Tw`

- **Sadaf Shaikh**, 2026-02-03
- **File:** `not located — find by heading below`
- **Section:** 3. Stakeholder Requirements Document
- *short anchor — locate by heading*

**Anchored on:**

> Issue entity

**Comment:**

> Mention of an earlier exercise done on risk and issue.

- [ ] applied

### `AAABzUWr0R4`

- **Sadaf Shaikh**, 2026-02-03
- **File:** `stages/1-requirements/d3-stakeholder-requirements-document.md`
- **Section:** 3. Stakeholder Requirements Document
- **Blocks:** Freeze (T15), helpful not blocking

**Anchored on:**

> Trade Study document as Artifact

**Comment:**

> Ailiya to make a separate table on a subset of relationships between entities from LML specification

- [ ] applied

### `AAABzurITFc`

- **Sadaf Shaikh**, 2026-02-04
- **File:** `stages/1-requirements/d2-context-diagram.md`
- **Section:** Why this deliverable is important

**Anchored on:**

> Note that the actions that were created in Figure 4.3 include a number of scenarios in Figure 4.4. A few adjustments were made from Figure 4.3 to Figure 4.5: - M.2, M.10, and M.12 were put as children of Scenario 3. - M.8 “Receive Habitat” was only part of Scenario 4, so it was made the child of that scenario. - M.13 “Prepare Personnel for Return to Earth” was renamed to S.6 “Rotate Personnel Out.” So, with a little bit of work, we were able to reuse all the work that was done from developing the context diagram.

**Comment:**

> should we keep it in this section?

- [ ] applied

### `AAABvWHEtbI`

- **Ailiya Fatima**, 2026-02-09
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** (none)

**Anchored on:**

> Student Checklist – User Needs Document

**Comment:**

> how to add this to innoslate

- [ ] applied

### `AAABvWHEtbE`

- **Ailiya Fatima**, 2026-02-09
- **File:** `not located — find by heading below`
- **Section:** 4.
- *short anchor — locate by heading*

**Anchored on:**

> Traceability

**Comment:**

> why not use import analyzer here

- [ ] applied

### `AAAB0D17ImY`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> Go to the “Documents” view and create a “Notes Document”. Name it “Extracts from {name of the artifact in step a}”. Number it “EX.n”, where n is an integer. Keep the template as “Blank Template”.

**Comment:**

> think about this

- [ ] applied

### `AAAB0D17ImM`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `not located — find by heading below`
- **Section:** Uploading Raw Evidence in Innoslate
- *short anchor — locate by heading*

**Anchored on:**

> Keep

**Comment:**

> needs to be reviewed

- [ ] applied

### `AAAB0D17ImI`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `not located — find by heading below`
- **Section:** Uploading Raw Evidence in Innoslate
- *short anchor — locate by heading*

**Anchored on:**

> “”

**Comment:**

> should be added in the appendix

- [ ] applied

### `AAAB0D17Il8`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> 5. If step iv fails, as a last resort, in the description of the artifact, enter the path of the audio/video file inside the official home folder (for example, data/video-recordings/Factory\_Visit\_1st\_Jan\_2026.mp4). 2.

**Comment:**

> elaborate on the attributes for each of these entities

- [ ] applied

### `AAABzXMVlDs`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> For reference, go over “Applying the Process” section in chapter 3 to understand how the authors extracted the statements from a book.

**Comment:**

> pg 87 of real-mbse book

- [ ] applied

### `AAAB0EbNaqM`

- **Sadaf Shaikh**, 2026-02-11
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> Enter a meaningful name (e.g., Factory Visit – Maintenance Supervisor – 12 Jan) which includes date, stakeholder role, and context of data collection.

**Comment:**

> as is architecture captured as context diagram?

> **Sadaf Shaikh replied:** list of scenarios for both?

> **Sadaf Shaikh replied:** list of scenarios for to-be only

- [ ] applied
