---
title: Relationship Guidelines (with review verdicts)
---

# Relationship Guidelines — with review verdicts

Sadaf's first version. Same table, plus a verdict column marking each instructed relationship
Correct, Incorrect or Caution, with the reasoning.

The other version, `index.md`, is the same corrections written without the verdicts. Both have
open comments on them, so both are being edited. One of them goes once everything is propagated.

---

**LML Relationship Correction & Traceability Matrix Guidelines**
Spring 2026  |  Habib University
## **1. Purpose and Scope**
This document provides two sets of guidelines to help you review and improve your Innoslate model.

  - Section 2 cross-references every LML relationship name explicitly instructed in the ASEPD deliverables document against LML Specification 2.0, identifies errors and non-standard usage, and gives the correct verb to use instead.
  - Section 3 defines which traceability matrices to generate, what entity pairs each matrix covers, and the minimum population thresholds required for a model to be considered reviewable.
These guidelines apply to all three gate stages: Requirements (Gate 2), System Concept (Gate 3), and Initial System Architecture (Gate 4).
**Note: **All relationship names in LML are bidirectional. The table in Section 2 always states the relationship from the perspective of the first entity in the pair (the source). The inverse is implied.
## **2. LML Relationship Review by Deliverable**
The table below lists every entity pair for which the ASEPD deliverables document instructs a specific relationship name. Each entry is evaluated against LML Specification 2.0 and assigned one of three verdicts:

|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| **✅ Correct** | Relationship is valid in base LML 2.0 for this entity pair. | **❌ Incorrect** | Relationship does not exist or direction is wrong in LML 2.0. | **⚠️ Caution** | Relationship exists only in the SysML extension (Appendix A) or semantics are weak. |

**Stage 1— Requirements Stage**

|  |  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- | :- |
| **Deliverable** | **Entity Pair (Source → Target)** | **Instructed Verb** | **Verdict** | **Correct Entity Pair** | **Correct LML 1.4 Verb** | **Explanation / Action Required** |
| Raw Evidence(Del. 1) | Notes Document → Raw Artifact | **"related to"** | **✅ Correct** |  |  | Relationships that exist between two artifacts are: “related to” and “decomposed by”. Out of the two, “related to” is more appropriate. |
| User Needs(Del. 1) | Statement (UN.1.n) → Statement (Notes Document) | **"traced to"** | **✅ Correct** |  |  | LML §3.4.0.2.13 defines traced from/traced to between Statements. Direction is correct: a refined UN Statement is traced to its source Statement in the Notes Document. |
| Stakeholder Req.(Del. 3) | Requirement (SR) → Statement (UN)  | **"traced from"** | **❌ Incorrect** |  | "traced to" | LML §3.4.11.3 and Fig. 3-1 confirm: Requirement traced from Statement is the primary requirements traceability path. No change needed. |
| Stakeholder Req.(Del. 3) | Requirement (SR) → Issue entity | **"causes"** | **✅ Correct** |  |  | LML §3.4.0.2.1 defines causes specifically toward a Risk entity. Since the issue is modelled as a Risk entity, causes is correct. If modelled as a Decision, use results in instead.  |
| Stakeholder Req.(Del. 3) | Trade Study (Artifact) → Issue/Risk | **"resolves"** | **⚠️ Caution** | Decision → Risk** ** | "resolves" | **Replace relationship between trade study and risk with decision and risk.** It is the decision that resolves the risk. Resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Risk, and Decision enabled by Trade Study.  |
| Stakeholder Req.(Del. 3) | Decision → Trade Study (Artifact) | **"enabled by"** | **✅ Correct** |  |  | LML §3.4.0.2.3 defines enables/enabled by toward Decision. The direction here is correct: Decision enabled by Trade Study Artifact. Ensure the relationship is created on the Decision entity pointing to the Artifact, not the reverse. |
| High-level Action Diagrams(Del. 4) | Action → Requirement | **"satisfies"** | **❌ Incorrect** |  | "traced to" | satisfies does not exist in base LML 2.0 (Table 3-3). |
| Verif. Req.(Del. 5) | Characteristic → Verif. Requirement | **"specifies"** | **✅ Correct** |  |  | LML §3.4.4.2 and §3.4.0.2.12 confirm: Characteristic specifies a Requirement or Verification Requirement. Direction and entity types are correct. |
| Verif. Req.(Del. 5) | Verif. Requirement → Decision | **"enables"** | **✅ Correct** |  |  | LML §3.4.0.2.3 defines enables/enabled by toward Decision. Direction is correct: Verification Requirement enables Decision. No change needed. |
| Verif. Req.(Del. 5) | Verif. Requirement → Issue/Risk | **"causes"** | **✅ Correct** |  |  | LML §3.4.0.2.1 defines causes specifically toward a Risk entity. Since the issue is modelled as a Risk entity, causes is correct. If modelled as a Decision, use results in instead. |
| Verif. Req.(Del. 5) | Verif. Requirement → Test Case | **"verified by"** | **✅ Correct** |  |  | LML §3.4.11.4.2 explicitly defines verifies/verified by between Verification Requirement and Test Case. This is correct. Ensure the relationship direction is verified by placed on the Verification Requirement pointing to the Test Case. |

