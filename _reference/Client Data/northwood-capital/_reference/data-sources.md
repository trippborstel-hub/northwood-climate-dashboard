# Data Sources

CONFIDENTIAL -- Northwood Capital

**Effective:** February 2026
**Applies to:** All data used in Northwood Capital deliverables, models, and reporting. This document defines what sources exist, how fresh they are, how they rank in priority, and what quality caveats apply to each.

---

## Internal Sources

### Portfolio Company Monthly Financial Package

**Description:** Standardized reporting package submitted by each portfolio company CFO. Contains income statement, balance sheet, cash flow statement, budget-to-actual comparison, and management commentary.

| Attribute | Detail |
|---|---|
| Frequency | Monthly |
| Delivery | By 20th of the following month |
| Format | Excel workbook (standardized template) + PDF management commentary |
| Coverage | All 8 active portfolio companies |
| Owner | Portfolio company CFO |
| Northwood recipient | Deal lead + Brian Taylor (CFO) |

**Contents:**
- Income statement (monthly actual vs. budget vs. prior year)
- Balance sheet (end-of-period)
- Cash flow statement (monthly)
- Debt schedule (balances, draws, compliance)
- Revenue detail by segment, customer tier, or geography (varies by portco)
- Headcount report (ending, additions, departures)
- Management commentary (1-2 pages, narrative on performance drivers)

**Quality Notes:**
- Financial figures are unaudited. Annual audit occurs within 90 days of fiscal year end.
- EBITDA adjustments are management-reported. Northwood validates material adjustments against supporting documentation on a quarterly basis.
- Budget figures are set during Q4 board planning process and are not restated mid-year.

**Freshness:** 20-day lag from period end. January 2026 data available by February 20, 2026.

### Management Calls

**Description:** Regularly scheduled calls between Northwood deal leads and portfolio company management teams (CEO, CFO, and occasionally COO or functional leaders).

| Attribute | Detail |
|---|---|
| Frequency | Weekly for early-stage (first 12 months post-close); bi-weekly for mature portcos |
| Format | Phone/video call, Northwood-prepared agenda, notes captured by deal team |
| Participants | Deal lead, supporting associate/VP, portco CEO and CFO |

**Current Cadence by Portfolio Company:**

| Portfolio Company | Call Frequency | Deal Lead |
|---|---|---|
| Meridian Business Solutions | Bi-weekly | Mark Sullivan |
| NovaCare Health Partners | Bi-weekly | Priya Kapoor |
| Sterling Precision Manufacturing | Bi-weekly | James Harrison |
| Trident IT Solutions | Bi-weekly | Mark Sullivan |
| Clearview Environmental Services | Bi-weekly | Priya Kapoor |
| Patriot Staffing Solutions | Weekly | Andrew Walsh |
| Keystone Behavioral Health | Weekly | Nadia Fernandez |
| Pinnacle Testing & Inspection | Weekly | Andrew Walsh |

**Quality Notes:**
- Call notes are informal and may contain management's verbal estimates that have not been reconciled to financials.
- Verbal figures cited in deliverables must reference the specific call date.
- Management verbal estimates rank below financial package data in source priority (see priority hierarchy below).
- Patriot and Keystone/Pinnacle are on weekly cadence due to below-plan performance and early integration status respectively.

### Board Minutes

**Description:** Approved minutes from portfolio company board meetings. Formal record of board decisions, approvals, and key discussions.

| Attribute | Detail |
|---|---|
| Frequency | Quarterly (aligned with portco board meeting schedule) |
| Format | PDF, prepared by portco legal counsel or corporate secretary |
| Approval | Approved at subsequent board meeting |
| Storage | Northwood shared drive, portco-specific board folder |

**Quality Notes:**
- Minutes are the authoritative record of board-level decisions (capex approvals, management incentive plans, add-on acquisitions, dividend distributions).
- Draft minutes may be referenced prior to approval but must be flagged as `[Draft Board Minutes]`.

