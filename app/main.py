from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api import entries, expenses, stats

app = FastAPI(
    title="Aura API"
)

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entries.router)
app.include_router(expenses.router)
app.include_router(stats.router)

app.mount(
    "/",
    StaticFiles(
        directory="frontend/dist",
        html=True
    ),
    name="frontend"
)