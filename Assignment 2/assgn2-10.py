str = input("Enter the String:")
n = len(str)
t = 0
up = 0
low = 0
dig = 0
while(t != n):
    ch = str[t]
    if(ch >= 'A' and ch <= 'Z'):
        up += 1
    elif(ch >= 'a' and ch <= 'z'):
        low += 1
    elif(ch >= '0' and ch <= '9'):
        dig += 1
    else:
        s += 1
    t += 1
print("Uppercase:",up)
print("Lowercase:",low)
print("Digits:",dig)