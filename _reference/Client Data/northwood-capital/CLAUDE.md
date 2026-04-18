# Northwood Capital Partners — Operating Environment

## Firm Identity

See `_reference/firm-overview.md` for full firm data (team roster, fund details, portfolio summary).

**Quick reference:** Mid-market control buyout PE firm. $1.75B AUM. 2 funds (Fund I $650M harvesting, Fund II $1.1B deploying). 10 active portfolio companies, 2 realized exits. Chicago, IL.

---

## How This Architecture Works

This workspace is the firm's operating environment. Claude Code reads these files to understand context, produce deliverables, and maintain institutional knowledge across sessions.

**Before producing any deliverable, read `_reference/`.** Those files encode the investment thesis, screening criteria, risk framework, deliverable templates, QA protocols, and data source documentation. They are the source of truth for how this firm operates.

Every deliverable goes to `outputs/` in the appropriate subfolder.

Every deliverable runs through the QA protocol in `_reference/qa-protocol.md` before being marked complete.

---

## Folder Architecture

Key top-level folders:

- `_reference/` — READ-ONLY templates, standards, criteria, methodology docs
- `_secrets/` — API keys (read before external calls)
- `_data/` — Data files and generated datasets
- `fund/` — Fund-level data, performance, LP communications
- `pipeline/` — Deal pipeline (active, monitoring, passed). Tracker: `pipeline/_pipeline-tracker.md`
- `portfolio/` — Portfolio companies post-close. Dashboard: `portfolio/_portfolio-dashboard.md`
- `outputs/` — All generated deliverables (screening-memos, ic-memos, board-decks, comp-analyses, market-landscapes, ad-hoc)
- `tools/` — Python scripts and utilities (LBO model, comp analysis, screening memo, board deck generators)
- `ad-hoc/` — Scratch work, one-off analyses

---

## File Naming

`[type]-[deal-or-portco]-[date]-v[#].[ext]`

