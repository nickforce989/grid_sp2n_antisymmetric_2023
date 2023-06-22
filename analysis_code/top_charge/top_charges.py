####################################################################################
# Given files hmc_*.out, we find the files for plots of Top charges. Both for      #
# b = 6.8 and 6.9.	                                                            #
####################################################################################

import os

directory = os.path.dirname(os.path.abspath(__file__))  # get the directory of the script

def process_files(input_files, output_file, output_file_with_index, top_charge_number):
    unique_numbers = set()  # Keep track of unique numbers seen so far
    numbers_in_order = []  # Keep track of the order in which numbers appear in the input files

    for file in input_files:
        with open(file, "r") as f_in:
            for line in f_in:
                if f"Top. charge           : {top_charge_number}" in line:
                    number = float(line.split()[-1])
                    if number not in unique_numbers:
                        unique_numbers.add(number)
                        numbers_in_order.append(number)

    with open(output_file, "w") as f_out, open(output_file_with_index, "w") as f_out_index:
        for i, number in enumerate(numbers_in_order):
            f_out.write(f"{number}\n")
            f_out_index.write(f"{i + 1}\t{number}\n")


directory2 = '../../raw_data/WF_TopCharge/'
input_files = [f for f in os.listdir(directory2) if f.endswith(".out") and "b69" in f]
input_files.sort(key=lambda f: int(f.split("_")[-1].split("-")[-1].split(".")[0]))  # sort by last number before ".out"
directory = '../../raw_data/WF_TopCharge/'
modified_names = [os.path.join(directory, name) for name in input_files]
process_files(modified_names, "../../data/TopCharge/top_charges_b69-am08.txt",
              "../../data/TopCharge/top_charges_b69-am08_with_index.txt", 407)

input_files = [f for f in os.listdir(directory2) if f.endswith(".out") and "b68" in f]
input_files.sort(key=lambda f: int(f.split("_")[-1].split("-")[-1].split(".")[0]))  # sort by last number before ".out"
modified_names = [os.path.join(directory2, name) for name in input_files]
process_files(modified_names, "../../data/TopCharge/top_charges_b68-am08.txt",
              "../../data/TopCharge/top_charges_b68-am08_with_index.txt", 223)