**Stage 2 — System Concept Stage**

|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| **Deliverable** | **Entity Pair (Source → Target)** | **Instructed Verb** | **Verdict** | **Correct LML 2.0 Verb** | **Explanation / Action Required** |
| System Req.(Del. 3) | System Requirement → Stakeholder Requirement | **"refines" or "satisfies"** | **❌ Incorrect** | "traced to" | Neither refines nor satisfies exists in base LML 2.0 Table 3-3. The correct verb is traced from: System Requirement traced from Stakeholder Requirement. This is the same traceability verb used for Stakeholder Requirements tracing to User Needs. Using different verbs for the same traceability pattern breaks the chain. |
| System Req.(Del. 3) | System Requirement → Decision | **"enabled by"** | **✅ Correct** | "enabled by" (correct) | LML §3.4.0.2.3 defines this correctly. The Decision that drove the system requirement enables it. Ensure the relationship is created on the Requirement entity, pointing to the Decision. |
| System Req.(Del. 3) | System Requirement → Trade Study (Artifact) | **"derived from"** | **❌ Incorrect** | ”sourced by” | derived from does not exist in base LML 2.0. The correct relationship between a Requirement and a supporting Artifact is references / referenced by (§3.4.0.2.8): Requirement references Trade Study Artifact. This captures that the artifact informs the requirement without implying derivation, which is not an LML concept. |
| Verif. Req. forSystem Req. | Verif. Requirement → System Requirement | **"verifies"** | **✅ Correct** |  | LML §3.4.11.4.2 defines verifies/verified by. This is correct and consistent with the Gate 2 approach. Ensure this relationship is created for every system requirement, not just selected ones. |

**Stage 3 — Initial System Architecture Stage**

