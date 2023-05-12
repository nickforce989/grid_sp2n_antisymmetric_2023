import sys
import os

# Check if a file has been provided as an argument
if len(sys.argv) != 2:
    print("Usage: python even_lines.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Check if the file exists
if not os.path.isfile(filename):
    print(f"Error: file '{filename}' not found.")
    sys.exit(1)

# Create the output filename by adding '-nodegeracies' to the end of the input filename
output_filename = filename.split(".")[0] + "-nodegeneracies.txt"

# Open the input file for reading
with open(filename, "r") as input_file:
    # Open the output file for writing
    with open(output_filename, "w") as output_file:
        # Read the input file line by line
        for i, line in enumerate(input_file):
            # Write odd lines to the output file
            if i % 2 == 0:
                output_file.write(line)
