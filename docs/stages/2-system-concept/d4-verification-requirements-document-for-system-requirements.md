---
title: "Verification Requirements Document (for System Requirements)"
stage: "System Concept"
deliverable_id: stage2-d4
status: draft
last_reviewed: 2026-05-23
---

# Verification Requirements Document (for System Requirements)

## **Verification Requirements Document (for System Requirements)**

### **What this deliverable is**

This document defines how **system requirements will be verified**.

System verification requirements describe:

- **What evidence is needed** to prove the system requirement is satisfied

- **What verification method will be used** (test, inspection, analysis, demonstration, modeling & simulation)

Unlike stakeholder requirements, **system requirements are solution-dependent**.  
They are derived after trade studies and architectural design decisions.

Because of this:

- Most system requirements **must be verifiable**.

- Verification requirements help ensure the **designed solution can actually be validated** once implemented.

Not all system requirements need a separate verification requirement:

- **Straightforward, measurable requirements** may link directly to a test case.

- **Complex or derived technical requirements** should have explicit verification requirements defined first.

## **Why this deliverable is important**

This deliverable ensures that **the designed system can be objectively validated**.

It helps:

- Ensure system requirements are **testable and measurable  
  **

- Prevent ambiguity about **how the final system will be validated  
  **

- Enable structured **verification planning  
  **

- Ensure the **engineering design decisions are accountable  
  **

- Identify **metrics and technical performance measures (TPMs)** early

- Prepare the project for **system-level testing and validation  
  **

## **Guidelines**

### **Create a Verification Requirements Document**

Create a separate Requirements Document for system verification requirements.

1.  Navigate to **“Documents” view  
    **

2.  Create a new document

3.  Select **“Requirements Document”  
    **

Set:

Number: **“VR.2”  
** Name: **“System Verification Requirements”  
** Template: **“Blank Document”**

## **Identify Verification Requirements**

Use the **same format as the System Requirements document**.

Each verification requirement should clearly state:

- **what performance metric will be verified  
  **

- **how the system requirement will be evaluated  
  **

When writing verification requirements:

- Replace ambiguous wording such as:

  - sufficient

  - adequate

  - at least

  - minimal

  - efficient

- with **measurable values**.

- Convert qualitative requirements into **quantified technical criteria**.

Example:

If the system requirement states:

> The robot shall move efficiently across rough terrain.

A verification requirement should define measurable performance:

> The robot shall maintain a forward velocity of **≥ 0.5 m/s on terrain slopes up to 15°**.

A requirement typically becomes verifiable **only when measurable**.

These measurable quantities are often called:

- **Metrics  
  **

- **Technical Performance Measures (TPMs)  
  **

## **Trace Verification Requirements to Test Cases (Optional)**

??? note "Sadaf · 2026-05-15"
    System Req (verified by) Verification Req
<!-- comment:12 -->


??? note "Sadaf · 2026-05-07"
    what about tracing to system requirements?
<!-- comment:11 -->


A **Test Case** is a subclass of the **Action** class.

It is useful because it:

- Supports the **Innoslate Test Center  
  **

- Allows visualization using **Action Diagrams  
  **

- Helps plan verification **cost, schedule, and resources  
  **

For each verification requirement:

Create a **Test Case**.

Steps:

1.  On the left sidebar under **Relationships  
    **

2.  Use **“verified by”  
    **

3.  Create a new Test Case

Fill attributes:

Number: **TS.n**

Name: **Test Case Name**

Description: Description of the test

Set Up: Test preparation steps

Expected Result: Expected outcome

Status: **Not Run**

Save changes.

## **Review and Finalize**

Review the verification requirements with the **engineering team and domain experts**.

Record outcomes.

If design decisions are required:

Create **Decision entities**

Create relationship:

Verification Requirement → **enables → Decision**

## **Reporting Instructions**

1.  Download the Verification Requirements document from Innoslate as:

**Basic Document Output (DOCX)**

2.  Create a **traceability matrix between System Requirements and Verification Requirements  
    **

