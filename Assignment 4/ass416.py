import pandas as pd
data = pd.read_csv("emp.csv")
#print(data)
print(data[data['basic']>2000])