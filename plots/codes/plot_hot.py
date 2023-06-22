import argparse
import matplotlib.pyplot as plt
import numpy as np

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dp1', action='store_true', help='Toggle dp1 file path')
parser.add_argument('--dp2', action='store_true', help='Toggle dp2 file path')
args = parser.parse_args()

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = ['magenta', 'indigo', 'grey', 'green', 'blue', 'purple']
# Define a list of beta values
betas = [5.6, 5.8, 6.0, 6.2, 6.3, 6.4]

# Create a figure with 3 rows and 2 columns of subplots
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(8.5, 7))
# Flatten the axs array for easy iteration
axs = axs.flatten()

# Create 6 different plots
for i in range(6):
    # Construct file paths based on the dp flags
    dp1 = '../../precomputed_data/Nf4_data/bulktrans_nf4_sp4_2AS_' if args.dp1 else '../../data/Nf4_data/bulktrans_nf4_sp4_2AS_'
    dp2 = '../../precomputed_data/Nf4_hot/bulktrans_sp4_2AS_hot_' if args.dp2 else '../../data/Nf4_hot/bulktrans_sp4_2AS_hot_'
    data1 = np.loadtxt(f'{dp1}{5-i+1}.dat')
    data2 = np.loadtxt(f'{dp2}{5-i+1}.dat')

    # Extract columns
    x1 = data1[:, 0]
    y1 = data1[:, 1]
    x2 = data2[:, 0]
    y2 = data2[:, 1]

    # Plot data1 with lines connecting points and using different color for each file
    axs[i].plot(x1, y1, color=colors[i], linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'$\\beta = {betas[i]}$')
    # Plot data2 with lines connecting points and using red color
    axs[i].plot(x2, y2, color='red', linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'$\\beta = {betas[i]}$ (Hot)')

    # Remove x ticks on the bottom plots
    if i == 4 or i == 5:
        axs[i].set_xticks([-1.5, -1.0, -0.5, 0.0])
        axs[i].tick_params(axis='x', labelsize=14)
    else:
        axs[i].tick_params(axis='x', labelbottom=False)

    # Customize x and y ranges
    axs[i].set_xlim([-1.5, 0.05])
    axs[i].set_ylim([0.345, 0.74])
    axs[i].tick_params(axis='both', which='major', labelsize=14)

    if i == 0 or i == 2 or i == 4:
        # Remove y ticks on the rightmost plots
        axs[i].tick_params(axis='y', labelright=False)
        axs[i].set_xlabel('')
    else:
        # Remove y ticks on all other plots
        axs[i].tick_params(axis='y', labelleft=False)
        axs[i].set_xlabel('')

# Add shared x and y axis labels to the figure
fig.text(0.5, -0.0115, '$am^{\\rm as}_0$', ha='center', fontsize=14)
fig.text(-0.02, 0.5, '$\\langle P \\rangle $', va='center', rotation='vertical', fontsize=14)

# Add a tight layout to the figure to eliminate any white space
fig.tight_layout()

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/bulktrans_plots.pdf', dpi=300, bbox_inches='tight')
