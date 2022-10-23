import os

import pytest

from lms_homework.No21.lesson_21 import File


def test_positive_create_file():
    with File("test_positive1.txt", "w") as file:
        file.write("testing 1....")
    assert os.path.isfile("test_positive1.txt") is True


def test_positive_write_file():
    with File("test_positive2.txt", "w") as file:
        file.write("testing done")

    with open("test_positive2.txt", "r") as temp_test_file:
        readline = temp_test_file.readline()
        assert "testing done" == readline


def test_negative_read_file():
    try:
        with File("test_positive3.txt", "r") as file:
            file.write("testing done")
    except TypeError as error:
        assert error
