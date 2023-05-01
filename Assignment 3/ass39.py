import numpy as np
a = []
for i in range(3):
    tmp = []
    print("Enter 2 Numbers for 1st Matrix:")
    for j in range(2):
        tmp.append(int(input(" ")))
    a.append(tmp)
b = []
for i in range(2):
    tmp1 = []
    print("Enter 3 Numbers for 2nd Matrix:")
    for j in range(3):
        tmp1.append(int(input(" ")))
    b.append(tmp1) 
print("Dot Product: \n",np.dot(a,b))