3.  Download the matrix as:

**Matrix Report (xlsx)**

4.  Convert the matrix to **PDF  
    **

5.  Merge:

- Verification Requirements document

- Traceability matrix

6.  Upload the **single merged document** on Canvas.

## **Student Checklist**

### **Document Setup**

☐ Created **VR.2 – System Verification Requirements** document (Blank template)  
☐ Format matches the **System Requirements document**

### **Verification Requirements**

☐ Every system requirement has a corresponding verification requirement (or direct test case)  
☐ Ambiguous wording replaced with measurable values  
☐ Performance metrics defined as **technical measures (TPMs)**

### **Traceability**

☐ Verification requirements linked to **System Requirements  
** ☐ Test cases created where appropriate  
☐ **verified by / verifies** relationships created

### **Review & Decisions**

☐ Reviewed with engineering team  
☐ Decisions recorded and linked to verification requirements using **enables**

Red Review Team Instructions

## ![](../../assets/images/image17.png){ style="width:5.38021in;height:2.58333in" }

##  **Red Team Review Instructions**

**Role: Adversarial Design Auditor**

You are not collaborators for this stage.  
You are independent reviewers whose job is to expose weaknesses in another team’s concept **before it reaches the client**.

Your marks depend on the quality of your criticism, not politeness and not whether you are “correct”.

Your responsibility:

> <u>Help prevent a team from building a system that fails in the real world.</u>

Do not redesign their system.  
Do not suggest improvements unless needed to explain a failure.  
Your job is to identify where their reasoning may break.

### **What You Will Receive**

From the assigned team you will see:

- Assumptions & design space

- Preliminary architectures

- Intended sensing / actuation / control approach

You are evaluating the *reasoning*, not presentation quality.

### **Your Deliverable** 

Submit a **document** titled:

**Top 5 Ways This Design Could Fail**

For each failure include:

1.  The hidden assumption being violated

2.  The scenario where failure occurs

3.  The mechanism of failure

4.  The observable consequence

Use this structure:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 25%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Hidden Assumption</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Failure Scenario</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Failure Mechanism</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Consequence</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### **What Counts as a Strong Critique**

You must include at least:

- one physics or scaling constraint

- one operational environment case

- one integration interaction

#### **Weak (low marks)**

Opinion or preference  
“Camera may not be accurate”  
“This seems complicated”

#### **Medium**

Scenario-based  
“Forklift may block view”

#### **Strong**

Constraint-based  
“Stopping distance exceeds sensing range at max speed”

#### **Excellent**

Falsifiable and measurable  
“At 1 m/s, braking distance is 1.2 m but detection range is 0.8 m → collision inevitable”

### 

### **Important Rules**

You are NOT penalized if the other team rejects your critique with good evidence.

You ARE penalized if:

- critiques are vague

- critiques are stylistic

- critiques only target presentation quality

### **What Not To Do**

- Do not propose a better design

- Do not help them fix it

- Do not debate socially

- Do not evaluate effort

You are auditing logic.

Your grade depends on:

- specificity of assumptions identified

- realism of failure scenario

- technical reasoning quality

- testability of claim

The goal is not to win an argument.

The goal is to reveal uncertainty before the system is built.

Stage 2 Overview Guidelines

## **System-Level Concept Design Stage (4 Weeks)**

**Weight: 12% total**

- Trade Studies and Risk Reduction: 8%

- System Requirements: 2%

- System Verification Requirements: 2%

### **Purpose of This Stage**

In this stage, your objective is to systematically explore the system design space and justify a concept choice using structured reasoning. You are expected to make alternatives explicit, compare them along relevant attributes, and select a concept because it reduces risk and uncertainty, not because it was the first idea or easiest to defend.

Concept selection follows three principles:

1.  **Enumerate before evaluating  
    ** Identify all *fundamentally different* system concepts before any scoring occurs.

2.  **Compare only along relevant attributes  
    ** Concepts are compared using attributes derived from stakeholder and system objectives. If an attribute does not distinguish between concepts, it should not influence the decision.

