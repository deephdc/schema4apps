"""Utility functions for the AI4 Metadata utils."""

import json
import pathlib
import typing

import typer


def load_json(path: typing.Union[str, pathlib.Path]) -> typing.Dict:
    """Load a JSON from the file f."""
    file = open(path, "r")
    try:
        data = file.read()
        return json.loads(data)
    except json.JSONDecodeError as e:
        typer.secho(f"Error loading schema as JSON: {e}", fg=typer.colors.RED, err=True)
        raise e


def dump_json(data: typing.Dict, path: typing.Optional[pathlib.Path] = None) -> None:
    """Dump a JSON object to stdout or to path if provided."""
    if path is None:
        typer.echo(json.dumps(data, indent=4))
    else:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
