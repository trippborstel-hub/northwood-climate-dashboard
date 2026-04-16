# Northwood Capital — IC Memo Production Methodology

**Reference Document — Read-Only**
**Last Updated: March 2026**

---

## Overview

This document codifies the end-to-end process for producing an Investment Committee memorandum — from deal folder data through markdown draft, LBO model integration, QA protocol, and HTML rendering. It captures the dependency chain, cross-reference map, and design decisions learned from the Project Everest IC memo build. Use this as the scaffold for every future IC memo.

**Template:** `_reference/ic-memo-template.md` — section-by-section content requirements
**QA Protocol:** `_reference/qa-protocol.md` — four-check validation
**Deliverable Standards:** `_reference/deliverable-standards.md` — formatting, HTML design system
**LBO Model:** `_reference/lbo-model-methodology.md` — returns analysis engine

---

## Production Workflow

### Phase 1: Source Material Assembly

Before writing a single line, read the entire deal folder. Every file is a potential source.

**Required inputs (in dependency order):**

| Source | Location | What It Provides |
|---|---|---|
| CIM | `pipeline/active/project-{codename}/02-preliminary/cim.md` | Company overview, financials, market, management, customer data |
| Management meeting notes | `pipeline/active/project-{codename}/02-preliminary/management-notes.md` | On-site assessments, management quality, facility observations |
| Screening memo | `pipeline/active/project-{codename}/03-ic-materials/screening-memo.md` | Initial risk flags, thesis framing, auto-pass check results |
| LOI terms | `pipeline/active/project-{codename}/05-execution/loi-terms.md` | Entry price, leverage, structure, timeline, DD workstreams |
| LBO model summary | `pipeline/active/project-{codename}/06-model/model-summary.md` | Computed returns, sensitivities, scenarios |
| LBO model output | `pipeline/active/project-{codename}/06-model/model-output.html` | Detailed model tables (if model has been parameterized) |
| Deal status | `pipeline/active/project-{codename}/deal-status.md` | Current stage, key dates, team assignments |
| Data spine | Supabase `northwood_capital` schema | Canonical entity values, LBO assumptions |
| Investment thesis | `_reference/investment-thesis.md` | Firm strategy, sector focus, return targets |
| Screening criteria | `_reference/screening-criteria.md` | Pass/flag criteria (inform risk section) |
| Risk framework | `_reference/risk-framework.md` | Risk categories, severity definitions |

**Critical dependency:** If the LBO model has been parameterized (i.e., `lbo_assumptions` exists in the data spine), the IC memo MUST use computed model numbers, not hand-estimated returns. The model is the source of truth for all returns, sensitivities, and scenario analysis once it exists.

### Phase 2: Markdown Draft

Write the IC memo per `_reference/ic-memo-template.md`. All 11 sections are mandatory. Key principles:

1. **Rewrite, don't regurgitate.** The CIM is a banker document. The IC memo is Northwood's analytical document. Same data, different voice — direct, adversarial, conclusion-first.

2. **Every number has a source.** Label assumptions per QA protocol: Hard Data / Management Guidance / Firm Estimate / Aspirational. Use `[RC Assumption — ...]` tags for firm estimates.

3. **Thesis pillars are testable claims.** Each pillar follows the structure: What we believe / Evidence / Why we're right / Value creation mechanism / Key assumption to monitor. If a pillar can't be validated or invalidated, it's an assertion, not a thesis.

4. **Returns from model, not from hand calculation.** If the model exists, pull exact numbers. If it doesn't exist yet, use conservative hand estimates and flag them — the memo will require a v2.0 update once the model is parameterized.

### Phase 3: LBO Model Integration

When the computed model produces different numbers than the IC memo's initial estimates, update the memo. This is the v1 → v2 transition.

**Root cause of differences:** The parameterized model typically differs from hand estimates because:
- D&A tax shield reduces cash taxes ($EBITDA × D&A% × tax rate per year)
- Compounding effect of accelerated deleveraging (lower debt → lower interest → more FCF → faster paydown)
- Precise amortization and cash sweep mechanics vs. simplified annual estimates

**Sections requiring updates (cross-reference map):**