3.  **Use structure to guide discussion  
    ** The purpose of trade-study matrices is not numerical accuracy, but disciplined reasoning and traceable decisions.

Engineering failures frequently arise not from lack of effort but from premature commitment to an appealing solution followed by selective justification. Therefore, this stage evaluates the quality of reasoning used to arrive at a system concept rather than the apparent quality of the concept itself.

The activities in this stage are designed to encourage five specific forms of engineering behavior.

For more detail on this process you can refer to Peter L Jackson’s “Getting design right”’ following chapters:

1.  Chapter 4: Explore the Design Space (pg 103-128) to

    1.  Discover concepts relevant to the design problem at hand.

    2.  Combine the concepts and generate integrated solutions.

2.  Chapter 5: Optimize Design Choices (pg 131- 146) to

    1.  Identify the alternative design concepts;

    2.  Identify the relevant attributes (product objectives);

    3.  Perform an initial screening of alternatives;

    4.  Rate the alternatives in each attribute;

    5.  Weight the attributes;

    6.  Score and rank the alternatives; and

    7.  Select an alternative.

#### **Exploration Completeness**

Teams must demonstrate that the design space was explored before committing to a solution. Alternatives should be derived from system functions, constraints, and operating context rather than informal brainstorming. The submission should provide evidence that multiple fundamentally different approaches to performing the required functions were considered.

#### **Meaningful Alternatives**

Alternatives must differ in operating principle, architecture, or mechanism. Variations in parameters or components within the same mechanism do not constitute meaningful alternatives. The intent is to compare competing approaches rather than incremental modifications of a single idea.

#### **Justified Decision Rule**

The criteria used to compare alternatives must be derived from stakeholder and system needs and must be defined before selecting a concept. The comparison method should therefore exist independently of preference for any specific alternative.

#### **Falsification Effort**

Teams are expected to actively attempt to invalidate their own assumptions. Evidence of examining failure modes, constraints, unrealistic operating conditions, and external critique will be evaluated positively. Discovering weaknesses in a concept is considered progress rather than error.

#### **Risk-Reducing Convergence**

The purpose of concept selection is to reduce uncertainty in the system. The final concept should be justified in terms of elimination or reduction of major risks rather than numerical scoring alone.

<span class="mark">Changing a design in response to credible evidence will be rewarded. Defending an assumption without supporting evidence will be penalized.</span>

The central question addressed in this stage is:

*What system architecture should be built, and why does it reduce the most significant risks?*

### **Timeline Overview**

| **Week** | **Activity**                                 |
|----------|----------------------------------------------|
| Week 1   | Exploration of design space                  |
| Week 2   | Commitment to candidate concepts             |
| Week 3   | Red Team review                              |
| Week 4   | Evidence-based convergence and formalization |

### **Week 1 — Assumption Mapping and Design Space Exploration**

**Objective:** Establish understanding of the problem and possible solution mechanisms before committing to a concept.

**Submission: Assumption and Design Space Sheet**

The document must include:

1.  Core system functions

2.  At least three fundamentally different mechanisms for each major function

3.  Environmental and operational assumptions

4.  Unknowns that could invalidate a concept

No concept selection should occur at this stage. Evaluation will focus on breadth and relevance of exploration.

### **Week 2 — Preliminary Concepts (Commitment Phase)**

**Objective:** Establish candidate architectures and the method for evaluating them.

**Submission: Preliminary Concept Document**

The document must include:

- Two to three candidate system architectures

- Subsystem decomposition (sensing, actuation, control, computation, interaction)

- Decision criteria derived from stakeholder requirements

- Known risks and uncertainties

The comparison criteria must be defined before Red Team review. This submission represents commitment to an evaluation framework rather than a final decision.

### **Week 3 — Red Team Review**

**Objective:** Subject reasoning to adversarial evaluation.

Each team will receive critique from another team in the form of a document identifying major failure possibilities. Teams must analyze the critique but should not yet submit responses.

Evaluation in this stage will depend on how the critique is later addressed, not on the absence of critique.

