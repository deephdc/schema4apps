"""Unit tests for the validator module."""

import pathlib
import pytest

from ai4_metadata import validate


@pytest.fixture
def valid_schema_file():
    return open(pathlib.Path(__file__).parent / "../schemata/ai4-apps-v2.0.0.json", "r")


@pytest.fixture
def invalid_schema_file():
    return None


@pytest.fixture
def valid_instance():
    i = open(
        pathlib.Path(__file__).parent / "../../../instances/sample-v2.mods.json", "r"
    )
    return validate.load_json(i)


@pytest.fixture
def invalid_instance():
    return {"foo": "bar"}


def test_validator(valid_schema_file, valid_instance):
    assert validate.validate(valid_instance, valid_schema_file) is None


def test_validator_invalid_instance(valid_schema_file, invalid_instance):
    with pytest.raises(Exception):
        validate.validate(invalid_instance, valid_schema_file)


def test_validator_invalid_schema(invalid_schema_file, valid_instance):
    with pytest.raises(Exception):
        validate.validate(valid_instance, invalid_schema_file)


def test_validator_invallid_all(invalid_schema_file, invalid_instance):
    with pytest.raises(Exception):
        validate.validate(invalid_instance, invalid_schema_file)
