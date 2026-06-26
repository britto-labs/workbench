import typer

from workbench.plugins.doctor.plugin import DoctorPlugin

app = typer.Typer(
    name="workbench",
    help="Workbench - AI Engineering Platform",
)


@app.command()
def doctor():
    """Run workstation health checks."""

    plugin = DoctorPlugin()
    plugin.health_check()