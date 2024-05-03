def f(x):
    if (x == 1):
         return 1
    else:
        return x * f(x-1)

print("Wie lautet die Zahl?")
text = input()
print(text + "! = " + str(f(int(text))))