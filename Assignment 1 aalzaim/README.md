
# Assignment 1 README
### Author: Adam Alzaim

## Overview of the Assignment
This assignment is made up of three python scripts, each designed to run specific bioinformatics calculations:

1. protein_to_daltons.py - Computes the average weight of this protein sequence in kilodaltons.

2. input_to_amino_acids.py - Takes the length of a DNA sequence and calculates the length of it's decoded protien sequence, then calculates the average weight.

3. input_to_protocol.py - Assists in solution preparation by determining the volumes of NaCl and MgCl2 based on specified concentrations.

## How to Run the Scripts
Running protein_to_daltons.py:
`
python protein_to_daltons.py
`

Running input_to_amino_acids.py:
`
python input_to_amino_acids.py
`

Running input_to_protocol.py:
`
python input_to_protocol.py
`
## Documentation
1. protein_to_daltons.py - Calculates the molecular weight of a predefined protein sequence by multiplying the length of the sequence with the average molecular weight per amino acid (110 Daltons). 

2. input_to_amino_acids.py - Asks for user input to name a DNA sequence and define its length. Validates that the sequence length is divisible by 3 (a requirement for amino acid chains). Calculates the corresponding amino acid chain length and its estimated molecular weight. 

3. input_to_protocol.py - Takes user input for the final volume of a solution, and the stock and final concentrations of NaCl and MgCl2. Uses the calculate_volume function to determine the necessary volume of each component to achieve the desired final concentration. 

## Expected Output
1. protein_to_daltons.py - Outputs the length and molecular weight (in kilodaltons) of the predefined protein sequence.

2. input_to_amino_acids.py- Outputs the length of the amino acid chain derived from the input DNA sequence and its estimated molecular weight.

3. input_to_protocol.py - Provides the volumes (in ml) of NaCl, MgCl2, and water to add to achieve the specified final solution.