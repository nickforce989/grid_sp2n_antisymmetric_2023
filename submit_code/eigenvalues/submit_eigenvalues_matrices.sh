#!/bin/bash

####################################################################
# This submits 16 jobs at a time for eigenvalues, for 8 times,     #
# hence it will generate 128 configurations in total.              #
# It takes configurations from /scratch/s.2227764.                 #
####################################################################


conf_dir="./../../conf_saved_eigen/"
ckpoint_file="ckpoint_lat."

module purge
module load cuda/11.4.1  openmpi/4.1.1-cuda11.4.1  ucx/1.12.0-cuda11.4.1

export LD_LIBRARY_PATH=/home/dp208/dp208/dc-forz1/grid/prefix/lib:/mnt/lustre/tursafs1/apps/basestack/cuda-11.4.1/ucx/1.12.0-cuda11.4.1/lib:/mnt/lustre/tursafs1/apps/basestack/cuda-11.4.1/openmpi/4.1.1-cuda11.4.1/lib:/mnt/lustre/tursafs1/apps/cuda/11.4.1/lib64/

sbatch eigen_test1
sbatch eigen_test2
sbatch eigen_test3
sbatch eigen_test4

wait 

for j in {0..7}
do
	python3 substitute_values.py
	sbatch eigen_test1
	sbatch eigen_test2
	sbatch eigen_test3
	sbatch eigen_test4
	wait

done