### KPI Dashboards

**Description:** Operational KPIs tracked outside the monthly financial package. Reported by portco operations teams and compiled by Northwood deal leads.

| Attribute | Detail |
|---|---|
| Frequency | Monthly (some KPIs weekly) |
| Delivery | By 15th of the following month |
| Format | Varies by portco (Excel, dashboards, portco-internal systems) |
| Standardization | Northwood-defined KPI template applied at 100-day mark |

**Standard KPIs Tracked Across All Portcos:**

| KPI | Definition |
|---|---|
| Headcount | Ending headcount (internal employees; temp workers reported separately for staffing businesses) |
| Customer count | Active customers, patients, clinics, or contracts as applicable |
| Net revenue retention (NRR) | Applicable to recurring-revenue businesses (Trident, Meridian) |
| Utilization | Billable utilization for services businesses |
| DSO (days sales outstanding) | Accounts receivable collection efficiency |
| Employee turnover | Annualized voluntary turnover rate |

**Quality Notes:**
- KPI definitions vary by portco before standardization. Northwood applies consistent definitions at 100-day mark.
- KPI data has a 15-day lag from period end. Faster than financial package but less auditable.
- For recently acquired portcos (Keystone, Pinnacle), KPI reporting may be incomplete during integration.

### Internal Models

**Description:** Northwood-built LBO models, returns models, and scenario analyses for portfolio companies and pipeline deals.

| Attribute | Detail |
|---|---|
| Format | Excel (pipeline deals), markdown summary outputs |
| Ownership | Deal lead and supporting team member |
| Version control | Model versions tracked with date suffix |
| Review | All IC-presented models reviewed by a second partner |

**Quality Notes:**
- Models contain Northwood assumptions that must be labeled per the QA Protocol.
- Base case, downside, and upside scenarios required for all IC presentations.
- Model outputs are derived data -- they are never a source of truth for actuals. Only for projected and scenario values.

---

## External Sources

### PitchBook

**Description:** Primary source for private market transaction data, comparable company valuations, and market mapping.

| Attribute | Detail |
|---|---|
| Subscription | Full platform access |
| Primary use | Comparable transaction multiples, precedent deals, market sizing, add-on target identification |
| Update frequency | Continuous (deal data updated as transactions are reported) |
| Northwood users | All deal team members |

**Typical Data Points Sourced:**
- Comparable transaction EV/EBITDA multiples
- Sector deal volume and trends
- Add-on acquisition target identification
- Sponsor activity in target sectors
- Public comparable trading multiples

**Quality Notes:**
- PitchBook transaction multiples are based on reported deal values. Many middle-market transactions do not disclose terms, creating selection bias toward larger, disclosed deals.
- Revenue multiples from PitchBook may not distinguish between recurring and non-recurring revenue.
- Always note the sample size and date range when citing PitchBook comp sets.

### S&P Capital IQ

**Description:** Public company financial data, market data, and company screening.

| Attribute | Detail |
|---|---|
| Subscription | Full platform access |
| Primary use | Public comparable company analysis, credit data, industry financial benchmarks |
| Update frequency | Real-time for public market data; quarterly for financials |
| Northwood users | All deal team members |

**Typical Data Points Sourced:**
- Public company financial statements and ratios
- Trading multiples (EV/EBITDA, EV/Revenue, P/E)
- Credit market conditions (leveraged loan spreads, issuance volumes)
- Industry financial benchmarks (median margins, growth rates)

**Quality Notes:**
- Public comps are useful as directional benchmarks but must be adjusted for size, growth, and risk profile differences versus private middle-market targets.
- Capital IQ segment data may not align with how target companies define their segments.

### Industry Reports

**Description:** Third-party research reports providing market sizing, growth projections, competitive landscape, and industry trend analysis.

