import matplotlib.pyplot as plt
op = [774.25,776.030029,779.309998,779,779.659973]
high = [776.065002,778.710022,782.070007,780.47998,779.659973]
low = [769.5,772.890015,775.650024,775.539978,770.75]
close = [772.559998,776.429993,776.469971,776.859985,775.080017]
dt = [0,1,2,3,4]
labels = ["10-03-16","10-04-16","10-05-16","10-06-16","10-07-16"]
plt.plot(op, label = "Open")
plt.plot(high, label = "High")
plt.plot(low, label = "Low")
plt.plot(close, label = "Close")
plt.title("Line Chart")
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.xticks(dt,labels)
plt.legend()
plt.show()