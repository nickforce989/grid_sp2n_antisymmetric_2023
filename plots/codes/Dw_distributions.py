from pylab import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
from math import gamma

# Activating text rendering by LaTeX
plt.style.use("paperdraft.mplstyle")

# Create a new figure with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.5))

# Define the functions to fit to the histogram
def fit_func(x, N, c):
    return N * x**4 * np.exp(-c*x**2)

def fit_func2(x, N, c):
    return N * x**2 * np.exp(-c*x**2)

def fit_func3(x, N, c):
    return N * x**1 * np.exp(-c*x**2)


# Read the first file and plot it in the corresponding axis
file = '../../data/spacings_density_2.txt'
with open(file, 'r') as f:
    data = [float(line.strip()) for line in f]
# Plot the data in the corresponding axis
col = 0
ax = axs[col]
Nbins = 186
y, x, _ = ax.hist(data, Nbins, color='blue', alpha=.3, density=True, edgecolor="black")
erry = np.sqrt(y)
x = (x[1:] + x[:-1]) / 2  # for len(x)==len(y)
ax.set_xlabel("", fontsize=9)
ax.set_ylabel("", fontsize=9)
ax.set_xlim(-0.04, 3.5)
ax.set_xticks(np.arange(0.00, 3.51, 0.5))
ax.set_ylim(0.0, 1.42)

# Define the parameters for each function
N = 2 * (gamma(2+1)**5) / (gamma(5/2)**6)
c = (gamma(2+1)**2) / (gamma(5/2)**2)

N2 = 2 * (gamma(1+1)**3) / (gamma(3/2)**4)
c2 = (gamma(1+1)**2) / (gamma(3/2)**2)

N3 = 2 * (gamma(0.5+1)**2) / (gamma(1)**3)
c3 = (gamma(0.5+1)**2) / (gamma(1)**2)

# Fit each function to the histogram data
popt, pcov = curve_fit(fit_func, x, y, p0=[N, c])
popt2, pcov2 = curve_fit(fit_func2, x, y, p0=[N2, c2])
popt3, pcov3 = curve_fit(fit_func3, x, y, p0=[N3, c3])

ax.plot(x, fit_func(x, N, c), 'r-', linewidth=2, label='$SU(2N_f)/SO(2N_f)$')
ax.plot(x, fit_func2(x, N2, c2), 'g--', linewidth=2, label='$SU(N_f) \\times SU(N_f)/SU(N_f)$')
ax.plot(x, fit_func3(x, N3, c3), 'm-.', linewidth=2, label='$SU(2N_{\\rm as})/Sp(2N_{\\rm as})$')


# Read the second file and plot it in the corresponding axis
file = '../../data/spacings_density_2as.txt'
with open(file, 'r') as f:
    data = [float(line.strip()) for line in f]
# Plot the data in the corresponding axis
col = 1
ax = axs[col]
Nbins = 93
y, x, _ = ax.hist(data, Nbins, color='blue', alpha=.3, density=True, edgecolor="black")
erry = np.sqrt(y)
x = (x[1:] + x[:-1]) / 2  # for len(x)==len(y)
ax.set_xlabel("", fontsize=9)
ax.set_ylabel("", fontsize=9)
ax.set_xlim(-0.04, 3.5)
ax.set_xticks(np.arange(0.00, 3.51, 0.5))
ax.set_ylim(0.0, 1.42)
ax.set_yticklabels('')

# Fit each function to the histogram data
popt, pcov = curve_fit(fit_func, x, y, p0=[N, c])
popt2, pcov2 = curve_fit(fit_func2, x, y, p0=[N2, c2])
popt3, pcov3 = curve_fit(fit_func3, x, y, p0=[N3, c3])

ax.plot(x, fit_func(x, N, c), 'r-', linewidth=2, label='$SU(2N_f)/SO(2N_f)$')
ax.plot(x, fit_func2(x, N2, c2), 'g--', linewidth=2, label='$SU(N_f) \\times SU(N_f)/SU(N_f)$')
ax.plot(x, fit_func3(x, N3, c3), 'm-.', linewidth=2, label='$SU(2N_{\\rm as})/Sp(2N_{\\rm as})$')
ax.legend()

# Set the x and y labels for the plot
fig.text(0.5, 0.00, '$s$', ha='center', fontsize=9)
fig.text(0.06, 0.5, '$P(s)$', va='center', rotation='vertical', fontsize=9)

# Adjust the spacing between the subplots
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('../figures/Dw_merged.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
