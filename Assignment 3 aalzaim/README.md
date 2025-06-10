
# Assignment 3 README
### Author: Adam Alzaim

## Overview of the Assignment
This project includes four Python scripts designed to process FASTA files for bioinformatics analysis. Two main scripts, `secondary_structure_splitter.py` and `nt_fasta_stats.py`, perform specific tasks on FASTA files, including splitting sequence and structure data and calculating nucleotide composition statistics, respectively. Additionally, two test scripts provide examples of how to validate the functionality of the main scripts.
## How to Run the Scripts
Running `secondary_structure_splitter.py`:

`
python secondary_structure_splitter.py --infile <FASTA file>
`

Running `nt_fasta_stats.py`:

`
python nt_fasta_stats.py --infile <input_fasta_file> --outfile <output_stats_file>
`

Running `test_secondary_structure_splitter.py`:

`
pytest test_secondary_structure_splitter.py
`

`
pytest --cov=. --cov-report term --cov-report html
`

Running `test_nt_fasta_stats.py`:

`
pytest test_nt_fasta_stats.py
`

`
pytest --cov=. --cov-report term --cov-report html
`

## Documentation

## secondary_structure_splitter.py
### Important Functions:
`get_cli_args()`: Parses command-line arguments to obtain the path to the input FASTA file. Utilizes the argparse module for easy CLI interface creation.

`get_fasta_lists(fasta_filename)`: Reads the input FASTA file, separates the content into headers and sequences, and verifies the integrity of the FASTA format. 

`_verify_lists(headers, sequences)`: Ensures that the numbers of headers and sequences match.

`output_results_to_files(headers, sequences, protein_file, ss_file)`: Writes the separated sequence and structure data into two distinct FASTA files. 

## nt_fasta_stats.py
### Important Functions:
`get_cli_args()`: Parses command-line arguments to obtain paths for both the input FASTA file and the output file for statistics.

`get_fasta_lists(fasta_filename)`: Extracts headers and sequences from the input FASTA file.

`_verify_lists(headers, sequences)`: Confirms that the headers and sequences lists are of equal length.

`_get_num_nucleotides(nucleotide, sequence)`: Counts the occurrences of a specified nucleotide within a given sequence.

`_get_ncbi_accession(header)`: Extracts the NCBI accession number from a sequence header.

`print_sequence_stats(headers, sequences, outfile_name)`: Writes the calculated nucleotide statistics to an output file.

## Test Scripts
### test_secondary_structure_splitter.py
`test_verify_lists_equal_size()`: Tests that _verify_lists does not raise an error for lists of equal size, ensuring the script correctly handles well-formatted FASTA files.

`test_verify_lists_different_size()`: Tests that _verify_lists raises an error for lists of different sizes, which helps identify improperly formatted FASTA files.

`test_get_fasta_lists_real_file()`: Verifies that get_fasta_lists can accurately parse headers and sequences from a real FASTA file, ensuring the script's functionality with actual data.

### test_nt_fasta_stats.py
`test_get_num_nucleotides()`: Validates the accuracy of _get_num_nucleotides in counting nucleotides.

`test_get_fasta_lists_real_file()`: Checks that get_fasta_lists functions correctly with real FASTA file.

## Expected Output
`secondary_structure_splitter.py` generates two output FASTA files: one containing protein sequences and the other containing secondary structures. It will also output the length of the protein sequence and secondary structure. 

`nt_fasta_stats.py` generates an output file detailing the nucleotide composition statistics of the input FASTA file.