#!/bin/bash

initial_tests_dir="../../precomputed_data/eigenvalues/"

cd ../analysis_code/eigenvalues

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}


if is_dir_empty_except_hidden "$initial_tests_dir"; then
  bash fund_analysis.sh
  bash 2AS_analysis.sh
fi

cd ../../plots/codes/

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  # Plotting distributions
  python Dw_distributions.py
else
  python Dw_distributions.py --dp
fi


