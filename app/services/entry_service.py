from app.models.entry import AuraEntry
from app.models.expense import Expense
from app.storage.json_storage import JSONStorage
from app.core.logger import logger
from datetime import date

class EntryService:

    def __init__(self):
        self.storage = JSONStorage()



    def get_entries(self) -> list[AuraEntry]:
        """
         Alyt, lemme fetch da lore frm da vault...
    
        """

        data = self.storage.load()

        return [
            AuraEntry.model_validate(entry)
            for entry in data
        ]



    def add_entry(self, entry: AuraEntry) -> None:
        """
        Log today's lore bruh.
        """

        entries = self.get_entries()

        if any(existing.date == entry.date for existing in entries):
            raise ValueError(
                "Ayo, today's aura is aldy locked in!"
            )

        entries.append(entry)

        self.storage.save(
            [
                e.model_dump(mode="json")
                for e in entries
            ]
        )

        logger.info(
            f"Lore updated for {entry.date}"
        )

    def get_entry_by_date(self, entry_date: date) -> AuraEntry | None:

        entries = self.get_entries()
        for entry in entries:
            if entry.date == entry_date:
                return entry

        return None


    def get_history(self) -> list[AuraEntry]:
    
        entries = self.get_entries()
        return sorted(
            entries,
            key=lambda entry: entry.date,
            reverse=True
        )
    def add_expense(self, amount: float, category: str) -> None:
        """
        Add an expense to today's Aura entry.
        """

        entries = self.get_entries()
        for entry in entries:
            if entry.date == date.today():
                entry.expenses.append(
                    Expense(
                        amount=amount,
                        category=category
                    )
                )

                self.storage.save(
                    [
                        e.model_dump(mode="json")
                        for e in entries
                    ]
                )

                logger.info(
                    f"Added ₹{amount} under {category}"
                )

                return

        raise ValueError(
            "No Aura entry found for today. Commit today's aura first!"
        )