---
title: "Initial System Architecture — Stage Overview"
stage: "Stage Synthesis"
deliverable_id: stage3-overview
status: draft
last_reviewed: 2026-08-05
---

# Initial System Architecture

Stage Overview — Synthesis Phase of MBSE

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>What is Initial System Architecture?</strong></p>
<p>Initial System Architecture is the first major technical output of the Synthesis phase. It is the stage in which the functional model — built during Functional Analysis — is transformed into a physical design by identifying subsystems, allocating functions to those subsystems, verifying the design's feasibility through simulation, and producing the specifications that enable procurement or build decisions.</p>
<p>Dam describes the overall goal of Synthesis as a process that <em>"must transform [requirements and functional analysis] information into concrete designs"</em> (Ch. 6). Initial System Architecture is where that transformation begins in earnest.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **Position in the MBSE Lifecycle**

Initial System Architecture sits on the left-hand descent of the V-model, after Requirements Analysis and Functional Analysis & Allocation, and before the finalised System Architecture baseline. Dam places this work within three overlapping processes — Functional Analysis (Ch. 5), Solution Synthesis (Ch. 6), and Systems Analysis and Control (Ch. 7) — all executed concurrently in the Middle-Out approach.

| **Precondition** | Functional model (Action Diagrams) completed; scenarios defined; context diagram established. |
|----|----|
| **Stage output** | Subsystem Asset Diagram, Physical I/O Diagram, granular Action Diagrams, Functional Requirements Document (FRD), Verification Requirements Document, trade study results, initial BOM, and project plan. |
| **Governing process** | Middle-Out Steps 7–15, Figures 51 and 74 (Dam, Real MBSE, 2020). |

## **Sub-Stage 1: Subsystem Decomposition and Interfaces**

| **MO 7–10** | **Derive subsystem behaviour, identify assets, prepare interface diagrams** |
|----|----|

### **1.1 From Scenarios to Integrated Behaviour Model**

The foundation of subsystem decomposition is the set of operational scenarios constructed during Functional Analysis. Dam recommends starting with the simplest scenario and building toward the most complex, producing Action Diagrams for each and reusing actions across scenarios. As the textbook states, the approach *"starts with the simplest scenario that the team can dream up, then the most difficult. These two scenarios form the bounds we want to work within"* (Ch. 5). The accumulated set of scenario Action Diagrams is then integrated into a single top-level behaviour model, with the most complex scenario (Scenario 9 in the Moonbase case study) becoming the *integrated behaviour model* for the system.

This integrated model is not a static document — the textbook explicitly states that it will be *"updated"* as verification data is gathered, calibrating predictions against reality throughout the lifecycle.

### **1.2 Action Diagram Decomposition Rules**

The textbook provides clear guidance on how deep to decompose. Decomposition continues until actions can be implemented by hardware, software, or people — the textbook's own definition of functional analysis:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Functional Analysis</strong></p>
<p><em>"The process of describing the transformation of inputs to outputs by decomposing the actions to a level where those actions can be implemented by hardware, software, or people."</em> — Dam, Real MBSE, Ch. 5</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Two additional stopping criteria follow from this definition:

- **COTS/GOTS identification:** Once a class of commercial or government off-the-shelf product can be identified to fulfil an action, decomposition should stop. Going further risks over-specifying a particular solution and constraining procurement.

- **Functional wording discipline:** If actions begin to describe implementation detail rather than capability, the model has gone too deep. The textbook advises: *"roll back up a level (or more) … make sure you use functional wording to avoid over specification"* (Ch. 6).

### **1.3 The Three Diagram Products**

Initial System Architecture at the subsystem decomposition level produces three distinct but concordant diagram types, all of which are automatically linked in Innoslate through the concordance principle:

#### **Granular Action Diagrams**

Each scenario produces its own Action Diagram decomposed at least two levels below each identified subsystem. Actions in these diagrams directly become the functional requirements in the FRD. The textbook is explicit: *"Note that all the actions in Figure 64 represent the functional requirements for the rover. Here is how we derive the requirements for the different components of our system"* (Ch. 5). Resources (people, data stores, physical assets) are modelled as hexagram nodes within the Action Diagram to constrain performance during simulation.

See [D1 · Low Level Action Diagram](d1-low-level-action-diagram.md) for the deliverable that produces these.

#### **Physical I/O Diagram**

