import typer
from datetime import date

from app.models.entry import AuraEntry
from app.models.expense import Expense
from app.services.entry_service import EntryService
from app.services.stats_service import StatsService

app = typer.Typer()
entry_service = EntryService()

@app.command()
def Suii():
    print("Presenting The Suiiiperior... Aura")
@app.command()
def commit():
    typer.echo(" A U R A\n Boi's Daily Commits To Aura\n")
    category = typer.prompt("Category").strip().title()

    mood = typer.prompt("Mood").strip().title()
    while True:
        energy = typer.prompt("Energy (1-10)", type=int)

        if 1 <= energy <= 10:
            break

        typer.secho(
            "Ain't no way ur energy's trippin like that bruh",
            fg=typer.colors.RED
        )

    win = typer.prompt("Today's W")

    song = typer.prompt("Song of da Day").strip()

    expenses = []

    add_expense = typer.confirm("Did your wallet get lighter today?")

    while add_expense:
        amount = typer.prompt("Alyt, How much was it?", type=float)
        category = typer.prompt("What category bruh?").strip().title()

        expenses.append(
            Expense(
                amount=amount,
                category=category
            )
        )

        add_expense = typer.confirm("Anything else?")

    entry = AuraEntry(
        date=date.today(),
        mood=mood,
        energy=energy,
        win=win,
        song=song,
        expenses=expenses
    )

    EntryService().add_entry(entry)

    typer.secho(
        " Aura entry clocked Bruhh!!!",
        fg=typer.colors.GREEN
    )

@app.command()
def history():

    entries = entry_service.get_history()
    if not entries:
        typer.echo("Da vault's lkn empty bruh")
        return

    for entry in entries:

        typer.secho(
            f"\n {entry.date}",
            fg=typer.colors.CYAN
        )

        typer.echo(f" Moooood      : {entry.mood}")
        typer.echo(f" Energy    : {entry.energy}")
        typer.echo(f" Today's W : {entry.win}")
        typer.echo(f" Song      : {entry.song}")

        if entry.expenses:

            typer.echo("\nExpenses")

            for expense in entry.expenses:

                typer.echo(
                    f"• {expense.category:<20} ₹{expense.amount}"
                )

        typer.echo("\n" + "─" * 35)

from app.services.stats_service import StatsService
stats_service = StatsService()

@app.command()
def stats():

    stats = stats_service.get_stats()

    if not stats:

        typer.echo(
            "No Aura entries yet."
        )

        return

    typer.secho(
        "\n-----------AURA STATS ----------",
        fg=typer.colors.CYAN
    )

    typer.echo(
        f" Total clockins      : {stats['total_entries']}"
    )

    typer.echo(
        f" Avg Energy     : {stats['average_energy']}"
    )

    typer.echo(
        f" Fav Mood    : {stats['favourite_mood']}"
    )

    typer.echo(
        f" Fav Song    : {stats['favourite_song']}"
    )

    typer.echo(
        f" Total Expenses    : ₹{stats['total_expense']}"
    )

    typer.echo(
        f" Biggest Category  : {stats['biggest_category']}"
    )

    typer.secho(
        "---------------------------",
        fg=typer.colors.CYAN
    )

@app.command()
def search(query: str):
    """
    Search Aura entries.
    """
    results = entry_service.search_entries(query)

    if not results:
        typer.secho(
            "No matching Aura entries found buddy...",
            fg=typer.colors.RED
        )
        return

    for entry in results:
        typer.echo("\n" + "=" * 40)

        typer.echo(f" {entry.date}")
        typer.echo(f"Mood: {entry.mood}")
        typer.echo(f"Energy: {entry.energy}")
        typer.echo(f"Today's W: {entry.win}")
        typer.echo(f"Song: {entry.song}")

        if entry.expenses:
            typer.echo("\nExpenses:")

            for expense in entry.expenses:
                typer.echo(
                    f"• {expense.category} - ₹{expense.amount}"
                )

@app.command()
def edit():
    """
    Alyt make those changes...
    """

    typer.echo("\nEdit Today's Aura\n")

    typer.echo("1. Mood")
    typer.echo("2. Energy")
    typer.echo("3. Today's W")
    typer.echo("4. Song")

    choice = typer.prompt( "\nChoose an option to edit (1-4)", type=int)
    if choice == 1:

        field = "mood"

        value = typer.prompt(
            "Enter new mood"
        )

    elif choice == 2:

        field = "energy"

        value = typer.prompt(
            "Enter new energy",
            type=int
        )

    elif choice == 3:

        field = "win"

        value = typer.prompt(
            "Enter today's new W"
        )

    elif choice == 4:

        field = "song"

        value = typer.prompt(
            "Enter new song"
        )

    else:

        typer.secho(
            "Invalid choice.",
            fg=typer.colors.RED
        )

        return
    try:

        entry_service.update_entry(
            field,
            value
        )

        typer.secho(
            "Alyt bruh, tdy's Aura entry's updated...",
            fg=typer.colors.GREEN
        )

    except ValueError as e:

        typer.secho(
            str(e),
            fg=typer.colors.RED
        )


@app.command()
def expense():

    typer.echo("\n Drop some more receipts\n")

    amount = typer.prompt( 
        "Amount",
        type=float
    )

    category = typer.prompt(
        "Category"
    ).strip().title()

    entry_service.add_expense(
        amount,
        category
    )

    typer.secho(
        "Money vanished...Bruhh but at least it's tracked in Aura",
        fg=typer.colors.GREEN
    )
if __name__ == "__main__":
    app()