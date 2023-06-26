#!/bin/bash

initial_tests_dir="../../precomputed_data/WF/"

cd ../analysis_code/WF/

# Function to check if a directory is empty except for hidden files
is_dir_empty_except_hidden() {
  local dir=$1
  local files_count=$(find "$dir" -maxdepth 1 -type f ! -iname ".*" | wc -l)
  [[ $files_count -eq 0 ]]
}

if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python WF_energydens.py
fi

cd ../../plots/codes/


if is_dir_empty_except_hidden "$initial_tests_dir"; then
  python plot_WF_E.py
  python plot_WF_W.py
else
  python plot_WF_E.py --dp
  python plot_WF_W.py --dp
fi


