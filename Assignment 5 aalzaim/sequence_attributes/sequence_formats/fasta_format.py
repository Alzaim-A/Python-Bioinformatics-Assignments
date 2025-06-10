"""fasta_format.py
This script reads FASTA files, extracting headers and sequences into separate lists.
It ensures headers and sequences align properly, throwing an error otherwise.
"""
from typing import Tuple, List
from sequence_attributes.utils.io_utils import FileHandler


def _verify_lists(header_list: List[str], seq_list: List[str]) -> bool:
    """
        Checks if header and sequence lists have the same length.

        @param header_list: List of header strings.
        @param seq_list: List of sequence strings.
        @return: True if both lists have the same length, otherwise raises ValueError.
        """
    if len(header_list) != len(seq_list):
        raise ValueError("Header and sequence lists have different lengths.")
    return True


def get_fasta_lists(infile: str) -> Tuple[List[str], List[str]]:
    """
        Parses a FASTA file into separate lists for headers and sequences.

        @param infile: Path to the FASTA file.
        @return: A tuple of two lists - (headers, sequences).
        """
    headers = []
    sequences = []
    seq = ""  # initialization
    with FileHandler(infile, mode='r', encoding='utf-8') as file:
        for line in file:  # open file and iterate over each line
            if line.startswith('>'):  # check if the line is a header
                if seq or headers:
                    sequences.append(seq)
                    seq = ""  # reset sequence variable
                header = line.strip().lstrip('>')
                headers.append(header)
            else:
                seq += line.strip()  # add sequence line to current sequence string
        if seq or headers:
            sequences.append(seq)
    _verify_lists(headers, sequences)
    return headers, sequences  # return the lists of headers and sequences


if __name__ == "__main__":
    infile = args.infile_ccds_fasta

    headers, sequences = get_fasta_lists(infile)
