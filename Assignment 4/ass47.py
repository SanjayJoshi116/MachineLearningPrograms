import pandas as pd
m = int(input("Enter the number of elements:"))
a = []
b = []
print("Enter the elements for first series:")
for i in range(m):
    a.append(int(input(" ")))
print("Enter the elements for second series:")
for i in range(m): 
    b.append(int(input(" ")))
ds1 = pd.Series(a)
ds2 = pd.Series(b)
ds = ds1 + ds2
print("Addition:\n",ds)
ds = ds1 - ds2
print("Subtraction:")
print(ds)
print("Multiplication:")
ds = ds1 * ds2
print(ds)
print("Division:")
ds = ds1 / ds2
print(ds)
