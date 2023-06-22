from pylab import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dp', action='store_true', help='Use precomputed data path')
args = parser.parse_args()

# Define the base data path
base_path = '../../data/polyakov_loops/output_l'

# Update the data path if --dp flag is provided
if args.dp:
    base_path = '../../precomputed_data/polyakov_loops/output_l'

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Create a new figure with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(7.5, 4.5))

# Define an array of titles
titles = ["$\\tilde{{V}} = ({2}a)^4$", "$\\tilde{{V}} = ({4}a)^4$", "$\\tilde{{V}} = ({12}a)^4$", "$\\tilde{{V}} = ({20}a)^4$"]

# Read the four images and plot them in the corresponding axes
for i, filename in enumerate(['2_polyloop.txt', '4_polyloop.txt', '12_polyloop.txt', '20_polyloop.txt']):
    # Construct the full file path
    file_path = base_path + filename
    
    # Read the data from the file
    with open(file_path, 'r') as f:
        data = [float(line.strip()) for line in f]
    
    # Plot the data in the corresponding axis
    row = i // 2
    col = i % 2
    ax = axs[row, col]
    Nbins = 80
    y, x, _ = ax.hist(data, Nbins, color='blue', alpha=0.4, density=True, edgecolor="black")
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
