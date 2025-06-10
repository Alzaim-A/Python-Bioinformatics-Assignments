"""
File: secondary_structure_splitter.py
Splits a combined FASTA file of protein sequences
and their secondary structures into two files
Usage: python secondary_structure_splitter.py --infile <FASTA file>

"""
import argparse
import sys


def get_cli_args():  #pragma: no cover
    """
    Parses command-line arguments
    @return: Namespace object containing the input file path
    """
    parser = argparse.ArgumentParser(description='Split a FASTA file '
                                                 'into sequences and secondary structures.')
    parser.add_argument('-i', '--infile', type=str, required=True, help='Path to input FASTA file')
    return parser.parse_args()


def get_fasta_lists(fasta_filename):
    """
    Separates FASTA file contents into headers and sequences
    @param fasta_filename: Path to the FASTA file to be processed
    @return: A tuple containing two lists, the first for headers, the second for sequences.
    """
    #Intitialize empty list and string for header and sequence count storage
    headers, sequences = [], []
    current_seq = ''
    #Open FASTA for reading and iterate over each line
    with open(fasta_filename, 'r', encoding='utf-8') as in_fh:
        #For loop going over each line dealing with headers and appending
        #header and sequence data to current_seq, then header and sequence list
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
    #calls _verify_lists helper function
    _verify_lists(headers, sequences)
    return headers, sequences


def _verify_lists(headers, sequences):
    """
    Compares the sizes of headers and sequences lists to confirm they match
    the FASTA format.
    @param headers: List of sequence headers.
    @param sequences: List of sequences.
    @raise SystemExit: If the sizes of headers and sequences lists do not match.
    """
    if len(headers) != len(sequences):
        sys.exit(
            "Error: Header and Sequence lists are different in size."
            " Check if the FASTA file is properly formatted.")


def output_results_to_files(headers, sequences,protein_file='pdb_protein.fasta',
                            ss_file='pdb_ss.fasta'):
    """
    Writes sequences and secondary structures to separate files
    @param headers: List containing all headers from the FASTA file
    @param sequences: List containing all sequences from the FASTA file
    @param protein_file: Filename for the output FASTA file with protein sequences
    @param ss_file: Filename for the output FASTA file with secondary structures
    """
    #Initialize list for protein_seqs and ss_seqs
    protein_seqs = []
    ss_seqs = []
    for header, sequence in zip(headers, sequences):
        if 'sequence' in header:
            protein_seqs.append((header, sequence))
        else:
            ss_seqs.append((header, sequence))
    #Open file to write output file, protein_seqs
    with open(protein_file, 'w', encoding='utf-8') as pfh:
        for header, seq in protein_seqs:
            pfh.write(f"{header}\n{seq}\n")
    # Open file to write output file, ss_seqs
    with open(ss_file, 'w', encoding='utf-8') as sfh:
        for header, seq in ss_seqs:
            sfh.write(f"{header}\n{seq}\n")

    print(f"Found {len(protein_seqs)} protein sequences", file=sys.stderr)
    print(f"Found {len(ss_seqs)} ss sequences", file=sys.stderr)


def main():  #pragma: no cover
    """
    Main Function
    """
    args = get_cli_args()
    headers, sequences = get_fasta_lists(args.infile)
    output_results_to_files(headers, sequences)


if __name__ == '__main__':  #pragma: no cover
    main()
