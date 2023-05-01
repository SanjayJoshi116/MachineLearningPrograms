lst = []
s = 0
for i in range(10):
    num = int(input("Enter a Number:"))
    s += num
    lst.append(num)
lst.sort()
min = lst[0]
max = lst[len(lst)-1]
print("Sum:",s,"\nMinimum:",min,"\nMaximum:",max)