import argparse
from jsonschema import Draft7Validator
import simplejson as json


SCHEMA = './schemata/deep-apps.json'

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
        Draft7Validator(schema).validate(instance)
