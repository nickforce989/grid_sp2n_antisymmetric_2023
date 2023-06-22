#!/bin/bash

initial_tests_dir="../../precomputed_data/eigenvalues/"

cd ../analysis_code/eigenvalues

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  bash fund_analysis.sh
  bash 2AS_analysis.sh
fi

cd ../../plots/codes/

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  # Plotting distributions
  python3 Dw_distributions.py
else
  python3 Dw_distributions.py --dp
fi


