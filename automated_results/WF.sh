#!/bin/bash

initial_tests_dir="../../precomputed_data/WF/"

cd ../analysis_code/WF/

if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python WF_energydens.py
fi

cd ../../plots/codes/


if [ -z "$(ls -A $initial_tests_dir)" ]; then
  python plot_WF_E.py
  python plot_WF_W.py
else
  python plot_WF_E.py --dp
  python plot_WF_W.py --dp
fi


