#!/bin/bash


initial_tests_dir="../../precomputed_data/force_contribution/"

cd ../analysis_code/forces

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python analyse_forces.py
fi


cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python plot_forces.py
else
  python plot_forces.py --dp
fi


