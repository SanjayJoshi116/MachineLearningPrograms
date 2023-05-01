import pandas as pd
d1 = {}
empno = int(input("Enter EmpNo:"))
ename = input("Enter EName:")
basic = int(input("Enter Basic Salary:"))
d1["empno"] = empno
d1["ename"] = ename
d1["basic"] = basic
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)
