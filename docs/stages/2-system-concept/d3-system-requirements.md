---
title: "System Requirements"
stage: "System Concept"
deliverable_id: stage2-d3
status: draft
last_reviewed: 2026-09-29
---

# System Requirements

### **What this deliverable is**

The **System Requirements Document (SRD)** translates the selected system architecture and trade study decisions into **solution-dependent, verifiable system requirements**.

Unlike Stakeholder Requirements (which define *what* the system must achieve), System Requirements define:

- The performance the chosen solution must meet

- The interfaces it must support

- The constraints it must operate under

- The architectural decisions it must implement

These requirements reflect **how the selected system concept will satisfy stakeholder requirements**.

### **Why this deliverable is important**

- It bridges architecture and implementation.

- It formalizes trade study outcomes into enforceable requirements.

- It defines measurable system performance.

- It provides the basis for subsystem design and verification.

- It prevents architectural decisions from remaining informal or undocumented.

If trade studies are not captured in system requirements, decisions become assumptions.

### **Key Characteristics of System Requirements**

System Requirements must be:

- **Solution-dependent** (reflect chosen architecture/components)

- **Traceable to Stakeholder Requirements  
  **

- **Derived from trade studies and decisions  
  **

- **Quantified where applicable  
  **

- **Verifiable  
  **

- **Technically feasible  
  **

They should describe system-level behavior and performance, not detailed part specifications (those belong to subsystem/component requirements later).

### **Guidelines**

#### **1. Create System Requirements Document**

a\. Create a new Requirements Document using “Create Document” in Innoslate.  
b. Name the document: **SYS.1 – System Requirements Document  
** c. Create requirements using “New Requirement”  
d. Number them as: **SYS.1.N**

#### **2.** **Derive Requirements from Architecture & Trade Studies**

??? note "Sadaf · 2026-05-15"
    provide instructions on deriving system technical requirements. take inspiration from stage 3 technical requirements instructions.
<!-- comment:5 -->


System Requirements should come from:

- Approved Final System Architecture

- Trade Study outcomes

- Performance analyses

- Interface definitions

- Integration constraints

For each trade study decision:

- Identify the architectural implication

- Convert that implication into a requirement

- Ensure it is measurable and testable

#### **3. Create Required Relationships in Innoslate**

For each System Requirement:

- Create relationship **“traced from”** → System Req traced from Stakeholder Requirement

- Create relationship **“enabled by”** → Decision entity (if applicable)

- Create relationship **“sourced by”** → Trade Study (Artifact)

- Create relationship **“performs”** → Asset (performs) Action

This ensures:

Stakeholder Req → Trade Study → Decision → System Req → Architecture

#### **4. Include Performance & Interface Requirements**

System Requirements should now include:

- Quantitative performance values

- Interface definitions

- Throughput limits

- Timing constraints

- Environmental tolerances

- Reliability or availability targets (realistic ones)

Unlike stakeholder requirements, numbers are expected here.

#### **5. Identify System-Level Constraints**

Include:

- Regulatory constraints

- Physical constraints

- Environmental limits

- Budget-driven architectural constraints

- Integration constraints

These are no longer abstract — they must reflect the chosen concept.

#### **6. Address Critical Issues**

1.  (a. Identify unresolved risks or architectural limitations  
    (b. Create Issue entities if necessary  
    (c). Link requirements using “causes”  
    (d). Link Trade Studies using “resolves”  
    (e). Create Decision entity with rationale

2.  For a specific entity, if you haven’t decided on an empirical value yet (e.g the total compute power requirements for the MCU), create an issue against it.

System Requirements must reflect resolved architectural choices.

#### **7. Quality Check Using Innoslate Quality Checker**

Each System Requirement must be:

- Clear

- Complete

- Consistent

- Correct

- Feasible

- Traceable

- Verifiable

Unlike Stakeholder Requirements, they are **not required to be design-independent** — they are intentionally architecture-dependent.

### **Reporting Instructions**

1.  Download System Requirements document from Innoslate as “Basic Document Output (DOCX)”

2.  Create traceability matrix:

    - Stakeholder Requirements ↔ System Requirements

3.  Download matrix as “Matrix Report (xlsx)”

4.  Convert to PDF

5.  Merge:

    - System Requirements Document

    - Traceability Matrix

6.  Upload merged document

### **Student Checklist – System Requirements**

System Requirements must be:

✔ Clear and unambiguous  
✔ Singular (one idea per requirement)  
✔ Quantified where appropriate  
✔ Traceable to Stakeholder Requirements  
✔ Linked to trade studies and decisions  
✔ Feasible with chosen architecture  
✔ Verifiable  
✔ Consistent with final system architecture

### **Common Pitfalls to Avoid**

DO NOT:

- Write subsystem-level requirements too early

- Copy stakeholder requirements without refinement

- Include vague performance language (“fast”, “robust”)

- Leave trade study decisions undocumented

- Introduce new functionality not traced to stakeholders

- Use “may”, “should”, or ambiguous language

- Write multi-clause requirements

### **Balanced Modeling Guidance**

At System Requirements stage:

Be precise where:

- Performance drives architecture

- Interfaces impact integration

- Trade studies forced a measurable decision

Be restrained where:

- Details belong to subsystem/component design

- Part numbers are not yet finalized

- Implementation details do not affect system-level performance
