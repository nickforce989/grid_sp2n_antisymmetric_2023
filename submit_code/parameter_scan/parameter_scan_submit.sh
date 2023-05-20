#!/bin/bash

#####################################################################
# Cycle over beta values and scan the mass parameters.              #
# For each beta listed, we scan the masses.                         #
# We do one-beta masses, wait for them to finish, and then launch   #
# the new ones.                                                     #
#####################################################################

# Ask for beta values
read -p "Enter the beta values (space-separated): " -a betas

# Check if betas are provided
if [ ${#betas[@]} -eq 0 ]; then
  echo "No beta values provided."
  exit 1
fi

# Ask for the number of flavors
read -p "Enter the number of flavors: " nf

# Loop over the provided beta values
for beta in "${betas[@]}"
do
  # Variate mass
  bash change_mass.sh "$beta" "$nf"

  # Wait for all jobs to complete, supposed to last 6 hours
  sleep 6h
done