| Section | What Changes | How to Find It |
|---|---|---|
| **1. Executive Summary** | Base/upside/downside IRR and MOIC | Search for "Base Case Returns", "Upside Case Returns", "Downside Case Returns" |
| **1. Note on base case** | Returns vs. hurdle discussion | Search for "below Northwood's 20%+" |
| **5. Thesis Pillar 1** | Debt paydown projection | Search for "projected $XXM over 5 years" |
| **5. Thesis Pillar 3** | Upside returns reference (if cited) | Search for upside IRR/MOIC in thesis context |
| **6.5 Value Creation Bridge** | EBITDA growth %, deleveraging %, multiple expansion % | The entire bridge table — replace with model output |
| **7.2 Leverage context** | Downside coverage ratio | Search for "coverage falls to" |
| **8.1 Three-Case Returns** | Full returns table: exit debt, exit equity, IRR, MOIC | The entire Section 8.1 table |
| **8.1 Case descriptions** | Narrative text referencing specific returns | Paragraphs below the returns table |
| **8.1 Fund hurdle note** | Returns vs. hurdle numbers | Search for "below Northwood's 20%+" in Section 8 |
| **8.2 Sensitivity** | Full MOIC matrix | The entire sensitivity table — replace with model output |
| **8.3 Value Creation Attribution** | MOIC contribution breakdown | The entire attribution table |
| **9. Risk 1 residual** | Downside returns in risk context | Search for "reduces returns to X.Xx / X%" |
| **11. Recommendation** | Returns references in thesis summary and hurdle discussion | Two locations: "organic-only base case" and "upside case" |
| **QA Summary** | Structural consistency check — returns cross-reference | Search for "Returns (XX% / X.Xx base)" |
| **Revision History** | Add v2.0 entry | Bottom of document |

**Total edit locations:** ~15 targeted edits across 10 sections. Use Edit tool with exact string matching — do not rewrite full sections.

### Phase 4: QA Protocol

Run the four-check protocol per `_reference/qa-protocol.md`:

1. **Source Verification** — Every figure traced to CIM, management call, model output, or firm estimate. No unsourced claims.
2. **Structural Consistency** — Returns match across Sections 1, 5, 6.5, 8, 9, 11, and QA Summary. Entry terms match across Sections 1, 7, and 8. Every number that appears in multiple places is identical.
3. **Adversarial Review** — Thesis stress-tested. Downside is genuinely painful (not "slightly below plan"). Base case doesn't require every pillar to work.
4. **Assumption Flagging** — Every forward-looking number carries a category label. Exit multiple assumption sourced to comparable transactions.

### Phase 5: HTML Rendering

Generate a self-contained HTML file per `_reference/deliverable-standards.md`. The HTML rendering is the board-ready version.

**Output location:** `outputs/ic-memos/ic-memo-project-{codename}-{date}-v{#}.html`

---

## HTML Design System for IC Memos

### Base Layout

```css
body {
    max-width: 1100px;
    margin: 0 auto;
    padding: 40px 60px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: #1a1a1a;
    background: #ffffff;
}
```

Font loaded via: `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">`

### Components

#### 1. Coversheet (Dark Header)

Full-width dark block (`#1B2A3D`) with:
- Firm name in uppercase tracking (`NORTHWOOD CAPITAL PARTNERS — INVESTMENT COMMITTEE MEMORANDUM`)
- Project codename as H1 (28px, 700, white)
- Company name as subtitle (18px, 400, `#94a3b8`)
- Two-column grid of deal metadata (Date, IC Meeting, Deal Lead, Deal Team, Fund, Classification)
- PROCEED/PASS/DEFER badge — green (`#166534` bg) for PROCEED, red for PASS
- Confidential notice

```html
<div style="background: #1B2A3D; color: #fff; padding: 50px 60px 40px; margin: -40px -60px 40px;">
    <!-- coversheet content -->
</div>
```

#### 2. Metric Callout Cards

Four cards in a flex row for the Executive Summary. Each card:
- `background: #f8f9fa`
- `border-left: 4px solid #0D6EAA`
- Label: 12px, uppercase, `#555`
- Value: 32px, 700, `#1B2A3D`
- Subtitle: 13px, `#555`

