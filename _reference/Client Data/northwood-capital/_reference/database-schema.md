# Database Schema Reference

**Schema:** `northwood_capital`
**Access:** Read-only. Credentials in `_secrets/api-keys.md`.

---

## Core Tables

### portfolio_companies

Active portfolio companies — entry terms, current performance, deal team, board schedule.

| Column | Type | Description |
|--------|------|-------------|
| slug | text (PK) | Unique identifier (e.g., `sterling_precision`) |
| portco_name | text | Display name |
| portco_slug | text | URL-safe slug |
| fund | text | Fund (fund_i, fund_ii) |
| sector | text | Industry sector |
| sector_detail | text | Sub-sector |
| acq_date | date | Acquisition close date |
| entry_ev | numeric | Enterprise value at entry ($M) |
| entry_ebitda | numeric | EBITDA at entry ($M) |
| entry_revenue | numeric | Revenue at entry ($M) |
| equity_invested_total | numeric | Total equity ($M) |
| equity_invested_fund | numeric | Fund equity portion ($M) |
| equity_invested_mgmt | numeric | Management rollover ($M) |
| entry_debt | numeric | Debt at close ($M) |
| debt_lender | text | Lead lender(s) |
| debt_terms | text | Rate, maturity, amortization |
| revolver_size | numeric | Revolver capacity ($M) |
| revolver_drawn | numeric | Revolver drawn at entry ($M) |
| transaction_type | text | Platform, add-on, etc. |
| current_revenue | numeric | LTM revenue ($M) |
| current_ebitda | numeric | LTM EBITDA ($M) |
| current_debt | numeric | Current net debt ($M) |
| revolver_drawn_current | numeric | Current revolver draw ($M) |
| distributions | numeric | Cumulative distributions ($M) |
| distributions_detail | text | Distribution narrative |
| exit_multiple_assumption | numeric | Assumed exit EV/EBITDA |
| performance_status | text | RAG status (Green/Amber/Red/Watch) |
| gross_irr | numeric | Gross IRR (%) |
| deal_lead | text | Northwood deal lead |
| management_ceo | text | CEO name |
| management_cfo | text | CFO name |
| management_coo | text | COO name |
| headcount | integer | Current headcount |
| headcount_at_entry | integer | Headcount at close |
| customer_count | integer | Current customer count |
| customer_count_label | text | Customer unit label |
| top_customer_concentration | numeric | Top customer revenue % |
| key_risks | text[] | Risk factors |
| add_ons_completed | text[] | Completed add-on acquisitions |
| key_thesis | text | Investment thesis summary |
| next_board_date | date | Next board meeting |
| next_board_agenda | text | Board agenda items |
| lbo_assumptions | jsonb | LBO model parameters |
| updated_at | timestamptz | Last modified |

---

### portco_financials

Monthly financial data in entity-attribute-value (EAV) format. One row per portco per period per metric.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| portco | text | Portfolio company slug |
| period | text | Month (e.g., `2026-01`) |
| metric | text | Financial metric (revenue, cogs, gross_profit, ebitda, net_income) |
| actual | numeric | Actual value ($M) |
| budget | numeric | Budget value ($M) |
| prior_year | numeric | Prior year value ($M) |
| created_at | timestamptz | Row created |

**Query pattern:**
```sql
SELECT period, metric, actual, budget, prior_year
FROM northwood_capital.portco_financials
WHERE portco = 'sterling_precision'
ORDER BY period, metric;
```

---

### portco_kpis

Monthly operational KPIs in EAV format. One row per portco per period per KPI.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| portco | text | Portfolio company slug |
| period | text | Month (e.g., `2026-01`) |
| kpi | text | KPI name (headcount, customer_count, nrr, utilization, dso, turnover, etc.) |
| value | numeric | Actual KPI value |
| target | numeric | Target/benchmark value |
| created_at | timestamptz | Row created |

**Query pattern:**
```sql
SELECT period, kpi, value, target
FROM northwood_capital.portco_kpis
WHERE portco = 'clearview_environmental'
ORDER BY period, kpi;
```

---

### fund_performance

Fund-level data — capital, returns, portfolio composition.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| fund | text | Fund slug (fund_i, fund_ii) |
| fund_name | text | Display name |
| vintage | integer | Vintage year |
| committed_capital | numeric | Total committed ($M) |
| drawn_capital | numeric | Capital drawn ($M) |
| status | text | Fund status (harvesting, deploying) |
| total_investments | integer | Total investments made |
| realized_exits | integer | Realized exits |
| active_portfolio_count | integer | Active portcos |
| preferred_return | numeric | Preferred return (%) |
| management_fee | text | Fee structure |
| carried_interest | text | Carry structure |
| gp_commitment | numeric | GP commitment ($M) |
| net_moic | numeric | Net MOIC |
| net_irr | numeric | Net IRR (%) |
| gross_irr | numeric | Gross IRR (%) |
| portco_ids | text[] | Active portfolio company slugs |
| realized_ids | text[] | Realized investment IDs |
| as_of_date | date | Data as-of date |
| updated_at | timestamptz | Last modified |

---

### team_members

