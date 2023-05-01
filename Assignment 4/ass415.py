import pandas as pd
df = pd.read_csv('emp.csv')
print(df[['ename','basic']])