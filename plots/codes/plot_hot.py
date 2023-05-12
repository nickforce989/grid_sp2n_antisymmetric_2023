import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Define a list of colors for each file
colors = ['magenta', 'indigo', 'grey', 'green', 'blue', 'purple']
# Define a list of beta values
betas = [5.6, 5.8, 6.0, 6.2, 6.3, 6.4]

# Create a figure with 3 rows and 2 columns of subplots
fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(8.5, 7))
# Flatten the axs array for easy iteration
axs = axs.flatten()

# Create 6 different plots
for i in range(6):
    # Read data from input files
    data1 = np.loadtxt(f'bulktrans_sp4_2AS_{5-i+1}.dat')
    data2 = np.loadtxt(f'bulktrans_sp4_2AS_hot_{5-i+1}.dat')

    # Extract columns
    x1 = data1[:, 0]
    y1 = data1[:, 1]
    x2 = data2[:, 0]
    y2 = data2[:, 1]

    # Plot data1 with lines connecting points and using different color for each file
    axs[i].plot(x1, y1, color=colors[i], linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'$\\beta = {betas[i]}$')
    # Plot data2 with lines connecting points and using red color
    axs[i].plot(x2, y2, color='red', linestyle='-', linewidth=1.5, marker='o', markersize=3, label=f'$\\beta = {betas[i]}$ (Hot)')

    # Add horizontal red line at y=0
#   axs[i].axhline(y=0.535717, color='red', linestyle='-')

    # Remove x ticks on the bottom plots
    if i == 4 or i == 5:
        axs[i].set_xticks([-1.5, -1.0, -0.5, 0.0])
        axs[i].tick_params(axis='x', labelsize=14)
    else:
        axs[i].tick_params(axis='x', labelbottom=False)


    # Customize x and y ranges
    axs[i].set_xlim([-1.5, 0.05])
    axs[i].set_ylim([0.345, 0.74])

    axs[i].tick_params(axis='both', which='major', labelsize=14)

    if i == 0 or i == 2 or i == 4:
        # Remove y ticks on the rightmost plots
        axs[i].tick_params(axis='y', labelright=False)
        axs[i].set_xlabel('')
    else:
        # Remove y ticks on all other plots
        axs[i].tick_params(axis='y', labelleft=False)
        axs[i].set_xlabel('')
        

    

#    ax.set_xlabel('$am^{\\rm as}_0$', fontsize=11)
 #   ax.set_ylabel('$\\langle P \\rangle $', fontsize=11)

# Add shared x and y axis labels to the figure
fig.text(0.5, -0.0115, '$am^{\\rm as}_0$', ha='center', fontsize=14)
fig.text(-0.02, 0.5, '$\\langle P \\rangle $', va='center', rotation='vertical', fontsize=14)

# Add a tight layout to the figure to eliminate any white space
fig.tight_layout()

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('bulktrans_plots.pdf', dpi=300, bbox_inches='tight')    
    
