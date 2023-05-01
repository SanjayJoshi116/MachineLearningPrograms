import pandas as pd
data = pd.read_csv("emp.csv")
nam = input("Enter a Name:")
df = data.replace("Sam",nam)
print(df)