The Physical I/O Diagram is the integrating artefact between the functional and physical models. As the textbook states, it *"provides a mechanism for linking these functional and physical models together into a single, integrated model of the system"* (Ch. 6). It is constructed by connecting Asset nodes through Conduits, where each Conduit creation dialog simultaneously defines the Input/Output entity, the generating Action, and the receiving Action — automatically building both functional and physical relationships in a single modelling step.

#### **Asset Diagram**

The Asset Diagram is the physical view of the system, showing subsystems as boxes and Conduits as the interfaces between them. It is generated directly from the Physical I/O Diagram through Innoslate's concordance. Per MO Step 8, subsystems are derived from the functional behaviour description as Asset class entities. The Asset Diagram also serves as the entry point for generating the FRD: *"Open the Asset Diagram. Use the wrench at the top-right to select Generate SRD"* (ASEPD Deliverables guidance, drawing directly on the textbook process).

See [D2 · Physical I/O and Asset Diagram](d2-physical-i-o-and-asset-diagram.md) for the deliverable that produces both.

## **Sub-Stage 2: Analysis — Discrete Event, Monte Carlo Simulation, Kinematic, and many more!**

| **MO 12** | **Verify logic, derive performance characteristics, quantify risk** |
|----|----|

Simulation is the mechanism by which the functional model is proven feasible before any physical commitment is made. The textbook treats it not as an optional enhancement but as an integral step of Functional Analysis and Systems Analysis & Control. The textbook defines the goal plainly: *"Simulation provides a means for early verification of the process models and derivation of the performance requirements needed"* (Ch. 5). Two techniques are used in combination.

### **2.1 Discrete Event Simulation (DES)**

DES executes the Action Diagram as an ordered sequence of events over time. Because functional models are *"an ordered sequence of well-defined events"*, the technique maps directly onto the action diagram structure. The textbook describes what DES checks:

- Logic correctness — are there unresolved decision paths or deadlocks?

- Timing — how long does the system take to transform inputs to outputs end-to-end?

- Resource constraints — *"availability or lack of resources will constrain the system performance, often impacting timing"* (Ch. 5). Resources modelled as hexagram nodes in the Action Diagram feed directly into the DES.

- Failure modes — the simulation can track bottlenecks and resource exhaustion that would not be visible by inspection.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Why timing is not schedule</strong></p>
<p>The textbook draws an important distinction that students frequently conflate: <em>"This kind of time is not to be confused with schedule. Schedule is the time we need to build the system. Timing is a performance metric that indicates how long the system will take to transform inputs to outputs"</em> (Ch. 5). DES produces timing performance data; the project plan (Sub-Stage 5) addresses schedule.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### **2.2 Monte Carlo Simulation**

DES alone is deterministic given fixed input values. Real systems have uncertainty in durations, resource availability, and decision outcomes. Monte Carlo simulation addresses this by running the DES repeatedly, each time sampling from distributions of values rather than using fixed points:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Monte Carlo Simulation</strong></p>
<p><em>"Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. It is a technique used to understand the impact of risk and uncertainty in prediction and forecasting models."</em> — Dam, Real MBSE, Ch. 5, citing Investopedia</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

In practice, each Monte Carlo run picks a random seed from the distribution of each uncertain parameter — duration, capacity, latency, decision point probability — and executes the full DES. By repeating this hundreds or thousands of times, the simulation produces a distribution of outcomes rather than a single-point estimate. The textbook states:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>What Monte Carlo reveals</strong></p>
<p><em>"By repeating this approach a large number of times, we execute all (or at least most) of the possible paths and parameters for the system operation. As we explore these paths through the system model, we will likely run into problems and find that some paths do not work as expected. Perhaps we didn't account for resources running out, or have included a logic error, or some other problem. By detecting these problems early in the design process, we can eliminate them from occurring in the actual system."</em> — Dam, Real MBSE, Ch. 7</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### **2.3. Physics Simulation**

A Kinematic Simulation can be in CAD, Blender, any 3D or 2D visualization tool, a Python script, or even an excel sheet. The goal is to represent all objects (moving or static) as bluff bodies (approximate or generic shape bodies) and/or point masses (no geometry, only forces acting on the center of gravity)

- **Collisions** between different parts.

- **Calculate motion ranges** for different parts so that you can check sizes and make appropriate part/material choices.

- **Calculate speeds** of various components which you can use to find acceleration, and then force input required.

