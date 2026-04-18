# _reference/ — Kith Consulting Institutional Knowledge

This folder contains the domain knowledge, methodologies, templates, and frameworks that make Kith's work *Kith's work*. Claude Code reads from this folder to produce output that reflects Kith's actual approach — not generic consulting.

## Folder Structure

### methodology/
How Kith does the technical work. Calculation approaches, data handling protocols, and standards references.

- `ghg-protocol-approach.md` — Kith's specific GHG Protocol implementation: which scopes, which emission factor databases, how to handle data gaps and estimation, boundary-setting conventions
- `scope3-screening-methodology.md` — How Kith conducts Scope 3 category screening: spend-based vs. activity-based, materiality thresholds, which of the 15 categories to prioritize by sector
- `emission-factors.md` — Which emission factor sources Kith uses (EPA, IEA, DEFRA), hierarchy of preference, how to handle geography-specific vs. global factors, update cadence
- `bau-modeling-approach.md` — How Kith builds BAU projections: growth assumption sourcing, grid decarbonization treatment, projection horizons (2030/2050), sensitivity parameters
- `sbti-target-setting-guide.md` — Kith's approach to science-aligned targets: absolute contraction vs. sectoral decarbonization, interim vs. long-term, how to position SBTi as reference without formal commitment
- `decarbonization-pathways.md` — Lever library by sector, top-down assumption ranges for capex/opex/savings, how to size levers against portco financials

### templates/
What Kith deliverables look like. Structure, format, and content standards for each deliverable type.

- `data-gap-assessment-template.md` — Structure and format for a climate data gap assessment: what fields, how to rate data quality, how to present gaps vs. available data
- `data-collection-template.md` — The reusable quarterly data collection template sent to portco owners: what to ask for, format, instructions
- `dashboard-design-standards.md` — How Kith designs climate dashboards: portco-level vs. fund-level views, key metrics to show, visualization conventions, interactivity expectations
- `bau-model-template.md` — Structure of the BAU and decarbonization pathway model: inputs, calculations, outputs, scenario parameters
- `financial-impact-template.md` — How Kith presents decarbonization costs and savings against portco financials: P&L mapping, EBITDA impact framing, CapEx sizing

### frameworks/
How Kith connects climate to PE value creation. The conceptual frameworks that differentiate Kith's thinking.

- `climate-value-bridge.md` — How Kith connects climate metrics to PE value creation: the framework for translating emissions data into financial impact, exit positioning, and LP narrative
- `portco-prioritization-framework.md` — Criteria and methodology for selecting which portfolio companies to focus on: status spectrum, sector diversity, data readiness, value-at-stake
- `pe-operating-rhythm-integration.md` — How climate deliverables plug into PE operating cadences: board meetings, operating reviews, IC memos, LP quarterly updates, exit prep

### voice/
How Kith communicates. Tone, terminology, and formatting conventions.

- `tone-and-terminology.md` — Kith's writing voice: precise but not academic, PE-native language, terms to use and avoid (e.g., "gap assessment" not "audit", "data pond" not "data lake")
- `slide-formatting-guide.md` — Visual and structural conventions for Kith presentations: color palette, typography, slide structure, how much text per slide
- `proposal-structure.md` — How Kith structures engagement proposals: slide order, framing approach (needs-first, not capabilities-first), what to include and what to leave out

---

## How to Use This Folder

**Populate these files** with Kith's actual methodologies, templates, and frameworks as they develop. Each file is a placeholder with a description of what should go in it. Replace the placeholder content with real content as it becomes available.

**Claude Code reads these files** when producing deliverables. The more specific and detailed the content here, the more Kith-specific the output will be. Generic placeholder content produces generic output.

**Update as the firm evolves.** These files are living documents. As Kith refines its methodology through engagements like Northwood, update the reference files so future work builds on what was learned.
