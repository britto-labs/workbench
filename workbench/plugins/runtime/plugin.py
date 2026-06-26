import subprocess

from rich import print

from workbench.core.plugin import Plugin
from workbench.plugins.docker.plugin import DockerPlugin
from workbench.plugins.ollama.plugin import OllamaPlugin


class RuntimePlugin(Plugin):

    @property
    def name(self):
        return "runtime"

    def install(self):
        pass

    def configure(self):
        pass

    def start(self):

        print("\n[bold cyan]Starting Workbench...[/bold cyan]\n")

        DockerPlugin().start()
        OllamaPlugin().start()

        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                "compose/core.yml",
                "up",
                "-d",
            ]
        )

        print("\n[green]Workbench is ready.[/green]")

    def stop(self):

        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                "compose/core.yml",
                "down",
            ]
        )

        print("[yellow]Workbench stopped.[/yellow]")

    def restart(self):
        self.stop()
        self.start()

    def status(self):

        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                "compose/core.yml",
                "ps",
            ]
        )

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass