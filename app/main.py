from fastapi import FastAPI
from app.api import entries, expenses, stats

app = FastAPI()
app.include_router(entries.router)
app.include_router(expenses.router)
app.include_router(stats.router)