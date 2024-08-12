# AI4 Metadata utilities

Metadata utilities for the AI4OS hub data science applications.

The AI4OS hub data science applications use metadata to describe the data
sources, models, and other resources. The metadata is used to validate the
resources and to provide information to the users.

## Installation

The metadata utilities can be installed using pip:

    $ pip install ai4-metadata

## Usage

### Metadata validation

The metadata utilities provide a command-line interface (CLI) tool
`ai4-metadata-validate` that can be used to validate the metadata files. The
CLI tool accepts the metadata files as input parameters.

    $ ai4-metadata-validate instances/sample-v2.mods.json

Different metadata versions can be specified, either by using the
`--metadata-version` or by providing the metadata schema file.

    $ ai4-metadata-validate --metadata-version 2.0.0 instances/sample-v2.mods.json
    $ ai4-metadata-validate --schema schemata/ai4-apps-v2.0.0.json instances/sample-v2.mods.json
