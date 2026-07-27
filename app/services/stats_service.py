
from collections import Counter
from app.services.entry_service import EntryService


class StatsService:

    def __init__(self):
        self.entry_service = EntryService()


    def get_stats(self):
        entries = self.entry_service.get_entries()

        if not entries:
            return None

        total_entries = len(entries)

        average_energy = (
            sum(entry.energy for entry in entries)
            / total_entries
        )

        mood_counter = Counter(
            entry.mood
            for entry in entries
        )
        favourite_mood = mood_counter.most_common(1)[0][0]

        song_counter = Counter(
            entry.song
            for entry in entries
        )
        favourite_song = song_counter.most_common(1)[0][0]

        total_expense = sum(
            expense.amount
            for entry in entries
            for expense in entry.expenses
        )

        category_counter = Counter()

        for entry in entries:
            for expense in entry.expenses:
                category_counter[
                    expense.category
                ] += expense.amount

        biggest_category = None
        if category_counter:

            biggest_category = max(
                category_counter,
                key=category_counter.get
            )

        return {

            "total_entries": total_entries,

            "average_energy": round(
                average_energy,
                2
            ),

            "favourite_mood": favourite_mood,

            "favourite_song": favourite_song,

            "total_expense": total_expense,

            "biggest_category": biggest_category

        }