import matplotlib.pyplot as plt
import numpy as np
import argparse

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dp', action='store_true', help='Use alternative data file path')
args = parser.parse_args()

# Set data file path based on the flag
data_file_path = '../../data/rhmc_compatibilities/compatibilita_rhmc.txt'
if args.dp:
    data_file_path = '../../precomputed_data/rhmc_compatibilities/compatibilita_rhmc.txt'

# Read data from input file
data = np.loadtxt(data_file_path)

# Rest of the code remains the same...
# Extract columns
x = data[:, 0]
y = data[:, 1]
err_x = data[:, 2]
err_y = data[:, 3]

# Set the figure size
fig = plt.figure(figsize=(5, 2.5))

# Create axis object
ax = fig.add_subplot(111)

# Plot data with error bars
ax.errorbar(x, y, xerr=err_x, yerr=err_y, fmt='o', markersize=5, capsize=3, color='blue')

# Add horizontal red line at y=0
ax.axhline(y=0.0, color='black', linestyle='-')

# Customize x and y ranges
ax.set_xlim([-1.5, 0.1])
ax.set_ylim([-0.0025, 0.0025])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$am^{\\rm as}_0$', fontsize=9)
ax.set_ylabel('$\langle P \\rangle_{\\rm HMC} - \langle P \\rangle_{\\rm RHMC} $', fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/Compatibility_rhmc.pdf', dpi=300, bbox_inches='tight')
