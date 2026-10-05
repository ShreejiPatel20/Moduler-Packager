"""
Custom File Operations Module
"""

from pathlib import Path


def validate_filename(filename):
    path = Path(filename)

    if not filename:
        raise ValueError(
            "Filename cannot be empty."
        )

    if path.name != filename:
        raise ValueError(
            "Only simple filenames are allowed."
        )

    if path.suffix.lower() != ".txt":
        raise ValueError(
            "File must have .txt extension."
        )

    return path


def create_file(filename):
    path = validate_filename(filename)

    with open(
        path,
        "x",
        encoding="utf-8"
    ):
        pass

    return True


def write_file(filename, data):
    path = validate_filename(filename)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(data)

    return True


def read_file(filename):
    path = validate_filename(filename)

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        content = file.read()

    return content


def append_file(filename, data):
    path = validate_filename(filename)

    with open(
        path,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(data)

    return True
