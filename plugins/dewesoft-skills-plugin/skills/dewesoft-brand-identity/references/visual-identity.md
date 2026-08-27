# Visual Identity — colors, typography, logo, terminology

Source: *Dewesoft Brand Identity Guidelines*, Ver. 1.0, January 2018 (bundled in `../assets/`).

---

## 1. Color palette

The brand rests on three colors — **black, white, and DS Orange** (the "signal" color). DS Orange
placed on black or white is the core motif. Graphite and Silver are neutral support tones.

| Name | HEX | RGB | Print refs | Role |
|---|---|---|---|---|
| **DS Orange** | `#F15D2D` | 241, 93, 45 | Pantone 1655C · RAL 2004 · CMYK 0/79/92/0 | The one accent. Logo mark, key titles, H2 headings, badges, links/cross-refs, highlights. |
| **DS Black** | `#232323` | 35, 35, 35 | Pantone 7C · CMYK 71/65/64/72 | Primary text, H1 headings, dark document accents, dark slide background. |
| **DS Graphite** | `#404040` | 64, 64, 64 | CMYK 68/61/60/47 | Secondary dark: sub-headings, dark cards, dividers. |
| **DS Silver** | `#A7A7A7` | 167, 167, 167 | CMYK 36/29/30/0 | Muted text: captions, header address line, secondary slide text. |
| **Black** | `#000000` | 0, 0, 0 | CMYK 0/0/0/100 | Pure-black slide backgrounds. |
| **White** | `#FFFFFF` | 255, 255, 255 | — | Document page background; text on dark. |

**Derived tints (for table fills / subtle bands), use sparingly:**
- DS Orange very-light band (spec-table section headers): `#FBE4D5`
- DS Orange light (callout fills): `#F8CBAD`

**Rule:** in documents, orange is the *only* accent. Do not add blues/greens as decoration. (Slides
have a defined secondary category palette — see `slide-template.md` — but black/white/orange still
dominate.)

---

## 2. Typography

- **Primary and only typeface: Oswald.** A condensed sans-serif (Google Fonts). Weights available:
  Light, Regular, Medium, SemiBold, Bold. Native in Google Docs/Slides; for Office and generated
  `.docx`/`.pptx`, set the run/shape font to **`Oswald`** with **`Arial`** declared as fallback for
  environments where Oswald is not installed. Never mix in other fonts.
- **Make the name stick (.docx):** Oswald isn't installed on most generators, so setting it on a few
  runs isn't enough — unstyled text falls back to Calibri (and Google Docs then shows Calibri too).
  Set the literal name `Oswald` on the **document defaults**, the **Normal** style, **every**
  heading/table/list style **and** every run (rFonts `ascii`+`hAnsi`+`cs`). `Arial` is a fallback name
  only — never a run's real font. Mechanics: `document-template.md` §0.1.
- **No italics:** Oswald has no true italic. Where the templates ask for italic (figure captions,
  card descriptions), substitute **Oswald Light and/or DS Silver color** for the same secondary
  effect — never apply faux/synthetic italic.
- **Condensed → mind the spacing:** Oswald is narrow and tall, so give text room to breathe. Body
  line spacing **≥ 1.5**, comfortable paragraph spacing, and always keep clear space between any
  separation line (header/footer rules, table rules, dividers) and adjacent text — see the clear-space
  rules in `document-template.md` / `slide-template.md`. Avoid very small body sizes; size body up
  slightly versus a normal-width font.
- **Weight usage:**
  - Document H1 → Bold. Document H2 → Bold (orange). Sub-headings → SemiBold.
  - Slide titles → Bold. Body → Regular. Captions/notes → Light + DS Silver.
- **Logo wordmark:** the `DEWESoft` lockup is fixed artwork — embed a ready-made file from
  `../assets/logo/` (see §3), do **not** recreate or re-typeset the wordmark in Oswald.

---

## 3. Logo & brandmark

- **Brandmark:** the 3-part triangle (three solid triangles separated by white gaps) in **DS Orange**.
  Symbolises Customers, Partners, Team members. Constructed from a 1:4 ellipse rotated 0°/60°/-60°,
  inner gaps = x/10. Reproduce, do not redraw freehand.
