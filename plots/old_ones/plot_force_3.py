import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

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

# Define a custom color map
colors = plt.cm.Purples(np.linspace(0.3, 0.9, 2))

# Define a custom style
plt.style.use({
    'axes.facecolor': '#f5f5f5',
    'axes.edgecolor': 'black',
    'axes.grid': False,
    'grid.color': 'black',
    'xtick.bottom': True,
    'xtick.color': 'black',
    'ytick.color': 'black'
})

# make data:
x_labels = ['Gauge', '2-AS (HMC)']
y_values = [7.50914940330241,6.53331114256598]

# Set the figure size
fig = plt.figure(figsize=(5, 4.0))

# Create axis object
ax = fig.add_subplot(111)


# plot
fig, ax = plt.subplots()

ax.bar(x_labels, y_values, width=0.7, edgecolor="black", linewidth=0.7, color=colors)

# Add labels above each box
#for i in range(len(x_labels)):
#    ax.text(x_labels[i], y_values[i]+0.1, str(y_values[i]), ha='center', va='bottom')

ax.set(ylim=(0, 15), yticks=np.arange(0, 15, 1),
       xlabel='', ylabel='MD Force',
       title='')

# Add a label on the y-axis
ax.set_ylabel('MD Force', fontsize=11)

# Set the figure size before saving
fig.set_size_inches(5, 3.0)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('forces_am+06.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
