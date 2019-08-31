import dataclasses
import os
import pytest
import tempfile


@dataclasses.dataclass
class ExampleContext:
    a_value: str
    another_value: str


@pytest.fixture
def example_context():
    context = ExampleContext("the value", "the other value")
    return context


@pytest.fixture
def data_dir():
    return os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def an_example_dir(data_dir):
    return os.path.join(data_dir, "an_example")


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir
