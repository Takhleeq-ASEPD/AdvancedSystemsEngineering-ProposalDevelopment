---
title: "Trade Studies and Associated Risks (Component Selection)"
stage: "Stage Synthesis"
deliverable_id: stage3-d7
status: draft
last_reviewed: 2026-09-29
---

# Trade Studies and Associated Risks (Component Selection)

This deliverable selects specific components within the technology class chosen in Deliverable 4. Where Deliverable 4 answered "what type of technology can perform this function," this deliverable answers "which specific product within that technology class best meets our derived requirements."

The starting point is the Technical Requirements Table from Deliverable 4. The final specified values in Column 9 are your evaluation criteria — they are not re-derived here. The task is to find candidate components, evaluate them against those criteria, select the best fit, and document the associated risks.

Remember! The goal of stage 3 is an initial system architecture with a **rough-cut BOM** and a **preliminary performance analysis**.

## **2. Why This Deliverable Matters**

Completing this deliverable correctly achieves four things:

- **Make the architecture concrete.** For the first time, requirements and technology classes become specific, real components your industry partner can evaluate and respond to.

- **Creates a defensible rationale.** Every component choice traces back to a requirement, a worst-case scenario, and a datasheet value — not engineering intuition.

- **Produces the first rough-cut BOM.** Real datasheet values and supplier data surface cost, availability, and lead time risks before they become surprises.

- **Resolves open items.** Component selection implies interface standards, connector types, and data formats — closing TBDs that would otherwise compound into integration problems later.

## 

## 

## **3. Step-by-Step Instructions**

Work through the following steps in order:

**Step 1 — Decide how you would document component selection**

As you research and evaluate candidate components in Step 2, document your findings in a format of your choosing — a table, a spreadsheet, a written comparison, or any other structure that captures the information you need to make a defensible selection.

At minimum, your documentation should allow someone to trace each selected component back to the technical requirements it satisfies. You will upload this documentation as an Artifact in Step 6.

**Step 2 — Research Candidate Components**

For each subsystem, research commercially available components and identify at least two to three candidate components within the selected technology class. Use the following sources in order:

1.  **Literature review from Deliverable 4**

    1.  If the literature review in Deliverable 4 identified specific products or manufacturers by name, use these as a starting point.

2.  **Distributor databases**

    1.  Search Digi-Key, Mouser, or equivalent using the technology class name and key technical parameter as search terms.

    2.  Filter by the final specified value as a minimum threshold.

> For example, if the final specified value for detection range is 40 m, filter for components that meet or exceed that figure.

3.  **Manufacturer websites**

> Once a candidate is identified from a distributor database, go directly to the manufacturer's product page and download the datasheet.
>
> Do not rely on distributor summary specifications — always verify against the full datasheet.

For each candidate component found, record its name, manufacturer, model number, and datasheet source in the Technical Requirements Table.

**Step 3 — Use verification requirements to define selection criteria**

Each verification requirement specifies a method (Analysis, Test, Inspection, Demonstration, or Modeling & Simulation) and a measurable threshold.

Convert these directly into selection criteria for component evaluation. For example:

- **Technical requirement**: "The power subsystem shall deliver a minimum of 15W continuous to the payload."

- **Verification requirement**: "The power subsystem shall be verified by test to deliver ≥ 15W at the output terminals under nominal operating conditions."

- **Selection criterion derived**: Does the candidate component's datasheet specify ≥ 15W output, and is that claim independently testable under your conditions?

**Step 4 — Evaluate Candidates Against Selection Criteria**

For each candidate component, compare its datasheet performance figures against the selection criteria:

1.  For each technical parameter, locate the corresponding specification in the datasheet. Record the datasheet value in the table.

2.  Check whether the datasheet conditions match your worst-case scenario assumptions from Deliverable 4.

> Datasheets typically report performance under nominal conditions — if your worst-case scenario involves stressing conditions (e.g., high temperature, low reflectivity, full sunlight), note whether the datasheet addresses those conditions or whether the nominal figure may not hold. Flag any mismatches as open items.

3.  Mark each cell as Pass or Fail against the final specified value.

> A component passes only if its datasheet value meets or exceeds the threshold under conditions consistent with the worst-case scenario.

4.  If no candidate component passes all parameters, flag this as an Issue entity in Innoslate and record what relaxation of requirements or change of technology class would be needed to resolve it.

The book emphasizes keeping "several optional solutions available" before committing, and explicitly warns against locking in the first solution found.

**Step 5 — Select the Component**

1.  Select the optimal candidate that satisfies all technical parameters and secondary criteria including cost, availability, lead time, and supplier reliability, justified through a Pugh matrix or pro/con discussion.

2.  Identify a fallback component — a second candidate that could substitute if the primary selection becomes unavailable. Record both in the table.

3.  In Innoslate, create an Asset entity for each selected component. Record the following attributes: component name, manufacturer, model number, and a link to the datasheet as a reference artifact.

??? note "Sadaf · 2026-05-07"
    also, add the label "Selected component" for easy filtering when we create traceability matrix between functional requirements and selected components
<!-- comment:22 -->


4.  Allocate the component Asset to the relevant subsystem Asset using the "decomposed by" relationship, consistent with the asset hierarchy established in Deliverable 3.

