"""Test suite for fasta_format.py"""
import pytest
import os
from sequence_attributes.sequence_formats.fasta_format import get_fasta_lists, _verify_lists


# testing the _verify_lists function
def test_verify_lists_success():
    headers = ['header1', 'header2']
    sequences = ['ATGC', 'GGGG']
    # This should pass as lengths are equal
    assert _verify_lists(headers, sequences) is True

# testing the successful verification of headers and sequences lists' lengths
def test_verify_lists_failure():
    headers = ['header1', 'header2']
    sequences = ['ATGC']  # Mismatch in lengths
    # Expecting a ValueError due to length mismatch
    with pytest.raises(ValueError):
        _verify_lists(headers, sequences)


# Testing get_fasta_lists function by bypassing file operations
def test_get_fasta_lists():
    mocked_data = (
        ">CCDS1.1|chr1",
        "ATGC",
        ">CCDS2.1|chr2",
        "GGGG"
    )

    headers, sequences = process_fasta_data(mocked_data)
    expected_sequences = ['ATGC', 'GGGG']
    assert headers == ['>CCDS1.1|chr1', '>CCDS2.1|chr2']
    assert sequences == ['ATGC', 'GGGG']


# processes FASTA data from strings, used for mocking FASTA content
def process_fasta_data(lines):
    headers = []
    sequences = []
    seq = ""
    for line in lines:
        if line.startswith('>'):
            if seq:
                sequences.append(seq)
                seq = ""
            headers.append(line.strip())
        else:
            seq += line.strip()
    if seq:  # Adding the last sequence if exists
        sequences.append(seq)
    return headers, sequences


# tests get_fasta_lists with an empty file, expecting empty lists as output
def test_get_fasta_lists_empty_file(tmp_path):
    empty_file = tmp_path / "empty.fasta"
    empty_file.write_text("")  # Create an empty file

    headers, sequences = get_fasta_lists(str(empty_file))
    assert headers == []
    assert sequences == []


# tests handling of incomplete FASTA records, expecting headers without sequences
def test_get_fasta_lists_incomplete_records(tmp_path):
    incomplete_fasta_path = tmp_path / "incomplete.fasta"
    incomplete_fasta_content = ">CCDS1.1|chr1\n>CCDS2.1|chr2\n"
    incomplete_fasta_path.write_text(incomplete_fasta_content)

    headers, sequences = get_fasta_lists(str(incomplete_fasta_path))
    assert headers == ["CCDS1.1|chr1", "CCDS2.1|chr2"]
    assert sequences == ["", ""]


# tests multiline sequence handling in FASTA files, expecting concatenated sequences
def test_get_fasta_lists_multiline_sequences(tmp_path):
    multiline_fasta_path = tmp_path / "multiline.fasta"
    multiline_fasta_content = ">CCDS1.1|chr1\nATG\nC\n>CCDS2.1|chr2\nGGG\nG\n"
    multiline_fasta_path.write_text(multiline_fasta_content)

    headers, sequences = get_fasta_lists(str(multiline_fasta_path))
    assert headers == ["CCDS1.1|chr1", "CCDS2.1|chr2"]
    assert sequences == ["ATGC", "GGGG"]


# tests get_fasta_lists with an unexpected header format, expecting correct parsing
def test_get_fasta_lists_unexpected_header_format(tmp_path):
    unexpected_format_fasta_path = tmp_path / "unexpected_header.fasta"
    unexpected_format_fasta_content = ">UnexpectedHeader\nATGC\n"
    unexpected_format_fasta_path.write_text(unexpected_format_fasta_content)

    headers, sequences = get_fasta_lists(str(unexpected_format_fasta_path))
    assert headers == ["UnexpectedHeader"]
    assert sequences == ["ATGC"]
