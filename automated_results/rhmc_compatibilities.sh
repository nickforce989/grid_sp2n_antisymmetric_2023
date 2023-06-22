#!/bin/bash

initial_tests_dir="../../precomputed_data/rhmc_compatibilities/"

cd ../analysis_code/rhmc_compatibility

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 analyse_rhmc_compatibilities.py
fi


cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 plot_data_comp_rhmc.py
  python3 plot_data_comp_rhmc_2p2.py
else
  python3 plot_data_comp_rhmc.py --dp
  python3 plot_data_comp_rhmc_2p2.py --dp
fi

