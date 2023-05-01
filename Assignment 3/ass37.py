file1 = open("myfile.txt","a")
opt = "y"
while(opt == "y" or opt == "Y"):
    word = input("Enter a Word:")
    file1.write(word)
    file1.write("\n")
    opt = input("Enter choice y or n:")
file1.close()
s = input("Enter the search element:")
f = False
with open("myfile.txt","r") as file:
    for line in file:
        for word in line.split():
            if s == word:
                f = True
                print("Word Found")
if not f:
    print("Word not found")