```html
<div style="display: flex; gap: 20px; margin: 25px 0; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 200px; background: #f8f9fa; border-left: 4px solid #0D6EAA; padding: 16px 20px;">
        <div style="font-size: 12px; color: #555; text-transform: uppercase;">Enterprise Value</div>
        <div style="font-size: 32px; font-weight: 700; color: #1B2A3D;">$155.0M</div>
        <div style="font-size: 13px; color: #555;">8.6x LTM Adj. EBITDA</div>
    </div>
    <!-- 3 more cards: LTM EBITDA, Base Case Returns, Entry Leverage -->
</div>
```

Standard 4-card set for IC memos:
| Card | Primary | Secondary |
|---|---|---|
| Enterprise Value | $EV | X.Xx LTM Adj. EBITDA |
| LTM Adj. EBITDA | $EBITDA | X.X% margin |
| Base Case Returns | ~XX% / X.Xx | IRR / MOIC — X-year hold |
| Entry Leverage | X.Xx | $XX.XM Senior Term Loan |

#### 3. Tables

Standard deliverable-standards.md table styling:
- Header: `#1B2A3D` background, white text, 13px, 600
- Body: 13px, 400, `#1a1a1a`
- Borders: `1px solid #dee2e6`
- Alternating rows: `#f8f9fa`
- Numeric columns: `text-align: right; font-variant-numeric: tabular-nums;`

**Highlighted rows** (for totals, key metrics): `background: #e8eef4; font-weight: 600;`

#### 4. Sensitivity Matrix

Standard table with one highlighted cell for the base case intersection:

```css
.sensitivity-base {
    background: #e8f4fd;
    font-weight: 700;
    border: 2px solid #0D6EAA;
}
```

Matrix dimensions: 6 rows (exit multiples) × 5 columns (exit EBITDA values). Base case EBITDA and base case multiple at center.

#### 5. Thesis Pillar Boxes

Each thesis pillar rendered as a bordered box with left accent:

```html
<div style="border: 1px solid #dee2e6; border-left: 4px solid #0D6EAA; padding: 24px; margin: 20px 0; border-radius: 4px;">
    <h3>Thesis Pillar 1: [Title]</h3>
    <!-- What we believe / Evidence / Why we're right / Value creation / Key assumption -->
</div>
```

Internal structure uses bold labels for each subsection.

#### 6. Risk Severity Badges

Inline badges next to each risk title:

| Rating | Background | Text Color | CSS |
|---|---|---|---|
| Critical | `#c62828` | `#ffffff` | `background: #c62828; color: #fff;` |
| High | `#f8d7da` | `#721c24` | `background: #f8d7da; color: #721c24;` |
| Medium | `#fff3cd` | `#856404` | `background: #fff3cd; color: #856404;` |
| Low | `#d1ecf1` | `#0c5460` | `background: #d1ecf1; color: #0c5460;` |

Likelihood badges use the same palette. Badge CSS:

```css
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 3px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 8px;
}
```

#### 7. Callout Boxes

For important notes (fund hurdle discussion, adversarial review, risk flags):

```html
<div style="background: #f8f9fa; border-left: 4px solid #856404; padding: 16px 20px; margin: 20px 0; border-radius: 0 4px 4px 0;">
    <strong>Note on base case returns vs. fund hurdle:</strong> [content]
</div>
```

Use `#856404` (amber) border for warnings/notes. Use `#0D6EAA` (blue) for neutral callouts.

#### 8. Table of Contents Sidebar

Fixed-position left sidebar, toggled via a button. Hidden in print.

```css
.toc-sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 260px;
    height: 100vh;
    background: #1B2A3D;
    color: #cbd5e1;
    padding: 60px 20px 20px;
    overflow-y: auto;
    z-index: 1000;
    transform: translateX(-100%);
    transition: transform 0.2s;
}
.toc-sidebar.open { transform: translateX(0); }
```

Toggle button: fixed top-left corner, `#1B2A3D` background, "☰ Contents" label. Changes to "✕ Close" when open.

Section links: `font-size: 13px; color: #94a3b8;` → hover: `color: #ffffff;`

Navigation uses `id` attributes on section headings (e.g., `id="sec-1"`, `id="sec-8"`). Links use `href="#sec-X"` with smooth scrolling.

#### 9. PROCEED/PASS/DEFER Box (Recommendation Section)

