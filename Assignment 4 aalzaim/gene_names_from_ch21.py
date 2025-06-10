"""gene_names_from_ch21.py"""
import argparse
from assignment4.assignment4_utils import read_file_lines, parse_lines_to_dict


def get_cli_args():
    """
    Sets up command-line arguments for the script and parses them.
    @return: Namespace object with command-line arguments as attributes.
    """
    # define and parse cli arguments
    parser = argparse.ArgumentParser(description="Open chr21_genes.txt, and ask user for a gene name")
    parser.add_argument('-i', '--infile', type=str, required=False,
                        default='chr21_genes.txt', help="Path to the chr21_genes.txt file")
    return parser.parse_args()


def print_output(gene_dict: dict):
    """
    Interactively queries the user for gene names and prints their descriptions if found.
    @param gene_dict: A dictionary mapping gene symbols (as lowercase strings) to their descriptions.
    @return: None
    """
    # prompt user for gene names and provide descriptions
    print("Enter gene name of interest. Type 'quit' to exit:")
    while True:
        gene_symbol = input("> ").strip().lower()  # handle user input case-insensitively
        if gene_symbol in ['quit', 'exit']:
            print("Thanks for querying the data.")
            break
        elif gene_symbol in gene_dict:
            print(f"{gene_symbol.upper()} found! Here is the description: \n{gene_dict[gene_symbol]}")
        else:
            print("Not a valid gene name.")


def main():
    """
    Main function to execute the script's workflow: reads gene descriptions from a file,
    then allows the user to query this data interactively.
    @return: None
    """
    # parse cli arguments
    args = get_cli_args()

    # read file and parse gene descriptions, sets headers to skip
    lines = read_file_lines(args.infile, skip_header=True)
    # sets parse_lines_to_dict to lowercase
    gene_dict = parse_lines_to_dict(lines, to_lower=True)

    # interactive gene query
    print_output(gene_dict)


if __name__ == "__main__":
    main()
