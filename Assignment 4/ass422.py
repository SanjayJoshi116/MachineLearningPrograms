import pandas as pd
data = pd.read_csv('emp.csv')
df = data['basic']<2000
for i,j in data.iterrows():
   if(df == True):
       data.drop(['eno'],['ename'],['department'],axis=1)
   print(i,j)
   print()