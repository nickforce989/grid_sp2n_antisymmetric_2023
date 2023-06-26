#!/bin/bash

############################################################################
# Run this just with eigenvalues_*.txt files in the directory              #
# Fundamental representation version                                       #
############################################################################

# create an array to store the names of the files starting with "eigenvalues_"
files=($(ls ../../data/eigenvalues/2as_*))
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

# create a new array to store the modified file names
modified_files=()
for file in "${files[@]}"; do
  # add "-nodegeneracies" to the file name before the .txt extension
  modified_files+=("${file/.txt/-nodegeneracies.txt}")
done

# print the list of file names
echo "List of files:"
for file in "${modified_files[@]}"; do
  echo "$file"
done


# create a new array to store the second modified file names
modified_files_2=()
for file in "${modified_files[@]}"; do
  # add "_2" to the file name before the .txt extension
  modified_files_2+=("${file/.txt/_2.txt}")
done

# print the list of file names
echo "List of files:"
for file in "${modified_files_2[@]}"; do
  echo "$file"
done

for file in "${files[@]}"
do
    python even_lines.py "$file"
done
python merge_and_sort.py "${modified_files[@]}"
python assign_positions.py "${modified_files[@]}"
python 2as_find_spacings.py "${modified_files_2[@]}"
python 2as_find_spacings_2.py "${modified_files_2[@]}"

rm ../../data/eigenvalues/2as_*
rm ../../data/eigenvalues/unfolded_dist.txt