|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| **Deliverable** | **Entity Pair (Source → Target)** | **Instructed Verb** | **Verdict** | **Correct LML 2.0 Verb** | **Explanation / Action Required** |
| Low-level Action Diagrams    (Del. 1) | Asset → Action | **"performs"** | **✅ Correct** |  | LML §3.4.1.2.3 defines performed by / performs. Asset performs Action is the canonical functional allocation relationship. Correct. |
| Low -level Action Diagrams    (Del. 1) | Action → Action (decomposition) | **"decomposes"** | **✅ Correct** |  | LML §3.4.0.2.2 defines decomposed by / decomposes. Parent Action decomposed by child Action is standard. Correct. |
| Physical I/O(Del. 2) | I/O entity → Conduit | **"transferred by"** | **✅ Correct** |  | LML §3.4.5.3.2.2 defines transfers / transferred by between Conduit and Input/Output. The direction here (I/O transferred by Conduit) is correct. |
| Physical I/O(Del. 2) | Asset → Asset (hierarchy) | **"decomposed by"** | **✅ Correct** |  | Standard LML §3.4.0.2.2. Parent Asset decomposed by child Asset establishes subsystem hierarchy. Correct. |
| Subsystem Req. (Del. 5) | Subsystem Req → System Req | **Direct relationship doesnt exist.** |  | “traced to” | Use SRD to create relationship between subsystem requirements and system requirements. |
| Trade Studies(Del. 4 & 7) | Trade Study (Artifact) → Subsystem Requirement | **"satisfies"** | **❌ Incorrect** | "sourced by” | As noted for Del. 7 high-level actions: satisfies is not in base LML 1.4.  |
| Trade Studies(Del. 4 & 7) | Issue/Risk → Trade Study (Artifact) | **"caused by"** | **✅ Correct** |  | LML §3.4.10.2 confirms: Risk caused by other entities, and other entities cause Risk. If the Issue is a Risk entity, caused by from the Risk to the Artifact is valid. Correct. |
| Trade Studies(Del. 4 & 7) | Decision → Trade Study (Artifact) | **"enabled by"** | **✅ Correct** |  | Consistent with Stage 1 and Stage 2 usage. LML §3.4.0.2.3. Correct. |
| Trade Studies(Del. 4 & 7) | Measure → Requirement | **"specified by"** | **❌ Incorrect** | "specifies" placed on Requirement(direction is inverted) | In LML §3.4.0.2.12, specified by is placed on the entity being described, pointing to the Characteristic / Measure. The deliverables document instructs placing the relationship on the Measure entity, which reverses the direction. Corrective action: open each Requirement entity, go to Relationships, and create specified by pointing to the Measure — not the other way around. |
| Trade Studies(Del. 4 & 7) | Risk → Trade Study (Artifact) | **"related to"** | **✅ Correct** |  | LML §3.4.0.2.9 defines related to as a generic peer-to-peer link. It is valid here, though references would be more semantically precise (the Risk is informed by the artifact). Either is acceptable. |
| Trade Studies(Del. 4 & 7) | Risk → Requirement | **"traced from"** | **✅ Correct** |  | LML §3.4.0.2.13 allows traced from across entity classes. A Risk entity traced from a Requirement captures that the risk is tied to that requirement's achievement. Correct. |
| Trade Studies(Del. 4 & 7) | Decision (mitigation) → Risk | **"resolves"** | **✅ Correct** |  | LML §3.4.0.2.10 defines resolves / resolved by: a Decision resolves a Risk. This is the correct pattern for documenting mitigation decisions. Correct. |
| Component TradeStudies (Del. 7) | Component Asset → Subsystem Asset | **"decomposed by"** | **✅ Correct** |  | Standard asset hierarchy decomposition (§3.4.0.2.2). Subsystem Asset decomposed by Component Asset. Correct. |
| Component TradeStudies (Del. 7) | Component Asset → Action | **"performs"** | **✅ Correct** |  | LML §3.4.1.2.3. Correct and consistent with granular action diagram allocation. Must be explicitly set — Innoslate does not propagate this from parent assets. |
| Component TradeStudies (Del. 7) | Risk → Component Asset | **"related to"** | **✅ Correct** |  | See note above for Trade Studies (Del. 4 & 7). Valid generic link. Acceptable. |
| Verif. Req. forSubsystem Req. | Verif. Requirement → Subsystem Requirement | **"verifies"** | **✅ Correct** |  | Consistent with Gate 2 and Gate 3. LML §3.4.11.4.2. Correct. |

## **3. Traceability Matrix Guidelines**
## **3.1  Why Traceability Matrices Matter for Review**
A traceability matrix is a two-dimensional table that confirms every entity in one class is connected to at least one entity in another class through a specific LML relationship. Matrices serve three purposes:

  - Completeness check: every row and every column must have at least one cell populated. Sparse rows or columns signal missing relationships, not missing content.
  - Correctness check: the relationship verb used to generate the matrix must match the LML 2.0 standard — this is why Section 2 matters before you generate matrices.
  - Coverage check: the population density of the matrix indicates whether the engineering work is superficial (one link per row) or thorough (multiple supporting links).
