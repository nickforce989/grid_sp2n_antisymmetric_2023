import sys
import os

# Check if a file has been provided as an argument
if len(sys.argv) != 2:
    print("Usage: python even_lines.py <filename>")
    sys.exit(1)

file_path = sys.argv[1]

# Check if the file exists
if not os.path.isfile(file_path):
    print(f"Error: file '{file_path}' not found.")
    sys.exit(1)

# Create the output file path by adding '-nodegeneracies' before the extension
directory, filename = os.path.split(file_path)
filename_parts = os.path.splitext(filename)
output_filename = os.path.join(directory, filename_parts[0] + "-nodegeneracies" + filename_parts[1])

# Open the input file for reading
with open(file_path, "r") as input_file:
    # Open the output file for writing
    with open(output_filename, "w") as output_file:
        # Read the input file line by line
        for i, line in enumerate(input_file):
            # Write odd lines to the output file
            if i % 2 == 0:
                output_file.write(line)
