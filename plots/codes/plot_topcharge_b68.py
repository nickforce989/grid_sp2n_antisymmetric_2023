import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Load data from first file
data1 = np.loadtxt('../../data/top_charges_b68-am08_with_index.txt')
x = data1[:, 0]
y = data1[:, 1]


# Create first plot
fig, ax1 = plt.subplots(figsize=(6,4))
ax1.plot(x, y, label='$\\beta = 6.8$')
#ax1.axhline(y=np.mean(y), color='orange', linestyle='-', linewidth=1.5)
ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.6)
ax1.text(0.02, 0.98, r'$\langle Q_L \rangle$ = {:.3f}({:.0f})'.format(np.mean(y), 1000*np.std(y)/np.sqrt(2012)), transform=ax1.transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))
ax1.set_xlabel('Trajectories', fontsize=12)
ax1.set_ylabel('$Q_L(w^2_0)$', fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.set_ylim([-1.2*np.max(np.abs(y)), 1.2*np.max(np.abs(y))])
ax1.legend(loc='lower left', fontsize=12, frameon=False)

# Load data from second file
data2 = np.loadtxt('../../data/top_charges_b68-am08.txt')
# Normalize the data for histogram
data2_norm = (data2 - np.mean(data2)) / np.std(data2)

# Create second plot
ax2 = fig.add_axes([0.65, 0.1, 0.3, 0.8])
n, bins, patches = ax2.hist(data2_norm, bins=14, range=(-3, 3), orientation='horizontal', density=True, edgecolor='black', linewidth=0.5)
for patch in patches:
    patch.set_facecolor('white')
    patch.set_edgecolor('darkblue')
    patch.set_linestyle('-')
    patch.set_linewidth(1)
ax2.tick_params(axis='both', which='major', labelsize=11)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticklabels([])
ax2.tick_params(axis='x', which='major', bottom=False, labelbottom=False)

# Fit histogram with normal distribution
mu, std = norm.fit(data2_norm)
xmin, xmax = ax2.get_xlim()
x_fit = np.linspace(xmin, xmax, 100)
p_fit = norm.pdf(x_fit, mu, std)
ax2.plot(p_fit, x_fit, 'r-', linewidth=2)

# Set y limits for the fit line
ymin, ymax = ax2.get_ylim()
y_fit = np.linspace(ymin, ymax, 100)
x_fit_range = norm.pdf(y_fit, mu, std)
ax2.plot(x_fit_range, y_fit, color='orange', linestyle='-', linewidth=2)


# Adjust subplots and show the plot
fig.subplots_adjust(left=0.10, right=0.6, bottom=0.1, top=0.9)


# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/topological_charge_b68.pdf', dpi=300, bbox_inches='tight')
