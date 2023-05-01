import pandas as pd
a = []
print("Enter the elements:")
for i in range(10):
    a.append(int(input(" ")))
s = pd.Series(a)
#print("Original Data Series:")
#print(s)
print("Mean of the Series:",s.mean())
print("Standard deviation of the Series:\n",s.std())