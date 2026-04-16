# Deliverable Standards

CONFIDENTIAL -- Northwood Capital

**Effective:** February 2026
**Applies to:** All documents produced by the Northwood Capital deal team, operations team, investor relations, and fund accounting.

---

## Naming Conventions

### File Names

All files use lowercase with hyphens. No spaces, no underscores, no camelCase.

**Format:** `[document-type]-[subject]-[date-or-version].[ext]`

| Document Type | Example |
|---|---|
| Screening memo | `screening-memo-falcon-2026-02.md` |
| IC memo | `ic-memo-orion-2026-02-v2.md` |
| Portfolio status | `portco-status-meridian-2026-01.md` |
| Board deck | `board-deck-sterling-q4-2025.md` |
| Closing summary | `closing-summary-clearview-2023-03.md` |
| Monthly financial package | `financial-package-novacare-2026-01.md` |
| LP quarterly report | `lp-report-fund-ii-q4-2025.md` |
| Pipeline tracker | `pipeline-tracker-2026-02.md` |
| Model | `model-everest-base-case-v3.md` |

### Date Formats

| Context | Format | Example |
|---|---|---|
| File name (monthly) | YYYY-MM | `2026-01` |
| File name (quarterly) | QN-YYYY | `q4-2025` |
| In-document dates | Month DD, YYYY | January 31, 2026 |
| Period labels | "LTM as of January 31, 2026" or "FY 2025" | -- |
| Board decks | Quarter label | Q4 2025 |

### Version Suffixes

- First version: no suffix or `-v1`
- Revisions: `-v2`, `-v3`, etc.
- Never overwrite a previous version. Create the next version.
- Draft documents carry `-draft` suffix until finalized: `ic-memo-orion-2026-02-draft.md`

---

## Markdown Standards

### Heading Hierarchy

- **H1 (`#`):** Document title. One per document. Includes company name and document type.
- **H2 (`##`):** Major sections. These are the primary navigation points.
- **H3 (`###`):** Subsections within a major section.
- **H4 (`####`):** Rarely used. Only for detailed breakdowns within subsections.

Do not skip heading levels. An H3 must be preceded by an H2 in the same section.

### Text Formatting

- **Bold** for emphasis and key terms. Use sparingly.
- No italics. Bold or plain text only.
- No emojis. No decorative characters.
- No colored text or highlighting in markdown source.
- Use `code formatting` only for file names, field names, and technical identifiers.
- Blockquotes (`>`) for direct quotes from management, board minutes, or external sources.

### Tables

- Use markdown tables for any structured data with 2+ rows and 2+ columns.
- Right-align all numerical columns.
- Left-align all text columns.
- Include units in column headers, not in cell values.
- No merged cells.
- Header row is always bold (markdown default).

**Example:**

```
| Portfolio Company | Revenue ($M) | EBITDA ($M) | EBITDA Margin (%) | Headcount |
|---|---:|---:|---:|---:|
| Meridian Business Solutions | 225.0 | 38.3 | 17.0 | 580 |
| NovaCare Health Partners | 175.0 | 28.0 | 16.0 | 385 |
| Sterling Precision Manufacturing | 168.0 | 30.2 | 18.0 | 420 |
```

### Lists

- Bullet lists for unordered items.
- Numbered lists only when sequence matters.
- No nested lists deeper than 2 levels.
- Each list item is a complete thought or a labeled data point. No fragments.

---

## Numerical Precision

All numbers in Northwood deliverables follow these rounding and formatting rules without exception.

| Data Type | Format | Examples |
|---|---|---|
| Currency (large) | $X.XM (one decimal, millions) | $195.0M, $38.3M, $1,750.0M |
| Currency (small, <$1M) | $X.XM (one decimal, millions) | $0.8M, $0.3M |
| Currency (fund-level, >$1B) | $X.XB or $X,XXX.XM | $1.75B or $1,750.0M |
| Multiples (EV/EBITDA, MOIC) | X.Xx (one decimal) | 9.0x, 2.2x, 10.5x |
| Margins and percentages | XX.X% (one decimal) | 17.0%, 7.7%, 85.0% |
| IRR | XX% (integer) | 22%, 18%, 35% |
| IRR (approximate) | ~XX% (tilde prefix) | ~22%, ~15% |
| Basis points | Nearest 10bps | 420bps, 500bps, 50bps |
| Headcount | Exact integer | 580, 385, 420 |
| Leverage (Debt/EBITDA) | X.Xx (one decimal) | 3.6x, 1.1x, 2.5x |
| Customer count | Exact integer | 145, 118, 95 |
| Ownership percentage | XX% (integer) | 80%, 20% |
| Year | YYYY (four digits) | 2026, 2018 |
| Basis point spread | +XXXbps or S+XXXbps | S+475bps, L+425bps |

### Rules

1. **Consistency over precision.** If a number appears in multiple places, it must be formatted identically. $38.3M in one place and $38M in another is a QA failure.
2. **No false precision.** Do not report a management estimate as "$38.347M." Report it as $38.3M. The additional decimals imply accuracy that does not exist.
3. **Negative numbers.** Use parentheses for negative currency: ($2.5M). Use a minus sign for negative percentages: -3.2%.
4. **Zeros matter.** Write $0.0M, not $0 or $--. Write 0.0%, not 0% or --%.
5. **N/M for not meaningful.** Use "N/M" for metrics that are mathematically valid but not meaningful (e.g., IRR for an investment less than 6 months old). Do not use "N/A" for this purpose. Reserve "N/A" for metrics that do not apply.
6. **Thousands separator.** Use commas in numbers >= 1,000: $1,750.0M, 1,250 patients, $1,100.0M committed capital.

