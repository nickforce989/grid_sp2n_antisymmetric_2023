from pylab import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
from math import gamma

# Activating text rendering by LaTex
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.monospace": 'Computer Modern Roman',
    "lines.linewidth": 0.5,  # set thicker line width
    "lines.markersize" : '3',
    "lines.markeredgewidth" : '0.5',
    "errorbar.capsize" : '1.5',
    "axes.linewidth" : '0.5',
    "legend.fontsize" : 'small',
    "legend.handletextpad" : '0.3',
    "legend.columnspacing" : '0.5'
})

# Set the figure size
fig = plt.figure(figsize=(5, 3.5))

# Create axis object
ax = fig.add_subplot(111)


# Define the functions to fit to the histogram
def fit_func(x, N, c):
    return N * x**4 * np.exp(-c*x**2)

def fit_func2(x, N, c):
    return N * x**2 * np.exp(-c*x**2)

def fit_func3(x, N, c):
    return N * x**1 * np.exp(-c*x**2)

Nbins = 186
data = []
with open('spacings_density_2.txt', 'r') as f:
    for line in f:
        data.append(float(line.strip()))
y,x,_=hist(data,Nbins,color='blue',alpha=.4, density = True, edgecolor = "black")
erry = sqrt(y)
x=(x[1:]+x[:-1])/2 # for len(x)==len(y)

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

# Compute reduced chi square for fit_func3
yfit = fit_func3(x, *popt3)
residuals = y - yfit
if any(y == 0):
    ignore = y == 0
    chi_squared = np.sum((residuals[~ignore] / erry[~ignore]) ** 2)
else:
    chi_squared = np.sum((residuals / erry) ** 2)
dof = len(x) - len(popt3)
reduced_chi_squared = chi_squared / dof
print("Reduced Chi-Squared for fit_func3:", reduced_chi_squared)



# Plot the histogram and the fitted curves
plt.bar(x, y, width=x[1]-x[0], color='azure', alpha=.6, edgecolor='black')
plt.plot(x, fit_func(x, N, c), 'r-', linewidth=2, label='$SU(2N_f)/SO(2N_f)$')
plt.plot(x, fit_func2(x, N2, c2), 'g--', linewidth=2, label='$SU(N_f) \\times SU(N_f)/SU(N_f)$')
plt.plot(x, fit_func3(x, N3, c3), 'm-.', linewidth=2, label='$SU(2N_{\\rm as})/Sp(2N_{\\rm as})$')

plt.rcParams.update({'font.size': 9})
plt.xlim(-0.04, 3.5)
plt.ylim(0.0, 1.42)
plt.title("")
plt.xlabel("s")
plt.ylabel("P(s)")
plt.legend()

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('Dw_fund.pdf', dpi=300, bbox_inches='tight')

plt.show()
