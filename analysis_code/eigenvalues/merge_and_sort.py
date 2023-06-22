import sys

# read input file names from command line arguments
input_files = sys.argv[1:]

# initialize an empty list to store all the numbers
numbers = []

# loop through each input file
for file_name in input_files:
    # open the file and read each line as a float number
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            number = float(line.strip())
            numbers.append(number)

# sort the numbers in ascending order
numbers.sort()

# write the sorted numbers to a file
with open('../../data/eigenvalues/unfolded_dist.txt', 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')
