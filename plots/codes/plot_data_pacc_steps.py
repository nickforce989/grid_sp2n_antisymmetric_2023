import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Read data from input file
data = np.loadtxt('../../data/pacc_steps.txt')

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

# Plot the function y = erfc(sqrt(x)/2) with red color and solid line style
ax.plot(x_line, erfc(np.sqrt(x_line)/2), color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([0.0, 0.053])
ax.set_ylim([0.85, 1.0])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$\langle \Delta H \\rangle $',fontsize=9)
ax.set_ylabel('$P_{acc}$',fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/Pacc_steps.pdf', dpi=300, bbox_inches='tight')
