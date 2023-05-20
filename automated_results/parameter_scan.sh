#!/bin/bash

#########################################################################################
# Usage: 'bash parameter_scan.sh 6.4 6.0 5.6 100 4', where the float numbers are the    #
# beta values you want to consider and then there is an integer is is the number of     #
# thermalisations. The last integer is the number of 2AS Dirac fermions.                #
# #######################################################################################


# Get beta values from command line arguments
betas="${@:1:$(($#-2))}"

# Get thermalization from the last command line argument
therm_num="${@: -2}"

flavours="${@: -1}"

# Get flavours 
#flavours="${@: -1}"

cd ../analysis_code/parameter_scan

# Run analyze_plaquette.py for beta values
python3 analyze_plaquette.py $betas $therm_num $flavours

cd ../../plots/codes/

# Run plot stuff
python3 plot_data_nf${flavours}_scan.py $betas
