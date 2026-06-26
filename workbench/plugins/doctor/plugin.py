import subprocess

from rich import print

from workbench.core.plugin import Plugin


class DoctorPlugin(Plugin):

    @property
    def name(self) -> str:
        return "doctor"

    def install(self):
        pass

    def configure(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def status(self):
        pass

    def update(self):
        pass

    def uninstall(self):
        pass

    def health_check(self):

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