## **3.2  Required Matrices by Gate**
The following table defines the matrices that must be generated, and the LML relationship that drives each one..

|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| **Matrix Name** | **Row Entity (source)** | **Column Entity (target)** | **LML Relationship** | **Review Purpose** | **How to Create** |
| **Stage 1 — Requirements Stage** |  |  |  |  |  |
| **Stakeholder Req. to User Needs** | Requirement (SR) | Statement (UN) | **traced to** | Confirms every stakeholder requirement traces to at least one user need. Orphan requirements (no column link) are ungrounded and likely invented. Multiple SR rows tracing to the same UN column indicate requirements that may need merging. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Query” in Y-axis field.     \- Enter “class:Requirement order:number number:SR.\* class:Requirement”.    \- Press “Update”.    \- Apply filter “Query” in Top(X axis) and enter “order:number number:UN.\* class:Statement”.    \- Set Relationship  to “traced to”.    \- Review traces.    \- Save Matrix. |
| **High Level Actions/Scenarios to High Level Stakeholder Functional Req. ** | Action | Requirement (SR) | **traced to** | Confirms every scenario traces to atleast one stakeholder requirement. We're doing it earlier because at this stage of the project you hadn’t yet decomposed into system requirements, and we want you to verify your functional model has coverage before that decomposition. | 1\. Follow the steps 1-6  in Section 3.4.    2\. Select Query in Yaxis field and enter query:    **order:modified is:top class:Action**    3\. Press “Update”    4\. Under "Top (X Axis)" enter the query:     **order:number number:SR.\* class:"Requirement" label:"Functional Requirement" **    5\. Set Relationship to "traced to".    6\. Review traces and save Matrix.    This gives the top level actions from all the action diagrams created. |
| **Verif. Req. to Stakeholder Req.** | Verif. Requirement (VR.1) | Requirement (SR) | **verifies** | Confirms every stakeholder requirement has a verification path. Any SR column with no populated cell means that requirement cannot be objectively proven — it must either be made verifiable or removed. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Entity” in Y-axis field.     \- Enter “VR.1” and select the Stakeholder Verification Requirements Document. Make sure this document has just the Verification Requirements.    \- Press “Update”.    \- Apply filter “Query” in Top(X axis) and enter the query:    query:     **order:number number:SR.\* class:"Requirement"**    \- Set Relationship to “verifies”.    \- Review traces.    \- Save Matrix. |
| **Stage 2 — System Concept Stage** |  |  |  |  |  |
| **System Req. to Stakeholder Req.** | Requirement (SysReq) | Requirement (SR) | **traced to** | Confirms every system requirement is grounded in a stakeholder requirement. Any SysReq row with no SR column link is a gold-plated requirement (added without stakeholder basis). Columns with no row link indicate stakeholder requirements not yet decomposed into system requirements. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Entity” in Y-axis field.     \- Enter “SYS.1” and select the System Requirements Document. Make sure this document has just the System Requirements.    \- Press “Update”.    \- Apply filter “Hierarchy” in Top(X axis) and Search for “SR.1” in Root Entity.    \- Set Relationship type to “traced to”.    \- Review traces.    \- Save Matrix. |
| **System Functional Req. to Scenarios** | Requirement (SysReq) | Action | **traced to** | Confirms every system functional requirement is traced to a scenario. In other words, it confirms that every operational scenario can be executed by the architecture. | 1\. Open the top-level action diagram.    2\. Open the Hierarchy or Tree diagram to review the traces between functional requirements/actions and scenarios. |
| **Verif. Req. to System Req.** | Verif. Requirement (VR.2) | Requirement (SysReq) | **verifies** | Confirms every system requirement has a verification path. System requirements are solution-dependent and more specific — most should be directly verifiable. Columns with no row link must be addressed before Gate 3 approval. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Entity” in Y-axis field.     \- Enter “VR.2” and select the System Verification Requirements Document. Make sure this document has just the Verification Requirements.    \- Press “Update”.    \- Apply filter “Hierarchy” in Top(X axis) and Search for “SYS.1” in Root Entity.    \- Set Relationship type to “verifies”.    \- Review traces and Save Matrix. |
| **Risks to Requirements** | Risk | Requirement (SR or SysReq) | **caused by** | Confirms that identified risks are anchored to specific requirements whose achievement they threaten. A Risk entity with no requirement link is floating and cannot be prioritised. A requirement with many Risk links is a signal of high-risk scope that warrants trade study attention. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Query” in Y-axis field.     \- In Query field, type “order:modified- class:Risk”     \- Press “Update”.    \- Apply filter “Hierarchy” in Top(X axis) and Search for “Stakeholder Requirements Document” for Stakeholder Requirements and “System Requirements Document” for System requirements, respectively  in Root Entity.    \- Set Relationship type to “caused by”.    \- Review traces and save Matrix. |
| **Stage 3 — Initial System Architecture Stage** |  |  |  |  |  |
| **System Asset to System Action** | Asset | Action | **performs** | This is the functional allocation process at the system-level and ensures that every action is allocated to an asset. | \- Go to Schema Editor and create a label “to-be” for Asset and Action classes.    \- Go to Database view and apply the label “to-be” to Assets and Actions that belong to the To-be Architecture.    \- Follow the steps 1-6  in Section 3.4.     \- Select “Query” in Y-axis field and enter the query:    **order:number class:Asset label:to-be**    \- Press “Update”.    \- Apply filter “Query” in Top(X axis) and enter query:    **order:number class:Action label:to-be**    \- Set Relationship type to “performs”.    \- Review traces and save Matrix. |
| **Subsystem Req. to System Req.** | Requirement (SubReq) | Requirement (SysReq) | **traced to** | Confirms every subsystem requirement is grounded in a system requirement. This matrix closes the full requirements chain: User Need → Stakeholder Req → System Req → Subsystem Req. Any SubReq row with no column link is an ungrounded subsystem requirement. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Entity” in Y-axis field.     \- Enter “SUBSYS.1” and select the Subsystem Requirements Document.     \- Press “Update”.    \- Apply filter “Hierarchy” in Top(X axis) and Search for “SYS.1” in Root Entity.    \- Set Relationship type to “traced to”.    \- Review traces and save Matrix. |
| **Requirements to Components** | Requirement (SysReq or SubReq) | Asset (component) | **satisfied by** | Generated from the satisfied by relationship chain through trade study artifacts. Confirms every technical requirement is met by a selected component. This is the primary matrix the industry panel will scrutinise to confirm build-vs-buy decisions are traceable. | 1\. Go to Schema Editor    2\. Create Label “Selected Component” for Asset Class and “Technical” for Requirement class.    3\. Go to Database view    4\. Apply “Selected Component” to each component that was selected after the trade study.    5\. Open SRD and create separate technical requirement entities for functional requirements with associated Measure entities. Label these requirements “Technical”.    6\. Remove relationship between functional requirements and Measure entities and instead create relationship between technical requirements and Measure entities using “specified by”.    7\. Follow the steps 1-6  in Section 3.4.    8\. Select “Query” in Yaxis field and create query:    order:number class:"Requirement" label:Technical    9\. Press “Update”    10.under "Top (X Axis)" enter the query: order:modified class:Asset label:”Selected Component”    11\. Set Relationship type to “satisfied by”.    12\. Review traces and save Matrix. |
| **Component to Function** | Asset (component) | Action (leaf-level) | **performs** | Confirms every leaf-level action in the granular action diagram is performed by at least one component asset. Unallocated action columns mean the system has functions with no physical implementation — a critical design gap. Multiple asset rows linked to one action identify redundancy or parallel execution. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Query” in Y-axis field and enter the query:    **order:number class:Asset label:Selected Component**    \- Press “Update”.    \- Apply filter “Query” in Top(X axis) and enter query:    **order:number class:Action is:leaf**    \- Set Relationship type to “performs”.    \- Review traces and save Matrix. |
| **Interface Req. to Conduit** | Requirement | Connection | **traced to** | Confirms every conduit has a corresponding interface requirement created. | 1\. Go to Schema Editor and create a label “Interface” for the Requirement class.    2\. Open the SRD and apply the label “Interface” to all the interface requirements.    3\. Follow the steps 1-6 in Section 3.4.    4\. Create Y-axis Query type:    Order:number class:Requirement label:Interface    5\. Create X-axis Query type:    Order:number class:Conduit    6\. Set Relationship type to “traced to”    7\. Press Update.    8\. Review traces and save Matrix. |
| **Verif. Req. to Subsystem Req.** | Verif. Requirement (VR.3) | Requirement (SubReq) | **verifies** | Confirms every subsystem requirement has a verification path. This is the most detailed verification matrix and often reveals missing test planning. Any SubReq column with no VR row must be addressed before the architecture review. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Query” in Y-axis field and type query:    **order:number number:VR.3.\* class:Requirement**    \- Press “Update”.    \- Apply filter “Hierarchy” in Top(X axis) and Search for “SUBSYS.1” in Root Entity.    \- Set Relationship type to “verifies”.    \- Review traces and save Matrix. |
| **Risks to Components** | Risk | Asset (component) | **caused by** | Confirms component-level risks are attached to specific components. Risks with no asset link cannot be managed. Particularly important for COTS/GOTS components where supply chain and obsolescence risks must be explicitly tracked. | \- Follow the steps 1-6  in Section 3.4.     \- Select “Query” in Y-axis field.     \- In Query field, type “order:modified- class:Risk”     \- Press “Update”.    \- under "Top (X Axis)" enter the query: order:modified class:Asset label:”Selected Component”    \- Review traces. |

