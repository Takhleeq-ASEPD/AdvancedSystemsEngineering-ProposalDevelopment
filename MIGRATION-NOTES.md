# Migration notes

What was restored, what is still wrong, and one thing about the source document that is easy
to misread. Written against the repo at tag `before-restore`.

---

## Two versions of the relationship guidelines, both kept

The source has *relationships guidelines* and *Copy of relationships guidelines*. Both are Sadaf's,
both are current, and both carry open comments, so both are in the repo and both get edited.

| | |
|---|---|
| `docs/relationships/index.md` | The *Copy of* version. Corrections applied, no verdict column. |
| `docs/relationships/with-verdicts.md` | The first version. Same table plus Correct / Incorrect / Caution and the reasoning. |

They differ because the second was written without announcing that the earlier instructions had been
wrong. One of the two goes once everything is propagated. Not yet.

The original migration appended both to the bottom of the Stage 4 PDR page. Delete that block once
these files are in.

---

## What the remaining work actually is

`docs/relationships/index.md` already carries the corrected verbs. **The stage pages do not.**
They still instruct the old ones.

So the work is not deciding what is correct. Sadaf did that. The work is propagating the table
into `docs/stages/`, consistently, in every place each verb appears. That is what comment
`AAAB60w8-zM` means by *MAJOR PROBLEM: look for consistency in the deliverables document as well
as in these guidelines*, and it is the reason this is a git job rather than a document job.

**Innoslate implements LML 1.4**, confirmed at help.specinnovations.com, page dated 21 April 2026:
its relationships mirror Table 3-3 of the LML Relationships Specification 1.4. Both tables assess
against 2.0, so a row marked Correct may still name a verb Innoslate does not offer. Check the
relationship dropdown in the tool before applying anything.

---

## Restored in this commit

| | |
|---|---|
| `docs/relationships/index.md` | Student-facing guidelines, one copy, all four sections |
| `docs/relationships/README-first.md` | What each file is and which to edit |
| `docs/relationships/open-comments.md` | All 50 open review threads with real Google comment IDs |
| `docs/relationships/stage1-checklist-patch.md` | Stage 1 checklist sections 4 to 7, dropped by the original migration |
| `docs/relationships/with-verdicts.md` | The version with the review verdicts |

---

## Known problems not fixed here

**Both guideline copies are still on the PDR page**, from roughly line 321 of
`docs/stages/4-later-deliverables/d1-preliminary-design-review-pdr-document.md`. Delete that block
once the new files are in, so the guidelines live in one place.

**Comments cannot be re-anchored automatically.** The Google export does not record which text each
comment was attached to. The 34 already inline were placed by the original migration and at least one
is provably wrong: on the Stage 1 stakeholders page, `Risk (references) trade study` sits on a
stakeholder evidence step where the source has no comment at all. Treat inline placements as unverified.

**Sixteen comments were missing entirely**, all from February 2026, including every comment by Munzir
and by Ailiya. They are in `open-comments.md`.

**Page boundaries are wrong.** Content following a deliverable in the source was appended to the
preceding page:

- `d1-list-of-stakeholders.md` also contains Raw Evidence Sources and the whole User Needs Document
- stage 2 `d4-verification-requirements-...md` also contains Red Team Review Instructions, the
  System-Level Concept Design Stage overview, the grading scheme and OCD material

**Stage index pages are stubs** listing deliverable names that do not match the pages beside them.

**Two source sections were never migrated:** *Tab 1*, an alternative drafting of four Stage 1
deliverables, and *Tab 14*, industry project briefs. Both may be superseded; nobody has confirmed it.

**Sixty-two of the 65 resolved comments were dropped.** They record decisions already taken about
relationship names, which the freeze will want.