Firm roster — investment team and operating partners.

| Column | Type | Description |
|--------|------|-------------|
| id | text (PK) | Member identifier |
| full_name | text | Full name |
| title | text | Title |
| background | text | Professional background |
| education | text | Education |
| year_joined | integer | Year joined firm |
| board_seats | text[] | Board seat assignments |
| deal_assignments | text[] | Active deal assignments |
| portco_assignments | text[] | Portfolio company assignments |
| sector_focus | text | Sector specialization |
| role_note | text | Additional context |
| created_at | timestamptz | Row created |

---

## Deal Pipeline

### pipeline_deals

Deal pipeline — active opportunities, passed deals, and monitoring.

| Column | Type | Description |
|--------|------|-------------|
| codename | text (PK) | Deal codename (e.g., `project_everest`) |
| target_name | text | Target company name |
| sector | text | Industry sector |
| sector_detail | text | Sub-sector |
| status | text | active, passed, monitoring |
| stage | text | Pipeline stage (sourcing, cim_review, management_meeting, loi, diligence) |
| ev_ask | numeric | Seller asking price ($M) |
| ev_range_low | numeric | Northwood valuation range low ($M) |
| ev_range_high | numeric | Northwood valuation range high ($M) |
| ebitda | numeric | Adjusted EBITDA ($M) |
| ebitda_reported | numeric | Reported EBITDA ($M) |
| revenue | numeric | Revenue ($M) |
| implied_multiple | numeric | Implied EV/EBITDA |
| source | text | Deal source type |
| source_detail | text | Specific source |
| date_received | date | Date deal entered pipeline |
| deal_lead | text | Northwood deal lead |
| deal_support | text | Supporting team member |
| next_step | text | Next action item |
| next_step_date | date | Next action date |
| hq_city | text | Target HQ location |
| employee_count | integer | Target headcount |
| founding_year | integer | Year founded |
| key_merits | text[] | Investment merits |
| key_risks | text[] | Key risks identified |
| notes | text | Additional notes |
| lbo_assumptions | jsonb | LBO model parameters |
| seller_rationale | text | Why selling |
| process_type | text | Auction, bilateral, etc. |
| pass_reason | text | Reason for passing (if passed) |
| pass_date | date | Date passed |
| pass_type | text | Pass category |
| what_killed_it | text | Primary pass driver |
| what_we_liked | text | Positive attributes noted |
| re_engage_possible | boolean | Could revisit |
| re_engage_trigger | text | What would trigger re-engagement |
| seeded_risk | text | Identified risk factor |
| updated_at | timestamptz | Last modified |

---

## Comparables

### transaction_comps

Precedent M&A transactions by sector.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| sector | text | Industry sector |
| target | text | Acquired company |
| acquirer | text | Buyer |
| date | text | Transaction date |
| ev | numeric | Enterprise value ($M) |
| ebitda | numeric | Target EBITDA ($M) |
| revenue | numeric | Target revenue ($M) |
| ev_ebitda | numeric | EV/EBITDA multiple |
| ev_revenue | numeric | EV/Revenue multiple |
| buyer_type | text | Strategic, financial, etc. |
| description | text | Transaction context |
| citation | text | Data source |
| created_at | timestamptz | Row created |

### trading_comps

Public company trading multiples by sector.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| sector | text | Industry sector |
| ticker | text | Stock ticker |
| company | text | Company name |
| ev | numeric | Enterprise value ($M) |
| ebitda | numeric | EBITDA ($M) |
| revenue | numeric | Revenue ($M) |
| ev_ebitda | numeric | EV/EBITDA multiple |
| ev_revenue | numeric | EV/Revenue multiple |
| ebitda_margin | numeric | EBITDA margin (%) |
| revenue_growth | numeric | Revenue growth (%) |
| market_cap | numeric | Market capitalization ($M) |
| as_of_date | text | Pricing date |
| citation | text | Data source |
| created_at | timestamptz | Row created |

---

## Realized Investments

### realized_investments

Exited portfolio companies — full lifecycle data.

| Column | Type | Description |
|--------|------|-------------|
| id | text (PK) | Investment identifier |
| portco_name | text | Company name |
| fund | text | Fund |
| sector | text | Industry sector |
| sector_detail | text | Sub-sector |
| acq_date | date | Acquisition date |
| exit_date | date | Exit date |
| entry_ev | numeric | Entry enterprise value ($M) |
| entry_ebitda | numeric | Entry EBITDA ($M) |
| entry_revenue | numeric | Entry revenue ($M) |
| exit_ev | numeric | Exit enterprise value ($M) |
| exit_ebitda | numeric | Exit EBITDA ($M) |
| equity_invested | numeric | Fund equity invested ($M) |
| equity_invested_total | numeric | Total equity ($M) |
| realized_proceeds | numeric | Total proceeds ($M) |
| gross_moic | numeric | Gross MOIC |
| gross_irr | numeric | Gross IRR (%) |
| hold_period_years | numeric | Hold period (years) |
| exit_type | text | Exit route (strategic sale, secondary, IPO) |
| exit_buyer | text | Acquirer name |
| thesis_summary | text | Original investment thesis |
| value_creation_summary | text | Value creation narrative |
| updated_at | timestamptz | Last modified |

