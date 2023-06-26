#!/bin/bash

cd ../analysis_code/susceptibility

initial_tests_dir="../../precomputed_data/susceptibility/"


if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python analyse_susceptibility.py
fi

cd ../../plots/codes/

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python plot_susc.py
else
  python plot_susc.py --dp
fi
