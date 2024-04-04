def histogramm(liste):
    for i in range(10):
        anzahl = liste.count(i)
        #print (anzahl)
        print (i, " : ", anzahl, " | ", anzahl*"x")

zahl = str(input("Notiere deine Zahlen:"))
liste = []
for zeichen in zahl:
    liste.append(int(zeichen))
print (liste)
histogramm(liste)
