a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

temp = a
if b > temp:
    temp = b
if c > temp:
    temp = c
print("Największa jest %d" % temp)
