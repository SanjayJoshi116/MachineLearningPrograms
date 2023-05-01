import numpy as np
from numpy import random
a = []
m = random.randint(5)
n = random.randint(5)
for i in range(m):
    tmp = []
    print("Enter a Matrix:")
    for j in range(n):
        tmp.append(int(input(" ")))
    a.append(tmp)
shp = np.shape(a)
print("Shape of the Matrix:",shp)