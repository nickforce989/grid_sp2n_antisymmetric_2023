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
    input_file = os.path.join(directory, '/../../data/spacings_density.txt')
    output_file = os.path.join(directory, '/../../data/spacings_density_2.txt')
    with open(input_file, 'r') as f_in:
        spacings = [float(line.strip()) for line in f_in]
    avg_spacing = sum(spacings) / len(spacings)
    factor = 1 / avg_spacing if avg_spacing != 0 else 1
    with open(output_file, 'w') as f_out:
        for spacing in spacings:
            f_out.write('{:.4f}\n'.format(spacing * factor))

if __name__ == '__main__':
    for input_file in sys.argv[1:]:
        create_spacings_file(input_file)
    merge_spacings_files(os.getcwd())
