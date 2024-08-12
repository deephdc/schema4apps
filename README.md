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

### Metadata migration

The metadata utilities provide a command-line interface (CLI) tool
`ai4-metadata-migrate` that can be used to migrate the metadata files from V1
to latest V2.

    $ ai4-metadata-migrate instances/sample-v1.mods.json

To save the output, use the `--output` option.

    $ ai4-metadata-migrate --output sample-v2.mods.json instances/sample-v1.mods.json

Please review the changes, as the metadata migration is not complete, and
manual steps are needed.
