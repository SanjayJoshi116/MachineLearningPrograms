import pandas as pd
a = []
print("Enter 15 digits:\n")
for i in range(15):
    a.append(int(input(" ")))
ser = pd.Series(a)
print("Unique Values:\n",ser.value_counts())
