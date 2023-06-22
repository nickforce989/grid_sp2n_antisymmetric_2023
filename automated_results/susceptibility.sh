#!/bin/bash

cd ../analysis_code/susceptibility

initial_tests_dir="../../precomputed_data/susceptibility/"


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 analyse_susceptibility.py
fi

cd ../../plots/codes/

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 plot_susc.py
else
  python3 plot_susc.py --dp
fi
