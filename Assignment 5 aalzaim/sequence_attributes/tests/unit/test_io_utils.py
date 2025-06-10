"""Test suite for io_utils.py"""
import pytest
import os
from sequence_attributes.utils.io_utils import FileHandler


TEST_FILE_NAME = "test_file_handler.txt"
TEST_STRING = "Hello, World!"


# helper function to create a test file
def _create_test_file():
    with open(TEST_FILE_NAME, "w", encoding='utf-8') as f:
        f.write(TEST_STRING)


# test for successfully reading from a file
def test_file_handler_reading():
    _create_test_file()
    with FileHandler(TEST_FILE_NAME, mode="r") as file:
        content = file.read()
    assert content == TEST_STRING, "File content does not match expected string."
    os.remove(TEST_FILE_NAME)


# test for successfully writing to a file
def test_file_handler_writing():
    test_content = "Writing test"
    with FileHandler(TEST_FILE_NAME, mode="w") as file:
        file.write(test_content)
    with open(TEST_FILE_NAME, "r", encoding='utf-8') as file:
        content = file.read()
    assert content == test_content, "File content does not match written string."
    os.remove(TEST_FILE_NAME)


# tests FileHandler's behavior with a non-existent file
def test_file_handler_os_error():
    with pytest.raises(OSError):
        with FileHandler("non_existent_file.txt", mode="r"):
            pass


# Test for raising ValueError when an invalid mode is provided
def test_file_handler_value_error():
    with pytest.raises(ValueError):
        with FileHandler(TEST_FILE_NAME, mode="invalid_mode"):
            pass

