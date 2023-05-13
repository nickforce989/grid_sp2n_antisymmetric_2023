#############################################################################
# Given the two files hmc_.out for the WF for b = 6.8 and 6.9, it will      #
# compute the Wilson Flow files with standard and clover plaquettes.        #
# NB: This will generate temporary files that will be eliminated.           #
#############################################################################

import re
import os


def compute_jackknife(data):
    """
    Compute the jackknife error given a list of data.
    """
    n = len(data)
    block_size = n // 10
    num_blocks = n // block_size
    averages = []
    for i in range(num_blocks):
        block_start = i * block_size
        block_end = block_start + block_size
        jackknife_data = data[:block_start] + data[block_end:]
        average = sum(jackknife_data) / (n - block_size)
        averages.append(average)
    mean = sum(data) / n
    variance = sum((avg - mean)**2 for avg in averages) * (num_blocks - 1) / num_blocks
    return (variance ** 0.5)


# Define the input file search pattern and output file names
input_file_pattern = r".*b69.*\.out"
output_file_name1 = "WF_b69_am-08_l8_clover.txt"
output_file_name2 = "WF_b69_am-08_l8.txt"

# Define the input file search pattern and output file names
input_file_pattern2 = r".*b68.*\.out"
output_file_name3 = "WF_b68_am-08_l8_clover.txt"
output_file_name4 = "WF_b68_am-08_l8.txt"

# Max Wilson Flow time
evolution_time = 450

###############################################################################
# Procedure for b = 6.9


# Find the input file that matches the pattern
input_file_name = None
for file_name in os.listdir("."):
    if re.match(input_file_pattern, file_name):
        input_file_name = file_name
        break

if input_file_name is None:
    print("Error: no input file found that matches the pattern.")
    exit()

# Read in the input file
with open(input_file_name, "r") as input_file:
    input_lines = input_file.readlines()

# Define the regular expression patterns to match the desired lines
pattern1 = r"\[WilsonFlow\] Energy density \(Clover plaq\) : (\d{1,3})"
pattern2 = r"\[WilsonFlow\] Energy density \(plaq\) : (\d{1,3})"

# Loop over the lines and extract the numbers for the first pattern
numbers1 = set()
for line in input_lines:
    match = re.search(pattern1, line)
    if match is not None:
        number = int(match.group(1))
        if number >= 1 and number <= evolution_time:
            numbers1.add(number)

# Loop over the numbers and write the corresponding lines to output files for the first pattern
for number in numbers1:
    output_file_name = f"output_clover_{number}.txt"
    with open(output_file_name, "w") as output_file:
        for line in input_lines:
            match = re.search(pattern1, line)
            if match is not None:
                this_number = int(match.group(1))
                if this_number == number:
                    output_file.write(line)

# Compute jackknife errors and write to output file for the first pattern
with open(output_file_name1, "w") as output_file:
    for i in range(1, evolution_time):
        input_file = f"output_clover_{i}.txt"
        if os.path.isfile(input_file):
            data = []
            with open(input_file) as f:
                line_count = 0
                for line in f:
                    line_count += 1
                    if line_count > 10:
                        numbers = line.strip().split()
                        if numbers:
                            data.append(float(numbers[-1]))
            if data:
                average = sum(data) / len(data)
                error = compute_jackknife(data)
                output_file.write(f"{average}\t{error}\n")

# Remove intermediate output files (for plaq)
for number in numbers1:
    output_file_name = f"output_clover_{number}.txt"
    os.remove(output_file_name)

# Loop over the lines and extract the numbers for the second pattern
numbers2 = set()
for line in input_lines:
    match = re.search(pattern2, line)
    if match is not None:
        number = int(match.group(1))
        if number >= 1 and number <= evolution_time:
            numbers2.add(number)

# Loop over the numbers and write the corresponding lines to output files for the second pattern
for number in numbers2:
    output_file_name = f"output_{number}.txt"
    with open(output_file_name, "w") as output_file:
        for line in input_lines:
            match = re.search(pattern2, line)
            if match is not None:
                this_number = int(match.group(1))
                if this_number == number:
                    output_file.write(line)

