# Business Scripts

Local automation scripts for LLC bookkeeping and admin.

## Structure

```
scripts/
├── config/
│   ├── settings.json        # Shared config — paths, preferences, per-script settings
│   └── credentials.json     # API keys (gitignored, never committed)
├── lib/
│   └── config.py            # Shared config loader — all scripts import from here
├── import_expenses.py       # (planned) Bank CSV → expense tracker spreadsheet
└── requirements.txt
```

## Adding a new script

1. Create `your_script.py` in the root of this directory
2. Add a config section to `config/settings.json` under a key matching your script name
3. Import shared config:

```python
from lib.config import load_config
config = load_config()
my_settings = config["your_script"]
```

## Setup

```bash
pip install -r requirements.txt
```
