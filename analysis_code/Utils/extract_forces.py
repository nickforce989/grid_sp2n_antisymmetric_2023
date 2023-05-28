import sys
import re
import os

def extract_last_float(input_file, search_pattern, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    values = []
    for line in lines:
        if re.search(search_pattern, line):
            floats = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            if floats:
                values.append(float(floats[-1]))

    if values:
        with open(output_file, 'w') as f:  # Replace the file if it exists
            for value in values:
                formatted_value = "{:.5f}".format(value)  # Format value to have 5 decimal places
                f.write(formatted_value + '\n')

def sum_lines(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    sum_values = []
    for i in range(0, len(lines), 2):
        line1 = float(lines[i].strip())
        line2 = float(lines[i+1].strip())
        sum_value = line1 + line2
        formatted_sum_value = "{:.5f}".format(sum_value)  # Format sum_value to have 5 decimal places
        sum_values.append(formatted_sum_value)

    with open(input_file, 'w') as f:
        for value in sum_values:
            f.write(value + '\n')

# Check if the input file path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the input file path.")
    sys.exit(1)

input_file = sys.argv[1]
input_file_path = f'../../raw_data/{input_file}'

search_pattern_fermionic = r'Hirep Force average:'
output_file_fermionic = '../../data/fermionic_forces.out'

# Check if the output file already exists and replace it
if os.path.isfile(output_file_fermionic):
    os.remove(output_file_fermionic)

extract_last_float(input_file_path, search_pattern_fermionic, output_file_fermionic)

search_pattern_gauge = r'\[1\]\[0\] Force average:'
output_file_gauge = '../../data/gauge_forces.out'

# Check if the output file already exists and replace it
if os.path.isfile(output_file_gauge):
    os.remove(output_file_gauge)

extract_last_float(input_file_path, search_pattern_gauge, output_file_gauge)

sum_lines(output_file_fermionic)

# Remove the first 100 lines from 'fermionic_forces.out'
with open(output_file_fermionic, 'r') as f:
    lines = f.readlines()

with open(output_file_fermionic, 'w') as f:
    f.writelines(lines[100:])

# Remove 800 lines from 'gauge_forces.out'
with open(output_file_gauge, 'r') as f:
    lines = f.readlines()

with open(output_file_gauge, 'w') as f:
    f.writelines(lines[800:])
