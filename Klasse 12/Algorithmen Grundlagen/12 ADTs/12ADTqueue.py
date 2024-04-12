#Enqueue
def enqueue(x):
    return schlange.insert(0,x)
#Dequeue
def dequeue():
    return schlange.pop()
#GetHead
def getHead():
    return schlange[len(schlange)]
#IsEmpty
def isEmpty():
    if len(schlange)==0:
        return ("Schlange ist leer.")
    else:
        return ("Schlange ist nicht leer.")



schlange = ["Hans", "Franz", "Peter", "Wiola", "Lola"]
enqueue("Robert")
dequeue()
print(schlange)
print (getHead())
print (isEmpty())



