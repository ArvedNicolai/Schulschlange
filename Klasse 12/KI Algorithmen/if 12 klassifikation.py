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
    for i in daten:
        sum = 0

        ndaten = (i[0]-min_value_echt)/(max_value_echt-min_value_echt)
        nbeispiel = (beispiel[0]-min_value_echt)/(max_value_echt-min_value_echt)
        quadrat = abs((ndaten-nbeispiel)*(ndaten-nbeispiel))
        #quadrat = abs((i[0] - beispiel[0])*(i[0] - beispiel[0]))
        #ich glaube Thore hat alle Daten normalisiert.
        sum = sum + quadrat
        quadrat = abs((i[1] - beispiel[1])*(i[1] - beispiel[1]))
        sum = sum + quadrat
        quadrat = abs((i[2] - beispiel[2])*(i[2] - beispiel[2]))
        sum = sum + quadrat
        quadrat = abs((i[3] - beispiel[3])*(i[3] - beispiel[3]))
        sum = sum + quadrat
        ergebnis = math.sqrt(sum)
        #man könnte die Ergebnisse noch in eine Liste schreiben
        distanzliste.append([ergebnis,i[4]])
        #print(ergebnis,i[4])
    
    distanzliste.sort()
    print(distanzliste)
    
beispiel = [26,1,0,1]

euklidische_distanz(beispiel)

