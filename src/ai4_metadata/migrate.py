"""Migrate metadata from V1 to V2."""

import collections
import datetime
import pathlib
import typing

import ai4_metadata
from ai4_metadata import utils


def migrate(instance_file: pathlib.Path) -> collections.OrderedDict:
    """Try to migrate metadata from V1 to latest V2."""
    v1_metadata = utils.load_json(instance_file)

    v2: collections.OrderedDict[str, typing.Any] = collections.OrderedDict()

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
