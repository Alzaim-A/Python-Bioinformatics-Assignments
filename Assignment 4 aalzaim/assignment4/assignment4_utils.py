"""assignment4_utils.py: Utility"""
import os
import re
from collections import defaultdict


def read_file_lines(file_path: str, skip_header: bool = False) -> list[str]:
    """
    Reads a file and returns its lines as a list.
    @param file_path: The path to the file.
    @param skip_header: Whether to skip the first line of the file (the header), optional, defaults to False.
    @return: A list of lines from the file.
    """
    # open file and optionally skip header
    with open(file_path, 'r') as file:
        if skip_header:
            next(file, None)  # skip header if requested
        return [line.strip() for line in file]  # return stripped lines


def parse_lines_to_dict(lines: list[str], to_lower: bool = False) -> dict[str, str]:
    """
    Parses lines from a file and maps keys to their values. Originally intended for different modes, but
    currently implemented identically for 'description' ('d') and 'gene' ('g') modes.
    @param lines: Lines from the file.
    @param to_lower: Convert the key part to lowercase, optional, defaults to False.
    @return: A dictionary mapping keys to their values.
    """
    result_dict = {}
    for line in lines:
        parts = line.split('\t')
        key = parts[0]
        value = parts[1] if len(parts) > 1 else ""  # Use empty string if the second part is not available

        if to_lower:
            key = key.lower()

        result_dict[key] = value

    return result_dict


def count_gene_categories(lines: list[str]) -> dict[str, int]:
    """
    Counts occurrences of each category from lines of a gene file.
    @param lines: Lines from the gene file.
    @return: A dictionary mapping categories to their occurrence counts.
    """
    # count category occurrences
    category_counts = defaultdict(int)
    for line in lines:
        parts = line.split('\t')
        if len(parts) >= 3:
            category_counts[parts[2]] += 1
    return dict(category_counts)


def sort_categories_by_code(category_counts: dict[str, int]) -> list[tuple[str, int]]:
    """
    Sorts categories based on their codes, which are assumed to be strings
    that can be split by '.' and converted to integers for sorting purposes.
    @param category_counts: A dictionary mapping categories to their occurrence counts.
    @return: A sorted list of tuples, each containing a category and its count, sorted by the category code.
    """
    # sort categories by code
    return sorted(category_counts.items(), key=lambda x: tuple(map(int, x[0].split('.'))))
