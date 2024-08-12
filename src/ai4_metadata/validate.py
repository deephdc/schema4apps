"""Main module for AI4 metadata validator."""

import argparse
import sys
import typing

from jsonschema import validators

import ai4_metadata
from ai4_metadata import utils


def validate(instance: object, schema_file: typing.TextIO) -> None:
    """Validate the schema."""
    schema = utils.load_json(schema_file)

    try:
        validator = validators.validator_for(schema)
        validator.check_schema(schema)
    except Exception as e:
        print(f"Error validating schema: {e}")
        raise

    validators.validate(instance, schema)


def main() -> None:
    """Validate the AI4 metadata schema via CLI."""
    parser = argparse.ArgumentParser(
        description=("AI4 application metadata (JSON-schema based) validator.")
    )

    version_group = parser.add_mutually_exclusive_group()

    version_group.add_argument(
        "--schema",
        metavar="SCHEMA_JSON",
        type=argparse.FileType("r"),
        help="AI4 application metadata schema file to use. "
        "If set, overrides --metadata-version.",
    )

    version_group.add_argument(
        "--metadata-version",
        metavar="VERSION",
        choices=ai4_metadata.get_all_versions(),
        default=ai4_metadata.get_latest_version(),
        help="AI4 application metadata version "
        f"(default: {ai4_metadata.get_latest_version()})",
    )

    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress output for valid instances",
    )

    parser.add_argument(
        "instance",
        metavar="METADATA_JSON",
        type=argparse.FileType("r"),
        nargs="+",
        help="AI4 application metadata file to validate.",
    )
    args = parser.parse_args()

    schema = args.schema or open(ai4_metadata.get_schema(args.metadata_version), "r")

    exit_code = 0
    for f in args.instance:
        try:
            instance = utils.load_json(f)
            validate(instance, schema)
        except Exception as e:
            print(f"Error validating instance: {e}")
            exit_code = 1
        else:
            if not args.quiet:
                print(f"{f.name} is valid for version {args.metadata_version}")

    sys.exit(exit_code)
