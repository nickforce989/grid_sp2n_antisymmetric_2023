import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import sys

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Check if the flag '--dp' is provided
use_custom_path = '--dp' in sys.argv

# Define the data path based on the flag
if use_custom_path:
    data_path = '../../precomputed_data/initial_tests/dH_steps.txt'
else:
    data_path = '../../data/initial_tests/dH_steps.txt'

# Read data from input file
data = np.loadtxt(data_path)

# Extract columns
x = data[:, 0]
y = data[:, 1]
err_x = data[:, 2]
err_y = data[:, 3]

# Set the figure size
fig = plt.figure(figsize=(5, 2.5))
ax = fig.add_subplot(111)

# Plot data with error bars on a logarithmic scale
ax.errorbar(x, y, xerr=err_x, yerr=err_y, fmt='o', markersize=5, capsize=3, color='black')
ax.set_yscale('log')
ax.set_xscale('log')

# Define the quartic fit function in logarithmic space
def log_quartic_fit(log_x, log_A, log_B):
    return log_A + log_B * log_x

# Convert x and y to logarithmic space
log_x = np.log10(x)
log_y = np.log10(y)

# Perform curve fitting to find the best values for log_A and log_B
best_log_A, best_log_B = curve_fit(log_quartic_fit, log_x, log_y)[0]

# Calculate errors of the fit parameters
cov = curve_fit(log_quartic_fit, log_x, log_y)[1]
fit_errors = np.sqrt(np.diag(cov))

# Define x values for the line to cover the entire plot range
log_x_line = np.linspace(np.log10(0.035), np.log10(0.080), 100)

# Evaluate the logarithmic quartic fit function using the best log_A and log_B
log_y_line = log_quartic_fit(log_x_line, best_log_A, best_log_B)

# Convert back to linear space
y_line = 10**log_y_line

# Plot the quartic fit curve with red color and solid line style on a logarithmic scale
ax.semilogy(10**log_x_line, y_line, color='red', linestyle='-')

# Customize x and y ranges
ax.set_xlim([0.035, 0.080])
ax.set_ylim([1e-4, 1])

ax.tick_params(axis='both', which='major', labelsize=9)

# Customize x-axis tick labels to direct notation
ticks = [0.040, 0.050, 0.060, 0.070, 0.080]
ax.set_xticks(ticks)
ax.set_xticklabels([f'{tick:.3f}' for tick in ticks])

ax.set_xlabel('$\Delta \\tau$', fontsize=8)
ax.set_ylabel('$\langle \Delta H \\rangle $', fontsize=8)

# Calculate reduced chi-square
residuals = y - 10**log_quartic_fit(log_x, best_log_A, best_log_B)
reduced_chi_square = np.sum((residuals / err_y) ** 2) / (len(x) - 1)

# Print the parameters, errors, and reduced chi-square
print("Best fit parameters:")
print("log_A:", best_log_A)
print("log_B:", best_log_B)
print("Fit errors:")
print("log_A error:", fit_errors[0])
print("log_B error:", fit_errors[1])
print("Reduced chi-square:", reduced_chi_square)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/dH_steps.pdf', dpi=300, bbox_inches='tight')
