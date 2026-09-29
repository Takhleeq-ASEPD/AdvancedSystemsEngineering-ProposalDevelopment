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

## Status summary (checked 29 September 2026)

**Read this before using the "Anchored on" lines below.** Those anchors were recovered automatically, and about
half are wrong or unusable: some point at text that has since moved, some are one or two words, and in several
places neighbouring comments had their anchors swapped. Every open comment now carries a **Status** block,
checked by hand against the current files. Trust the Status block, not the anchor.

| Status | Meaning | Count |
|---|---|---|
| **Ready** | Spot confirmed, change spelled out. The editor fixes it. | 12 |
| **Draft** | Spot confirmed, but the fix needs new wording. The editor drafts it, Munzir reviews before merge. | 5 |
| **Find in Google Doc** | Spot not known. Look it up in the original Google Doc first. | 12 |
| **Munzir decides** | Needs a decision, not an edit: future iterations, questions, your own comments, stage-wide passes. | 20 |

**Ready:** `AAAB4xFXrvE`, `AAAB4xFXrrk`, `AAAB5d3-5l8`, `AAAB4xFXrqw`, `AAAB4xFXrrE`, `AAAB5d3-5l0`, `AAAB3YKxxYg`, `AAAB4xlgcPo`, `AAAB4xlgcPw`, `AAAB5eBvJ7o`, `AAAB6wHzTzk`, `AAABzXMVlDs`

**Draft:** `AAAB6wHzTzc`, `AAAB57gYWLs`, `AAAB6feBJ5M`, `AAAB6wHzTzQ`, `AAAB5eL9tMg`

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

**Status: Munzir decides**

**Why:** Re-assess the relationship tables against LML 1.4 instead of 2.0. A whole-table decision.

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

**Status: Ready**

**Where:** `docs/stages/2-system-concept/d3-system-requirements.md`, near line 118

**Search for this exact text** (it appears exactly once):

```text
- Create relationship **“derived from”** → Trade Study (Artifact)
```

**Change:** Change **derived from** to **sourced by** (System Req sourced by Trade Study).

**Also delete the inline note(s) starting:** `incorrect. "sourced by"`; `System Req (sourced by) Trade Study`

**Why this is the right spot:** Comment text and both inline notes sit on this exact line.

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

**Status: Ready**

**Where:** `docs/stages/2-system-concept/d4-verification-requirements-document-for-system-requirements.md`, near line 131

**Search for this exact text** (it appears exactly once):

```text
## **Trace Verification Requirements to Test Cases (Optional)**
```

**Change:** Under this heading, add an instruction to create the relationship System Requirement **verified by** Verification Requirement.

**Also delete the inline note(s) starting:** `what about tracing to system requirements?`; `System Req (verified by) Verification Req`

**Why this is the right spot:** Anchor and both inline notes agree.

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

**Status: Find in Google Doc**

**Likely spot:** Probably Deliverable 4 (stage 3), step 4c.4: "Link the entity to the trade study artifact using the **caused by** relationship...". The listed anchor (about assumptions) is unrelated.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Find in Google Doc**

**Likely spot:** Probably the same step as AAAB4xlgcPk (Deliverable 4, step 4c.4). The listed anchor (Final Specified Value) is unrelated.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Ready**

