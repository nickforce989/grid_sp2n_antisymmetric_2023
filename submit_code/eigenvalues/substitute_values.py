import re

input_files = ['eigen_test1', 'eigen_test2', 'eigen_test3', 'eigen_test4']

for input_file in input_files:
    with open(input_file, 'r+') as file:
        original_content = file.read()

        # Modify g5Dw_Operator_
        modified_content = re.sub(r'g5Dw_Operator_(\d+)', lambda match: f'g5Dw_Operator_{int(match.group(1)) + 16}', original_content)

        # Modify ckpoint_lat.
        modified_content = re.sub(r'ckpoint_lat\.(\d+)', lambda match: f'ckpoint_lat.{int(match.group(1)) + 3200}', modified_content)

        # Move file pointer to the beginning and truncate the file
        file.seek(0)
        file.truncate()

        # Write modified content to the file
        file.write(modified_content)
