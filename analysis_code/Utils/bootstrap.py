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
    variance = sum((avg - mean)**2 for avg in averages) / (num_samples - 1)
    return (variance ** 0.5)

output_file = open("output_bootstrap.txt", "w")
for i in range(1, 15):
    input_file = f"output_{i}.txt"
    if os.path.isfile(input_file):
        data = []
        with open(input_file) as f:
            lines_to_skip = 20
            for j, line in enumerate(f):
                if j < lines_to_skip:
                    continue
                numbers = line.strip().split()
                if numbers:
                    data.append(float(numbers[-1]))
        if data:
            average = sum(data) / len(data)
            error = compute_bootstrap(data)
            output_file.write(f"{average}\t{error}\n")

output_file.close()

