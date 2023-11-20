# AI4 Metadata validator

Metadata validator for the AI4OS hub data science applications.

## Motivation

`ai4-metadata-validator` validates the metadata used by the AI4OS hub models
and applications.

## Implementation

The [schema](schemata/ai4-apps.json) has been implemented according to [JSON
schema specification](https://json-schema.org/) (Draft 7), using [Python's
jsonschema](https://pypi.org/project/jsonschema/) module.

Once installed, the `ai4-metadata-validator` CLI tool is provided, which
accepts schema instance files as input parameters.

## Installation
```
$ pip install ai4-metadata-validator
```

## Usage
```
$ ai4-metadata-validator instances/sample.mods.json
```
