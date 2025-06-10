"""find_common_cats.py"""
import argparse
from assignment4.assignment4_utils import (read_file_lines,
                                           parse_lines_to_dict, count_gene_categories, sort_categories_by_code)
from assignment4.io_utils import mkdir_from_infile


def get_cli_args():
    """
    Parses command-line arguments for the script.
    @return: Namespace object containing arguments and their values.
    """
    # define cli arguments
    parser = argparse.ArgumentParser(description="Count gene categories and provide descriptions")
    parser.add_argument('-i1', '--infile1', type=str, required=False,
                        default='chr21_genes.txt', help="Path to the chr21_genes.txt file")
    parser.add_argument('-i2', '--infile2', type=str, required=False,
                        default='chr21_genes_categories.txt', help="Path to the chr21_genes_categories.txt file")
    return parser.parse_args()


def print_output(outfile: str, sorted_categories: list, category_descriptions: dict):
    """
    Writes the sorted categories and their descriptions to an output file.
    @param outfile: Path to the output file.
    @param sorted_categories: List of tuples containing categories and their occurrence counts.
    @param category_descriptions: Dictionary mapping categories to their descriptions.
    @return: None
    """
    # create output directory if it doesn't exist
    mkdir_from_infile(outfile)
    # write output to file
    with open(outfile, 'w') as f:
        f.write("Category\tOccurrence\tDescription\n")
        for category, count in sorted_categories:
            description = category_descriptions.get(category, "No description available")
            f.write(f"{category}\t{count}\t{description}\n")
    # confirm output location
    print(f"Output written to {outfile}")


def main():
    """
    Main function to execute script workflow: reads gene files,
    counts and sorts categories, then prints output.
    @return: None
    """
    # parse cli arguments
    args = get_cli_args()

    # read lines from gene files, skipping headers
    lines = read_file_lines(args.infile1, skip_header=True)
    description_lines = read_file_lines(args.infile2)

    # count categories from gene file
    category_counts = count_gene_categories(lines)
    # parse_lines_to_dict
    category_descriptions = parse_lines_to_dict(description_lines, to_lower=False)

    # sort categories by their code
    sorted_categories = sort_categories_by_code(category_counts)

    # print sorted categories and descriptions to output file
    print_output("OUTPUT/categories.txt", sorted_categories, category_descriptions)


if __name__ == "__main__":
    main()
