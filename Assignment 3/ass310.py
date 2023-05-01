import numpy as np
import numpy.matlib
a = []
for i in range(3):
    tmp = []
    print("Enter 2 Numbers for 1st Matrix:")
    for j in range(2):
        tmp.append(int(input(" ")))
    a.append(tmp)
b = np.matlib.identity(2)
print("Original Matrix:")
for i in a:
    print(i)
print("Identity Matrix:")
for i in b:
    print(i)
print("Dot Product:\n",np.dot(a,b))