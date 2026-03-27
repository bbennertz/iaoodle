# Moodle WS Extractor — CLAUDE.md

## Project Overview

This project extracts data from the Moodle REST Web Service API and stores it locally for analysis, reporting, or integration with other systems.

## Stack

- **Language**: Python 3.11+
- **HTTP client**: `requests`
- **Data handling**: `pandas`
- **Config**: `python-dotenv` (`.env` file)
- **Testing**: `pytest`

## Project Structure

```
moodle-ws-extractor/
├── src/
│   ├── client.py          # MoodleClient: low-level API calls
│   ├── extractors/        # One module per Moodle entity
│   │   ├── users.py
│   │   ├── courses.py
│   │   ├── grades.py
│   │   └── activities.py
│   ├── models/            # Dataclasses / Pydantic models
│   └── utils/             # Shared helpers (pagination, rate-limit)
├── data/
│   ├── raw/               # JSON responses as received from API
│   └── processed/         # Cleaned / transformed output
├── scripts/               # Entry-point scripts (CLI)
└── tests/
```

## Key Conventions

- All Moodle API calls go through `src/client.py:MoodleClient`. Never call `requests` directly in extractors.
- Credentials and the Moodle URL are **always** read from `.env` (never hardcoded).
- Raw API responses are saved to `data/raw/` before transformation so reruns don't need extra API calls.
- Use dataclasses or Pydantic models in `src/models/` to represent domain objects.
- Extractor functions return a `list[Model]`; serialization happens in scripts.

## Environment Variables

```
MOODLE_URL=https://your-moodle-instance.example.com
MOODLE_TOKEN=your_ws_token_here
```

Generate a token at: **Site administration → Plugins → Web services → Manage tokens**

## Common Moodle WS Functions Used

| Function | Purpose |
|---|---|
| `core_user_get_users` | List all users |
| `core_course_get_courses` | List all courses |
| `gradereport_user_get_grade_items` | Get grades per user |
| `core_enrol_get_enrolled_users` | Get enrolled users per course |
| `mod_assign_get_assignments` | Get assignments |

## Running

```bash
# Install dependencies
pip install -r requirements.txt

# Copy and fill env
cp .env.example .env

# Run extraction
python scripts/extract.py
```

## Testing

```bash
pytest tests/
```
