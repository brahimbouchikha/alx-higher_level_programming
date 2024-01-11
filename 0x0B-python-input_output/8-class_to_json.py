#!/usr/bin/python3

"""Define class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description
    with simple data strcuture.
    """
    return {'name': obj.name, 'number': obj.number}
