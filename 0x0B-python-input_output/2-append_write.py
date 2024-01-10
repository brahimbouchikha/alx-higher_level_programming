#!/usr/bin/python3
"""Define function append_write """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8).

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
