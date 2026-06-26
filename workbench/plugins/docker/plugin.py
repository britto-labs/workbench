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

        print("\n[yellow]Starting Docker Desktop...[/yellow]")
        print("[yellow]Waiting for Docker daemon...[/yellow]\n")

        for _ in range(30):
            try:
                subprocess.check_output(
                    ["docker", "info"],
                    stderr=subprocess.STDOUT,
                    text=True,
                )

                print("[green]✓ Docker daemon is running[/green]")
                print("[green]Docker is ready.[/green]")
                return

            except subprocess.CalledProcessError:
                time.sleep(2)

        print("[red]Timed out waiting for Docker.[/red]")

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
            output = subprocess.check_output(
                ["docker", "version", "--format", "{{.Server.Version}}"],
                stderr=subprocess.STDOUT,
                text=True,
            ).strip()

            print(f"[green]✓ Docker daemon is running[/green]")
            print(f"Docker Server Version: {output}")

        except subprocess.CalledProcessError:
            print("[red]✗ Docker daemon is not running[/red]")

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass