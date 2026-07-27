Aura CLI

> A  CLI-based daily journal + expense tracker built while learning production grade python.

Aura is a personal command line application that lets you log your daily mood, wins, music, energy levels, and expenses while exploring real world backend development concepts such as layered architecture, data validation, configuration management, logging, and testing.

---

# Features

-  Daily Aura Commit
  - Mood
  - Energy Level
  - Today's Win
  - Song of the Day

- Expense Tracker
  - Add multiple expenses
  - Categorize expenses
  - Append expenses to today's entry

-  History
  - View all previous Aura entries

-  Statistics
  - Total entries
  - Average energy
  - Favourite mood
  - Favourite song
  - Total expenses
  - Highest spending category

-  Environment-based Configuration
-  Logging Support
-  JSON-based Storage

---

# Project Structure

```
Aura/
│
├── app/
│   ├── cli/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── storage/
│
├── data/
├── logs/
├── tests/
│
├── .env
├── .gitignore
└── README.md
```

---

#  Tech Stack

- Python 3.12+
- Typer
- Pydantic v2
- Pydantic Settings
- JSON
- Python Logging
- Pytest
- Git & GitHub

---

#  Getting Started

Clone the repo
```bash
git clone https://github.com/<your-username>/AURA-Cli.git
```
Navigate into the project
```bash
cd AURA-Cli
```
Create a virtual env
```bash
python -m venv .venv
```
Activate it

### Windows

```bash
.venv\Scripts\activate
```
### Linux / macOS
```bash
source .venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

---

#  Env Variables

Create a `.env` file in the project root.
```
APP_NAME=Aura
DATA_PATH=data/aura.json
LOG_PATH=logs/aura.log
```

---

#  Commands

Create today's Aura
```bash
python -m app.cli.main commit
```

Add an expense
```bash
python -m app.cli.main expense
```

View history
```bash
python -m app.cli.main history
```

View statistics

```bash
python -m app.cli.main stats
```

---

#  Data Storage

Aura stores all entries inside
```
data/aura.json
```
No database is required for now.

---

#  Concepts Practiced

- Layered Architecture
- Separation of Concerns
- Type Hints
- Pydantic Models
- Environment Variables
- JSON Serialization
- Logging
- Dependency Management
- CLI Development
- Error Handling

---

#  Testing

(Currently it's under development)

Planned:
- Unit Tests
- Service Tests
- Storage Tests

---

# Roadmap

- [x] Daily Aura Commit
- [x] Expense Tracking
- [x] History
- [x] Statistics
- [ ] Search Entries
- [ ] Edit Entries
- [ ] Delete Entries
- [ ] Rich Terminal UI
- [ ] FastAPI Backend
- [ ] Docker
- [ ] Redis
- [ ] Celery
- [ ] PostgreSQL
- [ ] Deployment

---

#  Common Errors and their fixes

### `ModuleNotFoundError`
Make sure the virtual environment is activated and all dependencies are installed.
```
pip install -r requirements.txt
```

---

### `JSONDecodeError`
If `data/aura.json` becomes corrupted or empty, initialize it with:
```json
[]
```

---

### `ValidationError`
Ensure the `.env` file exists in the project root and contains:
```
APP_NAME=Aura
DATA_PATH=data/aura.json
LOG_PATH=logs/aura.log
```

---

### Git Authentication Failed
Use SSH authentication instead of GitHub password authentication.

---

#  Current Status as of now...
This project is being continuously improved while learning:
- Production Grade Python
- FastAPI
- Docker
- Redis
- Celery
- Backend Engineering

---

# Author

**Aditya S Hegde**