For example: say you have to design a toy car powered by a shaken soft drink bottle. We can assume the car as point mass, and the forces acting on it would be thrust (from the soda bottle, gravity, wind resistance, wheel friction, etc) . You can use kinematic equations and Newton's laws of motion to figure out how fast the car will go for varying soda bottle sizes. Then for each bottle size you can make a rough sketch to see how big your car should be to accommodate varying soda bottle sizes. Then depending on your user's needs you can make a selection on specifications of the car.

### **2.4 What Simulation Produces for the Architecture**

The outputs of these feed directly into the downstream sub-stages of Initial System Architecture:

- **Performance requirements quantification:** Simulation-derived timing distributions become the numerical thresholds in the FRD's System Capability Requirements (Section 3.2) and System Quality Factors (Section 3.11). The textbook confirms: *"the simulation helps us determine what the ultimate requirements set should be"* (Ch. 7).

- **Trade study inputs:** Distributions over O2 extraction rates, resource consumption, and scenario timing provide the quantitative basis for trade studies in Sub-Stage 4.

- **Risk quantification:** The probability dimension of the Monte Carlo output directly feeds the risk matrix — high-variance paths in the simulation correspond to high-risk design areas.

- **Verification requirements seed:** Performance metrics derived from simulation become the initial basis for the Verification Requirements Document in Sub-Stage 3.

| **DES timing & resource analysis** | **Monte Carlo performance distributions** | **Simulation-derived performance thresholds** |
|----|----|----|

## **Sub-Stage 3: Functional Allocation and the Functional Requirements Document**

| **MO 8 / Fig. 74 Step 3** | **Allocate actions to assets; generate the FRD** |
|----|----|

### **3.1 Functional Allocation**

Functional allocation is the bridge between the logical architecture (Action Diagrams) and the physical architecture (Asset Diagram). The textbook's Figure 74, Step 3 defines it precisely: *"we relate the actions to the assets and the input/outputs to the propagation mechanisms"* (Ch. 6). This relationship is the *Allocate* relation in LML, and it provides the traceability needed to make the architecture modular — if an asset changes, the engineer can immediately see which actions are affected.

The textbook advises that the best packaging of actions into assets minimises interface requirements between them: *"You can determine best ways to package actions into assets to minimise the interface requirements (i.e. input/output) between assets"* (Ch. 5). This is not a purely mechanical mapping — it is a design decision with architectural consequences.

### **3.2 The Functional Requirements Document (FRD)**

The FRD is the primary document product of the allocation step. The textbook identifies it explicitly as an output of the Synthesis process: *"Another interesting product from this process is the Functional Requirements Document (FRD). The FRD provides a functional (including performance) specification for each of the component assets of the system"* (Ch. 6).

The FRD serves two simultaneous purposes:

- **Technical:** It provides testable, asset-grouped functional and performance requirements that are traceable to the actions in the model.

- **Programmatic:** By grouping requirements by asset, the FRD makes the build-vs-buy decision tractable. As the textbook states: *"you can then go out with a competitive procurement for those assets, since not only are the actions (capabilities) of the assets part of this document, they also contain a description of the links between assets. Now the programmatic decision of build or buy becomes much easier"* (Ch. 6).

See [D3 · Functional Requirements Document (FRD)](d3-functional-requirements-document-frd.md) for the deliverable itself.

#### **What Innoslate Auto-Generates vs. What Must Be Added**

Innoslate generates the FRD from the Asset Diagram, but only captures what is explicitly in the model. The capability requirements (FRD Section 3.2) and partial interface requirements (Sections 3.3–3.5) are auto-populated from allocated actions and named I/O flows. Non-functional, safety, security, and quality requirements — Sections 3.7, 3.8, and 3.11 — must be manually authored from engineering judgement, threat modelling, and applicable standards. Performance thresholds from the simulation (Sub-Stage 2) must also be manually added to the auto-generated capability statements.

### **3.3 Verification Requirements Document**

The Verification Requirements Document is generated concurrently with the FRD. The textbook calls this a best practice: *"We recommend developing the verification requirements at the same time as the \[system\] requirements so that you don't get backlogged"* (Ch. 4). Each functional requirement is traced to one or more verification requirements, which are in turn traced to test cases in Innoslate's Test Center. Verification methods — analysis, demonstration, inspection, modelling and simulation, or test — are assigned using Innoslate labels.

The textbook emphasises the quantification imperative: requirements only become verifiable when they can be quantified. *"We often call a quantifiable requirement a metric or technical performance measure (TPM)"* (Ch. 4). The simulation-derived performance thresholds from Sub-Stage 2 are the primary source for these TPMs.

