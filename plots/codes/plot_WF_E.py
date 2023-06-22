import argparse
import matplotlib.pyplot as plt
import numpy as np

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dp', action='store_true', help='Use precomputed data path')
args = parser.parse_args()

# Determine data path prefix
data_path_prefix = '../../data/WF/'
if args.dp:
    data_path_prefix = '../../precomputed_data/WF/'

# Load data from files
data1 = np.loadtxt(data_path_prefix + 'WF_b68_am-08_l8.txt')
data2 = np.loadtxt(data_path_prefix + 'WF_b68_am-08_l8_clover.txt')
data3 = np.loadtxt(data_path_prefix + 'WF_b69_am-08_l8.txt')
data4 = np.loadtxt(data_path_prefix + 'WF_b69_am-08_l8_clover.txt')

# Set up plot
fig, ax = plt.subplots()
ax.set_xlim(0, 4.7)

# Define line styles
line_style1 = 'purple'
line_style2 = '#29BCC1'
line_style3 = '#4581A9'
line_style4 = 'orange'

# Set the figure size
fig = plt.figure(figsize=(4.5, 3.0))

# Create axis object
ax = fig.add_subplot(111)

# Plot lines
ax.plot(data1[:, 0], data1[:, 1], label='$\\beta = 6.8, \\rm pl.$', color=line_style1, linewidth=3.5)
ax.plot(data2[:, 0], data2[:, 1], label='$\\beta = 6.8, \\rm cl.$', color=line_style2, linewidth=3.5)
ax.plot(data3[:, 0], data3[:, 1], label='$\\beta = 6.9, \\rm pl.$', color=line_style3, linewidth=3.5)
ax.plot(data4[:, 0], data4[:, 1], label='$\\beta = 6.9, \\rm  cl.$', color=line_style4, linewidth=3.5)

ax.set_xlabel('$t$')
ax.set_ylabel('${\cal E}(t)$')

ax.legend(loc='upper right', bbox_to_anchor=(2.15, 1.56), ncol=1)

# Add legend
ax.legend(loc='best')

# Fill curves between lines
ax.fill_between(data1[:, 0], data1[:, 1] - data1[:, 3], data1[:, 1] + data1[:, 3], color=line_style1, alpha=0.35)
ax.fill_between(data2[:, 0], data2[:, 1] - data2[:, 3], data2[:, 1] + data2[:, 3], color=line_style2, alpha=0.35)
ax.fill_between(data3[:, 0], data3[:, 1] - data3[:, 3], data3[:, 1] + data3[:, 3], color=line_style3, alpha=0.35)
ax.fill_between(data4[:, 0], data4[:, 1] - data4[:, 3], data4[:, 1] + data4[:, 3], color=line_style4, alpha=0.35)

plt.savefig('../figures/WF_b68_am-08_l8.pdf', dpi=300, bbox_inches='tight')