## **3.3  Population Thresholds and What They Signal**
The minimum sizes in Section 3.2 are floors, not targets. The table below explains what different population densities indicate to a reviewer and what action should be taken in each case.

|  |  |  |  |  |
| :- | :- | :- | :- | :- |
| **Population Level** | **What It Looks Like** | **Signal to Reviewer** | **Likely Root Cause** | **Corrective Action** |
| **Below minimum threshold** | Many empty rows or columns; fewer cells than the minimum size guide | Model is incomplete. Matrix is not reviewable. | Missing entities, missing relationships, or wrong relationship verb used to generate the matrix | Add missing entities; fix relationship verbs per Section 2; re-generate matrix before submission |
| **At minimum (1 link per row/col)** | Every row and column has exactly one populated cell; matrix is diagonal or near-diagonal | Requirements are superficially linked. Coverage is thin. | Requirements were written one-to-one with needs rather than being properly decomposed; or relationships were added to pass the check rather than to reflect the model | Review whether each requirement genuinely traces to only one source. If yes, this is acceptable. If relationships were forced, remove them and re-examine decomposition. |
| **Good coverage (2–4 links per row)** | Most rows have 2–4 populated cells; some concentration in high-priority requirements | Model reflects realistic traceability. Healthy. | Requirements were derived through proper decomposition; multiple user needs support key requirements; multiple verification methods applied to complex requirements | No action needed. Highlight high-link-count requirements in the review presentation as risk-informed priorities. |
| **Dense (5+ links per row)** | Many cells populated; almost every combination has a link | Possible over-linking. Review carefully. | Relationships may have been created indiscriminately to appear thorough; or the model genuinely captures a highly interdependent system | Check that every link reflects a real engineering dependency. Remove links that exist only to populate the matrix. Over-linked matrices obscure genuine priorities. |

