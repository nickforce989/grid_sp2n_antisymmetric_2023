#!/bin/bash

initial_tests_dir="../../precomputed_data/polyakov_loops/"

cd ../analysis_code/polyakov_loops

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 polyloops_analysis.py
fi


cd ../../plots/codes/

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 plot_poly.py
else
  python3 plot_poly.py --dp
fi
