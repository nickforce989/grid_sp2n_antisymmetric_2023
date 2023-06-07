import re
import numpy as np
import os
import glob
import sys

# Get beta values from command line arguments
beta_values = sorted([float(arg) for arg in sys.argv[1:-2]])

# Get therm_num from command line argument
therm_num = int(sys.argv[-2])

flavours = int(sys.argv[-1])

# Initialize a dictionary to store the results
results = {}

# Iterate over each beta value
for n, beta in enumerate(beta_values, start=1):
    # Initialize a dictionary to store the results for this beta value
    results = {}
    # Get list of all files with names matching the pattern 'hmc_nf{flavours}_*_b{int(beta*10)}-*.out' in the same directory
    pattern = f"../../raw_data/hmc_nf{flavours}_*_b{int(beta*10)}-*.out"
    files = glob.glob(pattern)
    files = [f for f in files if os.path.isfile(f)]

    # Check if any files were found
    if not files:
        print(f"No files found for beta = {beta} and flavours = {flavours}")
        continue

    # Iterate over each file
    for filename in files:
        # Use grep command to select relevant lines and write to temporary file
        os.system(f"grep 'Plaquette' {filename} | awk '{{print $NF}}' > ../../data2/plaquette_lines.txt")

        # Read in the temporary file
        with open("../../data/plaquette_lines.txt", "r") as f:
            lines = f.readlines()

        # Extract plaquette values and their line numbers
        plaquette_values = [float(line.strip()) for line in lines]

        # Select the last plaquette value for each line
        last_plaquettes = [plaquette_values[i] for i in range(len(plaquette_values)-1) if i+1 not in plaquette_values[:i]]

        # Eliminate first therm_num values
        last_plaquettes = last_plaquettes[therm_num:]

        # Compute bin size and number of bins
        bin_size = int(len(last_plaquettes) / 10)
        num_bins = int(len(last_plaquettes) / bin_size)

        # Compute jackknife averages and errors
        bin_avgs = []
        for i in range(num_bins):
            bin_start = i * bin_size
            bin_end = bin_start + bin_size
            bin_data = last_plaquettes[bin_start:bin_end]
            jackknife_data = np.delete(last_plaquettes, range(bin_start, bin_end))
            bin_avg = np.mean(jackknife_data)
            bin_avgs.append(bin_avg)

        bin_avg = np.mean(bin_avgs)
        bin_err = np.sqrt((num_bins - 1) / num_bins * np.sum((bin_avgs - bin_avg) ** 2))

        # Get integer value from filename using bash commands
        integer_val = os.popen(f"basename {filename} | sed 's/.*-am\\([0-9]\\+\\)\\.out/\\1/'").read().strip()
        if not integer_val.isdigit():
            print(f"Error: No integer value found in filename {filename}")
            continue

        # Insert decimal point after first digit
        float_val = integer_val[0] + "." + integer_val[1:]

        # Add results to the dictionary
        results[float_val] = (bin_avg, bin_err)

        # Delete the temporary file
        os.remove("../../data/plaquette_lines.txt")

    # Write the results to the output file in ascending order based on the first column
    with open(f"../../data/bulktrans_nf{flavours}_sp4_2AS_{n}.dat", "w") as f:
        for key in sorted(results.keys(), reverse=True):
            bin_avg, bin_err = results[key]
            f.write(f"-{key} {bin_avg} 0.0 {bin_err}\n")