## **3.4  How to Generate a Matrix in Innoslate**
To create a Traceability Matrix, simply follow these steps:

1.  Navigate to Database View. 
2.  Create an Artifact entity.
3.  Assign the 'Matrix' label on the left sidebar.
4.  Give the Matrix a Number (mandatory) and Name (optional).
5.  Click 'Open' and select Traceability Matrix.
6.  Innoslate will navigate to the Traceability Matrix where the 'Missing Matrix' window will appear.
7.  Select your preferred method to access Y-axis entities, 'Query' or Root 'Entity' from the dropdown menu.
8.  On the left sidebar, select the X-axis via Hierarchy, Query or Related.
9.  (optional) If Query or Hierarchy is selected in step 8, users will then want to select the Relationship desired in the dropdown that appears (or type in the field to pull it up).
10. The Traceability Matrix View will then be completed to create relationships among the entities displayed in the matrix. Select 'Save' on the toolbar.
## **3.5  How to Treat Floating Requirements Identified through Traceability Matrix**
During the process of generating Traceability matrices as instructed in Section 3.2, you may come across floating requirements, i.e. requirements that are not linked to a parent. For these requirements, follow the steps below:

1.  Go to Schema Editor and add a label “Orphan” to the Requirement class.
2.  Open any traceability matrix that contains floating requirements and using the wrench icon on the top-right, select Traceability Assist.
3.  Review the links created by the Assist.
4.  If floating requirements still exist, add a label “Orphan” to those requirements.
5.  To review Orphan requirements, go to Database view.
6.  Create a filter to isolate floating requirements using the query “class:Requirement label:Orphan”
7.  If parent is genuinely missing, create an issue and set the relationship Issue “caused by” Requirement.
## **4. End-to-End Traceability Chain Reference**
The diagram below shows the complete LML traceability chain your model should reflect by the end of Gate 4. Each arrow represents a relationship. Where Section 2 has identified a correction, the corrected verb is shown.

