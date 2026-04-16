#!/usr/bin/env python3
"""
Northwood Capital — Shared Utilities

Data abstraction layer and formatting helpers for deal pipeline and portfolio tools.
Primary data source: Supabase (northwood_capital schema).
Fallback: local JSON files (_reference/data-spine.json, _data/comp-data.json).

Set SUPABASE_URL and SUPABASE_ANON_KEY environment variables to enable Supabase mode.
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime


# ============================================================
# DATA ACCESS LAYER
# Supabase primary, JSON fallback.
# ============================================================

_SUPABASE_SCHEMA = "northwood_capital"
_supabase_client = None
_supabase_available = None


def _base_dir():
    """Return the northwood-capital root directory."""
    return Path(__file__).resolve().parent.parent


def _get_supabase():
    """Get or create the Supabase client. Returns None if unavailable."""
    global _supabase_client, _supabase_available
    if _supabase_available is False:
        return None
    if _supabase_client is not None:
        return _supabase_client

    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_ANON_KEY")
    if not url or not key:
        _supabase_available = False
        return None

    try:
        from supabase import create_client
        _supabase_client = create_client(url, key)
        _supabase_available = True
        return _supabase_client
    except Exception:
        _supabase_available = False
        return None


def _sb_select(table, columns="*", filters=None):
    """Query a Supabase table in the northwood_capital schema.

    Args:
        table: Table name.
        columns: Column selection string (default "*").
        filters: Optional dict of {column: value} for eq filters.

    Returns:
        List of row dicts, or None if Supabase is unavailable.
    """
    client = _get_supabase()
    if client is None:
        return None
    try:
        query = client.schema(_SUPABASE_SCHEMA).table(table).select(columns)
        if filters:
            for col, val in filters.items():
                query = query.eq(col, val)
        return query.execute().data
    except Exception:
        return None


def _sb_insert(table, data):
    """Insert a row into a Supabase table in the northwood_capital schema.

    Args:
        table: Table name.
        data: Dict of column values to insert.

    Returns:
        Inserted row dict, or None if Supabase is unavailable.
    """
    client = _get_supabase()
    if client is None:
        return None
    try:
        result = client.schema(_SUPABASE_SCHEMA).table(table).insert(data).execute()
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"[rc_utils] Supabase insert error: {e}")
        return None


def _sb_update(table, row_id, data):
    """Update a row in a Supabase table in the northwood_capital schema.

    Args:
        table: Table name.
        row_id: UUID of the row to update.
        data: Dict of column values to update.

    Returns:
        Updated row dict, or None if Supabase is unavailable.
    """
    client = _get_supabase()
    if client is None:
        return None
    try:
        result = (
            client.schema(_SUPABASE_SCHEMA)
            .table(table)
            .update(data)
            .eq("id", row_id)
            .execute()
        )
        return result.data[0] if result.data else None
    except Exception as e:
        print(f"[rc_utils] Supabase update error: {e}")
        return None


def load_spine():
    """Load the full data spine.

    Tries Supabase first — assembles the spine dict from multiple tables.
    Falls back to local JSON file.
    """
    # Try Supabase
    client = _get_supabase()
    if client is not None:
        try:
            config_rows = _sb_select("firm_config")
            team_rows = _sb_select("team_members")
            portco_rows = _sb_select("portfolio_companies")
            deal_rows = _sb_select("pipeline_deals")
            fund_rows = _sb_select("fund_performance")
            realized_rows = _sb_select("realized_investments")

            if config_rows is not None and team_rows is not None:
                spine = {}
                # Unpack firm_config JSONB rows
                for row in (config_rows or []):
                    spine[row["key"]] = row["value"]

                spine["team"] = team_rows or []

                # Portfolio companies keyed by slug
                portcos = {}
                for row in (portco_rows or []):
                    slug = row.pop("slug", row.get("id"))
                    portcos[slug] = row
                spine["portfolio_companies"] = portcos

                # Pipeline deals grouped by status
                pipeline_active, pipeline_passed, pipeline_monitoring = {}, {}, {}
                for row in (deal_rows or []):
                    codename = row.get("codename", "")
                    status = row.get("status", "active")
                    if status == "passed":
                        pipeline_passed[codename] = row
                    elif status == "monitoring":
                        pipeline_monitoring[codename] = row
                    else:
                        pipeline_active[codename] = row
                spine["pipeline_active"] = pipeline_active
                spine["pipeline_passed"] = pipeline_passed
                spine["pipeline_monitoring"] = pipeline_monitoring

                # Funds keyed by fund name
                funds = {}
                for row in (fund_rows or []):
                    funds[row.get("fund", "")] = row
                spine["funds"] = funds

                # Realized investments keyed by slug
                realized = {}
                for row in (realized_rows or []):
                    realized[row.get("slug", "")] = row
                spine["realized_investments"] = realized

                return spine
        except Exception:
            pass  # Fall through to JSON

    # Fallback: local JSON
    spine_path = _base_dir() / "_reference" / "data-spine.json"
    with open(spine_path) as f:
        return json.load(f)


def load_pipeline_deal(deal_id):
    """Load a pipeline deal by codename.

    Tries Supabase first, falls back to data spine JSON.
    """
    # Try Supabase direct query
    rows = _sb_select("pipeline_deals", filters={"codename": deal_id})
    if rows and len(rows) > 0:
        deal = rows[0]
        status = deal.get("status", "active")
        section_map = {"active": "pipeline_active", "passed": "pipeline_passed", "monitoring": "pipeline_monitoring"}
        deal["_section"] = section_map.get(status, "pipeline_active")
        deal["_deal_id"] = deal_id
        return deal

    # Fallback: JSON spine
    spine = load_spine()
    for section in ["pipeline_active", "pipeline_passed", "pipeline_monitoring"]:
        deal = spine.get(section, {}).get(deal_id)
        if deal:
            deal["_section"] = section
            deal["_deal_id"] = deal_id
            return deal

    raise ValueError(
        f"Deal '{deal_id}' not found in pipeline. "
        f"Available active deals: {list(spine.get('pipeline_active', {}).keys())}"
    )


def load_portco(slug):
    """Load a portfolio company by slug.

    Accepts either underscore format (meridian_business_solutions)
    or hyphen format (meridian-business-solutions).
    Tries Supabase first, falls back to data spine JSON.
    """
    underscore_slug = slug.replace("-", "_")

    # Try Supabase
    rows = _sb_select("portfolio_companies", filters={"slug": underscore_slug})
    if not rows:
        rows = _sb_select("portfolio_companies", filters={"slug": slug})
    if rows and len(rows) > 0:
        portco = rows[0]
        portco["_portco_id"] = portco.get("slug", underscore_slug)
        return portco

    # Fallback: JSON spine
    spine = load_spine()
    portcos = spine.get("portfolio_companies", {})

    if slug in portcos:
        portco = portcos[slug]
        portco["_portco_id"] = slug
        return portco

    if underscore_slug in portcos:
        portco = portcos[underscore_slug]
        portco["_portco_id"] = underscore_slug
        return portco

    for key, portco in portcos.items():
        if portco.get("portco_slug") == slug:
            portco["_portco_id"] = key
            return portco

    raise ValueError(
        f"Portfolio company '{slug}' not found. "
        f"Available: {list(portcos.keys())}"
    )


def load_comp_data():
    """Load comparable company data.

    Tries Supabase first (transaction_comps + trading_comps tables),
    falls back to _data/comp-data.json.
    Returns dict keyed by sector with transaction_comps and trading_comps lists.
    """
    tx_rows = _sb_select("transaction_comps")
    tr_rows = _sb_select("trading_comps")

    if tx_rows is not None and tr_rows is not None:
        sectors = {}
        for row in tx_rows:
            sector = row.get("sector", "Unknown")
            sectors.setdefault(sector, {"transaction_comps": [], "trading_comps": []})
            sectors[sector]["transaction_comps"].append(row)
        for row in tr_rows:
            sector = row.get("sector", "Unknown")
            sectors.setdefault(sector, {"transaction_comps": [], "trading_comps": []})
            sectors[sector]["trading_comps"].append(row)
        return {"sectors": sectors}

    # Fallback: local JSON
    comp_path = _base_dir() / "_data" / "comp-data.json"
    with open(comp_path) as f:
        return json.load(f)


def load_team():
    """Load team roster. Tries Supabase first, falls back to data spine JSON."""
    rows = _sb_select("team_members")
    if rows is not None:
        return rows

    spine = load_spine()
    return spine.get("team", [])


# ============================================================
# TEAM LOOKUP
# ============================================================

def resolve_team_member(member_id):
    """Resolve a team member ID to their full name and title."""
    team = load_team()
    for member in team:
        if member.get("id") == member_id:
            return {
                "id": member["id"],
                "name": member["full_name"],
                "title": member["title"],
            }
    return {"id": member_id, "name": member_id.replace("_", " ").title(), "title": ""}


def resolve_deal_team(deal):
    """Resolve all team members assigned to a deal."""
    members = []
    if "deal_lead" in deal:
        m = resolve_team_member(deal["deal_lead"])
        m["role"] = "Deal Lead"
        members.append(m)
    if "deal_support" in deal:
        m = resolve_team_member(deal["deal_support"])
        m["role"] = "Deal Support"
        members.append(m)
    return members


# ============================================================
# FORMATTING HELPERS
# Per deliverable-standards.md: Currency $X.XM (1 decimal),
# multiples X.Xx (1 decimal), margins XX.X% (1 decimal),
# IRR XX% (integer), negatives in parentheses.
# ============================================================

def fc(val, d=1):
    """Format currency in millions."""
    if val is None:
        return "N/A"
    if abs(val) < 0.05:
        return "$0.0M"
    if val < 0:
        return f"(${abs(val):,.{d}f}M)"
    return f"${val:,.{d}f}M"


def fp(val, d=1):
    """Format percentage."""
    if val is None:
        return "N/A"
    if val < 0:
        return f"-{abs(val):.{d}f}%"
    return f"{val:.{d}f}%"


def fm(val, d=1):
    """Format multiple."""
    if val is None:
        return "N/A"
    return f"{val:.{d}f}x"


def fd(val):
    """Format date string to Month DD, YYYY."""
    if val is None:
        return "N/A"
    try:
        dt = datetime.strptime(val, "%Y-%m-%d")
        return dt.strftime("%B %d, %Y")
    except (ValueError, TypeError):
        return str(val)


def fi(val):
    """Format integer with comma separator."""
    if val is None:
        return "N/A"
    return f"{int(val):,}"


# ============================================================
# SECTOR VALUATION RANGES
# From screening-criteria.md guardrails
# ============================================================

SECTOR_VALUATION_RANGES = {
    "Business Services": {"low": 7.0, "high": 10.0, "note": "Higher for 80%+ recurring"},
    "Healthcare Services": {"low": 8.0, "high": 11.0, "note": "Premium for non-discretionary demand"},
    "Industrial Technology": {"low": 6.0, "high": 9.0, "note": "Reflects capital intensity, cyclicality"},
    "Environmental Services": {"low": 7.0, "high": 10.0, "note": "Similar to business services"},
    "Technology Services": {"low": 8.0, "high": 11.0, "note": "Premium for recurring revenue"},
}

HARD_CEILING_MULTIPLE = 12.0


# ============================================================
# SECTOR MAPPING
# Maps deal sectors (which may be composite like "Business Services / IT Services")
# to comp-data.json sector keys.
# ============================================================

SECTOR_MAP = {
    "business services": "Business Services",
    "healthcare services": "Healthcare Services",
    "industrial technology": "Industrial Technology",
    "environmental services": "Environmental Services",
    "technology services": "Technology Services",
    "it services": "Technology Services",
    "dental": "Healthcare Services",
    "behavioral health": "Healthcare Services",
    "staffing": "Business Services",
    "testing": "Environmental Services",
    "specialty chemical": "Industrial Technology",
    "chemical distribution": "Industrial Technology",
    "automation": "Industrial Technology",
    "robotics": "Industrial Technology",
}


def map_sector_to_comp_keys(sector_string):
    """Map a deal's sector string to one or more comp-data.json sector keys.
    
    Handles composite sectors like 'Business Services / IT Services' 
    by splitting on '/' and matching each part.
    """
    if not sector_string:
        return []
    
    parts = [p.strip().lower() for p in sector_string.split("/")]
    matched = set()
    
    for part in parts:
        # Try exact match first
        if part in SECTOR_MAP:
            matched.add(SECTOR_MAP[part])
            continue
        # Try substring match
        for key, val in SECTOR_MAP.items():
            if key in part or part in key:
                matched.add(val)
    
    return list(matched) if matched else ["Business Services"]


# ============================================================
# MARKDOWN TABLE PARSER
# Robust parser for portco markdown files.
# Handles $X.XM, XX.X%, X.Xx, negatives in parens.
# ============================================================

def parse_number(text):
    """Parse a formatted number from markdown.
    
    Handles: $195.0M, 17.0%, 9.0x, (2.5), 580, $0.8M, -3.2%, N/A, N/M
    """
    if not text or not isinstance(text, str):
        return None
    
    text = text.strip()
    
    if text in ("N/A", "N/M", "—", "--", "-", ""):
        return None
    
    # Check for negative in parentheses
    negative = False
    if text.startswith("(") and text.endswith(")"):
        negative = True
        text = text[1:-1]
    elif text.startswith("-"):
        negative = True
        text = text[1:]
    
    # Remove currency symbol and suffixes
    text = text.replace("$", "").replace(",", "").strip()
    
    multiplier = 1.0
    if text.upper().endswith("M"):
        text = text[:-1]
    elif text.upper().endswith("B"):
        text = text[:-1]
        multiplier = 1000.0
    elif text.upper().endswith("K"):
        text = text[:-1]
        multiplier = 0.001
    
    # Remove percentage and multiple suffix
    text = text.replace("%", "").replace("x", "").strip()
    
    try:
        val = float(text) * multiplier
        return -val if negative else val
    except (ValueError, TypeError):
        return None


def parse_markdown_table(content, section_header=None):
    """Parse a markdown table from file content.
    
    Args:
        content: Full markdown file content as string.
        section_header: Optional H2/H3 header to find the table under.
                       If None, parses the first table found.
    
    Returns:
        List of dicts, one per row, with header names as keys.
    """
    lines = content.split("\n")
    
    # Find the section if specified
    start_idx = 0
    if section_header:
        for i, line in enumerate(lines):
            cleaned = line.strip().lstrip("#").strip()
            if cleaned.lower() == section_header.lower():
                start_idx = i
                break
    
    # Find table header row (line with |)
    header_idx = None
    for i in range(start_idx, len(lines)):
        line = lines[i].strip()
        if "|" in line and not line.startswith("#"):
            # Check if next line is separator (---|---)
            if i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1].strip()):
                header_idx = i
                break
    
    if header_idx is None:
        return []
    
    # Parse headers
    header_line = lines[header_idx].strip()
    headers = [h.strip() for h in header_line.split("|") if h.strip()]
    
    # Parse data rows (skip separator)
    rows = []
    for i in range(header_idx + 2, len(lines)):
        line = lines[i].strip()
        if not line or not line.startswith("|"):
            break
        cells = [c.strip() for c in line.split("|") if c.strip() != ""]
        if len(cells) >= len(headers):
            row = {}
            for j, header in enumerate(headers):
                row[header] = cells[j] if j < len(cells) else ""
            rows.append(row)
    
    return rows


# ============================================================
# FILE OUTPUT HELPERS
# ============================================================

def ensure_output_dir(subdir):
    """Ensure an output subdirectory exists under outputs/."""
    output_dir = _base_dir() / "outputs" / subdir
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def write_output(content, subdir, filename):
    """Write content to outputs/{subdir}/{filename}.
    
    Returns the full path of the written file.
    """
    output_dir = ensure_output_dir(subdir)
    filepath = output_dir / filename
    with open(filepath, "w") as f:
        f.write(content)
    return filepath


# ============================================================
# QA SUMMARY
# Per qa-protocol.md: every deliverable includes QA footer.
# ============================================================

def qa_summary_section(sources, checks_passed, assumptions=None, warnings=None):
    """Generate a QA summary section per qa-protocol.md.
    
    Args:
        sources: List of source citation strings, e.g. ["[Spine]", "[PitchBook, 2025]"]
        checks_passed: List of QA checks that passed.
        assumptions: Optional list of assumption labels.
        warnings: Optional list of warnings or flags.
    
    Returns:
        Formatted QA summary string.
    """
    lines = []
    lines.append("---")
    lines.append("")
    lines.append("## QA Summary")
    lines.append("")
    
    # Source verification
    lines.append("**Source Verification:**")
    for src in sources:
        lines.append(f"- {src}")
    lines.append("")
    
    # Structural consistency
    lines.append("**Structural Consistency:**")
    for check in checks_passed:
        lines.append(f"- [x] {check}")
    lines.append("")
    
    # Assumptions
    if assumptions:
        lines.append("**Assumptions Flagged:**")
        for assumption in assumptions:
            lines.append(f"- {assumption}")
        lines.append("")
    
    # Warnings
    if warnings:
        lines.append("**Warnings:**")
        for warning in warnings:
            lines.append(f"- {warning}")
        lines.append("")
    
    lines.append(f"*QA completed: {datetime.now().strftime('%B %d, %Y')}*")
    lines.append("")
    lines.append("CONFIDENTIAL -- Northwood Capital")
    
    return "\n".join(lines)


# ============================================================
# PORTCO FILE READERS
# Supabase for structured data (financials, KPIs).
# Markdown files for narrative content (status, memos, decks).
# ============================================================

def _read_file_safe(path):
    """Read a file, returning None if it doesn't exist."""
    try:
        with open(path) as f:
            return f.read()
    except (FileNotFoundError, OSError):
        return None


