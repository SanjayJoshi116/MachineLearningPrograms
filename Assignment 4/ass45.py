import pandas as pd
m = int(input("Enter the number of elements:"))
n = []
for i in range(m):
    n.append(int(input(" ")))
ds = pd.Series(n)
print(ds)
