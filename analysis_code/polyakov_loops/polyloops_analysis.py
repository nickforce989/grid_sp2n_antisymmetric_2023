import subprocess
import re
import os

# Input file paths
input_paths = [
    '../../raw_data/polyakov_loops/hmc_l2.out',
    '../../raw_data/polyakov_loops/hmc_l4.out',
    '../../raw_data/polyakov_loops/hmc_l12.out',
    '../../raw_data/polyakov_loops/hmc_l20.out'
]

# Output file paths
tmp_paths = [
    '../../data/polyakov_loops/tmp_l2_polyloop.txt',
    '../../data/polyakov_loops/tmp_l4_polyloop.txt',
    '../../data/polyakov_loops/tmp_l12_polyloop.txt',
    '../../data/polyakov_loops/tmp_l20_polyloop.txt'
]

# Output file paths
output_paths = [
    '../../data/polyakov_loops/output_l2_polyloop.txt',
    '../../data/polyakov_loops/output_l4_polyloop.txt',
    '../../data/polyakov_loops/output_l12_polyloop.txt',
    '../../data/polyakov_loops/output_l20_polyloop.txt'
]

# Process each input file
for input_path, output_path in zip(input_paths, tmp_paths):
    # Use grep command to select lines containing 'Polyakov Loop' and save to output file
    grep_command = f"grep 'Polyakov Loop' {input_path} > {output_path}"
    subprocess.run(grep_command, shell=True)

for i in range(4):
    # Regular expression pattern to extract the number
    pattern = r'\(([+-]?\d+(\.\d+)?(?:[eE][+-]?\d+)?)'

    # Open input and output files
    with open(tmp_paths[i], 'r') as f_input, open(output_paths[i], 'w') as f_output:
        # Process each line in the input file, skipping the first 5000 lines
        lines = f_input.readlines()[5000:]
        for line in lines:
            # Extract the number using the regular expression pattern
            match = re.search(pattern, line)
            if match:
                number = match.group(1)
                # Write the number to the output file
                f_output.write(number + '\n')

# Delete the files in tmp_paths
for file_path in tmp_paths:
    os.remove(file_path)
