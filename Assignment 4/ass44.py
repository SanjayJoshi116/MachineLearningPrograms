import matplotlib.pyplot as plt
x1 = []
y1 = []
x2 = []
y2 = [] 
m = int(input("Enter no of points for X1,Y1:"))
print("Enter",m,"points for X1 and Y1:")
for i in range(m):
    x1.append(int(input(" ")))
    y1.append(int(input(" ")))
n = int(input("Enter no of points for X2,Y2:"))
print("Enter",n,"points for X2 and Y2:")
for i in range(n):
    x2.append(int(input(" ")))
    y2.append(int(input(' ')))
plt.plot(x1, y1, label = "Line 1")
plt.plot(x2, y2, label = "Line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("Two or more lines on same plot")
plt.legend()
plt.show()
