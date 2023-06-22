import os

def extract_lines_with_plaquette(file_path):
    directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)


    # Extract the suffix after 'hmc_'
    suffix = file_name.split('hmc_')[1]

    temp_directory = os.path.join(os.path.dirname(directory), '../data/susceptibility/')
    temp_file_name = 'tmp_' + suffix
    temp_file_path = os.path.join(temp_directory, temp_file_name)

    with open(file_path, 'r') as file:
        lines_with_plaquette = [line for line in file if 'Plaquette' in line]

    with open(temp_file_path, 'w') as temp_file:
        temp_file.writelines(lines_with_plaquette)

    print(f"Filtered lines with 'Plaquette' saved to: {temp_file_path}")

# Specify the directory paths
input_directory = '../../raw_data/susceptibility/'
output_directory = '../../data/susceptibility/'

# Get all file names in the input directory
file_names = os.listdir(input_directory)

# Filter files to process only those starting with 'hmc_'
file_paths = [os.path.join(input_directory, file_name) for file_name in file_names if file_name.startswith('hmc_')]

for path in file_paths:
    extract_lines_with_plaquette(path)


import numpy as np

def extract_last_float(file_path):
    file_name = os.path.basename(file_path)
    output_file_path = os.path.splitext(file_path)[0] + '-refined.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    n_plq = len(lines)
    plq = np.empty(n_plq, dtype=np.float64)

    for i in range(n_plq):
        line = lines[i]
        plq_value = line.split(' ')[-1].strip()
        plq[i] = float(plq_value)

    with open(output_file_path, 'w') as output_file:
        for i in range(n_plq):
            output_file.write(str(plq[i]) + '\n')

    print(f"Last floating numbers extracted and saved in: {output_file_path}")

def remove_first_lines(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        file.writelines(lines[num_lines:])

    print(f"First {num_lines} lines removed from: {file_path}")

# Specify the directory paths
input_directory2 = '../../data/susceptibility/'

# Get all file names in the input directory
file_names = os.listdir(input_directory2)

# Filter files to process only those starting with 'tmp_hmc_'
file_paths = [os.path.join(input_directory2, file_name) for file_name in file_names if file_name.startswith('tmp_')]

# Extract the last floating number from each line in the temporary files
for path in file_paths:
    extract_last_float(path)

# Calculate therm as 60% of the number of lines in each file
for path in file_paths:
    with open(path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        therm = int(0.6 * num_lines)
    remove_first_lines(os.path.splitext(path)[0]+'-refined.txt', therm)


# Specify the directory path
directory_path = '../../data/susceptibility/'

# Get all file names in the directory
file_names = os.listdir(directory_path)

# Filter files to process only those starting with 'tmp' and not containing '-refined.txt' in their names
files_to_delete = [file_name for file_name in file_names if file_name.startswith('tmp') and '-refined.txt' not in file_name]

# Delete the files
for file_name in files_to_delete:
    file_path = os.path.join(directory_path, file_name)
    os.remove(file_path)
    print(f"File deleted: {file_path}")


import os
import re
import numpy as np

def extract_number_from_filename(filename):
    match = re.search(r'am-(\d+)', filename)
    if match:
        number = match.group(1)
        formatted_number = f"-{int(number[:1])}.{number[1:]}"
        return formatted_number
    else:
        return ""

def compute_susceptibility(data, factor):
    # Compute susceptibility from data
    mean = np.mean(data)
    mean_of_squares = np.mean(data**2)
    susceptibility = mean_of_squares - mean**2
    return susceptibility * factor

def jackknife(data, factor):
    n = len(data)
    jackknife_estimates = []
    for i in range(n):
        data_i = np.concatenate((data[:i], data[i+1:]))  # Leave out one data point
        susceptibility_i = compute_susceptibility(data_i, factor)
        jackknife_estimates.append(susceptibility_i)
    jackknife_mean = np.mean(jackknife_estimates)
    jackknife_error = np.sqrt((n-1)/n * np.sum((jackknife_estimates - jackknife_mean)**2))

    jackknife_error *= 1.5

    return jackknife_mean, jackknife_error

def process_files(file_prefix, output_file):
    directory = '../../data/susceptibility/'
    files = [f for f in os.listdir(directory) if f.startswith(file_prefix)]

    data_output = []
    for file in files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as data_file:
            data = np.loadtxt(data_file)  # Load data from file
            block_size = len(data) // 10  # Compute block size

            # Extract number from file name
            number = extract_number_from_filename(file)

            # Compute multiplication factor based on 'l16' or 'l8'
            if 'l16' in file:
                factor = 16**4
            elif 'l8' in file:
                factor = 8**4
            else:
                factor = 1

            # Compute susceptibility and jackknife error
            susceptibility = compute_susceptibility(data, factor)
            jackknife_mean, jackknife_error = jackknife(data, factor)

            data_output.append([number, susceptibility, 0.0, jackknife_error])

    # Sort the data based on the extracted numbers
    sorted_data_output = sorted(data_output, key=lambda x: float(x[0]))

    # Write results to output file
    with open(output_file, 'w') as f:
        for row in sorted_data_output:
            f.write("\t".join(map(str, row)) + "\n")

# Process files starting with 'tmp_l16_b62'
process_files('tmp_l16_b62', '../../data/susceptibility/susceptibility_b62_nf4_vol16.txt')

# Process files starting with 'tmp_l16_b65'
process_files('tmp_l16_b65', '../../data/susceptibility/susceptibility_b65_nf4_vol16.txt')

# Process files starting with 'tmp_l8_b62'
process_files('tmp_l8_b62', '../../data/susceptibility/susceptibility_b62_nf4_vol8.txt')

# Process files starting with 'tmp_l8_b65'
process_files('tmp_l8_b65', '../../data/susceptibility/susceptibility_b65_nf4_vol8.txt')


import os

# Specify the directory path
directory_path = '../../data/susceptibility/'

# Get all file names in the directory
file_names = os.listdir(directory_path)

# Filter files to process only those starting with 'tmp'
files_to_delete = [file_name for file_name in file_names if file_name.startswith('tmp')]

# Delete the files
for file_name in files_to_delete:
    file_path = os.path.join(directory_path, file_name)
    os.remove(file_path)
    print(f"File deleted: {file_path}")
