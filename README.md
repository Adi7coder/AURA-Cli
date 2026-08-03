# Aura

> A CLI based (for now...) daily journal + expense tracker built while learning Production Grade Python, FastAPI, React and other cool backend engineering topics...
Aura started off as a simple command line application and is gradually evolving into a  personal production project while I learn backend engineering concepts one by one.

---

# Features...

## CLI Features
- Daily Aura Commit
  - Date
  - Mood
  - Energy Level
  - Today's Win
  - Song of the Day

- Expense Tracker
  - Add multiple expenses
  - Categorize expenses
  - Append expenses to today's Aura entry

- History
  - View all previous Aura entries
  - Chronological ordering

- Stats
  - Total entries
  - Average energy
  - Favourite mood
  - Favourite song
  - Total expenses
  - Highest spending category

- Search feature
  - Search by date (`YYYY-MM-DD`)
  - Search today's entry
  - Search yesterday's entry
  - Search by mood
  - Search by today's win
  - Search by song
  - Search by expense category

- Editing Entries Feature
  - Update today's mood
  - Update energy level
  - Update today's win
  - Update today's song

---

## FastAPI Backend (newly unlocked...)
- REST API Endpoints
- Request Validation using Pydantic
- JSON Responses
- HTTP Exception Handling
- API Routing using APIRouter
- CORS Configuration
- Swagger/OpenAPI Documentation
- Dependency Injection using existing Service Layer

---

## React Frontend (still under construction...{i mean refinement})
- Beautiful Glassmorphism UI
- Daily Aura Commit Form
- Connected to FastAPI using Axios
- Component based architecture
- Responsive layout (more improvements coming...)

---

## Other Stuff
- Environment based Configuration
- JSON based Storage
- Logging Support
- Automated Unit Testing using Pytest

---

# Project Structure (still trying to keep it simple plzz)
```
Aura
│
├── app
│   ├── api
│   │   ├── entries.py
│   │   ├── expenses.py
│   │   └── stats.py
│   │
│   ├── cli
│   ├── core
│   ├── models
│   ├── services
│   └── storage
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── styles
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── tests
├── data
├── logs
│
├── README.md
├── requirements.txt
├── .env
└── .gitignore
```

---

# Tech Stack (for now...)

### Backend
- Python 3.12+
- FastAPI
- Uvicorn
- Typer
- Pydantic v2
- Pydantic Settings
- JSON
- Python Logging

### Frontend
- React
- Vite
- Axios
- HTML
- CSS

### Testing
- Pytest

### Version Control
- Git
- GitHub

(More coming soon...Docker, Redis, Celery, PostgreSQL)

---

# Getting Started (for someone who's just opened the folder)

Clone the repo
```bash
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

Create a virtual environment
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

Install Python dependencies
```bash
pip install -r requirements.txt
```

---

## Running the CLI
```bash
python -m app.cli.main commit
```

---

## Running the FastAPI Backend
```bash
python -m uvicorn app.main:app --reload
```
Swagger Documentation
```
http://127.0.0.1:8000/docs
```
Redoc
```
http://127.0.0.1:8000/redoc
```

---

## Running the React Frontend
Move into the frontend folder
```bash
cd frontend
```

Install dependencies
```bash
npm install
```

Start the development server
```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

(Currently the frontend supports Aura Commit...more features are being added as I learn.)

---

# Env Variables
Create a `.env` file in the project root.
```env
APP_NAME=Aura
DATA_PATH=data/aura.json
LOG_PATH=logs/aura.log
```

---

# Commands (to run ovbio...)
## CLI Commands

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

---

## FastAPI Endpoints

Launch the backend
```bash
python -m uvicorn app.main:app --reload
```

Swagger UI
```
http://127.0.0.1:8000/docs
```

Current Endpoints
```
GET     /entries/
POST    /entries/
PUT     /entries/{date}
DELETE  /entries/{date}
```
(More endpoints coming soon...)

---

## React Frontend

Run the frontend
```bash
cd frontend

npm install

npm run dev
```

Frontend
```
http://localhost:5173
```

---

# Data Storage (what goes where..again, for now)

Aura currently stores everything inside
```
data/aura.json
```

No database yet.

(PostgreSQL will eventually replace this once that part of the roadmap begins.)

---

# Concepts Practiced as per the roadmap given...

### Production Grade Python
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

### FastAPI
- FastAPI Project Structure
- APIRouter
- Request Validation
- REST API Design
- HTTP Methods
- Path Parameters
- JSON Responses
- Exception Handling
- CORS
- Swagger/OpenAPI Documentation

---

### Frontend
- React Fundamentals
- Component Based Architecture
- Props
- useState
- Axios
- React + FastAPI Integration
- Modern CSS
- Glassmorphism UI

---

# Testing

Aura currently includes automated unit tests using **Pytest**.
Covered functionality

- Add Aura Entry
- Prevent Duplicate Entries
- Search Entries
- Update Existing Entries
- Statistics Calculation

Run all tests
```bash
python -m pytest
```

(Currently 5 tests...more will be added as new backend features are built.)

---

# Roadmap
## Aura CLI

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

### ---- Aura CLI Completed ----

## FastAPI

- [x] FastAPI Backend
- [x] REST API Endpoints
- [x] Interactive API Documentation (Swagger/OpenAPI)
- [x] React Frontend Setup
- [x] React ↔ FastAPI Integration
- [ ] Complete all CRUD Endpoints
- [ ] History UI
- [ ] Statistics UI
- [ ] Expense Management UI

### ---- Currently Here ----

- [ ] Docker Containerization
- [ ] Redis Integration
- [ ] Celery Background Tasks
- [ ] Async Processing
- [ ] PostgreSQL Database
- [ ] Authentication
- [ ] Deployment

---

# Common Errors and Fixes (u can thank me later ;) .....)

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
If `data/aura.json` becomes empty or corrupted, initialize it with
```json
[]
```

---

### `ValidationError`
Ensure the `.env` file exists in the project root.
```env
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

If imports fail verify
- `app/` is a package
- Virtual environment is activated

---

### `CORS Error`
Usually happens when React tries talking to FastAPI.

Ensure FastAPI has
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
```

---

### `Axios Network Error`
Make sure the backend is actually running.
```bash
python -m uvicorn app.main:app --reload
```

---

### `404 Not Found`
Usually means the API endpoint doesn't exist or the frontend is pointing to the wrong URL.
Double check
```
/entries/
/stats/
/expenses/
```

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

### Completed

- Production Grade Python Fundamentals
- Layered Project Architecture
- CLI Development using Typer
- Configuration Management
- JSON Storage
- Logging
- Search
- Editing
- Automated Testing (Pytest)
- FastAPI
- REST API Design
- Swagger Documentation
- React Setup
- Axios Integration
- React ↔ FastAPI Communication
- Modern UI (still improving...)

Currently working on
- Completing the React frontend
- Docker
- Redis
- Celery
- Backend Engineering

---

# Project Highlights
- Layered Architecture (CLI → Services → Storage → Models)
- FastAPI Backend using APIRouter
- React Frontend
- REST API Design
- Swagger/OpenAPI Documentation
- Dependency Injection for improved testability
- JSON Persistence Layer
- Environment Based Configuration
- Logging
- 5 Automated Unit Tests
- Built while learning backend engineering concepts instead of just reading about them.

(Current goal: Slowly keep upgrading Aura while progressing through the backend roadmap.)

---

# Guess who built this.......

**Aditya S Hegde**

If you've read till here...
Thanks :)

Now excuse me while I go break something else and spend the next 3 hours figuring out why it broke....
