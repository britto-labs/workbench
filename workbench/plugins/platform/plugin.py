from rich import print

from workbench.core.plugin import Plugin
from workbench.plugins.docker.plugin import DockerPlugin
from workbench.plugins.ollama.plugin import OllamaPlugin
from workbench.plugins.postgres.plugin import PostgresPlugin


class PlatformPlugin(Plugin):

    @property
    def name(self):
        return "platform"

    def install(self):
        pass

    def configure(self):
        pass

    def start(self):
        DockerPlugin().start()
        OllamaPlugin().start()
        PostgresPlugin().start()

    def stop(self):
        PostgresPlugin().stop()
        OllamaPlugin().stop()
        DockerPlugin().stop()

    def restart(self):
        self.stop()
        self.start()

    def status(self):

        print("\n[bold cyan]Workbench Platform[/bold cyan]\n")

        DockerPlugin().status()
        OllamaPlugin().status()
        PostgresPlugin().status()

    def health_check(self):
        self.status()

    def update(self):
        pass

    def uninstall(self):
        pass