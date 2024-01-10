#!/usr/bin/python3

"""Define load_from_json_file function."""


import json


def load_from_json_file(filename):
    """Create an Object from a json file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
