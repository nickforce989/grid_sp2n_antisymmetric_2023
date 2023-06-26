#!/bin/bash

initial_tests_dir="../../precomputed_data/WF/"

cd ../analysis_code/WF/

if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python WF_energydens.py
fi

cd ../../plots/codes/


if [ -z "$(find "$initial_tests_dir" -mindepth 1 -type f -not -path '*/\.*')" ]; then
  python plot_WF_E.py
  python plot_WF_W.py
else
  python plot_WF_E.py --dp
  python plot_WF_W.py --dp
fi


