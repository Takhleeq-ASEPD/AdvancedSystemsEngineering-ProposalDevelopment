---
title: "Verification Requirements Document (for System Requirements)"
stage: "System Concept"
deliverable_id: stage2-d4
status: draft
last_reviewed: 2026-08-05
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
