#!/bin/bash

cd ../analysis_code/top_charge/

python3 top_charges.py

cd ../../plots/codes/

python3 plot_topcharge_b68.py
python3 plot_topcharge_b69.py
