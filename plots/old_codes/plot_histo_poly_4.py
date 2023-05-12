from pylab import *
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

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

Nbins = 100
data = []
with open('output_vol20_b9_4.txt', 'r') as f:
    for line in f:
        data.append(float(line.strip()))
y,x,_=hist(data,Nbins,color='blue',alpha=.4, density = True, edgecolor = "black")
erry = sqrt(y)
x=(x[1:]+x[:-1])/2 # for len(x)==len(y)

plt.rcParams.update({'font.size': 24})
#plt.xlim(-0.04, 0.04)

title("$\\tilde{V} = (20a)^4$", fontsize=9)
xlabel("Polyakov loop", fontsize=9)
ylabel("Frequency", fontsize=9)

# Save the figure in PDF format with dpi=300 and specified size
plt.savefig('Polyloops_vol20.pdf', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
