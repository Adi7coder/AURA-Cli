from datetime import date
from pydantic import BaseModel
from app.models.expense import Expense

class AuraEntry(BaseModel):
    date: date
    mood: str
    energy: int
    win: str
    song: str
    expenses: list[Expense] = []