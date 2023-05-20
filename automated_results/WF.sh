#!/bin/bash

cd ../analysis_code/WF/

python3 WF_energydens.py

cd ../../plots/codes/

python3 plot_WF_E.py
python3 plot_WF_W.py
