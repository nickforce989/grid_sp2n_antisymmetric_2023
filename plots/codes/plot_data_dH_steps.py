import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Read data from input file
data = np.loadtxt('../../data2/dH_steps.txt')

# Extract columns
x = data[:, 0]
y = data[:, 1]
err_x = data[:, 2]
err_y = data[:, 3]

# Set the figure size
fig = plt.figure(figsize=(5, 2.5))
ax = fig.add_subplot(111)

# Plot data with error bars
ax.errorbar(x, y, xerr=err_x, yerr=err_y, fmt='o', markersize=5, capsize=3, color='black')

# Define the quartic fit function
def quartic_fit(x, A):
    return A * x**4

# Perform curve fitting to find the best value for A
best_A, _ = curve_fit(quartic_fit, x, y)

# Define x values for the line to cover the entire plot range
x_line = np.linspace(0.0, 0.080, 100)

# Evaluate the quartic fit function using the best A
y_line = quartic_fit(x_line, best_A)

# Plot the quartic fit curve with red color and solid line style
ax.plot(x_line, y_line, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([0.0, 0.080])
ax.set_ylim([-0.0007, 0.06])

ax.tick_params(axis='both', which='major', labelsize=9)

ax.set_xlabel('$\Delta \\tau$', fontsize=9)
ax.set_ylabel('$\langle \Delta H \\rangle $', fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/dH_steps.pdf', dpi=300, bbox_inches='tight')
