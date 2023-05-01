import numpy.linalg as np
a = []
for i in range(3):
    tmp = []
    print("Enter a Matrix:")
    for j in range(3):
        tmp.append(int(input(" ")))
    a.append(tmp)
eig = np.eigvals(a)
print("Eigan Values:",eig)