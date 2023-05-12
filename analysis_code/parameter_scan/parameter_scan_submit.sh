#!/bin/bash

#################################################################
# Cycle over beta values and scan the mass parameters.          #
# For each beta listed, we scan the masses.                     #
# We do one-beta masses, wait them to finish, and then launch   #
# the new ones.                                                 #
#################################################################

# Define the values of beta to loop over
betas=(6.6 6.7 6.8 6.9 7.0 7.1)

# Number of flavours for 2AS fermions
nf=4

for beta in "${betas[@]}"
do
  # Variate mass
  bash change_mass.sh $beta $nf

  # Wait for all jobs to complete, supposed to last 6 hours
  sleep 6h
done

