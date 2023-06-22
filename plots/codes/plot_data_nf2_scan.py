import argparse
import matplotlib.pyplot as plt
import numpy as np

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('betas', type=float, nargs=6, help='List of beta values')
parser.add_argument('--dp', action='store_true', help='Use different path')
args = parser.parse_args()

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = [(0.3, 0.0, 0.4), (0.6, 0.1, 0.1), (0.1, 0.2, 0.5), (0.7, 0.4, 0.1), 
          (0.4, 0.4, 0.4), (0.8, 0.8, 0.8)]

# Define the base path for data files
base_path = '../../data/Nf2_data/'

# Check if the --dp flag is provided
if args.dp:
    base_path = '../../precomputed_data/Nf2_data/'

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6, 3.5))

# Loop through each file
for i, beta in enumerate(args.betas):
    # Read data from input file
    data = np.loadtxt(f'{base_path}bulktrans_nf2_sp4_2AS_{i+1}.dat')

    # Extract columns
    x = data[:, 0]
    y = data[:, 1]

    # Plot data with lines connecting points and using different color for each file
    ax.plot(x, y, color=colors[i], linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'${beta}$')

# Add horizontal red line at y=0
# ax.axhline(y=0.535717, color='red', linestyle='-')

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
plt.savefig('../figures/bulktrans_nf2_2AS_all.pdf', dpi=300, bbox_inches='tight')
