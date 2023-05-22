#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <Number of flavours> <Beta1> <Beta2> ..."
  exit 1
fi

# Set the number of flavors
num_flavours=$1

# Remove the number of flavors and store the beta values in an array
shift
beta_values=("$@")

# Function to check if all jobs are completed
function check_jobs_completed() {
  local job_names=("test1" "test2" "test3" "test4")
  for job_name in "${job_names[@]}"; do
    if squeue -u dc-forz1 --name="$job_name" &>/dev/null; then
      return 1
    fi
  done
  return 0
}

# Loop through each beta value
for beta in "${beta_values[@]}"; do
  # Launch substitute_beta.sh with current beta value and number of flavors
  bash substitute_beta.sh "$num_flavours" "$beta"
  sbatch test1
  sbatch test2
  sbatch test3
  sbatch test4

  # Wait for the completion of all jobs
  while ! check_jobs_completed; do
    sleep 10
  done

  # Change the beta value
  echo "Changing beta value..."
done