|  |
| :- |
| **EVIDENCE LAYER**    **══════════════**    **Raw Artifact (ART.n)**    **    ↑ sourced by**    **Notes Document Statement (EX.n.n)**    **    ↑ traced to**    **USER NEEDS LAYER**    **════════════════**    **User Need Statement (UN.1.n)**    **    ↑ traced to**    **STAKEHOLDER REQUIREMENT LAYER**    **══════════════════════════════**    **Stakeholder Requirement (SR.1.n) ← verifies ── Verification Requirement (VR.1.n)**    **    ↑ traced to                                                                                     ↑ verified by**    **                                                                                                     Test Case**    **SYSTEM REQUIREMENT LAYER**    **═════════════════════════**    **System Requirement (SysReq.n) ←  verifies ── Verification Requirement (VR.2.n)**    **    ↑ traced to    **    **    ↓ sourced by  →  Trade Study (Artifact) ← enabled by ── Decision**    **    ↓ enabled by  →  Decision                                    ↓ resolves**    **                                                                                   Risk**    **SUBSYSTEM REQUIREMENT LAYER**    **════════════════════════════**    **Subsystem Requirement (SubReq.n) ← verifies ── Verification Requirement (VR.3.n)**    **    ↑ traced to**    **    ↓ specified by → Measure (threshold)**    **    ↓ sourced by   → Trade Study (Artifact)**    **ACTION / FUNCTIONAL LAYER**    **═════════════════════════**    **Action (leaf-level) ── traced to → Subsystem Functional Requirement**    **    ↓ decomposes  parent Action**    **    ↓ performed by Component Asset**    **COMPONENT / PHYSICAL LAYER**    **═══════════════════════════**    **Subsystem Asset**    **    ↓ decomposed by**    **Component Asset (selected via Trade Study)**    **    ↓ performs**    **Action (leaf-level)**    **INTERFACE LAYER (cross-cutting)**    **═══════════════════════════════**    **Interface Requirement ── traced to → Conduit**    **I/O Entity ── transferred by → Conduit**    **RISK LAYER (cross-cutting)**    **═══════════════════════════**    **Risk ── caused by → Requirement (SR / SysReq / SubReq)**    **Risk ── caused by → Component Asset**    **Risk ── related to → Trade Study (Artifact)**    **Decision ── resolves → Risk** |

Before stage 3, the supervisor should be able to pick any leaf-level action in the action diagram and trace upward through this chain to the raw evidence that originated the need for that function. If any step in the chain breaks — an empty cell in a matrix, a missing relationship, or a non-LML verb — the model is incomplete.


#
