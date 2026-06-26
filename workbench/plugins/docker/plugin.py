import subprocess

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
        subprocess.run(["open", "-a", "Docker"])

    def stop(self):
        subprocess.run(["pkill", "Docker"])

    def status(self):
        logger.info("Checking Docker status")

        try:
            output = subprocess.check_output(
                ["docker", "info"],
                stderr=subprocess.STDOUT,
                text=True,
            )

            print("[green]✓ Docker daemon is running[/green]")
            return output

        except subprocess.CalledProcessError as e:
            print("[red]✗ Docker daemon is not running[/red]")
            print(e.output)

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass