import numpy as np
import matplotlib.pyplot as plt
import sys

data = []

file = open(sys.argv[1], "r")

for i in range(10000):
    data.append( int(file.readline())/1000000)

data = np.array(data)

for i in range(9999):

    data[i] = data[i+1] - data[i]

data[9999] = 0

nums = np.arange(10000)

plt.scatter(nums, data)
plt.show()