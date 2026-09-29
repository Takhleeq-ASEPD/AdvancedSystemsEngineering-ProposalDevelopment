---
title: "Trade Studies and Associated Risks"
stage: "Stage Synthesis"
deliverable_id: stage3-d4
status: draft
last_reviewed: 2026-09-29
---

# Trade Studies and Associated Risks

This deliverable translates subsystem functional requirements from the FRD into preliminary technical requirements. It does this by combining analytical worst-case reasoning, a structured technology class trade study, and risk identification. It sits between two milestones: after **subsystem identification** and the **FRD**, and before **detailed component selection**.

It answers three questions in sequence:

1.  What must each subsystem do, in technical terms — and how well?

2.  What technology classes exist that can provide that capability?

3.  Which technology class best satisfies the derived requirements, and what risks does that choice carry?

The goal is an initial system architecture with a **rough-cut BOM** and a **preliminary performance analysis**.

**When to Stop Decomposing**

Knowing when to stop is one of the hardest judgement calls in systems engineering. Dam gives three clear signals:

1.  **You can point to a technology class that exists.** You do not need a part number. You need to be able to say: *"a technology of this type exists and is procurable."* If you cannot point to anything real that performs the function, go deeper. If you are specifying how a component works internally, you have gone too far.

> Dam: *"When you can identify potential products or at least classes of products, you're done."*

2.  **You are specifying performance end-to-end, not per component.** The performance budget belongs to the subsystem as a whole — not to individual components within it. If you find yourself splitting a budget between a sensor, a processor, and a communication link, stop. That belongs to detailed design.

> Dam: *"define end-to-end performance factors, not detailed ones for each asset."*

3.  **You have not accidentally specified a solution.** Read your Technical Requirements Table entry and ask: could more than one technology class satisfy this? If only one specific product could satisfy it, you have over-specified. Roll back up a level and use functional wording.

> Dam: *"make sure you do not over-specify or specify a particular solution. If necessary, roll back up a level."*

## **2. Why This Deliverable Matters**

Technical requirements at the subsystem level are not given — they must be derived. The functional requirements in the FRD tell each subsystem *what it must do*; *they do not tell it how well it must do it*, or which engineering parameters govern the ability to do it.

Without a systematic method for making that translation, technical requirements become arbitrary — set by engineering intuition, copied from datasheets of familiar products, or simply left unspecified. This causes serious problems during integration and verification.

Dam \[1\] makes this point explicitly in the context of requirements trade studies: "Conducting an explicit tradeoff on requirements is crucial to optimisation and ensures that you have the right set of requirements" (Ch. 7). This deliverable enforces that discipline.

Completing this deliverable correctly achieves four things:

- **It provides evaluation criteria** for technology selection that are traceable to functional requirements, not to product preferences.

- **It makes the rationale for each technical requirement explicit and reviewable**, so that stakeholders can challenge assumptions rather than accept numbers on faith.

- **It surfaces risks associated with each technology class** before a selection is committed — consistent wit<span class="mark">h Dam’s guidance th</span>at "COTS/GOTS comes with a risk: you do not control their development schedule."

- **It keeps the functional architecture abstract**, preventing over-specification, as Dam <span class="mark">warns:</span> "Make sure you do not over-specify (or specify a particular solution). If necessary, roll back up a level."

## **3. Step-by-Step Instructions**

Work through the following steps in order:

**Step 1 - Create a Technical Requirements Table**

1.  Create an Excel sheet

2.  Name the column headings the following:

    1.  System Functional Requirement

    2.  Subsystem functional requirement

    3.  Technical parameter

    4.  Rationale for parameter (including citations)

    5.  Worst-case scenario

    6.  Derivation method

    7.  Derived value

    8.  Margin applied

    9.  Final specified value

    10. Open Item (yes/no)

**Step 2 - Review Literature**

#### **2a. Conduct a Literature Review of Subsystem Functionality and Technology Classes**

For each subsystem functional requirement, conduct a literature review that answers the following three questions in order:

**Question 1 — What do practitioners measure to characterise this function?**

Start with **review or survey papers** — not datasheets. Review papers synthesise the state of the art and will tell you what performance quantities the field uses to compare approaches, which is what you need before anything else.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><p><strong>Search</strong></p>
<p><strong>Strategy</strong></p></th>
<th><em>Use Google Scholar or Scopus with terms like "[subsystem function] review" or "survey of [subsystem function] technologies." Prioritise papers from the last five years.</em></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A good review paper will identify:

