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

output_file = open("../../data/output_jackknife.txt", "w")
for i in range(1, 451):
    input_file = f"../../data/output_{i}.txt"
    if os.path.isfile(input_file):
        data = []
        with open(input_file) as f:
            line_count = 0
            for line in f:
                line_count += 1
                if line_count > 20:
                    numbers = line.strip().split()
                    if numbers:
                        data.append(float(numbers[-1]))
        if data:
            average = sum(data) / len(data)
            error = compute_jackknife(data)
            output_file.write(f"{average}\t{error}\n")

output_file.close()

