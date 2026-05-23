---
title: "Narrative Description of Functional Concept Fragments"
stage: "System Concept"
deliverable_id: stage2-d2
status: draft
last_reviewed: 2026-05-23
---

# Narrative Description of Functional Concept Fragments

## **Narrative Description of Functional Concept Fragments**

In addition to matrix-based comparison, all design alternatives must be supported by a **concise, well-referenced narrative description**. Matrices summarize trade-offs; they do not, by themselves, justify the inclusion of an alternative in the design space.

A **functional concept fragment** is a partial design concept that describes **one plausible way to realize a specific system function**, independent of the complete system architecture. Functional concept fragments are later combined to form integrated system concepts.

Each option appearing in any design-space table or comparison matrix must be traceable to a corresponding functional concept fragment.

#### **Required Content**

For each retained concept fragment, the following shall be included:

1.  **Mechanism Overview  
    ** A clear description of how the function is achieved, including the sequence of actions, transformations, or information flow involved. The emphasis shall be on *how the mechanism works*, not on why it is chosen.

2.  **Illustrative Material  
    ** Diagrams, sketches, block diagrams, or annotated figures that clarify operation and interfaces. These need not be detailed designs but must accurately convey functional behavior.

3.  **Technical Basis and References  
    ** Citations to relevant research papers, textbooks, standards, patents, or existing systems that demonstrate the mechanism is grounded in established practice or theory.

4.  **Key Operating Conditions and Limits  
    ** Identification of operating ranges, performance drivers, or known constraints inherent to the mechanism (e.g., sensitivity to environment, scaling behavior, latency sources).

In summary, we are expecting you to elaborate on your competing mechanisms i.e. details of how they work. A good example for this is given in the **sample for system level design concept.pdf** in the module “system level design concept” on LMS.

## **2) Preliminary Concepts Document**

#### **Purpose**

To define **candidate architectures** clearly enough to be attacked.

### **A. Candidate Architectures Overview**

List **2–3 integrated system concepts**.

| **Concept ID** | **One-Line Description** |
|----------------|--------------------------|
| C1             |                          |
| C2             |                          |
| C3             |                          |

### **B. Architecture Descriptions** 

For each concept:

**Concept ID:**

**High-Level Architecture Diagram:  
** (block diagram or sketch)

**Key Components:**

- sensing

- actuation

- computation

- communication

- control logic

**Key Assumptions Used:  
** (list Assumption IDs)

### **C. Initial Risk Identification**

| **Risk ID** | **Description** | **Source (Assumption / Interface / Environment)** |
|----|----|----|
| R1 |  |  |
| R2 |  |  |

### **D. Decision Criteria (Pre-Commit)**

Define criteria **before any scoring**.Weightage is supposed to be distributed across the criteria according to the relative importance.

| **Criterion** | **Weightage** | **Derived From (Req / Objective)** | **Why It Matters** |
|----|----|----|----|
|  |  |  | Add weight for each criterion as well |

> No scores yet. This locks the decision logic.

<u>Instructions for uploading the trade studies on Innoslate:</u>

1.  Document your trade studies as Pugh matrix on excel or any other format of your liking.

2.  Download that document as a pdf or docx file

3.  On Innoslate, create an Artifact with the name “Trade study for xyz” and upload the aforementioned document there.

4.  Create a decision entity on Innoslate. Name it according to whatever decision was made in the trade study.

5.  Create a “enables” relation between the artifact and decision entity.

For reference a pugh matrix is attached below that you can use to understand how to make one for your design choices:  
![Pugh matrix example](../../assets/images/image14.png)

Detailed steps for making this can be found in “getting design right” chapter 5.
