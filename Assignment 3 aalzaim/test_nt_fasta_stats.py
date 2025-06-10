"""Test scripts for nt_fasta_stats.py"""
from nt_fasta_stats import _get_num_nucleotides, get_fasta_lists

def test_get_num_nucleotides():
    """Test counting nucleotides in a sequence"""
    sequence = "AAGGCT"
    assert _get_num_nucleotides('A', sequence) == 2
    assert _get_num_nucleotides('G', sequence) == 2
    assert _get_num_nucleotides('C', sequence) == 1
    assert _get_num_nucleotides('T', sequence) == 1

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
