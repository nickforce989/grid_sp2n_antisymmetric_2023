#!/bin/bash

initial_tests_dir="../../precomputed_data/rhmc_compatibilities/"

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}


cd ../analysis_code/rhmc_compatibility

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python analyse_rhmc_compatibilities.py
fi


cd ../../plots/codes/


if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python plot_data_comp_rhmc.py
  python plot_data_comp_rhmc_2p2.py
else
  python plot_data_comp_rhmc.py --dp
  python plot_data_comp_rhmc_2p2.py --dp
fi

