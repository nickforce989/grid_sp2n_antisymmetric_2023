#!/bin/bash

initial_tests_dir="../../precomputed_data/rhmc_compatibilities/"

cd ../analysis_code/rhmc_compatibility

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python analyse_rhmc_compatibilities.py
fi


cd ../../plots/codes/


if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python plot_data_comp_rhmc.py
  python plot_data_comp_rhmc_2p2.py
else
  python plot_data_comp_rhmc.py --dp
  python plot_data_comp_rhmc_2p2.py --dp
fi