- The quantities used to compare technology classes (e.g., detection range, update rate, angular resolution) → these become candidate technical parameters for **Step 2a**.

- The conditions under which performance degrades → these become the raw material for **Step 2b**.

- How technology classes compare on those quantities → this feeds the technology comparison table.

Once review papers have established the relevant quantities, use datasheets and standards as a second layer to find specific performance numbers.

**Question 2 — What operating conditions are known to stress this function?**

From the literature, identify the environmental conditions, geometric edge cases, and operational states that limit performance → these become the worst-case scenario assumptions for **Step 2b**.

**Question 3 — What technology classes are used to provide this function?**

For each technology class identified, note:

- Its operating principle.

- Its typical performance envelope on the quantities identified in Question 1.

- Its known limitations under the stressing conditions identified in Question 2.

These become the candidate technology classes for the trade study in **Step 3**.

#### **2b. Document findings**

For each subsystem functional requirement, write a short structured passage covering:

1.  What physical quantities practitioners use to characterise this function, and why those quantities matter.

2.  What operating conditions are known to stress this function.

3.  What technology classes are used to provide this function, their operating principles, their typical performance ranges, and their known limitations under the worst-case conditions identified in point 2.

#### **2c. Create Pugh Matrix**

Distill the information in step 2b into a Pugh Matrix or any other template of your choice to illustrate comparison between identified technology classes.

**Step 3 - Derive Technical Parameters**

This is the analytical core of the deliverable. Using the domain knowledge built in Step 1, work through the following sub-steps for each subsystem functional requirement. Each sub-step populates specific columns in the Technical Requirements Table.

**3a. Identify the Governing Technical Parameter**

- **Column 0** — Record the system-level functional requirement that is the source for the subsystem-level requirement.

- **Column 1** — Record the subsystem-level functional requirement derived from it.

- **Column 2** — Identify the physical quantity whose drop below a threshold would constitute a violation of the subsystem functional requirement. Clearly name this quantity. If multiple parameters jointly govern the requirement, list all of them.

- **Column 3** — Provide a brief rationale explaining *why* this parameter governs the requirement — not merely what it is. For any non-obvious relationships, support the link using a credible source. Include citations where applicable.

**3b. Define the Worst-Case Scenario**

- **Column 4** — For each technical parameter identified in Step 2a, define the operating scenario that places the most demanding requirement on that parameter. Be explicit about all assumptions. Ensure the assumptions are sufficient to make the derived value in Column 6 defensible — the worst-case scenario is the direct justification for why the derived value is set at the level it is.

> It's a good practice to be explicit about all assumptions underlying the scenario.
>
> **Example — Localization Subsystem**
>
> Subsystem functional requirement: "*The localization subsystem shall maintain a bounded pose error where the nearest persistent vertical structure is up to 40 m away*."

- Governing parameter: Maximum detection range at 10% reflectivity.

- Why 10% reflectivity? Industry-standard worst-case surface (dark concrete, wet asphalt). Manufacturers use it as the benchmark for minimum usable range.

- Worst-case scenario: Outdoor operation in full sunlight, at maximum range, against a low-reflectivity surface.

- **Why this is worst-case**: Two stressing conditions coincide:

<!-- -->

- At maximum range → return signal is weakest (intensity falls with square of distance).

- In full sunlight → background photon noise is highest, making weak returns harder to detect above the noise floor.

#### **3c. Derive the Minimum Acceptable Value**

The following step produces results to be recorded in Column 5 (Derivation Method) and Column 6 (Derived Value) of the Technical Requirements Table.

1.  **Column 5 – Derivation Method** - Using the worst-case scenario defined in Step 2b, state the method by which the minimum acceptable value of the governing parameter is derived. Table 1.1 illustrates the various derivation methods you can use. The method must include:

    1.  The governing formula or analytical relationship being applied.

    2.  The assumed input values, linked explicitly to the worst-case scenario assumptions from Step 2b.

    3.  The computed result, showing how the inputs yield the minimum acceptable value.

2.  **Column 6 – Derived Value** - Record the numerical result of the derivation as the minimum value of the governing parameter that still satisfies the functional requirement under the worst-case scenario.

