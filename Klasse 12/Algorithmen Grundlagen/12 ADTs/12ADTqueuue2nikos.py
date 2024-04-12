import operations_lv1 as op

einlesen = [
    ("Hans", 1), ("Franz", 2), ("Peter", 2), ("Wiola", 2), ("Lola",1), ("Adrian",2)
]
menu1 = []
menu2 = []

#print(op.getHead(einlesen))

def checkMenu(person: tuple):
    if person[1] == 1:
        return 1
    else:
        return 2
for i in range(len(einlesen)):
    if checkMenu(op.getHead(einlesen)) == 1:
        op.enQueue(menu1, op.getHead(einlesen))
        op.deQueue(einlesen)
    else:  
        op.enQueue(menu2, op.getHead(einlesen))
        op.deQueue(einlesen)

print(menu1)
print(menu2)