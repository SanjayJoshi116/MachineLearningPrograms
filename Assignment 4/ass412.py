import numpy as np
array = []
#n = int(input("Enter the no of elements:"))
for i in range(10): 
    array.append(int(input(" ")))
r1 = np.mean(array)
print("\nMean: ", r1)
r2 = np.std(array)
print("\nStandard Deviation: ", r2)
