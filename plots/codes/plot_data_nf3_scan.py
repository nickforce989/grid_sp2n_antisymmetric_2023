import matplotlib.pyplot as plt
import numpy as np
import sys

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = [(0.8, 0.6, 0.8), (0.9, 0.5, 0.5), (0.5, 0.7, 0.9), (0.9, 0.7, 0.5), 
          (0.5, 0.5, 0.5), (0.3, 0.3, 0.3), (0.7, 0.6, 0.4), (0.3, 0.2, 0.1)]

# Check if flag '--dp' is present
use_dp = False
if "--dp" in sys.argv:
    use_dp = True

# Define the base path depending on the flag
base_path = "../../data/Nf3_data/"
if use_dp:
    base_path = "../../precomputed_data/Nf3_data/"


# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6, 3.5))

# Define a list of beta values
betas = [5.8, 6.0, 6.2, 6.4, 6.5, 6.6, 6.7, 6.8]

# Loop through each file
for i in range(8):
    # Construct the path based on the flag
    data_path = f"{base_path}bulktrans_nf3_sp4_2AS_{i+1}.dat"

    # Read data from input file
    data = np.loadtxt(data_path)
    # Extract columns
    x = data[:, 0]
    y = data[:, 1]

    # Plot data with lines connecting points and using different color for each file
    ax.plot(x, y, color=colors[i], linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'${betas[i]}$')

# Add horizontal red line at y=0
#ax.axhline(y=0.535717, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([-1.45, 0.05])
ax.set_ylim([0.345, 0.74])

ax.tick_params(axis='both', which='major', labelsize=11)

ax.set_xlabel('$am^{\\rm as}_0$',fontsize=11)
ax.set_ylabel('$\langle P \\rangle $',fontsize=11)

# Add legend with two columns and title
legend = ax.legend(ncol=2, title='$\\beta$')
legend.get_title().set_fontsize('10')

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/bulktrans_nf3_2AS_all.pdf', dpi=300, bbox_inches='tight')
