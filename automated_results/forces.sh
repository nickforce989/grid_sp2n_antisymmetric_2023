#!/bin/bash


initial_tests_dir="../../precomputed_data/force_contribution/"

cd ../analysis_code/forces

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 analyse_forces.py
fi


cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 plot_forces.py
else
  python3 plot_forces.py --dp
fi


