#!/bin/bash

############################################################################
# Run this just with eigenvalues_*.txt files in the directory              #
# Fundamental representation version                                       #
############################################################################

# create an array to store the names of the files starting with "eigenvalues_"
files=($(ls ../../data/eigenvalues/eigenvalues_*))
directory='../../data/eigenvalues/'

modified_files=()

for file in "${files[@]}"; do
  modified_files+=("${directory}${file}")
done

# print the list of file names
echo "List of files:"
for file in "${files[@]}"; do
  echo "$file"
done

# create a new array to store the second modified file names
modified_files_2=()
for file in "${files[@]}"; do
  # add "_2" to the file name before the .txt extension
  modified_files_2+=("${file/.txt/_2.txt}")
done

# print the list of file names
echo "List of files:"
for file in "${modified_files_2[@]}"; do
  echo "$file"
done

bash remove_extremal_eigenvalues.sh
python merge_and_sort.py "${files[@]}"
python assign_positions.py "${files[@]}"
python find_spacings.py "${modified_files_2[@]}"
python find_spacings_2.py "${modified_files_2[@]}"

rm ../../data/eigenvalues/eigenvalues_*
rm ../../data/eigenvalues/spacings_density.txt
rm ../../data/eigenvalues/unfolded_dist.txt
