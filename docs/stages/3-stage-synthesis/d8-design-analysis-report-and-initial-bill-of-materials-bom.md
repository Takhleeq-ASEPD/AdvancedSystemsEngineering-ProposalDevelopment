---
title: "Design Analysis Report and Initial Bill-of-Materials (BOM)"
stage: "Stage Synthesis"
deliverable_id: stage3-d8
status: draft
last_reviewed: 2026-10-22
---

# Design Analysis Report and Initial Bill-of-Materials (BOM)

With specific components selected in Deliverable 7, the architecture is no longer abstract — it has real parts with real datasheet values. This deliverable asks the question: does the architecture as a whole actually work?

Component-level Pass/Fail checks from Deliverable 7 only confirm that individual parts meet individual requirements in isolation. *They do not confirm that the integrated system meets its top-level objectives* — budget, total mass, operational timing, power balance, or any other system-level constraint that only emerges when the parts are considered together.

This deliverable identifies which of those system-level analyses are necessary for your specific project and carries them out.

The goal is not an exhaustive engineering analysis. It is a targeted set of analyses sufficient to give your industry partner **reasonable confidence** that the chosen architecture is viable before committing further resources.

## **2. Why This Deliverable Matters**

- **Closes the gap between component selection and system performance.** A component can pass every individual criterion and still produce a system that misses a top-level objective. This deliverable is what catches that.

- **Converts requirements into quantified confidence.** Each analysis produces a number — a predicted mass, a predicted cycle time, a predicted power draw — that can be compared directly against the system requirement. That comparison is what makes the architecture defensible.

- **Identifies where margins are tight before they become problems.** An analysis that shows the power budget is 95% consumed early is far more valuable than discovering this during integration.

- **Grounds the preliminary BOM in reality.** The rough-cut BOM from Deliverable 7 gains credibility when supported by analyses showing the architecture is feasible at the system level.

## **3. Step-by-step Instructions**

**Step 1 — Identify Which Analyses Are Required**

Not every project needs the same analyses. The analyses required for your project are determined by your system-level requirements and the nature of the architecture. Work through the following:

1.  **Review the System-level Requirements document** that applies to the system as a whole rather than to an individual component — these are your system-level constraints. Common examples include:

- Total mass or volume budget

- Total power consumption vs. available supply

- End-to-end operational timing

- Total cost vs. project budget

- Data throughput or storage capacity across the architecture

- Any other quantity, quality, or timeliness metric identified during functional analysis

2.  For each system-level constraint, ask: **can this be verified by summing or combining the datasheet values already recorded in Deliverable 7, or does it require a more involved calculation or simulation?** This determines the method for each analysis:

| **Constraint type** | **Method** |
|----|----|
| Mass, volume, power (additive) | Budget Analysis |
| Operational timing, sequencing | Discrete event Simulation |
| Cost | BOM/ Cost Analysis |
| Performance under variation or uncertainty | Monte Carlo Simulation |
| Interface compatibility | Inspection against interface requirements in SRD Sections 3.3–3.5 |
| Physical or Behavioural | Domain-specific Analyses |

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>When is domain-specific analysis needed?</strong></th>
<th><ul>
<li><p>A requirement on electrical performance under switching conditions (e.g., voltage ripple, current transient, efficiency at load) that depends on component interaction rather than individual component ratings.</p></li>
<li><p>A requirement on motion, navigation, or spatial coverage for a robotic or autonomous system operating in a physical environment.</p></li>
<li><p>A requirement on thermal, structural, or fluid performance that depends on geometry and material properties.</p></li>
<li><p>A requirement on control system stability, step response, or bandwidth.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  **Create an analysis plan table** listing: the stakeholder requirement, the system-level requirement, the analysis method, and the team member responsible.

> *This table becomes the opening section of your Design Analysis Report.*

**Step 2 — Conduct Analyses**

Use the list of analyses created in Step 2 and follow the guidelines below respectively:

**1. Budget Analysis**

For constraints that are additive — mass, power, cost, volume — conduct a budget rollup:

1.  For each subsystem, **sum the datasheet values of all selected components** recorded in Deliverable 7 for the relevant parameter (e.g., mass in grams, quiescent current in mA).

2.  **Add estimated values for non-component contributions**: structural elements, wiring harness, connectors, enclosures, and any other items not yet selected. Use estimates with explicitly stated assumptions.

3.  **Apply an engineering margin** to the total.

> The margin must be justified based on the maturity of the design:

- Early-stage architecture (as here): 20–30% is appropriate for mass and power.

- Cost estimates at this stage typically carry a higher uncertainty — document the confidence level explicitly. Imported components should have a safety factor of 2 and locally purchased components should have a safety factor of 1.3.

4.  **Record the margined total and the requirement value.**

**2. Operational Timing Analysis**

There are two simulation methods available in Innoslate — Discrete Event Simulation and Monte Carlo Simulation — and both should be applied in sequence.

1.  **Open Action Diagram.**

2.  For every leaf-level action (actions with no children), **open the entity and assign a duration**.

