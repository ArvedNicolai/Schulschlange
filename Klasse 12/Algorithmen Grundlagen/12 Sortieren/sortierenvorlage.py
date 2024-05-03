import random

laenge = int(input("Wie viele Elemente soll ich erzeugen?"))
zuSortieren = [0]*laenge
print("Aktuelle Belegung: ", zuSortieren)

for zeichen in range(len(zuSortieren)):
    zuSortieren[zeichen] = int(random.randint(1,laenge+1))

print("Aktuelle Belegung: ", zuSortieren)

