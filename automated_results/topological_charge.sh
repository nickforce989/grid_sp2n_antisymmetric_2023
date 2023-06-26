#!/bin/bash

initial_tests_dir="../../precomputed_data/TopCharge/"

cd ../analysis_code/top_charge/

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python top_charges.py
fi


cd ../../plots/codes/


if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python plot_topcharge_b68.py
  python plot_topcharge_b69.py
else
  python plot_topcharge_b68.py --dp
  python plot_topcharge_b69.py --dp
fi



