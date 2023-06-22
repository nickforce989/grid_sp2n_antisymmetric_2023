import re
import numpy as np

file_paths = ['../../raw_data/initial_tests/hmc_initialtests-step14.out', '../../raw_data/initial_tests/hmc_initialtests-step16.out', '../../raw_data/initial_tests/hmc_initialtests-step18.out', '../../raw_data/initial_tests/hmc_initialtests-step22.out', '../../raw_data/initial_tests/hmc_initialtests-step26.out']  # Replace with your input file paths

output_file = '../../data/initial_tests/dH_steps.txt'
block_fraction = 0.1
num_bootstrap_samples = 1000

with open(output_file, 'w') as file:
    for file_path in file_paths:
        dH_values = []
        with open(file_path, 'r') as input_file:
            lines = input_file.readlines()
            for line in lines:
                if 'exp(-dH) =' in line:
                    match = re.search(r'exp\(-dH\) = (-?\d+\.\d+)', line)
                    if match:
                        dH_values.append(-np.log(float(match.group(1))))

        dH_values = np.array(dH_values[400:])  # Exclude the first 200 values
        average = np.mean(dH_values)

        block_size = int(len(dH_values) * block_fraction)
        num_blocks = len(dH_values) // block_size

        # Calculate bootstrap errors
        errors = []
        for _ in range(num_bootstrap_samples):
            bootstrap_indices = np.random.choice(len(dH_values), size=len(dH_values), replace=True)
            bootstrap_data = dH_values[bootstrap_indices]
            bootstrap_mean = np.mean(bootstrap_data)
            errors.append(np.std(bootstrap_data) / np.sqrt(len(dH_values)))

        # Estimate error as the mean of bootstrap errors
        error = np.mean(errors)

        match = re.search(r'-step(\d+)\.out', file_path)
        if match:
            N = int(match.group(1))
            M = 1.0 / N
            file.write(f'{M} {average} 0.0 {error}\n')

# Read the data from the output file
data = np.genfromtxt(output_file)
