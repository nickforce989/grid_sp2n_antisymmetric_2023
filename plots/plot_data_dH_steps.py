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
data = np.loadtxt('dH_steps.txt')

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

# Define x values for the line to cover the entire plot range
x_line = np.linspace(0.0, 0.080, 100)  # 100 points for smoother line

# Plot the function y=1599.26*x^4 with red color and solid line style
ax.plot(x_line, 1599.26*x_line**4, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([0.0, 0.080])
ax.set_ylim([-0.002, 0.06])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$\Delta \\tau$',fontsize=9)
ax.set_ylabel('$\langle \Delta H \\rangle $',fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('dH_steps.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
