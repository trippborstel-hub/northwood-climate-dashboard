# Northwood Capital — Brand Identity

CONFIDENTIAL -- Northwood Capital

---

## Wordmark

The Northwood Capital wordmark is the primary brand element. "NORTHWOOD" is set in all-caps spaced tracking; "CAPITAL" sits below in lighter weight with wider letter-spacing. A geometric ridge mark (stylized peak) precedes the name in the horizontal lockup.

### Files

| Asset | File | Use |
|---|---|---|
| Primary wordmark (dark) | `wordmark.svg` | Light backgrounds |
| Primary wordmark (light) | `wordmark-light.svg` | Dark backgrounds, navy fields |
| Icon only | `icon.svg` | Favicon, small formats, app icons |

### Clear Space

Minimum clear space around the wordmark equals the cap-height of the "R" in NORTHWOOD on all sides.

### Minimum Size

- Digital: 120px wide minimum
- Print: 1.5 inches wide minimum

---

## Color Palette

### Primary

| Color | Hex | RGB | Use |
|---|---|---|---|
| Northwood Navy | `#1A2744` | 26, 39, 68 | Primary brand color, wordmark, headers, backgrounds |
| Northwood Slate | `#3D5A80` | 61, 90, 128 | Secondary text, supporting elements |

### Secondary

| Color | Hex | RGB | Use |
|---|---|---|---|
| Warm Gray | `#8B8680` | 139, 134, 128 | Body text, secondary labels |
| Light Gray | `#E8E6E3` | 232, 230, 227 | Backgrounds, table alternating rows, dividers |
| Off-White | `#F7F6F4` | 247, 246, 244 | Page backgrounds, light panels |

### Accent

| Color | Hex | RGB | Use |
|---|---|---|---|
| Copper | `#A67C52` | 166, 124, 82 | Accent lines, key data highlights, select borders |
| Copper Light | `#C9A87C` | 201, 168, 124 | Hover states, secondary accent |

### Status

| Color | Hex | Use |
|---|---|---|
| Green | `#2D6A4F` | RAG Green, positive variance |
| Amber | `#B8860B` | RAG Amber, monitoring |
| Red | `#9B2226` | RAG Red, negative variance, alerts |

---

## Typography

### Primary Typeface

**Georgia** (serif) — Headers, titles, wordmark text in documents.

Georgia is available on all systems and conveys institutional authority without requiring custom font licensing.

### Secondary Typeface

**Inter** or **system-ui sans-serif** — Body text, tables, data, captions.

### Hierarchy

| Element | Font | Weight | Size | Tracking |
|---|---|---|---|---|
| H1 (document title) | Georgia | Bold | 28px / 2.0em | Normal |
| H2 (section header) | Georgia | Bold | 20px / 1.4em | Normal |
| H3 (subsection) | Inter / sans-serif | Semibold | 16px / 1.15em | Normal |
| Body | Inter / sans-serif | Regular | 14px / 1.0em | Normal |
| Table header | Inter / sans-serif | Semibold | 13px | +0.02em |
| Table body | Inter / sans-serif | Regular | 13px | Normal |
| Caption / footer | Inter / sans-serif | Regular | 11px | +0.01em |
| Data callout | Georgia | Bold | 36px | -0.01em |

---

## Design System (HTML Deliverables)

When generating print-ready or presentation HTML (board decks, LP reports, comp analyses), apply these specifications.

### Page Layout

- Max content width: 960px
- Page margins: 48px
- Section spacing: 32px
- Background: `#F7F6F4` (off-white)
- Content panels: `#FFFFFF` with 1px `#E8E6E3` border, 8px border-radius

### Header Bar

- Height: 64px
- Background: `#1A2744` (Northwood Navy)
- Text: white, Georgia, 18px
- Copper accent line: 3px `#A67C52` bottom border

### Tables

- Header row: `#1A2744` background, white text
- Alternating rows: `#FFFFFF` / `#F7F6F4`
- Cell padding: 10px 16px
- Border: 1px `#E8E6E3`
- Numerical columns: right-aligned, tabular-nums

### Footer

- Text: "CONFIDENTIAL -- Northwood Capital"
- Font: 10px Inter, `#8B8680`
- Centered, with 1px `#E8E6E3` top border
- 24px top margin

---

## Usage Rules

1. **Do not stretch, rotate, or recolor** the wordmark.
2. **Do not place the wordmark on busy backgrounds.** Use solid navy or solid white/off-white fields.
3. **Copper is an accent, not a primary.** Use it for lines, borders, and small highlights. Never for large background fills.
4. **Status colors are functional only.** Green/Amber/Red are for RAG ratings and data indicators. Never decorative.
5. **Maintain contrast ratios.** Navy text on white meets WCAG AAA. White text on navy meets WCAG AAA. Do not use light gray text on white backgrounds.
