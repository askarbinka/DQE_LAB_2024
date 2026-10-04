import os

import pytest
import yaml


def add_numbers(a, b, c):
    return a + b + c


def get_test_cases():
    project_dir = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    config_path = os.path.join(
        project_dir,
        "Configs",
        "config_unit.yaml"
    )

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config["cases"]


@pytest.mark.unit
@pytest.mark.smoke
@pytest.mark.parametrize(
    "case",
    get_test_cases(),
    ids=lambda case: case["case_name"]
)
def test_add_numbers(case):
    a, b, c = case["input"]

    result = add_numbers(a, b, c)

    assert result == case["expected"]


@pytest.mark.unit
@pytest.mark.critical
def test_add_invalid_types():
    with pytest.raises(TypeError):
        add_numbers("a", 2, 1)