def load_portco_status(portco_slug):
    """Load portco-status.md for a portfolio company."""
    path = _base_dir() / "portfolio" / portco_slug / "portco-status.md"
    return _read_file_safe(path)


def load_portco_kpi_dashboard(portco_slug):
    """Load KPI data for a portfolio company.

    Tries Supabase first (portco_kpis table), returns structured data.
    Falls back to kpi-dashboard.md markdown file.
    """
    underscore_slug = portco_slug.replace("-", "_")
    rows = _sb_select("portco_kpis", filters={"portco": underscore_slug})
    if rows:
        return rows

    # Fallback: markdown file
    path = _base_dir() / "portfolio" / portco_slug / "financial-reporting" / "kpi-dashboard.md"
    return _read_file_safe(path)


def load_portco_monthly_package(portco_slug, year_month):
    """Load monthly financial data for a portfolio company.

    Tries Supabase first (portco_financials table), returns structured data.
    Falls back to monthly package markdown file.

    Args:
        portco_slug: e.g. 'novacare-health-partners' or 'novacare_health_partners'
        year_month: e.g. '2026-01'
    """
    underscore_slug = portco_slug.replace("-", "_")
    rows = _sb_select("portco_financials", filters={"portco": underscore_slug, "period": year_month})
    if rows:
        return rows

    # Fallback: markdown file
    path = _base_dir() / "portfolio" / portco_slug / "financial-reporting" / "monthly" / f"{year_month}-package.md"
    return _read_file_safe(path)


