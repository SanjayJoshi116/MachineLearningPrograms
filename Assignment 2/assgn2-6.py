ch = 'y'
x = 0
y = 0
z = 0
while(ch == 'y'):
    num = int(input("Enter any Integer:"))
    if(num > 0):
        print("Positive Integer")
        x += 1
    elif(num == 0):
        print("Number is Zero")
        y += 1
    else:
        print("Negative Integer")
        z += 1
    print("Do you wish to continue?")
    ch = input("Enter y to Continue:")
print("Positive Integers:",x,"Zeros:",y,"Negative Integers:",z)