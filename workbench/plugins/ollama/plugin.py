import subprocess

from rich import print

from workbench.core.logger import logger
from workbench.core.plugin import Plugin


class OllamaPlugin(Plugin):

    @property
    def name(self):
        return "ollama"

    def install(self):
        pass

    def configure(self):
        pass

    def start(self):
        logger.info("Starting Ollama service")

        subprocess.run(["brew", "services", "start", "ollama"])

        print("[green]✓ Ollama service started[/green]")

    def stop(self):
        logger.info("Stopping Ollama service")

        subprocess.run(["brew", "services", "stop", "ollama"])

        print("[yellow]Ollama service stopped[/yellow]")

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        logger.info("Checking Ollama status")

        try:
            output = subprocess.check_output(
                ["ollama", "list"],
                stderr=subprocess.STDOUT,
                text=True,
            )

            print("[green]✓ Ollama server is running[/green]")
            print(output)

        except subprocess.CalledProcessError:
            print("[red]✗ Ollama server is not running[/red]")

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass