import pandas as pd
m = int(input("Enter the number of elements:"))
a = []
b = []
print("Enter the elements of first series:")
for i in range(m):
    a.append(int(input(" ")))
print("Enter the elements of second series:")
for i in range(m):
    b.append(int(input(" ")))
ds1 = pd.Series(a)
ds2 = pd.Series(b)
print("Series1:\n",ds1)
print("Series2:\n",ds2)
print("Comparision:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)
