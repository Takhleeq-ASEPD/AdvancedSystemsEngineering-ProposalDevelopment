---
title: "Preliminary Design Review (PDR) Document"
stage: "Later Deliverables"
deliverable_id: stage4-d1
status: draft
last_reviewed: 2026-05-23
---

# Preliminary Design Review (PDR) Document

Stage 3 — Synthesis

**0.0 Introduction**

A design review evaluates a design against its requirements to **verify previous work** and **identify issues** before committing to further development. It must involve reviewers external to the design team. Because the cost of correcting a fault grows as development progresses, early reviews are a high-value investment.

This document demonstrates that the preliminary design meets all system requirements with acceptable risk and within cost and schedule constraints, and establishes the basis for proceeding with detailed design. It confirms that the correct design options have been selected, interfaces identified, and verification methods defined.

The structure follows Preliminary Design Review (PDR) conventions as described in the Auburn University systems engineering curriculum, consistent with DoD and NASA PDR practice. Each section corresponds to a distinct stage of the synthesis process and maps to one or more Stage 3 deliverables.

**Purpose of this document**

The purpose of the PDR is to **review the** **conceptual design** to ensure that the planned technical approach will meet the requirements.

The following are typical objectives of a PDR:

- Ensure that all system requirements have been validated, allocated, the requirements are complete, and the flowdown is adequate to verify system performance

- Show that the proposed design is expected to meet the functional and performance requirements

- Show sufficient maturity in the propos**Preliminary Design Review Document**ed design approach to proceed to final design

- Show that the design is verifiable and that the risks have been identified, characterized, and mitigated where appropriate.

**1.0 Functional architecture**

This section presents how the selected system concept was transformed into a functional architecture. It covers the decomposition of high-level actions into subsystem-level behaviours, the identification of interfaces between subsystems, and the construction of the Physical I/O and Asset diagrams that form the basis for requirements generation.

### **1.1 Subsystem decomposition** 

**➤** 1.1.1 Briefly describe the subsystem structure with how many subsystems the system has, what each one is responsible for, and the overall operational logic that connects them.

*Note: This narrative should be written for an industry reviewer who has not seen your Innoslate model.*

### **1.2 Low-level action diagrams**

The low-level action diagrams decompose the high-level action diagram from Stage 1 to a level where individual subsystems can be assigned responsibility for each action. Decomposition continues until actions can be implemented by hardware, software, or people.

**➤** 1.2.1 Present the low-level action diagrams for each high-priority use case. For each diagram:

- Embed the diagram image exported from Innoslate.

- Provide a figure caption identifying the use case and the scenario.

- Include a one to two sentence description beneath the figure explaining what the diagram shows and which subsystems are most active in this scenario.

*Note: If diagrams exist for multiple scenarios of the same use case, group them together.*

### **1.3 Physical I/O and asset diagram** 

The Physical I/O Diagram integrates the functional model (action diagrams) with the physical model (subsystems and assets) into a single connected representation.

**➤** 1.3.1 Present the top-level Physical I/O Diagram showing all subsystem assets and external entities, with conduits connecting them. For each:

- Embed the diagrams with figure captions.

- Add decomposition diagrams for any subsystem that is itself composed of sub-assets.

- After the Physical I/O Diagram, include a brief interface summary table identifying each conduit, the subsystems it connects, and the type of flow (information, energy, or material).

**➤** 1.3.2 Present the top-level Asset Diagram generated from the Physical I/O Diagram. For each diagram:

- Embed the diagram with figure captions.

- Add decomposition diagrams for any subsystem that is itself composed of sub-assets.

*Note: If subsystem-level decomposition diagrams exist for complex assets, include them as sub-figures immediately after the top-level diagram.*

## **2.0 Requirements baseline**

This section presents the formal requirements baseline established during Stage 3. The primary document is the System Requirements Document (SRD), which contains three integrated layers: functional requirements (SRD Section 3.2, corresponding to Deliverable 3), technical requirements derived from the trade studies, and verification requirements (SRD Section 4, corresponding to Deliverable 6).

### **2.1 Completing the SRD**

The SRD is generated from the Asset Diagram using the Generate SRD function in Innoslate. This auto-populates sections that are directly traceable to the model.

**➤** 2.1.1 Populate the following sections in SRD manually to the extent possible given the current state of component selection:

- Section 3.1 — Required states and modes: identify each distinct operational mode (standby, active, emergency, maintenance) and note which Section 3.2 requirements apply in each mode.

- Section 3.6 — Adaptation requirements: installation-dependent parameters and operational variables.

- Section 3.7 — Safety requirements: hazardous conditions, fail-safe behaviours, required interlocks. If no hazardous elements exist, state this explicitly.

- Section 3.8 — Security and privacy requirements: protection mechanisms, threats, applicable regulations.

- Section 3.9 — System environment requirements: temperature, humidity, shock, vibration, electromagnetic environment, and storage and transportation conditions.

- Section 3.11 — System quality factors: reliability (MTBF), availability (uptime), maintainability (MTTR), testability, and usability — all stated quantitatively where possible.

