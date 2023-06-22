#!/bin/bash

initial_tests_dir="../../precomputed_data/initial_tests/"
initial_tests_dir2="../../precomputed_data/reversibility/"

cd ../analysis_code/initial_tests

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 analyse_creutz.py
  python3 analyse_plaquette.py
  python3 analyse_dHsteps.py
  python3 analyse_pacc.py
fi

if [ -z "$(ls -A $initial_tests_dir2)" ]; then
  python3 analyse_rev.py
fi

cd ../../plots/codes

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 plot_data_creutz.py
  python3 plot_data_plaq_step.py
  python3 plot_data_dH_steps.py
  python3 plot_data_pacc_steps.py
else
  python3 plot_data_creutz.py --dp
  python3 plot_data_plaq_step.py --dp
  python3 plot_data_dH_steps.py --dp
  python3 plot_data_pacc_steps.py --dp
fi

if [ -z "$(ls -A $initial_tests_dir2)" ]; then
  python3 plot_data_reversibility.py
else
  python3 plot_data_reversibility.py --dp
fi

