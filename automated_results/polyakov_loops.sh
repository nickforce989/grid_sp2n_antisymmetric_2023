#!/bin/bash

initial_tests_dir="../../precomputed_data/polyakov_loops/"

cd ../analysis_code/polyakov_loops

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python polyloops_analysis.py
fi


cd ../../plots/codes/

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python plot_poly.py
else
  python plot_poly.py --dp
fi
