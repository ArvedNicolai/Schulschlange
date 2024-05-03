import random

laenge = int(input("Wie viele Elemente soll ich erzeugen?"))
zuSortieren = [0]*laenge
print("Aktuelle Belegung: ", zuSortieren)

for zeichen in range(len(zuSortieren)):
    zuSortieren[zeichen] = int(random.randint(1,laenge+1))

print("Aktuelle Belegung: ", zuSortieren)

#unvollständiger Sortieralgorithmus
i = 0
for element in zuSortieren:
    if (zuSortieren[i] > zuSortieren[i+1]):
        hilf = zuSortieren[i]
        zuSortieren[i] = zuSortieren[i+1]
        zuSortieren[i+1] = hilf