def load_portco_annual_budget(portco_slug, year=2026):
    """Load annual budget file."""
    path = _base_dir() / "portfolio" / portco_slug / "financial-reporting" / f"annual-budget-{year}.md"
    return _read_file_safe(path)


def load_portco_strategic_initiatives(portco_slug):
    """Load strategic-initiatives.md from value-creation."""
    path = _base_dir() / "portfolio" / portco_slug / "value-creation" / "strategic-initiatives.md"
    return _read_file_safe(path)


def load_portco_closing_summary(portco_slug):
    """Load closing-summary.md from acquisition."""
    path = _base_dir() / "portfolio" / portco_slug / "acquisition" / "closing-summary.md"
    return _read_file_safe(path)


def load_portco_board_deck(portco_slug, quarter="2025-q4"):
    """Load prior board deck from board-materials."""
    path = _base_dir() / "portfolio" / portco_slug / "board-materials" / f"{quarter}-board-deck.md"
    return _read_file_safe(path)


# ---------------------------------------------------------------------------
# Process Execution Logging
# ---------------------------------------------------------------------------
# These functions provide the public API for logging process runs and QA
# results to the northwood_capital.process_execution_log table in Supabase.
#
# Usage pattern (inside a process script):
#   exec_id = log_execution_start("board-deck", "NovaCare Health Partners",
#                                  input_files=["portco-status.md", "kpi-dashboard.md"])
#   ... run process, write output ...
#   log_execution_complete(exec_id, output_file="outputs/board-decks/novacare-2026-q1.md",
#                          output_type="markdown")
#   ... run QA checks ...
#   log_qa_results(exec_id, source_verification={...}, structural_consistency={...},
#                  adversarial_review={...}, assumption_flagging={...})
# ---------------------------------------------------------------------------

