#!/bin/bash

initial_tests_dir="../../precomputed_data/initial_tests/"
initial_tests_dir2="../../precomputed_data/reversibility/"

cd ../analysis_code/initial_tests

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python analyse_creutz.py
  python analyse_plaquette.py
  python analyse_dHsteps.py
  python analyse_pacc.py
fi

if [ -z "$(ls -A $initial_tests_dir2)" ]; then
  python analyse_rev.py
fi

cd ../../plots/codes

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python plot_data_creutz.py
  python plot_data_plaq_step.py
  python plot_data_dH_steps.py
  python plot_data_pacc_steps.py
else
  python plot_data_creutz.py --dp
  python plot_data_plaq_step.py --dp
  python plot_data_dH_steps.py --dp
  python plot_data_pacc_steps.py --dp
fi

if [ -z "$(ls -A $initial_tests_dir2)" ]; then
  python plot_data_reversibility.py
else
  python plot_data_reversibility.py --dp
fi

