#!/usr/bin/python3

"""Define Student Class."""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation Function."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance
        if attrs is a list of strings, only attrubute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        try:
            for attr in attrs:
                if is not isinstance(attr, str):
                    return self.__dict__
        except Exeception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
