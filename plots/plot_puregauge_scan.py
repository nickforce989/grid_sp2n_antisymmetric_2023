import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.monospace": 'Computer Modern Roman',
    "lines.linewidth": 1.5,  # set thicker line width to 1.5
    "lines.markersize" : 3,
    "lines.markeredgewidth" : 0.5,
    "errorbar.capsize" : 1.5,
    "legend.fontsize" : 10,  # Set the legend font size to 11 points
    "axes.linewidth" : 0.5,
    "legend.handletextpad" : 0.3,
    "legend.columnspacing" : 0.5
})

# Define a list of colors for each file
colors = ['grey']

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6.5, 4.0))

# Loop through each file
for i in range(1):
    # Read data from input file
    data = np.loadtxt(f'bulktrans_nf0_sp4_{i+1}.dat')  # assuming files are named as bulktrans_sp4_2AS_b56_1.dat, bulktrans_sp4_2AS_b56_2.dat, etc.

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

ax.set_xlabel('$\\beta$',fontsize=11)
ax.set_ylabel('$\langle P \\rangle $',fontsize=11)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('bulktrans_puregauge.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
