Aura CLI

> A  CLI-based daily journal + expense tracker built while learning production grade python.

Aura is a personal command line application that lets you log your daily mood, wins, music, energy levels, and expenses while exploring real world backend development concepts such as layered architecture, data validation, configuration management, logging, and testing.
(Its simple but cool)
---

# Features..

-  Daily Aura Commit
  - Category
  - Mood
  - Energy Level
  - Today's Win
  - Song of the Day

-  Expense Tracker
  - Add multiple expenses
  - Categorize expenses
  - Append expenses to today's entry

-  History
  - View all previous Aura entries
  - Chronological ordering

-  Stats
  - Total entries
  - Average energy
  - Favourite mood
  - Favourite song
  - Total expenses
  - Highest spending category

-  Search feature
  - Search by date (`YYYY-MM-DD`)
  - Search today's entry
  - Search yesterday's entry
  - Search by mood
  - Search by today's win
  - Search by song
  - Search by expense category

-  Editing Entries Feature
  - Update today's mood
  - Update energy level
  - Update today's win
  - Update song

-  Env based Configuration

-  Logging Support

-  JSON based Storage

-  Automated Unit Testing using Pytest

---

# Project Structure

```
Aura
│
├── app
│   ├── cli
│   ├── core
│   ├── models
│   ├── services
│   └── storage
│
├── tests
├── data
├── logs
│
├── README.md
├── .env
├── .gitignore
└── requirements.txt
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
```
git clone git@github.com:Adi7coder/AURA-Cli.git
```
For users without SSH
```bash
git clone https://github.com/Adi7coder/AURA-Cli.git
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

Add expenses to today's entry
```bash
python -m app.cli.main expense
```

View all previous entries
```bash
python -m app.cli.main history
```
Search Aura entries
```bash
python -m app.cli.main search <query>
```
Example runs
```bash
python -m app.cli.main search today
python -m app.cli.main search yesterday
python -m app.cli.main search 2026-07-28
python -m app.cli.main search bella
python -m app.cli.main search food
```

Edit today's Aura entry
```bash
python -m app.cli.main edit
```

View overall statistics
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

# Concepts Practiced

- Layered Architecture
- Separation of Concerns
- Type Hints
- Pydantic Models
- Environment Variables
- JSON Serialization
- Logging
- Dependency Injection
- Service Layer Design
- CLI Development using Typer
- Error Handling
- Search Algorithms
- Dynamic Attribute Updates (`setattr`)
- Unit Testing with Pytest

---

# Testing

Aura currently includes automated unit tests using **Pytest**.

Covered functionality:

-  Add Aura Entry
-  Prevent Duplicate Entries
-  Search Entries
-  Update Existing Entries
-  Statistics Calculation

Run all tests
```bash
python -m pytest
```
---

# Roadmap
- [x] Daily Aura Commit
- [x] Expense Tracking
- [x] History
- [x] Statistics
- [x] Search Entries
- [x] Edit Entries
- [x] Environment-based Configuration
- [x] JSON Storage
- [x] Logging
- [x] Unit Testing with Pytest
### ---Aura CLI (Completed)---


- [ ] FastAPI Backend
- [ ] REST API Endpoints
- [ ] Interactive API Documentation (Swagger/OpenAPI)
- [ ] Docker Containerization
- [ ] Redis Integration
- [ ] Celery Background Tasks
- [ ] PostgreSQL Database
- [ ] Deployment
---

# Common Errors and Fixes

### `ModuleNotFoundError`

Ensure the virtual environment is activated.
```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

---

### `ImportError`

Usually caused by incorrect package imports or missing `__init__.py`.
Verify project structure and imports.

---

### `JSONDecodeError`

If `data/aura.json` becomes empty or corrupted, initialize it with:
```json
[]
```

---

### `ValidationError`

Ensure the `.env` file exists in the project root.
```
APP_NAME=Aura
DATA_PATH=data/aura.json
LOG_PATH=logs/aura.log
```

---

### `Pytest Import Errors`

Run tests from the project root.
```bash
python -m pytest
```
If imports fail, verify:
- `app/` is a package
- Virtual environment is activated

---

### `Git Authentication Failed`
GitHub no longer supports password authentication.
Use SSH authentication instead.

---

### `Non-fast-forward Push Rejected`
Your local and remote branches have diverged.

Synchronize them before pushing.

```bash
git pull --rebase origin main
git push origin main
```

---

### `JSONStorage() takes no arguments`
Occurs when tests use dependency injection but `JSONStorage` hasn't been updated.
Ensure the constructor accepts an optional storage path.

---

### `StatsService.__init__() takes 1 positional argument`
Refactor `StatsService` to support dependency injection.
```python
def __init__(
    self,
    entry_service=None
):
    self.entry_service = entry_service or EntryService()
```
---

# Current Status as of now...

Aura CLI (v1.0) is Completed

- Production-grade Python Fundamentals
- Layered Project Architecture
- CLI Development using Typer
- Configuration Management
- JSON Storage
- Logging
- Search
- Editing
- Automated Testing (Pytest)

Now will embark on these topics: 
- FastAPI
- Docker
- Redis
- Celery
- Backend Engineering

---


# Project Highlights
- Layered Architecture (CLI → Services → Storage → Models)
- Production oriented Python project structure
- Dependency Injection for improved testability
- 5 Automated Unit Tests
- Built while learning backend engineering concepts
  
# Author

**Aditya S Hegde**