---

## ESG & Climate

### esg_portco_scores

ESG risk scores by dimension per portfolio company. Dimensions: E1-E3 (Environmental), S1-S3 (Social), G1-G2 (Governance).

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| portco | text | Portfolio company slug |
| period | text | Assessment period |
| dimension | text | Score dimension (E1, E2, E3, S1, S2, S3, G1, G2) |
| dimension_label | text | Dimension name |
| weight | numeric | Dimension weight in composite |
| score | integer | Risk score (1-5) |
| rating | text | Risk rating label |
| rationale | text | Score justification |
| created_at | timestamptz | Row created |

### esg_portco_composites

Weighted composite ESG score per portfolio company.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| portco | text | Portfolio company slug |
| period | text | Assessment period |
| composite_score | numeric | Weighted composite (1.0-5.0) |
| composite_method | text | Aggregation method |
| risk_level | text | Overall risk level |
| key_findings | text[] | Summary findings |
| escalation_flags | text[] | Items requiring attention |
| created_at | timestamptz | Row created |

### esg_climate_risk

Physical climate risk scores by portfolio company and hazard type.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| portco | text | Portfolio company slug |
| assessment_date | date | Assessment date |
| hazard | text | Climate hazard (heat, drought, flood, wildfire, storm) |
| score | numeric | Risk score |
| facility_count | integer | Total facilities assessed |
| facilities_at_risk | integer | Facilities with material exposure |
| revenue_at_risk | numeric | Revenue exposed ($M) |
| notes | text | Assessment notes |
| created_at | timestamptz | Row created |

### esg_climate_composites

Physical climate risk composite per portfolio company.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| portco | text | Portfolio company slug |
| assessment_date | date | Assessment date |
| composite_score | numeric | Overall climate risk score |
| risk_level | text | Risk level label |
| total_facilities | integer | Facilities assessed |
| states_count | integer | States with operations |
| geographic_concentration | text | Concentration risk assessment |
| key_risk | text | Primary climate risk |
| created_at | timestamptz | Row created |

### esg_deal_scores

Pipeline deal ESG due diligence scores by dimension.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| deal_codename | text | Deal codename |
| assessment_date | date | Assessment date |
| dimension | text | Score dimension |
| dimension_label | text | Dimension name |
| weight | numeric | Dimension weight |
| score | integer | Risk score (1-5) |
| rating | text | Risk rating label |
| weighted_score | numeric | Weight-adjusted score |
| rationale | text | Score justification |
| created_at | timestamptz | Row created |

### esg_deal_composites

Pipeline deal ESG composite with IC recommendation.

| Column | Type | Description |
|--------|------|-------------|
| id | integer (PK) | Row identifier |
| deal_codename | text | Deal codename |
| assessment_date | date | Assessment date |
| composite_score | numeric | Weighted composite |
| risk_level | text | Overall risk level |
| ic_recommendation | text | Recommendation for IC |
| recommendation_conditions | text | Conditions on recommendation |
| critical_dimension | text | Highest-risk dimension |
| critical_score | integer | Score of critical dimension |
| key_findings | text[] | Summary findings |
| created_at | timestamptz | Row created |

---

## System

### firm_config

Key-value store for firm metadata and conventions.

| Column | Type | Description |
|--------|------|-------------|
| key | text (PK) | Config key |
| value | jsonb | Config value |
| updated_at | timestamptz | Last modified |

### process_execution_log

Audit trail of deliverables generated by Claude Code.

| Column | Type | Description |
|--------|------|-------------|
| id | uuid (PK) | Execution identifier |
| process_type | text | Deliverable type |
| entity | text | Target entity |
| triggered_by | text | Trigger source |
| operator | text | Executing system |
| started_at | timestamptz | Execution start |
| completed_at | timestamptz | Execution end |
| duration_seconds | numeric | Duration |
| input_files | text[] | Source files used |
| input_params | jsonb | Parameters |
| output_file | text | Output file path |
| output_type | text | Output format |
| output_version | integer | Version number |
| exec_status | text | running, completed, failed |
| exec_error | text | Error message (if failed) |
| qa_status | text | QA status |
| qa_run_at | timestamptz | QA timestamp |
| qa_source_verification | jsonb | QA check 1 results |
| qa_structural_consistency | jsonb | QA check 2 results |
| qa_adversarial_review | jsonb | QA check 3 results |
| qa_assumption_flagging | jsonb | QA check 4 results |
| qa_warnings | text[] | QA warnings |
| qa_blocking_issues | text[] | QA blockers |
| notes | text | Additional notes |
| created_at | timestamptz | Row created |
| updated_at | timestamptz | Last modified |

---

## Sectors Covered

**Transaction comps:** Business Services, Environmental Services, Healthcare Services, Industrial Technology, IT Services, Food & Agriculture, Real Estate Services

**Trading comps:** Same sectors as transaction comps

**Portfolio companies span:** Industrial Technology, Environmental Services, IT Services, Business Services, Healthcare Services, Food & Agriculture, Real Estate Services
