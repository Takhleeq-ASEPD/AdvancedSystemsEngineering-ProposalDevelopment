---
title: Open review comments
---

# Open review comments

Fifty-one review threads from the source document (fifty from the original list, one added on 29 September). Each one carries **the exact text it was
attached to** and the file that text is in, so a change can be made in place rather than searched for.

Every "Anchored on" line below was taken directly from the Google Doc on 29 September 2026, using the comment markers in Google's own export. They replace an earlier list that was reconstructed by pairing and was wrong in many places.

**Working rule:** fix each comment in place. Only propagate when the comment itself says to.
A consistency pass at the end catches the rest.

## Status summary (29 September 2026)

Every comment carries a **Status** block. Use it, not the "File" line, to find where to work.
Click **Go to spot** to open the rendered page scrolled to the exact sentence, highlighted.

| Status | Meaning | Count |
|---|---|---|
| **Done** | Applied in the repo. Box ticked. | 8 |
| **Ready** | Spot confirmed, change spelled out. The editor fixes it. | 6 |
| **Draft** | Spot confirmed, but the fix needs new wording. The editor drafts it, Munzir reviews before merge. | 8 |
| **Munzir decides** | Needs a decision, not an edit: questions, future iterations, Munzir's own comments, stage-wide passes. | 29 |

**Ready:** `AAAB5d3-5l8`, `AAAB5d3-5l0`, `AAAB5eBvJ7o`, `AAAB6wHzTzk`, `AAABzXMVlDs`, `AAAB6wHzTzg`

**Draft:** `AAAB6wHzTzc`, `AAAB57gYWLs`, `AAAB6feBJ5M`, `AAAB5eL9tMg`, `AAAB6wHzTzQ`, `AAAB60w8-zo`, `AAAB6wHzTzI`, `AAAB6wHzTzA`

**The Google Doc is no longer edited.** The repo is the master copy from 29 September 2026. Fixes made in the doc on
25 August have been ported here.

---

## 1 · LML version

