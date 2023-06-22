#!/bin/bash

initial_tests_dir="../../precomputed_data/WF/"

cd ../analysis_code/WF/

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 WF_energydens.py
fi

cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python3 plot_WF_E.py
  python3 plot_WF_W.py
else
  python3 plot_WF_E.py --dp
  python3 plot_WF_W.py --dp
fi