**Where:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`, near line 156

**Search for this exact text** (it appears exactly once):

```text
2.  For each risk, create a Risk entity in Innoslate following the same format as Deliverable 4: unique ID, description, likelihood, consequence, assignee. Link it to the selected component Asset entity using "related to" and to the affected requirement using "traced from."
```

**Change:** Change both links: Risk **caused by** component Asset, and Risk **caused by** the affected Requirement.

**Also delete the inline note(s) starting:** `RIsk caused by Asset Risk caused by Requirement`

**Why this is the right spot:** The listed anchor was swapped with AAAB4xlgcPo. This comment is about linking a Risk; the inline note sits under this line.

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

**Status: Ready**

**Where:** `docs/stages/1-requirements/d3-stakeholder-requirements-document.md`, near line 74

**Search for this exact text** (it appears exactly once):

```text
3.  Resolve issues/risks through trade studies and discussion with customers. Create Trade Study document as Artifact and add a label “Trade Study”. Create relationship of trade study with Issue using “resolves”.
```

**Change:** Replace the last sentence with: create a Decision entity; Trade Study **enables** Decision; Decision **resolves** Issue.

**Also delete the inline note(s) starting:** `so Replace relationship between trade study`; `resolves in LML connects any entity`

**Why this is the right spot:** Anchor text found exactly; both inline notes sit on this step.

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

**Status: Ready**

**Where:** `docs/stages/1-requirements/d4-high-level-action-diagrams.md`, near line 57

**Search for this exact text** (it appears exactly once):

```text
1.  Create relationship “satisfies” for every use case/scenario with the relevant functional requirements in the Stakeholder Requirements document.
```

**Change:** Change **satisfies** to **traced from** (use case/scenario traced from Stakeholder Requirement). Note for the consistency pass: the relationship table currently says Action **traced to** Requirement.

**Also delete the inline note(s) starting:** `Use case/scenario (traced from) Stakeholder requirement.`

**Why this is the right spot:** Anchor and inline note agree. Leave the other note on this line ("This should be traced from...") in place; it belongs to AAAB60w8-zU.

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

**Status: Ready**

**Where:** `docs/stages/1-requirements/d5-verification-requirements-document-for-stakeholder-requirements.md`, near line 117

**Search for this exact text** (it appears exactly once):

```text
6.  **Trace to test cases (optional)**
```

**Change:** Add an instruction to create the relationship Stakeholder Requirement **verified by** Verification Requirement.

**Also delete the inline note(s) starting:** `Add instructions for creating relationship: Stakeholder req`

**Why this is the right spot:** Anchor and inline note agree.

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

**Status: Ready**

**Where:** `docs/stages/2-system-concept/d3-system-requirements.md`, near line 104

**Search for this exact text** (it appears exactly once):

```text
- Create relationship **“refines” or “satisfies”** → Stakeholder Requirement
```

**Change:** Change **refines or satisfies** to **traced from** (System Req traced from Stakeholder Req).

**Also delete the inline note(s) starting:** `incorrect. "traced from"`; `System Req (traced from) Stakeholder Req`

**Why this is the right spot:** The listed anchor ("allocated to" line) is wrong: that line belongs to AAAB6feBJ4M. This comment is about the Stakeholder Requirement link, and both inline notes sit under this line.

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

**Status: Ready**

**Where:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`, near line 259

**Search for this exact text** (it appears exactly once):

```text
1.  In the Artifact's relationships panel, add a **“satisfies”** relationship to each relevant subsystem requirement.
```

**Change:** Rewrite step 4b.1 by the triangle rule: trade study **satisfies** upstream requirement; derived (downstream) requirement **sourced by** trade study; derived requirement **traced from** upstream requirement. Do not link trade study as traced from derived requirements.

**Also delete the inline note(s) starting:** `modify instructions according to the following principle`; `derived reqs (sourced by) the trade study`

**Why this is the right spot:** Anchor and both inline notes agree.

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

**Status: Draft**

**Where:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`, near line 163

**Search for this exact text** (it appears exactly once):

```text
3.  For any risk rated Medium or above, document a mitigation strategy. The fallback component identified in Step 4 serves as the primary mitigation for supply chain and obsolescence risks — link the fallback component Asset to the Risk entity using "resolves."
```

**Change:** Change so a Decision **resolves** the Risk, and the fallback component is linked to that Decision. The comment does not name the component-to-Decision verb: Claude proposes one, Munzir confirms.

**Also delete the inline note(s) starting:** `component cannot resolve a risk`

**Why this is the right spot:** The inline note sits on this line and the comment is about it.

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

**Status: Ready**

**Where:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`, near line 134

**Search for this exact text** (it appears exactly once):

```text
4.  In the Artifact's relationships panel, add a **“satisfies”** relationship to the subsystem requirements.
```

**Change:** Rewrite this step by the triangle rule, the same way as AAAB3YKxxYg: trade study **satisfies** upstream requirement; derived requirement **sourced by** trade study; derived requirement **traced from** upstream requirement.

**Why this is the right spot:** The listed anchor was swapped with AAAB4xlgcPw. This comment (the trade study triangle) fits this Step 6 line; it is the same rule as AAAB3YKxxYg in Deliverable 4.

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

**Status: Munzir decides**

**Why:** Its first half ("traced from") is covered by AAAB4xFXrrE. Its second half asks for a new rule in the Stage 3 Low-level Action Diagram page, which has no relationship step yet. Decide where it goes.

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

**Status: Munzir decides**

**Why:** Asks for guideline changes so relationships flow downstream from Decisions. A design decision across pages.

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

**Status: Find in Google Doc**

**Likely spot:** Somewhere in the relationship tables. Listed on a Component Trade Studies row, but an inline note of the same text sits in the Stage 1 Context Diagram page. Unclear which.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Find in Google Doc**

**Likely spot:** Somewhere in the relationship tables, listed on a Component Trade Studies row. Unclear whether to add a row or change one.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Munzir decides**

