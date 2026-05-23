---
title: "Verification Requirements Document (for Stakeholder Requirements)"
stage: "Requirements"
deliverable_id: stage1-d5
status: draft
last_reviewed: 2026-05-23
---

# Verification Requirements Document (for Stakeholder Requirements)

### **What this deliverable is**

This document defines **how stakeholder requirements will be verified**.

Verification requirements describe:

- what evidence is needed

- what method will be used (test, inspection, analysis, demonstration)

Not all stakeholder requirements need a verification requirement:

- Simple requirements may link **directly to a test plan**

- Complex or abstract requirements require **verification requirements first**

### **Why this deliverable is important**

- It ensures requirements are not just written, but **provable**.

- It prevents late-stage disputes about “how do we know this works?”

- It enables structured test planning.

- It enforces engineering accountability.

- It gives an opportunity to create preliminary test requirements.

**Guidelines**

1.  **Create a new Requirements Document** for the purpose of identifying verification requirements separately.

    1.  Navigate to “Documents” view.

    2.  Create a new document.

    3.  Select “Requirements Document”.

    4.  Set:

        1.  Number: “VR.1”.

        2.  Name: “Stakeholder Verification Requirements”

        3.  Template: “Blank Document”

2.  **Identify Verification Requirements**

    1.  Use the same format as the Stakeholder Requirements document

    2.  Replace ambiguous wording (e.g., *at least*, *sufficient*, *adequate*) with measurable values.

    3.  Convert qualitative statements into **quantified performance criteria**.

> As an example, Figure 8.1 has two verification requirements that were traced from the original requirement (WMB.1.1.6.1. Extract Oxygen). These requirements attempt to define how much oxygen needs to be extracted to support life support and rocket fuel needs.
>
> Obviously, “100%” and “50%” need to be refined into specific amounts. The quality checker caught another problem. The words **“at least”** are **ambiguous** and would **make verification difficult**. Words like “greater than or equal to” a specific amount would be better.
>
> A requirement typically becomes verifiable only when measurable.
>
> A quantifiable requirement is often called “metric” or technical performance measure (TPM).

3.  **Handle Quantified Characteristics**

    1.  For quantified verification requirements:

        1.  Create Characteristic entity

        2.  Create a relationship “specifies” with the relevant verification requirement.

    2.  For verification requirements yet to be quantified:

        1.  Create an Issue or Decision entity

        2.  Create a relationship “enables” between verification requirement and Decision.

        3.  Create a relationship “causes” between verification requirement and Issue.

> This is to ensure that these decisions are made and issues are resolved in the near future.

4.  **Define Verification Methods**

> Consult domain experts and assign a verification method to each requirement using the Metadata labels on the sidebar:

- **Analysis:** Showing a requirement is met using calculations, logic, proofs, or reasoning—without physically running the system. For example, hand calculations, spreadsheet analysis, worst-case / margin analysis, tolerance stack-ups, standards-based reasoning, safety or reliability math, etc.

- **Demonstration:** Showing the requirement is met by operating the real system in a representative but informal way. No instruments, no precise measurements—just “watch it work.” For example, turn it on and observe behavior, drive the robot through a path, flip a switch and see the response, run a scenario once or twice, etc.**  
  **

- **Inspection:** Showing compliance by looking at the system—its configuration, dimensions, labels, or properties—without operating it. For example, visual checks, measurements with calipers, part number verification, checklist comparison, document conformance, etc.**  
  **

- **Modeling & Simulation:** Using a formal model of the system to simulate behavior under conditions that are too expensive, too dangerous, too rare, or not yet buildable. More formal than analysis; more abstract than demonstration. For example, MATLAB / Simulink models, physics simulators (Gazebo, ANSYS, Adams), control-system simulations, Monte-Carlo simulations, digital twins, etc.

> Multiple methods may be assigned if appropriate.
>
> For example, for the two verification requirements in Figure 8.1, we can verify them by analysis once the specific amounts of oxygen extracted have been identified. We can tag this method by using one of the built-in Innoslate labels.

