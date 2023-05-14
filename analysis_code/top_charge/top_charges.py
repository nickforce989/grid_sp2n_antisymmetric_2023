####################################################################################
# Given files hmc_*.out, we find the files for plots of Top charges. Both for      #
# b = 6.8 and 6.9.	                                                            #
####################################################################################

import os

directory = os.path.dirname(os.path.abspath(__file__)) # get the directory of the script

def process_files(input_files, output_file, output_file_with_index):
    unique_numbers = set() # Keep track of unique numbers seen so far
    numbers_in_order = [] # Keep track of the order in which numbers appear in the input files

    for file in input_files:
        with open(os.path.join(directory, file), "r") as f_in:
            for line in f_in:
                if "Top. charge           : 200" in line:
                    number = float(line.split()[-1])
                    if number not in unique_numbers:
                        unique_numbers.add(number)
                        numbers_in_order.append(number)

    with open(output_file, "w") as f_out, open(output_file_with_index, "w") as f_out_index:
        for i, number in enumerate(numbers_in_order):
            f_out.write(f"{number}\n")
            f_out_index.write(f"{i+1}\t{number}\n")

input_files = [f for f in os.listdir(directory) if f.endswith(".out") and "b69" in f] # get list of files in directory with ".out" extension and "b69" in filename
input_files.sort(key=lambda f: int(f.split("_")[-1].split("-")[-1].split(".")[0])) # sort by last number before ".out"
process_files(input_files, "top_charges_b69-am08.txt", "top_charges_b69-am08_with_index.txt")

input_files = [f for f in os.listdir(directory) if f.endswith(".out") and "b68" in f] # get list of files in directory with ".out" extension and "b68" in filename
input_files.sort(key=lambda f: int(f.split("_")[-1].split("-")[-1].split(".")[0])) # sort by last number before ".out"
process_files(input_files, "top_charges_b68-am08.txt", "top_charges_b68-am08_with_index.txt")

