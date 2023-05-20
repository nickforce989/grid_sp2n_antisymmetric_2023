#!/bin/bash

# Directory containing the txt files
directory="../../data/"

# Loop through each txt file starting with 'eigenvalues'
for file in "$directory"/eigenvalues*.txt; do
  # Check if file exists
  if [ -e "$file" ]; then
    # Get the total number of lines in the file
    total_lines=$(wc -l < "$file")
    
    # Calculate the number of lines to remove from both the beginning and end
    lines_to_remove=200
    
    # Ensure that the file has more than 400 lines before proceeding
    if [ "$total_lines" -gt $((lines_to_remove * 2)) ]; then
      # Remove the first 200 lines and the last 200 lines from the file
      tail -n $(($total_lines - lines_to_remove)) "$file" | head -n -$lines_to_remove > "$file.temp"
      
      # Replace the original file with the temporary file
      mv "$file.temp" "$file"
      
      echo "Processed: $file"
    else
      echo "Skipping: $file (not enough lines)"
    fi
  else
    echo "Skipping: $file (not found)"
  fi
done

