
import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.monospace": 'Computer Modern Roman',
    "lines.linewidth": 0.5,  # set thicker line width
    "lines.markersize" : '3',
    "lines.markeredgewidth" : '0.5',
    "errorbar.capsize" : '1.5',
    "axes.linewidth" : '0.5',
    "legend.fontsize" : 'small',
    "legend.handletextpad" : '0.3',
    "legend.columnspacing" : '0.5'
})

# Read data from input file
data = np.loadtxt('compatibilita_rhmc.txt')

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
ax.set_ylim([-0.0035, 0.0035])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$am^{\\rm as}_0$',fontsize=9)
ax.set_ylabel('$\langle P \\rangle_{\\rm HMC} - \langle P \\rangle_{\\rm RHMC} $',fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('Compatibility_rhmc.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
