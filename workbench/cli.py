import typer

from workbench.plugins.doctor.plugin import DoctorPlugin
from workbench.plugins.docker.plugin import DockerPlugin

app = typer.Typer(
    name="workbench",
    help="Workbench - AI Engineering Platform",
)


@app.command()
def doctor():
    """Run workstation health checks."""
    DoctorPlugin().health_check()


@app.command("docker-status")
def docker_status():
    """Check Docker status."""
    DockerPlugin().status()