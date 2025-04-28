#Klausuraufgaben Olaf, 11. Klasse Teil 2
#Testen ob Doppelvokale in einer Liste vorliegen


buch=["K","W","R","","S","e","e","l","h"]
i = 0
while (i<len(buch)-1):
    if buch[i] == buch[i+1] and buch[i] in "aeiou":
        print(buch[i])
    i+=1