### **Week 4 — Evidence-Driven Convergence and Formalization**

Teams refine and finalize the system concept using evidence.

#### **Submission 1: Attack–Response Table (Trade Study Evidence)**

| **Claim** | **Red Team Attack** | **Response** | **Evidence** | **Status** |
|-----------|---------------------|--------------|--------------|------------|

For each critique, the team must:

- Accept and modify the design, or

- Reject with justification, or

- Mark unresolved and bound the risk

Evidence may include calculations, references, experiments, or engineering reasoning.

The final concept must demonstrate reduction of major risks.

#### **Submission 2: Final Concept Selection Justification**

The document must clearly explain:

1.  The most critical threatening assumption

2.  Evidence that affected the decision

3.  Why the final architecture reduces risk relative to alternatives

### **System Requirements (2%)**

Create a System Requirements Document after finalizing the concept.

Requirements must:

- Describe system behavior rather than implementation

- Be testable

- Trace to stakeholder requirements

Traceability:  
Stakeholder Requirement → System Requirement

### **System Verification Requirements (2%)**

Create a Verification Requirements Document.

Each verification requirement must specify:

- Verification method (test, analysis, inspection, or demonstration)

- Measurable acceptance criteria

Traceability:  
System Requirement → Verification Requirement

### **Grading Principle**

Evaluation is based on the quality of reasoning demonstrated through exploration, evaluation criteria definition, response to critique, and risk-based convergence. Confidence without supporting evidence will receive low credit, while identification and correction of incorrect assumptions will receive high credit.

Red Team Attack Response

![](../../assets/images/image21.png){ style="width:5.18229in;height:2.58637in" }

**Red Team Attack Response**

**Goal:** Reduce uncertainty and strengthen your selected concept through structured critique and evidence-based responses.

**Deliverable:  
**Submit an **Attack–Response Table** that documents how your concept withstands critical scrutiny.

| **Claim** | **Red Team Attack** | **Your Response** | **Evidence** | **Status** |
|-----------|---------------------|-------------------|--------------|------------|

**Instructions:**

For every critique you must:

- Clearly state the **claim or assumption** being challenged.

- Describe the **red team attack**, identifying potential weaknesses, risks, or failure modes.

- Provide a **reasoned response** explaining how the concern is addressed, mitigated, or accepted.

- Support your response with **evidence**, such as calculations, simulations, references, experiments, or authoritative sources.

- Assign a **status** (e.g., Resolved, Partially Resolved, Open) indicating whether further work is required.

The purpose of this deliverable is not to defend the design at all costs, but to **expose and resolve critical uncertainties**. Claims that cannot be supported with evidence should remain open and inform future design decisions or risk mitigation plans.

- Accept and modify design

- Reject with justification

- Mark unresolved and propose test/calculation

Evidence may include:

- back-of-envelope calculations

- reference systems

- physics reasoning

- small experiments

- literature

Add about convergence of the idea

Operational Concept Description (OCD)

**Operational Concept Description (OCD)**

This document describes the operational concept for the proposed system. Its purpose is to explain, in clear and plain language, how stakeholders expect the system to operate within its intended environment. The document integrates the stakeholder needs, requirements, scenarios, and verification planning developed during the requirements analysis phase.

This document shall remain solution-agnostic. It shall describe **what the system must accomplish operationally**, not how it will be implemented. Architectural decisions, hardware selections, software design, and technical solutions are outside the scope of this document and will be addressed during later development phases.

1.0 Introduction

1.1 Background

*Summarize the current situation that motivates the development of the system. Describe the operational challenges, limitations, or gaps in existing processes and explain the rationale for pursuing a new or improved solution. The discussion shall establish the context in which the system will operate and clarify the mission objectives that the system is intended to support.*

*Key stakeholder needs that justify the project may be summarized here in narrative form. Detailed lists of needs shall be provided in **Appendix A**.*

1.2 Assumptions and Constraints

