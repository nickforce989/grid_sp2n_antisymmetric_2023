#############################################################################################
# Submit jobs for topological charges for b = 6.8, 6.9.                                     #
#############################################################################################

#!/bin/bash

module load compiler/gnu/10/2.0
module load CUDA/11.7

export LD_LIBRARY_PATH=/home/s.2227764/sympl_grid_modified/prefix/lib:${LD_LIBRARY_PATH}


sbatch b69_test_WF1
sbatch b69_test_WF2
sbatch b69_test_WF3
sbatch b69_test_WF4

wait

# If you want for longer WF time
for i in {1..1}; do
  python3 substitute_values.py b69_test_WF1 b69_test_WF2 b69_test_WF3 b69_test_WF4
  sbatch b69_test_WF1
  sbatch b69_test_WF2
  sbatch b69_test_WF3
  sbatch b69_test_WF4
done

###############################################################################

wait

###############################################################################

#Do the same thing for b = 6.8 

sbatch b68_test_WF1
sbatch b68_test_WF2
sbatch b68_test_WF3
sbatch b68_test_WF4

wait

# If you want for longer WF time
for i in {1..1}; do
  python3 substitute_values.py b68_test_WF1 b68_test_WF2 b68_test_WF3 b68_test_WF4
  sbatch b68_test_WF1
  sbatch b68_test_WF2
  sbatch b68_test_WF3
  sbatch b68_test_WF4
done
