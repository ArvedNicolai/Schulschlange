import random
from time import *

def zahlsuchen(zahl):
    for element in Schuelerlist:
        if (zahl==element):
            return #print("Zahl gefunden")

Schuelerlist=[]
zeiten = []
i = 0

while (i<=10000):
    zahl = random.randint(0,10000)
    Schuelerlist.append(zahl)
    i += 1


for j in range(10):
    t1 = process_time()

    for i in range(10000):
        zahlsuchen(random.choice(Schuelerlist))

    t2 = process_time()
    t = t2 - t1 
    zeiten.append(t)
    print("Rechenzeit: ", t)

print("Durchschnittszeit: ", sum(zeiten)/len(zeiten))




