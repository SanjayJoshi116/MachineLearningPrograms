num = int(input("Enter a Positive Integer:"))
s = 0
while(num != 0):
    digit = num % 10
    s = s + digit
    num = num // 10
print(s)