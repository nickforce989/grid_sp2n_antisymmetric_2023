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
                    first_column = "{:.2f}".format(0.02 + (i-1) * 0.01)  # Format the first column to two decimal places
                    output_file.write(f"{first_column}\t{average}\t0\t{error}\n")
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
                    first_column = "{:.2f}".format(0.02 + (i-1) * 0.01)  # Format the first column to two decimal places
                    output_file.write(f"{first_column}\t{average}\t0\t{error}\n")
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

# Create new file names with '_2' suffix
output_file_name1_2 = output_file_name1.replace(".txt", "_2.txt")
output_file_name2_2 = output_file_name2.replace(".txt", "_2.txt")
output_file_name3_2 = output_file_name3.replace(".txt", "_2.txt")
output_file_name4_2 = output_file_name4.replace(".txt", "_2.txt")

# Read the content of the original files
with open(output_file_name1, "r") as file1:
    content1 = file1.readlines()
with open(output_file_name2, "r") as file2:
    content2 = file2.readlines()
with open(output_file_name3, "r") as file3:
    content3 = file3.readlines()
with open(output_file_name4, "r") as file4:
    content4 = file4.readlines()

# Compute derivatives and propagate errors for the second column
def compute_derivative(data):
    x1 = data[0][0]
    y1 = data[0][1]
    x2 = data[1][0]
    y2 = data[1][1]
    derivative = (y2 - y1) / (x2 - x1)
    error1 = data[0][3]
    error2 = data[1][3]
    error = ((error1 ** 2) + (error2 ** 2)) ** 0.5
    return derivative * x1, error * x1

# Extract data from the original files and compute derivatives
data1 = [[float(value) for value in line.strip().split("\t")] for line in content1]
data2 = [[float(value) for value in line.strip().split("\t")] for line in content2]
data3 = [[float(value) for value in line.strip().split("\t")] for line in content3]
data4 = [[float(value) for value in line.strip().split("\t")] for line in content4]

derivatives1 = []
derivatives2 = []
derivatives3 = []
derivatives4 = []

# Compute derivatives with distance 1 for the first 30 values
for i in range(1, 31):
    derivative, error = compute_derivative(data1[i-1:i+1])
    derivatives1.append((data1[i][0], derivative, 0, error))

for i in range(1, 31):
    derivative, error = compute_derivative(data2[i-1:i+1])
    derivatives2.append((data2[i][0], derivative, 0, error))

for i in range(1, 31):
    derivative, error = compute_derivative(data3[i-1:i+1])
    derivatives3.append((data3[i][0], derivative, 0, error))

for i in range(1, 31):
    derivative, error = compute_derivative(data4[i-1:i+1])
    derivatives4.append((data4[i][0], derivative, 0, error))

# Compute derivatives with distance 10 for the remaining values
for i in range(30, len(data1)):
    derivative, error = compute_derivative(data1[i-10:i+1:10])
    derivatives1.append((data1[i][0], derivative, 0, error))

for i in range(30, len(data2)):
    derivative, error = compute_derivative(data2[i-10:i+1:10])
    derivatives2.append((data2[i][0], derivative, 0, error))

for i in range(30, len(data3)):
    derivative, error = compute_derivative(data3[i-10:i+1:10])
    derivatives3.append((data3[i][0], derivative, 0, error))

for i in range(30, len(data4)):
    derivative, error = compute_derivative(data4[i-10:i+1:10])
    derivatives4.append((data4[i][0], derivative, 0, error))

# Write the derivatives to the new files
with open(output_file_name1_2, "w") as file1_2:
    for line in derivatives1:
        file1_2.write(f"{line[0]:.2f}\t{line[1]}\t{line[2]}\t{line[3]}\n")

with open(output_file_name2_2, "w") as file2_2:
    for line in derivatives2:
        file2_2.write(f"{line[0]:.2f}\t{line[1]}\t{line[2]}\t{line[3]}\n")

with open(output_file_name3_2, "w") as file3_2:
    for line in derivatives3:
        file3_2.write(f"{line[0]:.2f}\t{line[1]}\t{line[2]}\t{line[3]}\n")

with open(output_file_name4_2, "w") as file4_2:
    for line in derivatives4:
        file4_2.write(f"{line[0]:.2f}\t{line[1]}\t{line[2]}\t{line[3]}\n")

# Print a message indicating the new files have been created
print(f"New files created with '_2' suffix: {output_file_name1_2}, {output_file_name2_2}, {output_file_name3_2}, {output_file_name4_2}")