> **Ensure the derivation is fully explicit** — a reader should be able to reproduce the result from the information recorded in Columns 5 and 6 alone, without additional context.

Apply the following standard engineering methods as appropriate:

Table 1.1

| **Method** | **When to apply** | **What to document** |
|----|----|----|
| **Worst-Case Analysis** | Performance, geometric, and environmental specs | Worst-case scenario definition, formula, assumed values, computed result, margin applied |
| **Budget Allocation** | Shared performance budgets (latency, accuracy, power, mass) | System-level budget, each subsystem’s allocation, rationale for split |
| **Interface-Driven Derivation** | Output specs set by what a consuming subsystem requires | Consuming subsystem’s requirement, Physical I/O Diagram conduit, derived spec value |
| **Standards / Precedent Lookup** | Mature domain specs where standards apply | Source document, applicability conditions, any adjustments made and why |

#### 

#### **3d. Add an Engineering Margin**

The following step produces results to be recorded in Column 8 (Margin Applied) and Column 9 (Final Specified Value) of the Technical Requirements Table.

1.  **Column 7 – Margin Applied** - Apply an engineering margin to the derived value from Column 6 to account for:

    1.  Uncertainty in the worst-case assumptions made in Step 2b.

    2.  Manufacturing tolerances in the physical components.

    3.  Performance degradation over the system lifecycle.

| **Key Concept** | *A margin of 10–20% is standard practice in most engineering domains. Record both the margin factor applied and the rationale for its chosen magnitude — i.e., why that specific margin is appropriate given the sources of uncertainty relevant to this parameter.* |
|----|----|

2.  **Column 8 – Final Specified Value** - Record the final specified value, computed by applying the margin factor to the derived value from Column 6. This is the value that enters the formal requirements document.

**3e. Flag Open Items**

This step applies to any cell in the Technical Requirements Table that cannot yet be completed.

For any parameter that cannot yet be derived — whether due to missing stakeholder input, unavailable site measurements, or incomplete analysis — record an open item in the Column 8 that states:

- What specific information or analysis is needed to resolve the gap.

- Who is responsible for providing or completing it.

**Step 4 - Document the Trade Study**

#### **4a. Create the Trade Study Artifact** 

1.  Open Innoslate and go to **Database View**.

2.  Create a new **Artifact** entity. Give it a unique ID (e.g., TS.1) and a descriptive name.

3.  Upload the document including the literature review and Technical Requirements Table produced in 3a.

**4b. Link to Requirements**

1.  In the Artifact's relationships panel, add a **“satisfies”** relationship to each relevant upstream requirement that the Trade Study aims to satisfy.

2.  The derived requirements resulting from the Trade Study are to be “sourced by” the Trade Study.

3.  The derived requirements are also to be “traced from” the upstream requirements the Trade Study satisfies.

4.  If the literature review revealed a requirement that is not yet captured, add it to the requirements document first, then link it here.

**4c. Capture Issues and Decisions**

1.  If any technology class fails to meet the final specified value (Column 9), create a **Decision** or **Issue** entity in Innoslate.

2.  For any metric where data is insufficient or TBD, flag it as an open item following the instructions in Step 2e.

3.  In the entity's attributes, record: the justification, any assumptions made, and who is responsible for resolution.

4.  Link the entity to the trade study artifact using the <span class="mark">**“caused by”** relationship for Issue and **“enabled by”** relationship for Decision.</span>

**<span class="mark">4d. Define Selection Metrics</span>**

1.  For each subsystem requirement in the Technical Requirements Table, create a **Measure** class entity in Innoslate.

??? note "Sadaf · 2026-05-08"
    -technical requirements should be created manually in the SRD along with their associated measure entities
<!-- comment:18 -->


??? note "Sadaf · 2026-05-08"
    if the generated subsystem functional requirement is related to the technical requirement, add the technical requirement to the same functional requirement create traceability with upstream requirement (system) from stage 2  technical requirement in SRD (specified by) Measure
<!-- comment:17 -->


2.  Set the final specified value from Column 8 as the minimum threshold for that metric.

3.  Link each metric to the corresponding requirement using **“specified by”**.

**4e. Record the Decision**

1.  Create a **Decision** entity in Innoslate.

