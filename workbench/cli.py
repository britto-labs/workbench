import subprocess

import typer
from rich import print

app = typer.Typer(
    name="workbench",
    help="Workbench - AI Engineering Platform",
)


@app.command()
def doctor():
    """Check workstation health."""

    print("\n[bold cyan]Workbench Doctor[/bold cyan]\n")

    checks = [
        ("Git", ["git", "--version"]),
        ("Docker", ["docker", "--version"]),
        ("Node", ["node", "-v"]),
        ("Python", ["python3", "--version"]),
        ("Ollama", ["ollama", "--version"]),
    ]

    for name, cmd in checks:
        try:
            output = subprocess.check_output(
                cmd,
                stderr=subprocess.STDOUT,
                text=True,
            ).strip()

            print(f"[green]✓[/green] {name}: {output}")

        except Exception:
            print(f"[red]✗[/red] {name}: Not Found")


if __name__ == "__main__":
    app()