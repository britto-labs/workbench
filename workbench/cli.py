import typer

from workbench.plugins.doctor.plugin import DoctorPlugin
from workbench.plugins.docker.plugin import DockerPlugin
from workbench.plugins.ollama.plugin import OllamaPlugin
from workbench.plugins.platform.plugin import PlatformPlugin
from workbench.plugins.postgres.plugin import PostgresPlugin

app = typer.Typer(
    name="workbench",
    help="Workbench - AI Engineering Platform",
)


@app.command()
def doctor():
    DoctorPlugin().health_check()


@app.command("platform-status")
def platform_status():
    PlatformPlugin().status()


@app.command("platform-start")
def platform_start():
    PlatformPlugin().start()


@app.command("platform-stop")
def platform_stop():
    PlatformPlugin().stop()


@app.command("docker-status")
def docker_status():
    DockerPlugin().status()


@app.command("docker-start")
def docker_start():
    DockerPlugin().start()


@app.command("docker-stop")
def docker_stop():
    DockerPlugin().stop()


@app.command("docker-restart")
def docker_restart():
    DockerPlugin().restart()


@app.command("ollama-status")
def ollama_status():
    OllamaPlugin().status()


@app.command("ollama-start")
def ollama_start():
    OllamaPlugin().start()


@app.command("ollama-stop")
def ollama_stop():
    OllamaPlugin().stop()


@app.command("postgres-status")
def postgres_status():
    PostgresPlugin().status()


@app.command("postgres-start")
def postgres_start():
    PostgresPlugin().start()


@app.command("postgres-stop")
def postgres_stop():
    PostgresPlugin().stop()