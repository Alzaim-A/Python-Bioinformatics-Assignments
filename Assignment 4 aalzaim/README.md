# Assignment 4 README
### Author: Adam Alzaim

## Overview of the Assignment
This project includes three main Python scripts, two utility scripts and two test scripts. The main scripts are `find_common_cats.py`, `gene_names_from_ch21.py`, and `intersection_of_gene_names.py`, which collectively provide functionalities for counting gene categories, interactive querying of gene names, and finding intersections between gene lists, respectively. The utility scripts `assignment4_utils.py` and `io_utils.py` support these main scripts by providing essential functionalities like file reading and directory management. Additionally the test scripts `test_assignment4_utils.py` and `test_io_utils.py`, validate the functionality of the utility scripts.

## How to Run the Scripts
#### find_common_cats.py:
`python find_common_cats.py --infile1 <file1.txt> --infile2 <file2.txt>` (infile optional)

#### gene_names_from_ch21.py:
`python gene_names_from_ch21.py --infile <file1.txt>`(infile optional)

#### intersection_of_gene_names.py:
`python intersection_of_gene_names.py --infile1 <file1.txt> --infile2 <file2.txt>`(infile optional)

#### test_assignment4_utils.py:
`pytest test_assignment4_utils.py`

#### test_io_utils.py:
`pytest test_assignment4_utils.py`

- *To generate coverage reports*:
`
pytest --cov=. --cov-report term --cov-report html
`
#### assignment4_utils.py & io_utils.py
Import functions as needed in main scripts 

## Documentation

### Main Scripts
#### find_common_cats.py
- `get_cli_args()`: Parses command-line arguments, specifically two input file paths.
- `print_output(outfile, sorted_categories, category_descriptions)`: Outputs sorted gene categories and their descriptions to a specified file. It ensures the output directory exists and writes detailed category data.
- `main()` :Orchestrates the script's workflow, beginning with parsing command-line arguments via `get_cli_args()`. It then reads gene files, counting and sorting categories using functions imported from `assignment4_utils.py`. Finally, it calls `print_output()` to generate a detailed output file containing sorted gene categories and their descriptions.

#### gene_names_from_ch21.py
- `get_cli_args()`: Sets up and parses command-line arguments for specifying the gene list file.
- `print_output(gene_dict)`: Engages the user in an interactive session to query gene names and display their descriptions based on input.
- `main()` : Manages the script's workflow for interactive querying of gene names. It first parses a specified gene list file to create a dictionary mapping gene names to descriptions. Then, it engages the user in an interactive session, allowing them to input gene names and receive descriptions in response. This interaction continues until the user exits by typing 'quit' or 'exit'.

#### intersection_of_gene_names.py
- `get_cli_args()`: Parses command-line arguments for two gene list files to compare.
- `print_output(outfile, common_genes, infile1_count, infile2_count, infile1, infile2)`: Writes the common gene names found in both input files to an output file and prints related statistics.
- `main()` :Uses command-line arguments to identify two gene list files for comparison. It reads and parses both files to dictionaries, then finds the intersection of gene names between them. This list of common genes, along with statistics about the gene lists, is then outputted both to a file and the console.

### Utility Scripts
#### assignment4_utils.py
- `read_file_lines(file_path, skip_header)`: Reads a file line-by-line, optionally skipping the first line, and returns a list of stripped lines.
- `parse_lines_to_dict(lines, to_lower)`: Converts a list of lines into a dictionary, with an option to lowercase dictionary keys.
- `count_gene_categories(lines)`: Counts the occurrences of gene categories within a list of gene data lines.
- `sort_categories_by_code(category_counts)`: Sorts gene categories based on a hierarchical code system, facilitating ordered data analysis.

#### io_utils.py
- `mkdir_from_infile(file)`: Attempts to create a directory from the given file path, handling various filesystem errors gracefully.

### Test Scripts
#### test_assignment4_utils.py
- `test_read_file_lines()`: Verifies that the function correctly reads file lines, with and without skipping headers.
- `test_parse_lines_to_dict()`: Tests dictionary parsing functionality under different conditions, including lowercasing keys.
- `test_count_gene_categories()`: Checks the accuracy of gene category counting against expected results.
- `test_sort_categories_by_code()`: Ensures gene categories are sorted correctly by their codes.

#### test_io_utils.py
- `test_mkdir_from_infile()`: Confirms directory creation for new file paths and proper handling of existing directories.
- `test_mkdir_from_infile_empty_path()` and `test_mkdir_from_infile_path_with_no_directory_raises_error()`: Validates error handling for invalid file paths.

## Expected Output

#### find_common_cats.py
This script generates an output file named "categories.txt" containing a list of gene categories found in the input files, along with their occurrence counts and descriptions. 

#### gene_names_from_ch21.py
This script enters an interactive mode where the user is prompted to input gene names. For each valid gene name entered, the script prints the gene's name (in uppercase) and its description to the console. If a gene name does not exist within the input file, the script notifies the user that it's not a valid gene name. The interactive session continues until the user types 'quit' or 'exit'.

#### intersection_of_gene_names.py
This script outputs a file named "intersection_output.txt" listing all gene names that are common between the two input files. Additionally, the script prints statistics to the console, including the number of unique gene names in each input file and the total number of common gene symbols found. A confirmation message indicating the location of the output file is also printed to the console.

