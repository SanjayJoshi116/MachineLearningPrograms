dict = {}
with open('document.txt','r') as file:
    for line in file:
        for word in line.split():
            if(dict.get(word)):
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
max = 0
maxword = None
min = 0
minword = None
for key,value in dict.items():
    if(value == 1):
        min = 1
        minword = key
    if(value > max):
        max = value
        maxword = key
print("Max Word:", maxword, "\nMax Count:", max)
print("Min Word:", minword, "\nMin Count:", min)