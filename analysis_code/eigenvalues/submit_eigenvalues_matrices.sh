#!/bin/bash

####################################################################
# This submits 11 jobs at a time for eigenvalues, for 10 times,    #
# hence it will generate 110 configurations in total.              #
# It takes configurations from /scratch/s.2227764.                 #
# NB: g5DwOperator has to be set to 0 initially!!!                 #
####################################################################



conf_dir="/scratch/s.2227764/conf_saved_eigen/"
ckpoint_file="ckpoint_lat."
ckpoint_num=200

module load compiler/gnu/10/2.0
module load CUDA/11.7

export LD_LIBRARY_PATH=/home/s.2227764/sympl_grid_modified/prefix/lib:${LD_LIBRARY_PATH}

for j in {0..10}
do
    for i in {0..11}
    do
       sed -i "s/std::ofstream outFile(\"\/scratch\/s.2227764\/Dw_stuff_new\/g5Dw_Operator_$((i+j*12)).txt\");/std::ofstream outFile(\"\/scratch\/s.2227764\/Dw_stuff_new\/g5Dw_Operator_$((i+j*12+1)).txt\");/g" ../../../tests/sp2n/Test_DW_Eigenvalues.cc


        ckpoint_path="$conf_dir$ckpoint_file$ckpoint_num"
        sed -i "s|./Test_DW_Eigenvalues .*|./Test_DW_Eigenvalues $ckpoint_path|" ./test_eigen

        make Test_DW_Eigenvalues
        sbatch test_eigen

        ((ckpoint_num+=200))
    done

    # Wait for 2 hours and 30 minutes
    sleep 2h 30m

    # Cancel previous jobs
    scancel --partition=accel_ai

done
