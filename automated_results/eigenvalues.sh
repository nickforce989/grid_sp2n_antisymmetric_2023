#!/bin/bash

cd ../analysis_code/eigenvalues

# Fundamental repr. analysis
bash fund_analysis.sh
bash 2AS_analysis.sh

cd ../../plots/codes/

# Plotting distributions
python3 Dw_distributions.py
