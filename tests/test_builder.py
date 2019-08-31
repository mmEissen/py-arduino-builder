import pytest
import os

from py_arduino_builder import builder


def assert_file_content(filename, expected_content):
    with open(filename) as file_:
        content = file_.read()
    assert content == expected_content


def test_build_template(an_example_dir, example_context, temp_dir):
    template_file = os.path.join(an_example_dir, "some_top_template.template")
    output_file = os.path.join(temp_dir, "out_file")

    builder.build_template(template_file, example_context, output_file)

    assert_file_content(output_file, "Hello, world!\nthe other value\nBye, world!\n")


def test_build_templates(an_example_dir, example_context, temp_dir):
    builder.build_templates(an_example_dir, example_context, temp_dir)

    assert_file_content(
        os.path.join(temp_dir, "some_top_template"),
        "Hello, world!\nthe other value\nBye, world!\n",
    )
    assert_file_content(
        os.path.join(temp_dir, "some_top_file"),
        "Hello, world!\n",
    )
    assert_file_content(
        os.path.join(temp_dir, "a_sub_dir", "some_file"),
        "Hello, world!\n",
    )
    assert_file_content(
        os.path.join(temp_dir, "a_sub_dir", "some_template"),
        "Hello, world!\nthe value\nBye, world!\n",
    )
