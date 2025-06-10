"""Test script for secondary_structure_splitter.py"""
import pytest
from secondary_structure_splitter import _verify_lists, get_fasta_lists

def test_verify_lists_equal_size():
    """Test that _verify_lists doesn't raise SystemExit for lists of equal size"""
    headers = ['>seq1', '>seq2']
    sequences = ['ATCG', 'GGCC']
    try:
        _verify_lists(headers, sequences)
    except SystemExit:
        pytest.fail("Unexpected SystemExit for lists of equal size")

def test_verify_lists_different_size():
    """Test that _verify_lists raises SystemExit for lists of different sizes"""
    headers = [">seq1"]
    sequences = ["ATCG", "GCTA"]
    with pytest.raises(SystemExit):
        _verify_lists(headers, sequences)


def test_get_fasta_lists_real_file():
    """Test that get_fasta_lists function can read FASTA
    file and parse the headers and sequences correctly.
    The (small) test FASTA has been included in the Assignment3 zip"""
    fasta_file_path = "./FASTA_for_test_scripts.fasta"
    expected_headers = [">seq1", ">seq2"]
    expected_sequences = ["ATCGATCG", "GCGTGCGT"]
    headers, sequences = get_fasta_lists(fasta_file_path)
    assert headers == expected_headers, ("The headers parsed from "
        "FASTA_for_test_scripts.fasta do not match the expected headers.")
    assert sequences == expected_sequences, ("The sequences parsed from "
        "FASTA_test.fasta do not match the expected sequences.")
