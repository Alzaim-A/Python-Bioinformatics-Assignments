# Assignment 5 README
### Author: Adam Alzaim

## Overview
This project is designed to facilitate bioinformatics analyses through a set of Python scripts. It primarily focuses on sequence attribute analysis and manipulation, using various bioinformatics files. The core of the project lies in `main.py`, which orchestrates the execution of the project's functionalities. Supporting scripts like `io_utils.py` and `seq_attribute_utils.py` provide input/output operations and sequence attribute manipulations, respectively. Test scripts ensure the reliability of the utility functions.


## How to Run the Scripts
#### main.py
`python -m sequence_attributes.main --infile_ccds_fasta  sequence_attributes/inputs/CCDS_nucleotide.current.fna --infile_ccds_attributes sequence_attributes/inputs/CCDS.current.txt --infile_ensembl_gene sequence_attributes/inputs/ensembl_gene_data.tsv --excel_outfile sequence_attributes.xlsx`

#### test_seq_attribute_utils.py:
`pytest test_seq_attribute_utils.py`

#### test_io_utils.py:
`pytest test_io_utils.py`

#### test_fasta_format.py:
`pytest test_fasta_format.py`

- *To generate coverage reports*:
`
pytest --cov=. --cov-report term --cov-report html
`

## Documentation

### Main Scripts
#### main.py
- `get_cli_args()`:This function parses and returns the arguments obtained from the command line.

- `main()`:This function serves as the central orchestrator for processing CCDS and Ensembl gene data alongside FASTA sequences, ultimately generating an two Excel files with the results. Its steps include parsing command-line arguments for input and output files, loading and preprocessing CCDS attributes and Ensembl gene data, merging data frames, retrieving FASTA sequences, extracting additional sequence attributes, compiling a summary DataFrame, and saving the summary to a TSV and XLSX file.

### Utility Scripts
#### seq_attributes_utils.py
- `calculate_amino_acid_content(protein_sequence, amino_acid, round_to)`:This function calculates the percentage content of a specified amino acid in a given protein sequence. It takes the protein sequence, the amino acid to calculate the content for, and an optional parameter to round the result to a specified number of decimal places.

- `return_standard_genetic_code()`:This function returns a dictionary representing the standard genetic code mapping from codons to amino acids. It provides a key-value mapping where each key is a codon (RNA sequence) and its corresponding value is the single-letter code of the amino acid or None for stop codons.

- `protein_translation(dna_sequence, genetic_code)`:This function translates a DNA sequence into a protein sequence using the provided genetic code. It takes the DNA sequence and the genetic code dictionary as inputs and returns the resulting protein sequence.

- `extract_kmers(dna_sequence, k)`:This function extracts all possible k-mers of a specified length from a given DNA sequence. It takes the DNA sequence and the length of each k-mer as inputs and returns a list of all extracted k-mers.

- `get_sequence_composition(dna_sequence)`:This function calculates the nucleotide composition of a DNA sequence. It counts the occurrences of each nucleotide symbol ('A', 'T', 'C', 'G') in the sequence and returns a dictionary with nucleotide symbols as keys and their counts as values.

- `gc_content(dna_sequence)`:This function calculates the GC content of a DNA sequence, i.e., the percentage of guanine (G) and cytosine (C) bases in the sequence. It takes the DNA sequence as input and returns the GC content as a percentage of the total sequence length.

- `get_tm_from_dna_sequence(dna_sequence)`:This function calculates the melting temperature (Tm) of a DNA sequence using the nearest-neighbor thermodynamic model. It estimates the Tm based on the sequence's thermodynamic parameters and returns the calculated Tm in degrees Celsius.

- `lookup_by_ccds(ccds_id, df, chrom=None)`:This function filters a DataFrame for rows matching a specified CCDS ID and optionally a chromosome. It takes the CCDS ID, the DataFrame to filter, and an optional chromosome number as inputs and returns a filtered DataFrame based on the specified criteria.

- `get_additional_sequence_attributes(headers, dna_sequence, attribute_df, genetic_code)`: This function compiles various attributes of a DNA sequence into a structured format. It takes the header information, DNA sequence, additional gene information DataFrame, and genetic code dictionary as inputs and returns a namedtuple containing calculated and extracted sequence attributes.

#### io_utils.py
- `FileHandler` class: This class is designed to streamline file management tasks by implementing automatic closing and exception handling. It allows for more robust error management and cleaner code by utilizing the context manager protocol. 

- `__enter__()` method: This method is called when entering a with statement. If successful, it returns the opened file object, allowing operations to be performed within the with block.

- `__exit__()` method: This method closes the file object opened in the __enter__() method, regardless of whether an exception occurred during execution within the with block. 

### Test Scripts
#### test_seq_attributes_utils.py
- `test_calculate_amino_acid_content()`: This function assesses the accuracy of the calculate_amino_acid_content function by verifying its ability to compute the percentage of a specified amino acid in a protein sequence.

- `test_return_standard_genetic_code()`: This function verifies the correctness of the return_standard_genetic_code function, ensuring that it correctly returns the standard genetic code mapping from codons to amino acids.

- `test_protein_translation()`: This function evaluates the protein_translation function, validating its capability to translate a DNA sequence into a protein sequence based on the provided genetic code.

- `test_extract_kmers()`: This function examines the behavior of the extract_kmers function, confirming its ability to extract k-mers of a specified length from a given DNA sequence.

- `test_get_sequence_composition()`: This function tests the correctness of the get_sequence_composition function by assessing its ability to calculate the nucleotide composition of a DNA sequence.

- `test_gc_content()`: This function validates the accuracy of the gc_content function in computing the GC content of a DNA sequence.

- `test_get_tm_from_dna_sequence()`: This function evaluates the correctness of the get_tm_from_dna_sequence function by checking its ability to calculate the melting temperature (Tm) of a DNA sequence.

- `test_lookup_by_ccds()`: This function assesses the functionality of the lookup_by_ccds function, ensuring its ability to filter a DataFrame based on a specified CCDS ID and chromosome.

#### test_io_utils.py
- `test_file_handler_reading()`:This test verifies that the FileHandler class can successfully read content from a file. It creates a test file, writes a string to it, reads the content using FileHandler, and compares it with the expected string. If the content matches the expected string, the test passes.

- `test_file_handler_writing()`:This test ensures that the FileHandler class can successfully write content to a file. It writes a test string to a file using FileHandler, reads the content from the file, and compares it with the expected string. If the content matches the test string, the test passes.

- `test_file_handler_os_error()`:This test evaluates the behavior of the FileHandler class when attempting to open a non-existent file. It uses pytest.raises to check whether an OSError is raised when trying to open a non-existent file. If an OSError is raised as expected, the test passes.

- `test_file_handler_value_error()`:This test ensures that the FileHandler class raises a ValueError when an invalid mode is provided. It uses pytest.raises to check whether a ValueError is raised when an invalid mode is passed to FileHandler. If a ValueError is raised as expected, the test passes.

## Expected Output

#### main.py
The script generates two main output files. The primary output is an Excel file named sequence_attributes.xlsx, which contains detailed information about the processed genes, including sequence attributes and gene data merged from the CCDS attributes and Ensembl gene data files. This Excel file provides a comprehensive overview of the analyzed genes and their associated sequence attributes. Additionally, the script produces a .tsv representing the top and bottom genes based on their proline composition. This file summarizes the top 10 genes with the highest proline composition and the last 10 genes with the lowest proline composition, allowing for quick insights into the variability of proline content across the analyzed gene dataset.

