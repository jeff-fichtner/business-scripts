"""
Shared config loader for business scripts.

Usage:
    from lib.config import load_config

    config = load_config()
    # Access shared paths
    config["paths"]["expense_tracker"]
    # Access script-specific settings
    config["import_expenses"]["default_status"]
"""

import json
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"
SETTINGS_FILE = CONFIG_DIR / "settings.json"
CREDENTIALS_FILE = CONFIG_DIR / "credentials.json"


def load_config() -> dict:
    """Load settings.json from config/. Returns the full config dict."""
    if not SETTINGS_FILE.exists():
        raise FileNotFoundError(f"Settings file not found: {SETTINGS_FILE}")
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def load_credentials() -> dict:
    """Load credentials.json from config/. Returns empty dict if file doesn't exist."""
    if not CREDENTIALS_FILE.exists():
        return {}
    with open(CREDENTIALS_FILE, "r") as f:
        return json.load(f)


def resolve_path(relative_path: str) -> Path:
    """Resolve a path relative to the scripts/ directory."""
    base = Path(__file__).resolve().parent.parent
    return (base / relative_path).resolve()
