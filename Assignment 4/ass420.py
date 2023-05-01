import pandas as pd
data = pd.read_csv("emp.csv")
commission = data['basic'] * 0.02
data['commission'] = commission
print(data)
data.to_csv('newfile.csv')