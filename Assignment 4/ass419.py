import pandas as pd
data = pd.read_csv("emp.csv")
df = data.drop(['basic'],axis = 1)
#print(data)
print(df)