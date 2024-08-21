"""Main module for AI4 metadata validator."""

import pathlib
from jsonschema import validators
import typing

from ai4_metadata import utils


def validate(
    instance: typing.Union[dict, pathlib.Path], schema: typing.Union[dict, pathlib.Path]
) -> None:
    """Validate the schema."""
    if isinstance(instance, pathlib.Path):
        instance_file = instance
        instance = utils.load_json(instance_file)

    if isinstance(schema, pathlib.Path):
        schema_file = schema
        schema = utils.load_json(schema_file)

    try:
        validator = validators.validator_for(schema)
        validator.check_schema(schema)
    except Exception as e:
        print(f"Error validating schema: {e}")
        raise

    validators.validate(instance, schema)