- Section 3.12 — Design and construction constraints: mandatory architecture choices, physical limits, material restrictions, applicable standards.

- Sections 3.13 to 3.18 — Personnel, training, logistics, packaging, statutory requirements: complete as applicable to the system.

- Sections 3.10 — Computer resource requirements

**➤** 2.1.2 Provide a brief narrative describing the key requirements from 2.1.1. Focus on explaining the intent and context behind the requirements rather than listing them verbatim. The full set of requirements will be documented in Appendix A.

### **2.2 Functional and Technical Requirements**

**➤** 2.2.1 Provide a brief narrative describing the key functional and technical requirements for each major subsystem in your design, and explain the rationale or the approach used to derive the requirements.

**➤** 2.2.2 Add the complete SRD in Appendix A. Add the full derivation of technical requirements in Appendix B.

**2.3 Open Requirements**

**➤** 2.3.1 List the requirements belonging to major or primary subsystems that are not specified as yet in the SRD. For each open item, identify the requirement ID and the information needed to resolve it.

*This list signals to the panel where the requirements baseline is still maturing.*

## **3.0 Technology selection and derivation**

This section covers the two-stage trade study process that translates subsystem functional requirements into specific component selections. The goal is to demonstrate that components were selected against those derived requirements, not by familiarity or convenience.

The process proceeds in two stages:

1.  **Technology Class Selection (Deliverable 4):** What type of technology can perform this function, and what technical parameters must it meet?

2.  **Component Selection (Deliverable 7):** Which specific product within that technology class best meets the derived specifications?

The outputs of both stages feed into quantitative thresholds that make Section 3.2 requirements verifiable, and component-level data needed for budget rollups.

### **3.1 Technology class trade studies**

**➤** 3.1.1 Summarise the key technical requirements that drove the technology class selection for each subsystem. For each subsystem, briefly state the functional requirement being addressed, the governing technical parameter, and the final specified value. Attach the full derivation working in Appendix B.

**➤** 3.1.2 For each subsystem, summarise the outcome of the technology class comparison, identifying the selected technology class and the key reasons for its selection.

**➤** 3.1.3 Summarise the key technology class risks identified during Deliverable 4 and their association with the technology selection decision. Do not reproduce the full risk details here — attach the complete risk documentation in Appendix C.

*Remember! The review panel needs to see the analytical chain — from functional requirement to technical parameter to evaluated technology classes to selected class — not just the conclusion.*

### **3.3 Component selection trade studies**

**➤** 3.3.1 For each subsystem, summarise the outcome of the component evaluation, highlighting which candidates met the selection criteria and which did not. Do not reproduce the full evaluation table here — attach the complete component evaluation table in Appendix B.

**➤** 3.3.2 Summarise the key component-level risks identified during Deliverable 7, including supply chain, obsolescence, integration, and environmental compliance risks, in the context of the component selection they are associated with. Do not reproduce the full risk details here — attach the complete risk documentation in Appendix C.

## **4.0 Performance analysis**

This section presents the system-level analyses conducted to confirm that the chosen architecture is viable as a whole. Where the component evaluation tables in Section 3 confirm that individual parts meet individual requirements in isolation, this section shows that the integrated system meets its top-level constraints.

### **4.1 Analyses**

**➤** 4.1.1 Present a summary of each of the analyses performed and their key results, including traditional and domain-specific analyses. Include the details in Appendix C.

## **5.0 Verification approach**

This section presents the verification requirements established in SRD Section 4. For each system requirement, there is a corresponding verification requirement that specifies the method by which compliance will be confirmed and the acceptance criterion that defines a passing result. The full verification requirements are in Appendix A (SRD).

**4.1 Verification methods**

For each requirement in the **Requirements Baseline** section, provide a brief narrative description of how the requirements will be verified — the methods used and the reasoning behind them. Detailed verification requirements are in Appendix A as part of the SRD.

### **4.2 Verification traceability**

Include the verification traceability matrix exported from Innoslate, showing each system requirement linked to its verification requirement(s). This confirms that every requirement has a verification path. Include the matrix in full here in Appendix E.

### **4.3 Notable verification considerations**

Identify any verification requirements that will require special equipment, facilities, access, or scheduling arrangements to execute. These are constraints on the build and test plan and should be visible to the panel before Section 6 is presented.

##  

## **6.0 Risk register**

This section consolidates the risks identified across the three analytical deliverables of Stage 3. Risks are presented in three layers reflecting the order in which they were discovered during the synthesis process. The risk register must be consistent with the Risk entities recorded in Innoslate.

### **6.1 Layer 1 — Technology class risks (from Deliverable 4)**

Present the risks identified when evaluating which type of technology could perform each subsystem function. These risks relate to the operating principle and supply characteristics of a technology class, not to any specific product. Typical technology class risks include:

- Performance risk: does the technology class meet the final specified value under the worst-case scenario, or only under nominal conditions?

- COTS or GOTS dependency: is the class dominated by a small number of suppliers or subject to export restrictions?

- Integration risk: does the class require specialised drivers, calibration equipment, or interface standards that could create compatibility issues?

- Environmental risk: does the class perform reliably across the full operating range defined in SRD Section 3.9?

