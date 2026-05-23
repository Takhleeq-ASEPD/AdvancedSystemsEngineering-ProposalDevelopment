"""Split the pandoc-converted markdown into per-deliverable files.

Reads the single converted .md file and writes one file per deliverable
under docs/stages/<stage>/d<N>-<slug>.md. Adds front matter, rewrites
image paths to be relative to the deliverable file, strips pandoc anchor
artefacts, and down-shifts H1 headings inside the body so the page has a
single top-level H1.

This is a one-shot migration script — re-runnable if the source docx is
re-converted, but not part of the day-to-day editing workflow.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONVERTED = Path("/tmp/converted.md")
DOCS = REPO / "docs"
TODAY = "2026-05-23"


@dataclass
class Deliverable:
    stage_folder: str    # e.g. "1-requirements"
    stage_label: str     # e.g. "Requirements"
    number: int
    title: str
    slug: str
    start_line: int      # 1-indexed inclusive (the boundary marker line, or 1 for stage1-d1)
    end_line: int        # 1-indexed inclusive

    @property
    def filename(self) -> str:
        return f"d{self.number}-{self.slug}.md"

    @property
    def deliverable_id(self) -> str:
        stage_num = self.stage_folder.split("-")[0]
        return f"stage{stage_num}-d{self.number}"


# Hardcoded mapping derived from inspection of the converted markdown.
# Boundary lines marked "deliverable N - <stage>" exist in the source;
# stage-1 d1 has no boundary and starts at line 1.
RAW_DELIVERABLES = [
    # Stage 1 — Requirements (5 deliverables)
    ("1-requirements", "Requirements", 1, "List of Stakeholders", 1),
    ("1-requirements", "Requirements", 2, "Context Diagram", 557),
    ("1-requirements", "Requirements", 3, "Stakeholder Requirements Document", 971),
    ("1-requirements", "Requirements", 4, "High-Level Action Diagrams", 1100),
    ("1-requirements", "Requirements", 5,
     "Verification Requirements Document (for Stakeholder Requirements)", 1196),
    # Stage 2 — System Concept (4 deliverables)
    ("2-system-concept", "System Concept", 1, "Assumption Mapping & Design Space", 1432),
    ("2-system-concept", "System Concept", 2,
     "Narrative Description of Functional Concept Fragments", 1510),
    ("2-system-concept", "System Concept", 3, "System Requirements", 1612),
    ("2-system-concept", "System Concept", 4,
     "Verification Requirements Document (for System Requirements)", 1853),
    # Stage 3 — Stage Synthesis (9 deliverables)
    ("3-stage-synthesis", "Stage Synthesis", 1, "Low Level Action Diagram", 2957),
    ("3-stage-synthesis", "Stage Synthesis", 2, "Physical I/O and Asset Diagram", 3057),
    ("3-stage-synthesis", "Stage Synthesis", 3, "Functional Requirements Document (FRD)", 3227),
    ("3-stage-synthesis", "Stage Synthesis", 4, "Trade Studies and Associated Risks", 3489),
    ("3-stage-synthesis", "Stage Synthesis", 5, "System Requirements Document (SRD)", 3866),
    ("3-stage-synthesis", "Stage Synthesis", 6, "Verification Requirements", 4024),
    ("3-stage-synthesis", "Stage Synthesis", 7,
     "Trade Studies and Associated Risks (Component Selection)", 4156),
    ("3-stage-synthesis", "Stage Synthesis", 8,
     "Design Analysis Report and Initial Bill-of-Materials (BOM)", 4338),
    ("3-stage-synthesis", "Stage Synthesis", 9, "Level 1 and Level 2 Planning", 4559),
    # Stage 4 — later deliverables (the post-D9 PDR document)
    ("4-later-deliverables", "Later Deliverables", 1,
     "Preliminary Design Review (PDR) Document", 4751),
]


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text


def build_deliverables(total_lines: int) -> list[Deliverable]:
    deliverables: list[Deliverable] = []
    raw = list(RAW_DELIVERABLES)
    for i, (stage_folder, stage_label, num, title, start) in enumerate(raw):
        end = raw[i + 1][4] - 1 if i + 1 < len(raw) else total_lines
        deliverables.append(Deliverable(
            stage_folder=stage_folder,
            stage_label=stage_label,
            number=num,
            title=title,
            slug=slugify(title),
            start_line=start,
            end_line=end,
        ))
    return deliverables


# Lines that should be dropped from the start of a slice:
#  - the "deliverable N - <stage>" boundary marker (any case, any dash style)
BOUNDARY_RE = re.compile(
    r"^\s*deliverable\s+\d+\s*[-—]?\s*(requirements stage|system concept stage|stage synthesis)\s*$",
    re.IGNORECASE,
)
# The Stage-3 title-preamble line that sits 1–3 lines BEFORE the boundary, e.g. "**Low Level Action Diagram**"
# We trim by scanning back from the start_line.
TITLE_PREAMBLE_RE = re.compile(r"^\s*\*\*[^*]+\*\*\s*$")
# Pandoc anchor noise: <a id="_xxx"></a>
ANCHOR_RE = re.compile(r'<a id="[^"]*"></a>\s*')
# The first H1 in the body, e.g. "# **1) Title**" or "# **1. Title**"
FIRST_H1_RE = re.compile(r"^\s*#\s+\*\*\s*\d+[.)]\s*[^*]+\*\*\s*$")
# Image path rewrite: docs/assets/media-extracted/media/imageN.png -> ../../assets/images/imageN.png
IMAGE_PATH_RE = re.compile(r"docs/assets/media-extracted/media/")
# Pandoc emits raw <img> tags with absolute width/height; we convert to markdown
# image syntax so MkDocs resolves the path correctly under directory URLs.
IMG_TAG_RE = re.compile(r'<img\s+([^>]*?)/?>', re.IGNORECASE)
_IMG_SRC_RE = re.compile(r'\bsrc="([^"]+)"')
_IMG_STYLE_RE = re.compile(r'\bstyle="([^"]+)"')
_IMG_ALT_RE = re.compile(r'\balt="([^"]+)"')


def _convert_img_tag(match: re.Match) -> str:
    attrs = match.group(1)
    src_m = _IMG_SRC_RE.search(attrs)
    if not src_m:
        return match.group(0)
    src = src_m.group(1)
    style_m = _IMG_STYLE_RE.search(attrs)
    alt_m = _IMG_ALT_RE.search(attrs)
    out = f"![{alt_m.group(1) if alt_m else ''}]({src})"
    if style_m:
        out += f'{{ style="{style_m.group(1)}" }}'
    return out


def downshift_headings(body: str) -> str:
    """Add one '#' to every ATX heading so H1→H2, H2→H3, etc.

    Leaves headings already at H6 alone (markdown max).
    """
    out_lines = []
    for line in body.splitlines():
        m = re.match(r"^(#{1,5})(\s+)(.*)$", line)
        if m and len(m.group(1)) < 6:
            line = "#" + line
        out_lines.append(line)
    return "\n".join(out_lines)


def trim_body(lines: list[str], deliv: Deliverable) -> list[str]:
    """Drop boundary markers, the Stage-3 preamble line, and the first numbered H1."""
    body = lines[deliv.start_line - 1 : deliv.end_line]

    # Drop leading boundary marker if present.
    while body and (BOUNDARY_RE.match(body[0]) or body[0].strip() == ""):
        if BOUNDARY_RE.match(body[0]):
            body.pop(0)
            break
        body.pop(0)

    # For Stage 3, the title-preamble line **Title** is just BEFORE the boundary
    # and lives in the previous slice. To keep our slices clean, scan back from
    # the start of the body to ensure we didn't leave a stray title-preamble at
    # the END of the previous deliverable's slice. (Handled below in the loop.)

    # Drop the first numbered H1 if present (Stage 1/2 style).
    # Skip blank lines while looking.
    idx = 0
    while idx < len(body) and body[idx].strip() == "":
        idx += 1
    if idx < len(body) and FIRST_H1_RE.match(body[idx]):
        del body[idx]

    # Trim trailing whitespace lines.
    while body and body[-1].strip() == "":
        body.pop()

    return body


def trim_trailing_preamble(body: list[str]) -> list[str]:
    """Drop a trailing **Title** preamble line that belongs to the NEXT deliverable.

    Pandoc placed the Stage-3 deliverable title 1-2 lines before its boundary
    marker, so when we slice by boundary lines the preamble ends up at the
    bottom of the PRECEDING slice.
    """
    while body and body[-1].strip() == "":
        body.pop()
    if body and TITLE_PREAMBLE_RE.match(body[-1]):
        body.pop()
        while body and body[-1].strip() == "":
            body.pop()
    return body


def rewrite_paths(text: str) -> str:
    text = ANCHOR_RE.sub("", text)
    text = IMAGE_PATH_RE.sub("../../assets/images/", text)
    text = IMG_TAG_RE.sub(_convert_img_tag, text)
    return text


def render_deliverable(deliv: Deliverable, body: str) -> str:
    front = (
        "---\n"
        f"title: \"{deliv.title}\"\n"
        f"stage: \"{deliv.stage_label}\"\n"
        f"deliverable_id: {deliv.deliverable_id}\n"
        "status: draft\n"
        f"last_reviewed: {TODAY}\n"
        "---\n\n"
    )
    h1 = f"# {deliv.title}\n\n"
    return front + h1 + body.strip() + "\n"


def main() -> None:
    lines = CONVERTED.read_text().splitlines()
    deliverables = build_deliverables(total_lines=len(lines))

    written = 0
    for deliv in deliverables:
        body_lines = trim_body(lines, deliv)
        body_lines = trim_trailing_preamble(body_lines)
        body_lines = downshift_headings("\n".join(body_lines)).splitlines()
        body = "\n".join(body_lines)
        body = rewrite_paths(body)

        out_path = DOCS / "stages" / deliv.stage_folder / deliv.filename
        out_path.write_text(render_deliverable(deliv, body))
        written += 1
        print(f"wrote {out_path.relative_to(REPO)}  ({deliv.end_line - deliv.start_line + 1} src lines)")

    print(f"\nTotal deliverables written: {written}")


if __name__ == "__main__":
    main()
