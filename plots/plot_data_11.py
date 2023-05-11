import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.monospace": 'Computer Modern Roman',
    "lines.linewidth": 0.5,  # set thicker line width
    "lines.markersize": 3,
    "lines.markeredgewidth": 0.5,
    "errorbar.capsize": 1.5,
    "axes.linewidth": 0.5,
    "legend.fontsize": 'small',
    "legend.handletextpad": 0.3,
    "legend.columnspacing": 0.5
})

# Read data from input files
data1 = np.loadtxt('susceptibility_b65_nf4_vol8.txt')
data2 = np.loadtxt('susceptibility_b65_nf4_vol16.txt')

# Extract columns for dataset 1
x1 = data1[:, 0]
y1 = data1[:, 1]
err_x1 = data1[:, 2]
err_y1 = data1[:, 3]

# Extract columns for dataset 2
x2 = data2[:, 0]
y2 = data2[:, 1]
err_x2 = data2[:, 2]
err_y2 = data2[:, 3]

# Set the figure size
fig = plt.figure(figsize=(5, 3.0))

# Create axis object
ax = fig.add_subplot(111)

# Plot dataset 1 with error bars in red
ax.errorbar(x1, y1, yerr=err_y1, fmt='o', markersize=5, capsize=3, color='red', label='$\\tilde{V}=(8a)^4$')

# Plot dataset 2 with error bars in purple
ax.errorbar(x2, y2, yerr=err_y2, fmt='o', markersize=5, capsize=3, color='purple', label='$\\tilde{V}=(16a)^4$')

# Add horizontal red line at y=0
#ax.axhline(y=0.535717, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([-1.02, -0.90])
ax.set_ylim([0.0, 0.2])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$am^{\\rm as}_0$', fontsize=9)
ax.set_ylabel('$\chi_P $', fontsize=9)

# Add legend
ax.legend(loc='best')

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('susceptibility_b65.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
