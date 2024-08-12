"""Utility functions for the AI4 Metadata utils."""

import typing

import simplejson as json


def load_json(f: typing.TextIO) -> typing.Dict:
    """Load a JSON from the file f."""
    try:
        data = f.read()
        return json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error loading schema as JSON: {e}")
        raise
