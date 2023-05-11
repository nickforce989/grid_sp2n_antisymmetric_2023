#################################################################################
# You expect to have a directory with all the values of mass for one fixed beta #
# This will find all the plaquette values for that curve with jackknife errors. #
# You expect to have a directory of files like 'hmc_7516154-b62_am-14.out'      #
# NB: You can fix the thermalization of values with therm_num.                  #
#################################################################################

import re
import numpy as np
import os

# Get list of all files starting with 'hmc_' in the same directory
dir_path = os.path.dirname(os.path.realpath(__file__))
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.startswith("hmc_")]

# Thermalisation of plaquette values 
therm_num = 300

# Initialize a dictionary to store the results
results = {}

# Iterate over each file
for filename in files:
    # Use grep command to select relevant lines and write to temporary file
    os.system(f"grep 'Plaquette' {filename} | awk '{{print $NF}}' > plaquette_lines.txt")

    # Read in the temporary file
    with open("plaquette_lines.txt", "r") as f:
        lines = f.readlines()

    # Extract plaquette values and their line numbers
    plaquette_values = [float(line.strip()) for line in lines]

    # Select the last plaquette value for each line
    last_plaquettes = [plaquette_values[i] for i in range(len(plaquette_values)-1) if i+1 not in plaquette_values[:i]]

    # Eliminate first 150 values
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
    integer_val = os.popen(f"basename {filename} | sed 's/.*-\\([0-9]\\+\\)\\.out/\\1/'").read().strip()
    if not integer_val.isdigit():
        print(f"Error: No integer value found in filename {filename}")
        continue

    # Insert decimal point after first digit
    float_val = integer_val[0] + "." + integer_val[1:]

    # Add results to the dictionary
    results[float_val] = (bin_avg, bin_err)

    # Delete the temporary file
    os.remove("plaquette_lines.txt")

# Write the results to the output file in ascending order based on the first column
with open("jackknife_plaquettes.txt", "w") as f:
    for key in sorted(results.keys(), reverse=True):
        bin_avg, bin_err = results[key]
        f.write(f"{key} {bin_avg} {bin_err}\n")


