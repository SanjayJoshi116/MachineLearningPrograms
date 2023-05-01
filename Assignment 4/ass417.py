import pandas as pd
data = pd.read_csv("emp.csv")
print(data[data['basic'].isnull()])