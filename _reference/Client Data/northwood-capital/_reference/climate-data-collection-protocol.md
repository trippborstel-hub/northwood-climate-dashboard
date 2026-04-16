# Climate Data Collection Protocol

CONFIDENTIAL -- Northwood Capital

**Effective:** Q1 2026
**Applies to:** All portfolio company climate/sustainability data submissions, GP-level climate analysis, board-level climate disclosures, and LP climate reporting.
**Owners:** VP of ESG & Sustainability, IR (LP disclosures)

---

## Purpose

Standardize climate data collection, analysis, and disclosure across the Northwood Capital portfolio. This protocol governs the flow of sustainability data from portfolio companies through GP-level analysis to LP disclosures.

Climate data at Northwood serves one purpose: quantifying the financial implications of climate risk and carbon exposure across the portfolio. Every metric collected, every analysis produced, and every disclosure issued ties back to a financial impact — margin effect, capex requirement, insurance cost, or exit multiple risk. Standalone ESG scores without financial context do not leave this firm.

---

## Data Architecture — Three-Tier Flow

Climate data flows in one direction: portfolio company submissions feed GP-level analysis, which feeds board materials and LP disclosures. Each tier has distinct access controls, quality standards, and output formats. Data never flows backward or sideways between portcos.

---

### Tier 1: Portfolio Company Submissions

**Location:** `portfolio/{portco}/climate/_submitted/`

What each portco's finance team provides to Northwood:

| Submission | Format | Content |
|---|---|---|
| Carbon collection template | CSV (`carbon-collection-template-{year}.csv`) | Annual energy consumption: electricity (kWh by facility), natural gas (therms by facility), fuel (gallons by vehicle/equipment type) |
| Facility specifications | Section within carbon template | Facility addresses, square footage, occupancy type (owned/leased), HVAC system type, any changes (new locations, closures, expansions) |
| Climate questionnaire | Structured form (annual) | Governance: board/management oversight of climate. Risk awareness: identified physical and transition risks. Targets: any emission reduction commitments. Initiatives: efficiency projects, renewable procurement, fleet changes |
| Incident reports | Ad hoc, within 5 business days of occurrence | Environmental violations, spills, regulatory citations, permit exceedances, environmental enforcement actions |

**Rules:**

1. **Portco data stays in its own folder.** Submitted data for Meridian lives in `portfolio/meridian-business-solutions/climate/_submitted/`. It is never cross-referenced with another portco's raw submissions. Analysis happens at the GP level (Tier 2), not by comparing raw portco files.
2. **Portco contacts see only their own data.** A portco CFO or Controller sees their own `_submitted/` folder and their own `_board-materials/` folder. They never see GP-level analytics, other portco data, or portfolio aggregates.
3. **Submission deadline: March 15 annually** for the prior calendar year. Late submissions delay the portfolio carbon footprint report and are flagged to the deal lead.
4. **Data quality hierarchy:**
   - **Grade A — Utility bills.** Actual consumption data from utility invoices. Preferred source. No estimation required.
   - **Grade B — Accounting estimates.** Derived from financial records (e.g., natural gas expense divided by average rate per therm). Acceptable with methodology documentation.
   - **Grade C — Landlord/proxy data.** Landlord-reported building averages, EPA benchmarks applied to square footage, or industry intensity factors applied to revenue. Last resort. Must be flagged as proxy data in all downstream analysis.

Every data point in the submission carries a quality grade. Grade C data triggers a note in the portco's emissions baseline and board materials.

---

### Tier 2: GP Climate Analysis

**Location:** `portfolio/{portco}/climate/_analysis/`

What Northwood's climate team produces from portco submissions:

**Emissions Baseline**

| Output | Methodology | Granularity |
|---|---|---|
| Scope 1 emissions (mt CO2e) | Direct combustion: natural gas, fuel, refrigerants. EPA Emission Factors (2023) applied to reported consumption | By facility, by source, total |
| Scope 2 emissions (mt CO2e) | Purchased electricity. EPA eGRID (2022) emission factors by state/subregion applied to reported kWh | By facility, total |
| Emissions intensity | Total Scope 1+2 divided by revenue ($M) and by headcount | Portfolio-comparable metrics |

**Climate Risk Assessment**

