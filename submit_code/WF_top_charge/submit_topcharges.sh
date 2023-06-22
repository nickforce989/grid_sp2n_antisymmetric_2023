#!/bin/bash

#############################################################################################
# Submit jobs for topological charges for b = 6.8, 6.9.                                     #
#############################################################################################


module purge
module load cuda/11.4.1  openmpi/4.1.1-cuda11.4.1  ucx/1.12.0-cuda11.4.1

export LD_LIBRARY_PATH=/home/dp208/dp208/dc-forz1/grid/prefix/lib:/mnt/lustre/tursafs1/apps/basestack/cuda-11.4.1/ucx/1.12.0-cuda11.4.1/lib:/mnt/lustre/tursafs1/apps/basestack/cuda-11.4.1/openmpi/4.1.1-cuda11.4.1/lib:/mnt/lustre/tursafs1/apps/cuda/11.4.1/lib64/


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
