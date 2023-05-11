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

output_file = open("output_sample_pl.txt", "w")
for i in range(1, 801):
    input_file = f"outputpl_{i}.txt"
    if os.path.isfile(input_file):
        data = []
        with open(input_file) as f:
            for j, line in enumerate(f):
                if j >= 14:
                    numbers = line.strip().split()
                    if numbers:
                        data.append(float(numbers[-1]))
        if data:
            average = sum(data) / len(data)
            error = compute_sample_error(data)
            output_file.write(f"{average}\t{error}\n")

output_file.close()