Every risk finding is expressed in financial terms. No standalone environmental metrics without dollar impact.

| Risk Category | Assessment Approach | Financial Expression |
|---|---|---|
| Physical risk — extreme weather | Facility locations mapped against FEMA NFHL flood zones, NOAA hurricane corridors, First Street Foundation forward-looking risk scores | Insurance cost trajectory (annual premium trend), business continuity exposure (estimated revenue-days at risk), capex for hardening or relocation |
| Transition risk — regulatory | Current and pending carbon pricing, state-level emissions regulations, industry-specific mandates | Regulatory cost exposure ($/year under current and proposed rules), energy transition capex ($M for equipment/fleet conversion), stranded asset risk (write-down exposure if carbon-intensive assets lose value) |
| Financial impact summary | Aggregated across physical and transition risk | Margin impact (bps), capex requirements ($M over hold period), exit multiple risk (turns — does climate exposure depress buyer appetite?) |

**Reduction Action Plan**

Prioritized list of emission reduction initiatives for each portco, ranked by financial return:

| Field | Description |
|---|---|
| Initiative | Specific action (e.g., LED retrofit, HVAC upgrade, fleet electrification, renewable energy procurement) |
| Estimated reduction (mt CO2e) | Annual emission reduction from initiative |
| Implementation cost ($) | Total capex or contract cost |
| Annual savings ($) | Energy cost reduction or incentive value |
| Payback period (years) | Implementation cost / annual savings |
| ROI | Annualized return on investment |
| Priority | Rank by ROI — highest-return initiatives first |

**Portco Climate Scorecard**

Scoring dimensions aligned to the firm's ESG framework:

| Dimension | What It Measures |
|---|---|
| E1 — Physical Climate Risk | Facility exposure to extreme weather; insurance adequacy; business continuity preparedness |
| E2 — Transition Risk | Carbon intensity; regulatory exposure; customer base transition vulnerability |
| E3 — Environmental Liability | Environmental compliance history; contamination risk; remediation obligations |

Scored 1–5 per the ESG Risk Assessment Methodology. Financial impact quantified for each dimension.

**Rules:**

1. **Analysis draws from submissions plus external sources.** Portco-submitted data is the primary input. External data — FEMA flood maps, EPA eGRID factors, industry benchmarks, First Street Foundation scores — supplements and contextualizes. Both sources are cited.
2. **Every figure traced to a source.** A submitted CSV row, an external database with retrieval date, or a documented assumption with methodology. No orphan numbers. Same standard as the firm's QA protocol (Check 1: Source Verification).
3. **Risk analysis always includes financial quantification.** "Flood zone exposure" is not a finding. "$1.2M estimated annual insurance premium increase and 12 revenue-days at risk from 100-year flood event" is a finding.
4. **Analysis updated annually after data collection.** Baseline and risk assessments refreshed each year after March 15 submissions are validated. Interim updates issued if material events occur — facility acquisition, environmental incident, regulatory change.

---

### Tier 3: Board-Level Disclosure

**Location:** `portfolio/{portco}/climate/_board-materials/`

What goes to each portco's board:

| Deliverable | Frequency | Aligned To |
|---|---|---|
| Climate review deck | Annual | Q4 board meeting |

**Content:**

- Emissions summary: Scope 1 + Scope 2 totals, year-over-year change, intensity metrics
- Risk profile: physical and transition risk findings, expressed in financial terms
- Action plan progress: status of reduction initiatives, actual vs. planned savings
- Peer benchmarking: portco performance against industry intensity benchmarks (public data only — no cross-portfolio comparisons)

**Rules:**

1. **Board materials are portco-specific only.** A Meridian board deck contains Meridian data. It never includes Sterling data, Clearview data, or portfolio aggregates. No cross-portfolio comparisons. No GP-level analytics.
2. **Language calibrated for board/management audience.** Plain financial language. Not technical climate jargon. A board member should understand every page without a glossary.
3. **Financial framing mandatory.** Every climate metric on every slide ties to a financial impact. "Scope 1 emissions: 2,340 mt CO2e" appears alongside "Estimated carbon cost exposure under proposed EPA rule: $85K/year." The emission number alone is insufficient.
4. **Format follows board deck template.** HTML or PDF per `_reference/deliverable-standards.md`. Consistent with the portco's quarterly board deck design system.

