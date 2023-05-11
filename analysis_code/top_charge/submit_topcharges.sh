#!/bin/bash

# Define initial values for n and m
n=150
m=$((n+200))

module load compiler/gnu/10/2.0
module load CUDA/11.7

export LD_LIBRARY_PATH=/home/s.2227764/sympl_grid_modified/prefix/lib:${LD_LIBRARY_PATH}

make Test_WilsonFlow
sbatch test

# Define the name of the output file based on n and m
output_file="./hmc_${SLURM_JOB_ID}_vol12_b69-am08_${n}-${m}.out"

# Use sed to modify the last line of the file 'test'
sed -i "\$s#.*#--grid \${VOL}   > $output_file#" test

# Loop 13 times
for i in {1..13}; do
  # Use sed to substitute n and m in the desired line
  sed -i "s/for (int conf = $n; conf <= $m; conf+= 1){/for (int conf = $((n+200)); conf <= $((m+200)); conf+= 1){/" ../../../tests/smearing/Test_WilsonFlow.cc
  # Increment n and m for the next loop
  n=$((n+200))
  m=$((n+200))

  # Update the output file name based on the new values of n and m
  output_file="./hmc_${SLURM_JOB_ID}_vol12_b69-am08_${n}-${m}.out"

  # Use sed to modify the last line of the file 'test'
  sed -i "\$s#.*#--grid \${VOL}   > $output_file#" test

  make Test_WilsonFlow
  sbatch test
done