_EXEC_LOG_TABLE = "process_execution_log"


def _resolve_operator():
    """Build an operator identity string from the local environment.

    Combines OS username + hostname, and appends git user config if available.
    An RC_OPERATOR env var overrides everything.

    Examples:
        "benhi@DESKTOP-XYZ"
        "benhi@DESKTOP-XYZ (Ben H <ben@kith.com>)"
        "Diego Espinosa"  # if RC_OPERATOR is set
    """
    import os
    import socket
    import subprocess

    # 1. Check for explicit override
    override = os.environ.get("RC_OPERATOR", "").strip()
    if override:
        return override

    # 2. OS username + hostname (always available)
    try:
        username = os.getlogin()
    except OSError:
        username = os.environ.get("USERNAME") or os.environ.get("USER") or "unknown"
    hostname = socket.gethostname()
    identity = f"{username}@{hostname}"

    # 3. Append git user if configured
    try:
        git_name = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True, text=True, timeout=3
        ).stdout.strip()
        git_email = subprocess.run(
            ["git", "config", "user.email"],
            capture_output=True, text=True, timeout=3
        ).stdout.strip()
        if git_name and git_email:
            identity += f" ({git_name} <{git_email}>)"
        elif git_name:
            identity += f" ({git_name})"
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass  # git not installed or not configured — that's fine

    return identity


