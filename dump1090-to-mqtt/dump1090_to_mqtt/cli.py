import asyncio
import logging

import typer

from dump1090_to_mqtt.main import forward_dump1090

logger = logging.getLogger(__name__)

typer_app = typer.Typer()


@typer_app.command(name="run")
def run_command():
    asyncio.run(forward_dump1090())
