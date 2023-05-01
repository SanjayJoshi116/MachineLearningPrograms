n = int(input("Enter a Number:"))
s1 = 0
s2 = 1
s3 = 0
t = 0
while(t != n):
    s3 = s1 + s2
    s1 = s2
    s2 = s3
    print(s3)
    t += 1