*State the major assumptions and constraints that influence the concept of operations. These may include environmental limitations, policy or regulatory constraints, schedule considerations, resource limitations, or dependencies on external systems.*

*Only high-level assumptions and constraints shall be described; the complete list shall be provided in **Appendix B**.*

2.0 Stakeholders and Operational Actors

*Identify and describe the stakeholders, users, operators, and external entities that interact with the system. For each major actor, explain the role they play, their responsibilities, and the nature of their interaction with the system.*

*Descriptions shall focus on behavior and interaction rather than internal design. The intent is to clarify who uses the system, who is affected by it, and what each party expects from it.*

*The detailed stakeholder list shall be included in **Appendix C**.*

3.0 Operational Overview

*Provide a high-level narrative description of how the system is expected to function during typical use. The description shall explain, from an operational perspective, how the system is initiated, how it performs its mission, how stakeholders interact with it, and what outcomes are produced.*

*The overview shall be written as a coherent story of use and shall avoid reference to specific technologies, components, algorithms, or architectural decisions. The goal is to communicate operational behavior rather than implementation details.*

3.1 System Context Diagram

*Present a context diagram that defines the system boundary and illustrates the external entities that interact with the system. The diagram shall identify major actors and the high-level information, material, or control flows exchanged with the system. The purpose of the diagram is to clarify the operational environment and scope of the system. The diagram shall remain implementation-agnostic and shall not depict internal subsystems or architectural components.*

4.0 Physical and Environmental Context

*Describe the physical environment in which the system is expected to operate. The discussion shall address relevant environmental conditions such as lighting, weather, terrain, temperature, indoor or outdoor conditions, and the presence of people or other equipment.*

*The description shall indicate whether the system must operate normally, operate with degraded performance, or merely survive under these conditions. The intent is to capture environmental expectations that influence system behavior and requirements.*

5.0 Operational Scenarios

*Present representative operational scenarios that illustrate how the system behaves in realistic situations. Scenarios shall include both nominal conditions, in which the system operates as intended, and off-nominal or abnormal conditions, in which disturbances, failures, or unexpected events occur.*

*Each scenario shall describe the initiating conditions, the sequence of events, the interactions among actors and the system, and the expected outcomes. Scenarios shall be written narratively and shall reference the corresponding use cases or action diagrams developed during requirements analysis.*

*Implementation details shall not be included. The purpose of these scenarios is to demonstrate system behavior and validate that stakeholder needs are addressed across a range of operational contexts.*

*All detailed scenarios and diagrams shall be provided in **Appendix D**.*

6.0 Verification Methods

*Describe, at a high level, how the operational behaviors described in this document are expected to be verified and validated. The intent of this section is to summarize the overall verification approach rather than to define specific tests or procedures.*

*Detailed stakeholder and verification requirements shall be provided in **Appendix E** and **F** respectively.*

7.0 Risks and Open Issues

*Identify significant risks, uncertainties, or unresolved issues that may affect successful system operation. These may include technical challenges, environmental uncertainties, safety concerns, or operational limitations.*

*Each risk or issue shall be briefly described along with its potential impact. The purpose of this section is to encourage early awareness of concerns that may influence requirements or future design decisions.*

*8.0 Candidate System Concepts*

*This section shall describe the different system concepts considered during the design process. Each candidate concept should be described briefly along with its key characteristics.*

*The purpose of this section is to demonstrate that multiple solution approaches were explored before selecting a preferred concept.*

*9.0 Trade Study Results*

*This section shall summarize the evaluation of candidate concepts. Students should describe the criteria used to compare alternatives and explain the reasoning used to evaluate the options.*

*Detailed trade study matrices and supporting analysis shall be provided in Appendix G.*

*10.0 Selected System Concept*

*This section shall describe the selected system concept and explain why it was chosen over the alternatives. The explanation should reference the evaluation criteria and trade study results.*

*The description should focus on the conceptual structure of the system rather than detailed engineering design.*

11.0 Risks

*Identify significant risks, uncertainties, or unresolved issues that may affect the chosen design concept. These may include technical challenges, environmental uncertainties, safety concerns, or operational limitations.*

