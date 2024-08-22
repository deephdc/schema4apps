# AI4 Metadata utilities

[![DOI](https://zenodo.org/badge/721337407.svg)](https://zenodo.org/doi/10.5281/zenodo.13343453)

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

    $ ai4-metadata validate --metadata-version 2.0.0 instances/sample-v2.mods.json
    $ ai4-metadata validate --schema schemata/ai4-apps-v2.0.0.json instances/sample-v2.mods.json

### Metadata migration

The metadata utilities provide a command-line interface (CLI) tool
`ai4-metadata-migrate` that can be used to migrate the metadata files from V1
to latest V2.

    $ ai4-metadata migrate instances/sample-v1.mods.json

To save the output, use the `--output` option.

    $ ai4-metadata migrate --output sample-v2.mods.json instances/sample-v1.mods.json

Please review the changes, as the metadata migration is not complete, and
manual steps are needed.

## Acknowledgements

<img width=300 align="left" src="https://raw.githubusercontent.com/AI4EOSC/.github/ai4eosc/profile/EN-Funded.jpg" alt="Funded by the European Union" />

This project has received funding from the European Union’s Horizon Research and Innovation programme under Grant agreement No. [101058593](https://cordis.europa.eu/project/id/101058593)