2.  Record: the recommended technology class, the rationale for selecting it, and the assumptions it depends on.

3.  Link the Decision to the trade study artifact using **“enabled by”**.

**Step 5 - Identify and Document Associated Risks**

Dam \[1\] defines risk as a *potential future event characterised by its probability of occurrence and consequence*. This step makes those risks explicit and traceable in Innoslate.

#### **5a. Identify Risks for the Recommended Technology Class**

For the recommended technology class, assess risks across the following categories:

- Performance risk — does the technology meet the final specified value under the worst-case scenario defined in Step 2b, or only under nominal conditions?

- COTS/GOTS dependency risk — could the specific product be discontinued, revised, or subject to export restrictions?

- Integration risk — does the technology require adaptors, drivers, or calibration procedures that could introduce latency or compatibility issues with adjacent subsystems?

- Environmental risk — does the technology's performance degrade in the actual operating environment (temperature, vibration, EMI, ingress)?

- Cost and schedule risk — does the technology have long lead times or high cost that could affect delivery? If so, is there a viable fallback option?

#### **5b. Create Risk Entities in Innoslate**

#### For each risk identified in Step 4a:

#### Go to **Database View** and create a new **Risk** entity.

#### Give it a unique ID and a concise name describing the risk event.

#### In the entity attributes, record:

#### **Description** — what the risk event is and why it could occur.

#### **Likelihood** — Low / Medium / High.

#### **Consequence** — Low / Medium / High.

#### **Assignee** — who is responsible for monitoring and mitigating it.

#### Link the Risk entity to the trade study artifact using the “**references”** relationship.

#### Link it to the affected requirement(s) using the **“caused by”** relationship.

#### 

#### **5c. Display Risks in a Risk Chart**

#### In Innoslate, open the **Diagrams View** and create a new **Risk Chart** diagram.

#### Add each Risk entity created in Step 4b to the chart.

#### **5d. Define Mitigation Strategies (Optional)**

For every risk rated Medium or above, define a mitigation strategy. Common approaches include:

- Identifying an alternative technology class as a fallback if the recommended class fails to deliver.

- Specifying accelerated environmental testing prior to integration.

- Requiring redundancy in the sensor or processing chain for high-consequence failure modes.

- Establishing interface contracts early to isolate COTS changes from the rest of the architecture.

For each mitigation:

1.  Create a **Decision** entity in Innoslate recording the chosen strategy, its rationale, and any assumptions.

2.  Link the Decision to its corresponding **Risk** entity using the “**resolves”** relationship, consistent with Dam's guidance in Chapter 7 (Figure 99).

## **6. Quality Checklist Before Submission**

Verify each of the following before submitting this deliverable:

|  | **Checklist Item** |
|----|----|
| ☐ | Every subsystem functional requirement from the FRD has at least one corresponding row in the Technical Requirements Table. |
| ☐ | Every governing technical parameter mapping includes a written rationale — not just the parameter name. |
| ☐ | Every derived spec value includes an explicit worst-case scenario definition with stated assumptions. |
| ☐ | Engineering margins have been applied and documented, with the margin factor justified. |
| ☐ | All open items are flagged with a description of what is needed and who is responsible — no blank cells. |
| ☐ | Every cell in the requirements table includes a source citation or analytical justification. |
| ☐ | The recommended technology class follows from the table; if it does not, the additional decision factors are explicitly stated. |
| ☐ | All risks rated Medium or above have a documented mitigation strategy. |
| ☐ | Trade study results and risks have been documented as an Innoslate Artifact. |
| ☐ | The customer (or their designated representative) has been informed of the recommended technology class and any risks rated High or Critical. |

## **6. References**

\[1\] Dam, S. H. Real MBSE: Model-Based Systems Engineering Using LML and Innoslate. — Primary source for the synthesis process, trade study methodology, COTS/GOTS risk identification, and functional analysis and allocation.

\[2\] Jackson, P. L. (2009). Getting Design Right: A Systems Approach. CRC Press. — Source for subsystem identification (Ch. 4), interface identification, and design structure matrix methods (Ch. 6).

\[3\] MIL-STD-499B (Draft). Systems Engineering. — Referenced in the MBSE textbook as the basis for trade study types associated with requirements, functional, and synthesis processes.

del 5 - subsystem tech reqs
