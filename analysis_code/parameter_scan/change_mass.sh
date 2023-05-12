#!/bin/bash

####################################################################
# This variates the masses for one fixed value of beta, for the    #
# parameter scan.                                                  #
####################################################################

if [[ $# -eq 0 ]] ; then
    echo 'Please provide a value for beta and Nf_2AS_flavours as an argument'
    exit 1
fi

# Replace this value of beta
sed -i "s/--beta [^\\ ]*/--beta $1/" test

# Load Modules
module load compiler/gnu/10/2.0
module load CUDA/11.7

export LD_LIBRARY_PATH=/home/s.2227764/sympl_grid_modified/prefix/lib:${LD_LIBRARY_PATH}

# Loop for ASmass
for ASmass in $(seq -f "%.1f" -1.4 0.1 0.0); do
    if (( $(echo "$ASmass > -1.0" | bc -l) )); then
        n=$(echo "-10 * $ASmass" | bc | awk '{printf("%d", $1)}')
        n="0$n"
    else
        n=$(echo "-10 * $ASmass" | bc | awk '{printf("%d", $1)}')
    fi

    # Replace the last line of the file called 'test'
    beta_times_10=$(echo "$1*10" | bc | awk '{printf("%d", $1)}')
    sed -i "\$s/.*/    --Thermalizations 100 > .\/Nf4_tests\/hmc_\${SLURM_JOB_ID}-b${beta_times_10}_am-$n.out/" test

    # Replace the value of ASmass
    sed -i "s/--fermionmass [^\\ ]*/--fermionmass $ASmass/" test

    # Compile the code
#    make Test_hmc_Sp_Wilson_$2_2ASFermionGauge

    # Launch the job
    sbatch test
done