- **Primary logo (horizontal lockup):** brandmark + `DEWESoft` wordmark + `measurement innovation`
  tagline, side by side.
  - **Type A — light background:** brandmark DS Orange, wordmark + tagline **black/DS Black**.
  - **Type B — dark background:** brandmark DS Orange, wordmark + tagline **white**.
- **Vertical lockup:** brandmark centered on top, wordmark centered beneath. Same color rules.
- **Clear space / margins:**
  - Horizontal lockup: empty space = ½ brandmark height (top/bottom) and ½ brandmark width (sides).
  - Vertical lockup: empty space = ¼ brandmark height all around.
- **® symbol:** part of the logo graphic; present in the lockup, **never** in running text.
- Placement convention in deliverables: **top-right** of document headers (Type A) and slide masters
  (Type B). On a co-branded deck, partner logo sits next to the Dewesoft logo top-left of title slides.

### Logo files — use these (in `../assets/logo/`)

Ready-to-use official artwork, vectorised from the brand-guidelines master. **Always embed one of
these files; never re-typeset the wordmark or redraw the mark.**

| File | When to use | Contents |
|---|---|---|
| `dewesoft_logo.svg` / `.png` | **Light** background — Type A | mark (orange) + `DEWESoft®` + tagline, text in DS Black `#232323` |
| `dewesoft_logo_dark.svg` / `.png` | **Dark** background — Type B | same lockup, text in **White** |
| `dewesoft_mark.svg` / `.png` | mark only (small slide corner, watermark, favicon) | 3-part orange brandmark, transparent gaps |

**Aspect ratios (lock them — scale by _height_, never distort):** horizontal lockup ≈ **5.26 : 1**
(W:H); mark ≈ **1.12 : 1**.

**Which format to embed:**
- **HTML → PDF pipelines** (designed one-pagers, pamphlets, anything rendered via headless Chromium):
  inline the **SVG** straight into the markup and size it with CSS `height` + `width:auto`. Crispest
  result, zero raster border. Pattern:
  `<span class="logo">…inline &lt;svg&gt;…</span>` with
  `.logo svg{ height:13mm; width:auto; display:block; }`.
- **Generated `.docx` / `.pptx`** (python-docx / python-pptx embed raster pictures): use the **PNG**
  (transparent — 1600 px wide lockup, 600 px mark). Insert at the document-header top-right (Type A)
  or the slide master (Type B); set the picture **height** and let width auto-scale. **Embed inline —
  never floated/anchored — and check the width fits its container** (height × 5.25 ≤ container width)
  so the lockup is never clipped; concrete safe sizes for documents are in `document-template.md` §0.3.
- The mark's gaps are **transparent**: on a dark surface they correctly show the dark background
  (the Type B look). Never fill them.

**Color:** the artwork is fixed to the official **DS Orange `#F15D2D`**. (The manual's embedded raster
preview renders a slightly different orange — always trust `#F15D2D`.)

---

## 4. Terminology & trademark usage (EN + IT)

**Company name in text:** `Dewesoft` (regular weight, first letter capital only). Never `DEWESoft`,
`DEWESOFT`, or `dewesoft` in prose. The legal entity in Italy is `Dewesoft SRL`.

**Registered names — no ® in text, ® only in logos/graphics:**
KRYPTON, SIRIUS, DSI, DS-NET (product families); DualCoreADC, SuperCounter, GrandView (technologies).
Software: `DewesoftX` (one word, capital D and X). Historian, DewesoftM as written.

**Casing for products in text:** product family names in CAPS as branded (KRYPTON, SIRIUS), model
codes verbatim (e.g. `KRYPTON-1XCNT`, `KRYPTONi-1XSTG`, `SIRIUS-R8DB`).

**Bilingual labels (use IT for Italian deliverables, EN otherwise):**

| EN | IT |
|---|---|
| Version | VERSIONE |
| Table of Contents | Indice |
| Reference and Applicable Documents | Documenti di Riferimento e Applicabili |
| Customer Request | Richiesta del Cliente |
| Proposed System Architecture | Architettura di Sistema Proposta |
| Hardware & Software | Hardware & Software |
| Change Log | Storico delle Modifiche |
| Company Confidential | Riservato Aziendale |
| Draft | Bozza |

**Tone of brand copy (when wording is needed):** confident, customer-first, "measurement innovation".
Brand pillars: robust yet simple; best-in-class T&M; on-the-ground global support. Do not overclaim
specs — cite sources.
