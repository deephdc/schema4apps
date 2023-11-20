import argparse
import os
import simplejson as json

from jsonschema import Draft7Validator
from jsonschema import draft7_format_checker


SCHEMA = os.path.join(os.path.dirname(__file__), 'schemata/ai4-apps.json')

def load_json(f):
    data = f.read()
    return json.loads(data)


def validate():
    parser = argparse.ArgumentParser(description=('DEEP application metadata '
                                                  '(JSON-schema based) '
                                                  'validator.'))
    parser.add_argument('instance',
                        metavar='METADATA_JSON',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='DEEP application metadata')
    args = parser.parse_args()

    with open(SCHEMA, 'r') as f:
        schema = load_json(f)
    Draft7Validator.check_schema(schema)

    for f in args.instance:
        instance = load_json(f)
        Draft7Validator(
            schema,
            format_checker=draft7_format_checker).validate(instance)
