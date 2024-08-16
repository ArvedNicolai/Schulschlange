import random
from time import process_time
from turtle import right
from binarytree import create_node, insert_node, in_order_traversal, binary_search

Schuelerlist=[]
zeiten = []
i = 0

while (i<=10000):
    zahl = random.randint(0,10000)
    Schuelerlist.append(zahl)
    i += 1

# Erstellen des Binärbaums und Einfügen der Zufallszahlen
binary_tree = None
for number in Schuelerlist:
    binary_tree = insert_node(binary_tree, number)

# Ausgabe des Binärbaums in geordneter Weise (In-Order-Traversal)
'''
sorted_numbers = []
in_order_traversal(binary_tree, sorted_numbers)
print("In-Order Traversal des Binärbaums:", sorted_numbers)
'''

zeiten = []

for j in range(10):
    t1 = process_time()

    for i in range(10000):
        binary_search(binary_tree,random.choice(Schuelerlist))

    t2=process_time()
    t = t2-t1
    print("Laufzeit: ", t)
    zeiten.append(t)

print("Durchschnittszeit: ", sum(zeiten)/len(zeiten))

