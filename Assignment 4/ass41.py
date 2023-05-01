import matplotlib.pyplot as plt
m = int(input("Enter Number of points required in X - axis:"))
x = []
print("Enter the points:")
for i in range(m):
    x.append(int(input(" ")))
n = int(input("Enter Number of points required in Y - axis:"))
y = []
print("Enter the points:")
for i in range(n):
    y.append(int(input(" ")))
plt.plot(x,y)
plt.title("Lines")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.show()