import re
import random
import numpy as np

file_paths = ['../../raw_data/reversibility/hmc_rev16.out',
              '../../raw_data/reversibility/hmc_rev17.out',
              '../../raw_data/reversibility/hmc_rev18.out',
              '../../raw_data/reversibility/hmc_rev19.out',
              '../../raw_data/reversibility/hmc_rev20.out',
              '../../raw_data/reversibility/hmc_rev21.out',
              '../../raw_data/reversibility/hmc_rev22.out',
              '../../raw_data/reversibility/hmc_rev23.out',
              '../../raw_data/reversibility/hmc_rev24.out',
              '../../raw_data/reversibility/hmc_rev25.out',
              '../../raw_data/reversibility/hmc_rev26.out']

def extract_float(line):
    match = re.search(r'dH =\s*(-?\d+(?:\.\d+)?(?:e-?\d+)?)', line)
    if match:
        return float(match.group(1))
    else:
        return None

def compute_bootstrap_error(data, num_samples=1000):
    n = len(data)
    errors = []
    if n < num_samples:
        num_samples = n
    for _ in range(num_samples):
        sample = random.choices(data[100:], k=n) if n >= num_samples else random.choices(data[100:], k=num_samples)
        errors.append(np.mean(sample))
    return np.std(errors)

results = []
for file_path in file_paths:
    file_name = file_path.split('/')[-1]
    rev_number = file_name.split('_rev')[-1].split('.')[0]
    rev_number = int(rev_number)

    with open(file_path, 'r') as file:
        lines = file.readlines()
        dH_lines = [line for line in lines if 'dH =' in line][100:]  # Exclude the first 100 lines
        floats = [np.absolute(extract_float(line)) for line in dH_lines if extract_float(line) is not None]

    average = np.mean(np.abs(floats))  # Compute the average of absolute values
    error = compute_bootstrap_error(floats, num_samples=min(len(floats), 1000))
    results.append((rev_number, average, error))

output_file = '../../data/reversibility/rev_test.txt'
with open(output_file, 'w') as file:
    for result in results:
        file.write(f'{result[0]} {result[1]} 0.0 {result[2]}\n')

