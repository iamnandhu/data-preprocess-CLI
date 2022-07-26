import pandas as pd
import numpy as np
from typer import Optional
import typer

from CLI import __app_name__,__version__

app = type.Typer()
def _version_callback(value: bool) -> None:
    if value:
        type.echo(f"{__app_name__} v{__version__}")
        raise type.Exit()

@app.callback()
def main(
    version : Optional[bool]=type.Option(
        None,
        "--version",
        "-v",
        help = "Show the appliction's version and exit :)",
        callback = _version_callback,
        is_eager = True,
    )
) -> None:
    return