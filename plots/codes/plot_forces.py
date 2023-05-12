import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

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

# Define the values for each plot
y_values_list = [
    [7.50914940330241, 11.130037903372],
    [7.50914940330241, 8.05618854289439],
    [7.50914940330241, 6.53331114256598],
    [7.50914940330241, 4.97905440935509],
    [7.50914940330241, 1.43521564137167],
    [7.50914940330241, 0.502597809352699]
]

# Set the figure size
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(10, 8), sharey=True, sharex=True)

# Create axis objects
axs = axs.ravel()

# Loop through the plots and plot each one
for i, y_values in enumerate(y_values_list):
    
    # make data:
    x_labels = ['Gauge', '2-AS (HMC)']

    # plot
    axs[i].bar(x_labels, y_values, width=0.7, edgecolor="black", linewidth=0.7, color=colors)

    # Set the y-axis limits and ticks
    axs[i].set(ylim=(0, 15), yticks=np.arange(0, 15, 2), title='')

    # Set the y-axis tick labels
    yticklabels = [f"{val:.0f}" for val in np.arange(0, 15, 2)]
    axs[i].set_yticklabels(yticklabels, fontsize=9)

    # Set font size of x-axis labels
    plt.setp(axs[i].get_xticklabels(), fontsize=9)
    # Set x-axis labels only for the bottom row of subplots
    if i >= 4:
        axs[-2].set_xlabel('')

# Add a label on the y-axis for all subplots
fig.text(0.06, 0.5, 'MD Force', fontsize=9, va='center', rotation='vertical')

# Set the figure size before saving
fig.set_size_inches(6, 4)


# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('forces.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
