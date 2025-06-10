
# Assignment 2 README
### Author: Adam Alzaim

## Overview of the Assignment
This Assignement involved creating a python script to perform descriptive statistical analysis on numerical data extracted from a specified column of a tab-delimited file. It uses python's standard sys and math modules for its functionality. The script contains two primary functions: calculate_statistics and main.

## How to Run the Scripts
Running protein_to_daltons.py:

`
python stats_in_python.py <name of file> <column number>
`

example: `python stats_in_python.py data_file1.txt 1
`

## Documentation

`calculate_statistics(numbers)`: This function takes a list of numbers as input and calculates several descriptive statistics, including mean, variance, standard deviation, maximum, minimum, and median. It uses basic mathematical operations and the math.sqrt function from the math module for the standard deviation calculation.

`main():` This function serves as the entry point of the script. It processes command-line arguments to obtain the filename and the column index for data extraction. It reads a tab-delimited file, extracts numbers from the specified column, handles potential exceptions (like non-numeric values and file not found errors), and then calls calculate_statistics to compute the statistics. Finally, it prints the total count of lines processed, count of valid numbers, and the computed statistics

## Expected Output
Upon execution the script outputs error messages (if applicable), or the total count of lines processed, count of valid numbers, average, max value, min value, variance, standard deviation and median of the given list of numbers.