import subprocess
import time

from rich import print

from workbench.core.logger import logger
from workbench.core.plugin import Plugin


class DockerPlugin(Plugin):

    @property
    def name(self) -> str:
        return "docker"

    def install(self):
        pass

    def configure(self):
        pass

    def start(self):
        logger.info("Starting Docker Desktop")

        subprocess.run(["open", "-a", "Docker"])

        print("[yellow]Starting Docker Desktop...[/yellow]")

    def stop(self):
        logger.info("Stopping Docker Desktop")

        subprocess.run(["pkill", "Docker"])

        print("[green]Docker Desktop stopped[/green]")

    def restart(self):
        self.stop()

        time.sleep(3)

        self.start()

    def status(self):
        logger.info("Checking Docker status")

        try:
            subprocess.check_output(
                ["docker", "info"],
                stderr=subprocess.STDOUT,
                text=True,
            )

            print("[green]✓ Docker daemon is running[/green]")

        except subprocess.CalledProcessError:
            print("[red]✗ Docker daemon is not running[/red]")

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass