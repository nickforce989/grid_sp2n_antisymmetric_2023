import matplotlib.pyplot as plt
import numpy as np
import sys

# Check if the '--dp' flag is present in the command-line arguments
use_dp = '--dp' in sys.argv

# Set the data path based on the flag
if use_dp:
    data_path = '../../precomputed_data/Nf0_data/bulktrans_nf0_sp4_2AS_1.dat'
else:
    data_path = '../../data/Nf0_data/bulktrans_nf0_sp4_2AS_1.dat'

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = ['grey']

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6.5, 4.0))

# Loop through each file
for i in range(1):
    # Read data from input file
    data = np.loadtxt(data_path)

    # Extract columns
    x = data[:, 0]
    y = data[:, 1]

    # Plot data with lines connecting points and using different color for each file
    ax.plot(x, y, color=colors[i], linestyle='-', linewidth=1.5, marker='o', markersize=3)

# Add horizontal red line at y=0
#ax.axhline(y=0.535717, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([0, 18])
ax.set_ylim([0, 1.0])

ax.tick_params(axis='both', which='major', labelsize=11)

ax.set_xlabel('$\\beta$', fontsize=11)
ax.set_ylabel('$\langle P \\rangle $', fontsize=11)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/bulktrans_puregauge.pdf', dpi=300, bbox_inches='tight')
