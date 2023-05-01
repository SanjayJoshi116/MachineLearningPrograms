import numpy as np
a = []
for i in range(3):
    tmp = []
    print("Enter 2 Numbers:")
    for j in range(2):
        tmp.append(int(input(" ")))
    a.append(tmp)
b = np.var(a)
print("Original Matrix:")
for i in a:
    print(i)
print("Variance:",b)