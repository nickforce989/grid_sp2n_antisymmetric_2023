import re
import os
import random

def compute_bootstrap(data):
    """
    Compute the bootstrap error given a list of data.
    """
    n = len(data)
    averages = []
    num_samples = 1000
    for i in range(num_samples):
        random.seed(42)  # Fix the seed to 42
        sample = [random.choice(data) for _ in range(n)]
        average = sum(sample) / n
        averages.append(average)
    mean = sum(data) / n
    variance = sum((avg - mean) ** 2 for avg in averages) / (num_samples - 1)
    return (variance ** 0.5)


def process_input_files(input_file_pattern, output_file_clover, output_file_plaq):
    # Find the input file that matches the pattern
    input_file_name = input_file_pattern

    if input_file_name is None:
        print("Error: no input file found that matches the pattern.")
        return

    # Read in the input file
    with open(input_file_name, "r") as input_file:
        input_lines = input_file.readlines()

    # Define the regular expression patterns to match the desired lines
    pattern1 = r"\[WilsonFlow\] Energy density \(Clover plaq\) : (\d{1,3})"
    pattern2 = r"\[WilsonFlow\] Energy density \(plaq\) : (\d{1,3})"

    numbers1 = set()
    numbers2 = set()

    # Loop over the lines and extract the numbers
    for line in input_lines:
        match1 = re.search(pattern1, line)
        match2 = re.search(pattern2, line)
        if match1:
            number = int(match1.group(1))
            if 1 <= number <= evolution_time:
                numbers1.add(number)
        elif match2:
            number = int(match2.group(1))
            if 1 <= number <= evolution_time:
                numbers2.add(number)

    # Process output files for pattern 1 (Clover plaq)
    for number in numbers1:
        output_file_name = f"../../data/output_clover_{number}.txt"
        with open(output_file_name, "w") as output_file:
            for line in input_lines:
                match = re.search(pattern1, line)
                if match and int(match.group(1)) == number:
                    output_file.write(line)

    # Compute bootstrap errors and write to output file for pattern 1 (Clover plaq)
    with open(output_file_clover, "w") as output_file:
        for i in range(1, evolution_time + 1):
            input_file = f"../../data/output_clover_{i}.txt"
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
                    error = compute_bootstrap(data)
                    output_file.write(f"{average}\t{error}\n")
                os.remove(input_file)

    # Process output files for pattern 2 (plaq)
    for number in numbers2:
        output_file_name = f"../../data/output_{number}.txt"
        with open(output_file_name, "w") as output_file:
            for line in input_lines:
                match = re.search(pattern2, line)
                if match and int(match.group(1)) == number:
                    output_file.write(line)

    # Compute bootstrap errors and write to output file for pattern 2 (plaq)
    with open(output_file_plaq, "w") as output_file:
        for i in range(1, evolution_time + 1):
            input_file = f"../../data/output_{i}.txt"
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
                    error = compute_bootstrap(data)
                    output_file.write(f"{average}\t{error}\n")
                os.remove(input_file)

# Define the input file search patterns and output file names
directory = "../../raw_data/"
input_files = [f for f in os.listdir(directory) if f.endswith(".out") and "b69" in f] 
output_file_name1 = "../../data/WF_b69_am-08_l8_clover.txt"
output_file_name2 = "../../data/WF_b69_am-08_l8.txt"

input_files2 = [f for f in os.listdir(directory) if f.endswith(".out") and "b68" in f] 
output_file_name3 = "../../data/WF_b68_am-08_l8_clover.txt"
output_file_name4 = "../../data/WF_b68_am-08_l8.txt"

# Max Wilson Flow time
evolution_time = 450

# Process input files for b = 6.9
process_input_files("../../raw_data/"+input_files[0], output_file_name1, output_file_name2)

# Process input files for b = 6.8
process_input_files("../../raw_data/"+input_files2[0], output_file_name3, output_file_name4)