### **6.2 Layer 2 — Component risks (from Deliverable 7)**

Present the risks identified when selecting specific components within the chosen technology class. Typical component risks include:

- Supply chain risk: single-source dependency, distributor availability, or extended lead times.

- Obsolescence risk: end-of-life products or recently released components with an unproven supply history.

- Performance risk: datasheet performance reported under nominal conditions that may not hold under worst-case operating conditions.

- Environmental compliance risk: component rated operating range narrower than the system environment requirement.

### **6.3 Layer 3 — System-level risks (from Deliverable 8)**

Present the risks that emerged from the performance analysis and reflect uncertainties at the level of the integrated system. These include:

- Budget margin risks: any mass, power, or cost budget with a yellow or red margin.

- Timing risks: scenarios where the Monte Carlo simulation shows a meaningful probability of failing the timing requirement.

- Analysis assumption risks: system-level analyses that relied on assumptions that may not hold in the actual operating environment.

### **6.4 Risk summary table**

Present a consolidated risk summary table for all risks rated medium or above, drawn from all three layers. The table should include, for each risk: a unique Risk ID (cross-referencing the Innoslate entity), a brief description, the layer it originated from, the likelihood and consequence ratings, and the mitigation strategy.

### **6.5 Risk summary table**

The following table should be completed for all risks rated medium or above. Risks rated low may be noted in the Innoslate risk chart without requiring a row in this table.

| **Risk ID** | **Description** | **Layer** | **Rating (L/C)** | **Mitigation** |
|----|----|----|----|----|
|  | Enter risk description | 1 / 2 / 3 | L: H/M/L C: H/M/L | Enter mitigation strategy |
|  |  |  |  |  |
|  |  |  |  |  |

## **7.0 Build and verification plan**

The plan describes how the team will build, integrate, and verify the system from the current state through to final demonstration. It converts technical decisions into a structured execution plan: risks from Section 6 become early-phase mitigation tasks, verification requirements from Section 4 become gate criteria, and the BOM from Section 5 drives the procurement schedule.

### **7.1 Plan structure overview**

Open with a brief narrative (three to five sentences) describing the overall plan structure: how many phases the plan has, the total duration, and the major gate events. This orients the panel to the plan before they examine the detail.

### **7.2 Level 1 phase plan**

Present the Level 1 phase plan. For each phase, include:

- The macro-deliverables produced in that phase, each stated as an output rather than an activity.

- The gate criteria that must be met before proceeding to the next phase, referenced to specific verification requirements in SRD Section 4.

- The planned start and end dates and the team members responsible.

The Level 1 plan should be presented as a Gantt view exported from the project plan template, with phase boundaries and gate events clearly visible.

### **7.3 Level 2 iteration plan**

Present a summary of the Level 2 sprint structure for each phase. For each phase, identify:

- The high-risk and high-uncertainty items placed at the front of the phase.

- Long-lead procurement items and their planned procurement dates.

- The gate review preparation sprint, placed one to two weeks before the end of the phase.

The full Level 2 plan is included as Appendix D. In this section, present a condensed view covering the most significant mid-level deliverables and dependencies per phase.

## **Appendices**

The appendices contain the full artifacts referenced in the main body. Each section of the main body is designed to be readable without opening the appendices. The appendices allow a reviewer to examine the detail behind any claim in the main body.

### **Appendix A — System Requirements Document (SRD)**

The full SRD exported from Innoslate, including all sections completed during Stage 3. This document captures the functional requirements (SRD Section 3.2), all technical requirements, and the verification requirements (SRD Section 4). Export as a Basic Document Output (DOCX) from Innoslate.

Also include the following traceability matrices exported from Innoslate:

- Stakeholder requirements to system requirements matrix.

- System requirements to verification requirements matrix.

### **Appendix B — Trade study tables (Deliverables 4 and 7)**

The complete trade study documentation, including:

- Literature review summaries for each subsystem function.

- Technical Requirements Tables with full derivation working (Deliverable 4).

- Technology class comparison tables or Pugh matrices.

- Component evaluation tables with candidate datasheets (Deliverable 7).

- Decision records for each technology class and component selection.

### **Appendix C — Design analysis report and BOM (Deliverable 8)**

The full Design Analysis Report from Deliverable 8, including:

- Analysis plan table.

- Budget analysis working for all applicable constraints.

- Discrete event simulation results and Monte Carlo histograms.

- Domain-specific analysis results where applicable.

- Full Bill of Materials compiled using the BOM template.

### **Appendix D — Project plan (Deliverable 9)**

The completed project plan Excel file, including the full Level 1 and Level 2 plans for all components. Export or print as a PDF showing the Gantt view with all rows visible.

### **Appendix E — Traceability matrices**

The following matrices exported from Innoslate to demonstrate end-to-end traceability across Stage 3:

- System requirements to component assets (satisfied by): confirms every technical requirement is satisfied by at least one selected component.

- Component assets to actions (performs): confirms every leaf-level action in the action diagram is allocated to a component asset.

- Requirements to risks: confirms that safety-critical and performance-critical requirements have associated risk analysis.

