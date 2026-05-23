---
title: "Stakeholder Requirements Document"
stage: "Requirements"
deliverable_id: stage1-d3
status: draft
last_reviewed: 2026-05-23
---

# Stakeholder Requirements Document

### **What this deliverable is**

The **Stakeholder Requirements Document** translates user needs into **formal, solution-independent requirements** that the system must satisfy.

These are **top-level requirements** representing *what the system must do*, not *how it will do it*.

### **Why this deliverable is important**

- It creates a contract between stakeholders and the engineering team.

- It enables objective verification later in the project.

- It is the foundation for architecture, design, and testing.

- Poorly written requirements cannot be verified.

**Guidelines**

Figure 6.1 shows an overview of requirements analysis in Model-Based Systems Engineering. We can break the analysis down into steps below:

1.  Decompose Statements

??? note "Sadaf · 2026-05-08"
    future iteration: stakeholder req -> scenarios ->action diagrams (some decomposition) add stakeholder functional requirements from the action diagram
<!-- comment:0 -->


    1.  Create a new Requirements Document using “Create Document” on the Manage Documents Dashboard view of your project. Name the document as “SR.1”.![](../../assets/images/image4.png){ style="width:0.38542in;height:0.20016in" }

    2.  Create requirements using “New Requirement” button. Number the requirements as “SR.1.N” where “N” is the number of the requirement.

    3.  Create relationship “traced from” with User need statements.

??? note "Sadaf · 2026-05-21"
    MAJOR PROBLEM: this is correct. Look for consistency in the deliverables document as well as in these guidelines.
<!-- comment:30 -->


??? note "Sadaf · 2026-04-28"
    Risk (caused by) Requirement
<!-- comment:20 -->


    4.  Add labels to each requirement such as "Functional Requirements" or "Technical Requirements".

    5.  Run <span class="mark">Quality checker</span> for clear, complete, consistent, design, and traceable quality parameters.

2.  Identify Existing/Planned Systems to extract additional requirements (**for projects where a legacy system exists**)

    1.  Look at existing systems or capabilities and abstract these systems into fundamental functions that they perform and measure performance values.

    2.  The functional and performance values can become the minimum requirements that a new system would be required to provide.

    3.  Then, these values can be used to suggest goals for improvement in the new system.

    4.  Add additional requirements to the Stakeholder Requirements Document.

3.  Identify any critical issues, resolve issues through trade studies and discussion with customers.

    1.  Identify any critical issues or risks during the time of analysis.

    2.  Create Issue entity and create relationship of requirement using “causes”.

    3.  Resolve issues/risks through trade studies and discussion with customers. Create Trade Study document as Artifact and add a label “Trade Study”. Create relationship of trade study with Issue using “resolves”.

??? note "Sadaf · 2026-05-08"
    so Replace relationship between trade study and risk(modelled as issue) with decision and risk.  trade study (enables) decision (resolves) issue (modelled as issue)
<!-- comment:2 -->


??? note "Sadaf · 2026-04-28"
    resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Issue, and Decision enabled by Trade Study.
<!-- comment:1 -->


    4.  Create a Decision entity and its rationale and create relationship with trade study as “enabled by”.  
        (for more details on relationships refer to the source: [<u>https://help.specinnovations.com/entity-data-elements</u>](https://help.specinnovations.com/entity-data-elements))

![1. requirements analysis.png](../../assets/images/image23.png){ style="width:5.86114in;height:3.57387in" }

Figure 6.1 Requirements Analysis captures and understands the users’ needs

Remember, although the steps mentioned above are laid out linearly, agile systems engineering is non-linear and iterative in nature as reflected in Figure 2 below. For more detail on Middle-out process, refer to section “Processes” in Real-MBSE book Chapter 1.

![](../../assets/images/image13.png){ style="width:5.16458in;height:3.0044in" }

Figure 2: The Middle-out process is non-linear in nature and is key to Agile Systems Engineering

**Reporting Instructions**

1.  Download Stakeholder Requirements document on Innoslate as “Basic Document Output (DOCX)”

2.  Create traceability matrix between Stakeholder Requirements and User Needs

    1.  Follow the steps in [<u>this</u>](https://help.specinnovations.com/traceability-matrix-overview) guide to create the traceability matrix.

3.  Download the traceability matrix as “Matrix Report (xlsx)”

4.  Convert to pdf

5.  Merge documents from step 1 and 3.

6.  Upload a single merged document on Canvas.

####  

#### **Student Checklist – Stakeholder Requirements** 

#### **The key to requirements analysis is the development of requirements that are:** 

- Clear and unambiguous so as not to confuse the reader

- Complete so that they express a whole, single idea, and not portions of one or many

- Consistent with other requirements

- Correct such that they describe the user’s true intent and are legally possible

- Design independent so that they do not impose a specific solution on design (“what” not “how”)

- Feasible so that they can be implemented with existing or projected technology, and within cost and schedule

- Traceable so that they can be uniquely identified, and be able to be tracked to predecessor and successor lifecycle items/objects, such as functions or components

- Verifiable so that you can prove (within realistic cost and schedule) that the solution meets the requirement

**In the development of these good requirements, you may want to avoid the following**

**pitfalls:**

• DON’T use ambiguous language

• DON’T use bullet lists; use numbered lists instead

• DON’T use jargon

• DON’T use language that provides an escape clause; e.g., “The user shall be able to

access the Internet as often as is practicable”

• DON’T write long, rambling sentences

• DON’T put two requirements in one sentence; e.g., “The system shall … and …”

• DON’T use vague terms; e.g., “user-friendly”

• DON’T include suggestions or possibilities; e.g., “may”, “should”, “ought”

• DON’T include wishful thinking; e.g., “The system shall be 100% reliable”