---

## Period Labeling

Never use ambiguous period references. Every financial metric must carry an explicit period.

### Required Labels

| Context | Correct | Incorrect |
|---|---|---|
| Current performance | LTM as of January 31, 2026 | "Current", "Latest", "Today" |
| Entry performance | At entry (March 2018) | "At acquisition", "Original" |
| Annual | FY 2025 | "Last year", "Prior year" |
| Quarterly | Q4 2025 | "Last quarter", "Recent quarter" |
| Monthly | January 2026 | "Last month", "This month" |
| Projected | FY 2026E | "Next year", "Forward" |
| Budget | FY 2026 Budget | "Budget" (without year) |

### Time Series Tables

When presenting historical data in tables:
- Label each column with the explicit period.
- Indicate whether figures are actual or estimated with "A" or "E" suffixes.
- Always include the entry period as the first column for context.

**Example:**

```
| Metric | At Entry (Q1 2018) | FY 2023A | FY 2024A | FY 2025A | LTM Jan-26 | FY 2026E |
```

---

## Status Indicators

### RAG Rating System

All portfolio companies carry a RAG (Red/Amber/Green) performance status in reporting documents.

| Rating | Label | Definition | Action Required |
|---|---|---|---|
| **Green** | On/above plan | Performing at or above underwrite on revenue, EBITDA, and key KPIs | Standard monitoring cadence |
| **Amber** | Monitoring | One or more KPIs trending below plan but corrective action underway; EBITDA within 10% of plan | Increased reporting frequency; operating partner engagement |
| **Red** | Below plan | EBITDA >10% below plan, or structural thesis risk identified | Board-level escalation; remediation plan required within 30 days |

### Mapping Spine Status to RAG

| Spine Performance Status | RAG Rating |
|---|---|
| `strong`, `strong_exit_prep`, `performing_above_plan` | Green |
| `steady_on_plan`, `performing_on_plan`, `early_100_day_plan`, `early_integration` | Green (with monitoring note for early-stage) |
| `below_plan` | Amber or Red depending on magnitude |

### Status in Documents

- Use text labels, not colored dots or emojis.
- Always pair the RAG rating with a one-sentence explanation.

**Example:**
> **Patriot Staffing:** Amber -- EBITDA margin compressed to 7.7% (plan: 8.5%) due to wage inflation outpacing bill rate increases. Management implementing client contract renegotiations in Q1-Q2 2026.

---

## Confidentiality

### Footer

Every document produced by Northwood Capital carries the following footer:

> CONFIDENTIAL -- Northwood Capital

This applies to:
- All internal documents (memos, status reports, pipeline trackers)
- All board materials
- All LP communications
- All models and analysis

### Pipeline Codenames

- Active pipeline deals are referred to by codename in all written materials until LOI execution.
- After LOI execution, the target company name may be used in IC materials.
- Codenames must never appear in documents shared outside Northwood (e.g., LP reports reference deal count and sector, not codenames).

### Classification Levels

| Level | Audience | Examples |
|---|---|---|
| Internal Only | Northwood deal team | Pipeline tracker, screening memos, IC memos, internal models |
| Board Restricted | Northwood + specific portco board | Board decks, board minutes, management presentations |
| LP Distribution | Northwood + limited partners | Quarterly reports, annual meeting materials, capital call notices |
| External | Counterparties | IOIs, LOIs, NDA-protected data requests |

---

## Document Structure Templates

### Screening Memo

```
# Screening Memo: [Codename]
## Executive Summary (1 paragraph)
## Company Overview
## Market Context
## Financial Summary
## Investment Thesis
## Key Risks
## Preliminary Valuation
## Recommendation
## Appendix: Source Log
```

### IC Memo

```
# Investment Committee Memo: [Target Name]
## Executive Summary
## Recommendation and Key Terms
## Company Overview
## Industry and Market
## Investment Thesis (3-5 numbered pillars)
## Key Risks and Mitigants
## Financial Analysis
## Returns Analysis (Base / Downside / Upside)
## Value Creation Plan
## Due Diligence Summary
## Appendix A: Comparable Transactions
## Appendix B: Model Assumptions
## Appendix C: Source Log
```

### Portfolio Company Status Report

```
# Portfolio Status: [Company Name]
## Performance Summary (RAG + 1 sentence)
## Financial Highlights (LTM table)
## KPIs
## Key Developments
## Risks and Issues
## Near-Term Priorities
## Board Update
```

---

## Deliverable Calendar

| Deliverable | Frequency | Owner | Due Date |
|---|---|---|---|
| Portfolio company financial package | Monthly | Portco CFO | 20th of following month |
| Portfolio status report | Monthly | Deal lead | 25th of following month |
| Fund performance summary | Quarterly | Brian Taylor (CFO) | 30 days after quarter end |
| LP quarterly letter | Quarterly | Jennifer Park (IR) | 45 days after quarter end |
| Board deck | Quarterly | Deal lead + operating partner | 5 business days before board |
| Pipeline tracker | Weekly | Deal team (rotating) | Friday COB |
| IC memo | As needed | Deal lead | 5 business days before IC meeting |
| Screening memo | As needed | Deal lead | Within 10 business days of CIM receipt |
