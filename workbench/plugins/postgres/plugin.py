import subprocess

from rich import print

from workbench.core.logger import logger
from workbench.core.plugin import Plugin


CONTAINER_NAME = "workbench-postgres"


class PostgresPlugin(Plugin):

    @property
    def name(self):
        return "postgres"

    def install(self):
        pass

    def configure(self):
        pass

    def start(self):
        logger.info("Starting PostgreSQL")

        subprocess.run(["docker", "start", CONTAINER_NAME])

    def stop(self):
        logger.info("Stopping PostgreSQL")

        subprocess.run(["docker", "stop", CONTAINER_NAME])

    def restart(self):
        self.stop()
        self.start()

    def status(self):

        logger.info("Checking PostgreSQL")

        try:
            status = subprocess.check_output(
                [
                    "docker",
                    "inspect",
                    "-f",
                    "{{.State.Status}}",
                    CONTAINER_NAME,
                ],
                text=True,
            ).strip()

            print(f"[green]✓ PostgreSQL: {status}[/green]")

        except Exception:

            print("[red]✗ PostgreSQL not found[/red]")

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass