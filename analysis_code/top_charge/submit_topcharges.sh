#############################################################################################
# Submit jobs for topological charges for b = 6.8, 6.9.                                     #
#############################################################################################

#!/bin/bash

# Define initial values for n and m
n=150
m=$((n+200))

module load compiler/gnu/10/2.0
module load CUDA/11.7

export LD_LIBRARY_PATH=/home/s.2227764/sympl_grid_modified/prefix/lib:${LD_LIBRARY_PATH}

# Set initial values in configurations
sed -i 's/--confstart.*/--confstart 150 \\/' test_WF
sed -i 's/--confend.*/--confend 350 \\/' test_WF

# Update the output file name based on the new values of n and m
output_file="./hmc_\${SLURM_JOB_ID}_vol12_b69-am08_${n}-${m}.out"

# Use sed to modify the last line of the file 'test'
sed -i "\$s#.*# > $output_file#" test_WF

sbatch test_WF

sleep 5s
# Loop 13 times
for i in {1..13}; do
  # Use sed to substitute n and m in the desired line
  sed -i "s/--confstart $n/--confstart $((n+200))/;s/--confend $m/--confend $((m+200))/" test_WF
  # Increment n and m for the next loop
  n=$((n+200))
  m=$((n+200))

  # Update the output file name based on the new values of n and m
  output_file="./../../raw_data/hmc_\${SLURM_JOB_ID}_vol12_b69-am08_${n}-${m}.out"

  # Use sed to modify the last line of the file 'test'
  sed -i "\$s#.*# > $output_file#" test_WF

  sbatch test_WF
  sleep 5s
done

###############################################################################

sleep 3h 30m

###############################################################################

#Do the same thing for b = 6.8 
sed -i "s|--confsave /scratch/s.2227764/WF_confs_vol12_b69-am08_final \\\|--confsave /scratch/s.2227764/WF_confs_vol12_final \\\|g" test_WF

# Set initial values in configurations
sed -i 's/--confstart.*/--confstart 150 \\/' test_WF
sed -i 's/--confend.*/--confend 350 \\/' test_WF


# Update the output file name based on the new values of n and m
output_file="./hmc_\${SLURM_JOB_ID}_vol12_b68-am08_${n}-${m}.out"

# Use sed to modify the last line of the file 'test'
sed -i "\$s#.*# > $output_file#" test_WF

sbatch test_WF

sleep 5s
# Loop 13 times
for i in {1..13}; do
  # Use sed to substitute n and m in the desired line
  sed -i "s/--confstart $n/--confstart $((n+200))/;s/--confend $m/--confend $((m+200))/" test_WF
  # Increment n and m for the next loop
  n=$((n+200))
  m=$((n+200))

  # Update the output file name based on the new values of n and m
  output_file="./../../raw_data/hmc_\${SLURM_JOB_ID}_vol12_b68-am08_${n}-${m}.out"

  # Use sed to modify the last line of the file 'test'
  sed -i "\$s#.*# > $output_file#" test_WF

  sbatch test_WF
  sleep 5s
done
