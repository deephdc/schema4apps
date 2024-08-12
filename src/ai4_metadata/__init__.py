"""AI4 Metadata validator."""

import os

VERSIONS = {
    "1.0.0": os.path.join(os.path.dirname(__file__), "schemata/ai4-apps-v1.0.0.json"),
    "2.0.0": os.path.join(os.path.dirname(__file__), "schemata/ai4-apps-v2.0.0.json"),
}

LATEST_VERSION = "2.0.0"


def get_latest_schema() -> str:
    """Return the path to the latest schema."""
    return VERSIONS[LATEST_VERSION]


def get_schema(version: str) -> str:
    """Return the path to the schema for the given version."""
    return VERSIONS[version]


def get_latest_version() -> str:
    """Return the latest version."""
    return LATEST_VERSION


def get_all_versions() -> list[str]:
    """Return all available versions."""
    return VERSIONS.keys()
