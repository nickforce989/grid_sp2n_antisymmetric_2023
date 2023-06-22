import matplotlib.pyplot as plt
import numpy as np
import sys

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = [(0.8, 0.2, 0.8), (0.0, 0.0, 0.0), (0.0, 0.6, 1.0), (1.0, 0.5, 0.0), (0.0, 1.0, 0.0), (1.0, 0.75, 0.79), (1.0, 0.843, 0.0), (0.0, 0.1, 0.5)]

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(6, 3.5))

# Define a list of beta values
betas = [5.8, 6.0, 6.1, 6.2, 6.3, 6.4]

# Check if "--dp" flag is present
use_dp_flag = "--dp" in sys.argv

# Define the base path
base_path = "../../data/Nf6_data/"

if use_dp_flag:
    base_path = "../../precomputed_data/Nf6_data/"

# Loop through each file
for i in range(6):
    # Read data from input file
    data = np.loadtxt(f"{base_path}bulktrans_nf6_sp4_2AS_{i+1}.dat")

    # Extract columns
    x = data[:, 0]
    y = data[:, 1]

    # Plot data with lines connecting points and using different color for each file
    ax.plot(x, y, color=colors[i], linestyle="-", linewidth=1.5, marker="o", markersize=3, label=f"${betas[i]}$")

# Add horizontal red line at y=0
# ax.axhline(y=0.535717, color="red", linestyle="-")

# Customize x and y ranges
ax.set_xlim([-1.45, 0.05])
ax.set_ylim([0.345, 0.74])

ax.tick_params(axis="both", which="major", labelsize=11)

ax.set_xlabel("$am^{\\rm as}_0$", fontsize=11)
ax.set_ylabel("$\langle P \\rangle $", fontsize=11)

# Add legend with two columns and title
legend = ax.legend(ncol=2, title="$\\beta$")
legend.get_title().set_fontsize("10")

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig("../figures/bulktrans_nf6_2AS_all.pdf", dpi=300, bbox_inches="tight")