11.0 Appendices

The appendices contain the detailed artifacts developed during requirements analysis. These materials are referenced throughout the document but are not repeated in the main narrative to avoid duplication.

**Appendix A – User Needs  
Appendix B – Assumptions and Constraints**

**Appendix C – Stakeholder List  
Appendix D – Operational Scenarios and Action Diagrams  
Appendix E – Stakeholder Requirements**

**Appendix F – Verification Requirements**

**Appendix G — Trade Study Tables**

**Appendix H — System Architecture Diagrams**

**Appendix I — Concept Evaluation Matrices**

**Appendix J — System Requirements**

**Appendix K — Verification Requirements**

overview - stage 3

**Initial System Architecture**

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

### 

### **1.3 The Three Diagram Products**

Initial System Architecture at the subsystem decomposition level produces three distinct but concordant diagram types, all of which are automatically linked in Innoslate through the concordance principle:

#### **Granular Action Diagrams**

Each scenario produces its own Action Diagram decomposed at least two levels below each identified subsystem. Actions in these diagrams directly become the functional requirements in the FRD. The textbook is explicit: *"Note that all the actions in Figure 64 represent the functional requirements for the rover. Here is how we derive the requirements for the different components of our system"* (Ch. 5). Resources (people, data stores, physical assets) are modelled as hexagram nodes within the Action Diagram to constrain performance during simulation.

#### **Physical I/O Diagram**

The Physical I/O Diagram is the integrating artefact between the functional and physical models. As the textbook states, it *"provides a mechanism for linking these functional and physical models together into a single, integrated model of the system"* (Ch. 6). It is constructed by connecting Asset nodes through Conduits, where each Conduit creation dialog simultaneously defines the Input/Output entity, the generating Action, and the receiving Action — automatically building both functional and physical relationships in a single modelling step.

#### **Asset Diagram**

The Asset Diagram is the physical view of the system, showing subsystems as boxes and Conduits as the interfaces between them. It is generated directly from the Physical I/O Diagram through Innoslate's concordance. Per MO Step 8, subsystems are derived from the functional behaviour description as Asset class entities. The Asset Diagram also serves as the entry point for generating the FRD: *"Open the Asset Diagram. Use the wrench at the top-right to select Generate SRD"* (ASEPD Deliverables guidance, drawing directly on the textbook process).

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
<p>The textbook draws an important distinction that students frequently conflate: <em>"This kind of time is not to be confused with schedule. Schedule is the time we need to build the system. Timing is a performance metric that indicates how long the system will take to transform inputs to outputs"</em> (Ch. 5). DES produces timing performance data; the project plan (Sub-Stage 4) addresses schedule.</p></th>
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

For example: say you have to design a toy car powered by a shaken soft drink bottle. We can assume the car as point mass, and the forces acting on it would be thrust (from the soda bottle, gravity, wind resistance, wheel friction, etc) . You can use kinematic equations and Newton's laws of motion to figure out how fast the car will go for varying soda bottle sizes. Then for each bottle size you can make a rough sketch to see how big your car should be to accommodate varying soda bottle sizes. Then depending on your user’s needs you can make a selection on specifications of the car.

### **2.4 What Simulation Produces for the Architecture**

The outputs of these feed directly into the downstream sub-stages of Initial System Architecture:

- **Performance requirements quantification:** Simulation-derived timing distributions become the numerical thresholds in the FRD's System Capability Requirements (Section 3.2) and System Quality Factors (Section 3.11). The textbook confirms: *"the simulation helps us determine what the ultimate requirements set should be"* (Ch. 7).

- **Trade study inputs:** Distributions over O2 extraction rates, resource consumption, and scenario timing provide the quantitative basis for trade studies in Sub-Stage 3.

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

### **5.3 Project Plan**

