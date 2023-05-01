import numpy as np
x = []
for i in range(3):
    tmp = []
    print("Enter 3 No.s:")
    for j in range(3):
        tmp.append(int(input(" ")))
    x.append(tmp)
y = np.array(x)
print("Original Matrix:")
for i in x:
    print(i)
print("\nTranspose:")
print(y.T)