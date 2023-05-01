str = """Hello, How are you?,
         Where are you from?,
         I'm fine.,
         I 'm from Dharmasthala,
         I'm the. Thank You."""

a  = str.upper()
print(a)

b = str.lower()
print(b)

c = len(str)
print(c)

d = str.startswith("Hello")
print(d)

e = str.endswith("lo")
print(e)

if(str.find("the") == -1):
    print("Not Found")
else:
    print("Found")

g = str.count("the")
print(g)

h = str[5:10]
print(h)

i = str[0:len(str)-1]
print(i)

j = str.replace("the","good")
print(j)