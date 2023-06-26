#!/bin/bash

#########################################################################################
# Usage: 'bash parameter_scan.sh 6.4 6.0 5.6 100 4', where the float numbers are the    #
# beta values you want to consider and then there is an integer is the number of         #
# thermalisations. The last integer is the number of 2AS Dirac fermions.                 #
# #######################################################################################


# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}


# Get beta values from command line arguments
last_arg="${@: -1}"
if [ "$last_arg" = "0" ]; then
  betas="1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.1 5.2 5.3 5.4 5.5 5.6 5.7 5.8 5.9 6.0 6.1 6.2 6.3 6.4 6.5 6.6 6.7 6.8 6.9 7.0 7.1 7.2 7.3 7.4 7.5 7.6 7.7 7.8 7.9 8.0 8.1 8.2 8.3 8.4 8.5 8.6 8.7 8.8 8 9.0 9.5 10.0 10.5 11.0 11.5 12.0 12.5 13.0 13.5 14.0 14.5 15.0 15.5 16.0"
else
  betas="${@:1:$(($#-2))}"
fi

# Get thermalization from the second last command line argument
therm_num="${@: -2}"

flavours="${@: -1}"

initial_tests_dir="../../precomputed_data/Nf${flavours}_data/"

cd ../analysis_code/parameter_scan

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python analyze_plaquette.py $betas $therm_num $flavours
fi

cd ../../plots/codes/

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  # Run plot stuff
  python plot_data_nf${flavours}_scan.py $betas
else
  python plot_data_nf${flavours}_scan.py $betas --dp
fi
