#!/bin/bash

#################################################################
# This take g5Dw_Operator_*.txt files, rename them and then     #
# finds the eigenvalues for each file.                          #
# NB: Before running this modify "find_eigenvalues.py" in       #
# "g5Dw_Operator_whatever.txt" in "g5Dw_Operator_1.txt" and     #
# "eigenvalues_whatever.txt" to "eigenvalues_1.txt"             #
# NNB: RUN IT JUST ONCE, IF RE-RUN, RECOPY AND PASTE THE FILES  #
# IN THE DIRECTORY.						#
#################################################################

counter=1
for file in eigenvalues_*.txt; do
  if [[ -f "$file" ]]; then
    mv "$file" "g5Dw_Operator_$counter.txt"
    counter=$((counter+1))
  fi
done


# Loop through files named eigenvalues_n.txt
for (( k=2; ; k++ )); do
  if [[ -f "g5Dw_Operator_$k.txt" ]]; then
    # Modify the first line of the Python code to read g5Dw_Operator_1.txt
    sed -i "s/read_matrix(\"g5Dw_Operator_$((k-1)).txt\")/read_matrix(\"g5Dw_Operator_$k.txt\")/" find_eigenvalues.py

    # Modify the second line of the Python code to write to eigenvalues_1.txt
    sed -i "s/eigenvalues_$((k-1)).txt/eigenvalues_$k.txt/" find_eigenvalues.py

    # Run the modified Python code
    python find_eigenvalues.py
  else
    # No more files found, exit the loop
    break
  fi
done



