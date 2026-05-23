---
title: "Context Diagram"
stage: "Requirements"
deliverable_id: stage1-d2
status: draft
last_reviewed: 2026-05-23
---

# Context Diagram

### **What this deliverable is**

This deliverable **visualizes the relationships between entities in a system**. The nodes of the network are the proposed system and the external entities. The connecting arcs of the network are the relationships between the system and the external entities.

In summary, a **context diagram** identifies:

- The internal systems

- external systems and actors

- interfaces and interactions

### **Why this deliverable is important**

- Defines **system boundaries,** i.e. what is within the scope of the design and what is outside the design scope.

- Avoids confusion over what entities are external.

- Exposes hidden interfaces, stakeholders, and dependencies.

- Minimizes integration failures coming from poor context understanding.

- Explains why each external entity was thought to be relevant to the system.

### **Guidelines**

1.  **Draw Context diagram for “As-is Architecture” and “To-be Architecture”**

> The *As-Is architecture* describes how the system works **right now**, before any improvements or new design is implemented.
>
> The *To-Be architecture* describes how the system will work after the new design or improvements are implemented.

1.  Draw rectangular nodes and identify them with the names of the system elements (nouns).

2.  Create arcs and label them with relationships (verb phrases) close to the origin node.

> As an example, Figure 4.1 shows the context diagram for the toy catapult. Note the dotted line used to mark the system clearly. Everything outside the dotted line is an external entity.
>
> ![](../../assets/images/image10.png){ style="width:4.78704in;height:2.52048in" }
>
> Figure 4.1 Example Context Diagram for toy catapult

2.  **Implement Context Diagram in Innoslate**

> There are two options in Innoslate for implementing a context diagram:

- The Asset Diagram

- Physical I/O diagrams

??? note "Sadaf · 2026-05-21"
    Asset connects to Conduit
<!-- comment:36 -->


> Given that the goal is to define the functional elements, the data flowing between them, and the allocation to the Assets and Conduits, the Physical I/O Diagram is the preferred approach. **Repeat the steps below for both the context diagrams drawn in step 1.**

1.  On Innoslate, go to the “Diagrams” view

2.  Select “New Diagram” and then “Physical I/O” from the drop-down list provided..

3.  For “As-is Architecture”, fill in the following attributes:

    1.  Number: “OCD.1”

    2.  Name: “Context Diagram for As-is Architecture”

    3.  Description: {*provide a description}*

4.  For “To-be Architecture”, fill in the following attributes:

    1.  Number: “OCD.2”

    2.  Name: “Context Diagram for To-be Architecture”

    3.  Description: {*provide a description}*

5.  Create an asset for the system, name it, number it as “SYS.1” and add a description.

6.  Create external assets, name them, and number them as “EXT.n”. Mark external assets by selecting ![](../../assets/images/image20.png){ style="width:1.03615in;height:0.25427in" }on the top-bar.

7.  **Connect external systems to the original system**

    1.  Drag the green circle on the selected Asset to another Asset and the dialog in Figure 4.2 will appear.

    2.  Define Input/Output, Conduit, Actions, Directionality, and Origin using the pop-up displayed in Figure 4.2. Directions and shapes for the conduits can be changed by selecting the line and using the “Line Options” button at the top. Fill as many fields as possible for each of the entities.

> ![](../../assets/images/image6.png){ style="width:3.09375in;height:4.125in" }
>
> Figure 4.2 New Input/Output Creation Dialog

For each of the relations in the conduit dialog box, there are various attributes that you can assign to it.

1.  **Action Entity:  
    **

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>What It Represents</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>When to Populate</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Modeling Guidance</strong></p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>The functional activity being performed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Always</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Use verb-object format (e.g., “Process Order”, “Transmit Data”). Avoid technical details.</strong></p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operational explanation of what the action does</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Always</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Describe behavior, not implementation. Keep it functional.</strong></p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Start</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Scheduled start time (if used for simulation)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Rarely at concept stage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Only use if doing timeline/simulation analysis.</strong></p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Duration</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Time required to perform action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Optional at concept stage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Add when timing affects performance, throughput, or constraints.</strong></p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Percent Complete</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Progress tracking (project management)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Development phase</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Not required for early conceptual modeling.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Spend time carefully naming top-level actions (they will drive requirements).

- Do NOT over-model internal logic too early.

- Duration should only be added when timing matters to system performance.

- Avoid decomposing actions prematurely.**  
  **

**II) Conduit Entity:**

| **Field** | **What It Represents** | **When to Populate** | **Modeling Guidance** |
|----|----|----|----|
| **Name** | **Type of flow between assets** | **Always** | **Name by flow (e.g., “Power Supply”, “Telemetry Data”), not hardware.** |
| **Description** | **Explanation of interaction** | **Always** | **Clarify direction, purpose, and conditions.** |
| **Capacity** | **Maximum throughput of flow** | **If performance matters** | **Add when bandwidth, power, or flow limits impact design.** |
| **Units** | **Measurement units for capacity** | **If capacity used** | **Always include if capacity entered.** |
| **Latency** | **Delay in the flow** | **If timing critical** | **Important for control or communication systems.** |

- At concept stage: focus on identifying flows correctly.

- Add capacity/latency only if it affects requirements.

- Avoid specifying cables, protocols, connector types early.

**III) Input/Output (I/O) Entity:**

