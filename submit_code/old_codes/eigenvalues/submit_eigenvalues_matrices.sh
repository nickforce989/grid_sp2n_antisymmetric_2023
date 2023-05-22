#!/bin/bash

####################################################################
# This submits 11 jobs at a time for eigenvalues, for 10 times,    #
# hence it will generate 110 configurations in total.              #
# It takes configurations from /scratch/s.2227764.                 #
####################################################################



conf_dir="/scratch/s.2227764/conf_saved_eigen/"
ckpoint_file="ckpoint_lat."
ckpoint_num=200

module purge
module load cuda/11.4.1  openmpi/4.1.1-cuda11.4.1  ucx/1.12.0-cuda11.4.1

export LD_LIBRARY_PATH=/home/dp208/dp208/dc-forz1/grid/prefix/lib:/mnt/lustre/tursafs1/apps/basestack/cuda-11.4.1/ucx/1.12.0-cuda11.4.1/lib:/mnt/lustre/tursafs1/apps/basestack/cuda-11.4.1/openmpi/4.1.1-cuda11.4.1/lib:/mnt/lustre/tursafs1/apps/cuda/11.4.1/lib64/

for j in {0..8}
do
    for i in {0..12}
    do
        ckpoint_path="$conf_dir$ckpoint_file$ckpoint_num"
        sed -i "s|./Test_DW_Eigenvalues .*|./Test_DW_Eigenvalues $ckpoint_path --wheresave /scratch/s.2227764/Dw_stuff_new/g5Dw_Operator_$((i+j*13+1)).txt|" ./test_eigen

#        make Test_DW_Eigenvalues
        sbatch test_eigen

        ((ckpoint_num+=200))
    done

    # Wait for 2 hours and 30 minutes, time for finishing jobs
    sleep 2h 30m

    # Cancel previous jobs
    scancel --partition=accel_ai

done
