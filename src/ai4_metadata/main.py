"""Main module for AI4 metadata validator."""

import argparse
import os
import simplejson as json
import sys

from jsonschema import validators


VERSIONS = {
    "1.0.0": os.path.join(os.path.dirname(__file__), "schemata/ai4-apps-v1.0.0.json"),
    "2.0.0": os.path.join(os.path.dirname(__file__), "schemata/ai4-apps-v2.0.0.json"),
}

LATEST_VERSION = "2.0.0"


def load_json(f):
    """Load a JSON from the file f."""
    data = f.read()
    return json.loads(data)


def validate():
    """Validate the schema."""
    parser = argparse.ArgumentParser(
        description=("AI4 application metadata (JSON-schema based) validator.")
    )

    version_group = parser.add_mutually_exclusive_group()

    version_group.add_argument(
        "--schema",
        metavar="SCHEMA_JSON",
        type=argparse.FileType("r"),
        help="AI4 application metadata schema file to use. "
             "If set, overrides --metadata-version."
    )

    version_group.add_argument(
        "--metadata-version",
        metavar="VERSION",
        choices=VERSIONS.keys(),
        default=LATEST_VERSION,
        help=f"AI4 application metadata version (default: {LATEST_VERSION})",
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
        help="DEEP application metadata",
    )
    args = parser.parse_args()

    schema = args.schema or open(VERSIONS[args.metadata_version])

    try:
        schema = load_json(schema)
    except json.JSONDecodeError as e:
        print(f"Error loading schema as JSON: {e}")
        raise

    try:
        validator = validators.validator_for(schema)
        validator.check_schema(schema)
    except Exception as e:
        print(f"Error validating schema: {e}")
        raise

    exit_code = 0
    for f in args.instance:
        try:
            instance = load_json(f)
            validators.validate(instance, schema)
        except Exception as e:
            print(f"Error validating instance: {e}")
            exit_code = 1
        else:
            if not args.quiet:
                print(f"{f.name} is valid for version {args.metadata_version}")

    sys.exit(exit_code)
