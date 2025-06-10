"""seq_attribute_utils.py
This program acts as a utility script for the main.py script. It calculates amino acid content,
translates DNA sequences to proteins, extracts k-mers, and computes nucleotide composition
and GC content. Additionally, it estimates DNA melting temperature,
filters gene data by CCDS ID and chromosome, and compiles sequence
attributes for genomic analysis.
"""
import argparse
from collections import namedtuple
from typing import Tuple, List, Dict, Union
from sequence_attributes.sequence_formats.fasta_format import get_fasta_lists
import pandas as pd


def calculate_amino_acid_content(
        protein_sequence: str, amino_acid: str, round_to: int = 2) -> float:
    """
       Calculates the content of a specified amino acid in a protein sequence.

       @param protein_sequence: The protein sequence as a string.
       @param amino_acid: The single-letter code of the amino acid to calculate the content for.
       @param round_to: The number of decimal places to round the result to.
       @return: The percentage of the protein sequence composed of the specified
       amino acid, rounded to `round_to` decimal places.
       """

    amino_acid_count = protein_sequence.upper().count(amino_acid.upper())
    total_length = len(protein_sequence)  # total length of the protein sequence

    if total_length == 0:   # if sequence is empty
        return 0.0

    percentage = (amino_acid_count / total_length) * 100
    return round(percentage, round_to)
# return rounded percentage


