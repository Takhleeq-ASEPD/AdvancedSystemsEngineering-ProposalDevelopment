---
title: "Subsystem Identification"
stage: "Stage Synthesis"
deliverable_id: stage3-d0
status: draft
last_reviewed: 2026-09-29
---

# Subsystem Identification

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

## **4. Appendix**

![Example of list of functions and components](../../assets/images/image18.png){ style="width:2.69883in;height:2.6494in" }

Figure 1. Example of list of functions and components

![Subsystems for toy catapult example](../../assets/images/image9.png){ style="width:3.65278in;height:3.71919in" }

Figure 2. Subsystems for toy catapult example

## **Where this feeds**

The named subsystems produced here are the direct input to:

- [D1 · Low Level Action Diagram](d1-low-level-action-diagram.md) — each high-level action is opened up against the subsystem responsible for it.
- [D2 · Physical I/O and Asset Diagram](d2-physical-i-o-and-asset-diagram.md) — one Asset box per subsystem identified here.