def log_execution_start(
    process_type,
    entity,
    input_files=None,
    input_params=None,
    triggered_by="user_request",
    operator=None,
    notes=None,
):
    """Log the start of a process execution. Returns the execution row ID (uuid str) or None on failure."""
    from datetime import datetime, timezone

    row = {
        "process_type": process_type,
        "entity": entity,
        "triggered_by": triggered_by,
        "operator": operator or _resolve_operator(),
        "started_at": datetime.now(timezone.utc).isoformat(),
        "exec_status": "running",
        "qa_status": "pending",
    }
    if input_files:
        row["input_files"] = input_files
    if input_params:
        row["input_params"] = input_params
    if notes:
        row["notes"] = notes

    result = _sb_insert(_EXEC_LOG_TABLE, row)
    if result:
        print(f"[rc_utils] Execution started — id={result['id']}  process={process_type}  entity={entity}")
        return result["id"]
    return None


def log_execution_complete(
    execution_id,
    output_file=None,
    output_type=None,
    output_version=1,
    notes=None,
):
    """Mark a running execution as completed and record its output metadata."""
    from datetime import datetime, timezone

    if not execution_id:
        print("[rc_utils] log_execution_complete called with no execution_id — skipping")
        return None

    data = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "exec_status": "completed",
    }
    if output_file:
        data["output_file"] = output_file
    if output_type:
        data["output_type"] = output_type
    if output_version is not None:
        data["output_version"] = output_version
    if notes:
        data["notes"] = notes

    result = _sb_update(_EXEC_LOG_TABLE, execution_id, data)
    if result:
        dur = result.get("duration_seconds")
        dur_str = f"{dur:.1f}s" if dur else "n/a"
        print(f"[rc_utils] Execution completed — id={execution_id}  duration={dur_str}")
    return result