The project plan is built from the WBS, which the textbook derives directly from the SE process steps. Systems Engineering (WBS 1) is decomposed into Requirements Analysis (WBS 1.1), Functional Analysis (WBS 1.2), and so on, with each step in the process becoming a WBS element with an associated duration and resource estimate. Labour costs are estimated from the duration and staffing level of each step; material costs from the BOM. The textbook notes: *"both have the goal of minimising the cost and schedule, while maximising the performance to an agreed upon threshold"* (Ch. 2).

Risk mitigation tasks must be included in the schedule explicitly, as the textbook states: *"these become tasks in the schedule chart and should be dealt with like any \[other task\]"* (Ch. 2). This connects the risk register — updated continuously throughout Initial System Architecture — directly to the project plan.

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

refined del 1 + 2

**Subsystem Identification**

Pre-requisite to Deliverables 1 & 2 - Stage Synthesis

## **1. What This Is**

By this stage in the process, a set of integrated design concepts has been created. Before moving into concept selection, it is useful to organise what you have built so far.

The appropriate step at this stage is to **identify and label the subsystems of the product**.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>What is a Subsystem?</strong></p>
<p>A subsystem is a collection of elements of a system that has an identifiable function of its own.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If subsystems are identified too early in the design process, the team becomes trapped into thinking about the design problem using only the first design concept.

Now that a number of very different integrated design concepts have been generated, that concern no longer applies. Think of this as surfacing after a deep-dive: you have just completed a dive that produced detailed integrated concepts, and you now rise back up and organize all of the detail into a smaller number abstract, named groups.

## **2. Why This Matters**

- Going through this process **forces you to look at every component and ask: what job does this actually do?** That functional thinking often reveals things you missed — components that serve the same function in different concepts, or functions that nobody has designed for yet.

- You may discover a function during this step that none of your current concepts addresses. That is a signal to go back and expand your concept generation before continuing.

## **3.** **Step-by-Step Instructions**

??? note "Sadaf · 2026-05-21"
    Look at all the deliverables in this stage for missing reporting instructions for Canvas.
<!-- comment:13 -->


??? note "Sadaf · 2026-05-08"
    future iteration: no instructions given to create relationship between system and subsystem requirements
<!-- comment:21 -->


### **Step 1 - Collect Functions and Components**

Create an unordered list of every function and component that has appeared in the integrated concept diagrams. Include existing and legacy components, because these represent external elements you may want to interface with or subsume into the design. Each item should occupy its own cell in a spreadsheet so it can be moved freely. Figure 1 in Appendix shows a toy catapult example.

***Note:** You do not need to "own" a product to include it in your design. Incorporating COTS/GOTS or another team's development is common, but always flag the dependency risk: you do not control their development schedule, and even mature products can change unexpectedly. These dependencies are inputs to later risk analysis.*

### **Step 2 - Organize Functions and Components into Subsystems**

Using the drag-and-drop affinity process:

1.  Parse the list and create a new column whenever a cell does not clearly belong to an existing column — that is, when it performs a distinctly different function.

2.  After all cells have been parsed, devise a column heading that captures the overall functionality of each column. These headings name the subsystems of the product.

3.  As a useful cross-check, examine each component and classify it by function rather than by the concept it came from. Components from different integrated concepts that serve the same function belong in the same subsystem column.

4.  Create Asset entities for all identified subsystems in Innoslate. Add attributes (mass, power, cost, etc.) as needed. If hardware-specific attributes are not appropriate for all entity types, consider creating a hardware Asset subclass rather than adding the attributes to the parent class.

Figure 2. in Appendix illustrates this with the toy catapult example.

***Note:** It is possible during this abstraction step to discover a function that was not addressed during concept generation. When this happens, expand the concept classification tree to explore that new functionality before proceeding. A common example: what first appeared to be a single "trigger" function may decompose into a detection sub-function and an actuation sub-function, each warranting separate treatment.*

**4. Appendix**

![](../../assets/images/image18.png){ style="width:2.69883in;height:2.6494in" }

Figure 1. Example of list of functions and components

![](../../assets/images/image9.png){ style="width:3.65278in;height:3.71919in" }

Figure 2. Subsystems for toy catapult example
