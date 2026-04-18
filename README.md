# Northwood Climate Dashboard

The living workspace for Northwood Climate Program's 6-week climate data and strategy engagement with Northwood Capital Partners.

**Live site:** https://trippborstel-hub.github.io/northwood-climate-dashboard/

> Note: this directory is named `ridgepoint-proposal-site/` for historical reasons — it began as the RidgePoint engagement site and was repurposed as the canonical Northwood dashboard. The GitHub repo and live URL use the correct name.

## Structure

```
index.html              # Sidebar shell — loads pages into a single iframe
proposal.html           # Engagement proposal
data-analysis.html      # Step 1 router (links to step1/ deliverables)
esg-scorecard.html      # ESG scorecard (McKinsey 8-dimension framework)
carbon-inventory.html   # BAU & science-aligned targets
portco-financials.html  # Portfolio financial overview
step1/
  ├── index.html
  ├── deliverable-1-data-inventory.html
  ├── deliverable-2-data-quality.html
  ├── deliverable-3-error-log.html
  ├── deliverable-4-gap-analysis.html
  ├── deliverable-5-data-ask.html
  └── data-pond.html
internal/               # Reference materials (not in main nav)
_reference/             # Source data and Kith reference library
```

## Run locally

From the parent `claude-projects/` directory:

```bash
npx serve ridgepoint-proposal-site -p 5560
```

Then open http://localhost:5560.

If you're working in Claude Code, just ask Claude to "start the northwood-site server" — the launch config is already wired up in `claude-projects/.claude/launch.json`.

## Deploying changes

GitHub Pages builds from `main` automatically. To publish updates:

```bash
git add -A
git commit -m "Your change description"
git push
```

Pages typically rebuilds within 1–2 minutes.

## Editing rules

This directory is marked as protected in the parent project's `CLAUDE.md`. Future Claude Code sessions will not modify these files without explicit user direction. If changes are approved, the convention is to commit before and after the edit so there's a clean rollback point.
