import matplotlib.pyplot as plt
x = []
y = []
ct = 1
with open("test.txt","r") as file:
    for line in file:
        for word in line.split():
            if(ct%2):
                x.append(word)
            else:
                y.append(word)
            ct += 1
plt.plot(x,y)
plt.title("Lines")
plt.xlabel("X - axis")
plt.ylabel("Y - axis")
plt.show()