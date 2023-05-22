import sys
import re

if len(sys.argv) < 2:
    print("Usage: python script.py <input_file1> <input_file2> ...")
    sys.exit(1)

input_files = sys.argv[1:]

for input_file in input_files:
    with open(input_file, 'r+') as file:
        original_content = file.read()

        # Modify g5Dw_Operator_
        modified_content = re.sub(r'--confstart (\d+)', lambda match: f'--confstart {int(match.group(1)) + 3350}', original_content)

        # Modify ckpoint_lat.
        modified_content = re.sub(r'--confend (\d+)', lambda match: f'--confend {int(match.group(1)) + 3350}', modified_content)

        # Replace integer numbers in the pattern '-am08_M-N.out'
        modified_content = re.sub(r'-am08_(\d+)-(\d+)\.out', lambda match: f'-am08_{int(match.group(1)) + 3350}-{int(match.group(2)) + 3350}.out', modified_content)

        # Move file pointer to the beginning and truncate the file
        file.seek(0)
        file.truncate()

        # Write modified content to the file
        file.write(modified_content)

