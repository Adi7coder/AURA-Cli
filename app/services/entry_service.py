from app.models.entry import AuraEntry
from app.models.expense import Expense
from app.storage.json_storage import JSONStorage
from app.core.logger import logger
from datetime import date, datetime, timedelta
class EntryService:

    def __init__(self, storage: JSONStorage | None = None):
        self.storage = storage or JSONStorage()


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

    def search_entries(self, query: str) -> list[AuraEntry]:
        """
        Search Aura entries by
         date
         mood
         today's win
         song
         expense category
        """
        entries = self.get_entries()
        query = query.strip().lower()
        results = []

        if query == "today":
            today = date.today()
            return [
                entry
                for entry in entries
                if entry.date == today
            ]

        if query == "yesterday":
            yesterday = date.today() - timedelta(days=1)
            return [
                entry
                for entry in entries
                if entry.date == yesterday
            ]
        try:
            search_date = datetime.strptime(
                query,
                "%Y-%m-%%d"
            ).date()
            return [
                entry
                for entry in entries
                if entry.date == search_date
            ]
        except ValueError:
            pass

        for entry in entries:

            if (
                query in entry.mood.lower()
                or query in entry.win.lower()
                or query in entry.song.lower()
            ):
                results.append(entry)
                continue

            for expense in entry.expenses:
                if query in expense.category.lower():
                    results.append(entry)
                    break
        return results

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
            "Ehhh, No Aura entry found for today my boi. Commit today's aura first!"
        )
    def update_entry(
        self,
        field: str,
        value
    ) -> AuraEntry:
        """
        Alyt bruh let's update today's Aura entry.
        """
        entries = self.get_entries()
        for entry in entries:
            if entry.date == date.today():
                if hasattr(entry, field):
                    setattr(entry, field, value)
                    self.storage.save(
                        [
                            e.model_dump(mode="json")
                            for e in entries
                        ]
                    )
                    logger.info(
                        f"Updated {field} for {entry.date}"
                    )
                    return entry
                else:
                    raise ValueError(
                        f"Ehhh, No Aura entry field named '{field}' found bruh."
                    )