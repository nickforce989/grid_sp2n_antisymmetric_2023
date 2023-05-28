import sys
import re
import os

def extract_value(line):
    match = re.search(r'Polyakov Loop:\s*\[\s*\d+\s*\]\s*\((-?\d+\.\d+)', line)
    if match:
        return float(match.group(1))
    return None

if len(sys.argv) != 4:
    print("Usage: python extract_numbers.py input_file output_file N_thermalise")
    sys.exit(1)

input_file = "../../raw_data/" + sys.argv[1]
output_file = "../../data/" + sys.argv[2]
lines_to_delete = int(sys.argv[3])

try:
    with open(input_file, 'r') as f:
        polyakov_numbers = []
        for line in f:
            value = extract_value(line)
            if value is not None:
                polyakov_numbers.append(str(value))

    with open(output_file, 'w') as f:
        f.write('\n'.join(polyakov_numbers[lines_to_delete:]))
    print(f"Numbers extracted from '{input_file}', saved to '{output_file}', and {lines_to_delete} lines deleted from the beginning.")

except FileNotFoundError:
    print(f"File '{input_file}' not found.")
except IOError:
    print("Error occurred while reading or writing the files.")