---

## GP-Level Aggregation

**Location:** `esg/`

Cross-portfolio analytics visible only to the Northwood investment team and IC:

| Output | Description | Update Frequency |
|---|---|---|
| Portfolio emissions dashboard | Total Scope 1+2 across all portcos. Breakdown by portco, by sector, by fund. Revenue and headcount intensity metrics | Annual (post-April 15 carbon footprint completion) |
| Climate risk heatmap | All portcos scored on physical + transition risk dimensions, plotted against financial materiality (margin impact, exit multiple risk) | Annual |
| Portfolio scorecard | Quarterly ESG dimension scores (E1/E2/E3) by portco. Trend tracking: improving, stable, deteriorating | Quarterly |
| Reduction tracking | Portfolio-wide progress against emission reduction targets. Aggregate savings from implemented initiatives | Annual |

**Rules:**

1. **GP-level analytics aggregate across all portcos.** This is the cross-portfolio view that does not exist at any other tier. It is the basis for portfolio-level climate strategy and LP disclosures.
2. **Access restricted to Northwood investment team.** Managing Partners, Partners, Principals, Operating Partners, VP of ESG, CFO, IR. Never shared with portco management teams or portco boards.
3. **LP disclosures derived from GP-level analytics.** LPs receive aggregated portfolio data processed through the GP tier — never raw portco submissions, never portco-level analysis files.

---

## LP Disclosure

**Location:** `esg/outputs/lp-disclosures/`

What LPs receive:

| Deliverable | Vehicle | Timing |
|---|---|---|
| Annual climate report | Standalone document, TCFD-aligned structure | Distributed with Q4 LP letter |
| Climate section in LP letter | Section within quarterly LP letter | Q4 annually |
| Annual Meeting presentation | Climate slides within AGM deck | Annual Meeting |

**Content — Minimum Viable Disclosure:**

- Portfolio emissions summary: aggregate Scope 1 + Scope 2, intensity metrics, year-over-year trend
- Risk overview: portfolio-level physical and transition risk profile (aggregated, not portco-specific)
- Initiatives: summary of reduction actions underway across the portfolio
- Targets: any portfolio-level emission reduction commitments and progress

**Rules:**

1. **No individual portco names unless specifically authorized.** Default: use sector and size descriptors ("a $150M revenue environmental services platform" rather than "Clearview Environmental"). Portco naming requires Managing Partner approval on a per-disclosure basis.
2. **Qualification language required.** Every LP climate disclosure includes: "Emissions data reflects management estimates based on portfolio company-reported energy consumption and EPA emission factors. Data has not been independently verified by a third-party assurance provider."
3. **TCFD alignment.** Annual climate report structured per TCFD recommended disclosures: Governance, Strategy, Risk Management, Metrics and Targets. Northwood does not claim full TCFD compliance — the report follows the framework as a structuring tool.
4. **IR owns LP distribution.** VP of ESG produces the content. IR (Jennifer Park) reviews for LP audience calibration and distributes through standard LP communication channels.

---

## Calendar

| Date | Activity | Owner |
|---|---|---|
| January 15 | Send carbon collection templates to portco finance teams | VP of ESG |
| March 15 | Portco data submission deadline | Portco CFO/Controller |
| March 15 – April 1 | Data validation, gap analysis, proxy estimation for incomplete data | VP of ESG |
| April 15 | Portfolio carbon footprint report complete (all portcos, portfolio aggregate) | VP of ESG |
| May 1 | Portco climate risk assessments updated (physical + transition risk, financial impact) | VP of ESG + Deal Lead |
| June 1 | GP portfolio climate analytics refreshed (dashboard, heatmap, scorecard) | VP of ESG |
| Q4 Board Meeting | Portco board climate review decks distributed to respective boards | VP of ESG + Deal Lead |
| Q4 LP Letter | Climate disclosure section drafted and included in LP letter | IR + VP of ESG |
| Annual Meeting | Full climate report presented to LPs | IC Chair + VP of ESG |

---

## Data Sources

