import random
import numpy as np

# Liste mit 26 Namen
names = [
    "Anna", "Ben", "Clara", "David", "Eva", "Felix", "Gina", "Hugo", "Isabel",
    "Jonas", "Klara", "Liam", "Mara", "Nina", "Oscar", "Paula", "Quentin", "Rita",
    "Sam", "Tina", "Uwe", "Vera", "Willy", "Xenia", "Yvonne", "Zach"
]

# Sicherstellen, dass die Liste genau 26 Namen enthält
assert len(names) == 26, "Die Liste muss genau 26 Namen enthalten."

# Die Namen zufällig mischen
random.shuffle(names)

# Eine leere 3x9-Matrix erstellen
matrix = np.full((3, 9), "", dtype=object)

# Die Namen in die Matrix einfügen
name_idx = 0
for i in range(3):
    for j in range(9):
        if name_idx < len(names):
            matrix[i, j] = names[name_idx]
            name_idx += 1

# Matrix ausgeben
print(matrix)