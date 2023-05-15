import sys

# Read in unfolded_dist.txt
with open('../../data/unfolded_dist.txt', 'r') as f:
    unfolded_dist = list(map(float, f.readlines()))
   
# Sort the list in ascending order
unfolded_dist_sorted = sorted(unfolded_dist)

# Assign an integer position to each value in the list
position_dict = {}
for i, value in enumerate(unfolded_dist_sorted):
    position_dict[value] = i+1

# Loop through the command line arguments and process each file
for file_name in sys.argv[1:]:
    with open(file_name, 'r') as f:
        file_data = list(map(float, f.readlines()))
       
    # Assign integer positions to values in the file
    positions = [position_dict[value] for value in file_data]
   
    # Write the positions to a new file with the same name but "_2" added
    with open(file_name[:-4] + "_2.txt", 'w') as f:
        for pos in positions:
            f.write(str(pos) + '\n')