| Source | Use | Location |
|---|---|---|
| Carbon collection template | Portco energy and fuel consumption data | `_data/carbon/carbon-collection-template-{year}.csv` |
| EPA Emission Factors (2023) | Scope 1 combustion emission calculations (natural gas, fuel, refrigerants) | Embedded in `tools/carbon_footprint.py` |
| EPA eGRID (2022) | Scope 2 electricity emission factors by state and subregion | Embedded in `tools/carbon_footprint.py` |
| FEMA NFHL | Flood zone assessment for facility physical risk mapping | External — fema.gov/flood-maps |
| NOAA Hurricane Data | Physical risk — historical and projected storm exposure by facility location | External — nhc.noaa.gov |
| First Street Foundation | Forward-looking physical risk scores (flood, fire, heat, wind) | External — firststreet.org |
| Industry benchmarks | Emissions intensity comparisons by sector and revenue band | EPA GHGRP, ENERGY STAR Portfolio Manager |
| Portco financial data | Revenue, EBITDA, headcount for intensity metric denominators | `portfolio/{portco}/financial-reporting/` |

---

## Quality Standards

All climate deliverables follow the firm's four-check QA protocol defined in `_reference/qa-protocol.md`:

### 1. Source Verification

Every emission figure traced to a CSV row or documented proxy assumption. Acceptable source chain:

| Source Type | Citation Format | Example |
|---|---|---|
| Utility bill data (Grade A) | `[Carbon Template, {Year}, Row {N}]` | `[Carbon Template, 2025, Row 14 — Facility: Chicago HQ, Electricity: 847,200 kWh]` |
| Accounting estimate (Grade B) | `[Accounting Estimate, Methodology: {description}]` | `[Accounting Estimate, Methodology: Annual gas expense $42,300 / avg rate $1.05/therm = 40,286 therms]` |
| Proxy data (Grade C) | `[Proxy, Source: {source}, Assumption: {description}]` | `[Proxy, Source: ENERGY STAR avg 22.5 kBtu/sq ft, Assumption: 15,000 sq ft leased office]` |
| Emission factor | `[EPA {Factor Set}, {Year}]` | `[EPA eGRID 2022, RFCW subregion: 0.000414 mt CO2e/kWh]` |
| External risk data | `[{Source}, Retrieved {Date}]` | `[FEMA NFHL, Retrieved 2026-03-20, Zone AE — 1% annual flood probability]` |

### 2. Structural Consistency

- Portco emission totals (Scope 1 + Scope 2) must sum to the portfolio total in the GP-level dashboard. No rounding discrepancies.
- Emissions intensity metrics must be consistent with financial data: if the dashboard shows Meridian revenue of $225.0M and emissions of 3,150 mt CO2e, the intensity must be 14.0 mt/$M — not 13.8 or 14.2 from a different revenue figure.
- Year-over-year changes must reconcile: prior year figures in the current report must match the prior year's final report exactly.

### 3. Adversarial Review

- Risk assessments stress-tested against alternative scenarios. If physical risk is scored low because facilities are outside flood zones, challenge: what about supply chain exposure, customer facility risk, or employee commute disruption?
- Emission reduction projections challenged against implementation track record. If no initiatives were completed last year, a plan showing 15% reduction next year requires justification.
- Financial impact estimates tested against comparable situations. If regulatory cost exposure is estimated at $50K/year, verify against actual costs at peer companies or other portcos facing similar regulations.

### 4. Assumption Flagging

- Every proxy estimate flagged with methodology and quality grade (A/B/C).
- Data quality grades assigned at the facility level and aggregated to the portco level:
  - **Grade A portfolio company:** >80% of emissions calculated from utility bill data
  - **Grade B portfolio company:** >80% from utility bills or accounting estimates combined
  - **Grade C portfolio company:** >20% of emissions rely on proxy/landlord data
- Portco-level data quality grade appears in the emissions baseline, board materials, and GP dashboard. LP disclosures reference the portfolio-level data quality distribution.

---

## Revision History

| Version | Date | Author | Changes |
|---|---|---|---|
| v1.0 | 2026-Q1 | VP of ESG & Sustainability | Initial protocol. Establishes three-tier data flow, collection standards, analysis methodology, disclosure requirements, and calendar. |

---

*This protocol is owned by the VP of ESG & Sustainability. Updates require IC Chair (Catherine Zhao) and IR (Jennifer Park) approval for any changes affecting LP disclosure content or timing.*
*Northwood Capital | Chicago, IL | Confidential*
