#Enqueue
def enqueue(name, x):
    return name.insert(0,x)

schlange = [["Hans",1],["Franz",2],["Peter",2],["Wiola",2],["Lola",1],["Adrian",3]]
essen1 = []
essen2 = []
print(schlange[1])
print(schlange)

#Damit das FIFO-Prinzip angewendet wird, muss die Queue von rechts nach links durchlaufen werden
j = int(len(schlange)-1)

while (j>0):
    for elemente in schlange:
        if (schlange[j][1] == 1):
            enqueue(essen1, schlange[j][0])
        elif (schlange[j][1] == 2):
            enqueue(essen2, schlange[j][0])
        else:
            print(schlange[j][0], "hat heute kein Essen.")
        j-=1

print(essen1)
print(essen2)



