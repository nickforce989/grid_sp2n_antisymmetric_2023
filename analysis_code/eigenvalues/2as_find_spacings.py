
import sys
import os

def create_spacings_file(input_file):
    output_file = os.path.splitext(input_file)[0] + '_spacings.txt'
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        prev_num = None
        for line in f_in:
            try:
                num = float(line.strip())
                if prev_num is not None:
                    spacing = num - prev_num
                    f_out.write(str(spacing) + '\n')
                prev_num = num
            except ValueError:
                pass

def merge_spacings_files(directory):
    output_file = os.path.join(directory, '../../data/eigenvalues/2as_spacings_density.txt')
    with open(output_file, 'w') as f_out:
    	new_dir = output_file = os.path.join(directory, '../../data/eigenvalues')
    	for filename in os.listdir(new_dir):
            if filename.endswith('_spacings.txt'):
                filepath = os.path.join(new_dir, filename)
                with open(filepath, 'r') as f_in:
                    for line in f_in:
                        f_out.write(line)

if __name__ == '__main__':
    for input_file in sys.argv[1:]:
        create_spacings_file(input_file)
    merge_spacings_files(os.getcwd())