# Compute jackknife errors and write to output file (for plaq)
with open(output_file_name2, "w") as output_file_plaq:
    for i in range(1, evolution_time):
        input_file = f"output_{i}.txt"
        if os.path.isfile(input_file):
            data = []
            with open(input_file) as f:
                line_count = 0
                for line in f:
                    line_count += 1
                    if line_count > 10:
                        numbers = line.strip().split()
                        if numbers:
                            data.append(float(numbers[-1]))
            if data:
                average = sum(data) / len(data)
                error = compute_jackknife(data)
                output_file_plaq.write(f"{average}\t{error}\n")

# Remove intermediate output files (for plaq)
for number in numbers2:
    output_file_name2 = f"output_{number}.txt"
    os.remove(output_file_name2)
    
###########################################################################
#Redoing for the other beta, b = 6.8
# Find the input file that matches the pattern
input_file_name = None
for file_name in os.listdir("."):
    if re.match(input_file_pattern2, file_name):
        input_file_name = file_name
        break

if input_file_name is None:
    print("Error: no input file found that matches the pattern.")
    exit()

# Read in the input file
with open(input_file_name, "r") as input_file:
    input_lines = input_file.readlines()

# Define the regular expression patterns to match the desired lines
pattern1 = r"\[WilsonFlow\] Energy density \(Clover plaq\) : (\d{1,3})"
pattern2 = r"\[WilsonFlow\] Energy density \(plaq\) : (\d{1,3})"

# Loop over the lines and extract the numbers for the first pattern
numbers1 = set()
for line in input_lines:
    match = re.search(pattern1, line)
    if match is not None:
        number = int(match.group(1))
        if number >= 1 and number <= evolution_time:
            numbers1.add(number)

# Loop over the numbers and write the corresponding lines to output files for the first pattern
for number in numbers1:
    output_file_name = f"output_clover_{number}.txt"
    with open(output_file_name, "w") as output_file:
        for line in input_lines:
            match = re.search(pattern1, line)
            if match is not None:
                this_number = int(match.group(1))
                if this_number == number:
                    output_file.write(line)

# Compute jackknife errors and write to output file for the first pattern
with open(output_file_name3, "w") as output_file:
    for i in range(1, evolution_time):
        input_file = f"output_clover_{i}.txt"
        if os.path.isfile(input_file):
            data = []
            with open(input_file) as f:
                line_count = 0
                for line in f:
                    line_count += 1
                    if line_count > 10:
                        numbers = line.strip().split()
                        if numbers:
                            data.append(float(numbers[-1]))
            if data:
                average = sum(data) / len(data)
                error = compute_jackknife(data)
                output_file.write(f"{average}\t{error}\n")

# Remove intermediate output files (for plaq)
for number in numbers1:
    output_file_name = f"output_clover_{number}.txt"
    os.remove(output_file_name)

# Loop over the lines and extract the numbers for the second pattern
numbers2 = set()
for line in input_lines:
    match = re.search(pattern2, line)
    if match is not None:
        number = int(match.group(1))
        if number >= 1 and number <= evolution_time:
            numbers2.add(number)

# Loop over the numbers and write the corresponding lines to output files for the second pattern
for number in numbers2:
    output_file_name = f"output_{number}.txt"
    with open(output_file_name, "w") as output_file:
        for line in input_lines:
            match = re.search(pattern2, line)
            if match is not None:
                this_number = int(match.group(1))
                if this_number == number:
                    output_file.write(line)

# Compute jackknife errors and write to output file (for plaq)
with open(output_file_name4, "w") as output_file_plaq:
    for i in range(1, evolution_time):
        input_file = f"output_{i}.txt"
        if os.path.isfile(input_file):
            data = []
            with open(input_file) as f:
                line_count = 0
                for line in f:
                    line_count += 1
                    if line_count > 10:
                        numbers = line.strip().split()
                        if numbers:
                            data.append(float(numbers[-1]))
            if data:
                average = sum(data) / len(data)
                error = compute_jackknife(data)
                output_file_plaq.write(f"{average}\t{error}\n")

# Remove intermediate output files (for plaq)
for number in numbers2:
    output_file_name4 = f"output_{number}.txt"
    os.remove(output_file_name4)
