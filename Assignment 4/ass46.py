import pandas as pd
m = []
n = int(input("Enter the number of elements:"))
for i in range(n):
    m.append(input(" "))
s = pd.Series(m)
print("Pandas Series and Type:")
print(s)
print(type(s))
print("Pandas Series to Python List:")
print(s.tolist())
print(type(s.tolist()))