| **Functional Requirements Document (FRD)** | **Verification Requirements Document** | **Allocated Asset Diagram** |
|----|----|----|

## **Sub-Stage 4: Derive Technical Specification — Trade Studies and Subsystem Requirements**

| **MO 14–15 / Fig. 74 Steps 1–2** | **Identify options, conduct trade-offs, select assets** |
|----|----|

With the FRD established, the architecture team evaluates alternative implementations for each subsystem asset. The textbook dedicates Chapter 7 to this process under Systems Analysis and Control, rooted in MIL-STD-499B and framing trade studies as inseparable from the synthesis process: *"all through this process, you will perform \[trade-off analyses\]"* (Ch. 6, Figure 74 annotation).

### **4.1 Types of Trade Studies Conducted**

- **Requirements trade studies:** The most commonly skipped category. Requirements are often set by engineering judgement rather than analysis. A trade study against scenario characteristics (e.g., minimum O2 extraction rate across mission scenarios) determines whether a stated threshold is actually the right one. The textbook states: *"Conducting an explicit trade-off on requirements is crucial to optimisation and ensures that you have the right set of requirements"* (Ch. 7).

- **Asset selection trade studies:** When multiple COTS/GOTS or internally developed options exist for an asset, a formal trade study evaluates them against the scenario-derived selection criteria. The textbook warns against selecting the first candidate: *"Rarely is this a good idea in the beginning of a program. Too often people jump on the first solution and then find it was not the best option"* (Ch. 6).

- **Performance allocation trade studies:** System-level performance budgets (power, mass, bandwidth, timing) must be allocated to subsystems. The textbook provides an extended worked example on power allocation, showing that rigid per-subsystem budgets can significantly increase cost: *"Work with the program management to ensure that all contracts enable you to trade off between contractor performance goals"* (Ch. 6).

- **Technology insertion trade studies:** Emerging technologies that could reduce cost, schedule, or performance risk are evaluated. These may result in Pre-Planned Product Improvement (P3I) provisions in the architecture.

See [D4 · Trade Studies and Associated Risks](d4-trade-studies-and-associated-risks.md) for the technology-class trade study and [D7 · Trade Studies (Component Selection)](d7-trade-studies-and-associated-risks-component-selection.md) for the component-level one.

### **4.2 Subsystem Requirements**

The output of the trade studies, combined with the FRD, produces subsystem-level specifications. These specifications give design engineers the inputs they need for detailed design. The textbook frames this relationship precisely: *"the overall design and analysis phase process results in a set of requirements for the next level of decomposition. We sometimes call these specifications, in an attempt to distinguish them from the originating requirements set. So, you might say one person's set of specifications is the next decomposition level's set of requirements"* (Ch. 4).

Each subsystem requirement must satisfy the standard quality criteria carried throughout the textbook: clear, complete, consistent, correct, design-independent, feasible, traceable, and verifiable.

| **Trade Study Reports (with decisions & rationale)** | **Risk register updates** | **Subsystem specifications** |
|----|----|----|

## **Sub-Stage 5: Analysis of Cost, Performance, Schedule, and Risk**

| **Ch. 6 + Ch. 3** | **BOM, design analysis, project plan, and risk register** |
|----|----|

The textbook's governing theme — *"optimizing cost, schedule, and performance, while mitigating risk"* — is not a post-synthesis activity. It is a concurrent obligation throughout Initial System Architecture. Chapter 6 devotes a full section to this under the heading *Cost is an Engineering Problem*, making explicit that program management cannot perform this work without engineering inputs.

### **5.1 Initial Bill of Materials (BOM)**

The BOM is the material-cost counterpart to the labour cost estimate. As the textbook states: *"you need to give them the information they need to do the cost right configuration of the software or other materials. In either case, the contracts personnel will go out for quotes on the BOM, so they need that draft as soon as possible"* (Ch. 6). The BOM is directly derived from the asset selection decisions made in the trade studies — each selected asset (COTS, GOTS, or new development) becomes a BOM line item.

COTS/GOTS lifecycle costs must be included, not just acquisition costs. The textbook specifically warns: *"the cost of continued maintenance … must be built into your trade-off analysis as part of asset selection. Not including this information in the original design decision can cause you to overly favour a COTS/GOTS solution, thus significantly increasing overall project cost"* (Ch. 6).

### **5.2 Design Analysis Report**

