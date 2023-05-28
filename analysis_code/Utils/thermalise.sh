#!/bin/bash

# Check if both the input filename and the number of lines to omit are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_filename> <lines_to_omit>"
  exit 1
fi

# Store the input filename and the number of lines to omit from the command line arguments
input_file="$1"
n="$2"

# Remove the first n lines from the input file
tail -n +$((n+1)) "$input_file" > temp.txt && mv temp.txt "$input_file"
