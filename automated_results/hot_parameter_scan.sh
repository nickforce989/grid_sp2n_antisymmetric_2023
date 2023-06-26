#!/bin/bash

#########################################################################################
# Usage: 'bash parameter_scan.sh 6.4 6.0 5.6 100 4', where the float numbers are the    #
# beta values you want to consider and then there is an integer is is the number of     #
# thermalisations. The last integer is the number of 2AS Dirac fermions.                #
#########################################################################################

# Get beta values from command line arguments
betas="5.6 5.8 6.0 6.2 6.3 6.4"

# Get thermalization from the last command line argument
therm_num=200

initial_tests_dir="../../precomputed_data/Nf4_hot/"
initial_tests_dir2="../../precomputed_data/Nf4_data/"

cd ../analysis_code/parameter_scan

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python hot_analyze_plaquette.py $betas $therm_num 4
fi

if is_dir_empty_except_hidden "$initial_tests_dir2"; then
  python analyze_plaquette.py $betas $therm_num 4
fi

cd ../../plots/codes/

if is_dir_empty_except_hidden "$initial_tests_dir" && is_dir_empty_except_hidden "$initial_tests_dir2"; then
  # Run plot stuff
  python plot_hot.py
elif is_dir_empty_except_hidden "$initial_tests_dir" && ! is_dir_empty_except_hidden "$initial_tests_dir2"; then
  python plot_hot.py --dp1
elif ! is_dir_empty_except_hidden "$initial_tests_dir" && is_dir_empty_except_hidden "$initial_tests_dir2"; then
  python plot_hot.py --dp2
else
  python plot_hot.py --dp1 --dp2
fi
