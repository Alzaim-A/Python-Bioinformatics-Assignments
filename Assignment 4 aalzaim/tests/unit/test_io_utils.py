"""test_io_utils.py Tests for io_utils.py"""
import pytest
import os
from assignment4.io_utils import mkdir_from_infile


def test_mkdir_from_infile(tmp_path):
    """
    Tests the `mkdir_from_infile` function to ensure it creates a directory from an infile string that does not exist.
    @param tmp_path: Pytest fixture that provides a temporary directory specific to the test being run.
    @return: None
    """
    # Use tmp_path fixture provided by pytest to create a temporary directory for the test
    test_file = tmp_path / "test_dir/test_file.txt"
    # Convert to string, as the function expects a string path
    test_file_str = str(test_file)

    # Call the function with the path of a file in a non-existent directory
    mkdir_from_infile(test_file_str)

    # Check if the directory was created
    assert os.path.exists(test_file.parent), "The directory should exist."


def test_mkdir_from_infile_existing_dir(tmp_path):
    """
    Tests the `mkdir_from_infile` function with a path where the directory already exists, verifying no errors occur.
    @param tmp_path: Pytest fixture that provides a temporary directory specific to the test being run.
    @return: None
    """
    # Setup: Create a directory and a file inside it using the tmp_path fixture
    existing_dir = tmp_path / "existing_dir"
    existing_dir.mkdir()  # Create the directory
    test_file = existing_dir / "test_file.txt"
    test_file.touch()  # Create an empty file in the existing directory

    # Convert to string, as the function expects a string path
    test_file_str = str(test_file)

    # Call the function with the path of a file in an existing directory
    mkdir_from_infile(test_file_str)

    # Check: The directory already exists, so the function should not attempt to create it or fail
    assert os.path.exists(existing_dir), "The directory should still exist."
    assert os.path.isdir(existing_dir), "The existing directory should be unchanged."
    assert test_file.exists(), "The test file inside the existing directory should remain unaffected."


def test_mkdir_from_infile_empty_path():
    """
    Tests the `mkdir_from_infile` function with an empty path, expecting a FileNotFoundError to be raised.
    @return: None
    """
    with pytest.raises(FileNotFoundError):
        mkdir_from_infile("")


def test_mkdir_from_infile_path_with_no_directory_raises_error():
    """
    Tests the `mkdir_from_infile` function with a path that has no directory component, expecting a FileNotFoundError.
    @return: None
    """
    with pytest.raises(FileNotFoundError):
        mkdir_from_infile("test_file_only.txt")
