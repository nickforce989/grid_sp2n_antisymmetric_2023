#!/bin/bash


initial_tests_dir="../../precomputed_data/force_contribution/"

cd ../analysis_code/forces

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python analyse_forces.py
fi


cd ../../plots/codes/


if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python plot_forces.py
else
  python plot_forces.py --dp
fi


