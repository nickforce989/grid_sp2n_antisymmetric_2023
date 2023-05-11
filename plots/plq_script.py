import numpy as np
import sys

#file_name = 'output_plaquettes_m-1.4.txt'
file_name = str(sys.argv[1])
f = open(file_name, 'r')
lines = f.readlines()
f.close()

n_plq = len(lines)
plq = np.empty(n_plq, dtype=np.float64)
for i in range(n_plq):
  line = lines[i]
  plq_value = line.split(' ')[-1]
  plq[i] = plq_value

f = open(file_name.split('.')[0] + '-refined.txt', 'w')
for i in range(n_plq):
  f.write(str(plq[i]) + '\n')
f.close()