| **Field** | **What It Represents** | **When to Populate** | **Modeling Guidance** |
|----|----|----|----|
| **Name** | **The thing flowing (data, material, energy, signal)** | **Always** | **Be precise (e.g., “Voltage Signal”, “Status Packet”, “Compressed Air”).** |
| **Description** | **Clarifies nature of the I/O** | **Recommended** | **Define meaning, format, or purpose if unclear.** |
| **Value** | **Default or nominal value** | **Optional** | **Only if needed for analysis or simulation.** |
| **Type** | **Data or physical type** | **Optional** | **Useful for later architectural refinement.** |
| **Size** | **Magnitude, data size, or quantity** | **Optional** | **Add when performance or capacity depends on it.** |
| **Units** | **Measurement units** | **If size/value specified** | **Always include if quantitative fields used.** |

- Focus on clearly defining what flows.

- Avoid over-specifying format (e.g., JSON, CAN frame) at early stages.

- Add size/type when it affects architecture decisions later.

  1.  Save changes

**Student Checklist**

☐ System boundary is clearly defined

☐ All external actors are included

☐ Each interaction is represented with a conduit

**5. List of Scenarios**

### **What this deliverable is**

The **List of Scenarios** is a structured enumeration of **all situations the system may experience during its lifecycle**, from normal operation to edge cases and failures.

A *scenario* describes:

- who is involved

- what triggers the situation

- how the system is expected to behave

- how the situation ends

### **Why this deliverable is important**

- It ensures the team designs for **real operational situations**, not just ideal ones.

- It exposes hidden interfaces, stakeholders, and dependencies.

**Guidelines**

The steps outlined below are typically applied in detail only after a system-level concept has been established. At this stage, **do not attempt full correctness or completeness**. Instead, use these steps solely to describe the **sequence of events** associated with the **core functions** the solution must perform.

The goal of the action diagram is to help you think clearly about *what needs to happen*, not *how it will be implemented*. A complete and exhaustive set of use cases will be developed later, once the system concept is finalized. For now, include only those scenarios or use cases that can be described **without assuming a specific solution or design choice**.

1.  **Implement foundational functional model in Innoslate**

    1.  On Innoslate, go to “Diagrams” View

    2.  Select “New Diagram” then “Action Diagram” from the drop-down list provided.

    3.  Fill in the following attributes:

        1.  Number: “ACT.1”

        2.  Name: “Top-level action diagram”.

        3.  Description: “This action diagram contains the top-level functionality, which will be used to derive requirements for the overall system”

    4.  On the left menu bar, enter the “Existing” tab and add existing action, input/output entities from the pull-down menu to the high-level action diagram in a sequence.

> *This should avoid any low-level technical detail.*

2.  **Derive all use cases/scenarios using the context diagram,** including both primary and secondary/abuse use cases.

> *Think of as many different use cases as you can without thinking about the solution. Do not criticize anyone’s suggestion because criticism will discourage the free flow of ideas.*

3.  **Prioritize use cases/scenarios** based on how likely the use case will give rise to new and important functional requirements.

> *Identify those cases with high priority (H), for which you must describe behaviors; cases with medium priority (M), for which you will describe behaviors if you have time; and cases with low priority (L), for which you will not describe behaviors.*
>
> *For complex systems, budget about 10 high-priority use cases per team member.*

4.  **Develop existing functional model on Innoslate**

    1.  Add the rest of the scenarios/use cases to the high-level action diagram

*<u>You can find an example of how to do it in the appendix below.</u>*

### **Possible scenario categories**

Students are expected to list scenarios across **multiple categories**, not just one.

1.  **Nominal / Normal Operation  
    **

    - Standard, expected use of the system

    - Typical user interactions

    - Routine workflows

2.  **Start-up and Shut-down  
    **

    - System initialization

    - Transitions into and out of operation

    - Safe shutdown conditions

3.  **Abnormal but Expected Conditions  
    **

    - Delays

    - Partial availability of resources

    - Human errors

    - Environmental variations

4.  **Failure and Fault Conditions  
    **

    - Component failures

    - Communication failures

    - Power loss

    - Sensor/actuator malfunction

5.  **Recovery and Mitigation  
    **

    - How the system detects issues

    - How it responds

    - How normal operation is restored (if applicable)

**Student Checklist**

☐ Created new Action Diagram (ACT.1 – Top-level action diagram)

**For each scenario:**

☐ Identifies **who is involved**

☐ States **what triggers it**

☐ Written without assuming a specific solution

**To include (this list is suggestive):**  
☐ Normal operation included

☐ Start-up / shut-down included

☐ Abnormal but expected cases included

☐ Failure cases included

☐ Recovery / mitigation included

**Appendix:**

**Example**

As an example, below is the initial functional model for the Moonbase project created using the existing action, input/output entities from the context diagram:

![](../../assets/images/image5.png){ style="width:5.06539in;height:2.48993in" }

Figure 4.3 Initial functional model for Moonbase project

After exploring how the system may be used, the table below lists scenarios for Selene Moonbase project:

![](../../assets/images/image2.png){ style="width:5.98264in;height:2.73246in" }

Figure 4.4 Initial List of Scenarios for Moonbase: Selene

Then, the table is used to modify the existing action diagram in Figure 4.3 to come up with a modified high-level action diagram (**Real MBSE eBook Chapter 5 pg 84)** below:

> ![](../../assets/images/image7.png){ style="width:5.24323in;height:3.69715in" }
>
> Figure 4.5 Developing the integrated behaviour model for Moonbase project

Note that the actions that were created in Figure 4.3 include a number of scenarios in Figure 4.4. A few adjustments were made from Figure 4.3 to Figure 4.5:

- M.2, M.10, and M.12 were put as children of Scenario 3.

- M.8 “Receive Habitat” was only part of Scenario 4, so it was made the child of that scenario.

- M.13 “Prepare Personnel for Return to Earth” was renamed to S.6 “Rotate Personnel Out.”

So, with a little bit of work, we were able to reuse all the work that was done from developing the context diagram.
