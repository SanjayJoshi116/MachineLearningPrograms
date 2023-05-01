s = input("Enter the search sentence:")
f = False
with open("greet.txt","r") as file:
    for line in file:
        if s in line:
            f = True          
            print("Sentence Found")
if not f:
    print("Sentence not found")