"""intersection_of_gene_names.py"""
import argparse
from assignment4.assignment4_utils import read_file_lines, parse_lines_to_dict
from assignment4.io_utils import mkdir_from_infile


def get_cli_args():
    """
    Sets up and parses command-line arguments for comparing two gene lists.
    @return: Namespace object with command-line arguments as attributes.
    """
    # setup cli arguments for gene list files
    parser = argparse.ArgumentParser(description="Provide two gene lists (ignore header line), find intersection")
    parser.add_argument('-i1', '--infile1', type=str, required=False,
                        default='chr21_genes.txt', help="Gene list 1 to open")
    parser.add_argument('-i2', '--infile2', type=str, required=False,
                        default='HUGO_genes.txt', help="Gene list 2 to open")
    return parser.parse_args()


def print_output(outfile: str, common_genes: set, infile1_count: int, infile2_count: int, infile1: str, infile2: str):
    """
    Writes the intersection of two gene lists to an output file and prints statistics.
    @param outfile: Path to the output file where common genes will be stored.
    @param common_genes: Set containing common gene symbols found in both input files.
    @param infile1_count: Number of unique gene names in the first input file.
    @param infile2_count: Number of unique gene names in the second input file.
    @param infile1: Name/path of the first input file.
    @param infile2: Name/path of the second input file.
    @return: None
    """
    # ensure directory exists for output file
    mkdir_from_infile(outfile)
    # write common genes to output file
    with open(outfile, 'w') as f:
        for gene in sorted(common_genes):
            f.write(gene + '\n')
    # print stats to console
    print(f"Number of unique gene names in {infile1}: {infile1_count}")
    print(f"Number of unique gene names in {infile2}: {infile2_count}")
    print(f"Number of common gene symbols found: {len(common_genes)}")
    print(f"Output stored in {outfile}")


def main():
    """
    Main function that finds the intersection of two gene lists and outputs the result.
    @return: None
    """
    # parse command-line arguments
    args = get_cli_args()

    # read and skip header for both gene files
    lines1 = read_file_lines(args.infile1, skip_header=True)
    lines2 = read_file_lines(args.infile2, skip_header=True)

    # parse lines into dictionaries
    gene_name1 = parse_lines_to_dict(lines1, to_lower=False)
    gene_name2 = parse_lines_to_dict(lines2, to_lower=False)

    # find intersection of gene names
    genes1 = set(gene_name1.keys())
    genes2 = set(gene_name2.keys())
    common_genes = genes1.intersection(genes2)

    # print results to specified output file
    print_output("OUTPUT/intersection_output.txt", common_genes, len(genes1), len(genes2), args.infile1, args.infile2)


if __name__ == "__main__":
    main()
