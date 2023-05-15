from pylab import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Create a new figure with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(7.5, 4.5))

# Define an array of titles
titles = ["$\\tilde{{V}} = ({2}a)^4$","$\\tilde{{V}} = ({8}a)^4$","$\\tilde{{V}} = ({16}a)^4$","$\\tilde{{V}} = ({20}a)^4$"]

# Read the four images and plot them in the corresponding axes
for i, file in enumerate(['../../data/output_vol2_b9_4.txt', '../../data/output_vol4_b9_3.txt', '../../data/output_vol12_b9_4.txt', '../../data/output_vol20_b9_4.txt']):
    # Read the data from the file
    with open(file, 'r') as f:
        data = [float(line.strip()) for line in f]
    # Plot the data in the corresponding axis
    row = i // 2
    col = i % 2
    ax = axs[row, col]
    Nbins = 100
    y, x, _ = ax.hist(data, Nbins, color='blue', alpha=.4, density=True, edgecolor="black")
    erry = np.sqrt(y)
    x = (x[1:] + x[:-1]) / 2  # for len(x)==len(y)
    ax.set_title(titles[i], fontsize=8)  # index titles array
    ax.set_xlabel("", fontsize=8)
    ax.set_ylabel("", fontsize=8)
    
# Set the x and y labels for the bottom center plot
fig.text(0.5, 0.04, '$\Phi$', ha='center', fontsize=9)
fig.text(0.06, 0.5, 'Frequency', va='center', rotation='vertical', fontsize=8)

# Adjust the spacing between the subplots
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/Polyloops_merged.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