> *Note: At this stage, use a triangular distribution (minimum, most likely, maximum) rather than a single value to reflect real uncertainty. In Innoslate, distributions are set by selecting the duration field and replacing the fixed value with the distribution parameters.*

3.  **Review and create relevant Resource entities in the diagram** and attach them to the actions using the “uses” relationship. This will allow the simulator to detect bottlenecks automatically.

4.  **Run Discrete Event Simulation**.

    1.  In the Action Diagram, **click the Simulate dropdown** on the toolbar and **select Discrete Event**.

    2.  **Press Play**.

> *Innoslate will step through every action in the diagram, following the branching and looping logic specified by your action constructs (sequential, parallel, decision, loop, synchronization).*

3.  **Add the Action Trace 3D panel to the simulation view** to observe all levels of decomposition executing in real time.

> *This view reveals whether the logical flow is correct and whether any actions are waiting unexpectedly for resources or inputs.*

4.  **Add the Total Time panels**.

> *These display running totals as the simulation progresses.*

5.  **Record the total elapsed time** and compare it against the system timing requirement.

6.  **Identify any actions that are blocked** (waited for a resource or input) — these are candidate bottlenecks.

7.  **Create an Issue entity** in Innoslate for each bottleneck, link it to the affected requirement using “caused by”.

8.  **Identify the critical path** — the sequence of actions whose durations sum to the minimum possible scenario time.

> *Actions on the critical path are where timing risk is concentrated. Any reduction in their duration directly improves the system's end-to-end performance.*

9.  **Export the discrete event results** to Excel using the available report export for documentation.

<!-- -->

5.  **Run Monte Carlo Simulation**

    1.  From the Action Diagram, **open the Simulate dropdown** and **select Monte Carlo.**

    2.  **Set the number of iterations.**

> *At this stage of design confidence, 300–1,000 iterations is sufficient to produce stable histograms; use a higher count (1,000+) if any individual action's duration range is very wide or if timing is close to the requirement boundary.*

3.  **Press Play** and allow the simulator to complete all iterations.

4.  **Review the outputs**:

    1.  The Time Bar Chart (histogram) shows the distribution of total scenario durations across all iterations. Read off the mean, the standard deviation, and the percentile at which the scenario duration exceeds the system requirement — this is the probability of a timing failure.

    2.  The Cost histogram shows the equivalent distribution for total cost.

    3.  The Resource panel shows how resource utilization varied across iterations, revealing whether any resource was consistently at capacity.

5.  **Export the Monte Carlo results** as a document to be inserted in the Design Report.

**3. Cost Analysis**

1.  Using the BOM template provided, compile all selected components into a single Bill of Materials. Each component occupies one numbered row. **Fill in the columns**.

2.  **Sum all rows** to produce the Total Estimated Project Cost.

3.  **Record this value** alongside the project cost constraint or industry partner budget, and compute the remaining margin.

**4. Domain-specific Analyses**

##### **Select the appropriate simulation tool for your domain**. 

- For electronics and control systems related projects, use **MATLAB/Simulink** with the **Simscape Electrical toolbox** or **Control System Toolbox**, respectively.

- For autonomous systems based projects, use **Gazebo** in combination with a **ROS (Robot Operating System)** control stack.

- For structural, thermal, or fluid analyses, use **finite element analysis (FEA)** tools such as ANSYS, Abaqus, or open-source alternatives such as FEniCS or OpenFOAM, depending on the domain.

##### **Build the simulation model using the selected tool,** parameterized with the values extracted in Step 3, and run the simulation under the operating conditions defined by the operational scenario. 

##### **Capture the key output metrics, plots, or data files** — for example, peak-to-peak ripple voltage, efficiency at full load, trajectory tracking error, settling time, maximum stress — and compare each metric directly against the relevant system-level requirement.

**Step 3 — Assess Margins**

Once all analyses are complete:

1.  For every analysis that results in a computed margin, **classify each margin**:

    - **Green:** margin ≥ 20% — comfortable at this design stage

    - **Yellow:** margin 5–20% — requires monitoring; may need design adjustment

    - **Red:** margin \< 5% or negative — immediate attention required; flag as Issue entity in Innoslate

2.  For any Red or Yellow margin, **identify the primary driver** (which component or subsystem contributes most to the problem) **and document a potential resolution path.**

**Step 4 — Document in Innoslate and Produce the Report**

1.  **Update the relevant Measure entities** in Innoslate with the predicted system-level values from each analysis.

> *These are the same Measure entities updated in Deliverable 7 — add the system-level rollup value alongside the component-level datasheet value.*

2.  **Add results from the analyses** to the Design Report.

> The written report should contain:

- Analysis plan table (from Step 1)

- A margin summary table covering all analyses

> *Note: Feel free to organize your report and its analyses in whatever structure you find most appropriate.*

3.  **Create a new Artifact entity** (e.g., DAR.1) for the Design Analysis Report. Upload the completed report and link it to any trade studies performed while making design choices in Stage 2 using "related to." Apply the Metadata label **Analysis** to this Artifact, so analysis artifacts can be filtered as a group.

4.  For any Issue entity created during this deliverable, link it to the affected requirement using "caused by" and to the analysis artifact using “references."

del 9 - project timeline