5.  Allocate the component Asset to the Actions it performs using the "performs" relationship, consistent with the functional allocation from Deliverable 3.**Innoslate does not automatically inherit or propagate actions down the hierarchy.**

6.  Update the existing Measure entities from Deliverable 4 with the actual datasheet performance values of the selected component. Do not create new Measure entities — update the threshold and objective values in the existing ones to reflect what the selected component actually delivers.

??? note "Sadaf · 2026-05-08"
    future iteration: technical requirement in SRD (specified by) Measure (satisfied by) selected component (specified by) Measure
<!-- comment:24 -->


??? note "Sadaf · 2026-05-06"
    modify this instruction to add a separate Measure entity for the selected component
<!-- comment:23 -->


**Step 6 — Document the trade study and Decision**

1.  Open Innoslate and go to **Database View**.

2.  Create a new **Artifact** entity. Give it a unique ID (e.g., TS.1) and a descriptive name.

3.  Upload the document containing your component selection analysis.

4.  In the Artifact's relationships panel, add a **“satisfies”** relationship to the subsystem requirements.

5.  Search the component Asset and assign “references” relationship with this Trade study.

6.  Create a Decision entity in Innoslate recording the selected component, the rationale for selection, the fallback component, and any assumptions the selection depends on. Link it to the trade study artifact from Deliverable 4 using the "enabled by" relationship.

**Step 7 — Identify and Document Associated Risks**

Follow the same process as Deliverable 4 Step 5, but with risks specific to the selected component rather than the technology class:

1.  For each selected component, assess risks across the following categories:

    - **Performance risk** — does the datasheet value meet the final specified value only under nominal conditions, with uncertainty under worst-case conditions?

    - **Supply chain risk** — is the component available from multiple suppliers, or is there a single-source dependency? What is the lead time?

    - **Obsolescence risk** — is the component approaching end-of-life, or is it a recently released product with an unproven supply history?

    - **Integration risk** — does the component require drivers, calibration procedures, or interface adaptors that could introduce compatibility issues with adjacent components?

    - **Environmental risk** — does the component's rated operating range match the environmental requirements in SRD Section 3.9?

2.  For each risk, create a Risk entity in Innoslate following the same format as Deliverable 4: unique ID, description, likelihood, consequence, assignee. Link it to the selected component Asset entity using "caused by" and to the affected requirement using "caused by".

3.  For any risk rated Medium or above, document a mitigation strategy. The fallback component identified in Step 4 serves as the primary mitigation for supply chain and obsolescence risks — link the fallback component Asset to the Risk entity using "resolves."

??? note "Sadaf · 2026-05-21"
    component cannot resolve a risk. Risk is resolved by decision and component should be linked to that decision.
<!-- comment:27 -->


4.  Update the Risk Chart diagram created in Deliverable 4 to include the new component-level risks.

**Step 8 — Resolve TBDs from Deliverable 4**

Component selection is the event that resolves many TBDs carried forward from Deliverable 4 and the SRD. Before closing this deliverable:

1.  Review all open Issue entities in Innoslate from Deliverable 4 that were flagged as pending product selection. For each one, determine whether the selected component resolves it and update the Issue entity status accordingly.

2.  Review SRD Sections 3.3 and 3.4 for interface entries marked TBD pending product selection. Update these with the specific interface type, protocol, and connector standard implied by the selected component.

3.  Review SRD Section 3.5 for data items marked TBD. Update encoding formats and data types where the selected component implies a specific standard.

**Step 9 — Review Traceability Matrices**

Review the traceability matrices below to verify that all entities created or updated in this deliverable are properly linked within the model. Where a matrix does not yet exist, create it. Where one exists from a prior deliverable, open and review it — do not recreate it.

*The goal is not to generate matrices for their own sake, but to confirm that nothing is floating unconnected in the model.*

1.  Requirements → Component Assets (satisfied by)

> Confirms that every subsystem technical requirement from the FRD is satisfied by at least one selected component. Any requirement with no component assigned is an unresolved gap.

2.  Component Assets → Actions (performs)

> Confirms that every leaf-level action in the action diagram has been allocated to a component asset via the "performs" relationship. Any action with no asset is functionally unallocated — which at this stage is a red flag.

3.  Component Assets → Subsystem Assets (decomposed by)

> Confirms the physical hierarchy is complete and every selected component sits within the correct subsystem in the asset hierarchy. This is the backbone of your rough-cut BOM — if a component is missing here, it won't appear in the BOM.

## **6. References**

\[1\] Dam, S. H. Real MBSE: Model-Based Systems Engineering Using LML and Innoslate. — Primary source for the synthesis process, trade study methodology, COTS/GOTS risk identification, and functional analysis and allocation.

\[2\] Jackson, P. L. (2009). Getting Design Right: A Systems Approach. CRC Press. — Source for subsystem identification (Ch. 4), interface identification, and design structure matrix methods (Ch. 6).

\[3\] MIL-STD-499B (Draft). Systems Engineering. — Referenced in the MBSE textbook as the basis for trade study types associated with requirements, functional, and synthesis processes.

del 8 - analysis report + BOM

**Design Analysis Report and**