def return_standard_genetic_code() -> Dict[str, Union[str, None]]:
    """
    Returns the standard genetic code mapping from codons to amino acids.

    @return: A dictionary where each key is a codon (RNA sequence)
    and its value is the corresponding amino acid single-letter code
    or None for stop codons.
    """
    # returns a dictionary mapping of codons to amino acids or stop codons
    return {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": None, "UAG": None,
        "UGU": "C", "UGC": "C", "UGA": None, "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }


def protein_translation(dna_sequence: str, genetic_code: Dict[str, Union[str, None]]) -> str:
    """
    Translates a DNA sequence into a protein sequence using a provided genetic code.

    @param dna_sequence: The DNA sequence to be translated.
    @param genetic_code: A dictionary representing the genetic code, mapping codons to amino acids.
    @return: The protein sequence resulting from the translation of the input DNA sequence.
    """

    protein_sequence = ""
    # DNA to RNA conversion
    rna_sequence = dna_sequence.upper().replace("T", "U")
    for i in range(0, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i+3]  # extract a codon
        # get the corresponding amino acid
        amino_acid = genetic_code.get(codon)
        if amino_acid:
            protein_sequence += amino_acid
        else:  # stop translation at stop codon
            break
    return protein_sequence


def extract_kmers(dna_sequence: str, k: int) -> List[str]:
    """
    Extracts all possible k-mers of a specified length from a given DNA sequence.

    @param dna_sequence: The DNA sequence from which to extract k-mers.
    @param k: The length of each k-mer.
    @return: A list of all possible k-mers of length k extracted from the input sequence.
    """

    k_mers = []
    for i in range(len(dna_sequence) - k + 1):
        # append k-mer to the list
        k_mers.append(dna_sequence[i:i+k])
    return k_mers


def get_sequence_composition(dna_sequence: str) -> dict:
    """
    Calculates the nucleotide composition of a DNA sequence.

    @param dna_sequence: The DNA sequence to analyze.
    @return: A dictionary with nucleotide symbols as keys and their counts as values.
    """
    # initialize nucleotide counts
    composition = {"A": 0, "T": 0, "C": 0, "G": 0}
    # iterate through each nucleotide in sequence
    for nucleotide in dna_sequence:
        if nucleotide in composition:
            composition[nucleotide] += 1
    return composition


def gc_content(dna_sequence: str) -> float:
    """
    Calculates the GC content of a DNA sequence.

    @param dna_sequence: The DNA sequence to analyze.
    @return: The GC content as a percentage of the total sequence length.
    """

    if isinstance(dna_sequence, str) and dna_sequence:
        # sum of g and c in dna sequence
        g_c_count = sum(nuc in ['G', 'C'] for nuc in dna_sequence)
        return round((g_c_count / len(dna_sequence)) * 100, 2)
    else:
        return 0.0


"""
coded a version of the get_tm_from_dna_sequence function like the way it was coded in 
the class example but could not get it to give me accurate/realist looking melting points
so instead I have included a different version of the function 
that uses the nearest-neighbor model as outlined in the 
directions

def get_tm_from_dna_sequence(dna_sequence: str) -> float:
        
    tm_parameters = {
        "AA": 2.3, "AT": 2.0, "TA": 2.0, "TT": 2.3,
        "CG": 3.0, "GC": 3.1, "GA": 3.1, "GG": 3.3,
        "CT": 3.3, "TC": 3.3, "AC": 2.4, "CA": 2.4,
        "GT": 3.4, "TG": 3.4, "AG": 2.5, "CC": 4.0
    }

   
    dna_sequence = dna_sequence.upper()
    tm_value = sum(tm_parameters.get(dna_sequence[i:i + 2], 0) for i in range(len(dna_sequence) - 1))
    return round(tm_value, 2)
"""


def get_tm_from_dna_sequence(dna_sequence: str) -> float:
    """
        Calculates the melting temperature (Tm) of a DNA sequence.

        @param dna_sequence: The DNA sequence to analyze.
        @return: The calculated melting temperature in degrees Celsius.
        """

    if not dna_sequence or len(dna_sequence) < 2:
        return 0.0

    # logarithm function to compute ln(x) for Tm calculation
    def ln(x, n_terms=100):
        
        if x <= 0:
            raise ValueError("x must be positive")
        elif x == 1:
            return 0.0
        else:  # approximation of ln(x) using Taylor series
            x_transformed = (x - 1) / (x + 1)
            return 2 * sum(x_transformed ** (2 * n + 1) / (2 * n + 1) for n in range(n_terms))

    # thermodynamic parameters for delta H (enthalpy) and delta S (entropy)
    delta_h = {
        'AA': -7.9, 'AC': -8.4, 'AG': -7.8, 'AT': -7.2,
        'CA': -8.5, 'CC': -8.0, 'CG': -10.6, 'CT': -7.8,
        'GA': -8.2, 'GC': -9.8, 'GG': -8.0, 'GT': -8.4,
        'TA': -7.2, 'TC': -8.2, 'TG': -8.5, 'TT': -7.9,
    }

    delta_s = {
        'AA': -22.2, 'AC': -22.4, 'AG': -21.0, 'AT': -20.4,
        'CA': -22.7, 'CC': -19.9, 'CG': -27.2, 'CT': -21.0,
        'GA': -22.2, 'GC': -24.4, 'GG': -19.9, 'GT': -22.4,
        'TA': -21.3, 'TC': -22.2, 'TG': -22.7, 'TT': -22.2,
    }
    # compute total delta H and S for the entire sequence
    total_delta_h = sum(delta_h[dna_sequence[i:i + 2]] for i in range(len(dna_sequence) - 1))
    total_delta_s = sum(delta_s[dna_sequence[i:i + 2]] for i in range(len(dna_sequence) - 1))

    # calculate Tm using the nearest-neighbor thermodynamic model
    tm = (1000 * total_delta_h) / (total_delta_s + 1.987 * ln(50e-3)) - 273.15

    return round(tm, 2)


def lookup_by_ccds(ccds_id: str, df: pd.DataFrame, chrom: str = None) -> pd.DataFrame:
    """
    Filters a DataFrame for rows matching a specified CCDS ID and optionally a chromosome.

    @param ccds_id: The CCDS ID to filter by.
    @param df: The DataFrame to filter.
    @param chrom: Optional chromosome number to further filter the DataFrame.
    @return: A DataFrame filtered based on the specified criteria.
    """

    filtered_df = df[df['ccds_id'] == ccds_id]  # filter by CCDS ID

    if chrom:  # if chromosome specified
        filtered_df = filtered_df[filtered_df['chromosome'] == chrom]

    return filtered_df


def get_additional_sequence_attributes(
        headers: str, dna_sequence: str, attribute_df: pd.DataFrame, genetic_code: dict) -> namedtuple:
    """
    Compiles various attributes of a DNA sequence into a structured format.

    @param headers: Header information from the FASTA file.
    @param dna_sequence: The DNA sequence to analyze.
    @param attribute_df: DataFrame containing additional gene information.
    @param genetic_code: A dictionary mapping codons to amino acids.
    @return: A namedtuple containing various calculated and extracted sequence attributes.
    """

    FastaAttributes = namedtuple("FastaAttributes", [
        "headers", "dna_sequence", "dna_sequence_length", "protein_sequence",
        "protein_sequence_length", "gc_content_value",
        "tm_value", "amino_acid_content_value", "kmers_list",
        "additional_gene_info", "dna_composition", "proline_comp"
    ])

    # split header info to extract CCDS ID and chromosome
    parts = headers.split('|')
    ccds_id = parts[0]
    chrom = parts[1]
    chrom = chrom.replace('chr', '')

    gene_info = attribute_df.loc[attribute_df['ccds_id'] == ccds_id].iloc[0]

    # calculate sequence attributes
    dna_composition = get_sequence_composition(dna_sequence)
    protein_sequence = protein_translation(dna_sequence, genetic_code)
    protein_sequence_length = len(protein_sequence)
    dna_sequence_length = len(dna_sequence)
    gc_content_value = gc_content(dna_sequence)
    tm_value = get_tm_from_dna_sequence(dna_sequence)
    amino_acid_content_value = calculate_amino_acid_content(protein_sequence, 'P', 2)
    kmers_list = extract_kmers(dna_sequence, 3)
    protein_sequence = protein_translation(dna_sequence, genetic_code)
    proline_comp = calculate_amino_acid_content(protein_sequence, 'P', 2)

    # assemble attributes into namedtuple
    attributes = FastaAttributes(

        dna_composition=dna_composition,
        headers=headers,
        dna_sequence=dna_sequence,
        dna_sequence_length=dna_sequence_length,
        protein_sequence=protein_sequence,
        protein_sequence_length=protein_sequence_length,
        gc_content_value=gc_content_value,
        tm_value=tm_value,
        amino_acid_content_value=amino_acid_content_value,
        kmers_list=kmers_list,
        additional_gene_info=gene_info.to_dict(),
        proline_comp=proline_comp
    )

    return attributes
