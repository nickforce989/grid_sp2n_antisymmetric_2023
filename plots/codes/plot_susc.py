import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Read data from input files
data1 = np.loadtxt('susceptibility_b62_nf4_vol8.txt')
data2 = np.loadtxt('susceptibility_b62_nf4_vol16.txt')

data3 = np.loadtxt('susceptibility_b65_nf4_vol8.txt')
data4 = np.loadtxt('susceptibility_b65_nf4_vol16.txt')

# Extract columns for dataset 1
x1 = data1[:, 0]
y1 = data1[:, 1]
err_x1 = data1[:, 2]
err_y1 = data1[:, 3]

# Extract columns for dataset 2
x2 = data2[:, 0]
y2 = data2[:, 1]
err_x2 = data2[:, 2]
err_y2 = data2[:, 3]

# Extract columns for dataset 1
x3 = data3[:, 0]
y3 = data3[:, 1]
err_x3 = data3[:, 2]
err_y3 = data3[:, 3]

# Extract columns for dataset 2
x4 = data4[:, 0]
y4 = data4[:, 1]
err_x4 = data4[:, 2]
err_y4 = data4[:, 3]


# Set the figure size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.0))

# Plot dataset 1 with error bars in red
ax1.errorbar(x1, y1, yerr=err_y1, fmt='o', markersize=5, capsize=3, color='red', label='$\\tilde{V}=(8a)^4$')

# Plot dataset 2 with error bars in purple
ax1.errorbar(x2, y2, yerr=err_y2, fmt='o', markersize=5, capsize=3, color='purple', label='$\\tilde{V}=(16a)^4$')

# Customize x and y ranges
ax1.set_xlim([-1.20, -1.00])
ax1.set_ylim([0.0, 0.45])


# Create axis object for second subplot
#ax2 = fig.add_subplot(122)

# Plot dataset 3 with error bars in blue
ax2.errorbar(x3, y3, yerr=err_y3, fmt='s', markersize=5, capsize=3, color='red', label='$\\tilde{V}=(8a)^4$')

# Plot dataset 4 with error bars in green
ax2.errorbar(x4, y4, yerr=err_y4, fmt='s', markersize=5, capsize=3, color='purple', label='$\\tilde{V}=(16a)^4$')

# Add horizontal blue line at y=0
#ax2.axhline(y=0.365243, color='blue', linestyle='-')

# Customize x and y ranges
ax2.set_xlim([-1.02, -0.90])
ax2.set_ylim([0.0, 0.20])

ax2.tick_params(axis='both', which='major', labelsize=9)

fig.text(0.5, -0.05, '$am^{\\rm as}_0$', ha='center', fontsize=9)
ax1.set_ylabel('$\\chi_P$', fontsize=9, labelpad=10, rotation=90)

# Add legend
ax2.legend(loc='best')

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('susceptibilities.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
