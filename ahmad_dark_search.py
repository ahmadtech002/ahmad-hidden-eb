import time
import random
from rich.console import Console
from rich.text import Text
from rich.progress import track
from rich.table import Table

# Console for rich animations
console = Console()

# Skull-themed ASCII Art
SKULL_ASCII_ART = """
       ______
    .-        -.
   /            \\
  |,  .-.  .-.  ,|
  | )(_o/  \o_)( |
  |/     /\     \|
  (_     ^^     _)
   \__|IIIIII|__/
    | \IIIIII/ |
    \          /
     `--------`
"""

# Expanded search results by category
SEARCH_RESULTS = {
    "Whispers": [
        "A voice calls out from the void, 'Help us...'",
        "A shadow speaks your name, but no one is there.",
        "The air grows colder; a whisper says, 'Turn back.'",
    ],
    "Portals": [
        "A swirling vortex appears before you. Enter?",
        "A rift tears open, revealing another dimension.",
        "A portal flickers with unstable energy. Proceed with caution.",
    ],
    "Artifacts": [
        "A glowing amulet lies on the ground. Take it?",
        "An ancient tome appears, written in an unknown language.",
        "A shard of glass hums with dark power. Do you dare touch it?",
    ],
    "Secrets": [
        "An ancient riddle whispers in your ear. Do you understand?",
        "A hidden compartment reveals a strange key.",
        "You find an old map, the markings incomprehensible.",
    ],
    "Echoes": [
        "You hear your own voice calling from the void.",
        "A melody plays faintly, evoking forgotten memories.",
        "A scream echoes, but its source remains unseen.",
    ],
}

def display_skull_intro():
    """Display skull-themed introduction with animated ASCII art."""
    for line in SKULL_ASCII_ART.split("\n"):
        console.print(Text(line, style="bold red"))
        time.sleep(0.1)
    console.print("[bold purple]Welcome to Ahmad's Dark Search Realm[/bold purple]\n", style="bold")
    time.sleep(1)

def search_dark_realm(query):
    """Simulate searching the dark abyss with animations, dynamic results, and Easter eggs."""
    # Easter eggs
    if query.lower() == "darkness":
        console.print("[bold magenta]You have summoned the eternal void...[/bold magenta]")
        return
    elif query.lower() == "truth":
        console.print("[bold yellow]The truth lies within yourself.[/bold yellow]")
        return

    # Simulate search animation
    console.print(f"[bold cyan]Searching the Dark Abyss for '{query}'...[/bold cyan]")
    time.sleep(1)

    for step in track(range(20), description=random.choice(["Piercing the shadows...", "Opening the veil...", "Revealing the abyss..."])):
        time.sleep(random.uniform(0.05, 0.15))

    # Display categorized results with dynamic result count
    table = Table(title="Ahmad's Dark Search Results")
    table.add_column("Category", justify="center", style="bold red")
    table.add_column("Result", justify="center", style="bold green")

    for category, results in SEARCH_RESULTS.items():
        # Randomize the number of results to display from each category
        selected_results = random.sample(results, random.randint(1, len(results)))
        for result in selected_results:
            table.add_row(category, result)
    
    console.print(table)

def main():
    # Display intro with skull ASCII art
    display_skull_intro()

    # Prompt user for search query
    query = console.input("[bold green]Enter your search query:[/bold green] ")
    search_dark_realm(query)

    # Ending note
    console.print("\n[bold red]The veil closes. Dare to return soon.[/bold red]")
    time.sleep(1)

if __name__ == "__main__":
    main()