5.  **Check Requirement quality**

    1.  In the Requirements Document dropdown ![](../../assets/images/image12.png){ style="width:0.36896in;height:0.22361in" }, select and run Quality Check.

    2.  Review flagged issues from the tool and refine wording.

> Note: The tool cannot evaluate Correctness (is it legal) and Feasibility (is it possible). Hence, a human check is required too.

6.  **Trace to test cases (optional)**

??? note "Sadaf · 2026-05-07"
    Add instructions for creating relationship: Stakeholder req (verified by) Verification Req
<!-- comment:4 -->


> A “Test case” class, which is a subclass of the Action class:

- supports Innoslate’s Test Center view, where different test cases can be analysed.

- inherits all the attributes and relationships from the Action class, which means these test cases can be visualized using all the diagrams associated with the Action, including the Action Diagram.

- used directly in the project planning for the verification activities, which includes cost, schedule, and resource impacts.

> For each verification requirement:

1.  Create a test case.

    1.  On the left side-bar, under “Relationships”, use “verified by” relationship, and create a new test case.

    2.  Fill the following attributes:

        1.  Number: “TS.n”

        2.  Name: {name of the test case}

        3.  Description: {add description}

        4.  Set up

        5.  Expected Result

        6.  Status: “Not Run”

    3.  Save changes

> You can at this point also start developing a test plan. Innoslate has a test plan template available, which you can use and/or tailor to your own. For more details on the test plan, refer to “Preliminary Verification Planning” section in Chapter 5 in *Real-MBSE book* and Lab 9 in the *Real-MBSE Lab Manual.*
>
> *This step is optional, but encouraged, because detailed planning of tests may not be feasible at the current level of clarity in the projects. But wherever the method of testing is well-understood, it should be documented in a test plan.*

7.  **Review and finalize**

    1.  Review verification requirements with stakeholders.

    2.  Record outcomes

        1.  Create decisions entities

        2.  Create relationship “enables” between relevant verification requirement and decision.

![](../../assets/images/image3.png){ style="width:6.5in;height:3.34722in" }

Figure 8.1 Adding explicit verification requirements enables better traceability.

**Reporting Instructions**

1.  Download Verification Requirements document on Innoslate as “Basic Document Output (DOCX)”

2.  Create traceability matrix between Verification and Stakeholder Requirements

    1.  Follow the steps in [<u>this</u>](https://help.specinnovations.com/traceability-matrix-overview) guide to create the traceability matrix.

3.  Download the traceability matrix as “Matrix Report (xlsx)”

4.  Convert to pdf

5.  Merge documents from step 1 and 4.

6.  Upload a single merged document on Canvas.

**ConOps template**

- Mission description ( to be incorporated in earlier deliverables)

  - Goals and objectives?

  - List of stakeholder template in conops

  - As-is gaps

- System operational context ..

  - Reference operational architecture has not been introduced to students yet.. Will be introduced during synthesis

- Remove section 4

- Operational scenarios

  - Add use cases and action diagram

- Remove section 6-8

**Students Checklist**

#### **Document Setup**

☐ Created **VR.1 – Stakeholder Verification Requirements** document (Blank template)  
☐ Format matches the Stakeholder Requirements document

#### **Verification Requirements**

☐ Every verifiable stakeholder requirement has a corresponding verification requirement  
☐ Ambiguous wording replaced with measurable values  
☐ Quantified criteria defined as metrics / TPMs

#### **Characteristics & Open Items**

☐ Characteristic entities created for quantified parameters  
☐ Linked using **specifies** relationship  
☐ Issues/Decisions created for undefined verification values

#### **Verification Method**

☐ Each requirement labelled with at least one method:Analysis, Demonstration, Inspection, Modeling & Simulation

#### **Quality Check**

☐ Quality Checker run and warnings addressed  
☐ Human review completed for correctness & feasibility

#### **Traceability**

☐ Each verification requirement linked to a **Test Case  
**☐ Verified by / verifies relationships created

#### **Review & Decisions**

☐ Reviewed with stakeholders  
☐ Decisions recorded and linked to requirements using “enabled by”