**Why:** Stage 3 Deliverable 7 step 6.5 already says the component Asset **references** the trade study. Decide whether the table needs a row too.

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

**Status: Munzir decides**

**Why:** Part of the final consistency pass.

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

**Status: Find in Google Doc**

**Likely spot:** One of the "traced from" cells in the relationship tables. There are several.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Munzir decides**

**Why:** This is the final consistency pass itself.

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

**Status: Ready**

**Where:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`, near line 103

**Search for this exact text** (it appears exactly once):

```text
3.  In Innoslate, create an Asset entity for each selected component. Record the following attributes: component name, manufacturer, model number, and a link to the datasheet as a reference artifact.
```

**Change:** Add: apply the label **Selected component** to each of these Asset entities.

**Also delete the inline note(s) starting:** `also, add the label "Selected component"`

**Why this is the right spot:** The inline note sits on this step. A label belongs where the Asset is created.

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

**Status: Ready**

**Where:** `docs/stages/3-stage-synthesis/d8-design-analysis-report-and-initial-bill-of-materials-bom.md`, near line 220

**Search for this exact text** (it appears exactly once):

```text
3.  **Create a new Artifact entity** (e.g., DAR.1) for the Design Analysis Report. Upload the completed report and link it to any trade studies performed while making design choices in Stage 2 using "related to."
```

**Change:** Add: apply the label **Analysis** to this Artifact.

**Also delete the inline note(s) starting:** `also, add label "Analysis" to this artifact`

**Why this is the right spot:** The listed anchor ("Budget Analys") is a fragment. The comment says "this artifact"; the inline note sits on this Artifact-creation step.

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

**Status: Draft**

**Where:** `docs/stages/3-stage-synthesis/d3-functional-requirements-document-frd.md`, near line 243

**Search for this exact text** (it appears exactly once):

```text
### **Step 9 — Establish links**
```

**Change:** Write the steps for linking Actions/Assets to the requirements that "Generate SRD" creates. Needs correct Innoslate steps, so Munzir reviews.

**Also delete the inline note(s) starting:** `write instructions on establishing links`

**Why this is the right spot:** Anchor and inline note agree.

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

**Status: Find in Google Doc**

**Likely spot:** Anchored on a lone "#". No usable location.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Find in Google Doc**

**Likely spot:** Anchored on "Context Diagram", section 4. Too short to place.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Munzir decides**

**Why:** Marked "future iteration" by Sadaf. Defer or do now?

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

**Status: Draft**

**Where:** `docs/stages/2-system-concept/d3-system-requirements.md`, near line 73

**Search for this exact text** (it appears exactly once):

```text
#### **2.** **Derive Requirements from Architecture & Trade Studies**
```

**Change:** Add instructions for deriving system technical requirements, adapted from the Stage 3 technical requirements instructions (Deliverable 4, step 3). New content, so Munzir reviews.

**Also delete the inline note(s) starting:** `provide instructions on deriving system technical requirements`

**Why this is the right spot:** The inline note sits under this heading and the comment is about deriving requirements.

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

**Status: Draft**

**Where:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`, near line 285

**Search for this exact text** (it appears exactly once):

```text
1.  For each subsystem requirement in the Technical Requirements Table, create a **Measure** class entity in Innoslate.
```

**Change:** Add instructions: technical requirements are created manually in the SRD with their Measure entities; technical requirement **specified by** Measure; trace to the upstream system requirement from Stage 2. New wording, so Munzir reviews.

**Also delete the inline note(s) starting:** `-technical requirements should be created manually`; `if the generated subsystem functional requirement`

**Why this is the right spot:** The listed anchor was not located. Both inline notes sit on this step and the comment is about Measures.

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

**Status: Find in Google Doc**

**Likely spot:** A "Decision → Risk" row in the relationship tables. There are two (Stage 1 and Trade Studies).

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Draft**

**Where:** `docs/relationships/index.md`, near line 52
**Where:** `docs/relationships/with-verdicts.md`, near line 65

**Search for this exact text** (it appears exactly once in each file):

```text
| Physical I/O(Del. 2) | I/O entity
```

**Change:** Add a short explanation of the Physical I/O rows. Do it in both files. New wording, so Munzir reviews.

**Why this is the right spot:** Anchor found in both relationship tables.

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

**Status: Munzir decides**

**Why:** Your own comment about report templates.

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

**Status: Munzir decides**

**Why:** Your own comment: a Canvas submission template.

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

**Status: Munzir decides**

**Why:** Your own thread. The replies never settled on an answer.

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

**Status: Munzir decides**

**Why:** A stage-wide audit of reporting instructions, not a single edit.

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

