import typer

from workbench.plugins.doctor.plugin import DoctorPlugin
from workbench.plugins.runtime.plugin import RuntimePlugin

app = typer.Typer(
    name="workbench",
    help="Workbench - AI Engineering Platform",
)


@app.command()
def doctor():
    DoctorPlugin().health_check()


@app.command()
def up():
    RuntimePlugin().start()


@app.command()
def down():
    RuntimePlugin().stop()


@app.command()
def status():
    RuntimePlugin().status()