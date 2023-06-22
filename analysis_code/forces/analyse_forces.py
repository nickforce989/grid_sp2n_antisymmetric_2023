import sys
import re
import os
import glob

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

def compute_average(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    data = [float(line.strip()) for line in lines]

    average = sum(data) / len(data)

    return average

# Check if the output directory exists, if not, create it
output_directory = '../../data/force_contribution'
os.makedirs(output_directory, exist_ok=True)

# Process each file starting with 'hmc' in the directory '../../raw_data/force_contribution'
input_files = glob.glob('../../raw_data/force_contribution/hmc*')

forces_output_file = '../../data/force_contribution/forces.txt'

with open(forces_output_file, 'w') as f:
    for input_file in input_files:
        input_file_path = os.path.join(input_file)
        input_file_name = os.path.basename(input_file)
        m_value_match = re.search(r"_am([+-]?\d+(\.\d+)?p?\d*)", input_file_name)
        if m_value_match:
            m_value = m_value_match.group(1)
            if 'p' in m_value:
                m_value = m_value.replace('p', '.')

        m_value = "{:.1f}".format(float(m_value))

        search_pattern_fermionic = r'Hirep Force average:'
        output_file_fermionic = os.path.join(output_directory, 'tmp_fermionic_forces.out')

        # Check if the output file already exists and replace it
        if os.path.isfile(output_file_fermionic):
            os.remove(output_file_fermionic)

        extract_last_float(input_file_path, search_pattern_fermionic, output_file_fermionic)

        search_pattern_gauge = r'\[1\]\[0\] Force average:'
        output_file_gauge = os.path.join(output_directory, 'tmp_gauge_forces.out')

        # Check if the output file already exists and replace it
        if os.path.isfile(output_file_gauge):
            os.remove(output_file_gauge)

        extract_last_float(input_file_path, search_pattern_gauge, output_file_gauge)

        sum_lines(output_file_fermionic)

        # Remove the first 100 lines from 'fermionic_forces.out'
        with open(output_file_fermionic, 'r') as f_read:
            lines = f_read.readlines()

        with open(output_file_fermionic, 'w') as f_write:
            f_write.writelines(lines[100:])

        # Remove 800 lines from 'gauge_forces.out'
        with open(output_file_gauge, 'r') as f_read:
            lines = f_read.readlines()

        with open(output_file_gauge, 'w') as f_write:
            f_write.writelines(lines[800:])

        fermionic_average = compute_average(output_file_fermionic)
        gauge_average = compute_average(output_file_gauge)

        f.write(f"{m_value}\t{gauge_average:.5f}\t{fermionic_average:.5f}\n")

# Delete the files starting with 'tmp' in the '../../data/force_contribution' directory
tmp_files = glob.glob(os.path.join(output_directory, 'tmp*'))
for tmp_file in tmp_files:
    os.remove(tmp_file)


def compute_Rn_ratio(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Sort the lines based on the first column in ascending order
    sorted_lines = sorted(lines, key=lambda line: float(line.split()[0]))

    # Extract the first number in the first line, second column
    first_number = float(sorted_lines[0].split()[1])

    # Compute Rn ratio for each number in the second column
    Rn_ratios = [first_number / float(line.split()[1]) for line in sorted_lines]

    # Replace the numbers in the second and third columns with their Rn ratio
    modified_lines = [f'{line.split()[0]}\t{float(line.split()[1]) * Rn_ratios[i]}\t{float(line.split()[2]) * Rn_ratios[i]}' for i, line in enumerate(sorted_lines)]

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(modified_lines))

# Specify the file path
file_path = '../../data/force_contribution/forces.txt'  # Replace with the actual file path

# Call the function to sort lines, compute Rn ratio, and replace values
compute_Rn_ratio(file_path)
