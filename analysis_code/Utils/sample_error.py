import os
import math

def compute_sample_error(data):
    """
    Compute the sample error given a list of data.
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / (n - 1)
    return math.sqrt(variance) / math.sqrt(n)

output_file = open("../../data/output_sample.txt", "w")
for i in range(1, 451):
    input_file = f"../../data/output_{i}.txt"
    if os.path.isfile(input_file):
        data = []
        with open(input_file) as f:
            for j, line in enumerate(f):
                if j >= 5:
                    numbers = line.strip().split()
                    if numbers:
                        data.append(float(numbers[-1]))
        if data:
            average = sum(data) / len(data)
            error = compute_sample_error(data)
            output_file.write(f"{average}\t{error}\n")

output_file.close()


