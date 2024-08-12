"""Migrate metadata from V1 to V2."""

import argparse
import collections
import datetime
import sys

import simplejson as json

import ai4_metadata
from ai4_metadata import utils
from ai4_metadata import validate


def migrate(v1_metadata: dict) -> collections.OrderedDict:
    """Try to migrate metadata from V1 to latest V2."""
    v2 = collections.OrderedDict()

    v2["metadata_version"] = ai4_metadata.get_latest_version()
    v2["title"] = v1_metadata.get("title")
    v2["summary"] = v1_metadata.get("summary")
    v2["description"] = " ".join(v1_metadata.get("description", []))
    v2["dates"] = {
        "created": v1_metadata.get("date_creation"),
        "updated": datetime.datetime.now().strftime("%Y-%m-%d"),
    }
    v2["links"] = {
        "source_code": v1_metadata.get("sources", {}).get("code"),
        "docker_image": v1_metadata.get("sources", {}).get("docker_registry_repo"),
    }
    v2["tags"] = v1_metadata.get("keywords", [])
    v2["tasks"] = []
    v2["categories"] = []
    v2["libraries"] = []

    # Now move things, if present, into links
    if v1_metadata.get("doi"):
        v2["links"]["doi"] = v1_metadata.get("doi")
    if v1_metadata.get("sources", {}).get("zenodo_doi"):
        v2["links"]["zenodo_doi"] = v1_metadata.get("sources", {}).get("zenodo_doi")
    if v1_metadata.get("sources", {}).get("pre_trained_weights"):
        v2["links"]["weights"] = v1_metadata.get("sources", {}).get(
            "pre_trained_weights"
        )
    if v1_metadata.get("sources", {}).get("ai4_template"):
        v2["links"]["ai4_template"] = v1_metadata.get("sources", {}).get("ai4_template")

    if v1_metadata.get("dataset_url"):
        v2["links"]["dataset_url"] = v1_metadata.get("dataset_url")
    if v1_metadata.get("training_files_url"):
        v2["links"]["training_files_url"] = v1_metadata.get("training_files_url")
    if v1_metadata.get("cite_url"):
        v2["links"]["cite_url"] = v1_metadata.get("cite_url")

    # Try to infer some some more information on libraries and categories
    kw = [k.lower() for k in v1_metadata.get("keywords", [])]
    if "tensorflow" in kw:
        v2["libraries"].append("TensorFlow")
    if "pytorch" in kw:
        v2["libraries"].append("PyTorch")
    if "keras" in kw:
        v2["libraries"].append("Keras")
    if "scikit-learn" in kw:
        v2["libraries"].append("Scikit-Learn")

    if "trainable" in kw:
        v2["categories"].append("AI4 trainable")
    if "inference" in kw:
        v2["categories"].append("AI4 inference")
        v2["categories"].append("AI4 pre trained")

    return v2


def main() -> None:
    """Convert metadata from V1 to latest V2."""
    parser = argparse.ArgumentParser(
        description=(
            "Migrate AI4 metadata from V1 to latest V2 (currently "
            f"{ai4_metadata.get_latest_version()})."
        )
    )

    parser.add_argument(
        "--output",
        "-o",
        metavar="OUTPUT_JSON",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="Output file for migrated metadata, default is stdout.",
    )

    parser.add_argument(
        "instance",
        metavar="METADATA_JSON",
        type=argparse.FileType("r"),
        help="AI4 application metadata file to migrate.",
    )

    args = parser.parse_args()

    v1_metadata = utils.load_json(args.instance)
    v1_schema = open(ai4_metadata.get_schema("1.0.0"), "r")
    validate.validate(v1_metadata, v1_schema)
    print("V1 metadata is valid, continuing with migration...")

    # Migrate metadata
    v2_metadata = migrate(v1_metadata)
    v2_schema = open(ai4_metadata.get_schema(ai4_metadata.get_latest_version()), "r")
    validate.validate(v2_metadata, v2_schema)

    # Write out the migrated metadata
    json.dump(v2_metadata, args.output, indent=4)
