#!/bin/bash

initial_tests_dir="../../precomputed_data/TopCharge/"

cd ../analysis_code/top_charge/

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python top_charges.py
fi


cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python plot_topcharge_b68.py
  python plot_topcharge_b69.py
else
  python plot_topcharge_b68.py --dp
  python plot_topcharge_b69.py --dp
fi