### `AAAB60w8-zg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/with-verdicts.md` (near line 29)
- **Go to spot:** [open in page](../relationships/with-verdicts.md#:~:text=Relationship%20exists%20only%20in%20the)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Relationship freeze (T15), all filters (T17,T18)

**Anchored on** (from the Google Doc):

> Relationship is valid in base LML 2.0

**Comment:**

> modify for version LML 1.4 because I later found that Innoslate employs LML 1.4

**Status: Munzir decides**

**Why:** Re-assess the relationship tables against LML 1.4 instead of 2.0. A whole-table decision.

- [ ] applied

## 2 · Relationship corrections

### `AAAB6feBJ4M`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/2-system-concept/d3-system-requirements.md` (near line 110)
- **Go to spot:** [open in page](../stages/2-system-concept/d3-system-requirements.md#:~:text=Create%20relationship%20%E2%80%9Cperforms%E2%80%9D%20%E2%86%92%20Asset)
- **Section:** 2.
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> Create relationship **“performs”** →

**Comment:**

> replace allocated to with "performs".   Asset (performs) Action

**Status: Done**

Fixed in the repo on 27 August (commit 3465079).

- [x] applied

### `AAAB4xFXrvE`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/2-system-concept/d3-system-requirements.md` (near line 108)
- **Go to spot:** [open in page](../stages/2-system-concept/d3-system-requirements.md#:~:text=Create%20relationship%20%E2%80%9Csourced%20by%E2%80%9D%20%E2%86%92)
- **Section:** 3. Create Required Relationships in Innoslate
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> Create relationship **“sourced by”** → Trade Study (Artifact)

**Comment:**

> incorrect. "sourced by"

> **Sadaf Shaikh replied:** System Req (sourced by) Trade Study

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB5d3-5l8`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/2-system-concept/d4-verification-requirements-document-for-system-requirements.md` (near line 131)
- **Go to spot:** [open in page](../stages/2-system-concept/d4-verification-requirements-document-for-system-requirements.md#:~:text=Trace%20Verification%20Requirements%20to%20Test)
- **Section:** (none)
- **Blocks:** Freeze (T15), V&V design

**Anchored on** (from the Google Doc):

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

- [ ] applied

### `AAAB4xlgcPk`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md` (near line 345) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md#:~:text=5c.%20Display%20Risks%20in%20a)
- **Section:** 2c. Create Pugh Matrix
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> “caused by”**

**Comment:**

> Risk (caused by) Requirement

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB4xlgcPg`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md` (near line 339)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md#:~:text=Link%20the%20Risk%20entity%20to)
- **Section:** 3d. Add an Engineering Margin
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> “**references”**

**Comment:**

> Risk (references) trade study

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB4xlgcPw`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md` (near line 156)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md#:~:text=For%20each%20risk%2C%20create%20a)
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> component Asset entity using "caused by" and to the affected requirement using "caused by"

**Comment:**

> RIsk caused by Asset Risk caused by Requirement

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB4xFXrqw`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/1-requirements/d3-stakeholder-requirements-document.md` (near line 74), where the unapplied change would go
- **Go to spot:** [open in page](../stages/1-requirements/d3-stakeholder-requirements-document.md#:~:text=Resolve%20issues%2Frisks%20through%20trade%20studies)
- **Section:** Why this deliverable is important
- **Blocks:** Freeze (T15), trade study guidance

**Anchored on:** comment no longer exists in the Google Doc.

**Comment:**

> resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Issue, and Decision enabled by Trade Study.

> **Sadaf Shaikh replied:** so Replace relationship between trade study and risk(modelled as issue) with decision and risk.  trade study (enables) decision (resolves) issue (modelled as issue)

**Status: Munzir decides**

**Why:** Deleted from the Google Doc, but not applied: both the doc and the repo still say "trade study ... resolves Issue". Sadaf asked for Decision **resolves** Issue instead. Apply, or drop?

- [ ] applied

### `AAAB4xFXrrE`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/1-requirements/d4-high-level-action-diagrams.md` (near line 57)
- **Go to spot:** [open in page](../stages/1-requirements/d4-high-level-action-diagrams.md#:~:text=Create%20relationship%20%E2%80%9Ctraced%20from%E2%80%9D%20for)
- **Section:** Why this deliverable is important
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> Create relationship “traced from” for every use case/scenario with the relevant functional requirements in the Stakeholder Requirements document.

**Comment:**

> Use case/scenario (traced from) Stakeholder requirement.

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB5d3-5l0`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/1-requirements/d5-verification-requirements-document-for-stakeholder-requirements.md` (near line 117)
- **Go to spot:** [open in page](../stages/1-requirements/d5-verification-requirements-document-for-stakeholder-requirements.md#:~:text=Trace%20to%20test%20cases%20%28optional%29)
- **Section:** Why this deliverable is important
- **Blocks:** Freeze (T15), V&V design

**Anchored on** (from the Google Doc):

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

- [ ] applied

### `AAAB4xFXrrk`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/2-system-concept/d3-system-requirements.md` (near line 104)
- **Go to spot:** [open in page](../stages/2-system-concept/d3-system-requirements.md#:~:text=Create%20relationship%20%E2%80%9Ctraced%20from%E2%80%9D%20%E2%86%92)
- **Section:** 3. Create Required Relationships in Innoslate
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> Create relationship **“traced from”** → System Req traced from Stakeholder Requirement

**Comment:**

> incorrect. "traced from"

> **Sadaf Shaikh replied:** System Req (traced from) Stakeholder Req

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB3YKxxYg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md` (near line 259)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md#:~:text=In%20the%20Artifact%27s%20relationships%20panel%2C)
- **Section:** 4a. Create the Trade Study Artifact
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> dd a **“satisfies”** relationship to each relevant upstream requirement that the Trade Study aims to satisfy
> 2.

**Comment:**

> derived reqs (sourced by) the trade study (avoid trade study is traced from derived reqs)  in the triangle: - upstream requirement - trade study - downstream requirement  t satisfies u d sourced by t d traced from u

**Status: Done**

Fixed in the Google Doc by Munzir on 25 August; ported to the repo on 29 September.

- [x] applied

### `AAAB6wHzTzc`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md` (near line 158)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md#:~:text=For%20any%20risk%20rated%20Medium)
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Freeze (T15), risk guidance

**Anchored on** (from the Google Doc):

> For any risk rated Medium or above, document a mitigation strategy. The fallback component identified in Step 4 serves as the primary mitigation for supply chain and obsolescence risks — link the fallback component Asset to the Risk entity using "resolves."

**Comment:**

> component cannot resolve a risk. Risk is resolved by decision and component should be linked to that decision.

**Status: Draft**

**Where:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md`, near line 158

**Search for this exact text** (it appears exactly once):

```text
3.  For any risk rated Medium or above, document a mitigation strategy. The fallback component identified in Step 4 serves as the primary mitigation for supply chain and obsolescence risks — link the fallback component Asset to the Risk entity using "resolves."
```

**Change:** Change so a Decision **resolves** the Risk, and the fallback component is linked to that Decision. The comment does not name the component-to-Decision verb: Claude proposes one, Munzir confirms.

**Also delete the inline note(s) starting:** `component cannot resolve a risk`

New wording: Munzir reviews before merge.

- [ ] applied

### `AAAB4xlgcPo`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md` (near line 134) (placed using the surrounding text in the Google Doc)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md#:~:text=In%20the%20Artifact%27s%20relationships%20panel%2C)
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> In the Artifact's relationships panel, add a **“satisfies”** relationship to the subsystem requirements

**Comment:**

> modify instructions according to the following principle:  in the triangle: - upstream requirement - trade study - downstream requirement   t satisfies u d sourced by t d traced from u

**Status: Munzir decides**

**Why:** Resolved in the Google Doc on 25 August, but the wording was not changed there. Accept as is, or reopen and apply the triangle rule as in Deliverable 4 step 4b?

- [ ] applied

### `AAAB60w8-zU`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 29) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../relationships/index.md#:~:text=satisfies%20does%20not%20exist%20in)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15), action diagram guidance

**Anchored on** (from the Google Doc):

> "satisfies"** | **

**Comment:**

> This should be "traced from"  in stage 3 under "Low-level action diagrams":  if they are serving as requirements, the same relationship should appear  if they serve as design choice, use Action "satisfies" Requirement relationship

**Status: Munzir decides**

**Why:** Its first half ("traced from") is done (see AAAB4xFXrrE). Its second half asks for a new rule in the Stage 3 Low-level Action Diagram page, which has no relationship step yet. Decide where it goes.

- [ ] applied

### `AAAB6wHzTzY`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 27) and `docs/relationships/with-verdicts.md` (near line 40)
- **Go to spot:** [open in index](../relationships/index.md#:~:text=Replace%20relationship%20between%20trade%20study) · [open in with-verdicts](../relationships/with-verdicts.md#:~:text=Replace%20relationship%20between%20trade%20study)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15), guidelines (T45)

**Anchored on** (from the Google Doc):

> Decision → Risk

**Comment:**

> there should be downstream relationships emanating from the decision (could be an asset or requirement or action)  need to make fixes in guidelines to incorporate this

**Status: Munzir decides**

**Why:** Asks for guideline changes so relationships flow downstream from Decisions. A design decision across pages.

- [ ] applied

### `AAAB6wHzTzI`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 52) and `docs/relationships/with-verdicts.md` (near line 65)
- **Go to spot:** [open in with-verdicts](../relationships/with-verdicts.md#:~:text=Asset%20%E2%86%92%20Asset%20%28hierarchy%29) · [open in index](../relationships/index.md#:~:text=Asset%20%E2%86%92%20Asset%20%28hierarchy%29)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15), interface guidance

**Anchored on** (from the Google Doc):

> Physical I/O(Del. 2)

**Comment:**

> Asset connects to Conduit

**Status: Draft**

**Where:** `docs/relationships/with-verdicts.md`, near line 66
**Where:** `docs/relationships/index.md`, near line 53

**Search for this exact text** (it appears exactly once in each file):

```text
| Asset → Asset (hierarchy) |
```

**Change:** Add a row after this one: Physical I/O (Del. 2) | Asset → Conduit | **"connected to"** (Asset connects to Conduit). Check the exact verb in Innoslate. Both files.

New wording: Munzir reviews before merge.

- [ ] applied

### `AAAB6wHzTzA`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 50) and `docs/relationships/with-verdicts.md` (near line 63)
- **Go to spot:** [open in with-verdicts](../relationships/with-verdicts.md#:~:text=Action%20%E2%86%92%20Action%20%28decomposition%29) · [open in index](../relationships/index.md#:~:text=Action%20%E2%86%92%20Action%20%28decomposition%29)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> Low -level Action Diagrams    (Del. 1) |

**Comment:**

> Action uses Resource

**Status: Draft**

**Where:** `docs/relationships/with-verdicts.md`, near line 64
**Where:** `docs/relationships/index.md`, near line 51

**Search for this exact text** (it appears exactly once in each file):

```text
| Action → Action (decomposition) |
```

**Change:** Add a row after this one: Low-level Action Diagrams (Del. 1) | Action → Resource | **"uses"** (Action uses Resource). Both files.

New wording: Munzir reviews before merge.

- [ ] applied

### `AAAB6wHzTy4`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 62) and `docs/relationships/with-verdicts.md` (near line 75)
- **Go to spot:** [open in index](../relationships/index.md#:~:text=Standard%20asset%20hierarchy%20decomposition%20%28%C2%A73.4.0.2.2%29.) · [open in with-verdicts](../relationships/with-verdicts.md#:~:text=Standard%20asset%20hierarchy%20decomposition%20%28%C2%A73.4.0.2.2%29.)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Freeze (T15)

**Anchored on** (from the Google Doc):

> Component TradeStudies (Del. 7) |

**Comment:**

> component asset "references" trade study

**Status: Munzir decides**

**Why:** Deliverable 7 step 6.5 already says the component Asset **references** the trade study. Decide whether the table needs a row too.

- [ ] applied

## 3 · Document inconsistency

### `AAAB60w8-3Q`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 132) and `docs/relationships/with-verdicts.md` (near line 145)
- **Go to spot:** [open in index](../relationships/index.md#:~:text=4.%20End%2Dto%2DEnd%20Traceability%20Chain%20Reference) · [open in with-verdicts](../relationships/with-verdicts.md#:~:text=4.%20End%2Dto%2DEnd%20Traceability%20Chain%20Reference)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines revision (T45)

**Anchored on** (from the Google Doc):

> End-to-End Traceability Chain Reference

**Comment:**

> this needs to be consistent with the rest of the guidelines in all the documents.

**Status: Munzir decides**

**Why:** Part of the final consistency pass.

- [ ] applied

### `AAAB60w8-zo`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 58) and `docs/relationships/with-verdicts.md` (near line 71)
- **Go to spot:** [open in with-verdicts](../relationships/with-verdicts.md#:~:text=Measure%20%E2%86%92%20Requirement) · [open in index](../relationships/index.md#:~:text=Measure%20%E2%86%92%20Requirement)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines revision (T45)

**Anchored on** (from the Google Doc):

> Measure → Requirement

**Comment:**

> Invert this so students are not confused when comparing with the deliverable guidelines

**Status: Draft**

**Where:** `docs/relationships/with-verdicts.md`, near line 71
**Where:** `docs/relationships/index.md`, near line 58

**Search for this exact text** (it appears exactly once in each file):

```text
| Measure → Requirement |
```

**Change:** Invert the row so it reads Requirement → Measure with **"specified by"**, matching how the stage pages instruct it. In `with-verdicts.md`, update the verdict and explanation to match. Both files.

New wording: Munzir reviews before merge.

- [ ] applied

### `AAAB60w8-zM`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 25) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../relationships/index.md#:~:text=LML%20%C2%A73.4.11.3%20and%20Fig.%203%2D1)
- **Section:** 4.
- **Blocks:** Guidelines revision (T45), compliance queries

**Anchored on** (from the Google Doc):

> "traced from"**

**Comment:**

> MAJOR PROBLEM:  this is correct. Look for consistency in the deliverables document as well as in these guidelines.

**Status: Munzir decides**

**Why:** This is the final consistency pass itself.

- [ ] applied

## 4 · Labels for filters

### `AAAB5eBvJ7o`

- **Sadaf Shaikh**, 2026-05-07
- **File:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md` (near line 103)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md#:~:text=In%20Innoslate%2C%20create%20an%20Asset)
- **Section:** 3. Step-by-Step Instructions
- **Blocks:** Template project (T19) — EARLIER than the freeze

**Anchored on** (from the Google Doc):

> In Innoslate, create an Asset entity for each selected component. Record the following attributes: component name, manufacturer, model number, and a link to the datasheet as a reference artifact.

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

- [ ] applied

### `AAAB6wHzTzk`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/3-stage-synthesis/d8-design-analysis-report-and-initial-bill-of-materials-bom.md` (near line 220)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d8-design-analysis-report-and-initial-bill-of-materials-bom.md#:~:text=Create%20a%20new%20Artifact%20entity)
- **Section:** 3. Step-by-step Instructions
- **Blocks:** Template project (T19)

**Anchored on** (from the Google Doc):

> Create a new Artifact entity** (e.g., DAR.1) for the Design Analysis Report. Upload the completed report and link it to any trade studies performed while making design choices in Stage 2 using "related to."

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

- [ ] applied

## 5 · SRD auto-link gap

### `AAAB5eL9tMg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/stages/3-stage-synthesis/d3-functional-requirements-document-frd.md` (near line 243)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d3-functional-requirements-document-frd.md#:~:text=Step%209%20%E2%80%94%20Establish%20links)
- **Section:** (none)
- **Blocks:** Traceability standups (T24), quality scan (T25)

**Anchored on** (from the Google Doc):

> Step 9 — Establish links**

**Comment:**

> write instructions on establishing links between actions/assets and requirements generated by SRD because "Generate SRD" doesnt automatically create these links

**Status: Draft**

**Where:** `docs/stages/3-stage-synthesis/d3-functional-requirements-document-frd.md`, near line 243

**Search for this exact text** (it appears exactly once):

```text
### **Step 9 — Establish links**
```

**Change:** Write the steps for linking Actions/Assets to the requirements that "Generate SRD" creates. Needs correct Innoslate steps.

**Also delete the inline note(s) starting:** `write instructions on establishing links`

New wording: Munzir reviews before merge.

- [ ] applied

## 6 · Missing instructions

### `AAABzzIlFRc`

- **Sadaf Shaikh**, 2026-02-06
- **File:** `docs/stages/1-requirements/d1-list-of-stakeholders.md` (near line 338) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../stages/1-requirements/d1-list-of-stakeholders.md#:~:text=Context%20%28meeting%2C%20site%20visit%2C%20email%2C)
- **Section:** (none)
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> “”

**Comment:**

> No relationship that makes sense to me

**Status: Munzir decides**

**Why:** The relationship verb to the Stakeholder entity is blank, and Sadaf says none makes sense. Delete the step, or name a verb?

- [ ] applied

### `AAABzzIlFO0`

- **Sadaf Shaikh**, 2026-02-06
- **File:** `docs/stages/1-requirements/d1-list-of-stakeholders.md` (near line 326)
- **Go to spot:** [open in page](../stages/1-requirements/d1-list-of-stakeholders.md#:~:text=Enter%20a%20meaningful%20name%20%28e.g.%2C%20Factory%20Visit%20%E2%80%93%20Maintenance%20Supervisor%20%E2%80%93%2012)
- **Section:** 4.
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> Enter a meaningful name (e.g., Factory Visit – Maintenance Supervisor – 12 Jan) which includes date, stakeholder role, and context of data collection.

**Comment:**

> mention standard naming convention

**Status: Munzir decides**

**Why:** Which naming convention to state for raw evidence artifacts.

- [ ] applied

### `AAAB57gYWUk`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `docs/stages/3-stage-synthesis/d5-system-requirements-document-srd.md` (near line 66) (placed using the surrounding text in the Google Doc)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d5-system-requirements-document-srd.md#:~:text=4.%20Step%2Dby%2DStep%20Instructions)
- **Section:** 4.
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> Step-by-Step Instructions

**Comment:**

> future iteration: no instructions given to create relationship between system and subsystem requirements

**Status: Munzir decides**

**Why:** Marked "future iteration" by Sadaf. Defer or do now?

- [ ] applied

### `AAAB6feBJ5M`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/2-system-concept/d3-system-requirements.md` (near line 73)
- **Go to spot:** [open in page](../stages/2-system-concept/d3-system-requirements.md#:~:text=2.%20Derive%20Requirements%20from%20Architecture)
- **Section:** 3
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> Derive Requirements from Architecture & Trade Studies

**Comment:**

> provide instructions on deriving system technical requirements.  take inspiration from stage 3 technical requirements instructions.

**Status: Draft**

**Where:** `docs/stages/2-system-concept/d3-system-requirements.md`, near line 73

**Search for this exact text** (it appears exactly once):

```text
#### **2.** **Derive Requirements from Architecture & Trade Studies**
```

**Change:** Add instructions for deriving system technical requirements, adapted from the Stage 3 technical requirements instructions (Deliverable 4, step 3).

**Also delete the inline note(s) starting:** `provide instructions on deriving system technical requirements`

New wording: Munzir reviews before merge.

- [ ] applied

### `AAAB57gYWLs`

- **Sadaf Shaikh**, 2026-05-15
- **File:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md` (near line 279)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md#:~:text=For%20each%20subsystem%20requirement%20in)
- **Section:** 1.
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> For each subsystem requirement in the Technical Requirements Table, create a **Measure** class entity in Innoslate.

**Comment:**

> if the generated subsystem functional requirement is related to the technical requirement, add the technical requirement to the same functional requirement  create traceability with upstream requirement (system) from stage 2   technical requirement in SRD (specified by) Measure

> **Sadaf Shaikh replied:** -technical requirements should be created manually in the SRD along with their associated measure entities

**Status: Draft**

**Where:** `docs/stages/3-stage-synthesis/d4-trade-studies-and-associated-risks.md`, near line 279

**Search for this exact text** (it appears exactly once):

```text
1.  For each subsystem requirement in the Technical Requirements Table, create a **Measure** class entity in Innoslate.
```

**Change:** Add instructions: technical requirements are created manually in the SRD with their Measure entities; technical requirement **specified by** Measure; trace to the upstream system requirement from Stage 2.

**Also delete the inline note(s) starting:** `-technical requirements should be created manually`; `if the generated subsystem functional requirement`

New wording: Munzir reviews before merge.

- [ ] applied

### `AAAB6wHzTzg`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 62) and `docs/relationships/with-verdicts.md` (near line 75)
- **Go to spot:** [open in with-verdicts](../relationships/with-verdicts.md#:~:text=Risk%20%E2%86%92%20Component%20Asset) · [open in index](../relationships/index.md#:~:text=Risk%20%E2%86%92%20Component%20Asset)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> Component TradeStudies (Del. 7) |

**Comment:**

> add after this: issue "references" Analysis Artifact called "Design Analysis Report"

**Status: Ready**

**Where:** `docs/relationships/with-verdicts.md`, near line 77
**Where:** `docs/relationships/index.md`, near line 64

**Search for this exact text** (it appears exactly once in each file):

```text
| Risk → Component Asset |
```

**Change:** Add a new row directly after this one, in both files: Component TradeStudies (Del. 7) | Issue → Design Analysis Report (Artifact) | **"references"**. In `with-verdicts.md`, fill the verdict and explanation columns like the rows around it.

- [ ] applied

### `AAAB6wHzTzQ`

- **Sadaf Shaikh**, 2026-05-21
- **File:** `docs/relationships/index.md` (near line 64) and `docs/relationships/with-verdicts.md` (near line 77)
- **Go to spot:** [open in with-verdicts](../relationships/with-verdicts.md#:~:text=See%20note%20above%20for%20Trade) · [open in index](../relationships/index.md#:~:text=See%20note%20above%20for%20Trade)
- **Section:** 2. LML Relationship Review by Deliverable
- **Blocks:** Guidelines (T45)

**Anchored on** (from the Google Doc):

> See note above for Trade Studies (Del. 4 & 7). Valid generic link. Acceptable. |
> |

**Comment:**

> add some explanation/context

**Status: Draft**

**Where:** `docs/relationships/with-verdicts.md`, near line 77
**Where:** `docs/relationships/index.md`, near line 64

**Search for this exact text** (it appears exactly once in each file):

```text
See note above for Trade Studies (Del. 4 & 7). Valid generic link.
```

**Change:** Replace this explanation cell with a short, self-contained explanation of why a Risk is linked to the Component Asset. Both files.

New wording: Munzir reviews before merge.

- [ ] applied

## 7 · Canvas reporting

### `AAABzy-qwus`

- **Munzir Zafar**, 2026-02-06
- **File:** `docs/stages/1-requirements/d1-list-of-stakeholders.md` (near line 546) (placed using the surrounding text in the Google Doc)
- **Go to spot:** [open in page](../stages/1-requirements/d1-list-of-stakeholders.md#:~:text=4.%20Traceability)
- **Section:** Guidelines
- **Blocks:** Deliverable templates (T92)

**Anchored on** (from the Google Doc):

> Traceability

**Comment:**

> traceability of user needs to extracts needs to be generated in a form that can be made part of the report to be submitted

**Status: Munzir decides**

**Why:** Your own comment about report templates.

- [ ] applied

### `AAABzy-qwug`

- **Munzir Zafar**, 2026-02-06
- **File:** `docs/stages/1-requirements/d1-list-of-stakeholders.md` (near line 564) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../stages/1-requirements/d1-list-of-stakeholders.md#:~:text=%E2%98%90%20All%20statements%20inside%20the)
- **Section:** Guidelines
- **Blocks:** Deliverable templates (T92)

**Anchored on** (from the Google Doc):

> **
> # **

**Comment:**

> Need a template for allowing students to easily populate the deliverables for canvas submission

> **Munzir Zafar replied:** see this chatgpt conversation for details https://chatgpt.com/share/69858d38-40a0-8001-81a5-bb744606d549

**Status: Munzir decides**

**Why:** Your own comment: a Canvas submission template.

- [ ] applied

### `AAABzy-qwuM`

- **Munzir Zafar**, 2026-02-06
- **File:** `docs/stages/1-requirements/d1-list-of-stakeholders.md` (near line 334)
- **Go to spot:** [open in page](../stages/1-requirements/d1-list-of-stakeholders.md#:~:text=Go%20to%20the%20%E2%80%9CDocuments%E2%80%9D%20view%20and%20create%20a%20%E2%80%9CNotes%20Document%E2%80%9D.%20Name)
- **Section:** Guidelines
- **Blocks:** Deliverable templates (T92)

**Anchored on** (from the Google Doc):

> Go to the “Documents” view and create a “Notes Document”. Name it “Extracts from {name of the artifact in step a}”. Number it “EX.n”, where n is an integer.  Keep the template as “Blank Template”.

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
- **File:** `docs/stages/3-stage-synthesis/d0-subsystem-identification.md` (near line 43) (placed using the surrounding text in the Google Doc)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d0-subsystem-identification.md#:~:text=3.%20Step%2Dby%2DStep%20Instructions)
- **Section:** 3.
- **Blocks:** Deliverable templates (T92)

**Anchored on** (from the Google Doc):

> Step-by-Step Instructions

**Comment:**

> Look at all the deliverables in this stage for missing reporting instructions for Canvas.

**Status: Munzir decides**

**Why:** A stage-wide audit of reporting instructions, not a single edit.

- [ ] applied

## 8 · Deferred by author

### `AAAB57gYWJ0`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `docs/stages/1-requirements/d3-stakeholder-requirements-document.md` (near line 31)
- **Go to spot:** [open in page](../stages/1-requirements/d3-stakeholder-requirements-document.md#:~:text=Decompose%20Statements)
- **Section:** Why this deliverable is important

**Anchored on** (from the Google Doc):

> Decompose Statements

**Comment:**

> future iteration: stakeholder req -> scenarios ->action diagrams (some decomposition) add stakeholder functional requirements from the action diagram

**Status: Munzir decides**

**Why:** Marked "future iteration" by Sadaf. Defer or do now?

- [ ] applied

### `AAAB57gYWJ8`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `docs/stages/3-stage-synthesis/d1-low-level-action-diagram.md` (near line 39)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d1-low-level-action-diagram.md#:~:text=3b.%20Build%20the%20Decomposition%20Diagram)
- **Section:** 3b.

**Anchored on** (from the Google Doc):

> Build the Decomposition Diagram

**Comment:**

> future iteration: after concept is finalized, we think of more solution-dep scenarios -> more action diagrams -> system functional requirements from added actions (these should be documented separately)

**Status: Munzir decides**

**Why:** Marked "future iteration" by Sadaf. Defer or do now?

- [ ] applied

### `AAAB5eL9tNY`

- **Sadaf Shaikh**, 2026-05-08
- **File:** `docs/stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md` (near line 114)
- **Go to spot:** [open in page](../stages/3-stage-synthesis/d7-trade-studies-and-associated-risks-component-selection.md#:~:text=Update%20the%20existing%20Measure%20entities)
- **Section:** 3. Step-by-Step Instructions

**Anchored on** (from the Google Doc):

> Update the existing Measure entities from Deliverable 4 with the actual datasheet performance values of the selected component. Do not create new Measure entities — update the threshold and objective values in the existing ones to reflect what the selected component actually delivers.

**Comment:**

> modify this instruction to add a separate Measure entity for the selected component

> **Sadaf Shaikh replied:** future iteration: technical requirement in SRD (specified by) Measure (satisfied by) selected component (specified by) Measure

**Status: Munzir decides**

**Why:** Sadaf's reply marks the change "future iteration". Defer or do now?

- [ ] applied

## 9 · Content and pedagogy

### `AAABzUWr0Tw`

- **Sadaf Shaikh**, 2026-02-03
- **File:** `docs/stages/1-requirements/d3-stakeholder-requirements-document.md` (near line 72) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../stages/1-requirements/d3-stakeholder-requirements-document.md#:~:text=Create%20Issue%20entity%20and%20create)
- **Section:** 3. Stakeholder Requirements Document

**Anchored on** (from the Google Doc):

> Issue entity

**Comment:**

> Mention of an earlier exercise done on risk and issue.

**Status: Munzir decides**

**Why:** Which earlier exercise to mention is yours to say.

- [ ] applied

### `AAABzUWr0R4`

- **Sadaf Shaikh**, 2026-02-03
- **File:** not found in the repo by its anchor text
- **Section:** 3. Stakeholder Requirements Document
- **Blocks:** Freeze (T15), helpful not blocking

**Anchored on** (from the Google Doc):

> “enabled by”.

**Comment:**

> Ailiya to make a separate table on a subset of relationships between entities from LML specification

**Status: Munzir decides**

**Why:** Asks Ailiya for a relationship table. The relationships pages now exist. Probably tick as done.

- [ ] applied

### `AAABzurITFc`

- **Sadaf Shaikh**, 2026-02-04
- **File:** `docs/stages/1-requirements/d3-stakeholder-requirements-document.md` (near line 157) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../stages/1-requirements/d3-stakeholder-requirements-document.md#:~:text=%E2%80%A2%20DON%E2%80%99T%20include%20suggestions%20or)
- **Section:** Why this deliverable is important

**Anchored on** (from the Google Doc):

> Step 4: Identify Risks

**Comment:**

> should we keep it in this section?

**Status: Munzir decides**

**Why:** A question ("should we keep it in this section?"). Needs a yes or no.

- [ ] applied

### `AAABvWHEtbI`

- **Ailiya Fatima**, 2026-02-09
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 306)
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=Prioritize%20use%20cases%2Fscenarios%20based%20on)
- **Section:** (none)

**Anchored on** (from the Google Doc):

> new and important functional requirements.

**Comment:**

> how to add this to innoslate

**Status: Munzir decides**

**Why:** A question ("how to add this to Innoslate"). Needs an answer before any edit.

- [ ] applied

### `AAABvWHEtbE`

- **Ailiya Fatima**, 2026-02-09
- **File:** `docs/stages/1-requirements/d1-list-of-stakeholders.md` (near line 507)
- **Go to spot:** [open in page](../stages/1-requirements/d1-list-of-stakeholders.md#:~:text=Add%20statement%20entity)
- **Section:** 4.

**Anchored on** (from the Google Doc):

> Add statement entity

**Comment:**

> why not use import analyzer here

**Status: Munzir decides**

**Why:** A question: use Innoslate's Import Analyzer instead of adding statements by hand?

- [ ] applied

### `AAAB0D17ImY`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 371) (placed using the surrounding text in the Google Doc). The Google Doc has an empty "Reporting instructions" heading here that the repo omits.
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=Created%20new%20Action%20Diagram%20%28ACT.1)
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on** (from the Google Doc):

> Reporting instructions

**Comment:**

> think about this

**Status: Munzir decides**

**Why:** "think about this". No instruction to act on.

- [ ] applied

### `AAAB0D17ImM`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 371) (placed using the surrounding text in the Google Doc). The Google Doc's checklist here has different items from the repo's.
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=Created%20new%20Action%20Diagram%20%28ACT.1)
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on** (from the Google Doc):

> Student Checklist

**Comment:**

> needs to be reviewed

**Status: Munzir decides**

**Why:** "needs to be reviewed": review the scenarios Student Checklist.

- [ ] applied

### `AAAB0D17ImI`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 398) (placed by the surrounding text; the anchor itself is too short)
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=As%20an%20example%2C%20below%20is)
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on** (from the Google Doc):

> Example

**Comment:**

> should be added in the appendix

**Status: Munzir decides**

**Why:** Move the Moonbase example to an appendix?

- [ ] applied

### `AAAB0D17Il8`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 96)
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=Define%20Input%2FOutput%2C%20Conduit%2C%20Actions%2C%20Directionality%2C)
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on** (from the Google Doc):

> Define Input/Output, Conduit, Actions, Directionality, and Origin using the pop-up displayed in Figure 4.2.

**Comment:**

> elaborate on the attributes for each of these entities

**Status: Munzir decides**

**Why:** Unclear which entities "these entities" means.

- [ ] applied

### `AAABzXMVlDs`

- **Sadaf Shaikh**, 2026-02-10
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 416)
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=Note%20that%20the%20actions%20that)
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on** (from the Google Doc):

> Note that the actions that were created in Figure 4.3 include a number of scenarios in Figure 4.4.  A few adjustments were made from Figure 4.3 to Figure 4.5:
>   - M.2, M.10, and M.12 were put as children of Scenario 3.
>   - M.8 “Receive Habitat” was only part of Scenario 4, so it was made the child of that scenario.
>   - M.13 “Prepare Personnel for Return to Earth” was renamed to S.6 “Rotate Person …

**Comment:**

> pg 87 of real-mbse book

**Status: Ready**

**Where:** `docs/stages/1-requirements/d2-context-diagram.md`, near line 416

**Search for this exact text** (it appears exactly once):

```text
Note that the actions that were created in Figure 4.3 include a number of scenarios in Figure 4.4. A few adjustments were made from Figure 4.3 to Figure 4.5:
```

**Change:** Add a reference at the end of this note: see page 87 of the Real MBSE book.

- [ ] applied

### `AAAB0EbNaqM`

- **Sadaf Shaikh**, 2026-02-11
- **File:** `docs/stages/1-requirements/d2-context-diagram.md` (near line 72)
- **Go to spot:** [open in page](../stages/1-requirements/d2-context-diagram.md#:~:text=For%20%E2%80%9CAs%2Dis%20Architecture%E2%80%9D%2C%20fill%20in)
- **Section:** Uploading Raw Evidence in Innoslate

**Anchored on** (from the Google Doc):

> For “As-is Architecture”, fill in the following attributes:
>     1.  Number: “OCD.1”
>     2.  Name: “Context Diagram for As-is Architecture”
>     3.  Description: {*provide a description}

**Comment:**

> as is architecture captured as context diagram?

> **Sadaf Shaikh replied:** list of scenarios for both?

> **Sadaf Shaikh replied:** list of scenarios for to-be only

**Status: Munzir decides**

**Why:** Is the as-is architecture captured as a context diagram? Sadaf's last reply: list of scenarios for to-be only. Decide and state it.

- [ ] applied

## Added 29 September 2026

### `AAACF1KD4Kk`

- **Sadaf Shaikh**, 2026-08-24
- **File:** `docs/relationships/with-verdicts.md` (near line 15)
- **Go to spot:** [open in page](../relationships/with-verdicts.md#:~:text=LML%20Relationship%20Correction%20%26%20Traceability)
- **Section:** top of the relationship guidelines

**Anchored on** (from the Google Doc):

> LML Relationship Correction & Traceability Matrix Guidelines**

**Comment:**

> This is the authoritative version and the copy tab was just to handle the spring 2026 batch by removing any corrections in the table.

**Status: Munzir decides**

**Why:** Sadaf says the relationship guidelines tab (with verdicts) is authoritative, and the copy tab only existed to give the Spring 2026 batch a table without corrections. Decide whether to retire `index.md` and keep only `with-verdicts.md`.

- [ ] applied
