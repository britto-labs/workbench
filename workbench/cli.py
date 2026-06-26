import typer

from workbench.plugins.doctor.plugin import DoctorPlugin
from workbench.plugins.docker.plugin import DockerPlugin

app = typer.Typer(
    name="workbench",
    help="Workbench - AI Engineering Platform",
)


@app.command()
def doctor():
    DoctorPlugin().health_check()


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