| Source | Coverage | Update Cycle | Subscription |
|---|---|---|---|
| IBISWorld | US industry reports by NAICS code | Annual, with quarterly updates | Full access |
| Frost & Sullivan | Technology, healthcare, industrial verticals | Varies by report | Select reports purchased |
| Gartner | IT services, cybersecurity, managed services | Annual | Select reports via Trident board |
| Healthcare industry associations | ABA therapy, PT, dental, behavioral health | Annual | Trade association memberships via portcos |

**Quality Notes:**
- Market sizing methodologies vary across providers. Always note the source and methodology when citing market size.
- Growth projections from industry reports are consensus estimates, not guaranteed outcomes. Label as `[Industry Benchmark]` per QA Protocol.
- Industry reports published before major regulatory changes may be stale. Check publication date against regulatory timeline.

### Bureau of Labor Statistics (BLS)

**Description:** Federal statistical data on labor markets, wages, employment, and occupational trends.

| Attribute | Detail |
|---|---|
| Primary use | Labor market analysis for staffing businesses (Patriot, Meridian), wage trend analysis, therapist/technician supply data |
| Update frequency | Monthly (employment data), quarterly (wage data), annual (occupational outlook) |
| Access | Free public data |

**Typical Data Points Sourced:**
- Unemployment rates by geography and sector
- Wage growth by occupation (critical for staffing businesses and labor-intensive portcos)
- Occupational employment projections (therapist supply, technician pipelines)
- Industry employment trends

**Quality Notes:**
- BLS data is backward-looking and subject to revision. Initial monthly estimates are revised in subsequent months.
- Metropolitan-level data may have wider confidence intervals than national data.
- Occupational projections (e.g., BCBA therapist supply) are 10-year forecasts and should be cited as long-range estimates, not near-term predictions.

---

## Source Priority Hierarchy

When data conflicts exist between sources, the following priority applies:

| Priority | Source | Rationale |
|---:|---|---|
| 1 | Internal financial package (portco-reported monthly actuals) | Closest to the books; prepared by portco finance team from general ledger |
| 2 | Board minutes and board-approved materials | Formal record with fiduciary oversight |
| 3 | Management verbal (dated call notes) | Direct from management but not reconciled to GL; may contain estimates |
| 4 | KPI dashboards (portco-reported operational data) | Operational metrics outside the financial close process; definitions may vary |
| 5 | Northwood internal model outputs | Derived data based on assumptions; useful for projections, not for actuals |
| 6 | External estimate (PitchBook, Capital IQ, industry reports) | Third-party data; useful for market context, benchmarking, and comps |

### Rules for Conflict Resolution

1. **Actuals always beat estimates.** If the financial package says $38.3M EBITDA and a management call from the prior week estimated ~$39M, use $38.3M.
2. **Specific beats general.** A portco-reported customer count of 145 beats an industry report estimating "~150 customers for firms of this size."
3. **Newer beats older for current metrics.** January 2026 financial package supersedes December 2025 financial package for current performance. But entry metrics are immutable -- they come from the data spine regardless of date.
4. **Flag disagreements.** If two credible sources materially disagree (>5% variance), note both values and the discrepancy in the deliverable. Do not silently choose one.

---

## Data Freshness

| Data Type | Reporting Lag | Practical Implication |
|---|---|---|
| Monthly financial package | 20 days after month-end | January 2026 data available ~February 20 |
| KPI dashboards | 15 days after month-end | January 2026 KPIs available ~February 15 |
| Management call notes | Same day | Most current verbal data, but lowest quality tier |
| PitchBook transaction data | Varies (days to weeks after close) | Middle-market deals may appear weeks after close; multiples often estimated |
| S&P Capital IQ public data | Real-time (market); quarterly (financials) | Public comps update quarterly with 10-Q/10-K filings |
| BLS employment data | ~30 days after reference month | Preliminary data subject to revision |
| Industry reports | Annual or semi-annual publication | May be 6-12 months stale on publication |
| Supabase (`northwood_capital` schema) | Updated quarterly or on material event | Canonical source; treat as current until next update |

