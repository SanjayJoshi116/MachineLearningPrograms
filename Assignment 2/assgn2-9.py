str = input("Enter the String:")
str = str.lower()
n = len(str)
t = 0
vowels = 0
cons = 0
while(t != n):
    ch = str[t]
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        vowels += 1
    else:
        cons += 1
    t += 1
print("Vowels:",vowels)
print("Consonants:",cons)