**Status: Munzir decides**

**Why:** Marked "future iteration" by Sadaf. Defer or do now?

- [ ] applied

### `AAAB57gYWJ8`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `stages/3-stage-synthesis/d1-low-level-action-diagram.md`
- **Section:** 3b.

**Anchored on:**

> Build the Decomposition Diagram

**Comment:**

> future iteration: after concept is finalized, we think of more solution-dep scenarios -> more action diagrams -> system functional requirements from added actions (these should be documented separately)

**Status: Munzir decides**

**Why:** Marked "future iteration" by Sadaf. Defer or do now?

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

**Status: Munzir decides**

**Why:** Location is certain (Deliverable 7, step 6 about Measures), but Sadaf's reply marks the change "future iteration". Defer or do now?

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

**Status: Munzir decides**

**Why:** Probably Stage 1 Deliverable 3, "Create Issue entity...". But which earlier exercise to mention is yours to say.

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

**Status: Munzir decides**

**Why:** Asks Ailiya for a relationship table. The relationships pages now exist. Probably tick as done.

- [ ] applied

### `AAABzurITFc`

- **Sadaf Shaikh**, 2026-02-04
- **File:** `stages/1-requirements/d2-context-diagram.md`
- **Section:** Why this deliverable is important

**Anchored on:**

> Note that the actions that were created in Figure 4.3 include a number of scenarios in Figure 4.4. A few adjustments were made from Figure 4.3 to Figure 4.5: - M.2, M.10, and M.12 were put as children of Scenario 3. - M.8 “Receive Habitat” was only part of Scenario 4, so it was made the child of that scenario. - M.13 “Prepare Personnel for Return to Earth” was renamed to S.6 “Rotate Personnel Out.” So, with a little bit of work, we were able to reuse all the work that was done from developing the context diagram.

**Comment:**

> should we keep it in this section?

**Status: Munzir decides**

**Why:** A question ("should we keep it in this section?"). Needs a yes or no.

- [ ] applied

### `AAABvWHEtbI`

- **Ailiya Fatima**, 2026-02-09
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** (none)

**Anchored on:**

> Student Checklist – User Needs Document

**Comment:**

> how to add this to innoslate

**Status: Munzir decides**

**Why:** A question ("how to add this to Innoslate"). Needs an answer before any edit.

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

**Status: Find in Google Doc**

**Likely spot:** Anchored on "Traceability", section 4. Too short to place.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

- [ ] applied

### `AAAB0D17ImY`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> Go to the “Documents” view and create a “Notes Document”. Name it “Extracts from {name of the artifact in step a}”. Number it “EX.n”, where n is an integer. Keep the template as “Blank Template”.

**Comment:**

> think about this

**Status: Munzir decides**

**Why:** "think about this". No instruction to act on.

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

**Status: Find in Google Doc**

**Likely spot:** Anchored on "Keep", in "Uploading Raw Evidence". Too short to place.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

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

**Status: Find in Google Doc**

**Likely spot:** Empty anchor, in "Uploading Raw Evidence".

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

- [ ] applied

### `AAAB0D17Il8`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> 5. If step iv fails, as a last resort, in the description of the artifact, enter the path of the audio/video file inside the official home folder (for example, data/video-recordings/Factory\_Visit\_1st\_Jan\_2026.mp4). 2.

**Comment:**

> elaborate on the attributes for each of these entities

**Status: Munzir decides**

**Why:** Unclear which entities "these entities" means.

- [ ] applied

### `AAABzXMVlDs`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `stages/1-requirements/d1-list-of-stakeholders.md`
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on:**

> For reference, go over “Applying the Process” section in chapter 3 to understand how the authors extracted the statements from a book.

**Comment:**

> pg 87 of real-mbse book

**Status: Ready**

**Where:** `docs/stages/1-requirements/d1-list-of-stakeholders.md`, near line 397

**Search for this exact text** (it appears exactly once):

```text
4.  Analyze reference documents to extract important information. For reference, go over “Applying the Process” section in chapter 4 to understand how the authors extracted the statements from a book. Create new Statement entities to capture it in the Notes Document.
```

**Change:** Add the page reference: page 87 of the Real MBSE book. Do not change the chapter number.

**Why this is the right spot:** Anchor matches except the chapter number: the source said chapter 3, the page now says chapter 4. Change only what the comment asks.

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

**Status: Find in Google Doc**

**Likely spot:** The listed anchor (a naming example) is unrelated to the question asked. February anchors drift.

Open the original Google Doc, click this comment, and note the highlighted text. Then Munzir updates this entry to Ready.

- [ ] applied
