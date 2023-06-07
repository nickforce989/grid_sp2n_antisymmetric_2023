import re
import math
import random

def compute_average(numbers):
    return sum(numbers) / len(numbers)

def compute_bootstrap_error(numbers, num_samples):
    n = len(numbers)
    averages = []
    for _ in range(num_samples):
        sample = [random.choice(numbers) for _ in range(n)]
        averages.append(compute_average(sample))
    mean = compute_average(numbers)
    error = math.sqrt(sum([(x - mean) ** 2 for x in averages]) / num_samples)
    return error

def process_file(file_path):
    lines_with_exp_dH = []
    exp_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.search(r'exp\(-dH\) = (\d+\.\d+)', line)
            if matches:
                number = float(matches.group(1))
                exp_numbers.append(number)
                lines_with_exp_dH.append(line.rstrip('\n'))
    num_samples = 1000  # Adjust the number of bootstrap samples as needed
    average = compute_average(exp_numbers)
    bootstrap_error = compute_bootstrap_error(exp_numbers, num_samples)
    return average, bootstrap_error

input_files = ['../../raw_data/hmc_7534350-step14.out', '../../raw_data/hmc_7534348-step16.out', '../../raw_data/hmc_7534347-step18.out', '../../raw_data/hmc_7534346-step22.out', '../../raw_data/hmc_7534360-step26.out']  # Replace with your input file paths
output_file = '../../data/expdh.txt'  # Replace with the desired output file path

output_lines = []
for file_path in input_files:
    match = re.search(r'step(\d+)\.out$', file_path)
    if match:
        step_number = match.group(1)
        inverse_step_number = 1 / int(step_number)
        average, bootstrap_error = process_file(file_path)
        output_line = f"{inverse_step_number} {average} 0.0 {bootstrap_error}"
        output_lines.append(output_line)

with open(output_file, 'w') as file:
    file.write('\n'.join(output_lines))
