#!/bin/bash

#################################################################
# This takes g5Dw_Operator_*.txt files, renames them, and then   #
# finds the eigenvalues for each file.                          #
# NB: Before running this, modify "find_eigenvalues.py" to      #
# replace "g5Dw_Operator_whatever.txt" with "g5Dw_Operator_1.txt"#
# and "eigenvalues_whatever.txt" with "eigenvalues_1.txt"       #
#################################################################

directory="../../raw_data/Dw_eigenvalues"
prefix="2as_g5Dw_Operator_"

# Get the list of files with integer numbers
file_list=$(ls -1 "$directory"/2as_g5Dw_Operator_*.txt 2>/dev/null | sort -V)

# Rename the files
counter=1
for file in $file_list
do
    new_name="${directory}/${prefix}${counter}.txt"
    mv "$file" "$new_name"
    counter=$((counter + 1))
done


# Loop through files named 2as_g5Dw_Operator_n.txt
for (( k=1; ; k++ )); do
  if [[ -f "../../raw_data/Dw_eigenvalues/2as_g5Dw_Operator_$k.txt" ]]; then
    # Modify the second line of the Python code to write to g5Dw_Operator_1.txt
    sed -i "s|../../raw_data/Dw_eigenvalues/2as_g5Dw_Operator_[0-9]*.txt|../../raw_data/Dw_eigenvalues/2as_g5Dw_Operator_$k.txt|" find_eigenvalues_2as.py

    # Modify the second line of the Python code to write to eigenvalues_1.txt
    sed -i "s|../../data/eigenvalues/2as_eigenvalues_[0-9]*.txt|../../data/eigenvalues/2as_eigenvalues_$k.txt|" find_eigenvalues_2as.py

    # Run the modified Python code which finds the eigenvalues for a tensor
    if python find_eigenvalues_2as.py; then
      echo "Eigenvalues found for 2as_g5Dw_Operator_$k.txt"
    else
      echo "Failed to find eigenvalues for 2as_g5Dw_Operator_$k.txt"
      continue
    fi
  else
    # No more files found, exit the loop
    break
  fi
done


directory="../../data/eigenvalues"
prefix="2as_eigenvalues_"

# Get the list of files with integer numbers
file_list=$(ls -1 "$directory"/2as_eigenvalues_*.txt 2>/dev/null | sort -V)

# Rename the files
counter=1
for file in $file_list
do
    new_name="${directory}/${prefix}${counter}.txt"
    mv "$file" "$new_name"
    counter=$((counter + 1))
done