### Staleness Rules

- Any data point used in a deliverable must be from the most recent available source.
- If the most recent source is older than 90 days, the data point must carry a staleness flag: `[as of YYYY-MM-DD -- update pending]`.
- Quarterly LP reports must use financial data no older than 45 days from distribution date.
- IC memos must use financial data no older than 30 days from IC meeting date.

---

## Data Integration and APIs

**Note:** This section describes the target-state architecture. In the current environment, data flows are manual (file-based). No live API integrations are active. All references below are simulation placeholders for future implementation.

### Target-State Integrations (Not Yet Implemented)

| System | Integration Type | Data Flow | Status |
|---|---|---|---|
| Portfolio company accounting systems | API pull | Monthly financials auto-imported | **Placeholder** -- manual Excel upload |
| PitchBook | API | Comp set refresh on demand | **Placeholder** -- manual export |
| S&P Capital IQ | API | Public comp data pull | **Placeholder** -- manual export |
| Northwood Supabase | Internal database | Canonical entity and metric store | **Active** -- `northwood_capital` schema, queried via MCP |
| CRM / deal pipeline | API | Pipeline stage tracking | **Placeholder** -- manual markdown files |

### Current Data Flow (Manual)

```
Portco Finance Team
    |
    v
Monthly Excel Package (email, 20th of month)
    |
    v
Deal Lead (validates, flags issues)
    |
    v
Northwood Working Files (portco status, fund reports)
    |
    v
Data Spine (quarterly reconciliation by CFO)
```

All data movement is manual. The deal team is responsible for ensuring that the most recent financial package data is reflected in working documents before deliverable deadlines.

---

## Source Quality Matrix

Summary view of source reliability and appropriate use by data type.

| Data Type | Best Source | Acceptable Backup | Not Acceptable |
|---|---|---|---|
| Portco LTM revenue | Financial package | Management verbal (with date) | Industry report estimate |
| Portco LTM EBITDA | Financial package | Management verbal (with date) | Prior quarter's financial package |
| Entry EV / equity invested | Data spine | Closing summary | Memory, verbal |
| Comparable transaction multiples | PitchBook | Capital IQ | CIM-cited multiples (seller-biased) |
| Market size | IBISWorld / Frost & Sullivan | Multiple corroborating sources | Single management assertion |
| Headcount | Financial package / KPI dashboard | Management verbal | LinkedIn estimate |
| Customer count | KPI dashboard | Management verbal | External estimate |
| Exit multiple assumption | RC model (sourced to comps) | -- | Unsourced assumption |
| Wage growth / labor data | BLS | Industry association data | Anecdotal |
| Reimbursement rates | CMS published schedules | Payor contract terms (portco-held) | Industry article |

---

## Appendix: Source Abbreviations

For inline citations in deliverables, use the following abbreviations.

| Abbreviation | Full Source |
|---|---|
| `[Spine]` | Supabase `northwood_capital` schema (current) |
| `[FP, YYYY-MM]` | Portfolio company financial package for stated month |
| `[Mgmt, YYYY-MM-DD]` | Management call on stated date |
| `[BM, Co Name, YYYY-MM-DD]` | Board minutes for stated company and date |
| `[PB, Dataset, Date]` | PitchBook, specific dataset or comp set, access date |
| `[CIQ, Dataset, Date]` | S&P Capital IQ, specific dataset, access date |
| `[IBIS, Report, Date]` | IBISWorld industry report |
| `[F&S, Report, Date]` | Frost & Sullivan report |
| `[BLS, Series, Date]` | Bureau of Labor Statistics, specific data series |
| `[VDD, Provider, Date]` | Vendor due diligence report |
| `[CDD, Provider, Date]` | Commercial due diligence report |
| `[RC Model, Version]` | Northwood internal model |
| `[RC Assumption]` | Northwood internal assumption (must include rationale) |
