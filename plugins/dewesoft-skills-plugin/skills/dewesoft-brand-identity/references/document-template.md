# Document Template (.docx / Google Doc)

The Dewesoft document look is derived from the **Technical Offer** deliverable. Reproduce this
**layout and design** exactly; the *content* changes per document. Read together with
`visual-identity.md` and `/mnt/skills/public/docx/SKILL.md`.

Page: A4, portrait. Margins ~2 cm. Body font **Oswald** — set the literal font name `Oswald` (declare
`Arial` only as a *fallback name* for machines without Oswald; never set a run's real font to Arial),
**~11–12 pt** (Oswald is condensed — size up slightly for legibility), **justified**, **line spacing
1.5** with **12 pt space after** each paragraph (raised from 6 pt). Body color DS Black `#232323`.

> **Read §0 first.** Fonts, spacing, logo placement and heading-numbering are governed by the
> *Global mechanics* block in §0 below; the per-section specs reference it rather than repeat it.

> **Clear-space principle (applies everywhere):** no horizontal rule ever touches text. Keep a
> minimum gap of **6 pt between text and a rule**, and **8–10 pt between a rule and the next block of
> text**. This matters more than usual because Oswald is tall and narrow.

---

## 0. Global mechanics — fonts, spacing, logo, numbering

These four rules fix the recurring problems. Apply them via **styles** (not just ad-hoc per run) so
they survive being opened and re-edited in Google Docs.

### 0.1 Font — making Oswald actually render
Oswald is a Google font and is **not installed** on most `.docx` generators or in desktop Word, so
any run or style left at the default silently falls back to Calibri. Because these documents are
finalised in **Google Docs** (where Oswald is native), the fix is to write the literal name `Oswald`
onto **everything**, never to rely on the font being installed:

- Set `Oswald` on the **document defaults** (`w:docDefaults`), on the **Normal** style, and on **every
  style the file uses** — `Heading 1–4`, `Title`, `Subtitle`, `Caption`, `Header`, `Footer`, table
  styles, list styles.
- Set it on **every run** too, writing the `w:rFonts` attributes `w:ascii`, `w:hAnsi` **and** `w:cs`
  all to `Oswald`. python-docx's `run.font.name` only sets ascii/hAnsi — set `w:cs` via the XML
  element or complex-script text stays Calibri.
- `Arial` is a **fallback name only** — never set a run's actual font to Arial.
- Optional (desktop-Word fidelity only): embed the Oswald TTF. Not required for Google Docs.
- **Verify:** after building, grep the document XML for stray `w:ascii="Calibri"` / `Aptos` / `Times`
  and fix every hit; nothing but `Oswald` should remain.

### 0.2 Spacing scale (raised ≥ 50 % for breathing room)
Oswald is tall and narrow and the old defaults felt cramped. Use these **explicit** before/after
values (each ≈ 1.5–2× the previous setting); do **not** let the generator fall back to its compact
defaults. Set them as paragraph-format `space_before` / `space_after` on the matching **style**.

| Element | Space before | Space after | Notes |
|---|---|---|---|
| Cover title → subtitle | — | **≥ 24 pt** gap | was one line; ≥ +50 % air between them |
| Cover subtitle → version | — | **≥ 18 pt** gap | |
| H1 | new page *or* **30 pt** | **18 pt** | |
| H2 | **24 pt** | **12 pt** | |
| H3 | **18 pt** | **10 pt** | |
| H4 | **14 pt** | **8 pt** | |
| Body paragraph | 0 | **12 pt** | raised from 6 pt; line spacing stays **1.5** |
| List item | 0 | **6 pt** | between items |

### 0.3 Logo placement — keep it fully visible (header + cover)
The lockup PNG is **1600 × 305 px → aspect ratio 5.25 : 1 (W : H)**. Clipping happens when the image
is (a) floated/anchored with absolute positioning, or (b) sized too wide for its container so it
crosses the page margin. Always:

- Embed the logo **inline** (`add_picture` inside a paragraph or table cell). **Never** float / anchor
  / place it "in front of text".
- **Scale by height only**; width follows the locked ratio (width = height × 5.25). Never set width
  and height independently — that distorts or overflows.
- **Check it fits:** required width = chosen height × 5.25 must be **≤ the container width** (the
  header-right cell, or the page usable width on the cover). If not, reduce the height.
- A4 usable width at 2 cm margins = **170 mm**.

Concrete safe sizes:
- **Header (Type A, light bg):** height **10 mm → width 52.5 mm**. Put it in the **right cell of a
  borderless 2-column header table**, **right-aligned**, right cell width **≥ 60 mm**, table autofit
  **off** (fixed layout) so the cell can't collapse. Set **top margin + header distance ≥ 16 mm** so
  the lockup is never clipped by the page top or overlapped by body text.
- **Cover (Type A):** height **16 mm → width 84 mm** (well under 170 mm). Place it in its **own** top
  paragraph of the title block — *not* overlapping the confidential badge or the circuit graphic —
  left-aligned or centered, with ≥ ½-mark-height clear space below it before the title.

### 0.4 Heading numbering — OFF
Generate **all headings as plain text with no numbers** (`Section Title`, not `1. Section Title`). Do
**not** apply Word auto-numbering or attach a multilevel list to the heading styles. Section numbers
and the numbered TOC are added later in **Google Docs via Apps Script**, so the `.docx` must ship
unnumbered — any pre-baked numbers would collide with that step.

---

## 1. Cover page

- **Decorative PCB / circuit-line graphic** in very light grey (`#EAEAEA`) flowing across top and
  bottom of the page — subtle, behind the title block. (Use a light background image/vector; if
  unavailable, omit rather than substitute another motif.)
- **Diagonal `DRAFT` watermark** (light grey, ~45°, large) when the document is not final.
- **"COMPANY CONFIDENTIAL" badge:** white **bold** text on a DS Orange (`#F15D2D`) rounded rectangle,
  upper-left of the title block. (IT: `RISERVATO AZIENDALE`.)
- **Logo (Type A):** inline at the top of the title block, **height 16 mm** (≈ 84 mm wide), **not
  floated** and not overlapping the badge or circuit graphic — see §0.3. Clear space below it before
  the title.
- **Main title:** project / document code in **large DS Orange bold**, e.g. `PROJECT DS-OGI01`.
- **Subtitle:** document type in **DS Black bold**, smaller, e.g. `Technical Offer`. Keep **≥ 24 pt**
  between the title and the subtitle (§0.2).
- **Version line:** small grey text, `VERSIONE: V1-1`, with **≥ 18 pt** above it.

No running header/footer on the cover.

---

## 2. Running header (every content page)

Two-zone header with a thin horizontal rule beneath it:

- **Left:** document title string in small **bold** DS Black, e.g.
  `PROJECT DS-OGI01 - Technical Offer V1-1`; directly below it the entity/address line in smaller
  **DS Silver** `#A7A7A7`: `Dewesoft SRL - via Sant'Arcangelo di Romagna 62 00127 Roma`.
- **Right:** Dewesoft **horizontal logo, Type A** (orange mark + dark `DEWESoft®` wordmark) on white —
  embedded **inline** in the right cell, **right-aligned**, **height 10 mm → width 52.5 mm**, right
  cell width **≥ 60 mm**, table autofit off. **Never floated/anchored.** This is the #1 cause of the
  logo being clipped, so follow the fit check in §0.3 exactly.
- Thin rule (`#A7A7A7`, ~0.5 pt) spanning the text width under the header. Leave **≥ 6 pt clear space
  between the header text and the rule**, and **≥ 8–10 pt between the rule and the first body line**.

---

## 3. Running footer (every content page)

Thin horizontal rule above (`#A7A7A7`, ~0.5 pt), then two zones. Leave **≥ 8–10 pt between the last
body line and the rule**, and **≥ 6 pt between the rule and the footer text**:

- **Left:** the same document title string, small, DS Black/Graphite.
- **Right:** page number as `current/total`, e.g. `7/20`.

---

## 4. Heading hierarchy (unnumbered, multilevel)

**Headings carry no numbers** (§0.4) — numbering is applied later in Google Docs. Patterns below are
plain text.

| Level | Pattern (plain text) | Style |
|---|---|---|
| **H1** | `Section Title` | Large (~20–22 pt), **Bold**, **DS Black** `#232323`. New page or 30 pt before, 18 pt after. |
| **H2** | `Subsection` | Medium (~14 pt), **Bold**, **DS Orange** `#F15D2D`. 24 pt before, 12 pt after. |
| **H3** | `Sub-subsection` | (~12 pt), **Bold**, **DS Graphite** `#404040`. 18 pt before, 10 pt after. |
| **H4** | `Deep heading` | (~11 pt), **Bold**, DS Graphite; may be underlined. 14 pt before, 8 pt after. |

Do **not** auto-number the levels and do **not** attach a multilevel list to the heading styles. The
orange H2 is the signature visual cue of a Dewesoft document — keep it.

---

## 5. Table of Contents

- Title `Table of Contents` (H1, **no number**). (IT: `Indice`.)
- Entries with **dotted leader lines** to right-aligned page numbers.
- TOC entries are hyperlinks: standard **blue underlined** link styling is acceptable for the TOC;
  deeper levels indented.
- Section numbers are added later in Google Docs, so the `.docx` TOC ships **without** leading numbers
  and will be regenerated (with numbers) in Google Docs after the Apps Script numbering runs.

---

## 6. Tables — two approved styles

**Style A — clean line table** (change logs, reference lists, requirements, value tables):
- Header row: **bold** labels, single rule **under** the header row, with **≥ 4–6 pt cell padding
  above and below the rule** so text never touches the line.
- Body rows separated by thin horizontal rules; **no vertical borders**. Use comfortable row height
  with **≥ 4–6 pt top/bottom cell padding** so the condensed Oswald text stays clearly off the rules.
- Generous cell padding. Bold key terms inside requirement text.
- Example column sets:
  - Change Log → `Date | Changed By | Release | Description`
  - Reference Documents → `Doc ID | Titolo | Release | Description`
  - Requirements → `REQ Code | Text | Notes` (codes like `REQ-FUN-010`)
  - Values → `Sub-assembly | Torque [Nm]`

**Style B — spec table** (product/technical specifications):
- **Full grid**, thin grey borders.
- **Section-header bands:** rows that introduce a spec group (e.g. `Counter`, `Analog input`,
  `Voltage Mode`, `Current Mode`, `Power`, `Physical`) span the full width and are filled with the
  light orange tint **`#FBE4D5`**, label in **bold** DS Black.
- Two-column `Parameter | Value` beneath each band; multi-range specs may use extra value columns.

---

## 7. Body conventions

- **Bulleted lists:** round bullets; bold the lead term, then the explanation
  (e.g. **Modular design**: …).
- **Cross-references / internal links:** DS Orange, e.g. references to a `REQ-…` code or a section.
- **Figure captions:** centered, **Oswald Light + DS Silver** (Oswald has no italic), e.g.
  *(a) Frontal view …*.
- **Inline emphasis:** bold for key terms; reserve orange for headings/links, not random words.
- **Hardware tables** that list products include a `Link` column to the Dewesoft product page
  (cite the real URL; never fabricate).

---

## Pre-delivery checklist

- [ ] **Font:** `Oswald` on document defaults, Normal, all heading/table styles **and** every run (rFonts ascii+hAnsi+cs); no stray Calibri/Aptos/Times in the XML.
- [ ] **Spacing (raised ≥50 %):** applied via styles — H1 30/18, H2 24/12, H3 18/10, H4 14/8, body 12 pt after @1.5; cover title→subtitle ≥24 pt.
- [ ] **Logo fully visible:** inline (never floated), scaled by height only @5.25:1 — header 10 mm (right cell ≥60 mm), cover 16 mm (≤170 mm); top margin + header distance ≥16 mm.
- [ ] Cover: orange code title, dark subtitle, version line, confidential badge, DRAFT watermark if not final.
- [ ] Header on every page: left title + silver address line; right Type A logo; rule beneath.
- [ ] Footer on every page: title left, `page/total` right; rule above.
- [ ] **Headings unnumbered** (plain text — no auto-numbering / multilevel list); numbers added later in Google Docs.
- [ ] Body justified, **Oswald**, ~11–12 pt, 1.5 spacing + **12 pt after**, DS Black.
- [ ] No rule touches text: ≥6 pt text→rule, ≥8–10 pt rule→next block; table cells padded ≥4–6 pt.
- [ ] Tables use Style A or Style B correctly; spec bands `#FBE4D5`.
- [ ] Orange is the only accent; "Dewesoft" cased correctly; no ® in text.
- [ ] Every stated spec/figure has a cited source; placeholders marked, nothing invented.
