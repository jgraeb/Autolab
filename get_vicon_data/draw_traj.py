import numpy as np
import matplotlib.pyplot as plt
from IPython.core.debugger import Pdb

ipdb = Pdb()

# read the values from the datafile
data = []
with open('nodes/dataFile.txt') as f:
	for line in f:
		data.append(line.split(' '))

data = np.array(data)
#ipdb.set_trace()
for j in range(0,2):
    for i in range(len(data)):
        if j == 0 or j == 1:
            data[i,j] = float(data[i,j])
        else:
            data[i,j] = float(data[i,j][0:-2])

#ipdb.set_trace()
print(data)
x = data[:,0]
y=data[:,1]
# plot the path
plt.plot(x,y)
plt.grid()
plt.show()
