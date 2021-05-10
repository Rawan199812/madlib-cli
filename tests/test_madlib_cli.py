import pytest
from madlib_cli.madlib import read_template, parse_template, get_user_inputs, merge, write_template
from madlib_cli import __version__


def test_version():
    assert __version__ == '0.1.0'

# def test_read_template():
#     expected = open("assets/madlib_template.txt", "r").read()
#     received = read_template()
#     assert expected == received
def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# def test_merge():
#     actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
#     expected = "It was a dark and stormy night."
#     assert actual == expected


def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_merge(monkeypatch):
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)

def test_write_template_output():
  actual = write_template("It was a {Adjective} and {Adjective} {Noun}.")
  expected = 'assets/madlib_template_output.txt'
  assert actual == expected 