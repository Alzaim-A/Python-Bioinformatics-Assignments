"""Test Suite for seq_attribute_utils.py"""
import pytest
import pandas as pd
from sequence_attributes import *


# testing the calculate_amino_acid_content function
def test_calculate_amino_acid_content():
    protein_sequence = "APPP"
    amino_acid = "P"
    result = calculate_amino_acid_content(protein_sequence, amino_acid)
    assert result == 75.0


def test_calculate_amino_acid_content_empty_sequence():
    assert calculate_amino_acid_content("", "P") == 0.0


# testing the return_standard_genetic_code function
def test_return_standard_genetic_code():
    genetic_code = return_standard_genetic_code()
    assert genetic_code["UUU"] == "F"
    assert genetic_code["UGA"] is None


# testing the protein_translation function
def test_protein_translation():
    dna_sequence = "ATGGCC"
    genetic_code = return_standard_genetic_code()
    result = protein_translation(dna_sequence, genetic_code)
    assert result == "MA"


# testing the extract_kmers function
def test_extract_kmers():
    dna_sequence = "ATGGCC"
    k = 2
    result = extract_kmers(dna_sequence, k)
    expected_kmers = ["AT", "TG", "GG", "GC", "CC"]
    assert result == expected_kmers


# testing the get_sequence_composition function
def test_get_sequence_composition():
    dna_sequence = "ATGGCC"
    result = get_sequence_composition(dna_sequence)
    expected_composition = {"A": 1, "T": 1, "G": 2, "C": 2}
    assert result == expected_composition


# testing the gc_content function
def test_gc_content():
    dna_sequence = "ATGGCC"
    result = gc_content(dna_sequence)
    assert result == pytest.approx(66.67, 0.01)


# testing the get_tm_from_dna_sequence function
def test_get_tm_from_dna_sequence():
    dna = 'AGCT'
    assert get_tm_from_dna_sequence(dna) == 77.91, f"Tm of {dna} is not 77.91"


# testing the lookup_by_ccds function
def test_lookup_by_ccds():
    data = {
        "ccds_id": ["ID1", "ID2"],
        "chromosome": ["chr1", "chr2"],
        "gene_name": ["Gene1", "Gene2"]
    }
    df = pd.DataFrame(data)
    ccds_id = "ID1"
    result_df = lookup_by_ccds(ccds_id, df)
    assert not result_df.empty
    assert result_df.iloc[0]["gene_name"] == "Gene1"


# testing protein translation including handling of stop codons
def test_protein_translation_with_stop_codon():
    dna_sequence = "ATGTAA"
    genetic_code = return_standard_genetic_code()
    result = protein_translation(dna_sequence, genetic_code)
    assert result == "M", "Should translate until stop codon but not include it"


# testing protein translation with non-standard codons
def test_protein_translation_non_standard_codon():
    dna_sequence = "ATGXYZ"
    genetic_code = return_standard_genetic_code()
    result = protein_translation(dna_sequence, genetic_code)
    assert result == "M", "Should skip non-standard codons"


# testing k-mer extraction with k larger than the sequence length
def test_extract_kmers_large_k():
    dna_sequence = "ATGGCC"
    k = 10
    result = extract_kmers(dna_sequence, k)
    assert result == [], "Should return an empty list if k is larger than sequence length"


# testing nucleotide composition calculation excluding non-ATGC characters
def test_get_sequence_composition_non_atgc():
    dna_sequence = "ATGXCCT"
    result = get_sequence_composition(dna_sequence)
    assert result == {"A": 1, "T": 2, "G": 1, "C": 2}, "Non-ATGC characters should be ignored"


# testing GC content calculation for an empty sequence
def test_gc_content_empty_sequence():
    assert gc_content("") == 0.0, "GC content of an empty sequence should be 0.0"


# testing melting temperature calculation with invalid inputs
def test_get_tm_from_dna_sequence_invalid_input():
    assert get_tm_from_dna_sequence("") == 0.0, "Tm of an empty sequence should be 0.0"
    assert get_tm_from_dna_sequence("A") == 0.0, "Tm calculation requires at least 2 nucleotides"


# testing data filtering with a non-matching CCDS ID
def test_lookup_by_ccds_non_matching():
    data = {
        "ccds_id": ["ID1", "ID2"],
        "chromosome": ["chr1", "chr2"],
        "gene_name": ["Gene1", "Gene2"]
    }
    df = pd.DataFrame(data)
    result_df = lookup_by_ccds("NonExistentID", df)
    assert result_df.empty, "Should return an empty DataFrame for non-matching CCDS ID"


# testing for additional sequence attribute extraction
def test_get_additional_sequence_attributes_integration():
    headers = "ID1|chr1"
    dna_sequence = "ATGGCC"
    attribute_df = pd.DataFrame({
        "ccds_id": ["ID1"],
        "chromosome": ["chr1"],
        "gene_name": ["Gene1"]
    })
    genetic_code = return_standard_genetic_code()
    attributes = get_additional_sequence_attributes(headers, dna_sequence, attribute_df, genetic_code)
    assert attributes.dna_sequence == dna_sequence, "DNA sequence should match input"


# testing amino acid content calculation when the amino acid is absent from the sequence
def test_calculate_amino_acid_content_absent_amino_acid():
    assert calculate_amino_acid_content("AAAA", "P") == 0.0, "Should return 0.0 if the amino acid is not present"


# testing protein translation with an incomplete final codon
def test_protein_translation_incomplete_codon():
    dna_sequence = "ATGGCCA"  # Last 'A' does not form a complete codon
    genetic_code = return_standard_genetic_code()
    result = protein_translation(dna_sequence, genetic_code)
    assert result == "MA", "Incomplete codon at the end should be ignored"

