---
title: "High-Level Action Diagrams"
stage: "Requirements"
deliverable_id: stage1-d4
status: draft
last_reviewed: 2026-05-23
---

# High-Level Action Diagrams

### **What this deliverable is**

The **Action Diagram** shows the **end-to-end workflow** of how work is performed *after the system is introduced*, integrated with existing practices.

It focuses on **behavior and flow**, not hardware or software structure.

### **Why this deliverable is important**

- It reveals process gaps and inefficiencies.

- It helps validate that the system actually improves operations.

- It aligns system behavior with stakeholder expectations.

- It supports requirement validation and scenario analysis.

**Guidelines**

The steps outlined below are typically applied in detail only after a system-level concept has been established. At this stage, **do not attempt full correctness or completeness**. Instead, use these steps solely to describe the **sequence of events** associated with the **core functions** the solution must perform.

The goal of the action diagram is to help you think clearly about *what needs to happen*, not *how it will be implemented*. A complete and exhaustive set of use cases will be developed later, once the system concept is finalized. For now, include only those scenarios or use cases that can be described **without assuming a specific solution or design choice**.

The following steps are followed depending on how detailed our system-level concept currently is:

1.  **Develop behavioural descriptions for each of the high-priority use cases (optional)**

> *Using the Use Case Behaviour Description template provided in Figure 7.1, describe actions performed by assets for each use case/scenario. These should include both system and human actions.*
>
> Note: This step is optional. You can skip this step if you would like to develop the functional model on Innoslate directly.

2.  **Develop Behaviour models for each scenario on Innoslate using action diagrams for As-is and To-be Architecture**

> If use case behaviour descriptions are developed, use them to decompose scenario blocks in the high-level action diagram by opening as “Decomposition Diagram”. Otherwise, decompose without them.
>
> While decomposing, follow the steps below:

1.  Walk the column of “System” and create action blocks for the entries.

2.  Walk the columns of the external entities who trigger any of the SoI’s action blocks or vice versa and implement their actions as parallel action streams

3.  Use inputs/outputs as triggers between action streams. Refer to Figure 7.2.

4.  Label these parallel action streams with performing assets for external entities and SoI.

<!-- -->

1.  Create relationship “satisfies” for every use case/scenario with the relevant functional requirements in the Stakeholder Requirements document.

??? note "Sadaf · 2026-05-21"
    This should be "traced from" in stage 3 under "Low-level action diagrams": if they are serving as requirements, the same relationship should appear if they serve as design choice, use Action "satisfies" Requirement relationship
<!-- comment:31 -->


??? note "Sadaf · 2026-04-28"
    Use case/scenario (traced from) Stakeholder requirement.
<!-- comment:3 -->


![](../../assets/images/image15.png){ style="width:4.10625in;height:4.8258in" }

Figure 7.1 Example Behavioural Description

To view an example on how to create an Action Diagram from a Use Case Behaviour Description, go to Appendix 2.

**<u>Appendix 2</u>**

Below is one of the use case behaviour description from the toy catapult example from *Getting Design Right*:

![](../../assets/images/image1.png){ style="width:3.88269in;height:4.48843in" }

By walking the columns of the table above, the following action diagram in Figure 7.2 can be developed:

> ![](../../assets/images/image8.png){ style="width:4.64756in;height:4.11875in" }
>
> Figure 7.2 Action diagram for Parent Entertains Child Use Case

Note that Toy is the System of Interest (SoI). We walk the column of “System” and create action blocks for the entries. Parent, Train, and projectile are external entities. Walk their columns and create parallel streams for each performing external asset.

**Reporting Instructions**

1.  Download “Opaque Image (PNG)” for both the parent diagram and children diagrams.

2.  Fill the template with the images in step 1.

3.  Upload the filled template on Canvas.

#### 

#### **Student Checklist – Action Diagram**

☐ A behaviour description exists for each high-priority use case/scenario

☐ An Action Diagram was created for each scenario

☐ Action diagrams exist for both As-Is and To-Be architectures

☐ All actions have performing assets (no unassigned actions)

☐ All interactions are connected with triggers

☐ All scenarios trace to requirements
