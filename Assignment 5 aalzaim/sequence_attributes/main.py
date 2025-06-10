"""main.py
Orchestrates gene data processing and FASTA sequence analysis,
outputting results to Excel and TSV formats. Utilizes CCDS and
Ensembl gene data merging, FASTA sequence retrieval, and
sequence attribute compilation.
Usage:
python main.py --infile_ccds_fasta <FASTA file>
--infile_ccds_attributes <CCDS attributes>
--infile_ensembl_gene <Ensembl gene data>
--excel_outfile <output Excel file>
"""
import argparse
import sys
import pandas as pd
from sequence_attributes import *


def get_cli_args():
    """
        Parses and returns command-line arguments for
        processing gene data and FASTA sequences.

        @return: The parsed arguments from the command line.
        """

    parser = argparse.ArgumentParser(description="Process CCDS and Ensembl "
                                                 "gene data along with FASTA sequences.")
    parser.add_argument("--infile_ccds_fasta", required=True, help="Path to the CCDS FASTA file.")
    parser.add_argument("--infile_ccds_attributes",
                        required=True, help="Path to the CCDS attributes file.")
    parser.add_argument("--infile_ensembl_gene",
                        required=True, help="Path to the Ensembl gene data file.")
    parser.add_argument("--excel_outfile",
                        required=True, help="Path for the output Excel file.")
    return parser.parse_args()


def main():
    """"Main Business Logic

        Main function to orchestrate the processing of CCDS and Ensembl gene data along with FASTA sequences,
        and output the results to an Excel file.

        This function does the following:
        - Parses command-line arguments for input and output files.
        - Loads and processes CCDS attributes and Ensembl gene data from provided input files.
        - Merges CCDS and Ensembl data frames on the gene column.
        - Retrieves FASTA sequences and headers using `get_fasta_lists`.
        - Extracts additional sequence attributes for each FASTA sequence.
        - Compiles a summary DataFrame of the top and bottom 10 sequences based on proline composition.
        - Saves the summary to a TSV file and detailed attributes to an Excel file.
        """
    args = get_cli_args()
    # load and preprocess ccds and ensembl data
    ccds_attributes_df = pd.read_csv(args.infile_ccds_attributes, sep='\t')
    ccds_attributes_df.rename(columns={
        'gene_id': 'refseq_gene_id', '#chromosome': 'chrom'}, inplace=True)

    ensembl_gene_df = pd.read_csv(args.infile_ensembl_gene, sep='\t')
    ensembl_gene_df.rename(
        columns={
            'ID': 'ensembl_gene_id', 'Canonical Transcript': 'ensembl_canonical_transcript_id',
            'Gene': 'gene', 'Description': 'description', 'Biotype': 'biotype'}, inplace=True)

    # merge ccds and ensembl data on gene names
    merged_df = pd.merge(ccds_attributes_df, ensembl_gene_df, on='gene', how='left')

    # retrieve and process fasta sequences
    seq_header, sequence = get_fasta_lists(args.infile_ccds_fasta)
    all_data = []
    for i, (header, dna_sequence) in enumerate(zip(seq_header, sequence)):
        attributes = get_additional_sequence_attributes(header,
                                                        dna_sequence, merged_df, return_standard_genetic_code())
        all_data.append(attributes._asdict())
        if i == sys.maxsize:  # sys.maxsize:   50:
            break  # break for dev purposes

    # compile and format data for tsv
    final_df_tsv = pd.DataFrame(all_data)
    additional_info_df = final_df_tsv['additional_gene_info'].apply(pd.Series)
    final_df_tsv = pd.concat([final_df_tsv.drop(
        'additional_gene_info', axis=1), additional_info_df], axis=1)
    final_df_tsv.sort_values(
        by=['proline_comp', 'protein_sequence_length'], ascending=[False, False], inplace=True)

    columns_for_tsv = [
        'ccds_id', 'refseq_gene_id', 'biotype', 'ensembl_gene_id',
        'description', 'protein_sequence_length', 'proline_comp']
    filtered_df_tsv = final_df_tsv[columns_for_tsv]
    top_10 = filtered_df_tsv.head(10)
    bottom_10 = filtered_df_tsv.tail(10)
    summary_df = pd.concat([top_10, bottom_10])

    tsv_filename = args.excel_outfile.replace('.xlsx', '.tsv')
    summary_df.to_csv(tsv_filename, sep='\t', index=False)

    # compile and format data for xlsx
    final_df_xlsx = pd.DataFrame(all_data)
    additional_info_df = final_df_xlsx['additional_gene_info'].apply(pd.Series)
    final_df_xlsx = pd.concat([final_df_xlsx.drop(
        'additional_gene_info', axis=1), additional_info_df], axis=1)
    final_df_xlsx.sort_values(
        by=['proline_comp', 'protein_sequence_length'], ascending=[False, False], inplace=True)

    columns_for_xlsx = ['refseq_gene_id', 'chrom', 'ensembl_gene_id',
                        'ensembl_canonical_transcript_id', 'gene',
                        'description', 'biotype', 'dna_sequence',
                        'dna_sequence_length', 'protein_sequence',
                        'protein_sequence_length', 'gc_content_value',
                        'tm_value', 'amino_acid_content_value',
                        'kmers_list', 'dna_composition', 'proline_comp']

    filtered_df_xlsx = final_df_xlsx[columns_for_xlsx]
    filtered_df_xlsx.to_excel(args.excel_outfile, index=False)


if __name__ == "__main__":
    main()
