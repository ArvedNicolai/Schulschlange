import math
#import numpy as np

def euklidische_distanz(beispiel):

    daten = [[59,1,1,1,"h"],
                 [55,1,0,0,"g"],
                 [40,0,0,0,"g"],
                 [37,1,1,1,"h"],
                 [26,0,0,0,"g"],
                 [24,1,0,0,"m"],
                 [22,1,1,1,"m"],
                 [53,0,1,0,"h"]]
    distanzliste = []
    
    #Kommentare klammern die Normalisierung des Alters aus.
    max_value = max(daten)
    max_value_echt = max_value[0]
    #print(max_value_echt)

    min_value = min(daten)
    min_value_echt = min_value[0]
    #print(min_value_echt)

    # ( vi - wi )^2
    for i in range(len(daten)):
        sum = 0
        sum = (norm(daten[i][0])- norm(beispiel[0]))**2+(daten[i][1]-beispiel[1])**2+(daten[i][2]-beispiel[2])**2+(daten[i][3]-beispiel[3])**2
        #for j in range(len(daten[i])-1):
        #    quadrat = abs((norm(daten[i][j]) - norm(beispiel[j]))*(norm(daten[i][j]) - norm(beispiel[j])))
        #    sum = sum + quadrat
        
        ergebnis = math.sqrt(sum)
        #man könnte die Ergebnisse noch in eine Liste schreiben
        distanzliste.append([ergebnis,daten[i][4]])

    #distanzliste.sort()
    print(distanzliste)

def norm(z):
    z = (z-22)/37
    return z


beispiel = [26,1,0,1]

euklidische_distanz(beispiel)

