def top():
    return len(stack)

stack = []

#push
#legt den Wert oben auf den Stapel
stack.append(3)
stack.append(4)
stack.append(5)


print (stack)

#top
#gibt erstes Elements des stacks zurück
print (stack[top()-1])

#pop
#oberstes Element des Stapels entfernen
stack.pop()
print (stack)

#isEmpty
#gibt an, ob Stack leer ist
if (len(stack) == 0):
    print ("Stack ist leer")

