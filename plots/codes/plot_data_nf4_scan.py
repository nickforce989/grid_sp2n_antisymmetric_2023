import matplotlib.pyplot as plt
import numpy as np
import sys

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = ['purple', 'blue', 'green', 'grey', 'indigo', 'magenta', 'yellow', 'black', 'brown', 'orange']

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6.5, 4.0))

# Check if the '--dp' flag is present in the command line arguments
use_dp_flag = '--dp' in sys.argv

# Define the base path for data files
base_path = '../../data/Nf4_data/'
if use_dp_flag:
    base_path = '../../precomputed_data/Nf4_data/'

# Get betas from command line arguments and sort them
betas = sorted([float(beta) for beta in sys.argv[1:] if not beta.startswith('--')])

# Loop through each file
for i, beta in enumerate(betas):
    # Construct the path based on the flag and beta index
    file_path = base_path + f'bulktrans_nf4_sp4_2AS_{i+1}.dat'

    # Read data from input file
    data = np.loadtxt(file_path)

    # Extract columns
    x = data[:, 0]
    y = data[:, 1]

    # Plot data with lines connecting points and using different color for each file
    ax.plot(x, y, color=colors[i], linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'${beta}$')

# Add horizontal red line at y=0
#ax.axhline(y=0.535717, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([-1.45, 0.05])
ax.set_ylim([0.345, 0.74])

ax.tick_params(axis='both', which='major', labelsize=11)

ax.set_xlabel('$am^{\\rm as}_0$', fontsize=11)
ax.set_ylabel('$\langle P \\rangle $', fontsize=11)

# Add legend with two columns and title
legend = ax.legend(ncol=2, title='$\\beta$')
legend.get_title().set_fontsize('10')

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/bulktrans_nf4_2AS_all.pdf', dpi=300, bbox_inches='tight')
