n1  = int(input("Number of elements in Set 1:"))
l1 = []
l2 = []
for i in range(n1):
    num = int(input("Enter a Number:"))
    l1.append(num)
n2 = int(input("Number of elements in Set 2:"))
for i in range(n2):
    num = int(input("Enter a Number:"))
    l2.append(num)
set1 = set(l1)
set2 = set(l2)
issubset = set2.issubset(set1)
if issubset:
    print("2nd set is the subset of 1st set")
else:
    print("2nd set is not subset of the 1st set")