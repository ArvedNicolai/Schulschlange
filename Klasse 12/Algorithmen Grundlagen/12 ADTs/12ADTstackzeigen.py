stack = []

#Push-Operation
stack.append(3)
stack.append(4)
stack.append(5)

#Top
print(stack[len(stack)-1])

#Pop
if (len(stack) == 0):
    print("Leer")
else:
    stack.pop()

print(stack)


