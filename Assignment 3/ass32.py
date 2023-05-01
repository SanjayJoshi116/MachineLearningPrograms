dict = {}
eno = int(input("Enter ENo:"))
ename = input("Enter EName:")
sal = int(input("Enter the Basic Salary:"))
dict["eno"] = eno
dict["ename"] = ename
dict["sal"] = sal
dict["da"] = round(sal * 0.05)
dict["hra"] = round(sal * 0.07)
dict["net"] = dict["sal"] + dict["da"] + dict["hra"]
print("ENo:",dict["eno"],"\nEName:",dict["ename"],"\nBasic Salary:",dict["sal"])
print("DA:",dict["da"],"HRA:",dict["hra"],"Net Salary:",dict["net"])
print(dict.keys())
print(dict.values())