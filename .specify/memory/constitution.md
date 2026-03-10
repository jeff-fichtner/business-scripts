<!-- Sync Impact Report
  Version change: 0.0.0 → 1.0.0 (initial ratification)
  Added principles:
    - I. Shared Config Pattern
    - II. Script Simplicity
    - III. Data Safety
    - IV. Preserve Existing Artifacts
    - V. Local-First
  Added sections:
    - Technology Constraints
    - Development Workflow
    - Governance
  Templates requiring updates:
    - .specify/templates/plan-template.md ⚠ pending (no feature spec yet)
    - .specify/templates/spec-template.md ⚠ pending (no feature spec yet)
    - .specify/templates/tasks-template.md ⚠ pending (no feature spec yet)
  Follow-up TODOs: none
-->

# Business Scripts Constitution

## Core Principles

### I. Shared Config Pattern

Every script in this repository MUST follow the same configuration pattern:

1. Import `from lib.config import load_config`
2. Read its settings from a dedicated top-level key in `config/settings.json`
3. Use `config/credentials.json` for any API keys or secrets (gitignored)

Adding a new script = one `.py` file + one new key in `settings.json`. No new folders, no new config files. The `paths` key in settings.json is shared across all scripts for common file references.

**Rationale**: A single config surface keeps the repo navigable as script count grows and eliminates per-script configuration sprawl.

### II. Script Simplicity

Each script MUST be a single Python file at the repository root with a clear, singular purpose. Scripts MUST accept CLI arguments for runtime input (file paths, flags) and read static configuration from `settings.json`.

Shared utilities live in `lib/`. Frameworks are acceptable when explicitly relevant to the task, but MUST NOT be introduced to over-engineer a simple problem. Standard library plus minimal pip dependencies (`requirements.txt`).

**Rationale**: These are personal business automation scripts, not production services. Complexity is the enemy.

### III. Data Safety

Scripts MUST NOT overwrite or destroy source data. Bank CSV imports MUST be append-only to the target spreadsheet. Deduplication MUST prevent double-entry but MUST NOT delete existing rows.

Files containing sensitive financial data (CSVs, OFX, QFX, QBO exports) MUST be gitignored. Credentials MUST never be committed.

**Rationale**: Financial data is irreplaceable. The spreadsheet is the source of truth; scripts are helpers, not owners.

### IV. Preserve Existing Artifacts

When writing to the expense tracker spreadsheet, scripts MUST preserve all existing sheets, formulas, formatting, and data. The Summary sheet's SUMIF/COUNTIF formulas MUST remain intact.

Scripts MUST only append to the Expense Log sheet and MUST NOT modify the Category Guide or Summary sheets.

**Rationale**: The spreadsheet was designed with working formulas and structure. Scripts extend it; they do not restructure it.

### V. Local-First

All scripts run locally. No cloud dependencies, no external services, no databases. File paths are resolved relative to the `scripts/` directory via `lib.config.resolve_path()`.

The only external interaction is reading exported files (bank CSVs) that the user manually downloads.

**Rationale**: Simplicity, privacy, and zero ongoing infrastructure cost.

## Technology Constraints

- **Language**: Python 3 (system or venv)
- **Dependencies**: Minimal; currently `openpyxl` for xlsx manipulation. All deps listed in `requirements.txt`.
- **Target files**: `../finance/2025/tax/LLC_Expense_Tracker_2025.xlsx` (path configured in `settings.json`)
- **Platform**: macOS (primary), should work on any POSIX system
- **No CI/CD**: Scripts are run manually by the user

## Development Workflow

- Scripts are developed and tested locally against real or sample data
- Each script MUST include `--help` or `-h` usage output via `argparse`
- New scripts MUST be documented with a usage section in README.md
- Bank-specific CSV parsers are configured in `settings.json` under `import_expenses.banks`, not hardcoded
- Category keyword mappings for auto-categorization live in `settings.json` under `import_expenses.category_keywords`

## Governance

This constitution governs all development in the `business/scripts` repository. Amendments require updating this file and incrementing the version per semver rules:

- **MAJOR**: Removing or redefining a core principle
- **MINOR**: Adding a new principle or section
- **PATCH**: Clarifications or wording fixes

All scripts and changes MUST comply with these principles. The CLAUDE.md file (if present) provides runtime agent guidance and MUST NOT contradict this constitution.

**Version**: 1.0.0 | **Ratified**: 2026-03-10 | **Last Amended**: 2026-03-10
