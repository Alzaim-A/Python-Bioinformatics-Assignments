"""test_assignment4_utils.py: Tests for test_assignment4_utils.py"""
import pytest
import os
from assignment4.assignment4_utils import (read_file_lines,
                                           parse_lines_to_dict, count_gene_categories, sort_categories_by_code)


def test_read_file_lines():
    """
    Tests the `read_file_lines` function with both skipping and not skipping the header.
    @return: None
    """
    # create a temporary test file
    test_file_path = "test_data.txt"
    with open(test_file_path, 'w') as f:
        f.write("Header\nLine1\nLine2")

    # verify header is skipped appropriately
    assert read_file_lines(test_file_path, skip_header=True) == ["Line1", "Line2"], "Should skip the first line"
    # verify header is included when not skipped
    assert read_file_lines(test_file_path, skip_header=False) == ["Header", "Line1", "Line2"], \
        "Should include the first line"

    # clean up by removing the test file
    os.remove(test_file_path)


def test_parse_lines_to_dict():
    """
    Tests the `parse_lines_to_dict` function in gene mode, description mode, and with to_lower option.
    @return: None
    """
    lines = ["Gene1\tDescription1", "Gene2\tDescription2"]

    # test parsing in gene mode
    result = parse_lines_to_dict(lines, mode='g', to_lower=False)
    expected = {"Gene1": "Description1", "Gene2": "Description2"}
    assert result == expected, "Gene mode failed to parse correctly"

    # test parsing in description mode
    result = parse_lines_to_dict(lines, mode='d', to_lower=False)
    assert result == expected, "Description mode failed to parse correctly"

    # test key conversion to lowercase
    result = parse_lines_to_dict(lines, mode='g', to_lower=True)
    expected_lower = {"gene1": "Description1", "gene2": "Description2"}
    assert result == expected_lower, "to_lower=True failed to convert keys to lowercase"


def test_count_gene_categories():
    """
    Tests counting gene categories from a list of lines using the `count_gene_categories` function.
    @return: None
    """
    lines = ["Gene1\tDesc1\tCat1", "Gene2\tDesc2\tCat2", "Gene3\tDesc3\tCat1"]
    expected_counts = {"Cat1": 2, "Cat2": 1}
    # verify category counts are as expected
    assert count_gene_categories(lines) == expected_counts, "Category counts did not match expected"


def test_sort_categories_by_code():
    """
    Tests sorting categories by their code using the `sort_categories_by_code` function.
    @return: None
    """
    category_counts = {"1.1": 5, "1.2": 3, "2.1": 7, "10.1": 1}
    expected_order = [("1.1", 5), ("1.2", 3), ("2.1", 7), ("10.1", 1)]
    # verify sorting by category code
    assert sort_categories_by_code(category_counts) == expected_order, "Categories were not sorted correctly by code"