| Component | Format | Examples |
|-----------|--------|----------|
| type | Deliverable category | `screening-memo`, `ic-memo`, `board-deck`, `comp-analysis`, `returns-model` |
| deal-or-portco | Project codename or company name | `project-everest`, `meridian`, `project-falcon` |
| date | ISO 8601 | `2026-02-15`, `2026-q1`, `2026-01` |
| v[#] | Version (always increment, never overwrite) | `v1`, `v2` |
| .[ext] | `.md` for analysis, `.html` for visual deliverables | |

---

## Workflows

Standard operating procedures for major deliverable types:

- **Deal Screening** — CIM review → screening criteria check → memo → tracker update
- **IC Memo Preparation** — Full deal folder review → 13-section memo → QA → output
- **Board Deck Generation** — Portco data → variance computation → HTML deck → output
- **Pipeline Management** — Tracker-first status transitions (Sourcing → Close or Pass)
- **Portfolio Monitoring** — Dashboard review → KPI tracking → RAG status updates

---

## Quality Standards

Every deliverable runs through the four-check QA protocol in `_reference/qa-protocol.md`:

1. **Source Verification** — Every figure traced to a source. No unsourced claims.
2. **Structural Consistency** — Numbers match across all sections. Template compliance verified.
3. **Adversarial Review** — Thesis stress-tested. Assumptions challenged. Missing analysis identified.
4. **Assumption Flagging** — Every assumption classified (hard data / management guidance / firm estimate / aspirational) and tested against parameter ranges.

Every deliverable includes a QA Summary section. No exceptions.

---

## Voice & Tone

Direct, precise, institutional. This is how a $1.75B fund communicates:

- State conclusions first. Support with data. Flag risks plainly.
- No filler phrases ("it is worth noting that," "it should be mentioned").
- No hedging language unless uncertainty is genuine and quantified.
- No superlatives without evidence ("best-in-class" requires proof).
- Concision is mandatory. If a sentence does not add information, delete it.
- Numbers speak louder than adjectives. "$18.5M EBITDA at 14.3% margins" over "strong profitability."

---

## Guardrails

**Never do the following:**

- **Overwrite source files.** Files in `_reference/` and `_secrets/` are read-only. Never modify them.
- **Overwrite prior versions.** Create v2, never replace v1.
- **Make investment recommendations.** Present analysis with scenarios. The IC decides.
- **Fabricate data.** If a data point is unavailable, say so. Flag it as an assumption or mark it TBD.
- **Expose confidential information.** Never include LP names, API keys, or portfolio company financials in external-facing materials unless explicitly instructed.
- **Skip QA.** Every deliverable gets the four-check protocol. No "preliminary" or "draft" exemptions.
- **Use project codenames and real company names interchangeably.** External documents use codenames. Internal documents may use real names. Confirm before drafting.

---

## Data Sources

| Source | Location | Use |
|--------|----------|-----|
| Firm context | `_reference/` | Investment thesis, criteria, templates, standards |
| API credentials | `_secrets/api-keys.md` | Read before any external API call |
| Deal pipeline | `pipeline/` | All opportunity data, tracker, deal materials |
| Portfolio data | `portfolio/` | Portco financials, KPIs, board materials, value creation |
| Fund performance | `fund/performance/` | Returns, NAV, MOIC/IRR by fund |
| LP communications | `fund/lp-communications/` | Quarterly letters, AGM materials |
| Carbon & energy data | `_data/carbon/` | Facility-level energy consumption and emissions data |
| Generated outputs | `outputs/` | All deliverables produced by CC |
| Supabase | `northwood_capital` schema | Structured data: portco financials, KPIs, comps, pipeline deals |

---

## Supabase Data Access

**Schema:** `northwood_capital`
**Credentials:** See `_secrets/api-keys.md`
**Access:** Read-only. The database holds queryable structured data; the file system holds documents, templates, and narratives.

### Tables

| Table | Rows | Description |
|-------|------|-------------|
| `portfolio_companies` | 10 | Active portcos — entry terms, current metrics, LBO assumptions, deal team, board dates |
| `portco_financials` | 74 | Monthly financials (EAV format). Metrics: revenue, cogs, gross_profit, ebitda, net_income. Actual vs. budget vs. prior year |
| `portco_kpis` | 311 | Monthly operational KPIs (EAV). headcount, customer_count, nrr, utilization, dso, turnover |
| `pipeline_deals` | 8 | Deal pipeline — active, passed, and monitoring. Stage, financials, deal team, LBO assumptions |
| `fund_performance` | 2 | Fund-level data — committed/drawn capital, MOIC, IRR, portco lists |
| `team_members` | 12 | Firm roster — name, title, board seats, deal/portco assignments |
| `realized_investments` | 2 | Exited companies — entry/exit terms, returns, value creation summary |
| `transaction_comps` | 45 | Precedent transaction multiples by sector |
| `trading_comps` | 28 | Public company trading multiples by sector |
| `firm_config` | 3 | Firm metadata, conventions, rounding rules |
| `esg_portco_scores` | — | ESG risk scores by dimension (E1-E3, S1-S3, G1-G2) per portco per period |
| `esg_portco_composites` | — | Weighted composite ESG score per portco |
| `esg_climate_risk` | — | Physical climate risk scores by portco and hazard type |
| `esg_climate_composites` | — | Physical climate risk composite per portco |
| `esg_deal_scores` | 8 | Pipeline deal ESG DD scores by dimension |
| `esg_deal_composites` | 1 | Pipeline deal ESG composite and IC recommendation |
| `process_execution_log` | — | Audit trail of CC-generated deliverables |

### Query Patterns

All queries use the `northwood_capital` schema.

```sql
-- Portfolio company current metrics
SELECT portco_name, current_revenue, current_ebitda, current_debt, performance_status
FROM northwood_capital.portfolio_companies;

-- Monthly financials for a specific portco
SELECT period, metric, actual, budget, prior_year
FROM northwood_capital.portco_financials
WHERE portco = 'sterling_precision' AND period = '2026-01';

-- Transaction comps for a sector
SELECT target, acquirer, date, ev, ebitda, ev_ebitda
FROM northwood_capital.transaction_comps
WHERE sector = 'Industrial Technology';
```

---

## Cross-Reference Rules (Direction of Truth)

| Metric | Source of Truth | Other Locations (derived) |
|--------|----------------|--------------------------|
| Deal status | `pipeline/_pipeline-tracker.md` | Individual `deal-status.md` files |
| Portfolio performance | `portfolio/_portfolio-dashboard.md` | Individual `portco-status.md` files |
| Fund returns | `fund/performance/{{fund-slug}}-returns.md` | LP letters, portfolio dashboard |
| KPIs | `portfolio/{{portco}}/financial-reporting/kpi-dashboard.md` | Board decks, portfolio dashboard |
| Entry terms | `portfolio/{{portco}}/acquisition/closing-summary.md` | IC memos, returns trackers |
| Screening criteria | `_reference/screening-criteria.md` | Screening memos (applied, not modified) |
| Assumptions ranges | `_reference/qa-protocol.md` | IC memos, returns analyses (applied, not modified) |
| Canonical entity values | `portfolio/_portfolio-dashboard.md` | Individual portco files (derived from dashboard) |

When sources conflict, the source of truth listed above prevails. Flag the discrepancy and resolve it.
