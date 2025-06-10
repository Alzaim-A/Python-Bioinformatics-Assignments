"""
File: nt_fasta_stats.py
Calculates and reports nucleotide composition statistics from FASTA files.
Usage: python nt_fasta_stats.py --infile <input_fasta_file> --outfile <output_stats_file>
"""

import argparse
import sys


def get_cli_args(): #pragma: no cover
    """
    Takes command-line inputs to specify the input FASTA file and the output
    file for statistics.
    @return: Parsed command-line arguments with input and output file paths.
    """
    parser = argparse.ArgumentParser(description="Provide a FASTA "
                                                 "file to generate nucleotide statistics.")
    parser.add_argument("-i", "--infile", type=str, required=True, help="Path to file to open")
    parser.add_argument("-o", "--outfile", type=str, required=True, help="Path to file to write")
    return parser.parse_args()


def get_fasta_lists(fasta_filename):
    """
    Separates a FASTA file into lists of headers and sequences
    @param fasta_filename: Path to the FASTA file to be processed
    @return: Two lists, one of headers and one of sequences,
    maintaining their order of appearance in the file
    """
    # Intitialize empty list and string for header and sequence count storage
    headers, sequences = [], []
    current_seq = ''
    # Open FASTA for reading and iterate over each line
    with open(fasta_filename, 'r', encoding='utf-8') as in_fh:
        # For loop going over each line dealing with headers and appending
        # header and sequence data to current_seq, then header and sequence list
        for line in in_fh:
            line = line.strip()
            if line.startswith('>'):
                if current_seq:
                    sequences.append(current_seq)
                    current_seq = ''
                headers.append(line)
            else:
                current_seq += line
        if current_seq:
            sequences.append(current_seq)
    return headers, sequences


def _verify_lists(headers, sequences):
    """
    Confirms the lists of headers and sequences are of equal length
    @param headers: List of sequence headers
    @param sequences: List of nucleotide sequences
    @raise SystemExit: If the lengths of the headers and sequences lists do not match
    """
    if len(headers) != len(sequences):
        sys.exit("Error: Header and Sequence lists are different in size.")
def _get_num_nucleotides(nucleotide, sequence):
    """
    Counts the occurrences of a specified nucleotide in a sequence.
    Validates the nucleotide type before counting its occurrences in the given sequence.
    @param nucleotide: A character representing the nucleotide ('A', 'T', 'G', 'C', or 'N').
    @param sequence: The nucleotide sequence to search.
    @return: The count of the specified nucleotide within the sequence.
    """
    if nucleotide not in ['A', 'T', 'G', 'C', 'N']:
        sys.exit("Non-nucleotide sequence")
    return sequence.count(nucleotide)


def _get_ncbi_accession(header):
    """
    Extracts the NCBI accession number from a sequence header.
    Splits the header string to retrieve the NCBI accession number, if available.
    @param header: The header line from the FASTA file.
    @return: The NCBI accession number or 'Unknown' if not applicable.
    """
    parts = header.split('|')
    return parts[1] if len(parts) > 1 else 'Unknown'


def print_sequence_stats(headers, sequences, outfile_name):
    """
    Writes nucleotide statistics for each sequence to an output file
    @param headers: List of sequence headers
    @param sequences: List of nucleotide sequences
    @param outfile_name: Filename for the output statistics file
    """
    # Open file to write output file
    with open(outfile_name, 'w', encoding='utf-8') as out_fh:
        out_fh.write("Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\n")
        for idx, (header, seq) in enumerate(zip(headers, sequences), start=1):
            a_count = _get_num_nucleotides('A', seq)
            t_count = _get_num_nucleotides('T', seq)
            g_count = _get_num_nucleotides('G', seq)
            c_count = _get_num_nucleotides('C', seq)
            n_count = _get_num_nucleotides('N', seq)
            length = len(seq)
            gc_percent = ((g_count + c_count) / length) * 100 if length else 0
            accession = _get_ncbi_accession(header)
            out_fh.write(f"{idx}\t{accession}\t{a_count}\t{g_count}"
                         f"\t{c_count}\t{t_count}\t{n_count}\t{length}\t{gc_percent:.1f}\n")


def main():  #pragma: no cover
    """
    Main Function
    """
    args = get_cli_args()
    headers, sequences = get_fasta_lists(args.infile)
    _verify_lists(headers, sequences)
    print_sequence_stats(headers, sequences, args.outfile)


if __name__ == '__main__':  #pragma: no cover
    main()
