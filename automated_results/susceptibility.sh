#!/bin/bash

cd ../analysis_code/susceptibility

initial_tests_dir="../../precomputed_data/susceptibility/"

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}


if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python analyse_susceptibility.py
fi

cd ../../plots/codes/

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python plot_susc.py
else
  python plot_susc.py --dp
fi
