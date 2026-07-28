from datetime import date
from app.models.entry import AuraEntry
from app.models.expense import Expense
from app.services.entry_service import EntryService
from app.services.stats_service import StatsService
from app.storage.json_storage import JSONStorage
import pytest

def sample_entry():
    return AuraEntry(
        date=date.today(),
        mood="Locked In",
        energy=9,
        win="Built Aura",
        song="Bella",
        expenses=[
            Expense(
                amount=250,
                category="Food"
            )
        ]
    )

def test_add_entry():
    storage = JSONStorage("tests/data/test_aura.json")
    storage.save([])
    service = EntryService(storage)
    service.add_entry(sample_entry())

    entries = service.get_entries()
    assert len(entries) == 1

def test_duplicate_entry():
    storage = JSONStorage("tests/data/test_aura.json")
    storage.save([])
    service = EntryService(storage)
    
    entry = sample_entry()
    service.add_entry(entry)
    with pytest.raises(ValueError):
        service.add_entry(entry)

def test_search_entries():
    storage = JSONStorage("tests/data/test_aura.json")
    storage.save([])
    service = EntryService(storage)
    service.add_entry(sample_entry())

    results = service.search_entries("bella")
    assert len(results) == 1
    assert results[0].song == "Bella"

def test_update_entry():
    storage = JSONStorage("tests/data/test_aura.json")
    storage.save([])
    service = EntryService(storage)
    service.add_entry(sample_entry())
    service.update_entry("mood","Chill")

    entry = service.get_entries()[0]
    assert entry.mood == "Chill"

def test_total_expenses():
    storage = JSONStorage("tests/data/test_aura.json")
    storage.save([])
    service = EntryService(storage)
    stats = StatsService(service)
    service.add_entry(sample_entry())

    stats = StatsService(service).get_stats()
    assert stats["total_expense"] == 250
