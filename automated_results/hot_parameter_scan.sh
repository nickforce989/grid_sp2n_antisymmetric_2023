#!/bin/bash

#########################################################################################
# Usage: 'bash parameter_scan.sh 6.4 6.0 5.6 100 4', where the float numbers are the    #
# beta values you want to consider and then there is an integer is is the number of     #
# thermalisations. The last integer is the number of 2AS Dirac fermions.                #
#########################################################################################

# Get beta values from command line arguments
betas="5.6 5.8 6.0 6.2 6.3 6.4"

# Get thermalization from the last command line argument
therm_num=200

initial_tests_dir="../../precomputed_data/Nf4_hot/"
initial_tests_dir2="../../precomputed_data/Nf4_data/"

cd ../analysis_code/parameter_scan

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 hot_analyze_plaquette.py $betas $therm_num 4
fi

if [ -z "$(ls -A $initial_tests_dir2)" ]; then
  python3 analyze_plaquette.py $betas $therm_num 4
fi

cd ../../plots/codes/

if [ -z "$(ls -A $initial_tests_dir)" ] && [ -z "$(ls -A $initial_tests_dir2)" ]; then
  # Run plot stuff
  python3 plot_hot.py
elif [ -z "$(ls -A $initial_tests_dir)" ] && [ ! -z "$(ls -A $initial_tests_dir2)" ]; then
  python3 plot_hot.py --dp1
elif [ ! -z "$(ls -A $initial_tests_dir)" ] && [ -z "$(ls -A $initial_tests_dir2)" ]; then
  python3 plot_hot.py --dp2
else
  python3 plot_hot.py --dp1 --dp2
fi

