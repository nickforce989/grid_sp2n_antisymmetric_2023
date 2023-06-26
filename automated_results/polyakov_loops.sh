#!/bin/bash

initial_tests_dir="../../precomputed_data/polyakov_loops/"

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}


cd ../analysis_code/polyakov_loops

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python polyloops_analysis.py
fi


cd ../../plots/codes/

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python plot_poly.py
else
  python plot_poly.py --dp
fi
