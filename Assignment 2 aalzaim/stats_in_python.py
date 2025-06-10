"""Importing sys and math modules"""
import sys
import math


def calculate_statistics(numbers):
    """Used to define variables used to calculate the various
    descriptive statistics for a list of number"""
    element_length = len(numbers)
    mean = sum(numbers) / element_length
    variance = sum((x - mean) ** 2 for x in numbers) / element_length
    std_dev = math.sqrt(variance)
    sorted_numbers = sorted(numbers)
    median = ((sorted_numbers[element_length // 2 - 1] + sorted_numbers[element_length // 2]) / 2
              if element_length % 2 == 0
              else sorted_numbers[element_length // 2])
    return mean, max(numbers), min(numbers), variance, std_dev, median
def main():
    """Main function that reads a tab-delimited file,
        extracts numbers from a specified column,
        calculates their descriptive statistics and prints the results."""
    if len(sys.argv) != 3:
        print("Usage: python3 stats_in_python.py <filename> <column>")
        sys.exit(1)

    filename = sys.argv[1]
    column_to_parse = int(sys.argv[2])

    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            numbers = []
            total_count = 0
            line_num = 0
            for line in infile:
                line_num += 1
                elements = line.split("\t")
                if len(elements) > column_to_parse:
                    total_count += 1
                try:
                    num = line.split("\t")[column_to_parse]
                    if num.strip().lower() != 'nan':
                        numbers.append(float(num))
                except ValueError:
                    print(f"Skipping line number {line_num} "
                          f": could not convert string to float: '{num.strip()}'")
                except IndexError:
                    print(f"Exiting: There is no valid 'list index' "
                          f"in column {column_to_parse} in line {line_num} in file: {filename}")
                    sys.exit(1)

            if not numbers:
                print(f"Error: There were no valid number(s) "
                      f"in column {column_to_parse} in file: {filename}")
                sys.exit(1)
            mean, maximum, minimum, variance, std_dev, median = calculate_statistics(numbers)

            print(f"    Column: {column_to_parse}\n\n")
            print(f"        Count     = {total_count:8.3f}")
            print(f"        ValidNum  = {len(numbers):8.3f}")
            print(f"        Average   = {mean:8.3f}")
            print(f"        Maximum   = {maximum:8.3f}")
            print(f"        Minimum   = {minimum:8.3f}")
            print(f"        Variance  = {variance:8.3f}")
            print(f"        Std Dev   = {std_dev:8.3f}")
            print(f"        Median    = {median:8.3f}")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        sys.exit(1)
if __name__ == "__main__":
    main()