def log_execution_failed(execution_id, error_message, notes=None):
    """Mark a running execution as failed and record the error."""
    from datetime import datetime, timezone

    if not execution_id:
        return None

    data = {
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "exec_status": "failed",
        "exec_error": str(error_message)[:2000],
        "qa_status": "skipped",
    }
    if notes:
        data["notes"] = notes

    result = _sb_update(_EXEC_LOG_TABLE, execution_id, data)
    if result:
        print(f"[rc_utils] Execution FAILED — id={execution_id}  error={error_message[:100]}")
    return result


def log_qa_results(
    execution_id,
    source_verification=None,
    structural_consistency=None,
    adversarial_review=None,
    assumption_flagging=None,
    warnings=None,
    blocking_issues=None,
):
    """Update an execution row with QA check results. Derives qa_status automatically."""
    from datetime import datetime, timezone

    if not execution_id:
        print("[rc_utils] log_qa_results called with no execution_id — skipping")
        return None

    data = {"qa_run_at": datetime.now(timezone.utc).isoformat()}

    if source_verification is not None:
        data["qa_source_verification"] = source_verification
    if structural_consistency is not None:
        data["qa_structural_consistency"] = structural_consistency
    if adversarial_review is not None:
        data["qa_adversarial_review"] = adversarial_review
    if assumption_flagging is not None:
        data["qa_assumption_flagging"] = assumption_flagging
    if warnings:
        data["qa_warnings"] = warnings
    if blocking_issues:
        data["qa_blocking_issues"] = blocking_issues

    # Derive overall QA status
    if blocking_issues:
        data["qa_status"] = "fail"
    elif warnings:
        data["qa_status"] = "pass_with_warnings"
    else:
        data["qa_status"] = "pass"

    result = _sb_update(_EXEC_LOG_TABLE, execution_id, data)
    if result:
        print(f"[rc_utils] QA logged — id={execution_id}  status={data['qa_status']}  "
              f"warnings={len(warnings or [])}  blocking={len(blocking_issues or [])}")
    return result
