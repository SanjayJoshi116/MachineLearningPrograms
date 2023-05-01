import numpy as np
import pandas as pd
a = [];n = int(input("Enter the no of elements:"))
for i in range(n):
    a.append(input(" "))
np_array = np.array(a)
print("NumPy Array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)