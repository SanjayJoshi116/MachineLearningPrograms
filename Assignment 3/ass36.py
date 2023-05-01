import numpy as np
a = []
for i in range(3):
    tmp = []
    print("Enter 3 Numbers:")
    for j in range(3):
        tmp.append(int(input(" ")))
    a.append(tmp)
b = [[25,25,25],
             [25,25,25],
             [25,25,25]]
print("Menu\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
c = int(input("Enter your choice:"))
m = np.array(a)
n = np.array(b)
print("First Matrix:\n", m, "\nSecond Matrix:\n", n)
if(c == 1):
    s = np.add(m,n);
    print("Sum:\n",s)
elif(c == 2):
    diff = np.subtract(m,n);
    print("Difference: \n",diff)
elif(c == 3):
    prod = np.multiply(m,n)
    print("Product: \n",prod)
elif(c == 4):
    d = np.divide(m,n)
    print("Division: \n",d)