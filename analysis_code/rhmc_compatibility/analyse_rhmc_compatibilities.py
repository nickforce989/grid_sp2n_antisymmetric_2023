import os
import math
import random
import re
import numpy as np

def compute_average(data):
    return np.mean(data)

def jackknife(data, func):
    n = len(data)
    estimates = []
    for i in range(n):
        data_without_i = data[:i] + data[i+1:]
        estimate = func(data_without_i)
        estimates.append(estimate)
    return np.mean(estimates)

def bootstrap_t(data, num_samples, func):
    n = len(data)
    estimates = []
    for _ in range(num_samples):
        sample = [random.choice(data) for _ in range(n)]
        estimate = func(sample)
        estimates.append(estimate)
    estimate_mean = np.mean(estimates)
    estimate_std = 2.*np.std(estimates, ddof=1)
    t_statistic = (func(data) - estimate_mean) / (estimate_std * np.sqrt(1 + 1 / num_samples))
    return estimate_mean, t_statistic

def extract_float_from_line(line):
    elements = line.strip().split()
    return float(elements[-1])

def process_file(hmc_file_path, rhmc_file_path):
    hmc_lines = []
    rhmc_lines = []

    with open(hmc_file_path, 'r') as hmc_file:
        line_count = 0
        for line in hmc_file:
            if 'Plaquette' in line:
                line_count += 1
                if line_count <= 50:
                    continue
                hmc_lines.append(extract_float_from_line(line))

    with open(rhmc_file_path, 'r') as rhmc_file:
        line_count = 0
        for line in rhmc_file:
            if 'Plaquette' in line:
                line_count += 1
                if line_count <= 50:
                    continue
                rhmc_lines.append(extract_float_from_line(line))

    hmc_average = compute_average(hmc_lines)
    rhmc_average = compute_average(rhmc_lines)

    num_bootstraps = 100
    hmc_jackknife = jackknife(hmc_lines, compute_average)
    rhmc_jackknife = jackknife(rhmc_lines, compute_average)

    hmc_boot_mean, hmc_t_statistic = bootstrap_t(hmc_lines, num_bootstraps, compute_average)
    rhmc_boot_mean, rhmc_t_statistic = bootstrap_t(rhmc_lines, num_bootstraps, compute_average)

    hmc_error = abs(hmc_average - hmc_jackknife) + abs(hmc_average - hmc_boot_mean) / hmc_t_statistic
    rhmc_error = abs(rhmc_average - rhmc_jackknife) + abs(rhmc_average - rhmc_boot_mean) / rhmc_t_statistic

    return hmc_average, rhmc_average, hmc_error, rhmc_error

def main():
    directory = '../../raw_data/rhmc_compatibilities'
    file_prefixes = ['hmc_nf4_', 'rhmc_', '2p2_rhmc_']

    hmc_files = {}
    rhmc_files = {}
    rhmc_2p2_files = {}
    common_suffixes = set()

    for prefix in file_prefixes:
        for file_name in os.listdir(directory):
            if file_name.startswith(prefix):
                file_path = os.path.join(directory, file_name)
                suffix = file_name[len(prefix):]
                if prefix == 'hmc_nf4_':
                    hmc_files[suffix] = file_path
                elif prefix == 'rhmc_':
                    rhmc_files[suffix] = file_path
                elif prefix == '2p2_rhmc_':
                    rhmc_2p2_files[suffix] = file_path
                    common_suffix = re.search(r'_am-([0-9]+)\.out', file_name)
                    if common_suffix:
                        common_suffixes.add(common_suffix.group(1))

    output_file_1 = '../../data/rhmc_compatibilities/compatibilita_rhmc.txt'
    output_file_2 = '../../data/rhmc_compatibilities/compatibilita_rhmc_2p2.txt'

    with open(output_file_1, 'w') as file1, open(output_file_2, 'w') as file2:
        for suffix in rhmc_files:
            hmc_file_path = hmc_files.get(suffix)
            rhmc_file_path = rhmc_files[suffix]
            common_suffix = re.search(r'_am-([0-9]+)\.out', rhmc_file_path)
            if common_suffix:
                suffix_value = float(common_suffix.group(1)) / 10.0
                hmc_average, rhmc_average, hmc_error, rhmc_error = process_file(hmc_file_path, rhmc_file_path)
                difference = hmc_average - rhmc_average
                sum_of_errors = math.sqrt(hmc_error**2 + rhmc_error**2)
                file1.write(f"-{suffix_value}\t{str(difference).ljust(15)}\t0.0\t{str(sum_of_errors).ljust(15)}\n")

        for suffix in rhmc_2p2_files:
            hmc_file_path = hmc_files.get(suffix)
            rhmc_file_path = rhmc_2p2_files[suffix]
            common_suffix = re.search(r'_am-([0-9]+)\.out', rhmc_file_path)
            if common_suffix:
                suffix_value = float(common_suffix.group(1)) / 10.0
                hmc_average, rhmc_average, hmc_error, rhmc_error = process_file(hmc_file_path, rhmc_file_path)
                difference = hmc_average - rhmc_average
                sum_of_errors = math.sqrt(hmc_error**2 + rhmc_error**2)
                file2.write(f"-{suffix_value}\t{str(difference).ljust(15)}\t0.0\t{str(sum_of_errors).ljust(15)}\n")

if __name__ == '__main__':
    main()
