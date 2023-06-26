#!/bin/bash

initial_tests_dir="../../precomputed_data/rhmc_compatibilities/"

cd ../analysis_code/rhmc_compatibility

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python analyse_rhmc_compatibilities.py
fi


cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python plot_data_comp_rhmc.py
  python plot_data_comp_rhmc_2p2.py
else
  python plot_data_comp_rhmc.py --dp
  python plot_data_comp_rhmc_2p2.py --dp
fi

