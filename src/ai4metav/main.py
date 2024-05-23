"""Main module for AI4 metadata validator."""

import argparse
import os
import simplejson as json

from jsonschema import validators


SCHEMAV1 = os.path.join(os.path.dirname(__file__), "schemata/ai4-apps-v1.json")
SCHEMAV2 = os.path.join(os.path.dirname(__file__), "schemata/ai4-apps-v2.json")


def load_json(f):
    """Load a JSON from the file f."""
    data = f.read()
    return json.loads(data)


def validate():
    """Validate the schema."""
    parser = argparse.ArgumentParser(
        description=("AI4 application metadata " "(JSON-schema based) " "validator.")
    )
    # Add argument to specify the schema version to use
    parser.add_argument(
        "--schema",
        metavar="SCHEMA_JSON",
        type=argparse.FileType("r"),
        default=SCHEMAV2,
        help=f"AI4 application metadata schema file (default: {SCHEMAV2})",

    )
    parser.add_argument(
        "instance",
        metavar="METADATA_JSON",
        type=argparse.FileType("r"),
        nargs="+",
        help="DEEP application metadata",
    )
    args = parser.parse_args()
    schema = args.schema

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

    for f in args.instance:
        instance = load_json(f)
        validators.validate(instance, schema)
