import re
import numpy as np

file_paths = ['../../raw_data/hmc_7534350-step14.out', '../../raw_data/hmc_7534348-step16.out', '../../raw_data/hmc_7534347-step18.out', '../../raw_data/hmc_7534346-step22.out', '../../raw_data/hmc_7534360-step26.out']  # Replace with your input file paths

output_file = '../../data/pacc_steps.txt'
block_fraction = 0.1
num_bootstrap_samples = 1000

with open(output_file, 'w') as file:
    for file_path in file_paths:
        dH_values = []
        pacc_values = []
        with open(file_path, 'r') as input_file:
            lines = input_file.readlines()
            for line in lines:
                if 'Probability =' in line:
                    match2 = re.search(r'Probability = (1|(-?\d+\.\d+))', line)
                    if match2:
                        pacc_values.append(float(match2.group(1)))
                if 'exp(-dH) =' in line:
                    match = re.search(r'exp\(-dH\) = (-?\d+\.\d+)', line)
                    if match:
                        dH_values.append(-np.log(float(match.group(1))))

        dH_values = np.array(dH_values[400:])  # Exclude the first 200 values
        average = np.mean(dH_values)
        pacc_values = np.array(pacc_values[400:])
        average2 = np.mean(pacc_values)

        block_size = int(len(dH_values) * block_fraction)
        num_blocks = len(dH_values) // block_size
        block_size2 = int(len(pacc_values) * block_fraction)
        num_blocks2 = len(pacc_values) // block_size

        # Calculate bootstrap errors
        errors = []
        errors2 = []
        for _ in range(num_bootstrap_samples):
            bootstrap_indices = np.random.choice(len(dH_values), size=len(dH_values), replace=True)
            bootstrap_data = dH_values[bootstrap_indices]
            bootstrap_mean = np.mean(bootstrap_data)
            errors.append(np.std(bootstrap_data) / np.sqrt(len(dH_values)))
            bootstrap_indices2 = np.random.choice(len(pacc_values), size=len(pacc_values), replace=True)
            bootstrap_data2 = pacc_values[bootstrap_indices2]
            bootstrap_mean2 = np.mean(bootstrap_data2)
            errors2.append(np.std(bootstrap_data2) / np.sqrt(len(pacc_values)))

        # Estimate error as the mean of bootstrap errors
        error = np.mean(errors)
        error2 = np.mean(errors2)

        match = re.search(r'-step(\d+)\.out', file_path)
        if match:
            file.write(f'{average} {average2} {error} {error2}\n')

# Read the data from the output file
data = np.genfromtxt(output_file)
