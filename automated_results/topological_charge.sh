#!/bin/bash

initial_tests_dir="../../precomputed_data/TopCharge/"

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}



cd ../analysis_code/top_charge/

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python top_charges.py
fi


cd ../../plots/codes/


if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python plot_topcharge_b68.py
  python plot_topcharge_b69.py
else
  python plot_topcharge_b68.py --dp
  python plot_topcharge_b69.py --dp
fi



