input_files = ["hmc_7472886_vol12_b69-am08_150-239.out", "hmc_7472942_vol12_b69-am08_240-900.out", "hmc_7473070_vol12_b69-am08_501-900_corr.out", "hmc_7473140_vol12_b69-am08_801-900_corr.out" , "hmc_7472946_vol12_b69-am08_901-1300.out", "hmc_7473073_vol12_b69-am08_1301-1600.out", "hmc_7473112_vol12_b69-am08_1601-2000.out", "hmc_7473138_vol12_b69-am08_1851-2000_corr.out", "hmc_7473137_vol12_b69-am08_2001-2350.out", "hmc_7473139_vol12_b69-am08_2201-2350_corr.out", "hmc_7473337_vol12_b69-am08_2351-2450.out", "hmc_7473409_vol12_b69-am08_2415-2450_corr.out", "hmc_7473338_vol12_b69-am08_2451-2550.out", "hmc_7473412_vol12_b69-am08_2515-2550_corr.out", "hmc_7473339_vol12_b69-am08_2551-2650.out", "hmc_7473416_vol12_b69-am08_2615-2650_corr.out", "hmc_7473340_vol12_b69-am08_2651-2750.out", "hmc_7473421_vol12_b69-am08_2715-2750_corr.out", "hmc_7473341_vol12_b69-am08_2751-2850.out", "hmc_7473482_vol12_b69-am08_2835-2850_corr.out", "hmc_7473342_vol12_b69-am08_2851-2950.out", "hmc_7473483_vol12_b69-am08_2935-2950_corr.out", "hmc_7473343_vol12_b69-am08_2951-3050.out", "hmc_7473484_vol12_b69-am08_3035-3050_corr.out", "hmc_7473355_vol12_b69-am08_3051-3150.out", "hmc_7473485_vol12_b69-am08_3130-3150_corr.out"] # Change this list to match the names of your input files
output_file = "top_charges_b69-am08.txt"
output_file_with_index = "top_charges_b69-am08_with_index.txt"

unique_numbers = set() # Keep track of unique numbers seen so far
numbers_in_order = [] # Keep track of the order in which numbers appear in the input files

for file in input_files:
    with open(file, "r") as f_in:
        for line in f_in:
            if "Top. charge           : 300" in line:
                number = float(line.split()[-1])
                if number not in unique_numbers:
                    unique_numbers.add(number)
                    numbers_in_order.append(number)

with open(output_file, "w") as f_out, open(output_file_with_index, "w") as f_out_index:
    for i, number in enumerate(numbers_in_order):
        f_out.write(f"{number}\n")
        f_out_index.write(f"{i+1}\t{number}\n")

