#!/bin/bash

initial_tests_dir="../../precomputed_data/eigenvalues/"

cd ../analysis_code/eigenvalues

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  bash fund_analysis.sh
  bash 2AS_analysis.sh
fi

cd ../../plots/codes/

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  # Plotting distributions
  python Dw_distributions.py
else
  python Dw_distributions.py --dp
fi


