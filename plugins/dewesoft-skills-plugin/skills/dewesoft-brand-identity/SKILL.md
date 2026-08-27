---
name: dewesoft-brand-identity
description: >-
  Apply the Dewesoft visual brand identity to every visual deliverable - Word/Google documents
  (.docx) and presentations (.pptx slide decks). Use this skill WHENEVER you create, edit, or
  restyle a document or slide deck for Dewesoft, even if the user never says "brand": triggers
  include "technical offer", "offerta tecnica", "proposal", "report", "datasheet", "quotation",
  "presentation", "deck", "slides", "pitch", "one-pager", "letter", "memo", or any request producing
  a .docx or .pptx to share, send, or publish. ALWAYS consult it for the exact colors, fonts, logo
  rules, terminology, the document layout template (header/footer, heading hierarchy, tables, cover)
  and the slide layout template (black background, orange accent, title pattern, cards) so output
  strictly matches the official Dewesoft templates instead of generic styling. Do NOT use for
  plain-text chat answers, code, or internal notes never exported. Covers EN and IT output.
---

# Dewesoft Brand Identity

Dewesoft is a test & measurement company (DAQ hardware + DewesoftX software). Its identity is built
on three colors - **black, white, and the DS Orange signal color** - with a single typeface family.
Every exported document or slide must look like it came from Dewesoft, not from a generic template.

This skill governs **visual deliverables only**: `.docx` (Word / Google Docs) and `.pptx` (slide
decks), plus any designed graphic. It does not change writing voice or chat answers.

## Non-negotiable rules (apply to every deliverable)

1. **Colors come only from the approved palette.** DS Orange is the single accent; never introduce
   off-brand accent colors into documents. (Slides may use the secondary category palette, see
   `references/slide-template.md`.) Full values: `references/visual-identity.md`.
2. **One typeface: Oswald.** A condensed Google sans — native in Google Docs/Slides; for Office and
   generated `.docx`/`.pptx` set the run/shape font to `Oswald` with fallback `Arial` for
   environments where Oswald is not installed. Never mix in other fonts. Oswald has **no true
   italic** — where italic is called for (captions, descriptions) use a lighter Oswald weight and/or
   DS Silver instead of faux italic. Because Oswald is narrow, give text room: never crowd it against
   separation lines (clear-space rules are in the template references).
3. **Write the company name as "Dewesoft" in body text** - regular weight, only the first letter
   capitalized. The all-caps `DEWESoft` styling and the ® symbol belong to the **logo graphic only**,
   never to running text. Same for products: write KRYPTON, SIRIUS, DSI, DS-NET, DewesoftX without ®
   in text.
4. **The brandmark is the 3-part orange triangle.** On light backgrounds use logo Type A (orange
   mark, dark text); on dark backgrounds Type B (orange mark, white text). Keep clear space around it.
   **Use the ready-made files in `assets/logo/`** — inline the **SVG** for HTML/PDF pipelines, embed
   the transparent **PNG** for `.docx`/`.pptx`; never redraw the mark or re-typeset the wordmark.
   Selection, aspect ratios and embedding details: `references/visual-identity.md` §3.
5. **Match the official template, do not improvise layout.** Documents follow
   `references/document-template.md`; slides follow `references/slide-template.md`. These are derived
   from real Dewesoft deliverables and are the source of truth for structure.
6. **Never invent facts or specs.** When stating product numbers, cite the source (Dewesoft web page
   / techref / the brand guidelines PDF in `assets/`). If a value is unknown, leave a clearly marked
   placeholder rather than guessing.

## Workflow

Before producing anything, read the right references, then build with the matching public skill.

1. **Always read** `references/visual-identity.md` first (colors, fonts, logo, terminology).
2. **If the deliverable is a document** (.docx, "Word doc", "Google Doc", technical offer, report,
   proposal, letter): read `references/document-template.md`, then read
   `/mnt/skills/public/docx/SKILL.md` for the mechanics and generate the file.
3. **If the deliverable is a deck** (.pptx, slides, presentation): read
   `references/slide-template.md`, then read `/mnt/skills/public/pptx/SKILL.md` and generate.
4. **Verify against the checklist** at the bottom of each template reference before delivering.

## Default metadata

Unless the user overrides them, these are the house defaults for Dewesoft Italy deliverables:

- **Entity / address line:** `Dewesoft SRL - via Sant'Arcangelo di Romagna 62 00127 Roma`
- **Document author (Change Log / footer):** the requesting user; example deliverables used
  `Alberto Boffi`.
- **Versioning label:** `VERSIONE: Vx-y` on the cover, e.g. `V1-1`.
- **Draft state:** while not final, show a diagonal `DRAFT` watermark (see document template).

## Quick palette reference (full detail in references/visual-identity.md)

| Token | HEX | Use |
|---|---|---|
| DS Orange | `#F15D2D` | accent: H2 headings, key titles, logo mark, badges, highlights |
| DS Black | `#232323` | primary dark text, H1 headings, dark backgrounds |
| DS Graphite | `#404040` | secondary dark, sub-headings, dark cards |
| DS Silver | `#A7A7A7` | muted/secondary text, captions, address line |
| Black | `#000000` | slide backgrounds |
| White | `#FFFFFF` | text on dark, document body background |

## Bundled source

`assets/dewesoft-brand-identity-guidelines.pdf` is the official brand manual (Ver. 1.0, Jan 2018).
Open it for exact color specs (Pantone/RAL/CMYK), logo construction geometry, and margin rules when
a deliverable needs precise reproduction or you must cite the source.

`assets/logo/` holds the **ready-to-use logo artwork** (vectorised from the manual): `dewesoft_logo`
(Type A, light bg), `dewesoft_logo_dark` (Type B, dark bg) and `dewesoft_mark` (brandmark only), each
as **SVG** (for HTML/PDF) and transparent **PNG** (for `.docx`/`.pptx`). Embed these instead of the
PDF preview or any cropped raster. Usage rules: `references/visual-identity.md` §3.