```html
<div style="border: 2px solid #166534; border-radius: 8px; padding: 24px; margin: 20px 0;">
    <div style="display: inline-block; background: #166534; color: #fff; padding: 8px 20px; border-radius: 4px; font-weight: 700; font-size: 16px; letter-spacing: 0.1em;">
        PROCEED
    </div>
    <div style="margin-top: 16px;">
        <!-- Deal Lead, IC Meeting Date, Fund -->
    </div>
</div>
```

Colors by recommendation: PROCEED = `#166534` (green), PASS = `#991b1b` (red), DEFER = `#92400e` (amber).

#### 10. Footer

```html
<div style="border-top: 1px solid #dee2e6; margin-top: 40px; padding-top: 15px; font-size: 11px; color: #888; text-align: center;">
    CONFIDENTIAL — Northwood Capital | Investment Committee Memorandum — Project [Codename] | [Date]
</div>
```

### Print CSS

```css
@media print {
    body { padding: 20px; max-width: 100%; }
    table { page-break-inside: avoid; }
    h2 { page-break-after: avoid; }
    .toc-sidebar, .toc-toggle { display: none !important; }
    .coversheet { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
```

---

## Cross-Reference Integrity Map

These numbers appear in multiple sections. When any source value changes, ALL locations must update.

### Returns Numbers (highest cross-reference count)

| Number | Sections Where It Appears |
|---|---|
| Base IRR / MOIC | 1 (Exec Summary), 1 (hurdle note), 8.1 (table), 8.1 (case description), 8.1 (hurdle note), 8.3 (attribution total), 11 (recommendation), QA Summary |
| Upside IRR / MOIC | 1 (Exec Summary), 5 (Thesis Pillar 3, if cited), 8.1 (table), 8.1 (case description), 8.1 (hurdle note), 11 (recommendation) |
| Downside IRR / MOIC | 1 (Exec Summary), 8.1 (table), 8.1 (case description), 9 (Risk 1 residual risk) |
| Exit debt (base) | 6.5 (value bridge), 8.1 (table), 8.3 (attribution) |
| Cumulative debt paydown | 5 (Thesis Pillar 1 — inelastic demand), 6.5 (value bridge) |

### Entry Terms (moderate cross-reference count)

| Number | Sections Where It Appears |
|---|---|
| Enterprise Value ($XXX.XM) | 1, 7.1 (Sources & Uses), 7.3 (indemnification cap calculation) |
| Entry EBITDA | 1, 4.1 (historical table), 4.2 (EBITDA bridge), 6.5 (bridge entry), 7.2 (leverage calc), 8.1 |
| Entry Leverage (X.Xx) | 1, 7.2 (capital structure), 7.2 (leverage context) |
| Total Equity | 1, 7.1, 8.1 (hurdle note — "X.Xx return on $XX.XM equity") |
| Fund Equity (80%) | 1, 7.1 |

### Value Creation Bridge

| Component | Sections Where It Appears |
|---|---|
| EBITDA growth % | 6.5, 8.3 |
| Deleveraging % | 6.5, 8.3 |
| Multiple expansion % | 6.5, 8.3 |

**Rule:** Sections 6.5 and 8.3 must match exactly. If they use different formats (% vs. MOIC contribution), both must be internally consistent.

---

## Sensitivity Table Conventions

The MOIC sensitivity matrix uses the following structure:

- **Rows:** Exit multiples (6 values, 0.5x–1.0x increments, centered on base case)
- **Columns:** Exit EBITDA (5 values, ±10% and ±20% of base case EBITDA)
- **Base case cell:** Highlighted with accent color and border
- **Range:** Must include at least one row below entry multiple and one row at entry + 2.0x

Source: `python tools/lbo_model.py {deal_id} --sensitivity` — the model outputs the full matrix.

When updating from model output:
1. Read the model's sensitivity output (JSON or terminal)
2. Map to the 6×5 grid with base case at center
3. Verify the base case cell matches the base case MOIC in Section 8.1

---

## Scenario Analysis Conventions

Three cases are mandatory. Each must answer a specific question:

