#   reverse string


txt = "I apples,   apple apple are y favorite fruit"

x = txt.count("apple", 10, 30)

print(x)


txt = "H\te\tl\tl\to"

x =  txt.expandtabs(5)

print(x)

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "banana"

x = txt.center(20, "I")

print(x)

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

txt = "Company12"

x = txt.isalnum()

print(x)

txt = "Compan4yX"

x = txt.isalpha()

print(x)

txt = "Company123"

x = txt.isascii()

print(x)

txt = "1234"

x = txt.isdecimal()

print(x)

txt = "50800"

x = txt.isdigit()

print(x)

txt = "Demo"

x = txt.isidentifier()

print(x)

txt = "hello worWld!"

x = txt.islower()

print(x)

txt = "565543"

x = txt.isnumeric()

print(x)

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

txt = "      "

x = txt.isspace()

print(x)

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

txt = "banana"

x = txt.rjust(20)

print("what us ",x, "is my favorite fruit.")

txt = "I could eat bananas all day bananas are my favorite fruit whare are the bananas in the town."

x = txt.rpartition("bananas")

print(x)

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"

x = txt.split()

print(x)

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

txt = "Welcome to my world"

x = txt.title()

print(x)

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


txt = "50"

x = txt.zfill(10)

print(x)

txt = "Rayaprafullborkute"
txt1 = "Rborkute"
x = txt[0:7]
z = txt[-1]
y = txt[1:-1]
y1 = txt[-1:1]
z1 = txt[0:-1]
z2 = txt1[::-2]
z3 = txt1[::2]
z4 = txt1[1:-1:2]
print(x)
print(y)
print(z)
print(y1)
print(z1)
print(z2)
print(z3)
print(z4)
b=""
c=0
a="prafull"
for i in a:
    c=c+1
    b=b+(a[-c])
print(b)

for _ in range(5):
    print("prafull")


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

x="PRAFULL"
print(len(x))