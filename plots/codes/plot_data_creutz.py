
import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Read data from input file
data = np.loadtxt('../../data2/expdh.txt')

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
ax.errorbar(x, y, xerr=err_x, yerr=err_y, fmt='o', markersize=5, capsize=3, color='black')

# Add horizontal red line at y=0
ax.axhline(y=1.0, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([0.035, 0.075])
ax.set_ylim([0.970, 1.020])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$\Delta \\tau$',fontsize=9)
ax.set_ylabel('$\langle \exp(-\Delta H) \\rangle $',fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/creutz.pdf', dpi=300, bbox_inches='tight')
