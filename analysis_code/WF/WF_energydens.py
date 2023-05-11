import re

# Define the input and output file names
input_file_name = "hmc_7472940_vol12_b69-am08.out"
output_file_prefix = "output_"

# Read in the input file
with open(input_file_name, "r") as input_file:
    input_lines = input_file.readlines()

# Define the regular expression to match the desired lines
pattern = r"\[WilsonFlow\] Energy density \(Clover plaq\) : (\d{1,3})"

# Loop over the lines and extract the numbers
numbers = set()
for line in input_lines:
    match = re.search(pattern, line)
    if match is not None:
        number = int(match.group(1))
        if number >= 1 and number <= 450:
            numbers.add(number)

# Loop over the numbers and write the corresponding lines to output files
for number in numbers:
    output_file_name = output_file_prefix + str(number) + ".txt"
    with open(output_file_name, "w") as output_file:
        for line in input_lines:
            match = re.search(pattern, line)
            if match is not None:
                this_number = int(match.group(1))
                if this_number == number:
                    output_file.write(line)
