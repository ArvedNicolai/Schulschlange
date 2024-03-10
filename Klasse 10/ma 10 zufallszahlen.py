import math
x = 0
z = float(input("Gib eine Zahl zwischen 0 und 1 ein. "))

while x < 10:
    z = z + math.pi
    z = z * z 
    z = z * z
    z = z * z
    z = z % 1
    print (z)
    x += 1