| Case | Question | Typical Structure |
|---|---|---|
| **Downside** | "Can we get our money back?" | Revenue decline/flat, margin compression, customer loss, exit at entry multiple or below. Target: 1.0–1.5x MOIC. |
| **Base** | "What does plan achievement look like?" | Organic growth at thesis rate, margin expansion per value creation plan, no add-ons, modest multiple expansion. Target: fund hurdle proximity. |
| **Upside** | "What does a home run look like?" | Organic outperformance + add-on acquisitions, full margin expansion, premium exit multiple. Target: >3.0x MOIC. |

Source: `python tools/lbo_model.py {deal_id} --scenarios` — the model computes all three from `lbo_assumptions.downside` and `lbo_assumptions.upside` blocks in the data spine.

---

## File Naming and Output Locations

| Deliverable | Location | Naming |
|---|---|---|
| IC memo (markdown) | `pipeline/active/project-{codename}/03-ic-materials/ic-memo.md` | In-place; add revision history entry for each update |
| IC memo (HTML) | `outputs/ic-memos/` | `ic-memo-project-{codename}-{date}-v{#}.html` |
| LBO model output | `pipeline/active/project-{codename}/06-model/model-output.html` | Generated by subagent |
| LBO model summary | `pipeline/active/project-{codename}/06-model/model-summary.md` | Updated when model is parameterized |

---

## Execution Checklist

Use this checklist when producing a new IC memo. Steps are in dependency order.

### New Deal (No Prior IC Memo)

- [ ] Read all files in `pipeline/active/project-{codename}/` — every subfolder
- [ ] Read `_reference/ic-memo-template.md` for section requirements
- [ ] Read `_reference/investment-thesis.md` for firm strategy and return targets
- [ ] Read `_reference/risk-framework.md` for risk categories and severity definitions
- [ ] Read `_reference/screening-criteria.md` for auto-pass and flag criteria
- [ ] Check if `lbo_assumptions` exists in data spine for this deal
  - If yes: use computed model numbers
  - If no: use conservative hand estimates, flag as preliminary
- [ ] Draft all 11 sections per template
- [ ] Run QA protocol (4 checks)
- [ ] Add QA Summary section
- [ ] Save markdown to `pipeline/active/project-{codename}/03-ic-materials/ic-memo.md`
- [ ] Generate HTML rendering to `outputs/ic-memos/`
- [ ] Preview HTML — verify all sections render, numbers consistent, print clean

### Model Integration Update (v1 → v2)

- [ ] Read existing IC memo
- [ ] Read `model-summary.md` for computed numbers
- [ ] Identify all ~15 edit locations using the cross-reference map above
- [ ] Update each location with computed model numbers
- [ ] Verify sensitivity table matches model output
- [ ] Verify value creation bridge matches model output
- [ ] Add revision history entry
- [ ] Re-run QA structural consistency check
- [ ] Regenerate HTML rendering (new version number)
- [ ] Preview HTML — spot-check returns table, sensitivity matrix, recommendation section

### Key Lessons from Everest Build

1. **D&A tax shield is the primary driver of model-vs-estimate divergence.** Hand estimates typically ignore D&A deduction from taxable income. At 2% of revenue, this reduces annual cash taxes by ~$0.9M, compounding through accelerated deleveraging. Always expect the parameterized model to show faster debt paydown and higher returns than hand estimates.

2. **Downside MOIC can go down when the model is more precise.** Hand estimates may overstate downside cash generation. The Everest downside dropped from 1.3x to 1.2x because the model correctly applies the same NWC and capex assumptions to the stressed revenue scenario.

3. **Value creation bridge attribution shifts with precise deleveraging.** When the model shows faster debt paydown (D&A shield), deleveraging's share of value creation increases and EBITDA growth's relative share decreases, even though the absolute EBITDA contribution doesn't change.

4. **The HTML is a subagent task.** The IC memo is 800+ lines of markdown → 1,200+ lines of HTML. Provide the subagent with: (a) the full updated markdown, (b) the deliverable standards design system, and (c) this methodology doc's component specs. One-shot generation works; verification via preview server catches rendering issues.

5. **TOC sidebar is essential for IC memos.** 11 sections + appendices means the document is 25-35 pages equivalent. The collapsible sidebar makes it navigable. Always include it.

---

*Northwood Capital | Reference Document | Do not modify*