The Design Analysis Report captures the results of any domain-specific analyses — structural, thermal, electromagnetic, fluid dynamics — that characterise how the selected physical architecture will perform under operational conditions. In the textbook's framework these analyses are conducted by design engineers using specialist tools, with the results fed back to the systems engineering simulation in Innoslate. The textbook refers to this as *"vertical integration"*, where: *"the specific outputs from each \[design engineering\] tool \[identify\] how they affect the decision-making process at the higher levels"* (Ch. 7). The Design Analysis Report records the simulation inputs provided to the specialist tools, the results obtained, and the decisions made as a consequence.

See [D8 · Design Analysis Report and Initial Bill-of-Materials (BOM)](d8-design-analysis-report-and-initial-bill-of-materials-bom.md).

### **5.3 Project Plan**

The project plan is built from the WBS, which the textbook derives directly from the SE process steps. Systems Engineering (WBS 1) is decomposed into Requirements Analysis (WBS 1.1), Functional Analysis (WBS 1.2), and so on, with each step in the process becoming a WBS element with an associated duration and resource estimate. Labour costs are estimated from the duration and staffing level of each step; material costs from the BOM. The textbook notes: *"both have the goal of minimising the cost and schedule, while maximising the performance to an agreed upon threshold"* (Ch. 2).

Risk mitigation tasks must be included in the schedule explicitly, as the textbook states: *"these become tasks in the schedule chart and should be dealt with like any \[other task\]"* (Ch. 2). This connects the risk register — updated continuously throughout Initial System Architecture — directly to the project plan.

See [D9 · Level 1 and Level 2 Planning](d9-level-1-and-level-2-planning.md).

| **Initial Bill of Materials (BOM)** | **Design Analysis Report** | **Project Plan (WBS, schedule, cost estimate)** | **Updated Risk Register** |
|----|----|----|----|

## **Summary: Initial System Architecture at a Glance**

| **Sub-Stage** | **What Happens** | **Textbook Source** | **Key Deliverables** |
|----|----|----|----|
| **1. Subsystem Decomposition & Interfaces** | Scenarios → granular Action Diagrams → Physical I/O Diagram → Asset Diagram. Actions decomposed until hardware/software/people can implement them. | *Ch. 5, Fig. 51, MO Steps 7–10* | Action Diagrams, Physical I/O Diagram, Asset Diagram |
| **2. Dynamic Analysis (Simulation)** | DES verifies logic and timing. Monte Carlo propagates uncertainty through distributions, producing performance ranges and revealing failure paths. | *Ch. 5 (intro); Ch. 7, MO Step 12* | Performance distributions, timing data, simulation-derived TPMs |
| **3. Functional Allocation & FRD** | Actions allocated to assets (Allocate relation). FRD and Verification Requirements Document generated from the Asset Diagram. | *Ch. 5 (Step 6); Ch. 6, Fig. 74 Step 3; Ch. 4* | FRD, Verification Requirements Document, Allocated Asset Diagram |
| **4. Technical Specification & Trade Studies** | Options identified for each asset; trade studies select best option. Subsystem specifications derived from FRD + trade study outcomes. | *Ch. 6 (COTS/GOTS, cost); Ch. 7, MO Step 15* | Trade Study Reports, Subsystem Specifications, Risk Register |
| **5. Cost, Schedule & BOM Analysis** | WBS built from process steps; BOM from asset selection; project plan integrates schedule, cost, and risk mitigation tasks. | *Ch. 6 (Cost is an Engineering Problem); Ch. 3* | BOM, Design Analysis Report, Project Plan |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Concurrency — the most important architectural point</strong></p>
<p>None of these five sub-stages runs in a strict waterfall sequence. The Middle-Out process is explicitly iterative: simulation results revise requirements, trade study outcomes trigger re-decomposition, and risk findings update cost estimates. The textbook's Figure 74 shows feedback arrows at every step of Synthesis. A student who completes Sub-Stage 1 before starting Sub-Stage 2 has misunderstood the methodology. All five sub-stages execute in overlapping spirals, converging on the Final System Architecture at the SDR milestone.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **Source Reference**

| **Primary source** | Dam, Steven. Real MBSE: Optimizing Cost, Schedule, and Performance, While Mitigating Risk. SPEC Innovations, 2020. |
|----|----|
| **Chapters used** | Chapter 5 — Functional Analysis, Allocation, and Simulation; Chapter 6 — Synthesizing Solutions; Chapter 7 — Systems Analysis and Control. |
| **Standards cited** | MIL-STD-499B (Draft, 1994); EIA-632; INCOSE SE Handbook (4th ed., 2015, INCOSE-TP-2003-002-04). |
