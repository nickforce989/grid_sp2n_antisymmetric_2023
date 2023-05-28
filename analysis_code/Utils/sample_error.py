import os
import math
import sys

def compute_sample_error(data):
    """
    Compute the sample error given a list of data.
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / (n - 1)
    return math.sqrt(variance) / math.sqrt(n)

def process_file(input_file, output_file):
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

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(output_file, "w") as f:
        process_file(input_file, f)
