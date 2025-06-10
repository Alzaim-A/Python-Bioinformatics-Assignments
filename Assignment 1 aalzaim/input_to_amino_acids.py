"""input_to_amino_acids.py"""
import sys


def main():
    """Ask the user for input"""
    gene_name = input("Please enter a name for the DNA sequence: ")
    print("Your sequence name is:", gene_name)

    try:
        nucleotides_length = int(input("Please enter the length of the sequence: "))
    except ValueError:
        print("\n\nError: Please enter a valid number for the sequence length", file=sys.stderr)
        sys.exit(1)

    print("The length of the DNA sequence is:", nucleotides_length)

    # Check if the sequence length is divisible by 3
    if nucleotides_length % 3 != 0:
        print("\n\nError: the DNA sequence is not a multiple of 3", file=sys.stderr)
        sys.exit(1)

    # Calculate the number of amino acids and the protein's estimated molecular weight
    amino_acids_length = nucleotides_length / 3
    average_weight_per_aa = 110  # in Daltons
    molecular_weight_kda = (amino_acids_length * average_weight_per_aa) / 1000

    # Print the results
    print("The length of the decoded protein is:", amino_acids_length)
    print("The average weight of the protein sequence is:", round(molecular_weight_kda, 2))


if __name__ == "__main__":
    main()
