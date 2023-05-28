#!/bin/bash

cd ../analysis_code/initial_tests

python3 analyse_creutz.py
python3 analyse_plaquette.py
python3 analyse_dHsteps.py
python3 analyse_pacc.py
python3 analyse_rev.py

cd ../../plots/codes/

python3 plot_data_creutz.py
python3 plot_data_plaq_step.py
python3 plot_data_dH_steps.py
python3 plot_data_pacc_steps.py
python3 plot_data_reversibility.py
