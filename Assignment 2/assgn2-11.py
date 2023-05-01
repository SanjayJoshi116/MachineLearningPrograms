str =  input("Enter a String:")
start = str[0]
end = str[-1]
str1 = end + str[1:-1] + start
print(str1)